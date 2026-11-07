#!/usr/bin/env python3
"""
Generates all 59 publication-grade technical diagrams (300 DPI) for Volume III:
THE STACK IN THE FIELD: When Mathematics Meets the Physical Trades.

Outputs PNG diagrams to:
  - documentation/manuals/assets/diagrams/domains/
  - Website/static/img/manuals/diagrams/domains/ (if present)
"""

from __future__ import annotations

import math
import shutil
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Arc, Wedge, Polygon, Rectangle, FancyArrowPatch

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "documentation" / "manuals" / "assets" / "diagrams" / "domains"

# Publication typography & grayscale-friendly high-contrast palette
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["STIXGeneral", "DejaVu Serif", "Times New Roman", "Times"],
    "mathtext.fontset": "stix",
    "font.size": 9.5,
    "axes.edgecolor": "#1F2937",
    "axes.linewidth": 1.0,
    "figure.facecolor": "#FFFFFF",
    "axes.facecolor": "#FFFFFF",
    "savefig.facecolor": "#FFFFFF",
})

INK = "#111827"
SLATE = "#374151"
MUTED = "#6B7280"
LIGHT_GRAY = "#E5E7EB"
MID_GRAY = "#D1D5DB"
SOFT_BG = "#F3F4F6"
ACCENT = "#1E3A8A"


def save_fig(fig: plt.Figure, name: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / name
    fig.savefig(out_path, dpi=300, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)


def new_canvas(w: float = 6.4, h: float = 2.5, xlim=(0, 10), ylim=(0, 4)):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    return fig, ax


def draw_box(ax, x, y, w, h, text="", subtext="", bg=SOFT_BG, ec=INK, lw=1.3, fontsize=9.5, bold=True, radius=0.12):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0.02,rounding_size={radius}",
        facecolor=bg, edgecolor=ec, linewidth=lw
    )
    ax.add_patch(patch)
    if text and subtext:
        ax.text(x + w / 2, y + h * 0.63, text, ha="center", va="center",
                fontsize=fontsize, fontweight="bold" if bold else "normal", color=INK)
        ax.text(x + w / 2, y + h * 0.30, subtext, ha="center", va="center",
                fontsize=fontsize - 1.2, color=SLATE)
    elif text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=fontsize, fontweight="bold" if bold else "normal", color=INK)
    return patch


def draw_arrow(ax, x0, y0, x1, y1, label="", label_offset=(0, 0.16), lw=1.4, color=INK, style="-|>", curved=0.0):
    conn = f"arc3,rad={curved}" if curved != 0 else "arc3,rad=0"
    arr = FancyArrowPatch(
        (x0, y0), (x1, y1),
        arrowstyle=style, mutation_scale=12,
        linewidth=lw, color=color, connectionstyle=conn
    )
    ax.add_patch(arr)
    if label:
        mx, my = (x0 + x1) / 2 + label_offset[0], (y0 + y1) / 2 + label_offset[1]
        ax.text(mx, my, label, ha="center", va="center", fontsize=8.8, color=INK)


def right_angle_mark(ax, vx, vy, dx1, dy1, dx2, dy2, size=0.25):
    p1 = (vx + dx1 * size, vy + dy1 * size)
    p2 = (vx + (dx1 + dx2) * size, vy + (dy1 + dy2) * size)
    p3 = (vx + dx2 * size, vy + dy2 * size)
    ax.plot([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], color=SLATE, lw=1.0)


# ===========================================================================
# INTRODUCTION (index.md)
# ===========================================================================
def gen_intro():
    # 0. Three Motivating Physical Puzzles (Compass, Conduit Bend, Dough Heat Balance)
    fig, axes = plt.subplots(1, 3, figsize=(6.6, 2.35))
    fig.subplots_adjust(wspace=0.14)
    for a in axes:
        a.set_xlim(0, 10)
        a.set_ylim(0, 10)
        a.axis("off")
        a.add_patch(FancyBboxPatch((0.2, 0.2), 9.6, 9.4, boxstyle="round,pad=0.02,rounding_size=0.35",
                                   facecolor="#FAFAFA", edgecolor=MID_GRAY, lw=1.1))

    # Panel 1: Compass & Canyon Sightline
    ax0 = axes[0]
    ax0.text(5.0, 8.95, "1. The Compass & Canyon", ha="center", fontweight="bold", fontsize=8.8, color=INK)
    ox, oy = 2.4, 2.2
    draw_arrow(ax0, ox, oy, ox, 7.6, lw=1.4, color=SLATE)
    draw_arrow(ax0, ox, oy, 8.6, oy, lw=1.4, color=SLATE)
    ax0.text(ox, 8.0, "True North (0°)", ha="center", fontsize=7.6, fontweight="bold")
    ax0.text(8.8, oy, "E (90°)", ha="left", va="center", fontsize=7.5)
    tx, ty = 7.8, 6.2
    ax0.plot([ox, tx], [oy, ty], color=INK, lw=2.0)
    ax0.plot([ox, tx], [ty, ty], color=SLATE, lw=1.1, ls="--")
    ax0.plot([tx, tx], [oy, ty], color=SLATE, lw=1.1, ls="--")
    ax0.scatter([ox, tx], [oy, ty], color=INK, s=28, zorder=5)
    ax0.add_patch(Arc((ox, oy), 2.8, 2.8, angle=0, theta1=36.5, theta2=90, color=INK, lw=1.3))
    ax0.text(3.65, 3.85, r"$\alpha=53^\circ$", fontsize=7.8, fontweight="bold")
    ax0.text(5.1, 4.75, r"$D=500\;\mathrm{ft}$", fontsize=7.8, fontweight="bold", rotation=34, ha="center")
    ax0.text(5.0, 0.85, r"$\Delta N = D\cos\alpha,\;\Delta E = D\sin\alpha$", ha="center", fontsize=7.6, fontweight="bold")

    # Panel 2: Pipefitter's 30° Conduit Bend
    ax1 = axes[1]
    ax1.text(5.0, 8.95, "2. The 30° Conduit Offset", ha="center", fontweight="bold", fontsize=8.8, color=INK)
    ax1.add_patch(Rectangle((5.8, 2.2), 2.6, 2.6, facecolor=LIGHT_GRAY, edgecolor=INK, lw=1.2))
    ax1.text(7.1, 3.5, "Steel\nBeam\n6 in", ha="center", va="center", fontsize=7.4, fontweight="bold")
    ax1.plot([0.8, 2.6, 6.2, 9.0], [2.2, 2.2, 4.9, 4.9], color=INK, lw=2.6)
    ax1.plot([2.6, 6.2], [2.2, 2.2], color=SLATE, lw=1.1, ls="--")
    ax1.scatter([2.6, 6.2], [2.2, 4.9], color=INK, s=26, zorder=5)
    ax1.text(3.7, 2.65, r"$\theta=30^\circ$", fontsize=7.6, fontweight="bold")
    ax1.text(4.1, 4.15, r"Travel $T = 12\;\mathrm{in}$", fontsize=7.8, fontweight="bold", rotation=35, ha="center")
    ax1.text(5.0, 0.85, r"$T = O / \sin 30^\circ = 2 \times O$", ha="center", fontsize=7.6, fontweight="bold")

    # Panel 3: Baker's Mixer Heat Balance
    ax2 = axes[2]
    ax2.text(5.0, 8.95, "3. The Baker's Heat Balance", ha="center", fontweight="bold", fontsize=8.8, color=INK)
    draw_box(ax2, 0.9, 6.3, 3.8, 1.6, "Room + Flour", "22°C + 20°C", bg=SOFT_BG, fontsize=7.6, radius=0.18)
    draw_box(ax2, 5.3, 6.3, 3.8, 1.6, "Mixer Friction", "+18°C Heat", bg=LIGHT_GRAY, fontsize=7.6, radius=0.18)
    draw_arrow(ax2, 2.8, 6.2, 4.4, 4.5, lw=1.3)
    draw_arrow(ax2, 7.2, 6.2, 5.6, 4.5, lw=1.3)
    draw_box(ax2, 1.5, 2.4, 7.0, 2.0, "Target Dough: 24°C", "Requires 12°C Chilled Water", bg=MID_GRAY, fontsize=7.8, radius=0.2)
    ax2.text(5.0, 0.85, r"$T_w = 3\,T_{\mathrm{dough}} - (T_r + T_f + F)$", ha="center", fontsize=7.5, fontweight="bold")

    save_fig(fig, "diagram_intro_problems.png")

    # 1. Forward Pipeline vs. Backward Design (Harbor Crane Wire Example)
    fig, ax = new_canvas(6.4, 2.45, (0, 10), (0, 3.9))
    ax.text(5.0, 3.62, "Two Ways Field Engineers Use the Same Physical Law (240 V Feeder, #10 AWG Copper)",
            ha="center", fontweight="bold", fontsize=9.2, color=INK)
    # Top row: Forward Pipeline
    draw_box(ax, 0.25, 2.0, 2.7, 1.25, "Known Field Inputs",
             "Current I = 24 A\nRun L = 150 ft (#10 AWG)", bg=SOFT_BG, fontsize=8.4)
    draw_arrow(ax, 3.0, 2.62, 3.65, 2.62, label="Forward", label_offset=(0, 0.24), lw=1.6)
    draw_box(ax, 3.7, 2.0, 3.0, 1.25, "Physical Wire Law",
             r"$V_{\mathrm{drop}} = 2 \times R \times L \times I / 1000$" "\n" r"($R = 1.24\;\Omega/\mathrm{kft}$)", bg="#FFFFFF", fontsize=8.3)
    draw_arrow(ax, 6.75, 2.62, 7.35, 2.62, lw=1.6)
    draw_box(ax, 7.4, 2.0, 2.35, 1.25, "Result on Stack",
             "Drop = 8.928 V\n(3.72% > 3% limit!)", bg=LIGHT_GRAY, fontsize=8.4)

    # Bottom row: Backward Solver Design
    draw_box(ax, 7.4, 0.3, 2.35, 1.25, "Safety Code Limit",
             "Max 3.0% of 240 V\nD = 7.20 V allowed", bg=SOFT_BG, fontsize=8.4)
    draw_arrow(ax, 7.35, 0.92, 6.75, 0.92, label="Backward", label_offset=(0, 0.24), lw=1.6)
    draw_box(ax, 3.7, 0.3, 3.0, 1.25, "Equation Solver [AWG]",
             "Store D = 7.20, I = 24\nPress [SOLVE] [L]", bg="#FFFFFF", fontsize=8.4)
    draw_arrow(ax, 3.65, 0.92, 3.0, 0.92, lw=1.6)
    draw_box(ax, 0.25, 0.3, 2.7, 1.25, "Solved Design Limit",
             "Max Safe Run:\nL = 120.97 ft", bg=MID_GRAY, fontsize=8.5)
    save_fig(fig, "diagram_intro_pipeline.png")

    # 2. 4-Register RPN Stack (Visual Inside-Out Evaluation)
    fig, ax = new_canvas(6.4, 2.4, (0, 10), (0, 3.8))
    regs = [
        ("Register T (Top)", "Holds earlier subtotals or 4th-level physical arguments", "#F9FAFB", 2.75),
        ("Register Z", "Stages 3rd argument (e.g., Load Current I = 24 A)", SOFT_BG, 1.90),
        ("Register Y", "Stages 2nd argument (e.g., One-Way Run L = 150 ft)", LIGHT_GRAY, 1.05),
        ("Register X (Active)", "Live entry & immediate result (e.g., Gauge 10 -> 8.928 V drop)", MID_GRAY, 0.20),
    ]
    for title, desc, bg, y in regs:
        draw_box(ax, 0.4, y, 2.5, 0.72, title, bg=bg, fontsize=9.0, radius=0.06)
        draw_box(ax, 3.0, y, 6.6, 0.72, desc, bg="#FFFFFF", bold=False, fontsize=8.8, radius=0.06)
    save_fig(fig, "diagram_intro_stack.png")


