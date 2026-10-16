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
        """Dyadic stack drop with T-replication."""
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
        """▸REC / →REC: Converts polar (theta in Y, r in X) to rectangular (Y in Y, X in X)."""
        r = self.stack[0]
        theta = self.stack[1]
        self.last_x = r
        rad = self._to_rad(theta)
        x = r * math.cos(rad)
        y = r * math.sin(rad)
        self.stack[0] = x
        self.stack[1] = y
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

    # --- Token Execution ---

    def execute_token(self, tok: str) -> None:
        """Executes a single normalized calculator token."""
        t = tok.strip()
        if not t:
            return

        # Direct numeric literals
        try:
            # Check for scientific notation or standard float
            val = float(t)
            self.push_number(val)
            return
        except ValueError:
            pass

        # Check for hexadecimal literal (e.g. '0x2F80' or '2F80h')
        if t.lower().endswith("h") and len(t) > 1:
            try:
                hex_val = int(t[:-1], 16)
                self.push_number(float(hex_val))
                return
            except ValueError:
                pass
        if self.base_mode == "hex":
            try:
                hex_val = int(t, 16)
                self.push_number(float(hex_val))
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

        # Operator dispatch table
        op_map = {
            "ENTER": self.enter,
            "=": self.enter,
            "+": lambda: self.execute_dyadic(lambda y, x: y + x),
            "-": lambda: self.execute_dyadic(lambda y, x: y - x),
            "−": lambda: self.execute_dyadic(lambda y, x: y - x),
            "×": lambda: self.execute_dyadic(lambda y, x: y * x),
            "*": lambda: self.execute_dyadic(lambda y, x: y * x),
            "÷": lambda: self.execute_dyadic(lambda y, x: y / x if x != 0 else 0.0),
            "/": lambda: self.execute_dyadic(lambda y, x: y / x if x != 0 else 0.0),
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
            "SIN": lambda: self.execute_monadic(lambda x: math.sin(self._to_rad(x))),
            "COS": lambda: self.execute_monadic(lambda x: math.cos(self._to_rad(x))),
            "TAN": lambda: self.execute_monadic(lambda x: math.tan(self._to_rad(x))),
            "ASIN": lambda: self.execute_monadic(lambda x: self._from_rad(math.asin(max(-1.0, min(1.0, x))))),
            "ACOS": lambda: self.execute_monadic(lambda x: self._from_rad(math.acos(max(-1.0, min(1.0, x))))),
            "ATAN": lambda: self.execute_monadic(lambda x: self._from_rad(math.atan(x))),
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
            "SGN": lambda: self.execute_monadic(lambda x: 1.0 if x > 0 else (-1.0 if x < 0 else 0.0)),
            "π": lambda: self.push_number(math.pi),
            "PI": lambda: self.push_number(math.pi),
            "e": lambda: self.push_number(math.e),
            "x!": lambda: self.execute_monadic(lambda x: float(math.factorial(int(x))) if 0 <= x <= 170 and int(x) == x else math.gamma(x + 1.0)),
            "n!": lambda: self.execute_monadic(lambda x: float(math.factorial(int(x))) if 0 <= x <= 170 and int(x) == x else math.gamma(x + 1.0)),
            "FACT": lambda: self.execute_monadic(lambda x: float(math.factorial(int(x))) if (not self.is_sc6 and 0 <= x <= 170 and int(x) == x) else (1.0 if self._is_prime(int(x)) else 0.0)),
            "nPr": lambda: self.execute_dyadic(lambda y, x: float(math.perm(int(y), int(x))) if int(y) >= int(x) >= 0 else 0.0),
            "nCr": lambda: self.execute_dyadic(lambda y, x: float(math.comb(int(y), int(x))) if int(y) >= int(x) >= 0 else 0.0),
            "MOD": lambda: self.execute_dyadic(lambda y, x: y - x * math.floor(y / x) if x != 0 else 0.0),
            "%": lambda: self.execute_dyadic(lambda y, x: (y * x) / 100.0),
            "%CHG": lambda: self.execute_dyadic(lambda y, x: ((x - y) / y) * 100.0 if y != 0 else 0.0),
            "Δ%": lambda: self.execute_dyadic(lambda y, x: ((x - y) / y) * 100.0 if y != 0 else 0.0),
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
            "σ": lambda: (setattr(self, "last_x", self.stack[0]), self.push_number(math.sqrt(max(0.0, (self.stat_sum_x2 - (self.stat_sum_x ** 2 / self.stat_n)) / self.stat_n)) if self.stat_n > 0 else 0.0)),
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
            "÷R": self.execute_div_r,
            "INT÷": self.execute_div_r,
            "REP": self.execute_rep,
            "GCF": lambda: self.execute_dyadic(lambda y, x: float(math.gcd(int(round(y)), int(round(x))))),
            "GCD": lambda: self.execute_dyadic(lambda y, x: float(math.gcd(int(round(y)), int(round(x))))),
            "LCM": lambda: self.execute_dyadic(lambda y, x: float(abs(int(round(y)) * int(round(x))) // math.gcd(int(round(y)), int(round(x)))) if int(round(y)) != 0 and int(round(x)) != 0 else 0.0),
            "PRIME": lambda: self.execute_monadic(lambda x: 1.0 if self._is_prime(int(round(x))) else 0.0),
            "RECT": lambda: self.execute_dyadic(lambda y, x: y * x),
            "AREA_RECT": lambda: self.execute_dyadic(lambda y, x: y * x),
            "TRI": lambda: self.execute_dyadic(lambda y, x: 0.5 * y * x),
            "AREA_TRI": lambda: self.execute_dyadic(lambda y, x: 0.5 * y * x),
            "CIRC": lambda: self.execute_monadic(lambda x: math.pi * x * x),
            "AREA_CIRC": lambda: self.execute_monadic(lambda x: math.pi * x * x),
            "HYP": lambda: self.execute_dyadic(lambda y, x: math.hypot(y, x)),
            "PRISM": lambda: self.execute_dyadic(lambda y, x: y * x),
            "VOL_PRISM": lambda: self.execute_dyadic(lambda y, x: y * x),
            "CYL": lambda: self.execute_dyadic(lambda y, x: math.pi * (y ** 2) * x),
            "VOL_CYL": lambda: self.execute_dyadic(lambda y, x: math.pi * (y ** 2) * x),
            "CONE": lambda: self.execute_dyadic(lambda y, x: (math.pi * (y ** 2) * x) / 3.0),
            "VOL_CONE": lambda: self.execute_dyadic(lambda y, x: (math.pi * (y ** 2) * x) / 3.0),
            "PYR": lambda: self.execute_dyadic(lambda y, x: (y * x) / 3.0),
            "▸POL": self.to_polar,
            "→POL": self.to_polar,
            "▸REC": self.to_rectangular,
            "→REC": self.to_rectangular,
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
    # Strip inline code backticks and bold markdown
    clean = raw_str.replace("`", "").replace("**", "")

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
        m_bracket = re.match(r"\[([^\]]+)\]", clean[pos:])
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

    return tokens


def execute_keystroke_sequence(sim: RPNStackSimulator, raw_str: str) -> None:
    """Tokenizes and executes a sequence of keystrokes on the given simulator."""
    tokens = tokenize_keystrokes(raw_str)

    # Process digit strings (e.g. ['4', '5'] -> builds 45)
    i = 0
    while i < len(tokens):
        tok = tokens[i]

        # Check for STO / RCL parameterization
        if tok in ("STO", "RCL") and (i + 1) < len(tokens) and len(tokens[i + 1]) == 1:
            var_name = tokens[i + 1]
            if tok == "STO":
                sim.regs[var_name] = sim.stack[0]
            else:
                sim.push_number(sim.regs.get(var_name, 0.0))
            i += 2
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
    s = cell_str.strip()
    # Strip markdown bolding
    if s.startswith("**") and s.endswith("**"):
        s = s[2:-2].strip()
    if s.startswith("`") and s.endswith("`"):
        s = s[1:-1].strip()

    # Strip any trailing commentary like "(Status Line: ...)" or "(Y=...)"
    if "(" in s and not s.startswith("("):
        s = s.split("(", 1)[0].strip()

    # Strip commas from thousands formatting e.g. $1,136,800.00$
    s = s.replace(",", "")

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


def audit_inline_traces(file_path: Path) -> List[InlineTraceDiscrepancy]:
    """
    Parses and verifies compact Gate S15 inline register traces:
      (T=..., Z=..., Y=..., X=...) or (X=..., Y=..., Z=..., T=...) or -> X=12, Y=12...
    Maintains running simulator state across contiguous lines within a worked block.
    """
    lines = file_path.read_text(encoding="utf-8").splitlines()
    discrepancies: List[InlineTraceDiscrepancy] = []
    is_sc6 = "sc6" in str(file_path)
    sim = RPNStackSimulator(is_sc6=is_sc6)

    # Patterns for inline traces
    trace_pattern = re.compile(
        r"(?:\$?\(\s*|->\s*)(?:T=([^,]+),\s*Z=([^,]+),\s*Y=([^,]+),\s*X=([^,\)\$]+)|X=([^,]+),\s*Y=([^,]+),\s*Z=([^,]+),\s*T=([^,\)\$]+))(?:\s*\)?\$?)",
        re.IGNORECASE,
    )

    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        # Reset simulator state at section boundaries, headings, or thematic breaks
        if not stripped or stripped.startswith("#") or stripped == "---" or stripped.startswith("|"):
            sim.reset()
            continue

        clean_line = re.sub(r"^>\s*", "", stripped)
        m = trace_pattern.search(clean_line)
        if m:
            prefix = clean_line[: m.start()]
            if "->" in prefix:
                prefix = prefix.split("->")[0]
            if "{{" in prefix or "[" in prefix:
                execute_keystroke_sequence(sim, prefix)

            # Extract expected register values
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

            if None in (exp_t, exp_z, exp_y, exp_x):
                continue

            expected = {"T": exp_t, "Z": exp_z, "Y": exp_y, "X": exp_x}
            actual = {"T": sim.t, "Z": sim.z, "Y": sim.y, "X": sim.x}

            # Tolerance check
            tol = 1e-3
            mismatch = any(abs(expected[reg] - actual[reg]) > max(tol, abs(expected[reg]) * 0.01) for reg in ("T", "Z", "Y", "X"))
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
        elif ("{{" in clean_line or "[" in clean_line) and "->" in clean_line:
            # Intermediate step in a block (e.g. line 206)
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


def audit_table(table: StackTableLocation) -> List[TableDiscrepancy]:
    """Audits a single 4-register markdown table against RPNStackSimulator physics."""
    is_sc6 = "sc6" in str(table.file_path)
    sim = RPNStackSimulator(is_sc6=is_sc6)
    discrepancies: List[TableDiscrepancy] = []

    for line_num, raw_line in table.row_lines:
        cells = [c.strip() for c in raw_line.split("|")[1:-1]]
        if len(cells) <= max(table.col_k, table.col_t, table.col_z, table.col_y, table.col_x):
            continue

        keystrokes = cells[table.col_k]
        execute_keystroke_sequence(sim, keystrokes)

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
            tol = 1e-3
            diff = abs(sim_val - parsed_c)
            if diff > max(tol, abs(parsed_c) * 0.01):
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

        traces = audit_inline_traces(fpath)
        total_traces += len(traces)
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


def sync_all_tables(
    repo_root: Path = REPO_ROOT,
    target_file: Optional[Path] = None,
    verbose: bool = False,
) -> int:
    """Synchronizes all 4-register markdown tables across manuals."""
    manual_files = get_manual_files(repo_root, target_file)
    synced_tables = 0

    for fpath in manual_files:
        tables = find_4_register_tables(fpath)
        if not tables:
            continue

        content = fpath.read_text(encoding="utf-8")
        # Sync each table in reverse order so line offsets remain stable
        for tbl in reversed(tables):
            content = sync_table_in_file(tbl, content)
            synced_tables += 1

        fpath.write_text(content, encoding="utf-8")
        if verbose:
            print(f"Synced {len(tables)} tables in {fpath.name}")

    print(f"✅ Synchronized {synced_tables} 4-register tables across {len(manual_files)} files.")
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
