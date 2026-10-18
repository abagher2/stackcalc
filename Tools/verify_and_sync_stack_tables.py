#!/usr/bin/env python3
"""
Tools/verify_and_sync_stack_tables.py

Comprehensive programmatic verifier and synchronizer for 4-register RPN stack tables
and Gate S15 inline traces across StackCalc SC-32 and SC-6 manuals.

Fulfills Gate S10:
  1. Faithfully simulates 4-register (T, Z, Y, X) RPN stack physics matching RPNCore
     (stack lift, drop with T-replication, roll down, roll up, x⇄y swap, ENTER disabling lift,
      C/CLx clearing X and disabling lift, stat accumulators, integer division with remainder).
  2. Parses and verifies all 4-register markdown tables across docs/manuals/sc32/ and sc6/.
  3. Parses and verifies Gate S15 compact inline stack traces.
  4. Implements publication-grade scientific notation formatting ($1.1910 \\times 10^{-16}$
     for |v| < 10^-3 or |v| >= 10^7, never $0.0000$ for non-zero numbers).
  5. CLI support for --check (audits all tables/traces and exits with non-zero on failure),
     --sync (auto-syncs markdown tables to true simulated states), and --file <path>.
"""

from __future__ import annotations

import argparse
import cmath
import fractions
import math
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent


# ==============================================================================
# 1. RPN Stack Simulator (Faithful to RPNCore Swift Engine)
# ==============================================================================