# ===========================================================================
# CHAPTER 01: GEOMATICS & NAVIGATION
# ===========================================================================
def gen_ch01():
    # 1. Slope reduction
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 4.0))
    A = (1.5, 0.8)
    B = (7.8, 0.8)
    C = (7.8, 3.3)
    ax.fill([A[0], B[0], C[0]], [A[1], B[1], C[1]], color=SOFT_BG, zorder=1)
    ax.plot([A[0], B[0]], [A[1], B[1]], color=INK, lw=2.0)
    ax.plot([B[0], C[0]], [B[1], C[1]], color=INK, lw=2.0, ls="--")
    ax.plot([A[0], C[0]], [A[1], C[1]], color=INK, lw=2.2)
    right_angle_mark(ax, B[0], B[1], -1, 0, 0, 1, 0.3)
    arc = Arc(A, 2.2, 2.2, angle=0, theta1=0, theta2=21.6, color=INK, lw=1.4)
    ax.add_patch(arc)
    ax.text(2.85, 1.08, r"Zenith / Vertical Angle $v$", fontsize=9.0)
    ax.scatter([A[0], C[0]], [A[1], C[1]], color=INK, s=45, zorder=5)
    ax.text(A[0], A[1] + 0.32, "Total Station\nInstrument", ha="center", fontweight="bold", fontsize=8.8)
    ax.text(C[0], C[1] + 0.25, "Reflector Prism", ha="center", fontweight="bold")
    ax.text(4.3, 2.35, r"Slope Distance $S$", ha="center", fontweight="bold", rotation=20)
    ax.text(4.65, 0.35, r"Horizontal Ground Distance $H = S \cos(v)$", ha="center", fontweight="bold")
    ax.text(8.0, 2.05, r"Vertical Rise" "\n" r"$V = S \sin(v)$", ha="left", va="center", fontweight="bold")
    save_fig(fig, "diagram_ch01_slope.png")

    # 2. Forward COGO
    fig, ax = new_canvas(6.4, 2.7, (0, 10), (0, 4.2))
    ox, oy = 2.4, 0.85
    draw_arrow(ax, ox, oy - 0.2, ox, 3.85, lw=1.6)
    draw_arrow(ax, ox - 0.2, oy, 8.6, oy, lw=1.6)
    ax.text(ox, 3.98, r"True / Grid North ($0^\circ$ Azimuth)", ha="center", fontweight="bold")
    ax.text(8.7, oy, r"East ($90^\circ$)", va="center", fontweight="bold")
    bx, by = 6.8, 3.2
    ax.fill([ox, bx, bx], [oy, oy, by], color=SOFT_BG, zorder=1)
    draw_arrow(ax, ox, oy, bx, by, lw=2.2)
    ax.plot([bx, bx], [oy, by], color=INK, lw=1.6, ls="--")
    ax.plot([ox, bx], [oy, oy], color=INK, lw=2.0)
    right_angle_mark(ax, bx, oy, -1, 0, 0, 1, 0.28)
    arc = Arc((ox, oy), 2.1, 2.1, angle=0, theta1=28.0, theta2=90, color=INK, lw=1.5)
    ax.add_patch(arc)
    ax.text(ox + 0.58, oy + 1.15, r"Azimuth $\alpha$", fontweight="bold")
    ax.scatter([ox, bx], [oy, by], color=INK, s=45, zorder=5)
    ax.text(ox - 0.15, oy - 0.35, r"Station A $(N_A, E_A)$", ha="right", fontweight="bold")
    ax.text(bx + 0.15, by + 0.18, r"Station B $(N_B, E_B)$", fontweight="bold")
    ax.text(4.3, 2.32, r"Distance $D$", fontweight="bold", rotation=26)
    ax.text(4.7, 0.42, r"Departure $\Delta E = D \sin(\alpha)$", ha="center", fontweight="bold")
    ax.text(7.0, 2.0, r"Latitude" "\n" r"$\Delta N = D \cos(\alpha)$", va="center", fontweight="bold")
    save_fig(fig, "diagram_ch01_fwd_cogo.png")

    # 3. Quadrant Bearings
    fig, ax = new_canvas(6.4, 2.8, (0, 10), (0, 4.4))
    cx, cy = 5.0, 2.2
    draw_arrow(ax, cx, 0.25, cx, 4.15, lw=1.6, style="<->")
    draw_arrow(ax, 1.5, cy, 8.5, cy, lw=1.6, style="<->")
    ax.text(cx, 4.25, r"North ($0^\circ / 360^\circ$)", ha="center", fontweight="bold")
    ax.text(cx, 0.05, r"South ($180^\circ$)", ha="center", fontweight="bold")
    ax.text(8.65, cy, r"East ($90^\circ$)", va="center", fontweight="bold")
    ax.text(1.35, cy, r"West ($270^\circ$)", va="center", ha="right", fontweight="bold")
    for ang, lbl, qlbl, tx, ty in [
        (52, r"$\mathrm{N}\;\theta\;\mathrm{E}$" "\n" r"($\theta = \alpha$)", "Quadrant I (NE)", 6.9, 3.45),
        (-42, r"$\mathrm{S}\;\theta\;\mathrm{E}$" "\n" r"($\theta = 180^\circ-\alpha$)", "Quadrant II (SE)", 6.9, 0.95),
        (-138, r"$\mathrm{S}\;\theta\;\mathrm{W}$" "\n" r"($\theta = \alpha-180^\circ$)", "Quadrant III (SW)", 3.1, 0.95),
        (132, r"$\mathrm{N}\;\theta\;\mathrm{W}$" "\n" r"($\theta = 360^\circ-\alpha$)", "Quadrant IV (NW)", 3.1, 3.45),
    ]:
        rad = math.radians(ang)
        draw_arrow(ax, cx, cy, cx + 1.65 * math.cos(rad), cy + 1.65 * math.sin(rad), lw=1.5, color=SLATE)
        ax.text(tx, ty, qlbl + "\n" + lbl, ha="center", va="center", fontsize=8.5,
                bbox=dict(boxstyle="round,pad=0.22", facecolor=SOFT_BG, edgecolor=MID_GRAY))
    save_fig(fig, "diagram_ch01_quadrant_bearings.png")

    # 4. Polygon Traverse & Misclosure
    fig, ax = new_canvas(6.4, 2.6, (0, 10), (0, 4.0))
    pts = [(1.6, 0.9), (3.8, 3.3), (7.6, 2.7), (6.5, 0.85), (2.25, 1.15)]
    poly = Polygon(pts[:4], closed=True, facecolor=SOFT_BG, edgecolor="none")
    ax.add_patch(poly)
    labels = [
        r"POB $(N_1, E_1)$", r"Vertex 2 $(N_2, E_2)$",
        r"Vertex 3 $(N_3, E_3)$", r"Vertex 4 $(N_4, E_4)$"
    ]
    for i in range(3):
        draw_arrow(ax, pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1],
                   label=f"Leg {i+1}", label_offset=(0, 0.22), lw=1.8)
    draw_arrow(ax, pts[3][0], pts[3][1], pts[4][0], pts[4][1],
               label="Leg 4", label_offset=(0, -0.25), lw=1.8)
    # Misclosure gap
    draw_arrow(ax, pts[4][0], pts[4][1], pts[0][0], pts[0][1], lw=1.8, color=INK, style="<->")
    ax.scatter([p[0] for p in pts], [p[1] for p in pts], color=INK, s=40, zorder=5)
    ax.text(pts[0][0] - 0.1, pts[0][1] - 0.38, labels[0], fontweight="bold")
    ax.text(pts[1][0], pts[1][1] + 0.25, labels[1], ha="center", fontweight="bold")
    ax.text(pts[2][0] + 0.15, pts[2][1] + 0.15, labels[2], fontweight="bold")
    ax.text(pts[3][0] + 0.2, pts[3][1] - 0.15, labels[3], fontweight="bold")
    ax.text(1.9, 1.65, r"Linear Misclosure $c = \sqrt{(\Sigma\Delta N)^2 + (\Sigma\Delta E)^2}$",
            fontsize=8.5, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#FFFFFF", edgecolor=INK))
    save_fig(fig, "diagram_ch01_polygon_traverse.png")

    # 5. Horizontal Curve (HCRV)
    fig, ax = new_canvas(6.4, 2.8, (0, 10), (0, 4.4))
    cx, cy, R = 5.0, 0.35, 2.7
    pc = (cx - R * math.sin(math.radians(40)), cy + R * math.cos(math.radians(40)))
    pt = (cx + R * math.sin(math.radians(40)), cy + R * math.cos(math.radians(40)))
    pi = (cx, cy + R / math.cos(math.radians(40)))
    ax.plot([cx, pc[0]], [cy, pc[1]], color=SLATE, lw=1.3, ls="--")
    ax.plot([cx, pt[0]], [cy, pt[1]], color=SLATE, lw=1.3, ls="--")
    ax.plot([pc[0], pi[0], pt[0]], [pc[1], pi[1], pt[1]], color=INK, lw=1.6, ls="-.")
    ax.plot([pc[0], pt[0]], [pc[1], pt[1]], color=SLATE, lw=1.4, ls=":")
    curve_arc = Arc((cx, cy), 2 * R, 2 * R, angle=0, theta1=50, theta2=130, color=INK, lw=2.4)
    ax.add_patch(curve_arc)
    ax.plot([cx, cx], [cy, pi[1]], color=MUTED, lw=1.0, ls=":")
    ax.scatter([cx, pc[0], pt[0], pi[0]], [cy, pc[1], pt[1], pi[1]], color=INK, s=42, zorder=5)
    ax.text(cx + 0.15, cy + 0.05, r"Center $O$ (Angle $\Delta$)", fontweight="bold")
    ax.text(pc[0] - 0.2, pc[1] + 0.05, "PC", ha="right", fontweight="bold")
    ax.text(pt[0] + 0.2, pt[1] + 0.05, "PT", ha="left", fontweight="bold")
    ax.text(pi[0], pi[1] + 0.22, r"PI (Deflection $\Delta$)", ha="center", fontweight="bold")
    ax.text(3.35, 3.05, r"Tangent $T = R\tan(\Delta/2)$", rotation=38, fontsize=8.4, ha="center")
    ax.text(5.0, 2.75, r"Arc $L = R\Delta$", ha="center", fontweight="bold")
    ax.text(5.0, 2.15, r"Long Chord $LC = 2R\sin(\Delta/2)$", ha="center", fontsize=8.5)
    ax.text(3.6, 1.25, r"Radius $R$", rotation=50, fontsize=8.8)
    ax.text(5.12, 3.35, r"$E$", fontweight="bold", fontsize=8.6)
    ax.text(5.12, 2.52, r"$M$", fontweight="bold", fontsize=8.6)
    save_fig(fig, "diagram_ch01_horiz_curve.png")

    # 6. Differential Spirit Leveling
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.8))
    gx = np.linspace(0.5, 9.5, 200)
    gy = 0.65 + 0.45 * (1 / (1 + np.exp(-(gx - 5.2) * 1.3)))
    ax.fill_between(gx, 0.1, gy, color=LIGHT_GRAY, edgecolor=INK, lw=1.4)
    bm_x, bm_y = 1.6, 0.66
    tp_x, tp_y = 8.3, 1.09
    hi_y = 2.85
    # Rods
    ax.plot([bm_x, bm_x], [bm_y, hi_y + 0.3], color=INK, lw=3.0)
    ax.plot([tp_x, tp_x], [tp_y, hi_y + 0.3], color=INK, lw=3.0)
    # Level instrument
    inst_x = 4.9
    ax.plot([inst_x - 0.35, inst_x, inst_x + 0.35], [0.85, hi_y, 0.85], color=INK, lw=1.6)
    # Sightline (interrupted across the Level box)
    ax.plot([bm_x, inst_x - 0.48], [hi_y, hi_y], color=INK, lw=1.6, ls="--")
    ax.plot([inst_x + 0.48, tp_x], [hi_y, hi_y], color=INK, lw=1.6, ls="--")
    draw_box(ax, inst_x - 0.45, hi_y - 0.15, 0.9, 0.30, "Level", bg=MID_GRAY, fontsize=8.2)
    ax.text(5.0, hi_y + 0.32, r"Optical Line of Sight: $\mathrm{HI} = E_{\mathrm{BM}} + \mathrm{BS}$",
            ha="center", fontweight="bold")
    draw_arrow(ax, bm_x + 0.25, bm_y, bm_x + 0.25, hi_y, label=r"Backsight $+BS$", label_offset=(0.95, 0), style="<->")
    draw_arrow(ax, tp_x - 0.25, tp_y, tp_x - 0.25, hi_y, label=r"Foresight $-FS$", label_offset=(-0.95, 0), style="<->")
    ax.text(bm_x, bm_y - 0.35, r"Benchmark $E_{\mathrm{BM}}$", ha="center", fontweight="bold")
    ax.text(tp_x, tp_y - 0.35, r"New Station $E_{\mathrm{new}} = \mathrm{HI} - \mathrm{FS}$", ha="center", fontweight="bold")
    save_fig(fig, "diagram_ch01_spirit_leveling.png")

    # 7. Wind Triangle
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.9))
    ox, oy = 2.5, 0.65
    # Runway axis
    ax.fill([ox - 0.25, ox + 0.25, ox + 0.25, ox - 0.25], [0.25, 0.25, 3.55, 3.55], color=LIGHT_GRAY, edgecolor=SLATE, ls=":")
    draw_arrow(ax, ox, oy, ox, 3.5, lw=2.0)
    ax.text(ox, 3.65, r"Runway / True Course ($\psi_{\mathrm{rwy}}$)", ha="center", fontweight="bold")
    wx, wy = 6.5, 2.85
    draw_arrow(ax, ox, oy, wx, wy, lw=2.2)
    draw_arrow(ax, ox, oy, wx, oy, lw=1.8, style="-|>")
    ax.plot([wx, wx], [oy, wy], color=INK, lw=1.5, ls="--")
    ax.plot([ox, wx], [wy, wy], color=INK, lw=1.5, ls="--")
    right_angle_mark(ax, wx, oy, -1, 0, 0, 1, 0.25)
    arc = Arc((ox, oy), 1.9, 1.9, angle=0, theta1=29, theta2=90, color=INK, lw=1.4)
    ax.add_patch(arc)
    ax.text(ox + 0.52, oy + 1.05, r"$\Delta\psi$", fontweight="bold")
    ax.text(4.2, 2.05, r"Wind Vector $V_{\mathrm{wind}}$", rotation=28, fontweight="bold")
    ax.text(4.5, 0.25, r"Crosswind $V_{\mathrm{xw}} = V_{\mathrm{wind}}\sin(\Delta\psi)$", ha="center", fontweight="bold")
    ax.text(6.75, 1.75, r"Headwind Component" "\n" r"$V_{\mathrm{hw}} = V_{\mathrm{wind}}\cos(\Delta\psi)$", va="center", fontweight="bold")
    save_fig(fig, "diagram_ch01_wind_triangle.png")


# ===========================================================================
# CHAPTER 02: ELECTRICAL TRADES & INDUSTRIAL MANUFACTURING
# ===========================================================================
def gen_ch02():
    # 1. Voltage Drop 2-wire loop
    fig, ax = new_canvas(6.4, 2.3, (0, 10), (0, 3.6))
    draw_box(ax, 0.3, 0.6, 1.65, 2.4, "Panel Source", r"$V_{\mathrm{source}}$", bg=SOFT_BG)
    draw_box(ax, 8.05, 0.6, 1.65, 2.4, "Field Load", r"$V_{\mathrm{load}} = V_S - V_{\mathrm{drop}}$", bg=LIGHT_GRAY)
    ax.plot([1.95, 3.15], [2.5, 2.5], color=INK, lw=1.8)
    draw_box(ax, 3.15, 2.2, 3.7, 0.6, r"Hot Conductor: $R_{\mathrm{line}} = R \cdot L / 1000$", bg="#FFFFFF", fontsize=8.5)
    ax.plot([6.85, 8.05], [2.5, 2.5], color=INK, lw=1.8)
    ax.plot([1.95, 3.15], [1.1, 1.1], color=INK, lw=1.8)
    draw_box(ax, 3.15, 0.8, 3.7, 0.6, r"Return Neutral: $R_{\mathrm{ret}} = R \cdot L / 1000$", bg="#FFFFFF", fontsize=8.5)
    ax.plot([6.85, 8.05], [1.1, 1.1], color=INK, lw=1.8)
    draw_arrow(ax, 2.1, 2.75, 3.0, 2.75, label=r"Current $I$", label_offset=(0, 0.2))
    draw_arrow(ax, 3.0, 0.85, 2.1, 0.85, label=r"Return $I$", label_offset=(0, -0.28))
    ax.text(5.0, 1.65, r"One-Way Distance $L$ ft  $\Longrightarrow$  Round-Trip Loop $= 2L$ ft",
            ha="center", fontsize=8.8, fontweight="bold")
    save_fig(fig, "diagram_ch02_voltage_drop.png")

    # 2. AC Power Triangle
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.9))
    A, B, C = (1.8, 0.8), (7.6, 0.8), (7.6, 3.25)
    ax.fill([A[0], B[0], C[0]], [A[1], B[1], C[1]], color=SOFT_BG)
    draw_arrow(ax, A[0], A[1], B[0], B[1], lw=2.0)
    draw_arrow(ax, B[0], B[1], C[0], C[1], lw=2.0)
    draw_arrow(ax, A[0], A[1], C[0], C[1], lw=2.2)
    right_angle_mark(ax, B[0], B[1], -1, 0, 0, 1, 0.28)
    arc = Arc(A, 2.2, 2.2, angle=0, theta1=0, theta2=22.9, color=INK, lw=1.4)
    ax.add_patch(arc)
    ax.text(3.2, 1.08, r"Phase Angle $\varphi$", fontweight="bold")
    ax.text(4.7, 0.35, r"Real Working Power $P = V I \cos\varphi = S \cdot \mathrm{PF}$ [W / kW]", ha="center", fontweight="bold")
    ax.text(4.3, 2.35, r"Apparent Power $S = V I$ [VA / kVA]", rotation=22.5, ha="center", fontweight="bold")
    ax.text(7.8, 2.0, r"Reactive Power" "\n" r"$Q = V I \sin\varphi$" "\n" "[VAR / kVAR]", va="center", fontweight="bold")
    save_fig(fig, "diagram_ch02_power_triangle.png")

    # 3. 3-Phase Phasor
    fig, ax = new_canvas(6.4, 2.7, (0, 10), (0, 4.2))
    cx, cy, r = 3.2, 2.1, 1.6
    angles = [(90, r"$V_{AN}$ ($0^\circ$)"), (-30, r"$V_{BN}$ ($-120^\circ$)"), (210, r"$V_{CN}$ ($+120^\circ$)")]
    pts = []
    for ang, lbl in angles:
        rad = math.radians(ang)
        px, py = cx + r * math.cos(rad), cy + r * math.sin(rad)
        pts.append((px, py))
        draw_arrow(ax, cx, cy, px, py, lw=2.0)
    ax.text(pts[0][0], pts[0][1] + 0.18, angles[0][1], ha="center", fontweight="bold")
    ax.text(pts[1][0], pts[1][1] - 0.32, angles[1][1], ha="center", fontweight="bold")
    ax.text(pts[2][0] - 0.15, pts[2][1] - 0.1, angles[2][1], ha="right", fontweight="bold")
    draw_arrow(ax, pts[1][0], pts[1][1], pts[0][0], pts[0][1], lw=1.8, color=SLATE, style="<->")
    ax.add_patch(Arc((cx, cy), 0.9, 0.9, angle=0, theta1=-30, theta2=90, color=INK, lw=1.2))
    ax.text(cx + 0.55, cy + 0.25, r"$120^\circ$", fontsize=8.8, fontweight="bold")
    ax.text(cx - 0.15, cy - 0.25, "N", fontweight="bold")
    draw_box(ax, 5.75, 1.15, 3.95, 1.9, "Line-to-Line Phasor Law",
             r"$V_{AB} = 2 V_{LN} \sin(60^\circ) = \sqrt{3}\,V_{LN}$" "\n"
             r"$120\;\mathrm{V} \times \sqrt{3} = 207.8\;\mathrm{V} \approx 208\;\mathrm{V}$" "\n"
             r"$277\;\mathrm{V} \times \sqrt{3} = 479.8\;\mathrm{V} \approx 480\;\mathrm{V}$", bg=SOFT_BG, fontsize=8.8)
    save_fig(fig, "diagram_ch02_three_phase_phasor.png")

    # 4. Conduit Offset Bend
    fig, ax = new_canvas(6.4, 2.4, (0, 10), (0, 3.8))
    ax.fill([6.2, 9.2, 9.2, 6.2], [0.4, 0.4, 2.2, 2.2], color=LIGHT_GRAY, edgecolor=INK, lw=1.3)
    ax.text(7.7, 1.3, "Structural\nObstruction", ha="center", va="center", fontweight="bold")
    # Conduit path
    ax.plot([0.6, 3.2, 5.7, 9.3], [0.65, 0.65, 2.45, 2.45], color=INK, lw=4.0)
    ax.plot([3.2, 5.7], [0.65, 0.65], color=SLATE, lw=1.3, ls="--")
    ax.plot([5.7, 5.7], [0.65, 2.45], color=SLATE, lw=1.3, ls="--")
    ax.scatter([3.2, 5.7], [0.65, 2.45], color="#FFFFFF", edgecolor=INK, s=55, zorder=5, lw=1.8)
    ax.add_patch(Arc((3.2, 0.65), 1.4, 1.4, angle=0, theta1=0, theta2=35.8, color=INK, lw=1.4))
    ax.text(4.1, 0.88, r"$\theta$", fontweight="bold")
    ax.text(3.2, 0.25, "Bend Mark 1", ha="center", fontweight="bold")
    ax.text(5.7, 2.8, "Bend Mark 2", ha="center", fontweight="bold")
    ax.text(3.95, 1.75, r"Travel $T = O / \sin\theta$", rotation=35, ha="center", fontweight="bold")
    draw_arrow(ax, 5.95, 0.65, 5.95, 2.45, label=r"Offset $O$", label_offset=(0.55, 0), style="<->")
    ax.text(2.4, 3.1, r"Shrinkage $\Delta S = O\csc\theta - O\cot\theta = O\tan(\theta/2)$", ha="center",
            bbox=dict(boxstyle="round,pad=0.22", facecolor=SOFT_BG, edgecolor=MID_GRAY), fontsize=8.6)
    save_fig(fig, "diagram_ch02_conduit_offset.png")

    # 5. Three-Point Saddle Bend
    fig, ax = new_canvas(6.4, 2.3, (0, 10), (0, 3.6))
    ax.add_patch(Circle((5.0, 0.95), 0.55, facecolor=MID_GRAY, edgecolor=INK, lw=1.5))
    ax.text(5.0, 0.95, "Pipe", ha="center", va="center", fontsize=8.5, fontweight="bold")
    ax.plot([0.7, 2.8, 5.0, 7.2, 9.3], [0.7, 0.7, 2.15, 0.7, 0.7], color=INK, lw=3.8)
    for x, y, lbl in [(2.8, 0.7, r"Outer $22.5^\circ$"), (5.0, 2.15, r"Center $45^\circ$"), (7.2, 0.7, r"Outer $22.5^\circ$")]:
        ax.scatter([x], [y], color="#FFFFFF", edgecolor=INK, s=55, zorder=5, lw=1.8)
    ax.text(2.8, 0.28, r"Outer Mark ($\theta/2 = 22.5^\circ$)", ha="center", fontweight="bold")
    ax.text(7.2, 0.28, r"Outer Mark ($\theta/2 = 22.5^\circ$)", ha="center", fontweight="bold")
    ax.text(5.0, 2.65, r"Center Apex ($\theta = 45^\circ$)", ha="center", fontweight="bold")
    ax.text(3.35, 1.65, r"$T = O / \sin 22.5^\circ$", rotation=33, ha="center", fontsize=8.5, fontweight="bold")
    ax.text(6.65, 1.65, r"$T = O / \sin 22.5^\circ$", rotation=-33, ha="center", fontsize=8.5, fontweight="bold")
    save_fig(fig, "diagram_ch02_saddle_bend.png")

    # 6. Machining SFM & RPM
    fig, ax = new_canvas(6.4, 2.4, (0, 10), (0, 3.8))
    cx, cy, r = 3.0, 2.2, 1.15
    ax.add_patch(Circle((cx, cy), r, facecolor=SOFT_BG, edgecolor=INK, lw=2.0))
    ax.add_patch(Circle((cx, cy), 0.18, facecolor="#FFFFFF", edgecolor=INK, lw=1.4))
    for k in range(8):
        ang = math.radians(k * 45)
        ax.plot([cx + r * math.cos(ang), cx + (r + 0.14) * math.cos(ang + 0.12)],
                [cy + r * math.sin(ang), cy + (r + 0.14) * math.sin(ang + 0.12)], color=INK, lw=1.8)
    draw_arrow(ax, cx - r, cy - 0.35, cx + r, cy - 0.35, label=r"Diameter $D$ (in)", label_offset=(0, -0.25), style="<->")
    ax.add_patch(Arc((cx, cy), 1.35, 1.35, angle=0, theta1=35, theta2=145, color=INK, lw=1.4))
    ax.text(cx, cy + 0.45, r"Spindle $N$ (RPM)", ha="center", fontsize=8.5, fontweight="bold")
    # Workpiece
    ax.fill([0.6, 9.2, 9.2, 0.6], [0.2, 0.2, 0.88, 0.88], color=LIGHT_GRAY, edgecolor=INK, lw=1.4)
    draw_arrow(ax, 3.0, 0.54, 6.2, 0.54, label=r"Tangential Velocity $V = \mathrm{SFM}$ (ft/min)", label_offset=(0, 0.18), lw=1.8)
    draw_box(ax, 5.2, 1.55, 4.4, 1.75, "Rotary Cutting Kinematics",
             r"Circumference $C = \pi D / 12\;\mathrm{ft}$" "\n"
             r"$\mathrm{SFM} = \pi D N / 12 \approx 0.2618\,D\,N$" "\n"
             r"$N = 12\,\mathrm{SFM} / (\pi D) \approx 3.8197\,\mathrm{SFM}/D$", bg="#FFFFFF", fontsize=8.8)
    save_fig(fig, "diagram_ch02_machining_sfm.png")

    # 7. Bolt Circle
    fig, ax = new_canvas(6.4, 2.6, (0, 10), (0, 4.0))
    cx, cy, r = 2.8, 2.0, 1.5
    ax.add_patch(Circle((cx, cy), r, facecolor="none", edgecolor=SLATE, lw=1.4, ls="--"))
    ax.scatter([cx], [cy], color=INK, s=30)
    pts = []
    for k in range(6):
        ang = math.radians(k * 60)
        bx, by = cx + r * math.cos(ang), cy + r * math.sin(ang)
        pts.append((bx, by))
        ax.add_patch(Circle((bx, by), 0.16, facecolor=LIGHT_GRAY, edgecolor=INK, lw=1.5, zorder=4))
    ax.plot([cx, pts[0][0]], [cy, pts[0][1]], color=INK, lw=1.6)
    ax.plot([cx, pts[1][0]], [cy, pts[1][1]], color=INK, lw=1.6)
    draw_arrow(ax, pts[0][0], pts[0][1], pts[1][0], pts[1][1], lw=2.0, style="<->")
    ax.add_patch(Arc((cx, cy), 1.0, 1.0, angle=0, theta1=0, theta2=60, color=INK, lw=1.3))
    ax.text(cx + 0.68, cy + 0.28, r"$\theta = 360^\circ/N$", fontsize=8.2, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.1", facecolor="#FFFFFF", edgecolor="none"))
    ax.text(cx + 0.65, cy - 0.22, r"$R = D/2$", fontsize=8.3)
    draw_box(ax, 5.2, 0.75, 4.4, 2.4, "Bolt Circle Layout ([BC])",
             r"• Angular Pitch: $\theta = 360^\circ / N$" "\n"
             r"• Hole Coordinates $(k = 0\dots N-1)$:" "\n"
             r"   $x_k = R\cos(k\theta),\;\; y_k = R\sin(k\theta)$" "\n"
             r"• Adjacent Chord Spacing:" "\n"
             r"   $C = D \sin(180^\circ / N)$", bg=SOFT_BG, fontsize=8.8)
    save_fig(fig, "diagram_ch02_bolt_circle.png")

    # 8. 4-20 mA Loop
    fig, ax = new_canvas(6.4, 2.2, (0, 10), (0, 3.4))
    draw_box(ax, 0.3, 0.6, 2.2, 2.1, "24 V DC Supply", "Loop Power Source", bg=SOFT_BG)
    draw_box(ax, 3.6, 0.6, 2.8, 2.1, "2-Wire Transmitter",
             r"$I(p) = 4.0 + 16.0\,(p/100)\;\mathrm{mA}$" "\n" r"($4\;\mathrm{mA}=0\%,\;20\;\mathrm{mA}=100\%$)", bg="#FFFFFF")
    draw_box(ax, 7.5, 0.6, 2.2, 2.1, r"PLC $250\;\Omega$ Input",
             r"$V = I \cdot 250\;\Omega$" "\n" r"($1.00\;\mathrm{V}$ to $5.00\;\mathrm{V}$)", bg=LIGHT_GRAY)
    draw_arrow(ax, 2.5, 2.15, 3.6, 2.15, label=r"$+24\;\mathrm{V}$", label_offset=(0, 0.22))
    draw_arrow(ax, 6.4, 2.15, 7.5, 2.15, label=r"$I_{\mathrm{loop}}$", label_offset=(0, 0.22))
    ax.plot([8.6, 8.6, 1.4, 1.4], [0.6, 0.2, 0.2, 0.6], color=INK, lw=1.6)
    draw_arrow(ax, 5.5, 0.2, 4.5, 0.2, label="Common Return Loop", label_offset=(0, 0.2))
    save_fig(fig, "diagram_ch02_current_loop.png")


# ===========================================================================
# CHAPTER 03: SYSTEMS & CYBERSECURITY
# ===========================================================================
def gen_ch03():
    # 1. 16-bit Hex Nibbles
    fig, ax = new_canvas(6.4, 2.2, (0, 10), (0, 3.4))
    ax.text(5.0, 3.05, r"16-Bit Register ($\mathrm{WSZ}=16$):  Hex $\mathtt{0x4A3F} = 19{,}007_{10}$",
            ha="center", fontweight="bold", fontsize=10.0)
    nibbles = [
        ("Nibble 3 (Bits 15..12)", ["0", "1", "0", "0"], "Hex '4'  (4 × 4096)", 0.3),
        ("Nibble 2 (Bits 11..8)", ["1", "0", "1", "0"], "Hex 'A'  (10 × 256)", 2.7),
        ("Nibble 1 (Bits 7..4)", ["0", "0", "1", "1"], "Hex '3'  (3 × 16)", 5.1),
        ("Nibble 0 (Bits 3..0)", ["1", "1", "1", "1"], "Hex 'F'  (15 × 1)", 7.5),
    ]
    for title, bits, sub, x0 in nibbles:
        ax.text(x0 + 1.1, 2.45, title, ha="center", fontsize=8.0, color=SLATE, fontweight="bold")
        for j, b in enumerate(bits):
            bg = LIGHT_GRAY if b == "1" else "#FFFFFF"
            draw_box(ax, x0 + j * 0.55, 1.35, 0.52, 0.85, b, bg=bg, radius=0.03)
        draw_box(ax, x0, 0.35, 2.17, 0.72, sub, bg=SOFT_BG, fontsize=8.3, radius=0.05)
    save_fig(fig, "diagram_ch03_hex_nibbles.png")

    # 2. Two's Complement Ring
    fig, ax = new_canvas(6.4, 2.7, (0, 10), (0, 4.2))
    cx, cy, r = 5.0, 2.1, 1.45
    ax.add_patch(Wedge((cx, cy), r, -90, 90, width=0.35, facecolor=SOFT_BG, edgecolor=INK, lw=1.4))
    ax.add_patch(Wedge((cx, cy), r, 90, 270, width=0.35, facecolor=LIGHT_GRAY, edgecolor=INK, lw=1.4))
    ax.plot([cx, cx], [cy - r - 0.25, cy + r + 0.25], color=INK, lw=1.4, ls="--")
    ax.text(cx, cy + r + 0.35, r"$\mathtt{0000\,0000}_2 = 0$", ha="center", fontweight="bold")
    ax.text(cx + 1.55, cy + 1.1, r"$\mathtt{0000\,0001}_2 = +1$", ha="left", fontsize=8.5)
    ax.text(cx - 1.55, cy + 1.1, r"$\mathtt{1111\,1111}_2 = -1$", ha="right", fontsize=8.5)
    ax.text(cx + 1.65, cy, "Positive Half\n" r"($b_7 = 0$)", ha="left", va="center", fontweight="bold")
    ax.text(cx - 1.65, cy, "Negative Half\n" r"($b_7 = 1$)", ha="right", va="center", fontweight="bold")
    ax.text(cx + 1.45, cy - 1.15, r"$\mathtt{0111\,1111}_2 = +127$", ha="left", fontsize=8.5)
    ax.text(cx - 1.45, cy - 1.15, r"$\mathtt{1000\,0000}_2 = -128$", ha="right", fontsize=8.5)
    ax.text(cx, 0.12, "Signed Overflow Discontinuity (OVF)", ha="center", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.18", facecolor="#FFFFFF", edgecolor=INK))
    save_fig(fig, "diagram_ch03_twos_complement_ring.png")

    # 3. Logical vs Arithmetic Shift
    fig, ax = new_canvas(6.4, 2.3, (0, 10), (0, 3.6))
    ax.text(0.4, 3.15, "Logical Shift Right (SHR): Vacated MSB filled with 0", fontweight="bold")
    draw_box(ax, 0.4, 2.15, 0.8, 0.7, "0", bg="#FFFFFF", radius=0.04)
    draw_arrow(ax, 1.25, 2.5, 1.85, 2.5)
    for k in range(8):
        draw_box(ax, 1.9 + k * 0.78, 2.15, 0.74, 0.7, f"b{7-k}", bg=LIGHT_GRAY if k == 0 else SOFT_BG, radius=0.04)
    draw_arrow(ax, 8.2, 2.5, 9.0, 2.5, label="LSB out", label_offset=(0, 0.25))

    ax.text(0.4, 1.45, "Arithmetic Shift Right (ASR): Sign bit b7 replicated into MSB", fontweight="bold")
    for k in range(8):
        draw_box(ax, 1.9 + k * 0.78, 0.45, 0.74, 0.7, f"b{7-k}", bg=MID_GRAY if k == 0 else SOFT_BG, radius=0.04)
    ax.plot([2.27, 2.27, 1.35, 1.35], [1.15, 1.32, 1.32, 0.8], color=INK, lw=1.5)
    draw_arrow(ax, 1.35, 0.8, 1.9, 0.8)
    ax.text(1.0, 0.8, "Sign\nCopy", ha="center", va="center", fontsize=8.2, fontweight="bold")
    draw_arrow(ax, 8.2, 0.8, 9.0, 0.8, label="LSB out", label_offset=(0, 0.25))
    save_fig(fig, "diagram_ch03_bit_shifts.png")

    # 4. Endian Byte Swap
    fig, ax = new_canvas(6.4, 2.2, (0, 10), (0, 3.4))
    ax.text(2.2, 2.95, "Little-Endian Host (x86 / ARM)", ha="center", fontweight="bold")
    ax.text(7.8, 2.95, "Big-Endian Network Order", ha="center", fontweight="bold")
    le = [("0x78", "A+0"), ("0x56", "A+1"), ("0x34", "A+2"), ("0x12", "A+3")]
    be = [("0x12", "A+0"), ("0x34", "A+1"), ("0x56", "A+2"), ("0x78", "A+3")]
    for i, ((v1, a1), (v2, a2)) in enumerate(zip(le, be)):
        bg = MID_GRAY if i in (0, 3) else SOFT_BG
        draw_box(ax, 0.4 + i * 0.92, 1.45, 0.88, 0.95, v1, a1, bg=bg, radius=0.04)
        draw_box(ax, 5.95 + i * 0.92, 1.45, 0.88, 0.95, v2, a2, bg=bg, radius=0.04)
    draw_arrow(ax, 4.25, 1.92, 5.75, 1.92, label="[ SWP ]", label_offset=(0, 0.28), lw=2.0, style="<->")
    ax.text(5.0, 0.55, r"32-Bit Word $\mathtt{0x12345678}$ Reversed Across 4-Byte Lanes", ha="center", fontweight="bold")
    save_fig(fig, "diagram_ch03_endian_swap.png")

    # 5. IEEE-754 Float
    fig, ax = new_canvas(6.4, 2.1, (0, 10), (0, 3.2))
    ax.text(5.0, 2.85, "IEEE-754 Single-Precision Binary32 Word Layout (FLT)", ha="center", fontweight="bold", fontsize=10.0)
    draw_box(ax, 0.4, 1.15, 1.1, 1.15, "Sign S", "Bit 31 (1b)", bg=MID_GRAY, radius=0.05)
    draw_box(ax, 1.6, 1.15, 2.8, 1.15, "Biased Exponent E", "Bits 30..23 (8b, Bias +127)", bg=LIGHT_GRAY, radius=0.05)
    draw_box(ax, 4.5, 1.15, 5.1, 1.15, "Fractional Mantissa M", "Bits 22..0 (23b, Implicit 1.M)", bg=SOFT_BG, radius=0.05)
    ax.text(5.0, 0.45, r"Decoded Value:  $V = (-1)^S \times (1 + M / 2^{23}) \times 2^{E - 127}$", ha="center", fontweight="bold", fontsize=9.8)
    save_fig(fig, "diagram_ch03_ieee754_float.png")

    # 6. PWM Timer
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.9))
    # Sawtooth
    t = np.linspace(0, 7.5, 600)
    saw = (t % 2.5) / 2.5 * 1.4
    ax.plot(1.5 + t, 1.85 + saw, color=INK, lw=1.8)
    ax.plot([1.5, 9.0], [1.85 + 0.84, 1.85 + 0.84], color=SLATE, lw=1.3, ls="--")
    ax.plot([1.5, 9.0], [1.85 + 1.4, 1.85 + 1.4], color=MUTED, lw=1.0, ls=":")
    ax.text(1.35, 3.25, r"$A-1$", ha="right", va="center", fontweight="bold")
    ax.text(1.35, 2.69, r"$\mathrm{CCR}$", ha="right", va="center", fontweight="bold")
    ax.text(1.35, 1.85, "0", ha="right", va="center", fontweight="bold")
    # PWM pulse
    pwm = np.where((t % 2.5) < 1.5, 1.15, 0.45)
    ax.plot(1.5 + t, pwm, color=INK, lw=2.0)
    ax.fill_between(1.5 + t, 0.45, pwm, color=LIGHT_GRAY)
    ax.text(1.35, 0.8, "PWM\nOut", ha="right", va="center", fontweight="bold")
    draw_arrow(ax, 1.5, 0.18, 4.0, 0.18, label=r"$T_{\mathrm{PWM}} = P \cdot A / f_{\mathrm{clk}}$", label_offset=(0, -0.18), style="<->")
    save_fig(fig, "diagram_ch03_pwm_timer.png")

    # 7. CRC-32 LFSR
    fig, ax = new_canvas(6.4, 2.1, (0, 10), (0, 3.2))
    draw_box(ax, 0.3, 1.0, 1.3, 1.0, "Bit Shift\nIn (0)", bg=SOFT_BG)
    draw_box(ax, 2.1, 1.0, 3.3, 1.0, "32-Bit CRC Shift Register", r"$b_{31}\;\dots\;b_1\;b_0$ (SHR 1)", bg="#FFFFFF")
    draw_box(ax, 5.9, 1.0, 1.6, 1.0, "LSB Gate", r"$b_0 == 1\mathrm{?}$", bg=LIGHT_GRAY)
    draw_box(ax, 8.0, 1.0, 1.7, 1.0, "XOR Poly", r"$\mathtt{0xEDB88320}$", bg=MID_GRAY)
    draw_arrow(ax, 1.6, 1.5, 2.1, 1.5)
    draw_arrow(ax, 5.4, 1.5, 5.9, 1.5)
    draw_arrow(ax, 7.5, 1.5, 8.0, 1.5, label="Yes", label_offset=(0, 0.22))
    ax.plot([8.85, 8.85, 3.75, 3.75], [2.0, 2.65, 2.65, 2.0], color=INK, lw=1.5)
    draw_arrow(ax, 3.75, 2.25, 3.75, 2.0)
    ax.text(6.3, 2.82, "Feedback XOR into Register Taps", ha="center", fontsize=8.5, fontweight="bold")
    save_fig(fig, "diagram_ch03_crc32_lfsr.png")

    # 8. CIDR Subnet
    fig, ax = new_canvas(6.4, 2.1, (0, 10), (0, 3.2))
    ax.text(5.0, 2.8, "IPv4 32-Bit Address Space under /26 Prefix (CIDR)", ha="center", fontweight="bold", fontsize=10.0)
    draw_box(ax, 0.5, 1.1, 6.4, 1.15, "Network Prefix (P = 26 bits = 1s)",
             "Mask: 11111111.11111111.11111111.11000000 = 255.255.255.192", bg=LIGHT_GRAY, radius=0.05)
    draw_box(ax, 7.0, 1.1, 2.5, 1.15, "Host Field (H = 6b)",
             r"$2^6 - 2 = 62$ Hosts", bg=SOFT_BG, radius=0.05)
    ax.text(5.0, 0.45, "Total Addresses = 64  |  Network ID (.0)  |  Usable Hosts (.1 to .62)  |  Broadcast (.63)",
            ha="center", fontsize=8.8, fontweight="bold")
    save_fig(fig, "diagram_ch03_cidr_subnet.png")

    # 9. Struct Alignment
    fig, ax = new_canvas(6.4, 2.1, (0, 10), (0, 3.2))
    ax.text(5.0, 2.8, "Hardware 4-Byte Memory Bus Alignment (ALGN)", ha="center", fontweight="bold", fontsize=10.0)
    for k in range(8):
        ax.text(0.75 + k * 1.12, 2.25, f"Byte +{k}", ha="center", fontsize=8.2, color=SLATE, fontweight="bold")
    draw_box(ax, 0.2, 1.0, 1.1, 1.05, "uint8_t", "id (1B)", bg=MID_GRAY, radius=0.04)
    draw_box(ax, 1.32, 1.0, 3.34, 1.05, "3 Padding Bytes (ALGN)", "Inserted to reach Offset +4", bg=SOFT_BG, radius=0.04)
    draw_box(ax, 4.68, 1.0, 4.46, 1.05, "uint32_t timestamp (4 Bytes)", "Aligned to 4-Byte Bus Word", bg=LIGHT_GRAY, radius=0.04)
    ax.text(5.0, 0.42, r"Alignment Formula: $\mathrm{Aligned}(S, A) = \lceil S / A \rceil \times A$", ha="center", fontweight="bold")
    save_fig(fig, "diagram_ch03_struct_alignment.png")