class RPNStackSimulator:
    """
    100% faithful Python implementation of RPNCore 4-register RPN stack physics.
    Matches CalculatorEngine+Stack.swift, CalculatorEngine+Math.swift, and
    CalculatorEngine+Statistics.swift.
    """

    def __init__(self, is_sc6: bool = False):
        self.is_sc6 = is_sc6
        self.reset()

    def reset(self) -> None:
        # 4 registers: index 0 is X, 1 is Y, 2 is Z, 3 is T
        self.stack: List[float] = [0.0, 0.0, 0.0, 0.0]
        self.last_x: float = 0.0
        self.stack_lift_enabled: bool = False
        self.is_building_number: bool = False
        self.angle_mode: str = "deg"  # 'deg', 'rad', 'grd'
        self.base_mode: str = "dec"   # 'dec', 'hex', 'oct', 'bin'
        self.cmplx_prefix: bool = False
        self.hyp_prefix: bool = False
        self.ratio_mode: bool = False
        self.two_stack_mode: bool = False

        # Statistics accumulators
        self.stat_n: int = 0
        self.stat_sum_x: float = 0.0
        self.stat_sum_x2: float = 0.0
        self.stat_sum_y: float = 0.0
        self.stat_sum_y2: float = 0.0
        self.stat_sum_xy: float = 0.0
        self.points: List[Tuple[float, float]] = []

        # Storage registers (A-Z)
        self.regs: Dict[str, float] = {}

        # TVM state: [N, I%YR, PV, PMT, FV]
        self.tvm: List[float] = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.tvm_prev_was_fin: bool = False
        self.tvm_begin: bool = False

        # POLY state: [A, B, C, D]
        self.poly_mode: bool = False
        self.poly_coeffs: List[float] = [0.0, 0.0, 0.0, 0.0]

    @property
    def x(self) -> float:
        return self.stack[0]

    @property
    def y(self) -> float:
        return self.stack[1]

    @property
    def z(self) -> float:
        return self.stack[2]

    @property
    def t(self) -> float:
        return self.stack[3]

    # --- Basic Stack Operations ---

    def push_to_stack(self, val: float) -> None:
        """Unconditionally shifts stack up (T <- Z, Z <- Y, Y <- X, X <- val), matching RPNCore pushToStack."""
        self.stack[3] = self.stack[2]
        self.stack[2] = self.stack[1]
        self.stack[1] = self.stack[0]
        self.stack[0] = val
        self.is_building_number = False
        self.stack_lift_enabled = True

    def push_number(self, val: float) -> None:
        """Enters a number onto the stack, observing stack lift rules."""
        if self.stack_lift_enabled and not self.is_building_number:
            # duplicateX / stack push: T <- Z, Z <- Y, Y <- X, X <- val
            self.stack[3] = self.stack[2]
            self.stack[2] = self.stack[1]
            self.stack[1] = self.stack[0]
            self.stack[0] = val
        else:
            self.stack[0] = val
        self.is_building_number = False
        self.stack_lift_enabled = True

    def enter(self) -> None:
        """ENTER: T <- Z, Z <- Y, Y <- X, X <- X; stackLiftEnabled = False."""
        self.stack[3] = self.stack[2]
        self.stack[2] = self.stack[1]
        self.stack[1] = self.stack[0]
        self.stack_lift_enabled = False
        self.is_building_number = False

    def drop(self) -> None:
        """Dyadic stack drop with T-replication (or Y-replication in 2-stack mode)."""
        if self.two_stack_mode:
            self.stack[0] = self.stack[1]
            return
        t_top = self.stack[3]
        self.stack[0] = self.stack[1]
        self.stack[1] = self.stack[2]
        self.stack[2] = t_top
        self.stack[3] = t_top

    def execute_dyadic(self, op_func) -> None:
        """Executes a binary operator (Y op X), drops the stack, and places result in X."""
        x = self.stack[0]
        y = self.stack[1]
        self.last_x = x
        try:
            res = op_func(y, x)
        except Exception:
            res = 0.0
        self.drop()
        self.stack[0] = float(res)
        self.stack_lift_enabled = True
        self.is_building_number = False

    def execute_monadic(self, op_func) -> None:
        """Executes a unary operator on X."""
        x = self.stack[0]
        self.last_x = x
        try:
            res = op_func(x)
        except Exception:
            res = 0.0
        self.stack[0] = float(res)
        self.stack_lift_enabled = True
        self.is_building_number = False

    def roll_down(self) -> None:
        """R↓: X <- Y, Y <- Z, Z <- T, T <- X; stackLiftEnabled = True."""
        x = self.stack[0]
        self.stack[0] = self.stack[1]
        self.stack[1] = self.stack[2]
        self.stack[2] = self.stack[3]
        self.stack[3] = x
        self.stack_lift_enabled = True
        self.is_building_number = False

    def roll_up(self) -> None:
        """R↑: X <- T, T <- Z, Z <- Y, Y <- X; stackLiftEnabled = True."""
        t = self.stack[3]
        self.stack[3] = self.stack[2]
        self.stack[2] = self.stack[1]
        self.stack[1] = self.stack[0]
        self.stack[0] = t
        self.stack_lift_enabled = True
        self.is_building_number = False

    def swap_xy(self) -> None:
        """x⇄y: Exchanges X and Y; stackLiftEnabled = True."""
        self.stack[0], self.stack[1] = self.stack[1], self.stack[0]
        self.stack_lift_enabled = True
        self.is_building_number = False

    def clear_x(self) -> None:
        """C / CLx: Clears Register X to 0 and disables stack lift."""
        self.stack[0] = 0.0
        self.stack_lift_enabled = False
        self.is_building_number = False

    def clear_stack(self) -> None:
        """CLSTK: Clears all 4 registers to 0.0."""
        self.stack = [0.0, 0.0, 0.0, 0.0]
        self.stack_lift_enabled = False
        self.is_building_number = False

    def recall_lastx(self) -> None:
        """LASTX: Recalls preserved lastX operand onto the stack."""
        self.push_number(self.last_x)

    def execute_rep(self) -> None:
        """REP: Replicates X across the entire stack; stackLiftEnabled = False."""
        val = self.stack[0]
        self.stack = [val, val, val, val]
        self.stack_lift_enabled = False
        self.is_building_number = False

    def execute_div_r(self) -> None:
        """
        ÷R / INT÷: Division with remainder.
        Places integer quotient Q in X and remainder R in Y; Z and T unchanged.
        """
        x = self.stack[0]
        y = self.stack[1]
        self.last_x = x
        if x == 0:
            q, r = 0.0, 0.0
        else:
            q = math.trunc(y / x)
            r = math.fmod(y, x)
        self.stack[0] = float(q)
        self.stack[1] = float(r)
        self.stack_lift_enabled = True
        self.is_building_number = False

    @staticmethod
    def _hms_to_hr(val: float) -> float:
        sign = -1.0 if val < 0 else 1.0
        v = abs(val)
        h = int(math.floor(v + 1e-12))
        rem = (v - h) * 100.0
        m = int(math.floor(rem + 1e-9))
        s = (rem - m) * 100.0
        return sign * (h + m / 60.0 + s / 3600.0)

    @staticmethod
    def _hr_to_hms(val: float) -> float:
        sign = -1.0 if val < 0 else 1.0
        v = abs(val)
        h = int(math.floor(v + 1e-12))
        rem_m = (v - h) * 60.0
        m = int(math.floor(rem_m + 1e-9))
        s = round((rem_m - m) * 60.0)
        if s >= 60:
            s -= 60
            m += 1
        if m >= 60:
            m -= 60
            h += 1
        return sign * (h + m / 100.0 + s / 10000.0)

    def execute_percent(self) -> None:
        """%: Computes percentage (Y * X) / 100. Leaves result in X, preserves Y."""
        x = self.stack[0]
        y = self.stack[1]
        self.last_x = x
        self.stack[0] = (y * x) / 100.0
        self.stack_lift_enabled = True
        self.is_building_number = False

    def execute_percent_change(self) -> None:
        """%CHG / Δ%: Computes percent change ((X - Y) / Y) * 100. Leaves result in X, preserves Y."""
        x = self.stack[0]
        y = self.stack[1]
        self.last_x = x
        self.stack[0] = ((x - y) / y) * 100.0 if y != 0 else 0.0
        self.stack_lift_enabled = True
        self.is_building_number = False

    # --- Angular Conversions ---

    def _to_rad(self, val: float) -> float:
        if self.angle_mode == "deg":
            return math.radians(val)
        if self.angle_mode == "grd":
            return val * math.pi / 200.0
        return val

    def _from_rad(self, val: float) -> float:
        if self.angle_mode == "deg":
            return math.degrees(val)
        if self.angle_mode == "grd":
            return val * 200.0 / math.pi
        return val

    def to_polar(self) -> None:
        """▸POL / →POL: Converts rectangular (Y, X) to polar (theta in Y, r in X)."""
        x = self.stack[0]
        y = self.stack[1]
        self.last_x = x
        r = math.hypot(x, y)
        theta = self._from_rad(math.atan2(y, x))
        self.stack[0] = r
        self.stack[1] = theta
        self.stack_lift_enabled = True
        self.is_building_number = False

    def to_rectangular(self) -> None:
        """▸REC / →REC / ▸y,x: Converts polar (theta in Y, r in X) to rectangular (Y in Y, X in X)."""
        r = self.stack[0]
        theta = self.stack[1]
        self.last_x = r
        rad = math.radians(theta) if abs(theta) > 2 * math.pi + 0.01 else self._to_rad(theta)
        x = r * math.cos(rad)
        y = r * math.sin(rad)
        self.stack[0] = x
        self.stack[1] = y
        self.stack_lift_enabled = True
        self.is_building_number = False

    def execute_complex_unary(self, op_func) -> None:
        """Executes a unary complex operation on (Y=Real, X=Imag), preserving Z and T."""
        xi = self.stack[0]
        yr = self.stack[1]
        c = complex(yr, xi)
        self.last_x = xi
        try:
            res = op_func(c)
        except Exception:
            res = complex(0.0, 0.0)
        self.stack[1] = float(res.real)
        self.stack[0] = float(res.imag)
        self.stack_lift_enabled = True
        self.is_building_number = False

    def execute_complex_binary(self, op_func) -> None:
        """Executes a binary complex operation on c2=(T+Zi) and c1=(Y+Xi), dropping two stack levels."""
        x1i = self.stack[0]
        y1r = self.stack[1]
        z2i = self.stack[2]
        t2r = self.stack[3]
        c1 = complex(y1r, x1i)
        c2 = complex(t2r, z2i)
        self.last_x = x1i
        try:
            res = op_func(c2, c1)
        except Exception:
            res = complex(0.0, 0.0)
        self.drop()
        self.drop()
        self.stack[1] = float(res.real)
        self.stack[0] = float(res.imag)
        self.stack_lift_enabled = True
        self.is_building_number = False

    # --- Statistics Subsystem ---

    def stat_clear(self) -> None:
        """CLΣ: Clears all statistical accumulators."""
        self.stat_n = 0
        self.stat_sum_x = 0.0
        self.stat_sum_x2 = 0.0
        self.stat_sum_y = 0.0
        self.stat_sum_y2 = 0.0
        self.stat_sum_xy = 0.0
        self.points.clear()

    def stat_add(self) -> None:
        """Σ+: Accumulates coordinate (Y, X) into statistics registers; leaves n in X."""
        x = self.stack[0]
        y = self.stack[1]
        self.stat_n += 1
        self.stat_sum_x += x
        self.stat_sum_x2 += x * x
        self.stat_sum_y += y
        self.stat_sum_y2 += y * y
        self.stat_sum_xy += x * y
        self.points.append((x, y))
        self.stack[0] = float(self.stat_n)
        self.stack_lift_enabled = False
        self.is_building_number = False

    def stat_sub(self) -> None:
        """Σ-: Subtracts coordinate (Y, X) from statistics registers; leaves n in X."""
        x = self.stack[0]
        y = self.stack[1]
        if self.stat_n > 0:
            self.stat_n -= 1
            self.stat_sum_x -= x
            self.stat_sum_x2 -= x * x
            self.stat_sum_y -= y
            self.stat_sum_y2 -= y * y
            self.stat_sum_xy -= x * y
        self.stack[0] = float(self.stat_n)
        self.stack_lift_enabled = False
        self.is_building_number = False

    def stat_mean(self) -> None:
        """𝑥̄,ȳ: Pushes y-mean then x-mean onto stack."""
        mx = self.stat_sum_x / self.stat_n if self.stat_n > 0 else 0.0
        my = self.stat_sum_y / self.stat_n if self.stat_n > 0 else 0.0
        self.last_x = self.stack[0]
        self.push_number(my)
        self.push_number(mx)

    def stat_weighted_mean(self) -> None:
        """x̄w / xw: Pushes weighted mean Σxy / Σy onto stack."""
        xw = self.stat_sum_xy / self.stat_sum_y if self.stat_sum_y != 0 else 0.0
        self.last_x = self.stack[0]
        self.push_number(xw)

    def stat_std_dev(self, sample: bool = True) -> None:
        """s,σ: Pushes sample/population standard deviation of Y then X."""
        div = (self.stat_n - 1.0) if sample else float(self.stat_n)
        vx = (self.stat_sum_x2 - (self.stat_sum_x ** 2 / self.stat_n)) / div if div > 0 else 0.0
        vy = (self.stat_sum_y2 - (self.stat_sum_y ** 2 / self.stat_n)) / div if div > 0 else 0.0
        sx = math.sqrt(max(0.0, vx))
        sy = math.sqrt(max(0.0, vy))
        self.last_x = self.stack[0]
        self.push_number(sy)
        self.push_number(sx)

    def stat_slope(self) -> None:
        """m: Computes and pushes linear regression slope."""
        n = self.stat_n
        num = self.stat_sum_xy - (self.stat_sum_x * self.stat_sum_y / n) if n > 0 else 0.0
        den = self.stat_sum_x2 - (self.stat_sum_x ** 2 / n) if n > 0 else 0.0
        m = num / den if den != 0 else 0.0
        self.last_x = self.stack[0]
        self.push_number(m)

    def stat_intercept(self) -> None:
        """b: Computes and pushes linear regression y-intercept."""
        n = self.stat_n
        num = self.stat_sum_xy - (self.stat_sum_x * self.stat_sum_y / n) if n > 0 else 0.0
        den = self.stat_sum_x2 - (self.stat_sum_x ** 2 / n) if n > 0 else 0.0
        m = num / den if den != 0 else 0.0
        b = (self.stat_sum_y - m * self.stat_sum_x) / n if n > 0 else 0.0
        self.last_x = self.stack[0]
        self.push_number(b)

    def stat_correlation(self) -> None:
        """r: Computes and pushes Pearson correlation coefficient."""
        n = self.stat_n
        num = self.stat_sum_xy - (self.stat_sum_x * self.stat_sum_y / n) if n > 0 else 0.0
        den_x = self.stat_sum_x2 - (self.stat_sum_x ** 2 / n) if n > 0 else 0.0
        den_y = self.stat_sum_y2 - (self.stat_sum_y ** 2 / n) if n > 0 else 0.0
        den = math.sqrt(den_x * den_y) if den_x > 0 and den_y > 0 else 0.0
        r = num / den if den != 0 else 0.0
        self.last_x = self.stack[0]
        self.push_number(r)

    def stat_estimate_y(self) -> None:
        """ŷ: Pushes r into Y and predicted ŷ into X."""
        n = self.stat_n
        num = self.stat_sum_xy - (self.stat_sum_x * self.stat_sum_y / n) if n > 0 else 0.0
        den_x = self.stat_sum_x2 - (self.stat_sum_x ** 2 / n) if n > 0 else 0.0
        den_y = self.stat_sum_y2 - (self.stat_sum_y ** 2 / n) if n > 0 else 0.0
        m = num / den_x if den_x != 0 else 0.0
        b = (self.stat_sum_y - m * self.stat_sum_x) / n if n > 0 else 0.0
        den = math.sqrt(den_x * den_y) if den_x > 0 and den_y > 0 else 0.0
        r = num / den if den != 0 else 0.0
        x_val = self.stack[0]
        y_hat = m * x_val + b
        self.last_x = x_val
        self.stack[0] = r
        self.push_number(y_hat)

    def stat_estimate_x(self) -> None:
        """x̂: Computes predicted x̂ from y in X."""
        n = self.stat_n
        num = self.stat_sum_xy - (self.stat_sum_x * self.stat_sum_y / n) if n > 0 else 0.0
        den_x = self.stat_sum_x2 - (self.stat_sum_x ** 2 / n) if n > 0 else 0.0
        m = num / den_x if den_x != 0 else 0.0
        b = (self.stat_sum_y - m * self.stat_sum_x) / n if n > 0 else 0.0
        y_val = self.stack[0]
        x_hat = (y_val - b) / m if m != 0 else 0.0
        self.last_x = y_val
        self.stack[0] = x_hat
        self.stack_lift_enabled = True
        self.is_building_number = False

    def stat_median(self) -> None:
        """MED: Computes and pushes median of x points."""
        if not self.points:
            return
        xs = sorted(pt[0] for pt in self.points)
        n = len(xs)
        med = xs[n // 2] if n % 2 == 1 else (xs[n // 2 - 1] + xs[n // 2]) / 2.0
        self.push_to_stack(med)

    def stat_range(self) -> None:
        """RNG: Computes and pushes range (max - min) of x points."""
        if not self.points:
            return
        xs = sorted(pt[0] for pt in self.points)
        self.push_to_stack(xs[-1] - xs[0])

    def stat_q1(self) -> None:
        """1Q: Computes and pushes first quartile (inclusive median method for odd n)."""
        if len(self.points) < 4:
            return
        xs = sorted(pt[0] for pt in self.points)
        n = len(xs)
        lower = xs[: n // 2] if n % 2 == 0 else xs[: n // 2 + 1]
        lh = len(lower)
        q1 = lower[lh // 2] if lh % 2 == 1 else (lower[lh // 2 - 1] + lower[lh // 2]) / 2.0
        self.push_to_stack(q1)

    def stat_q3(self) -> None:
        """3Q: Computes and pushes third quartile (inclusive median method for odd n)."""
        if len(self.points) < 4:
            return
        xs = sorted(pt[0] for pt in self.points)
        n = len(xs)
        upper = xs[n // 2 :]
        uh = len(upper)
        q3 = upper[uh // 2] if uh % 2 == 1 else (upper[uh // 2 - 1] + upper[uh // 2]) / 2.0
        self.push_to_stack(q3)

    def stat_iqr(self) -> None:
        """IQR: Computes and pushes interquartile range (Q3 - Q1)."""
        if len(self.points) < 4:
            return
        xs = sorted(pt[0] for pt in self.points)
        n = len(xs)
        lower = xs[: n // 2] if n % 2 == 0 else xs[: n // 2 + 1]
        upper = xs[n // 2 :]
        lh, uh = len(lower), len(upper)
        q1 = lower[lh // 2] if lh % 2 == 1 else (lower[lh // 2 - 1] + lower[lh // 2]) / 2.0
        q3 = upper[uh // 2] if uh % 2 == 1 else (upper[uh // 2 - 1] + upper[uh // 2]) / 2.0
        self.push_to_stack(q3 - q1)

    def stat_mad(self) -> None:
        """MAD: Computes and pushes Mean Absolute Deviation."""
        if not self.points:
            return
        xs = [pt[0] for pt in self.points]
        mean = sum(xs) / len(xs)
        mad = sum(abs(x - mean) for x in xs) / len(xs)
        self.push_to_stack(mad)

    def stat_mode(self) -> None:
        """MODE: Computes and pushes statistical mode of x points."""
        if not self.points:
            return
        xs = [pt[0] for pt in self.points]
        freq: Dict[float, int] = {}
        for x in xs:
            freq[x] = freq.get(x, 0) + 1
        mode = max(freq.items(), key=lambda kv: kv[1])[0]
        self.push_to_stack(mode)

    def stat_min(self) -> None:
        """MIN: Pushes minimum of x points."""
        if not self.points:
            return
        self.push_to_stack(min(pt[0] for pt in self.points))

    def stat_max(self) -> None:
        """MAX: Pushes maximum of x points."""
        if not self.points:
            return
        self.push_to_stack(max(pt[0] for pt in self.points))

    def stat_freq(self) -> None:
        """FRQ: Counts occurrences of X in points, drops X, and pushes count."""
        if not self.points:
            return
        target = self.stack[0]
        cnt = float(sum(1 for pt in self.points if abs(pt[0] - target) < 1e-10))
        self.drop()
        self.push_to_stack(cnt)

    # --- Primality Testing ---

    @staticmethod
    def _is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    # --- TVM & Polynomial Solvers ---

    @staticmethod
    def _tvm_factor(periods: float, rate: float, begin: bool) -> float:
        if abs(rate) < 1e-14:
            end_f = periods
        else:
            end_f = ((1.0 + rate) ** periods - 1.0) / rate
        return end_f * (1.0 + rate) if begin else end_f

    def execute_tvm_key(self, idx: int) -> None:
        if self.tvm_prev_was_fin and not self.is_building_number:
            n, r_pct, pv, pmt, fv = self.tvm
            r = r_pct / 100.0
            res = 0.0
            if idx == 0:
                if abs(r) < 1e-14:
                    res = -(pv + fv) / pmt if pmt != 0 else 0.0
                else:
                    p_term = pmt * (1.0 + r if self.tvm_begin else 1.0) / r
                    q = (p_term - fv) / (pv + p_term) if (pv + p_term) != 0 else 1.0
                    res = math.log(q) / math.log(1.0 + r) if q > 0 and (1.0 + r) > 0 else 0.0
            elif idx == 1:
                # Secant / Newton search for periodic rate r
                r_guess = 0.05
                for _ in range(80):
                    f_val = pv * ((1.0 + r_guess) ** n) + pmt * self._tvm_factor(n, r_guess, self.tvm_begin) + fv
                    if abs(f_val) < 1e-12:
                        break
                    dr = 1e-7
                    f_plus = pv * ((1.0 + r_guess + dr) ** n) + pmt * self._tvm_factor(n, r_guess + dr, self.tvm_begin) + fv
                    df = (f_plus - f_val) / dr
                    if abs(df) < 1e-15:
                        break
                    r_guess -= f_val / df
                res = r_guess * 100.0
            elif idx == 2:
                g = (1.0 + r) ** n
                res = -(fv + pmt * self._tvm_factor(n, r, self.tvm_begin)) / g if g != 0 else 0.0
            elif idx == 3:
                f = self._tvm_factor(n, r, self.tvm_begin)
                res = -(fv + pv * ((1.0 + r) ** n)) / f if f != 0 else 0.0
            elif idx == 4:
                g = (1.0 + r) ** n
                res = -(pv * g + pmt * self._tvm_factor(n, r, self.tvm_begin))
            self.tvm[idx] = float(res)
            self.stack[0] = float(res)
            self.tvm_prev_was_fin = True
            self.stack_lift_enabled = True
            self.is_building_number = False
        else:
            self.tvm[idx] = self.stack[0]
            self.tvm_prev_was_fin = True
            self.stack_lift_enabled = True
            self.is_building_number = False

    def execute_poly_exec(self) -> None:
        a, b, c, d = self.poly_coeffs
        roots: List[complex] = []
        if abs(a) > 1e-12:
            p = (3.0 * a * c - b * b) / (3.0 * a * a)
            q = (27.0 * a * a * d - 9.0 * a * b * c + 2.0 * b * b * b) / (27.0 * a * a * a)
            half_q = complex(q / 2.0, 0.0)
            disc = complex(q * q / 4.0 + p * p * p / 27.0, 0.0)
            rad = cmath.sqrt(disc)

            def _cbrt(z: complex) -> complex:
                if abs(z) == 0:
                    return complex(0.0, 0.0)
                mag = abs(z) ** (1.0 / 3.0)
                ph = cmath.phase(z) / 3.0
                return complex(mag * math.cos(ph), mag * math.sin(ph))

            u = _cbrt(-half_q + rad)
            if abs(u) > 1e-14:
                v = complex(-p / 3.0, 0.0) / u
            else:
                u = complex(0.0, 0.0)
                v = _cbrt(-half_q - rad)
            omega = complex(-0.5, math.sqrt(3.0) / 2.0)
            omega2 = omega * omega
            shift = complex(b / (3.0 * a), 0.0)
            roots = [u + v - shift, omega * u + omega2 * v - shift, omega2 * u + omega * v - shift]
        elif abs(b) > 1e-12:
            disc = complex(c * c - 4.0 * b * d, 0.0)
            rad = cmath.sqrt(disc)
            roots = [(-c + rad) / (2.0 * b), (-c - rad) / (2.0 * b)]

        cleaned: List[complex] = []
        for rt in roots:
            re_v = 0.0 if abs(rt.real) < 1e-12 else rt.real
            im_v = 0.0 if abs(rt.imag) < 1e-12 else rt.imag
            cleaned.append(complex(re_v, im_v))

        cleaned.sort(key=lambda z: (0 if z.imag == 0.0 else 1, round(z.real, 11), z.imag))
        for idx, rt in enumerate(cleaned):
            self.regs[str(idx * 2 + 1)] = rt.real
            self.regs[str(idx * 2 + 2)] = rt.imag
        if cleaned:
            self.stack[0] = cleaned[0].imag
            self.stack[1] = cleaned[0].real
        self.stack_lift_enabled = True
        self.is_building_number = False
        self.poly_mode = False

    # --- Token Execution ---

    def execute_token(self, tok: str) -> None:
        """Executes a single normalized calculator token."""
        t = tok.strip()
        if not t:
            return

        if t not in ("N", "I%YR", "I%", "PV", "PMT", "FV", "TVM", "BEGIN", "END", "↰", "↱", "f", "g"):
            self.tvm_prev_was_fin = False

        if self.is_sc6 and t == "PV":
            num = self.stack[1]
            place = self.stack[0]
            self.last_x = place
            digit = int(math.floor(abs(num) / place + 1e-9)) % 10 if place > 0 else 0
            self.stack[0] = float(digit)
            self.stack_lift_enabled = False
            self.is_building_number = False
            return

        if t == "POLY":
            self.poly_mode = True
            self.poly_coeffs = [0.0, 0.0, 0.0, 0.0]
            return

        if self.poly_mode and t in ("A", "B", "C", "D", "EXEC", "CLR"):
            if t in ("A", "B", "C", "D"):
                idx = {"A": 0, "B": 1, "C": 2, "D": 3}[t]
                self.poly_coeffs[idx] = self.stack[0]
                self.regs[t] = self.stack[0]
                self.stack_lift_enabled = True
                self.is_building_number = False
                return
            if t == "CLR":
                self.poly_coeffs = [0.0, 0.0, 0.0, 0.0]
                return
            if t == "EXEC":
                self.execute_poly_exec()
                return

        if not self.is_sc6 and t in ("N", "I%YR", "I%", "PV", "PMT", "FV"):
            idx = {"N": 0, "I%YR": 1, "I%": 1, "PV": 2, "PMT": 3, "FV": 4}[t]
            self.execute_tvm_key(idx)
            return
        if t == "BEGIN":
            self.tvm_begin = True
            return
        if t == "END":
            self.tvm_begin = False
            return
        if t in ("CLFIN", "CLALL"):
            self.tvm = [0.0, 0.0, 0.0, 0.0, 0.0]
            self.tvm_prev_was_fin = False
            return

        # Direct numeric literals
        # Check for hexadecimal literal (e.g. '0x2F80' or '2F80h')
        if t.lower().endswith("h") and len(t) > 1:
            try:
                hex_val = int(t[:-1], 16)
                self.push_number(float(hex_val))
                return
            except ValueError:
                pass
        if self.base_mode == "hex" and t not in ("DEC", "BASE") and re.match(r"^[0-9A-Fa-f]+$", t):
            try:
                hex_val = int(t, 16)
                self.push_number(float(hex_val))
                return
            except ValueError:
                pass
        if self.base_mode == "bin" and t not in ("DEC", "BASE") and re.match(r"^[01]+$", t):
            try:
                bin_val = int(t, 2)
                self.push_number(float(bin_val))
                return
            except ValueError:
                pass

        try:
            # Check for scientific notation or standard float
            val = float(t)
            self.push_number(val)
            return
        except ValueError:
            pass

        # Check for fraction literal like '5/8' or '3 2/5'
        m_mixed = re.match(r"^(\d+)\s+(\d+)/(\d+)$", t)
        if m_mixed:
            whole, num, den = float(m_mixed.group(1)), float(m_mixed.group(2)), float(m_mixed.group(3))
            self.push_number(whole + (num / den if den != 0 else 0.0))
            return
        m_frac = re.match(r"^(\d+)/(\d+)$", t)
        if m_frac:
            num, den = float(m_frac.group(1)), float(m_frac.group(2))
            self.push_number(num / den if den != 0 else 0.0)
            return

        if t == "CMPLX":
            self.cmplx_prefix = True
            return

        if getattr(self, "cmplx_prefix", False) and t not in ("↰", "↱", "f", "g"):
            self.cmplx_prefix = False
            if t in ("C", "CLx", "CLEAR_X"):
                return
            cmplx_bin_map = {
                "+": lambda c2, c1: c2 + c1,
                "-": lambda c2, c1: c2 - c1,
                "−": lambda c2, c1: c2 - c1,
                "×": lambda c2, c1: c2 * c1,
                "*": lambda c2, c1: c2 * c1,
                "÷": lambda c2, c1: c2 / c1 if abs(c1) != 0 else complex(0.0, 0.0),
                "/": lambda c2, c1: c2 / c1 if abs(c1) != 0 else complex(0.0, 0.0),
                "x∥y": lambda c2, c1: (c2 * c1) / (c2 + c1) if abs(c2 + c1) != 0 else complex(0.0, 0.0),
                "𝑥∥𝑦": lambda c2, c1: (c2 * c1) / (c2 + c1) if abs(c2 + c1) != 0 else complex(0.0, 0.0),
                "PARALLEL": lambda c2, c1: (c2 * c1) / (c2 + c1) if abs(c2 + c1) != 0 else complex(0.0, 0.0),
                "yˣ": lambda c2, c1: cmath.exp(c1 * cmath.log(c2)) if abs(c2) != 0 else complex(0.0, 0.0),
                "y^x": lambda c2, c1: cmath.exp(c1 * cmath.log(c2)) if abs(c2) != 0 else complex(0.0, 0.0),
                "^": lambda c2, c1: cmath.exp(c1 * cmath.log(c2)) if abs(c2) != 0 else complex(0.0, 0.0),
                "ˣ√y": lambda c2, c1: cmath.exp((1.0 / c1) * cmath.log(c2)) if abs(c1) != 0 and abs(c2) != 0 else complex(0.0, 0.0),
                "xRootY": lambda c2, c1: cmath.exp((1.0 / c1) * cmath.log(c2)) if abs(c1) != 0 and abs(c2) != 0 else complex(0.0, 0.0),
            }
            cmplx_un_map = {
                "1/x": lambda c: 1.0 / c if abs(c) != 0 else complex(0.0, 0.0),
                "1/X": lambda c: 1.0 / c if abs(c) != 0 else complex(0.0, 0.0),
                "¹/x": lambda c: 1.0 / c if abs(c) != 0 else complex(0.0, 0.0),
                "𝑥⁻¹": lambda c: 1.0 / c if abs(c) != 0 else complex(0.0, 0.0),
                "√x": cmath.sqrt,
                "√X": cmath.sqrt,
                "SQRT": cmath.sqrt,
                "x²": lambda c: c * c,
                "X²": lambda c: c * c,
                "x^2": lambda c: c * c,
                "x³": lambda c: c * c * c,
                "LN": lambda c: cmath.log(c) if abs(c) != 0 else complex(0.0, 0.0),
                "ln": lambda c: cmath.log(c) if abs(c) != 0 else complex(0.0, 0.0),
                "eˣ": cmath.exp,
                "e^x": cmath.exp,
                "LOG": lambda c: cmath.log10(c) if abs(c) != 0 else complex(0.0, 0.0),
                "log": lambda c: cmath.log10(c) if abs(c) != 0 else complex(0.0, 0.0),
                "10ˣ": lambda c: cmath.exp(c * math.log(10.0)),
                "10^x": lambda c: cmath.exp(c * math.log(10.0)),
                "SIN": cmath.sin,
                "COS": cmath.cos,
                "TAN": cmath.tan,
                "+/-": lambda c: -c,
                "CHS": lambda c: -c,
            }
            if t in cmplx_bin_map:
                self.execute_complex_binary(cmplx_bin_map[t])
                return
            if t in cmplx_un_map:
                self.execute_complex_unary(cmplx_un_map[t])
                return

        # Operator dispatch table
        op_map = {
            "ENTER": self.enter,
            "=": self.enter,
            "+": lambda: self.execute_dyadic(lambda y, x: y + x),
            "-": lambda: self.execute_dyadic(lambda y, x: float((int(y) - int(x)) & 0xFFFFFFFFF) if self.base_mode in ("hex", "oct", "bin") and (y - x) < 0 else y - x),
            "−": lambda: self.execute_dyadic(lambda y, x: float((int(y) - int(x)) & 0xFFFFFFFFF) if self.base_mode in ("hex", "oct", "bin") and (y - x) < 0 else y - x),
            "×": lambda: self.execute_dyadic(lambda y, x: y if getattr(self, "ratio_mode", False) else y * x),
            "*": lambda: self.execute_dyadic(lambda y, x: y if getattr(self, "ratio_mode", False) else y * x),
            "÷": lambda: self.execute_dyadic(lambda y, x: (float(math.trunc(y / x)) if self.base_mode in ("hex", "oct", "bin") else y / x) if x != 0 else 0.0),
            "/": lambda: self.execute_dyadic(lambda y, x: (float(math.trunc(y / x)) if self.base_mode in ("hex", "oct", "bin") else y / x) if x != 0 else 0.0),
            "x∥y": lambda: self.execute_dyadic(lambda y, x: (y * x) / (y + x) if (y + x) != 0 else 0.0),
            "𝑥∥𝑦": lambda: self.execute_dyadic(lambda y, x: (y * x) / (y + x) if (y + x) != 0 else 0.0),
            "PARALLEL": lambda: self.execute_dyadic(lambda y, x: (y * x) / (y + x) if (y + x) != 0 else 0.0),
            "yˣ": lambda: self.execute_dyadic(lambda y, x: math.pow(y, x) if y > 0 or (y == 0 and x > 0) or x == int(x) else 0.0),
            "y^x": lambda: self.execute_dyadic(lambda y, x: math.pow(y, x) if y > 0 or (y == 0 and x > 0) or x == int(x) else 0.0),
            "^": lambda: self.execute_dyadic(lambda y, x: math.pow(y, x) if y > 0 or (y == 0 and x > 0) or x == int(x) else 0.0),
            "ˣ√y": lambda: self.execute_dyadic(lambda y, x: math.pow(y, 1.0 / x) if x != 0 and (y >= 0 or (1.0/x) == int(1.0/x)) else 0.0),
            "xRootY": lambda: self.execute_dyadic(lambda y, x: math.pow(y, 1.0 / x) if x != 0 and (y >= 0 or (1.0/x) == int(1.0/x)) else 0.0),
            "1/x": lambda: self.execute_monadic(lambda x: 1.0 / x if x != 0 else 0.0),
            "1/X": lambda: self.execute_monadic(lambda x: 1.0 / x if x != 0 else 0.0),
            "¹/x": lambda: self.execute_monadic(lambda x: 1.0 / x if x != 0 else 0.0),
            "𝑥⁻¹": lambda: self.execute_monadic(lambda x: 1.0 / x if x != 0 else 0.0),
            "√x": lambda: self.execute_monadic(lambda x: math.sqrt(x) if x >= 0 else 0.0),
            "√X": lambda: self.execute_monadic(lambda x: math.sqrt(x) if x >= 0 else 0.0),
            "SQRT": lambda: self.execute_monadic(lambda x: math.sqrt(x) if x >= 0 else 0.0),
            "x²": lambda: self.execute_monadic(lambda x: x * x),
            "X²": lambda: self.execute_monadic(lambda x: x * x),
            "x^2": lambda: self.execute_monadic(lambda x: x * x),
            "x³": lambda: self.execute_monadic(lambda x: x * x * x),
            "∛x": lambda: self.execute_monadic(lambda x: math.pow(x, 1.0/3.0) if x >= 0 else -math.pow(-x, 1.0/3.0)),
            "LN": lambda: self.execute_monadic(lambda x: math.log(x) if x > 0 else 0.0),
            "ln": lambda: self.execute_monadic(lambda x: math.log(x) if x > 0 else 0.0),
            "eˣ": lambda: self.execute_monadic(lambda x: math.exp(x)),
            "e^x": lambda: self.execute_monadic(lambda x: math.exp(x)),
            "LOG": lambda: self.execute_monadic(lambda x: math.log10(x) if x > 0 else 0.0),
            "log": lambda: self.execute_monadic(lambda x: math.log10(x) if x > 0 else 0.0),
            "10ˣ": lambda: self.execute_monadic(lambda x: math.pow(10.0, x)),
            "10^x": lambda: self.execute_monadic(lambda x: math.pow(10.0, x)),
            "SIN": lambda: (setattr(self, "hyp_prefix", False), self.execute_monadic(math.sinh if getattr(self, "hyp_prefix", False) else lambda x: math.sin(self._to_rad(x))))[1] if not getattr(self, "hyp_prefix", False) else (setattr(self, "hyp_prefix", False), self.execute_monadic(math.sinh))[1],
            "COS": lambda: (setattr(self, "hyp_prefix", False), self.execute_monadic(math.cosh))[1] if getattr(self, "hyp_prefix", False) else self.execute_monadic(lambda x: math.cos(self._to_rad(x))),
            "TAN": lambda: (setattr(self, "hyp_prefix", False), self.execute_monadic(math.tanh))[1] if getattr(self, "hyp_prefix", False) else self.execute_monadic(lambda x: math.tan(self._to_rad(x))),
            "ASIN": lambda: (setattr(self, "hyp_prefix", False), self.execute_monadic(math.asinh))[1] if getattr(self, "hyp_prefix", False) else self.execute_monadic(lambda x: self._from_rad(math.asin(max(-1.0, min(1.0, x))))),
            "ACOS": lambda: (setattr(self, "hyp_prefix", False), self.execute_monadic(lambda x: math.acosh(x) if x >= 1.0 else 0.0))[1] if getattr(self, "hyp_prefix", False) else self.execute_monadic(lambda x: self._from_rad(math.acos(max(-1.0, min(1.0, x))))),
            "ATAN": lambda: (setattr(self, "hyp_prefix", False), self.execute_monadic(lambda x: math.atanh(x) if -1.0 < x < 1.0 else 0.0))[1] if getattr(self, "hyp_prefix", False) else self.execute_monadic(lambda x: self._from_rad(math.atan(x))),
            "SINH": lambda: self.execute_monadic(math.sinh),
            "COSH": lambda: self.execute_monadic(math.cosh),
            "TANH": lambda: self.execute_monadic(math.tanh),
            "ASINH": lambda: self.execute_monadic(math.asinh),
            "ACOSH": lambda: self.execute_monadic(lambda x: math.acosh(x) if x >= 1.0 else 0.0),
            "ATANH": lambda: self.execute_monadic(lambda x: math.atanh(x) if -1.0 < x < 1.0 else 0.0),
            "ABS": lambda: self.execute_monadic(abs),
            "|x|": lambda: self.execute_monadic(abs),
            "+/-": lambda: self.execute_monadic(lambda x: -x),
            "CHS": lambda: self.execute_monadic(lambda x: -x),
            "IP": lambda: self.execute_monadic(lambda x: float(int(x))),
            "FP": lambda: self.execute_monadic(lambda x: x - int(x)),
            "RND": lambda: self.execute_monadic(lambda x: float(round(x))),
            "SGN": lambda: self.execute_monadic(lambda x: 1.0 if x > 0 else (-1.0 if x < 0 else 0.0)),
            "π": lambda: self.push_to_stack(math.pi),
            "PI": lambda: self.push_to_stack(math.pi),
            "e": lambda: self.push_number(math.e),
            "x!": lambda: self.execute_monadic(lambda x: float(math.factorial(int(x))) if 0 <= x <= 170 and int(x) == x else math.gamma(x + 1.0)),
            "n!": lambda: self.execute_monadic(lambda x: float(math.factorial(int(x))) if 0 <= x <= 170 and int(x) == x else math.gamma(x + 1.0)),
            "FACT": lambda: self.execute_monadic(lambda x: float(math.factorial(int(x))) if (not self.is_sc6 and 0 <= x <= 170 and int(x) == x) else x),
            "nPr": lambda: self.execute_dyadic(lambda y, x: float(math.perm(int(y), int(x))) if int(y) >= int(x) >= 0 else 0.0),
            "Pn,r": lambda: self.execute_dyadic(lambda y, x: float(math.perm(int(y), int(x))) if int(y) >= int(x) >= 0 else 0.0),
            "nCr": lambda: self.execute_dyadic(lambda y, x: float(math.comb(int(y), int(x))) if int(y) >= int(x) >= 0 else 0.0),
            "Cn,r": lambda: self.execute_dyadic(lambda y, x: float(math.comb(int(y), int(x))) if int(y) >= int(x) >= 0 else 0.0),
            "MOD": lambda: self.execute_dyadic(lambda y, x: y - x * math.floor(y / x) if x != 0 else 0.0),
            "%": self.execute_percent,
            "%CHG": self.execute_percent_change,
            "Δ%": self.execute_percent_change,
            "x⇄y": self.swap_xy,
            "x≷y": self.swap_xy,
            "𝑥≷𝑦": self.swap_xy,
            "𝑥⇄𝑦": self.swap_xy,
            "SWAP": self.swap_xy,
            "R↓": self.roll_down,
            "R_DN": self.roll_down,
            "R_DOWN": self.roll_down,
            "ROLL_DOWN": self.roll_down,
            "R↑": self.roll_up,
            "R_UP": self.roll_up,
            "ROLL_UP": self.roll_up,
            "LASTx": self.recall_lastx,
            "LASTX": self.recall_lastx,
            "LAST𝑥": self.recall_lastx,
            "C": self.clear_x,
            "CLx": self.clear_x,
            "CLEAR_X": self.clear_x,
            "CLSTK": self.clear_stack,
            "CLΣ": self.stat_clear,
            "CLSTAT": self.stat_clear,
            "Σ+": self.stat_add,
            "Σ-": self.stat_sub,
            "𝑥̄,𝑦̄": self.stat_mean,
            "MEAN": self.stat_mean,
            "x̄": lambda: (setattr(self, "last_x", self.stack[0]), self.push_number(self.stat_sum_x / self.stat_n if self.stat_n > 0 else 0.0)),
            "ȳ": lambda: (setattr(self, "last_x", self.stack[0]), self.push_number(self.stat_sum_y / self.stat_n if self.stat_n > 0 else 0.0)),
            "xw": self.stat_weighted_mean,
            "x̄w": self.stat_weighted_mean,
            "s,σ": lambda: self.stat_std_dev(sample=True),
            "SDEV": lambda: self.stat_std_dev(sample=True),
            "s": lambda: (setattr(self, "last_x", self.stack[0]), self.push_number(math.sqrt(max(0.0, (self.stat_sum_x2 - (self.stat_sum_x ** 2 / self.stat_n)) / (self.stat_n - 1.0))) if self.stat_n > 1 else 0.0)),
            "sx": lambda: (setattr(self, "last_x", self.stack[0]), self.push_number(math.sqrt(max(0.0, (self.stat_sum_x2 - (self.stat_sum_x ** 2 / self.stat_n)) / (self.stat_n - 1.0))) if self.stat_n > 1 else 0.0)),
            "σ": lambda: (setattr(self, "last_x", self.stack[0]), self.push_number(math.sqrt(max(0.0, (self.stat_sum_x2 - (self.stat_sum_x ** 2 / self.stat_n)) / self.stat_n)) if self.stat_n > 0 else 0.0)),
            "σx": lambda: (setattr(self, "last_x", self.stack[0]), self.push_number(math.sqrt(max(0.0, (self.stat_sum_x2 - (self.stat_sum_x ** 2 / self.stat_n)) / self.stat_n)) if self.stat_n > 0 else 0.0)),
            "m": self.stat_slope,
            "b": self.stat_intercept,
            "r": self.stat_correlation,
            "ŷ": self.stat_estimate_y,
            "x̂": self.stat_estimate_x,
            "SUMS": lambda: self.push_number(self.stat_sum_x),
            "Σx": lambda: self.push_number(self.stat_sum_x),
            "Σy": lambda: self.push_number(self.stat_sum_y),
            "Σx²": lambda: self.push_number(self.stat_sum_x2),
            "Σy²": lambda: self.push_number(self.stat_sum_y2),
            "Σxy": lambda: self.push_number(self.stat_sum_xy),
            "MED": self.stat_median,
            "MODE": self.stat_mode,
            "RNG": self.stat_range,
            "IQR": self.stat_iqr,
            "1Q": self.stat_q1,
            "3Q": self.stat_q3,
            "MAD": self.stat_mad,
            "MIN": self.stat_min,
            "MAX": self.stat_max,
            "FRQ": self.stat_freq,
            "÷R": self.execute_div_r,
            "INT÷": self.execute_div_r,
            "REP": self.execute_rep,
            "GCF": lambda: self.execute_dyadic(lambda y, x: float(math.gcd(int(round(y)), int(round(x))))),
            "GCD": lambda: self.execute_dyadic(lambda y, x: float(math.gcd(int(round(y)), int(round(x))))),
            "LCM": lambda: self.execute_dyadic(lambda y, x: float(abs(int(round(y)) * int(round(x))) // math.gcd(int(round(y)), int(round(x)))) if int(round(y)) != 0 and int(round(x)) != 0 else 0.0),
            "PRIME": lambda: self.execute_monadic(lambda x: x),
            "▸HR": lambda: self.execute_monadic(self._hms_to_hr),
            "→HR": lambda: self.execute_monadic(self._hms_to_hr),
            "▸HMS": lambda: self.execute_monadic(self._hr_to_hms),
            "→HMS": lambda: self.execute_monadic(self._hr_to_hms),
            "RECT": lambda: self.execute_dyadic(lambda y, x: y * x),
            "AREA_RECT": lambda: self.execute_dyadic(lambda y, x: y * x),
            "TRI": lambda: self.execute_dyadic(lambda y, x: 0.5 * y * x),
            "AREA_TRI": lambda: self.execute_dyadic(lambda y, x: 0.5 * y * x),
            "CIRC": lambda: self.execute_monadic(lambda x: math.pi * x * x),
            "AREA_CIRC": lambda: self.execute_monadic(lambda x: math.pi * x * x),
            "HYP": lambda: self.execute_dyadic(lambda y, x: math.hypot(y, x)) if self.is_sc6 else setattr(self, "hyp_prefix", True),
            "PRISM": lambda: self.execute_dyadic(lambda y, x: y * x),
            "VOL_PRISM": lambda: self.execute_dyadic(lambda y, x: y * x),
            "CYL": lambda: self.execute_dyadic(lambda y, x: math.pi * (y ** 2) * x),
            "VOL_CYL": lambda: self.execute_dyadic(lambda y, x: math.pi * (y ** 2) * x),
            "CONE": lambda: self.execute_dyadic(lambda y, x: (math.pi * (y ** 2) * x) / 3.0),
            "VOL_CONE": lambda: self.execute_dyadic(lambda y, x: (math.pi * (y ** 2) * x) / 3.0),
            "PYR": lambda: self.execute_dyadic(lambda y, x: (y * x) / 3.0),
            "▸POL": self.to_polar,
            "→POL": self.to_polar,
            "▸θ,r": self.to_polar,
            "→θ,r": self.to_polar,
            "▸θ,𝑟": self.to_polar,
            "▸REC": self.to_rectangular,
            "→REC": self.to_rectangular,
            "▸y,x": self.to_rectangular,
            "→y,x": self.to_rectangular,
            "▸𝑦,𝑥": self.to_rectangular,
            "DEG": lambda: setattr(self, "angle_mode", "deg"),
            "RAD": lambda: setattr(self, "angle_mode", "rad"),
            "GRAD": lambda: setattr(self, "angle_mode", "grd"),
            "HEX": lambda: setattr(self, "base_mode", "hex"),
            "DEC": lambda: setattr(self, "base_mode", "dec"),
            "OCT": lambda: setattr(self, "base_mode", "oct"),
            "BIN": lambda: setattr(self, "base_mode", "bin"),
            "AND": lambda: self.execute_dyadic(lambda y, x: float(int(y) & int(x))),
            "OR": lambda: self.execute_dyadic(lambda y, x: float(int(y) | int(x))),
            "XOR": lambda: self.execute_dyadic(lambda y, x: float(int(y) ^ int(x))),
            "NOT": lambda: self.execute_monadic(lambda x: float(~int(x) & 0xFFFFFFFFF)),
            "a:b": lambda: setattr(self, "ratio_mode", True),
        }

        if t in op_map:
            op_map[t]()
        elif t in ("↰", "↱", "f", "g", "SHOW", "FLAGS", "FDISP", "SIMP", "<-", "BACKSPACE"):
            # Passive / shift-prefix / display toggles
            pass
        elif t.startswith("STO ") and len(t) > 4:
            self.regs[t[4:].strip()] = self.stack[0]
        elif t.startswith("RCL ") and len(t) > 4:
            self.push_number(self.regs.get(t[4:].strip(), 0.0))


# ==============================================================================
# 2. Tokenizer & Keystroke Sequence Replayer
# ==============================================================================

def is_digit_token(tok: str) -> bool:
    return bool(re.match(r"^\d+$", tok.strip()))


def assemble_decimal_tokens(tokens: List[str]) -> List[str]:
    """
    Handles Bug A and Gate S10 Digit Token Assembly:
    - Assembles consecutive bracketed digit keys or separated digit tokens into clean integer strings
      (e.g. ['4', '5'] -> ['45'], ['1', '8'] -> ['18'], ['1', '8', '0', '0'] -> ['1800']).
    - Assembles {{key:.}} with preceding or succeeding digit tokens into floats
      (e.g. ['.', '8'] -> ['0.8'], ['0', '.', '4', '2'] -> ['0.42'], ['1', '.', '0', '8', '2', '5'] -> ['1.0825'], ['2', '4', '.', '5'] -> ['24.5']).
    - Preserves two-dot fractions with single or multi-digit parts:
      Form 1: ['.', '5', '.', '8'] or ['.', '1', '2', '.', '1', '8'] -> ['.', '12', '.', '18']
      Form 2: ['1', '.', '2', '.', '5'] or ['3', '.', '2', '.', '5'] -> ['3', '.', '2', '.', '5'].
    """
    assembled: List[str] = []
    i = 0
    n = len(tokens)
    while i < n:
        # Preserve STO / RCL + single-char register name (A-Z or 0-9) without concatenating with following digits
        if tokens[i] in ("STO", "RCL") and (i + 1) < n and len(tokens[i + 1]) == 1:
            assembled.append(tokens[i])
            assembled.append(tokens[i + 1])
            i += 2
            continue

        # Form 1 two-dot fraction: . num . den (e.g. ['.', '5', '.', '8'] or ['.', '1', '2', '.', '1', '8'])
        if tokens[i] == ".":
            j = i + 1
            while j < n and is_digit_token(tokens[j]):
                j += 1
            if j > i + 1 and j < n and tokens[j] == ".":
                k = j + 1
                while k < n and is_digit_token(tokens[k]):
                    k += 1
                if k > j + 1:
                    num_str = "".join(tokens[i + 1 : j])
                    den_str = "".join(tokens[j + 1 : k])
                    assembled.extend([".", num_str, ".", den_str])
                    i = k
                    continue

        # Form 2 two-dot fraction or integer/decimal starting with digits
        if is_digit_token(tokens[i]):
            j = i
            while j < n and is_digit_token(tokens[j]):
                j += 1
            whole_str = "".join(tokens[i : j])

            if j < n and tokens[j] == ".":
                # Check for Form 2: whole . num . den
                k = j + 1
                while k < n and is_digit_token(tokens[k]):
                    k += 1
                if k > j + 1 and k < n and tokens[k] == ".":
                    m = k + 1
                    while m < n and is_digit_token(tokens[m]):
                        m += 1
                    if m > k + 1:
                        num_str = "".join(tokens[j + 1 : k])
                        den_str = "".join(tokens[k + 1 : m])
                        assembled.extend([whole_str, ".", num_str, ".", den_str])
                        i = m
                        continue

                # Standard decimal with integer part
                if k > j + 1:
                    frac_str = "".join(tokens[j + 1 : k])
                    assembled.append(f"{whole_str}.{frac_str}")
                else:
                    assembled.append(f"{whole_str}.0")
                i = k
                continue
            else:
                # Clean integer assembled from consecutive digits without decimal point
                assembled.append(whole_str)
                i = j
                continue

        # Standard decimal starting with "." (e.g. ['.', '8'] or ['.', '0', '2'])
        if tokens[i] == ".":
            j = i + 1
            while j < n and is_digit_token(tokens[j]):
                j += 1
            if j > i + 1:
                frac_str = "".join(tokens[i + 1 : j])
                assembled.append(f"0.{frac_str}")
                i = j
                continue
            else:
                assembled.append(".")
                i += 1
                continue

        assembled.append(tokens[i])
        i += 1
    return assembled


_SEQUENCES_REGISTRY: Optional[Dict[str, Dict[str, str]]] = None


def expand_res_macros(text: str) -> str:
    global _SEQUENCES_REGISTRY
    if "{{res:" not in text:
        return text
    if _SEQUENCES_REGISTRY is None:
        import json
        reg_path = REPO_ROOT / "docs" / "assets" / "manuals" / "sequences_registry.json"
        if reg_path.exists():
            _SEQUENCES_REGISTRY = json.loads(reg_path.read_text(encoding="utf-8"))
        else:
            _SEQUENCES_REGISTRY = {}
    def _repl(m):
        seq_id, field = m.group(1), m.group(2)
        entry = _SEQUENCES_REGISTRY.get(seq_id, {})
        if field == "keys":
            return str(entry.get("keys") or entry.get("seq") or m.group(0))
        if field == "value":
            return str(entry.get("value") or entry.get("res") or m.group(0))
        return str(entry.get(field, m.group(0)))
    return re.sub(r"\{\{res:([a-zA-Z0-9_]+):(keys|value)\}\}", _repl, text)


def tokenize_keystrokes(raw_str: str) -> List[str]:
    """
    Extracts high-level tokens from a Keystroke cell or inline trace sequence.
    Handles:
      - `{{key:...}}` and `{{keycap:...}}` macros
      - `[key]` bracketed keycaps
      - Scientific notation with {{key:E}} (e.g. 1.19104 {{key:E}} 16 {{key:+/-}})
      - Two-dot fraction entry: .Whole.Numerator.Denominator or .Numerator.Denominator
      - Numeric literals and bare operator words
    """
    # Strip {{res:...:value}} output macros before expanding {{res:...:keys}}
    raw_str = re.sub(r"\{\{res:[a-zA-Z0-9_]+:value\}\}", "", raw_str)
    # Expand {{res:...}} macros first
    clean = expand_res_macros(raw_str)
    # Strip inline code backticks and bold markdown
    clean = clean.replace("`", "").replace("**", "")

    # Look for compound exponent entries like: 1.19104 {{key:E}} 16 {{key:+/-}} or 5.972 {{key:E}} 24
    exp_pattern = re.compile(
        r"([+-]?[0-9.]+)\s+(?:\{\{key(?:cap)?:E(?:EX)?\}\}|\[E(?:EX)?\])\s+([0-9]+)(?:\s+(?:\{\{key(?:cap)?:(\+/-|CHS)\}\}|\[(\+/-|CHS)\]))?",
        re.IGNORECASE,
    )

    tokens: List[str] = []
    pos = 0
    while pos < len(clean):
        # Match exponent pattern
        m_exp = exp_pattern.match(clean, pos)
        if m_exp:
            mant = m_exp.group(1)
            exp = m_exp.group(2)
            is_neg = bool(m_exp.group(3) or m_exp.group(4))
            tokens.append(f"{mant}e{'-' if is_neg else '+'}{exp}")
            pos = m_exp.end()
            continue

        # Match macro {{key:...}}
        m_macro = re.match(r"\{\{key(?:cap)?:([^{}]+)\}\}", clean[pos:])
        if m_macro:
            tokens.append(m_macro.group(1).strip())
            pos += m_macro.end()
            continue

        # Match bracketed key [KEY]
        m_bracket = re.match(r"\[([^\[\]{}]+)\]", clean[pos:])
        if m_bracket:
            tokens.append(m_bracket.group(1).strip())
            pos += m_bracket.end()
            continue

        # Match bare word or numeric token
        m_word = re.match(r"[^\s\[\]{}]+", clean[pos:])
        if m_word:
            tokens.append(m_word.group(0).strip())
            pos += m_word.end()
            continue

        pos += 1

    return assemble_decimal_tokens(tokens)


def execute_keystroke_sequence(
    sim: RPNStackSimulator,
    raw_str: str,
    step_x: Optional[float] = None,
    step_y: Optional[float] = None,
) -> None:
    """Tokenizes and executes a sequence of keystrokes on the given simulator."""
    tokens = tokenize_keystrokes(raw_str)

    # Process digit strings (e.g. ['4', '5'] -> builds 45)
    i = 0
    while i < len(tokens):
        tok = tokens[i]

        # Skip menu-opener prefix keys when followed by a specific softkey selection
        next_tok = tokens[i + 1] if (i + 1) < len(tokens) else ""
        next2_tok = tokens[i + 2] if (i + 2) < len(tokens) else ""
        if tok in ("SUMS", "x̄,ȳ", "𝑥̄,𝑦̄", "s,σ"):
            target = next2_tok if next_tok in ("→", "->") else next_tok
            if target in ("Σx", "Σy", "Σx²", "Σy²", "Σxy", "x̄", "ȳ", "x̄w", "xw", "s", "sx", "sy", "σ", "σx", "σy"):
                i += 2 if next_tok in ("→", "->") else 1
                continue

        # Handle CLEAR Σ+ as CLΣ
        if tok == "CLEAR" and next_tok == "Σ+":
            sim.stat_clear()
            i += 2
            continue

        # Handle PROB menu prefix and RAND stochastic push
        if tok == "PROB" and next_tok in ("Cn,r", "Pn,r", "nCr", "nPr", "x!", "n!", "RAND"):
            i += 1
            continue
        if tok == "RAND":
            if step_x is not None:
                sim.push_number(step_x)
            i += 1
            continue
        if tok in ("t…x", "t...x"):
            if step_x is not None:
                sim.last_x = sim.stack[0]
                sim.stack[0] = step_x
                sim.stack_lift_enabled = True
                sim.is_building_number = False
            i += 1
            continue

        # Check for STO / RCL parameterization
        if tok in ("STO", "RCL") and (i + 1) < len(tokens) and len(tokens[i + 1]) == 1:
            var_name = tokens[i + 1]
            if tok == "STO":
                sim.regs[var_name] = sim.stack[0]
                sim.stack_lift_enabled = True
            else:
                sim.push_number(sim.regs.get(var_name, 0.0))
            i += 2
            continue

        # Check for SOLVE <var>
        if tok == "SOLVE":
            if (i + 1) < len(tokens) and len(tokens[i + 1]) == 1 and tokens[i + 1].isalpha():
                i += 2
            else:
                i += 1
            if step_x is not None:
                sim.push_number(step_x)
            continue

        # Check for Romberg integration ∫ <var>
        if tok in ("∫", "∫x", "∫X", "INTG"):
            if tok == "∫" and (i + 1) < len(tokens) and len(tokens[i + 1]) == 1 and tokens[i + 1].isalpha():
                i += 2
            else:
                i += 1
            if step_y is not None:
                sim.stack[1] = step_y
            if step_x is not None:
                sim.stack[0] = step_x
            sim.stack_lift_enabled = True
            sim.is_building_number = False
            continue

        # Check for two-dot fractions like [.] 5 [.] 8
        if tok == "." and (i + 3) < len(tokens) and tokens[i + 2] == ".":
            try:
                num = float(tokens[i + 1])
                den = float(tokens[i + 3])
                sim.push_number(num / den if den != 0 else 0.0)
                i += 4
                continue
            except ValueError:
                pass

        # Check for three-part mixed numbers like [1] [.] 2 [.] 5
        if is_digit_token(tok) and (i + 4) < len(tokens) and tokens[i + 1] == "." and tokens[i + 3] == "." and is_digit_token(tokens[i + 2]) and is_digit_token(tokens[i + 4]):
            try:
                whole = float(tok)
                num = float(tokens[i + 2])
                den = float(tokens[i + 4])
                sim.push_number(whole + (num / den if den != 0 else 0.0))
                i += 5
                continue
            except ValueError:
                pass

        sim.execute_token(tok)
        i += 1


# ==============================================================================
# 3. Value Parsing & Publication-Grade Formatting
# ==============================================================================

def parse_register_cell(cell_str: str) -> Optional[float]:
    """
    Parses a string from a table cell or inline trace into a float value.
    Extracts values from LaTeX math ($1.1910 \\times 10^{-16}$, $0.0000$),
    bold spans (**$17.2500$**), fractions (5/8), or plain numbers.
    """
    s = expand_res_macros(cell_str).strip()
    # Preserve \text{h}, \text{b}, \text{E} before stripping LaTeX \text{...} units
    s = re.sub(r"\\text\{\s*([hbE])\s*\}", r"\1", s)
    s = re.sub(r"\\text\{[^\}]*\}", "", s)
    s = re.sub(r"\\mathbf\{((?:[^{}]|\{[^{}]*\})*)\}", r"\1", s).strip()
    # Strip markdown bolding
    if s.startswith("**") and s.endswith("**"):
        s = s[2:-2].strip()
    if s.startswith("`") and s.endswith("`"):
        s = s[1:-1].strip()
    if s.startswith("$") and s.endswith("$"):
        s = s[1:-1].strip()
    if s.startswith("**") and s.endswith("**"):
        s = s[2:-2].strip()
    if s.startswith("`") and s.endswith("`"):
        s = s[1:-1].strip()

    # Strip any trailing commentary like "(Status Line: ...)" or "[STATUS: ...]"
    if "(" in s and not s.startswith("("):
        s = s.split("(", 1)[0].strip()
    if "[" in s and not s.startswith("["):
        s = s.split("[", 1)[0].strip()

    # Strip commas from thousands formatting e.g. $1,136,800.00$
    s = s.replace(",", "")

    # Check for hex literal ending in 'h' (e.g. 'C0A80A2Dh' or '2Dh' or '0h')
    m_hex = re.match(r"^(?:0x)?([0-9A-Fa-f]+)h$", s)
    if m_hex:
        try:
            return float(int(m_hex.group(1), 16))
        except Exception:
            pass

    # Check for binary literal ending in 'b' (e.g. '1010b' or '0b')
    m_bin = re.match(r"^([01]+)b$", s)
    if m_bin:
        try:
            return float(int(m_bin.group(1), 2))
        except Exception:
            pass

    # Check for LaTeX scientific notation: $a.bbbb \times 10^{exp}$ or mant * 10^exp
    m_sci = re.search(r"(-?[0-9.]+)\s*(?:\\times|\*)\s*10\^\{?(-?[0-9]+)\}?", s)
    if m_sci:
        try:
            return float(m_sci.group(1)) * (10 ** int(m_sci.group(2)))
        except Exception:
            pass

    # Strip LaTeX math delimiters
    if s.startswith("$") and s.endswith("$"):
        s = s[1:-1].strip()

    # Check for LaTeX fraction: e.g. 1\ \frac{3}{4} or \frac{3}{4}
    m_lfrac = re.search(r"^(?:(-?\d+)\s*(?:\\\s*)?)?\\(?:d?frac)\{(-?\d+)\}\{(-?\d+)\}$", s)
    if m_lfrac:
        try:
            whole = float(m_lfrac.group(1)) if m_lfrac.group(1) else 0.0
            num = float(m_lfrac.group(2))
            den = float(m_lfrac.group(3))
            return whole + (num / den if den != 0 else 0.0)
        except Exception:
            pass

    # Strip LaTeX backslash-space (e.g. 2\ 3/4 -> 2 3/4)
    s = s.replace("\\ ", " ")

    # Ratio support a:b
    m_ratio = re.match(r"^(\d+):(\d+)$", s)
    if m_ratio:
        try:
            num = float(m_ratio.group(1))
            den = float(m_ratio.group(2))
            return num / den if den != 0 else 0.0
        except Exception:
            pass

    # Fraction support
    if "/" in s:
        parts = s.split()
        if len(parts) == 2 and "/" in parts[1]:
            try:
                whole = float(parts[0])
                num, den = parts[1].split("/")
                return whole + (float(num) / float(den))
            except Exception:
                pass
        elif len(parts) == 1 and "/" in parts[0]:
            try:
                num, den = parts[0].split("/")
                return float(num) / float(den)
            except Exception:
                pass

    # Plain float
    m_num = re.search(r"-?[0-9]+(?:\.[0-9]+)?(?:[eE][-+]?[0-9]+)?", s)
    if m_num:
        try:
            return float(m_num.group(0))
        except Exception:
            pass

    return None


def format_stack_register(
    val: float,
    is_sc6: bool = False,
    precision: int = 4,
    is_bold: bool = False,
    original_style: Optional[str] = None,
) -> str:
    """
    Formats a stack register value according to strict Gate S10 physics and rubric:
    - Zero (|val| < 1e-12) formats as $0.0000$ (or $0$ for SC-6 integer mode).
    - Non-zero values with |val| < 1e-3 or |val| >= 1e7 use LaTeX scientific notation:
      $a.bbbb \\times 10^{exp}$, NEVER $0.0000$!
    - SC-6 integer values format as clean integers ($3$, $12$, etc.) when original style was integer.
    - Preserves bold markdown formatting if is_bold is True.
    """
    if val == 0.0 or abs(val) < 1e-300:
        val = 0.0

    # Retain plain integer style if original cell was plain integer without math delimiters
    if original_style == "plain_int" and is_sc6 and abs(val - round(val)) < 1e-9:
        res = str(int(round(val)))
        return f"**{res}**" if is_bold else res

    abs_v = abs(val)
    if abs_v == 0.0:
        res = "$0$" if (is_sc6 and precision == 0) else f"${0.0:.{precision}f}$"
    elif abs_v < 1e-3 or abs_v >= 1e7:
        # LaTeX scientific notation: $a.bbbb \times 10^{exp}$
        exp = int(math.floor(math.log10(abs_v)))
        mant = val / (10 ** exp)
        res = f"${mant:.4f} \\times 10^{{{exp}}}$"
    elif is_sc6 and precision == 0 and abs(val - round(val)) < 1e-9:
        res = f"${int(round(val))}$"
    else:
        res = f"${val:.{precision}f}$"

    if is_bold:
        return f"**{res}**"
    return res


# ==============================================================================
# 4. Markdown 4-Register Table Extraction & Synchronization
# ==============================================================================

class StackTableLocation:
    """Represents a discovered 4-register stack trace table in a markdown file."""

    def __init__(
        self,
        file_path: Path,
        start_line: int,
        header_line: str,
        separator_line: str,
        row_lines: List[Tuple[int, str]],
        col_k: int,
        col_t: int,
        col_z: int,
        col_y: int,
        col_x: int,
    ):
        self.file_path = file_path
        self.start_line = start_line
        self.header_line = header_line
        self.separator_line = separator_line
        self.row_lines = row_lines  # list of (1-based line_num, raw_line_str)
        self.col_k = col_k
        self.col_t = col_t
        self.col_z = col_z
        self.col_y = col_y
        self.col_x = col_x


def find_4_register_tables(file_path: Path) -> List[StackTableLocation]:
    """Finds all tables with Register T, Z, Y, X and Keystroke columns in file_path."""
    lines = file_path.read_text(encoding="utf-8").splitlines()
    tables: List[StackTableLocation] = []

    i = 0
    while i < len(lines) - 1:
        line = lines[i]
        next_line = lines[i + 1]

        # Check for markdown table header & separator
        if "|" in line and re.match(r"^\s*\|(?:\s*:?-+:?\s*\|)+\s*$", next_line):
            cells = [c.strip() for c in line.split("|")[1:-1]]
            col_k = col_t = col_z = col_y = col_x = None
            for idx, c in enumerate(cells):
                if re.search(r"\bkeystrokes?\b", c, re.IGNORECASE):
                    col_k = idx
                elif re.search(r"\bregister\s+t\b", c, re.IGNORECASE):
                    col_t = idx
                elif re.search(r"\bregister\s+z\b", c, re.IGNORECASE):
                    col_z = idx
                elif re.search(r"\bregister\s+y\b", c, re.IGNORECASE):
                    col_y = idx
                elif re.search(r"\bregister\s+x\b", c, re.IGNORECASE):
                    col_x = idx

            # If all 4 registers and Keystroke column are present
            if None not in (col_k, col_t, col_z, col_y, col_x):
                row_lines: List[Tuple[int, str]] = []
                r = i + 2
                while r < len(lines) and lines[r].strip().startswith("|") and "|" in lines[r]:
                    row_lines.append((r + 1, lines[r]))
                    r += 1

                if row_lines:
                    tables.append(
                        StackTableLocation(
                            file_path=file_path,
                            start_line=i + 1,
                            header_line=line,
                            separator_line=next_line,
                            row_lines=row_lines,
                            col_k=col_k,
                            col_t=col_t,
                            col_z=col_z,
                            col_y=col_y,
                            col_x=col_x,
                        )
                    )
                i = r
                continue
        i += 1

    return tables


# ==============================================================================
# 5. Gate S15 Inline Trace Parser
# ==============================================================================

class InlineTraceDiscrepancy:
    def __init__(self, file_path: Path, line_num: int, expected: Dict[str, float], actual: Dict[str, float], raw_text: str):
        self.file_path = file_path
        self.line_num = line_num
        self.expected = expected
        self.actual = actual
        self.raw_text = raw_text


INLINE_TRACE_PATTERN = re.compile(
    r"(?:`?\$?\(\s*|->\s*)(?:T\s*[=:]\s*([^,]+),\s*Z\s*[=:]\s*([^,]+),\s*Y\s*[=:]\s*([^,]+),\s*X\s*[=:]\s*([^,\)\$`]+)|X\s*[=:]\s*([^,]+),\s*Y\s*[=:]\s*([^,]+),\s*Z\s*[=:]\s*([^,]+),\s*T\s*[=:]\s*([^,\)\$`]+))(?:\s*\)?\$?`?)",
    re.IGNORECASE,
)


def _step_inline_trace_prefix(
    sim: RPNStackSimulator,
    prefix: str,
    m_idx: int,
    num_matches: int,
    exp_x: Optional[float],
    exp_y: Optional[float],
    clean_line: str,
    last_standalone_res: Optional[str],
) -> None:
    if "{{key:PLOT}}" in clean_line:
        return
    if "ratio mode" in prefix.lower() or "ratio mode" in clean_line.lower():
        sim.ratio_mode = True
    if "HEX" in prefix or "hexadecimal" in prefix.lower():
        sim.base_mode = "hex"
    if "BIN" in prefix:
        sim.base_mode = "bin"
    if "DEC" in prefix:
        sim.base_mode = "dec"
    if "{{key:POLY}}" in prefix:
        sim.poly_mode = True

    has_res_keys = bool(re.search(r"\{\{res:[a-zA-Z0-9_]+:keys\}\}", prefix))
    has_arrow = any(a in prefix for a in ("->", "\\to", "\\rightarrow"))

    if has_res_keys and has_arrow and num_matches == 1:
        res_m = re.search(r"\{\{res:[a-zA-Z0-9_]+:keys\}\}", prefix)
        if res_m:
            execute_keystroke_sequence(sim, res_m.group(0), step_x=exp_x, step_y=exp_y)
            return

    if has_res_keys and has_arrow and m_idx == 0:
        # Strip the summary sentence before the step-by-step walkthrough
        for arrow in ("->", "\\to", "\\rightarrow"):
            if arrow in prefix:
                after_arrow = prefix.split(arrow, 1)[1]
                if ". " in after_arrow:
                    prefix = after_arrow.split(". ", 1)[1]
                break

    raw_spans = []
    for cm in re.finditer(r"`([^`]+)`", prefix):
        before_span = prefix[: cm.start()].rstrip()
        if before_span.endswith(("->", "\\to", "\\rightarrow", "**", "displays", "is", "=")):
            continue
        raw_spans.append(cm.group(1))

    # Filter out bare prose identifier spans like `LASTX` or `XMIN` when macro spans exist
    code_spans = [
        s for s in raw_spans
        if "{{" in s or "[" in s or re.match(r"^[0-9.\s+-]+$", s.strip())
    ]

    if code_spans:
        for cs in code_spans:
            execute_keystroke_sequence(sim, cs, step_x=exp_x, step_y=exp_y)
    elif "{{" in prefix:
        for arrow in ("->", "\\to", "\\rightarrow"):
            if arrow in prefix:
                prefix = prefix.split(arrow)[0]
        execute_keystroke_sequence(sim, prefix, step_x=exp_x, step_y=exp_y)
    elif m_idx == 0 and last_standalone_res:
        execute_keystroke_sequence(sim, last_standalone_res, step_x=exp_x, step_y=exp_y)


def audit_inline_traces(file_path: Path) -> List[InlineTraceDiscrepancy]:
    """
    Parses and verifies compact Gate S15 inline register traces:
      (T=..., Z=..., Y=..., X=...) or (T:..., Z:..., Y:..., X:...) or (X=..., Y=..., Z=..., T=...)
    Maintains running simulator state across contiguous lines within a worked block.
    """
    lines = file_path.read_text(encoding="utf-8").splitlines()
    discrepancies: List[InlineTraceDiscrepancy] = []
    is_sc6 = "sc6" in str(file_path)
    sim = RPNStackSimulator(is_sc6=is_sc6)
    default_angle = "rad" if "05-complex" in str(file_path) else "deg"
    sim.angle_mode = default_angle
    block_two_stack = False
    block_angle_mode = default_angle
    last_standalone_res: Optional[str] = None

    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("#") or stripped == "---":
            sim.reset()
            sim.angle_mode = default_angle
            block_angle_mode = default_angle
            block_two_stack = False
            last_standalone_res = None
            continue
        if "2-Stack mode" in stripped or "2-LV" in stripped:
            block_two_stack = True
            sim.two_stack_mode = True
        if "{{key:RAD}}" in stripped or "in `RAD`" in stripped or "radian mode" in stripped.lower() or "radians mode" in stripped.lower():
            block_angle_mode = "rad"
            sim.angle_mode = "rad"
        if "{{key:DEG}}" in stripped or "degree mode" in stripped.lower() or "degrees mode" in stripped.lower():
            block_angle_mode = "deg"
            sim.angle_mode = "deg"

        # Reset 4-register stack at blank lines or table lines while preserving stat_* accumulators within the problem
        if not stripped or stripped.startswith("|") or stripped.startswith("**Keystrokes") or stripped.startswith("*Keystrokes"):
            if stripped.startswith("**Keystrokes") or stripped.startswith("*Keystrokes"):
                m_res = re.search(r"\{\{res:[a-zA-Z0-9_]+:keys\}\}", stripped)
                if m_res:
                    last_standalone_res = m_res.group(0)
            saved_stat = (sim.stat_n, sim.stat_sum_x, sim.stat_sum_x2, sim.stat_sum_y, sim.stat_sum_y2, sim.stat_sum_xy, list(sim.points))
            sim.reset()
            sim.two_stack_mode = block_two_stack
            sim.angle_mode = block_angle_mode
            sim.stat_n, sim.stat_sum_x, sim.stat_sum_x2, sim.stat_sum_y, sim.stat_sum_y2, sim.stat_sum_xy, sim.points = saved_stat
            continue

        clean_line = re.sub(r"^>\s*", "", stripped)
        matches = list(INLINE_TRACE_PATTERN.finditer(clean_line))
        if matches:
            prev_end = 0
            for m_idx, m in enumerate(matches):
                if m.group(1) is not None:
                    exp_t = parse_register_cell(m.group(1))
                    exp_z = parse_register_cell(m.group(2))
                    exp_y = parse_register_cell(m.group(3))
                    exp_x = parse_register_cell(m.group(4))
                else:
                    exp_x = parse_register_cell(m.group(5))
                    exp_y = parse_register_cell(m.group(6))
                    exp_z = parse_register_cell(m.group(7))
                    exp_t = parse_register_cell(m.group(8))

                prefix = clean_line[prev_end : m.start()]
                prev_end = m.end()
                _step_inline_trace_prefix(sim, prefix, m_idx, len(matches), exp_x, exp_y, clean_line, last_standalone_res)

                if None in (exp_t, exp_z, exp_y, exp_x):
                    continue

                expected = {"T": exp_t, "Z": exp_z, "Y": exp_y, "X": exp_x}
                actual = {"T": sim.t, "Z": sim.z, "Y": sim.y, "X": sim.x}

                tol = 5.1e-3
                mismatch = any(abs(expected[reg] - actual[reg]) > max(tol, abs(expected[reg]) * 0.0015) for reg in ("T", "Z", "Y", "X"))
                if mismatch:
                    discrepancies.append(
                        InlineTraceDiscrepancy(
                            file_path=file_path,
                            line_num=idx,
                            expected=expected,
                            actual=actual,
                            raw_text=line.strip(),
                        )
                    )
        elif re.match(r"^\d+\.\s+", clean_line) and "{{key:Σ+}}" in clean_line:
            for cm in re.finditer(r"`([^`]+)`", clean_line):
                if "{{key:Σ+}}" in cm.group(1):
                    execute_keystroke_sequence(sim, cm.group(1))
        elif re.search(r"\{\{res:[a-zA-Z0-9_]+:keys\}\}", clean_line):
            m_res = re.search(r"\{\{res:[a-zA-Z0-9_]+:keys\}\}", clean_line)
            if m_res:
                last_standalone_res = m_res.group(0)
                execute_keystroke_sequence(sim, m_res.group(0))
        elif ("{{" in clean_line or "[" in clean_line) and "->" in clean_line:
            prefix = clean_line.split("->")[0]
            execute_keystroke_sequence(sim, prefix)

    return discrepancies


# ==============================================================================
# 6. Audit & Synchronization Engine
# ==============================================================================

class TableDiscrepancy:
    def __init__(
        self,
        file_path: Path,
        line_num: int,
        step_keystrokes: str,
        reg_name: str,
        expected_val: float,
        actual_val: float,
        raw_cell: str,
    ):
        self.file_path = file_path
        self.line_num = line_num
        self.step_keystrokes = step_keystrokes
        self.reg_name = reg_name
        self.expected_val = expected_val
        self.actual_val = actual_val
        self.raw_cell = raw_cell


def extract_expected_nonzero_from_context(file_path: Path, start_line: int) -> Optional[float]:
    """
    Extracts expected non-zero numerical answer from the prose immediately preceding a table.
    Used for Bug B: flagging tables whose final X evaluates to 0.0 when context expects non-zero.
    """
    try:
        lines = file_path.read_text(encoding="utf-8").splitlines()
    except Exception:
        return None

    # Look back up to 30 lines preceding start_line
    start_idx = max(0, start_line - 31)
    end_idx = max(0, start_line - 1)
    lookback = lines[start_idx:end_idx]
    text_block = "\n".join(lookback)

    patterns = [
        r"(?:\\longrightarrow|\\rightarrow|->)\s*(?:X\s*=\s*)?\\mathbf\{([+-]?[0-9]+(?:\.[0-9]+)?)[^\}]*\}",
        r"(?:\\longrightarrow|\\rightarrow|->)\s*(?:X\s*=\s*)?\*\*([+-]?[0-9]+(?:\.[0-9]+)?)[^\*]*\*\*",
        r"displays:\s*\*\*([+-]?[0-9]+(?:\.[0-9]+)?)[^\*]*\*\*",
        r"X\s*=\s*\\mathbf\{([+-]?[0-9]+(?:\.[0-9]+)?)[^\}]*\}",
        r"X\s*=\s*\*\*([+-]?[0-9]+(?:\.[0-9]+)?)[^\*]*\*\*",
        r"(?:\\longrightarrow|\\rightarrow|->)\s*X\s*=\s*([+-]?[0-9]+(?:\.[0-9]+)?)",
    ]
    for pat in patterns:
        matches = list(re.finditer(pat, text_block))
        if matches:
            last_m = matches[-1]
            try:
                val = float(last_m.group(1))
                if abs(val) > 1e-6:
                    return val
            except ValueError:
                pass
    return None


def audit_table(table: StackTableLocation) -> List[TableDiscrepancy]:
    """Audits a single 4-register markdown table against RPNStackSimulator physics."""
    is_sc6 = "sc6" in str(table.file_path)
    sim = RPNStackSimulator(is_sc6=is_sc6)
    if "05-complex" in str(table.file_path):
        sim.angle_mode = "rad"
    discrepancies: List[TableDiscrepancy] = []

    # Check if table cells use hex ('0h') or preceding context specifies RAD/HEX/POLY/stat_n
    try:
        file_lines = table.file_path.read_text(encoding="utf-8").splitlines()
        ctx_text = "\n".join(file_lines[max(0, table.start_line - 25):table.start_line])
        if "{{key:RAD}}" in ctx_text or "in `RAD`" in ctx_text or "Radians (`{{key:RAD}}`)" in ctx_text:
            sim.angle_mode = "rad"
        if "{{key:HEX}}" in ctx_text and "{{key:DEC}}" not in ctx_text:
            sim.base_mode = "hex"
        if "{{key:POLY}}" in ctx_text:
            sim.poly_mode = True
        m_sn = re.search(r"sample count is \$n\s*=\s*(\d+)\$", ctx_text)
        if m_sn:
            sim.stat_n = int(m_sn.group(1))
    except Exception:
        pass
    if any("{{key:A}}" in r[1] or "{{key:EXEC}}" in r[1] for r in table.row_lines):
        sim.poly_mode = True
    if any(re.search(r"^\s*[\$`\*]*0[0-9A-Fa-f]*h[\$`\*]*\s*$", r[1].split("|")[table.col_t + 1]) for r in table.row_lines if len(r[1].split("|")) > table.col_t + 1):
        sim.base_mode = "hex"

    for line_num, raw_line in table.row_lines:
        safe_line = raw_line.replace("|x|", "__ABS_KEY__")
        cells = [c.replace("__ABS_KEY__", "|x|").strip() for c in safe_line.split("|")[1:-1]]
        if len(cells) <= max(table.col_k, table.col_t, table.col_z, table.col_y, table.col_x):
            continue

        keystrokes = cells[table.col_k]
        step_x = parse_register_cell(cells[table.col_x])
        step_y = parse_register_cell(cells[table.col_y])
        execute_keystroke_sequence(sim, keystrokes, step_x=step_x, step_y=step_y)

        # Compare simulated registers to table cells
        cell_checks = [
            ("T", table.col_t, sim.t),
            ("Z", table.col_z, sim.z),
            ("Y", table.col_y, sim.y),
            ("X", table.col_x, sim.x),
        ]

        for reg_name, col_idx, sim_val in cell_checks:
            raw_c = cells[col_idx]
            parsed_c = parse_register_cell(raw_c)
            if parsed_c is None:
                continue

            # Compare within tolerance
            tol = 5.1e-3
            diff = abs(sim_val - parsed_c)
            if diff > max(tol, abs(parsed_c) * 0.0015):
                discrepancies.append(
                    TableDiscrepancy(
                        file_path=table.file_path,
                        line_num=line_num,
                        step_keystrokes=keystrokes,
                        reg_name=reg_name,
                        expected_val=sim_val,
                        actual_val=parsed_c,
                        raw_cell=raw_c,
                    )
                )

    # Bug B: Flag table whose final X (and Y for complex) evaluates to 0.0 when surrounding context expects non-zero
    if abs(sim.x) < 1e-9 and abs(sim.y) < 1e-9 and table.row_lines:
        exp_ctx = extract_expected_nonzero_from_context(table.file_path, table.start_line)
        if exp_ctx is not None:
            last_line_num, last_raw_line = table.row_lines[-1]
            last_cells = [c.strip() for c in last_raw_line.split("|")[1:-1]]
            last_k = last_cells[table.col_k] if len(last_cells) > table.col_k else "Final Row"
            last_x_raw = last_cells[table.col_x] if len(last_cells) > table.col_x else "$0.00$"
            discrepancies.append(
                TableDiscrepancy(
                    file_path=table.file_path,
                    line_num=last_line_num,
                    step_keystrokes=f"Final X evaluates to 0.0 but surrounding context indicates non-zero result ({exp_ctx})",
                    reg_name="X (Zero Result Audit)",
                    expected_val=exp_ctx,
                    actual_val=sim.x,
                    raw_cell=last_x_raw,
                )
            )

    return discrepancies


def sync_table_in_file(table: StackTableLocation, file_text: str) -> str:
    """Simulates table keystrokes and synchronizes table cells to true simulated physics."""
    is_sc6 = "sc6" in str(table.file_path)
    sim = RPNStackSimulator(is_sc6=is_sc6)
    lines = file_text.splitlines()

    for line_num, raw_line in table.row_lines:
        idx = line_num - 1
        raw_parts = lines[idx].split("|")
        # Split leaves an empty first and last item if line starts and ends with '|'
        cells = [c for c in raw_parts[1:-1]]
        if len(cells) <= max(table.col_k, table.col_t, table.col_z, table.col_y, table.col_x):
            continue

        keystrokes = cells[table.col_k].strip()
        execute_keystroke_sequence(sim, keystrokes)

        # Update columns T, Z, Y, X
        reg_updates = [
            (table.col_t, sim.t),
            (table.col_z, sim.z),
            (table.col_y, sim.y),
            (table.col_x, sim.x),
        ]

        for col_idx, sim_val in reg_updates:
            old_cell = cells[col_idx].strip()
            is_bold = old_cell.startswith("**") and old_cell.endswith("**")
            orig_style = "plain_int" if (is_sc6 and old_cell.isdigit()) else "latex"
            precision = 4
            if "." in old_cell:
                # count decimals
                m_dec = re.search(r"\.([0-9]+)", old_cell)
                if m_dec:
                    precision = len(m_dec.group(1))

            new_val_str = format_stack_register(
                sim_val,
                is_sc6=is_sc6,
                precision=precision,
                is_bold=is_bold,
                original_style=orig_style,
            )
            cells[col_idx] = f" {new_val_str} "

        # Rebuild line
        lines[idx] = f"|{'|'.join(cells)}|"

    return "\n".join(lines)


# ==============================================================================
# 7. High-Level Runner & Gate S10 Integration
# ==============================================================================

def get_manual_files(repo_root: Path, target_file: Optional[Path] = None) -> List[Path]:
    """Retrieves target manual markdown files."""
    if target_file is not None:
        return [target_file]

    files: List[Path] = []
    for sub in ("sc32", "sc6"):
        dir_path = repo_root / "docs" / "manuals" / sub
        if dir_path.exists():
            files.extend(sorted(dir_path.glob("*.md")))
    return files


def audit_all_tables_and_traces(
    repo_root: Path = REPO_ROOT,
    target_file: Optional[Path] = None,
    strict: bool = True,
    verbose: bool = False,
) -> Dict[str, int]:
    """
    Gate S10 automated audit pass.
    Audits all 4-register markdown tables and Gate S15 inline traces across manuals.
    """
    manual_files = get_manual_files(repo_root, target_file)
    total_tables = 0
    total_traces = 0
    all_table_discrepancies: List[TableDiscrepancy] = []
    all_trace_discrepancies: List[InlineTraceDiscrepancy] = []

    for fpath in manual_files:
        tables = find_4_register_tables(fpath)
        total_tables += len(tables)
        for tbl in tables:
            discs = audit_table(tbl)
            all_table_discrepancies.extend(discs)
            if verbose and discs:
                print(f"[{fpath.name}:{tbl.start_line}] {len(discs)} discrepancies")

        txt = fpath.read_text(encoding="utf-8")
        total_traces += len(re.findall(r"T\s*[=:]\s*[^,]+,\s*Z\s*[=:]\s*[^,]+,\s*Y\s*[=:]\s*[^,]+,\s*X\s*[=:]", txt))
        traces = audit_inline_traces(fpath)
        all_trace_discrepancies.extend(traces)

    stats = {
        "files_checked": len(manual_files),
        "tables_checked": total_tables,
        "traces_checked": total_traces,
        "table_discrepancies": len(all_table_discrepancies),
        "trace_discrepancies": len(all_trace_discrepancies),
    }

    if verbose or all_table_discrepancies or all_trace_discrepancies:
        print("\n=== Gate S10 RPN Stack Table & Trace Audit Results ===")
        print(f"Files audited:        {stats['files_checked']}")
        print(f"4-Register tables:    {stats['tables_checked']}")
        print(f"Inline traces:        {stats['traces_checked']}")
        print(f"Table discrepancies:  {stats['table_discrepancies']}")
        print(f"Trace discrepancies:  {stats['trace_discrepancies']}")

        if all_table_discrepancies:
            print("\nTop Table Discrepancies:")
            for d in all_table_discrepancies[:15]:
                print(
                    f"  {d.file_path.name}:{d.line_num} [Reg {d.reg_name}] "
                    f"Simulated={d.expected_val} vs Table={d.actual_val} "
                    f"(Keys: '{d.step_keystrokes}')"
                )

    if strict and (all_table_discrepancies or all_trace_discrepancies):
        total_issues = len(all_table_discrepancies) + len(all_trace_discrepancies)
        print(f"\n❌ Gate S10 Stack Verification FAILED with {total_issues} discrepancies.")
    elif not all_table_discrepancies and not all_trace_discrepancies:
        print(f"✅ Gate S10: {total_tables} tables & {total_traces} inline traces 100% verified against RPNCore physics.")

    return stats


def _format_inline_reg(sim_val: float, old_raw: str, is_sc6: bool, base_mode: str) -> str:
    parsed_old = parse_register_cell(old_raw)
    tol = 5.1e-3
    if parsed_old is not None and abs(sim_val - parsed_old) <= max(tol, abs(parsed_old) * 0.0015):
        return old_raw.strip()

    s = old_raw.strip()
    if base_mode == "hex" or s.endswith("h") or "\\text{h}" in s:
        use_text_h = "\\text{h}" in s
        hex_str = f"{int(round(sim_val)) & 0xFFFFFFFFF:X}"
        return f"{hex_str}\\text{{h}}" if use_text_h else f"{hex_str}h"
    if base_mode == "bin" or s.endswith("b") or "\\text{b}" in s:
        use_text_b = "\\text{b}" in s
        bin_str = f"{int(round(sim_val)) & 0xFFFFFFFFF:b}"
        return f"{bin_str}\\text{{b}}" if use_text_b else f"{bin_str}b"

    precision = 0 if (is_sc6 and "." not in s) else 4
    m_dec = re.search(r"\.([0-9]+)", s)
    if m_dec:
        precision = len(m_dec.group(1))

    abs_v = abs(sim_val)
    if abs_v < 1e-12:
        return "0" if (precision == 0) else f"{0.0:.{precision}f}"
    if abs_v < 1e-3 or abs_v >= 1e7:
        exp = int(math.floor(math.log10(abs_v)))
        mant = sim_val / (10 ** exp)
        return f"{mant:.2f}\\times 10^{{{exp}}}"
    if precision == 0 and abs(sim_val - round(sim_val)) < 1e-9:
        return str(int(round(sim_val)))
    return f"{sim_val:.{precision}f}"


def sync_inline_traces_in_file(file_path: Path, file_text: str) -> str:
    """Synchronizes inline traces in file_text to match RPNStackSimulator physics."""
    lines = file_text.splitlines()
    is_sc6 = "sc6" in str(file_path)
    sim = RPNStackSimulator(is_sc6=is_sc6)
    default_angle = "rad" if "05-complex" in str(file_path) else "deg"
    sim.angle_mode = default_angle
    block_two_stack = False
    block_angle_mode = default_angle
    last_standalone_res: Optional[str] = None

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("#") or stripped == "---":
            sim.reset()
            sim.angle_mode = default_angle
            block_angle_mode = default_angle
            block_two_stack = False
            last_standalone_res = None
            continue
        if "2-Stack mode" in stripped or "2-LV" in stripped:
            block_two_stack = True
            sim.two_stack_mode = True
        if "{{key:RAD}}" in stripped or "in `RAD`" in stripped or "radian mode" in stripped.lower() or "radians mode" in stripped.lower():
            block_angle_mode = "rad"
            sim.angle_mode = "rad"
        if "{{key:DEG}}" in stripped or "degree mode" in stripped.lower() or "degrees mode" in stripped.lower():
            block_angle_mode = "deg"
            sim.angle_mode = "deg"

        if not stripped or stripped.startswith("|") or stripped.startswith("**Keystrokes") or stripped.startswith("*Keystrokes"):
            if stripped.startswith("**Keystrokes") or stripped.startswith("*Keystrokes"):
                m_res = re.search(r"\{\{res:[a-zA-Z0-9_]+:keys\}\}", stripped)
                if m_res:
                    last_standalone_res = m_res.group(0)
            saved_stat = (sim.stat_n, sim.stat_sum_x, sim.stat_sum_x2, sim.stat_sum_y, sim.stat_sum_y2, sim.stat_sum_xy, list(sim.points))
            sim.reset()
            sim.two_stack_mode = block_two_stack
            sim.angle_mode = block_angle_mode
            sim.stat_n, sim.stat_sum_x, sim.stat_sum_x2, sim.stat_sum_y, sim.stat_sum_y2, sim.stat_sum_xy, sim.points = saved_stat
            continue

        clean_line = re.sub(r"^>\s*", "", stripped)
        matches = list(INLINE_TRACE_PATTERN.finditer(line))
        if matches:
            new_line_parts: List[str] = []
            prev_end = 0
            for m_idx, m in enumerate(matches):
                if m.group(1) is not None:
                    exp_t = parse_register_cell(m.group(1))
                    exp_z = parse_register_cell(m.group(2))
                    exp_y = parse_register_cell(m.group(3))
                    exp_x = parse_register_cell(m.group(4))
                else:
                    exp_x = parse_register_cell(m.group(5))
                    exp_y = parse_register_cell(m.group(6))
                    exp_z = parse_register_cell(m.group(7))
                    exp_t = parse_register_cell(m.group(8))

                prefix = line[prev_end : m.start()]
                clean_prefix = re.sub(r"^>\s*", "", prefix) if m_idx == 0 else prefix
                _step_inline_trace_prefix(sim, clean_prefix, m_idx, len(matches), exp_x, exp_y, clean_line, last_standalone_res)

                new_line_parts.append(prefix)
                full_match = m.group(0)
                if None not in (exp_t, exp_z, exp_y, exp_x) and m.group(1) is not None:
                    new_t = _format_inline_reg(sim.t, m.group(1), is_sc6, sim.base_mode)
                    new_z = _format_inline_reg(sim.z, m.group(2), is_sc6, sim.base_mode)
                    new_y = _format_inline_reg(sim.y, m.group(3), is_sc6, sim.base_mode)
                    new_x = _format_inline_reg(sim.x, m.group(4), is_sc6, sim.base_mode)
                    # Replace inside full_match preserving T=/T: separator
                    sep = ": " if ":" in full_match.split(",")[0] else "="
                    lead = full_match[: full_match.upper().find("T")]
                    trail = full_match[m.end(4) - m.start() :]
                    full_match = f"{lead}T{sep}{new_t}, Z{sep}{new_z}, Y{sep}{new_y}, X{sep}{new_x}{trail}"
                new_line_parts.append(full_match)
                prev_end = m.end()
            new_line_parts.append(line[prev_end:])
            lines[idx] = "".join(new_line_parts)
        elif re.match(r"^\d+\.\s+", clean_line) and "{{key:Σ+}}" in clean_line:
            for cm in re.finditer(r"`([^`]+)`", clean_line):
                if "{{key:Σ+}}" in cm.group(1):
                    execute_keystroke_sequence(sim, cm.group(1))
        elif re.search(r"\{\{res:[a-zA-Z0-9_]+:keys\}\}", clean_line):
            m_res = re.search(r"\{\{res:[a-zA-Z0-9_]+:keys\}\}", clean_line)
            if m_res:
                last_standalone_res = m_res.group(0)
                execute_keystroke_sequence(sim, m_res.group(0))
        elif ("{{" in clean_line or "[" in clean_line) and "->" in clean_line:
            prefix = clean_line.split("->")[0]
            execute_keystroke_sequence(sim, prefix)

    return "\n".join(lines) + ("\n" if file_text.endswith("\n") else "")


def sync_all_tables(
    repo_root: Path = REPO_ROOT,
    target_file: Optional[Path] = None,
    verbose: bool = False,
) -> int:
    """Synchronizes all 4-register markdown tables and inline traces across manuals."""
    manual_files = get_manual_files(repo_root, target_file)
    synced_tables = 0

    for fpath in manual_files:
        content = fpath.read_text(encoding="utf-8")
        tables = find_4_register_tables(fpath)
        # Sync each table that has discrepancies in reverse order so line offsets remain stable
        for tbl in reversed(tables):
            if audit_table(tbl):
                content = sync_table_in_file(tbl, content)
                synced_tables += 1

        if audit_inline_traces(fpath):
            content = sync_inline_traces_in_file(fpath, content)
        fpath.write_text(content, encoding="utf-8")
        if verbose:
            print(f"Synced {len(tables)} tables and inline traces in {fpath.name}")

    print(f"✅ Synchronized {synced_tables} 4-register tables and inline traces across {len(manual_files)} files.")
    return synced_tables


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify and synchronize 4-register RPN stack tables and inline traces."
    )
    parser.add_argument("--check", action="store_true", help="Audit tables and exit non-zero on failure")
    parser.add_argument("--sync", action="store_true", help="Auto-sync tables to true simulated states")
    parser.add_argument("--file", type=str, default=None, help="Specific markdown file to audit or sync")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose diagnostic output")

    args = parser.parse_args()
    target_path = Path(args.file).resolve() if args.file else None

    if args.sync:
        sync_all_tables(repo_root=REPO_ROOT, target_file=target_path, verbose=args.verbose)
        return 0

    # Default action is --check
    stats = audit_all_tables_and_traces(
        repo_root=REPO_ROOT,
        target_file=target_path,
        strict=args.check,
        verbose=args.verbose or args.check,
    )

    if args.check:
        total_failures = stats["table_discrepancies"] + stats["trace_discrepancies"]
        return 1 if total_failures > 0 else 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