# ===========================================================================
# CHAPTER 04: CINEMA, OPTICS & BROADCAST
# ===========================================================================
def gen_ch04():
    # 1. SMPTE 29.97 Drop Frame
    fig, ax = new_canvas(6.4, 2.3, (0, 10), (0, 3.6))
    draw_box(ax, 0.4, 1.9, 9.2, 1.25, "Regular Minute Rollover (Minutes 01..09, 11..19, ...): Drop Labels :00 and :01",
             r"$\mathtt{00:00:59:28} \;\longrightarrow\; \mathtt{00:00:59:29} \;\longrightarrow\; \mathtt{00:01:00:02}$   (2 frame numbers skipped)", bg=SOFT_BG)
    draw_box(ax, 0.4, 0.35, 9.2, 1.25, "Every Tenth Minute Rollover (Minutes 00, 10, 20, 30, 40, 50): Retain All Labels",
             r"$\mathtt{00:09:59:28} \;\longrightarrow\; \mathtt{00:09:59:29} \;\longrightarrow\; \mathtt{00:10:00:00}$   ($9 \times 2 = 18$ labels dropped / 10 min = 108/hr)", bg=LIGHT_GRAY)
    save_fig(fig, "diagram_ch04_drop_frame.png")

    # 2. Rectilinear Lens FOV
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.9))
    lx, ly = 5.4, 1.95
    ax.plot([0.8, 9.2], [ly, ly], color=MUTED, lw=1.0, ls="-.")
    # Subject plane
    ax.plot([1.4, 1.4], [0.4, 3.5], color=INK, lw=2.2)
    ax.text(1.4, 3.65, "Subject Field", ha="center", fontweight="bold")
    # Optical nodal point
    ax.add_patch(Circle((lx, ly), 0.12, facecolor=INK))
    ax.plot([lx, lx], [0.6, 3.3], color=SLATE, lw=1.8, ls="--")
    ax.text(lx, 3.5, "Lens Nodal\nCenter O", ha="center", fontsize=8.5, fontweight="bold")
    # Sensor plane
    sx = 8.4
    ax.plot([sx, sx], [1.0, 2.9], color=INK, lw=3.0)
    ax.text(sx, 3.25, "Sensor Plane\nWidth W", ha="center", fontsize=8.5, fontweight="bold")
    # Rays
    ax.plot([1.4, sx], [3.4, 1.0], color=INK, lw=1.5)
    ax.plot([1.4, sx], [0.5, 2.9], color=INK, lw=1.5)
    ax.add_patch(Arc((lx, ly), 1.8, 1.8, angle=0, theta1=160, theta2=200, color=INK, lw=1.4))
    ax.text(lx - 1.55, ly, r"$\theta = 2\arctan(W / 2f)$", ha="center", va="center", fontweight="bold", fontsize=8.5,
            bbox=dict(boxstyle="round,pad=0.14", facecolor="#FFFFFF", edgecolor="none"))
    draw_arrow(ax, lx, 0.75, sx, 0.75, label=r"Focal Length $f$", label_offset=(0, -0.22), style="<->")
    draw_arrow(ax, sx + 0.35, ly, sx + 0.35, 2.9, label=r"$W/2$", label_offset=(0.4, 0), style="<->")
    save_fig(fig, "diagram_ch04_lens_fov.png")

    # 3. Circle of Confusion
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.9))
    lx, ly = 3.6, 1.95
    sx = 7.4
    ax.plot([0.8, 9.2], [ly, ly], color=MUTED, lw=1.0, ls="-.")
    # Lens aperture
    ax.plot([lx, lx], [0.4, 1.0], color=INK, lw=3.5)
    ax.plot([lx, lx], [2.9, 3.5], color=INK, lw=3.5)
    ax.text(lx, 3.65, r"Aperture $D = f / N$", ha="center", fontweight="bold")
    # Focused cone (solid)
    ax.plot([1.2, lx, sx], [ly, 2.9, ly], color=INK, lw=1.6)
    ax.plot([1.2, lx, sx], [ly, 1.0, ly], color=INK, lw=1.6)
    # Out-of-focus cone (dashed, converging at x=6.2 and hitting sensor at sx)
    ax.plot([lx, sx], [2.9, 1.55], color=SLATE, lw=1.4, ls="--")
    ax.plot([lx, sx], [1.0, 2.35], color=SLATE, lw=1.4, ls="--")
    # Sensor plane
    ax.plot([sx, sx], [0.5, 3.4], color=INK, lw=2.4)
    ax.plot([sx, sx], [1.55, 2.35], color=INK, lw=5.0)
    draw_arrow(ax, sx + 0.3, 1.55, sx + 0.3, 2.35, label=r"Blur Disk $c$", label_offset=(0.85, 0), style="<->")
    ax.text(1.2, ly + 0.35, "Subject at\nFocus s", ha="center", fontweight="bold", fontsize=8.5,
            bbox=dict(boxstyle="round,pad=0.1", facecolor="#FFFFFF", edgecolor="none"))
    ax.text(sx, 3.58, "Sensor Plane", ha="center", fontweight="bold")
    save_fig(fig, "diagram_ch04_circle_of_confusion.png")

    # 4. Hyperfocal Focus Zone
    fig, ax = new_canvas(6.4, 2.2, (0, 10), (0, 3.4))
    ax.fill([3.4, 9.4, 9.4, 3.4], [1.1, 1.1, 2.25, 2.25], color=LIGHT_GRAY, edgecolor=INK, lw=1.4)
    draw_box(ax, 0.5, 1.15, 1.1, 1.05, "Camera\nLens", bg=MID_GRAY)
    for x, lbl in [(3.4, r"Near Limit $D_{\mathrm{near}} = H/2$"), (5.8, r"Focus Plane $s = H$"), (9.1, r"Far Limit $D_{\mathrm{far}} = \infty$")]:
        ax.plot([x, x], [0.85, 2.5], color=INK, lw=1.8, ls="--" if x != 5.8 else "-")
        ax.text(x, 2.72, lbl, ha="center", fontweight="bold", fontsize=8.6)
    ax.text(6.4, 1.68, r"CONTINUOUS ACCEPTABLE SHARPNESS ZONE ($H/2 \;\longrightarrow\; \infty$)",
            ha="center", va="center", fontweight="bold", fontsize=8.8,
            bbox=dict(boxstyle="round,pad=0.18", facecolor="#FFFFFF", edgecolor=MID_GRAY))
    draw_arrow(ax, 1.6, 0.5, 3.4, 0.5, label=r"$H / 2$", label_offset=(0, -0.22), style="<->")
    draw_arrow(ax, 3.4, 0.5, 5.8, 0.5, label=r"$H / 2$", label_offset=(0, -0.22), style="<->")
    save_fig(fig, "diagram_ch04_hyperfocal_zone.png")

    # 5. Luminaire Beam Spread
    fig, ax = new_canvas(6.4, 2.4, (0, 10), (0, 3.8))
    lx, ly = 1.4, 1.9
    sx = 7.8
    ax.fill([lx, sx, sx], [ly, 0.55, 3.25], color=SOFT_BG, edgecolor=INK, lw=1.6)
    ax.plot([lx, sx], [ly, ly], color=SLATE, lw=1.2, ls="--")
    draw_box(ax, 0.35, 1.45, 1.05, 0.9, "Fixture", r"$I$ (cd)", bg=MID_GRAY)
    ax.plot([sx, sx], [0.45, 3.35], color=INK, lw=2.8)
    ax.add_patch(Arc((lx, ly), 2.2, 2.2, angle=0, theta1=-22.8, theta2=22.8, color=INK, lw=1.4))
    ax.text(lx + 1.85, ly + 0.25, r"Beam Angle $\theta$", fontweight="bold", fontsize=8.6,
            bbox=dict(boxstyle="round,pad=0.12", facecolor=SOFT_BG, edgecolor="none"))
    draw_arrow(ax, lx, 0.28, sx, 0.28, label=r"Throw Distance $d$   (Illuminance $E = I / d^2$)", label_offset=(0, 0.2), style="<->")
    draw_arrow(ax, sx + 0.35, 0.55, sx + 0.35, 3.25, label=r"Beam Width" "\n" r"$W = 2d\tan(\theta/2)$", label_offset=(0.95, 0), style="<->")
    save_fig(fig, "diagram_ch04_luminaire_beam.png")

    # 6. Acoustic Propagation Delay
    fig, ax = new_canvas(6.4, 2.2, (0, 10), (0, 3.4))
    draw_box(ax, 0.4, 1.8, 2.0, 1.1, "Main Stage PA", "t = 0.0 ms", bg=MID_GRAY)
    draw_box(ax, 3.6, 0.35, 2.3, 1.0, "DSP Delay Unit", r"$\Delta t = d / c_{\mathrm{sound}}$", bg=SOFT_BG)
    draw_box(ax, 6.6, 0.35, 2.2, 1.0, "Delay Tower", "Aligned Wavefront", bg=LIGHT_GRAY)
    draw_arrow(ax, 2.5, 2.35, 7.7, 2.35, label=r"Acoustic Air Propagation ($c \approx 343.2\;\mathrm{m/s}$ over distance $d$)", label_offset=(0.35, 0.28), lw=2.0)
    ax.plot([1.4, 1.4, 3.6], [1.8, 0.85, 0.85], color=INK, lw=1.6)
    draw_arrow(ax, 3.3, 0.85, 3.6, 0.85)
    ax.text(2.5, 1.08, "Electrical Signal (~c)", ha="center", fontsize=8.3)
    draw_arrow(ax, 5.9, 0.85, 6.6, 0.85)
    draw_arrow(ax, 7.7, 2.1, 7.7, 1.4, label="In-Phase Sum", label_offset=(0.8, 0), style="<->")
    save_fig(fig, "diagram_ch04_acoustic_delay.png")


# ===========================================================================
# CHAPTER 05: RF, MICROWAVE & SPECTRUM ENGINEERING
# ===========================================================================
def gen_ch05():
    # 1. VSWR Standing Wave
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.9))
    draw_box(ax, 0.3, 2.55, 1.8, 0.95, "RF Source", r"$Z_0 = 50\;\Omega$", bg=SOFT_BG)
    draw_box(ax, 7.9, 2.55, 1.8, 0.95, "Antenna Load", r"$Z_L = R + jX$", bg=LIGHT_GRAY)
    draw_arrow(ax, 2.2, 3.25, 7.8, 3.25, label=r"Incident Wave $V^+$", label_offset=(0, 0.2), lw=1.8)
    draw_arrow(ax, 7.8, 2.8, 2.2, 2.8, label=r"Reflected Wave $V^- = \Gamma V^+$", label_offset=(0, -0.22), lw=1.6, color=SLATE)
    z = np.linspace(1.5, 8.5, 400)
    env = 0.65 + 0.85 * np.abs(np.cos(1.35 * (z - 1.5)))
    ax.plot(z, 0.4 + env, color=INK, lw=2.0)
    ax.plot([1.5, 8.5], [0.4 + 1.5, 0.4 + 1.5], color=SLATE, lw=1.0, ls="--")
    ax.plot([1.5, 8.5], [0.4 + 0.65, 0.4 + 0.65], color=SLATE, lw=1.0, ls=":")
    ax.fill_between(z, 0.4, 0.4 + env, color=SOFT_BG)
    ax.text(1.35, 1.9, r"$V_{\max}$", ha="right", va="center", fontweight="bold")
    ax.text(1.35, 1.05, r"$V_{\min}$", ha="right", va="center", fontweight="bold")
    draw_arrow(ax, 1.5, 0.22, 1.5 + math.pi / 1.35, 0.22, label=r"$\lambda / 2$", label_offset=(0, -0.18), style="<->")
    ax.text(6.6, 0.18, r"$\mathrm{VSWR} = V_{\max}/V_{\min} = (1+|\Gamma|)/(1-|\Gamma|)$", ha="center", fontweight="bold", fontsize=8.6)
    save_fig(fig, "diagram_ch05_vswr_standing_wave.png")

    # 2. Smith Chart
    fig, ax = new_canvas(6.4, 2.8, (0, 10), (0, 4.4))
    cx, cy, R = 3.2, 2.2, 1.75
    ax.add_patch(Circle((cx, cy), R, facecolor=SOFT_BG, edgecolor=INK, lw=2.0))
    ax.plot([cx - R, cx + R], [cy, cy], color=INK, lw=1.4)
    # Constant resistance circles r = 0.5, 1.0, 2.0
    for r_val in [0.5, 1.0, 2.0]:
        rc = R * (1 / (1 + r_val))
        xc = cx + R * (r_val / (1 + r_val))
        ax.add_patch(Circle((xc, cy), rc, facecolor="none", edgecolor=SLATE, lw=1.1, ls="--"))
    # Reactance arcs (clipped visually inside circle via theta)
    t = np.linspace(0, 2 * np.pi, 300)
    for x_val in [0.6, -0.6, 1.3, -1.3]:
        rx = R / abs(x_val)
        ux = cx + R + rx * np.cos(t)
        uy = cy + (R / x_val) + rx * np.sin(t)
        mask = (ux - cx)**2 + (uy - cy)**2 <= R**2 + 0.01
        ax.plot(ux[mask], uy[mask], color=MUTED, lw=1.0, ls=":")
    ax.scatter([cx - R, cx, cx + R], [cy, cy, cy], color=INK, s=38, zorder=5)
    ax.text(cx - R - 0.15, cy, "Short\n" r"$\Gamma=-1$", ha="right", va="center", fontsize=8.3, fontweight="bold")
    ax.text(cx + R + 0.15, cy, "Open\n" r"$\Gamma=+1$", ha="left", va="center", fontsize=8.3, fontweight="bold")
    ax.text(cx, cy + R + 0.22, r"$+j1.0$ (Inductive $+90^\circ$)", ha="center", fontsize=8.5, fontweight="bold")
    ax.text(cx, cy - R - 0.28, r"$-j1.0$ (Capacitive $-90^\circ$)", ha="center", fontsize=8.5, fontweight="bold")
    ax.text(cx + 0.12, cy - 0.28, r"Match $(1,0)$", fontsize=8.1, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.08", facecolor=SOFT_BG, edgecolor="none"))
    draw_box(ax, 5.75, 0.85, 3.9, 2.65, "Bilinear Smith Mapping (SMTH)",
             r"• Normalized Impedance:" "\n"
             r"   $z = (R + jX) / Z_0 = r + jx$" "\n"
             r"• Reflection Coefficient:" "\n"
             r"   $\Gamma = (z - 1) / (z + 1) = |\Gamma|\angle\theta$" "\n"
             r"• Center $(1,0)$: $\Gamma = 0$, $\mathrm{VSWR}=1.0$", bg="#FFFFFF", fontsize=8.6)
    save_fig(fig, "diagram_ch05_smith_chart.png")

    # 3. Reactive L-Network
    fig, ax = new_canvas(6.4, 2.3, (0, 10), (0, 3.6))
    draw_box(ax, 0.5, 1.0, 1.8, 1.6, "Low Load", r"$R_{\mathrm{low}}$" "\n" r"($12.5\;\Omega$)", bg=SOFT_BG)
    draw_box(ax, 7.7, 1.0, 1.8, 1.6, "System Port", r"$R_{\mathrm{high}}$" "\n" r"($50.0\;\Omega$)", bg=LIGHT_GRAY)
    ax.plot([2.3, 3.5], [2.25, 2.25], color=INK, lw=1.8)
    draw_box(ax, 3.5, 1.9, 2.2, 0.7, r"Series $jX_{\mathrm{ser}}$", r"$X_{\mathrm{ser}} = Q \cdot R_{\mathrm{low}}$", bg="#FFFFFF", fontsize=8.5)
    ax.plot([5.7, 7.7], [2.25, 2.25], color=INK, lw=1.8)
    ax.plot([6.5, 6.5], [2.25, 1.95], color=INK, lw=1.8)
    draw_box(ax, 5.55, 1.05, 1.9, 0.9, r"Shunt $jX_{\mathrm{sh}}$", r"$X_{\mathrm{sh}} = R_{\mathrm{high}} / Q$", bg="#FFFFFF", fontsize=8.5)
    ax.plot([6.5, 6.5], [1.05, 0.65], color=INK, lw=1.8)
    ax.plot([2.3, 7.7], [0.65, 0.65], color=INK, lw=1.8)
    ax.scatter([6.5, 6.5], [2.25, 0.65], color=INK, s=35, zorder=5)
    ax.text(4.4, 0.22, r"Transformation Q-Factor:  $Q = \sqrt{(R_{\mathrm{high}} / R_{\mathrm{low}}) - 1}$", ha="center", fontweight="bold")
    save_fig(fig, "diagram_ch05_l_network.png")

    # 4. Fresnel Zone
    fig, ax = new_canvas(6.4, 2.3, (0, 10), (0, 3.6))
    t = np.linspace(0, 2 * np.pi, 300)
    ex = 5.0 + 3.4 * np.cos(t)
    ey = 2.0 + 0.85 * np.sin(t)
    ax.fill(ex, ey, color=SOFT_BG, edgecolor=INK, lw=1.6, ls="--")
    ax.plot([1.6, 8.4], [2.0, 2.0], color=INK, lw=1.8)
    # Towers
    ax.plot([1.6, 1.6], [0.4, 2.0], color=INK, lw=3.0)
    ax.plot([8.4, 8.4], [0.4, 2.0], color=INK, lw=3.0)
    ax.scatter([1.6, 8.4], [2.0, 2.0], color=INK, s=55, zorder=5)
    ax.text(1.6, 2.35, "Tx Dish", ha="center", fontweight="bold")
    ax.text(8.4, 2.35, "Rx Dish", ha="center", fontweight="bold")
    draw_arrow(ax, 5.0, 2.0, 5.0, 2.85, label=r"$r_1 = 8.656\sqrt{d_{\mathrm{km}} / f_{\mathrm{GHz}}}$", label_offset=(1.65, 0), style="<->")
    draw_arrow(ax, 1.6, 0.55, 8.4, 0.55, label=r"Total Link Path Distance $d$ (km)", label_offset=(0, 0.22), style="<->")
    ax.text(5.0, 3.18, "First Fresnel Zone Ellipsoid Boundary", ha="center", fontweight="bold")
    save_fig(fig, "diagram_ch05_fresnel_zone.png")

    # 5. IIP3 and SFDR
    fig, ax = new_canvas(6.4, 2.6, (0, 10), (0, 4.1))
    draw_arrow(ax, 1.2, 0.55, 1.2, 3.8, lw=1.5)
    draw_arrow(ax, 1.2, 0.55, 9.2, 0.55, lw=1.5)
    ax.text(1.05, 3.65, r"$P_{\mathrm{out}}$" "\n(dBm)", ha="right", va="center", fontweight="bold")
    ax.text(9.0, 0.2, r"Input Power $P_{\mathrm{in}}$ (dBm)", ha="right", fontweight="bold")
    # Noise floor
    ax.fill([1.2, 8.8, 8.8, 1.2], [0.55, 0.55, 1.05, 1.05], color=LIGHT_GRAY)
    ax.plot([1.2, 8.8], [1.05, 1.05], color=INK, lw=1.3, ls="--")
    ax.text(8.7, 0.8, r"Noise Floor $N_{\mathrm{flr}}$", ha="right", va="center", fontsize=8.4, fontweight="bold")
    # Fundamental (slope 1) and IM3 (slope 3)
    # Intersect at (7.4, 3.45)
    ax.plot([1.5, 5.8], [0.75, 2.71], color=INK, lw=2.2)
    ax.plot([5.8, 7.4], [2.71, 3.45], color=INK, lw=1.4, ls=":")
    ax.plot([3.8, 6.2], [0.55, 2.09], color=SLATE, lw=2.0)
    ax.plot([6.2, 7.4], [2.09, 3.45], color=SLATE, lw=1.4, ls=":")
    ax.scatter([7.4], [3.45], color=INK, s=50, zorder=5)
    ax.text(7.55, 3.45, "IIP3 Intercept\nPoint", va="center", fontweight="bold", fontsize=8.6)
    ax.text(3.3, 2.0, "Fundamental\n(1:1 Slope)", rotation=23, ha="center", fontweight="bold", fontsize=8.5)
    ax.text(6.65, 2.05, "3rd-Order IM3\n(3:1 Slope)", rotation=48, ha="center", fontweight="bold", fontsize=8.4)
    # SFDR arrow at x = 4.58 (where IM3 crosses Noise Floor y=1.05)
    x_sfdr = 4.58
    y_fund = 0.75 + (x_sfdr - 1.5) * (2.71 - 0.75) / (5.8 - 1.5)
    draw_arrow(ax, x_sfdr, 1.05, x_sfdr, y_fund, lw=1.8, style="<->")
    ax.text(x_sfdr + 0.15, (1.05 + y_fund) / 2 - 0.08, r"$\mathrm{SFDR} = \frac{2}{3}(\mathrm{IIP}_3 - N_{\mathrm{flr}})$",
            va="center", fontweight="bold", fontsize=8.5,
            bbox=dict(boxstyle="round,pad=0.16", facecolor="#FFFFFF", edgecolor=MID_GRAY))
    save_fig(fig, "diagram_ch05_iip3_sfdr.png")


# ===========================================================================
# CHAPTER 06: CHEMISTRY & WET-LAB STOICHIOMETRY
# ===========================================================================
def gen_ch06():
    # 1. Stock Dilution (C1V1 = C2V2)
    fig, ax = new_canvas(6.4, 2.3, (0, 10), (0, 3.6))
    draw_box(ax, 0.4, 0.5, 2.6, 2.5, "Concentrated Stock",
             r"Concentration $C_1$" "\n" r"Aliquot Volume $V_1$" "\n" r"Moles $n = C_1 V_1$", bg=MID_GRAY)
    draw_box(ax, 3.7, 0.9, 2.6, 1.7, "Pipette Transfer",
             r"Fixed Solute Moles $n$" "\n" "+ Pure Diluent Solvent\n" r"$\Delta V = V_2 - V_1$", bg=SOFT_BG)
    draw_box(ax, 7.0, 0.5, 2.6, 2.5, "Working Solution",
             r"Target Conc. $C_2$" "\n" r"Final Volume $V_2$" "\n" r"$C_1 V_1 = C_2 V_2$", bg=LIGHT_GRAY)
    draw_arrow(ax, 3.05, 1.75, 3.65, 1.75, lw=1.8)
    draw_arrow(ax, 6.35, 1.75, 6.95, 1.75, lw=1.8)
    save_fig(fig, "diagram_ch06_stock_dilution.png")

    # 2. Henderson-Hasselbalch Titration Curve
    fig, ax = new_canvas(6.4, 2.6, (0, 10), (0, 4.1))
    draw_arrow(ax, 1.2, 0.65, 1.2, 3.8, lw=1.5)
    draw_arrow(ax, 1.2, 0.65, 9.1, 0.65, lw=1.5)
    ax.text(1.05, 3.65, "pH", ha="right", va="center", fontweight="bold")
    ax.text(5.15, 0.08, r"Equivalents of Strong Base Added ($[\mathrm{A}^-] / ([\mathrm{HA}]+[\mathrm{A}^-])$)", ha="center", fontweight="bold")
    x = np.linspace(0.02, 0.98, 300)
    ph_norm = 2.05 + 0.38 * np.log10(x / (1 - x))
    x_plot = 1.4 + x * 6.2
    ax.fill_between(x_plot[(x >= 0.15) & (x <= 0.85)], 0.65, ph_norm[(x >= 0.15) & (x <= 0.85)], color=SOFT_BG)
    ax.plot(x_plot, ph_norm, color=INK, lw=2.2)
    ax.plot([7.48, 7.75, 8.5], [ph_norm[-1], 3.45, 3.6], color=INK, lw=2.2)
    ax.plot([1.2, 4.5], [2.05, 2.05], color=SLATE, lw=1.2, ls="--")
    ax.plot([4.5, 4.5], [0.65, 2.05], color=SLATE, lw=1.2, ls="--")
    ax.scatter([4.5], [2.05], color=INK, s=45, zorder=5)
    ax.text(1.08, 2.05, r"$\mathrm{pH}=\mathrm{p}K_a$", ha="right", va="center", fontweight="bold")
    ax.text(4.5, 0.42, "0.5 eq", ha="center", fontweight="bold", fontsize=8.4)
    ax.text(7.6, 0.42, "1.0 eq", ha="center", fontweight="bold", fontsize=8.4)
    ax.text(4.5, 2.55, r"Buffer Plateau ($\mathrm{pH} = \mathrm{p}K_a \pm 1$)" "\n" r"$[\mathrm{A}^-] = [\mathrm{HA}]$ at Midpoint",
            ha="center", fontweight="bold", fontsize=8.6,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#FFFFFF", edgecolor=MID_GRAY))
    save_fig(fig, "diagram_ch06_henderson_hasselbalch.png")

    # 3. Beer-Lambert Cuvette
    fig, ax = new_canvas(6.4, 2.3, (0, 10), (0, 3.6))
    draw_box(ax, 3.6, 0.55, 2.6, 2.3, "Quartz Cuvette",
             r"Concentration $c$ (M)" "\n" r"Absorptivity $\varepsilon$" "\n" r"$A = \varepsilon \cdot b \cdot c$", bg=LIGHT_GRAY)
    draw_arrow(ax, 0.8, 1.7, 3.55, 1.7, label=r"Incident Beam $I_0$", label_offset=(0, 0.28), lw=2.6)
    draw_arrow(ax, 6.25, 1.7, 8.9, 1.7, label=r"Transmitted $I = I_0 10^{-A}$", label_offset=(0, 0.28), lw=1.4)
    draw_arrow(ax, 3.6, 3.15, 6.2, 3.15, label=r"Optical Path $b$ (cm)", label_offset=(0, 0.22), style="<->")
    ax.text(5.0, 0.18, r"Transmittance $T = I / I_0$   |   Absorbance $A = -\log_{10}(T) = \varepsilon b c$", ha="center", fontweight="bold")
    save_fig(fig, "diagram_ch06_beer_lambert.png")

    # 4. Galvanic Cell (Nernst)
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.9))
    draw_box(ax, 0.3, 0.35, 3.15, 2.1, "Anode (Oxidation)",
             r"$\mathrm{Zn(s)} \rightarrow \mathrm{Zn}^{2+} + 2e^-$" "\n" r"$[\mathrm{Zn}^{2+}] = 1.0\;\mathrm{M}$", bg=SOFT_BG, fontsize=8.8)
    draw_box(ax, 6.55, 0.35, 3.15, 2.1, "Cathode (Reduction)",
             r"$\mathrm{Cu}^{2+} + 2e^- \rightarrow \mathrm{Cu(s)}$" "\n" r"$[\mathrm{Cu}^{2+}] = 0.10\;\mathrm{M}$", bg=LIGHT_GRAY, fontsize=8.8)
    draw_box(ax, 3.65, 1.35, 2.7, 0.75, "Salt Bridge (KCl)", r"$\leftarrow \mathrm{Cl}^-\;\;|\;\;\mathrm{K}^+ \rightarrow$", bg="#FFFFFF", fontsize=8.4)
    draw_box(ax, 3.5, 2.85, 3.0, 0.8, r"Voltmeter: $E = E^\circ - \frac{RT}{nF}\ln Q$", r"$E = 1.10 - 0.0296 = 1.0704\;\mathrm{V}$", bg=MID_GRAY, fontsize=8.5)
    ax.plot([1.85, 1.85, 3.5], [2.45, 3.25, 3.25], color=INK, lw=1.8)
    ax.plot([6.5, 8.15, 8.15], [3.25, 3.25, 2.45], color=INK, lw=1.8)
    draw_arrow(ax, 2.15, 3.45, 3.25, 3.45, label=r"$e^-$ flow", label_offset=(0, 0.18))
    save_fig(fig, "diagram_ch06_galvanic_cell.png")

    # 5. Centrifuge RCF
    fig, ax = new_canvas(6.4, 2.4, (0, 10), (0, 3.8))
    ax.plot([1.4, 1.4], [0.3, 3.5], color=INK, lw=2.4, ls="-.")
    ax.text(1.4, 3.6, "Spin Axis\n(RPM)", ha="center", fontweight="bold", fontsize=8.8)
    tube_pts = [(3.1, 3.0), (3.5, 3.2), (6.1, 0.9), (5.7, 0.7)]
    ax.add_patch(Polygon(tube_pts, closed=True, facecolor=SOFT_BG, edgecolor=INK, lw=1.8))
    ax.add_patch(Polygon([(5.3, 1.05), (5.7, 1.25), (6.1, 0.9), (5.7, 0.7)], closed=True, facecolor=MID_GRAY, edgecolor=INK, lw=1.5))
    for rx, ry, lbl in [
        (3.5, 2.9, r"$r_{\min}$ (Meniscus)"),
        (4.65, 1.9, r"$r_{\mathrm{av}}$ (Mid-Tube)"),
        (5.9, 0.85, r"$r_{\max}$ (Pellet Tip)"),
    ]:
        draw_arrow(ax, 1.4, ry, rx, ry, style="<->", lw=1.4)
        ax.text(rx + 0.2, ry, lbl, va="center", fontweight="bold", fontsize=8.5,
                bbox=dict(boxstyle="round,pad=0.08", facecolor="#FFFFFF", edgecolor="none"))
    draw_box(ax, 5.65, 2.45, 4.05, 1.15, "Relative Centrifugal Force (RCF)",
             r"$\mathrm{RCF} = 1.118 \times 10^{-5} \cdot r_{\mathrm{cm}} \cdot \mathrm{RPM}^2$", bg="#FFFFFF", fontsize=8.8)
    save_fig(fig, "diagram_ch06_centrifuge_rcf.png")


# ===========================================================================
# CHAPTER 07: CULINARY, BAKING & BREWING
# ===========================================================================
def gen_ch07():
    # 1. Baker's Percentage vs Total Weight %
    fig, ax = new_canvas(6.4, 2.4, (0, 10), (0, 3.7))
    ax.text(0.4, 3.3, "A. Coupled Total-Weight Percentages (All Ingredients Sum to 100%)", fontweight="bold")
    draw_box(ax, 0.4, 2.35, 4.5, 0.75, "Flour: 50.8%", bg=LIGHT_GRAY, radius=0.03)
    draw_box(ax, 4.92, 2.35, 3.35, 0.75, "Water: 38.1%", bg=SOFT_BG, radius=0.03)
    draw_box(ax, 8.29, 2.35, 0.95, 0.75, "Lv 10%", bg="#FFFFFF", fontsize=8.0, radius=0.03)
    draw_box(ax, 9.26, 2.35, 0.38, 0.75, "S", bg=MID_GRAY, fontsize=7.5, radius=0.02)

    ax.text(0.4, 1.85, "B. Decoupled Baker's Percentages (Flour Anchor FLR = 100.0%, Sum = 197.0%)", fontweight="bold")
    draw_box(ax, 0.4, 0.95, 5.2, 0.7, "Total Flour Anchor (FLR): 100.0%", bg=MID_GRAY, radius=0.03)
    draw_box(ax, 0.4, 0.15, 3.9, 0.7, "Water (HYD%): 75.0%", bg=LIGHT_GRAY, radius=0.03)
    draw_box(ax, 4.4, 0.15, 2.4, 0.7, "Levain: 20.0%", bg=SOFT_BG, radius=0.03)
    draw_box(ax, 6.9, 0.15, 1.8, 0.7, "Salt: 2.0%", bg="#FFFFFF", radius=0.03)
    save_fig(fig, "diagram_ch07_bakers_percentage.png")

    # 2. Dough Thermal Balance & Ice Substitution
    fig, ax = new_canvas(6.4, 2.3, (0, 10), (0, 3.6))
    draw_box(ax, 0.3, 1.95, 4.4, 1.35, "3-Factor DDT Thermal Inputs",
             r"$T_{\mathrm{room}}(27^\circ\mathrm{C}) + T_{\mathrm{flour}}(25^\circ\mathrm{C}) + F_{\mathrm{mix}}(11^\circ\mathrm{C}) = 63^\circ\mathrm{C}$" "\n"
             r"$T_{\mathrm{water}} = 3\,\mathrm{DDT}(72^\circ\mathrm{C}) - 63^\circ\mathrm{C} = 9.0^\circ\mathrm{C}$", bg=SOFT_BG, fontsize=8.5)
    draw_box(ax, 5.3, 1.95, 4.4, 1.35, "Latent Heat Ice Substitution (IC%)",
             r"Tap Water $21^\circ\mathrm{C} > 9^\circ\mathrm{C}$  ($L_{\mathrm{ice}} \approx 80\;\mathrm{kcal/kg}$)" "\n"
             r"$W_{\mathrm{ice}} = W_{\mathrm{water}}\frac{T_{\mathrm{tap}} - T_{\mathrm{req}}}{T_{\mathrm{tap}} + 80} = 2.40\;\mathrm{kg}$", bg=LIGHT_GRAY, fontsize=8.5)
    draw_box(ax, 1.8, 0.25, 6.4, 1.2, "Equilibrium Final Dough Batch",
             r"$13.60\;\mathrm{kg}$ Tap Water $+ 2.40\;\mathrm{kg}$ Crushed Ice $\Longrightarrow$ Target $\mathrm{DDT} = 24.0^\circ\mathrm{C}$", bg=MID_GRAY, fontsize=9.0)
    draw_arrow(ax, 2.5, 1.95, 3.8, 1.45, lw=1.6)
    draw_arrow(ax, 7.5, 1.95, 6.2, 1.45, lw=1.6)
    save_fig(fig, "diagram_ch07_dough_thermal_balance.png")

    # 3. Mash Tun Equilibrium
    fig, ax = new_canvas(6.4, 2.2, (0, 10), (0, 3.4))
    draw_box(ax, 0.4, 1.75, 4.1, 1.3, "Hot Strike Water (MSH)",
             r"Specific Heat $c_w = 1.0\;\mathrm{kcal/(kg\cdot^\circ C)}$" "\n"
             r"Liquor-to-Grist Ratio $R$, Temp $T_{\mathrm{strike}}$", bg=LIGHT_GRAY, fontsize=8.6)
    draw_box(ax, 5.5, 1.75, 4.1, 1.3, "Dry Malted Barley Grain",
             r"Specific Heat $c_g \approx 0.2\,c_w$ ($40\%$ of water)" "\n"
             r"Ambient Grain Temperature $T_{\mathrm{grain}}$", bg=SOFT_BG, fontsize=8.6)
    draw_box(ax, 1.6, 0.2, 6.8, 1.15, "Mash Tun First-Law Thermal Equilibrium",
             r"$T_{\mathrm{strike}} = \frac{0.2}{R}\,(T_{\mathrm{target}} - T_{\mathrm{grain}}) + T_{\mathrm{target}}$", bg=MID_GRAY, fontsize=9.5)
    draw_arrow(ax, 2.45, 1.75, 3.8, 1.35, lw=1.6)
    draw_arrow(ax, 7.55, 1.75, 6.2, 1.35, lw=1.6)
    save_fig(fig, "diagram_ch07_mash_equilibrium.png")

    # 4. Coffee Extraction Balance
    fig, ax = new_canvas(6.4, 2.2, (0, 10), (0, 3.4))
    draw_box(ax, 0.3, 0.65, 2.7, 2.1, "1. Dry Coffee Dose",
             r"$W_{\mathrm{dose}} = 18.0\;\mathrm{g}$" "\n" "(Roasted Grounds)", bg=SOFT_BG)
    draw_box(ax, 3.65, 0.65, 2.7, 2.1, "2. Beverage TDS",
             r"$W_{\mathrm{brew}} = 36.0\;\mathrm{g}$" "\n" r"$\mathrm{TDS} = 10.2\%$" "\n" r"$m_{\mathrm{sol}} = 3.672\;\mathrm{g}$", bg=LIGHT_GRAY)
    draw_box(ax, 7.0, 0.65, 2.7, 2.1, "3. Extraction Yield",
             r"$\mathrm{EY\%} = \frac{W_{\mathrm{brew}} \cdot \mathrm{TDS}}{W_{\mathrm{dose}}}$" "\n" r"$\mathrm{EY\%} = 20.40\%$", bg=MID_GRAY)
    draw_arrow(ax, 3.0, 1.7, 3.65, 1.7, lw=1.8)
    draw_arrow(ax, 6.35, 1.7, 7.0, 1.7, lw=1.8)
    save_fig(fig, "diagram_ch07_coffee_extraction.png")


# ===========================================================================
# CHAPTER 08: CLINICAL PHARMACY & NURSING
# ===========================================================================
def gen_ch08():
    # 1. Therapeutic Window & Steady State
    fig, ax = new_canvas(6.4, 2.6, (0, 10), (0, 4.1))
    draw_arrow(ax, 1.2, 0.65, 1.2, 3.8, lw=1.5)
    draw_arrow(ax, 1.2, 0.65, 9.2, 0.65, lw=1.5)
    ax.text(1.05, 3.65, r"$C(t)$" "\n(mg/L)", ha="right", va="center", fontweight="bold")
    ax.text(5.2, 0.08, r"Elapsed Half-Lives ($n \cdot t_{1/2}$,  $96.9\%$ Steady State at $5\,t_{1/2}$)", ha="center", fontweight="bold")
    # Therapeutic window
    ax.fill([1.2, 8.9, 8.9, 1.2], [1.55, 1.55, 3.0, 3.0], color=SOFT_BG)
    ax.plot([1.2, 8.9], [3.0, 3.0], color=INK, lw=1.4, ls="--")
    ax.plot([1.2, 8.9], [1.55, 1.55], color=INK, lw=1.4, ls="--")
    ax.text(8.8, 3.18, "MTC (Toxic Threshold)", ha="right", fontweight="bold", fontsize=8.4)
    ax.text(8.8, 1.28, "MEC (Min Effective)", ha="right", fontweight="bold", fontsize=8.4)
    # Multi-dose sawtooth curve
    t_all, c_all = [], []
    c_prev = 0.0
    for k in range(6):
        t_seg = np.linspace(0, 1.0, 60)
        c_peak = c_prev + 1.35
        c_seg = c_peak * np.exp(-0.693 * t_seg)
        t_all.extend(1.2 + (k + t_seg) * 1.25)
        c_all.extend(0.65 + c_seg)
        c_prev = c_seg[-1]
    ax.plot(t_all, c_all, color=INK, lw=2.0)
    for k in range(1, 6):
        ax.text(1.2 + k * 1.25, 0.42, f"{k}" r"$t_{1/2}$", ha="center", fontsize=8.3, fontweight="bold")
    save_fig(fig, "diagram_ch08_therapeutic_window.png")

    # 2. Body Weight Compartments
    fig, ax = new_canvas(6.4, 2.2, (0, 10), (0, 3.4))
    draw_box(ax, 0.5, 2.05, 5.4, 0.95, "Ideal Body Weight (IBW = 61.5 kg)", "Lean Metabolic Tissue Compartment", bg=MID_GRAY, radius=0.04)
    draw_box(ax, 5.95, 2.05, 3.55, 0.95, "Excess Adipose Mass (38.5 kg)", "40% Extracellular Perfusion Factor", bg=SOFT_BG, radius=0.04)
    draw_arrow(ax, 0.5, 1.65, 5.9, 1.65, label="Hydrophilic Drugs (Dosed on IBW)", label_offset=(0, 0.18), style="<->")
    draw_arrow(ax, 0.5, 1.05, 7.35, 1.05, label=r"Adjusted Body Weight $\mathrm{AdjW} = \mathrm{IBW} + 0.4(\mathrm{TBW}-\mathrm{IBW}) = 76.9\;\mathrm{kg}$", label_offset=(0, 0.18), style="<->")
    draw_arrow(ax, 0.5, 0.45, 9.5, 0.45, label="Total Body Weight (TBW = 100.0 kg)", label_offset=(0, 0.18), style="<->")
    save_fig(fig, "diagram_ch08_body_weight_compartments.png")

    # 3. Renal Clearance Tiers
    fig, ax = new_canvas(6.4, 2.3, (0, 10), (0, 3.6))
    tiers = [
        (r"$\mathrm{CrCl} \geq 90\;\mathrm{mL/min}$", 6.2, "Normal GFR (Standard Maintenance Dose)", 2.8, MID_GRAY),
        (r"$60\text{–}89\;\mathrm{mL/min}$", 4.6, "Mild Reduction (Monitor Narrow-TI Drugs)", 2.15, LIGHT_GRAY),
        (r"$30\text{–}59\;\mathrm{mL/min}$", 2.9, "Moderate Impairment (Reduce Dose 25%–50%)", 1.5, SOFT_BG),
        (r"$15\text{–}29\;\mathrm{mL/min}$", 1.7, "Severe Impairment (Extend Interval q24h–q48h)", 0.85, "#FFFFFF"),
        (r"$< 15\;\mathrm{mL/min}$", 0.85, "Renal Failure / Dialysis Dosing Protocol", 0.2, "#FFFFFF"),
    ]
    for lbl, w, desc, y, bg in tiers:
        ax.text(2.4, y + 0.25, lbl, ha="right", va="center", fontweight="bold", fontsize=8.6)
        draw_box(ax, 2.55, y, w, 0.48, "", bg=bg, radius=0.03)
        tx = 2.75 if w >= 4.5 else 2.55 + w + 0.18
        ax.text(tx, y + 0.24, desc, va="center", fontsize=8.3, fontweight="bold")
    save_fig(fig, "diagram_ch08_renal_clearance_tiers.png")

    # 4. Drip Dimensional Chain
    fig, ax = new_canvas(6.4, 2.1, (0, 10), (0, 3.2))
    steps = [
        ("Ordered Dose", r"$\mathrm{mcg/(kg\cdot min)}$", 0.25, SOFT_BG),
        ("× Weight W", r"$\mathrm{mcg / min}$", 2.15, LIGHT_GRAY),
        ("× 60 min/hr", r"$\mathrm{mcg / hr}$", 4.05, SOFT_BG),
        ("÷ Conc C", r"Pump $\mathrm{mL/hr}$", 5.95, MID_GRAY),
        ("× DF / 60", r"Gravity $\mathrm{gtt/min}$", 7.85, LIGHT_GRAY),
    ]
    for title, sub, x, bg in steps:
        draw_box(ax, x, 0.9, 1.65, 1.4, title, sub, bg=bg, fontsize=8.6, radius=0.06)
    for k in range(4):
        draw_arrow(ax, 1.9 + k * 1.9, 1.6, 2.15 + k * 1.9, 1.6, lw=1.6)
    ax.text(5.0, 0.35, r"Master Vasoactive Identity:  $R_{\mathrm{mL/hr}} = (D \times W \times 60) / C_{\mathrm{mcg/mL}}$", ha="center", fontweight="bold")
    save_fig(fig, "diagram_ch08_drip_dimensional_chain.png")

    # 5. Parkland Burn Resuscitation
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.9))
    draw_arrow(ax, 1.35, 0.65, 1.35, 3.7, lw=1.5)
    draw_arrow(ax, 1.35, 0.65, 9.3, 0.65, lw=1.5)
    ax.text(1.15, 3.45, "Infusion\nRate\n(mL/hr)", ha="right", va="center", fontweight="bold", fontsize=8.2)
    ax.text(5.3, 0.08, "Elapsed Time from Thermal Injury (Hours)", ha="center", fontweight="bold")
    # Phase 1: 0 to 8h (x: 1.35 to 4.15)
    draw_box(ax, 1.35, 0.65, 2.8, 2.35, "Phase 1 (Hours 0–8)",
             r"First $50\%$ of $V_{24}$" "\n" r"$5{,}100\;\mathrm{mL} / 8\;\mathrm{h} = 637.5\;\mathrm{mL/h}$", bg=MID_GRAY, fontsize=8.6, radius=0.02)
    # Phase 2: 8 to 24h (x: 4.15 to 9.0)
    draw_box(ax, 4.15, 0.65, 4.85, 1.3, "Phase 2 (Hours 8–24)",
             r"Remaining $50\%$ of $V_{24}$:  $5{,}100\;\mathrm{mL} / 16\;\mathrm{h} = 318.8\;\mathrm{mL/h}$", bg=LIGHT_GRAY, fontsize=8.5, radius=0.02)
    for x, lbl in [(1.35, "0 hr"), (4.15, "8 hr"), (9.0, "24 hr")]:
        ax.text(x, 0.42, lbl, ha="center", fontweight="bold", fontsize=8.4)
    ax.text(1.22, 2.95, "638", ha="right", va="center", fontweight="bold", fontsize=8.4)
    ax.text(1.22, 1.95, "319", ha="right", va="center", fontweight="bold", fontsize=8.4)
    save_fig(fig, "diagram_ch08_parkland_burn.png")

    # 6. Serum Gamblegram
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.9))
    draw_box(ax, 1.4, 0.55, 2.8, 2.8, r"Primary Cation $\mathrm{Na}^+$",
             r"$140\;\mathrm{mEq/L}$" "\n(Extracellular Anchor)", bg=LIGHT_GRAY, radius=0.03)
    draw_box(ax, 5.6, 1.55, 2.8, 1.8, r"Chloride $\mathrm{Cl}^-$", r"$102\;\mathrm{mEq/L}$", bg=SOFT_BG, radius=0.03)
    draw_box(ax, 5.6, 1.0, 2.8, 0.53, r"$\mathrm{HCO}_3^-$ ($16\;\mathrm{mEq/L}$)", bg="#FFFFFF", fontsize=8.4, radius=0.02)
    draw_box(ax, 5.6, 0.55, 2.8, 0.43, r"Anion Gap $\mathrm{AGAP} = 22$", bg=MID_GRAY, fontsize=8.4, radius=0.02)
    ax.text(4.9, 1.95, "=", ha="center", va="center", fontsize=18, fontweight="bold")
    ax.text(2.8, 0.2, "Total Cations = 140 mEq/L", ha="center", fontweight="bold")
    ax.text(7.0, 0.2, r"$\mathrm{Cl}^- + \mathrm{HCO}_3^- + \mathrm{AGAP} = 140\;\mathrm{mEq/L}$", ha="center", fontweight="bold")
    save_fig(fig, "diagram_ch08_serum_gamblegram.png")

    # 7. Patient Profile Wizard Bar
    fig, ax = new_canvas(6.4, 2.2, (0, 10), (0, 3.4))
    keys = [("F1: W", "72.0 kg"), ("F2: H", "168 cm"), ("F3: A", "74 yr"), ("F4: S", "1.25 mg/dL"), ("F5/F6", "MALE / FEM")]
    for k, (k_lbl, v_lbl) in enumerate(keys):
        x = 0.4 + k * 1.86
        draw_box(ax, x, 1.95, 1.72, 1.05, k_lbl, v_lbl, bg=LIGHT_GRAY, fontsize=8.6, radius=0.05)
        draw_arrow(ax, x + 0.86, 1.95, x + 0.86, 1.35, lw=1.4)
    draw_box(ax, 0.4, 0.25, 9.15, 1.05, "Persistent [PAT] Biometric Profile & Reference Table ([TBL])",
             r"Auto-Populates $[\mathrm{GFR}] \rightarrow 37.9\;\mathrm{mL/min}$,  $[\mathrm{BSA}] \rightarrow 1.83\;\mathrm{m}^2$,  $[\mathrm{IBW}] \rightarrow 59.7\;\mathrm{kg}$",
             bg=SOFT_BG, fontsize=8.8, radius=0.05)
    save_fig(fig, "diagram_ch08_patient_profile_bar.png")


# ===========================================================================
# CHAPTER 09: FINANCE, ECONOMICS & STATISTICAL INFERENCE
# ===========================================================================
def gen_ch09():
    # 1. Cash-Flow Timeline
    fig, ax = new_canvas(6.4, 2.4, (0, 10), (0, 3.8))
    ax.plot([1.2, 8.8], [1.9, 1.9], color=INK, lw=2.0)
    # Inflow at t=0
    draw_arrow(ax, 1.5, 1.9, 1.5, 3.35, lw=2.2)
    ax.text(1.5, 3.5, r"$+\mathrm{PV}$ (Cash Inflow at $t=0$)", ha="center", fontweight="bold")
    ax.text(1.5, 1.6, r"$t=0$", ha="center", fontweight="bold")
    for k, x, lbl in [(1, 3.2, r"$t=1$"), (2, 4.9, r"$t=2$"), (3, 6.6, r"$t=3$"), (4, 8.5, r"$t=N$")]:
        ax.plot([x, x], [1.8, 2.0], color=INK, lw=1.8)
        ax.text(x, 2.15, lbl, ha="center", fontweight="bold")
        h = 0.55 if k == 4 else 0.9
        draw_arrow(ax, x, 1.9, x, h, lw=1.8, color=SLATE)
        ax.text(x, h - 0.22, r"$-\mathrm{PMT}$" if k < 4 else r"$-\mathrm{PMT}-\mathrm{FV}$", ha="center", fontsize=8.5, fontweight="bold")
    ax.text(7.55, 1.98, r"$\cdots$", ha="center", fontsize=14, fontweight="bold")
    ax.text(5.2, 3.05, r"Discounting Factor: $(1 + i)^{-t}$", ha="center", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", facecolor=SOFT_BG, edgecolor=MID_GRAY))
    save_fig(fig, "diagram_ch09_cashflow_timeline.png")

    # 2. Mortgage Amortization Split
    fig, ax = new_canvas(6.4, 2.3, (0, 10), (0, 3.6))
    rows = [
        ("Month 1", 0.72, "$1,500.00 Interest (83.4%)", "$298.65 Prin.", 2.4),
        ("Month 180", 0.58, "$1,069.51 Interest (59.5%)", "$729.14 Principal", 1.35),
        ("Month 360", 0.14, "$8.95 Int.", "$1,789.70 Principal (99.5%)", 0.3),
    ]
    for m_lbl, frac, i_txt, p_txt, y in rows:
        ax.text(1.65, y + 0.38, m_lbl, ha="right", va="center", fontweight="bold")
        w_int = 7.7 * frac
        w_prin = 7.7 * (1 - frac)
        draw_box(ax, 1.8, y, w_int, 0.75, i_txt, bg=LIGHT_GRAY, fontsize=8.3, radius=0.02)
        draw_box(ax, 1.8 + w_int, y, w_prin, 0.75, p_txt, bg=MID_GRAY, fontsize=8.3, radius=0.02)
    save_fig(fig, "diagram_ch09_amortization_split.png")

    # 3. Bond Price-Yield Curve
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.9))
    draw_arrow(ax, 1.3, 0.55, 1.3, 3.65, lw=1.5)
    draw_arrow(ax, 1.3, 0.55, 9.1, 0.55, lw=1.5)
    ax.text(1.15, 3.5, "Bond\nPrice\n($)", ha="right", va="center", fontweight="bold", fontsize=8.6)
    ax.text(9.0, 0.18, "Market Yield to Maturity y (%)", ha="right", fontweight="bold")
    y_rate = np.linspace(0.02, 0.08, 200)
    price = 5 * (1 - (1 + y_rate)**(-10)) / y_rate + 100 * (1 + y_rate)**(-10)
    x_plot = 1.6 + (y_rate - 0.02) / 0.06 * 7.0
    y_plot = 0.7 + (price - 80) / 48 * 2.7
    ax.plot(x_plot, y_plot, color=INK, lw=2.2)
    for yr, pr, lbl in [(0.04, 108.11, "Premium (y=4% < c, P=108.11)"),
                        (0.05, 100.00, "Par Bond (y=5% = c, P=100.00)"),
                        (0.06, 92.64, "Discount (y=6% > c, P=92.64)")]:
        px = 1.6 + (yr - 0.02) / 0.06 * 7.0
        py = 0.7 + (pr - 80) / 48 * 2.7
        ax.scatter([px], [py], color=INK, s=45, zorder=5)
        ax.plot([1.3, px], [py, py], color=SLATE, lw=1.0, ls=":")
        ax.plot([px, px], [0.55, py], color=SLATE, lw=1.0, ls=":")
        ax.text(px + 0.2, py + 0.1, lbl, fontsize=8.4, fontweight="bold")
    save_fig(fig, "diagram_ch09_bond_price_yield.png")

    # 4. Wilson EOQ Cost Curve
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.9))
    draw_arrow(ax, 1.3, 0.55, 1.3, 3.65, lw=1.5)
    draw_arrow(ax, 1.3, 0.55, 9.1, 0.55, lw=1.5)
    ax.text(1.15, 3.5, "Annual\nCost ($)", ha="right", va="center", fontweight="bold", fontsize=8.6)
    ax.text(9.0, 0.18, "Order Lot Size Q (Units)", ha="right", fontweight="bold")
    q = np.linspace(0.35, 2.2, 250)
    c_hold = 0.95 * q
    c_ord = 0.95 / q
    c_tot = c_hold + c_ord
    qx = 1.4 + q * 3.3
    ax.plot(qx, 0.55 + c_hold, color=SLATE, lw=1.6, ls="--")
    ax.plot(qx, 0.55 + c_ord, color=SLATE, lw=1.6, ls="-.")
    ax.plot(qx, 0.55 + c_tot, color=INK, lw=2.2)
    q_opt_x = 1.4 + 1.0 * 3.3
    ax.scatter([q_opt_x, q_opt_x], [0.55 + 0.95, 0.55 + 1.90], color=INK, s=45, zorder=5)
    ax.plot([q_opt_x, q_opt_x], [0.55, 0.55 + 1.90], color=INK, lw=1.2, ls=":")
    ax.text(q_opt_x, 0.3, r"$Q^* = \sqrt{2DS/H}$", ha="center", fontweight="bold")
    ax.text(7.5, 2.45, r"Holding Cost $(Q/2)H$", fontsize=8.5, fontweight="bold")
    ax.text(7.5, 0.95, r"Ordering Cost $(D/Q)S$", fontsize=8.5, fontweight="bold")
    ax.text(4.7, 2.85, r"Minimum Total Cost $\mathrm{TC}(Q^*)$", ha="center", fontweight="bold", fontsize=8.6,
            bbox=dict(boxstyle="round,pad=0.14", facecolor="#FFFFFF", edgecolor="none"))
    save_fig(fig, "diagram_ch09_eoq_cost_curve.png")

    # 5. Normal CDF (pnorm) and Quantile (qnorm)
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.9))
    z = np.linspace(-3.4, 3.4, 400)
    pdf = np.exp(-0.5 * z**2) / np.sqrt(2 * np.pi)
    zx = 5.0 + z * 1.05
    zy = 0.85 + pdf * 6.2
    mask = z <= 1.65
    ax.fill_between(zx[mask], 0.85, zy[mask], color=LIGHT_GRAY)
    ax.plot(zx, zy, color=INK, lw=2.2)
    ax.plot([1.2, 8.8], [0.85, 0.85], color=INK, lw=1.5)
    z_cut = 5.0 + 1.65 * 1.05
    ax.plot([z_cut, z_cut], [0.85, 0.85 + np.exp(-0.5 * 1.65**2) / np.sqrt(2 * np.pi) * 6.2], color=INK, lw=1.8, ls="--")
    ax.text(5.0, 0.55, r"$z = 0$", ha="center", fontweight="bold")
    ax.text(z_cut, 0.55, r"$z_p = 1.96$", ha="center", fontweight="bold")
    ax.text(4.85, 1.65, r"Cumulative Probability $p = \Phi(z_p)$" "\n" r"(pnorm: $z \rightarrow p$,  qnorm: $p \rightarrow z$)",
            ha="center", fontweight="bold", fontsize=8.4,
            bbox=dict(boxstyle="round,pad=0.12", facecolor=LIGHT_GRAY, edgecolor="none"))
    ax.text(5.0, 3.55, r"Peak Density $\phi(0) = 1/\sqrt{2\pi} \approx 0.3989$  ([f][PDF])", ha="center", fontweight="bold")
    save_fig(fig, "diagram_ch09_normal_cdf_quantile.png")

    # 6. Student's t vs Chi-Square
    fig, ax = new_canvas(6.4, 2.4, (0, 10), (0, 3.7))
    # Left panel: Student's t vs Normal
    z = np.linspace(-3.2, 3.2, 300)
    n_pdf = np.exp(-0.5 * z**2) / np.sqrt(2 * np.pi)
    t_pdf = 0.35 * (1 + z**2 / 2.0)**(-1.5)
    lx = 2.6 + z * 0.65
    ax.plot(lx, 0.75 + n_pdf * 5.8, color=SLATE, lw=1.5, ls="--", label="N(0,1)")
    ax.plot(lx, 0.75 + t_pdf * 5.8, color=INK, lw=2.0, label="t(df)")
    ax.plot([0.4, 4.8], [0.75, 0.75], color=INK, lw=1.4)
    ax.text(2.6, 3.35, r"A. Student's $t(\nu)$ Heavy Tails vs. $N(0,1)$", ha="center", fontweight="bold", fontsize=8.8)
    ax.text(2.6, 0.35, r"Symmetric around $t = 0$ (pt, qt)", ha="center", fontsize=8.3, fontweight="bold")

    # Right panel: Chi-Square
    x = np.linspace(0.05, 14, 300)
    chi_pdf = (x**1.5) * np.exp(-x / 2) / 10.0
    rx = 5.5 + x * 0.29
    ry = 0.75 + chi_pdf * 7.2
    mask = x >= 9.2
    ax.fill_between(rx[mask], 0.75, ry[mask], color=MID_GRAY)
    ax.plot(rx, ry, color=INK, lw=2.0)
    ax.plot([5.4, 9.6], [0.75, 0.75], color=INK, lw=1.4)
    ax.text(7.5, 3.35, r"B. Right-Skewed $\chi^2(\nu)$ Density", ha="center", fontweight="bold", fontsize=8.8)
    ax.text(7.5, 0.35, r"Positive support $x \geq 0$ (pchisq, qchisq)", ha="center", fontsize=8.3, fontweight="bold")
    save_fig(fig, "diagram_ch09_student_t_chisq.png")

    # 7. Six Sigma Cpk
    fig, ax = new_canvas(6.4, 2.5, (0, 10), (0, 3.9))
    x = np.linspace(-3.5, 3.5, 400)
    # Shifted bell curve centered at x = 5.6
    bx = 5.6 + x * 0.65
    by = 0.85 + np.exp(-0.5 * x**2) * 2.15
    ax.fill_between(bx, 0.85, by, color=SOFT_BG)
    ax.plot(bx, by, color=INK, lw=2.2)
    ax.plot([1.0, 9.0], [0.85, 0.85], color=INK, lw=1.5)
    lsl, usl = 2.0, 8.0
    ax.plot([lsl, lsl], [0.65, 3.45], color=INK, lw=2.0, ls="--")
    ax.plot([usl, usl], [0.65, 3.45], color=INK, lw=2.0, ls="--")
    ax.plot([5.6, 5.6], [0.85, 3.0], color=SLATE, lw=1.4, ls=":")
    ax.text(lsl, 3.55, "LSL", ha="center", fontweight="bold")
    ax.text(usl, 3.55, "USL", ha="center", fontweight="bold")
    ax.text(5.6, 3.15, r"Shifted Mean $\mu$", ha="center", fontweight="bold")
    draw_arrow(ax, 5.6, 2.15, usl, 2.15, lw=1.5, style="<->")
    ax.text((5.6 + usl) / 2, 2.45, r"$\mathrm{USL}-\mu = 3\,\sigma\,\mathrm{CPU}$", ha="center", fontweight="bold", fontsize=8.4,
            bbox=dict(boxstyle="round,pad=0.1", facecolor="#FFFFFF", edgecolor="none"))
    draw_arrow(ax, lsl, 0.35, usl, 0.35, label=r"Tolerance Window $\mathrm{USL} - \mathrm{LSL}$   |   $\mathrm{Cpk} = \min(\mathrm{CPU}, \mathrm{CPL})$", label_offset=(0, -0.2), style="<->")
    save_fig(fig, "diagram_ch09_six_sigma_cpk.png")


def main() -> None:
    print("Generating 59 publication-grade diagrams for Volume III...")
    gen_intro()
    gen_ch01()
    gen_ch02()
    gen_ch03()
    gen_ch04()
    gen_ch05()
    gen_ch06()
    gen_ch07()
    gen_ch08()
    gen_ch09()

    pngs = sorted(OUT_DIR.glob("diagram_*.png"))
    print(f"Generated {len(pngs)} diagrams in {OUT_DIR}")

    # Sync to Website/static/img/manuals/diagrams/domains and stackcalc if present
    sync_dirs = [
        REPO_ROOT / "Website" / "static" / "img" / "manuals" / "diagrams" / "domains",
        REPO_ROOT.parent / "stackcalc" / "documentation" / "manuals" / "assets" / "diagrams" / "domains",
        REPO_ROOT.parent / "stackcalc" / "docs" / "assets" / "manuals" / "diagrams" / "domains",
    ]
    for d in sync_dirs:
        if d.parent.parent.exists():
            d.mkdir(parents=True, exist_ok=True)
            for p in pngs:
                shutil.copy2(p, d / p.name)
            print(f"Synced {len(pngs)} diagrams to {d}")


if __name__ == "__main__":
    main()
