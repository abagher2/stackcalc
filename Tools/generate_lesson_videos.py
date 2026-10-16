"""Tools/generate_lesson_videos.py

Generates publication-grade 1280x720 24fps animated lesson videos for all StackCalc
hardware manipulative kits and RPN calculators.

Lessons are drawn directly from:
- docs/curriculum/teacher-guide.md
- docs/curriculum/rpn-elementary-guide.md
- docs/curriculum/worksheets.md
- docs/products/<kit>/lessons.md

Output: docs/assets/videos/<filename>.mp4
"""

import os
import sys
import math
import argparse
import subprocess
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
FPS = 24
DURATION = 8  # 8 seconds per video = 192 frames (fast render, crisp pacing)
TOTAL_FRAMES = FPS * DURATION

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'docs', 'assets', 'videos')

# Try system fonts with fallbacks
def get_fonts():
    try:
        f_title = ImageFont.truetype('/System/Library/Fonts/SFNSMono.ttf', 24)
        f_sub = ImageFont.truetype('/System/Library/Fonts/SFNSMono.ttf', 16)
        f_mono = ImageFont.truetype('/System/Library/Fonts/SFNSMono.ttf', 14)
        f_bold = ImageFont.truetype('/System/Library/Fonts/SFNSMono.ttf', 18)
        f_tag = ImageFont.truetype('/System/Library/Fonts/SFNSMono.ttf', 12)
        f_large = ImageFont.truetype('/System/Library/Fonts/SFNSMono.ttf', 32)
    except Exception:
        f_title = f_sub = f_mono = f_bold = f_tag = f_large = ImageFont.load_default()
    return {
        'title': f_title,
        'sub': f_sub,
        'mono': f_mono,
        'bold': f_bold,
        'tag': f_tag,
        'large': f_large,
    }

def ease_out_cubic(t):
    return 1 - (1 - t) ** 3

def ease_in_out(t):
    return 0.5 * (1 - math.cos(math.pi * t))

def draw_header_and_chrome(draw, fonts, sku, kit_name, lesson_num, title, standard, t):
    # Base background: Deep Slate Obsidian
    # Subtle technical grid
    for x in range(0, W, 40):
        draw.line([(x, 0), (x, H)], fill=(17, 24, 38))
    for y in range(0, H, 40):
        draw.line([(0, y), (W, y)], fill=(17, 24, 38))

    # Top Header Bar
    draw.rectangle([(40, 24), (W - 40, 84)], fill=(13, 18, 30), outline=(36, 48, 70), width=1)
    
    # SKU pill
    draw.rectangle([(55, 36), (150, 72)], fill=(2, 132, 199))
    draw.text((68, 46), sku, fill=(255, 255, 255), font=fonts['tag'])

    # Lesson Pill
    draw.rectangle([(160, 36), (260, 72)], fill=(30, 41, 59), outline=(71, 85, 105))
    draw.text((172, 46), lesson_num, fill=(56, 189, 248), font=fonts['tag'])

    # Title
    draw.text((275, 44), title[:52], fill=(248, 250, 252), font=fonts['sub'])

    # Standard badge right
    draw.text((W - 320, 46), standard, fill=(148, 163, 184), font=fonts['tag'])

    # Left Viewport Box (Interactive Manipulation Simulation)
    draw.rectangle([(40, 96), (720, 620)], fill=(11, 15, 25), outline=(30, 41, 59), width=1)
    # Left Viewport Label
    draw.rectangle([(55, 108), (240, 132)], fill=(20, 28, 45))
    draw.text((65, 113), "// CPA CONCRETE STAGE", fill=(56, 189, 248), font=fonts['tag'])

    # Right Info Box (Abstract Pedagogy & Diagnostic Cue)
    draw.rectangle([(736, 96), (W - 40, 620)], fill=(13, 18, 30), outline=(30, 41, 59), width=1)

    # Bottom Progress Bar
    p_y = 636
    draw.rectangle([(40, p_y), (W - 40, 680)], fill=(13, 18, 30), outline=(30, 41, 59), width=1)
    
    # Phase indicators
    phase = 1 if t < 2.6 else (2 if t < 5.4 else 3)
    p1_fill = (2, 132, 199) if phase == 1 else (20, 28, 45)
    p2_fill = (217, 119, 6) if phase == 2 else (20, 28, 45)
    p3_fill = (5, 150, 105) if phase == 3 else (20, 28, 45)
    
    draw.rectangle([(55, p_y + 8), (420, p_y + 36)], fill=p1_fill)
    draw.text((75, p_y + 14), "1. CONCRETE EXPLORATION", fill=(255, 255, 255), font=fonts['tag'])

    draw.rectangle([(435, p_y + 8), (810, p_y + 36)], fill=p2_fill)
    draw.text((455, p_y + 14), "2. SPATIAL MANIPULATION", fill=(255, 255, 255), font=fonts['tag'])

    draw.rectangle([(825, p_y + 8), (W - 55, p_y + 36)], fill=p3_fill)
    draw.text((845, p_y + 14), "3. MATHEMATICAL PROOF", fill=(255, 255, 255), font=fonts['tag'])


def draw_right_panel(draw, fonts, steps, cue, t):
    x0 = 756
    y0 = 116
    phase = 1 if t < 2.6 else (2 if t < 5.4 else 3)

    # Step 1 Card
    s1_border = (56, 189, 248) if phase == 1 else (30, 41, 59)
    draw.rectangle([(x0, y0), (W - 60, y0 + 100)], fill=(17, 24, 38), outline=s1_border, width=1)
    draw.text((x0 + 15, y0 + 12), "PHASE 1: CONCRETE SETUP", fill=(56, 189, 248), font=fonts['tag'])
    draw.text((x0 + 15, y0 + 38), steps[0][:48], fill=(241, 245, 249), font=fonts['mono'])
    if len(steps[0]) > 48:
        draw.text((x0 + 15, y0 + 62), steps[0][48:100], fill=(148, 163, 184), font=fonts['tag'])

    # Step 2 Card
    y1 = y0 + 112
    s2_border = (245, 158, 11) if phase == 2 else (30, 41, 59)
    draw.rectangle([(x0, y1), (W - 60, y1 + 100)], fill=(17, 24, 38), outline=s2_border, width=1)
    draw.text((x0 + 15, y1 + 12), "PHASE 2: REPRESENTATIONAL ACTION", fill=(245, 158, 11), font=fonts['tag'])
    draw.text((x0 + 15, y1 + 38), steps[1][:48], fill=(241, 245, 249), font=fonts['mono'])
    if len(steps[1]) > 48:
        draw.text((x0 + 15, y1 + 62), steps[1][48:100], fill=(148, 163, 184), font=fonts['tag'])

    # Step 3 Card
    y2 = y1 + 112
    s3_border = (16, 185, 129) if phase == 3 else (30, 41, 59)
    draw.rectangle([(x0, y2), (W - 60, y2 + 100)], fill=(17, 24, 38), outline=s3_border, width=1)
    draw.text((x0 + 15, y2 + 12), "PHASE 3: ABSTRACT VERIFICATION", fill=(16, 185, 129), font=fonts['tag'])
    draw.text((x0 + 15, y2 + 38), steps[2][:48], fill=(241, 245, 249), font=fonts['mono'])
    if len(steps[2]) > 48:
        draw.text((x0 + 15, y2 + 62), steps[2][48:100], fill=(148, 163, 184), font=fonts['tag'])

    # Teacher Diagnostic Callout
    y3 = y2 + 112
    draw.rectangle([(x0, y3), (W - 60, y3 + 70)], fill=(30, 20, 10), outline=(217, 119, 6), width=1)
    draw.text((x0 + 15, y3 + 10), "TEACHER DIAGNOSTIC CUE:", fill=(251, 191, 36), font=fonts['tag'])
    draw.text((x0 + 15, y3 + 34), cue[:54], fill=(254, 243, 199), font=fonts['tag'])
    if len(cue) > 54:
        draw.text((x0 + 15, y3 + 50), cue[54:110], fill=(254, 243, 199), font=fonts['tag'])


# ==============================================================================
# LESSON RENDERING FUNCTIONS (Left Viewport Animations)
# ==============================================================================

def render_frac_equivalence(draw, fonts, t):
    # Floor at y=560
    draw.line([(60, 560), (700, 560)], fill=(71, 85, 105), width=2)
    # Datum line at 84mm (y=260) and 42mm (y=410)
    draw.line([(60, 410), (700, 410)], fill=(16, 185, 129), width=1)
    draw.text((80, 390), "WATERLINE: 42.0mm (1/2 DATUM)", fill=(16, 185, 129), font=fonts['tag'])

    # 1/2 block: x=140 to 220, height 150px (y=410 to 560)
    draw.rectangle([(140, 410), (220, 560)], fill=(2, 132, 199), outline=(56, 189, 248), width=2)
    draw.text((165, 475), "1/2", fill=(255, 255, 255), font=fonts['bold'])
    draw.text((150, 570), "42.0mm", fill=(148, 163, 184), font=fonts['tag'])

    # Two 1/4 blocks: x=260 to 340
    # Block 1 in place
    draw.rectangle([(260, 485), (340, 560)], fill=(217, 119, 6), outline=(251, 191, 36), width=2)
    draw.text((285, 515), "1/4", fill=(255, 255, 255), font=fonts['mono'])
    # Block 2 drops down if t > 2.0
    y_target = 410
    if t < 2.0:
        y_curr = 200
        alpha = 0.3
    else:
        prog = min(1.0, (t - 2.0) * 1.5)
        y_curr = int(200 + (y_target - 200) * ease_out_cubic(prog))
    draw.rectangle([(260, y_curr), (340, y_curr + 75)], fill=(217, 119, 6), outline=(251, 191, 36), width=2)
    draw.text((285, y_curr + 25), "1/4", fill=(255, 255, 255), font=fonts['mono'])
    draw.text((270, 570), "2 x 21mm", fill=(148, 163, 184), font=fonts['tag'])

    # Four 1/8 blocks: x=380 to 460
    # 3 in place
    for i in range(3):
        by = 560 - (i + 1) * 37
        draw.rectangle([(380, by), (460, by + 37)], fill=(124, 58, 237), outline=(167, 139, 250), width=1)
        draw.text((405, by + 10), "1/8", fill=(255, 255, 255), font=fonts['tag'])
    # 4th block drops if t > 4.5
    if t > 4.5:
        prog = min(1.0, (t - 4.5) * 1.5)
        y_curr = int(220 + (410 - 220) * ease_out_cubic(prog))
    else:
        y_curr = 220
    draw.rectangle([(380, y_curr), (460, y_curr + 37)], fill=(124, 58, 237), outline=(167, 139, 250), width=1)
    draw.text((405, y_curr + 10), "1/8", fill=(255, 255, 255), font=fonts['tag'])
    draw.text((390, 570), "4 x 10.5mm", fill=(148, 163, 184), font=fonts['tag'])

    if t > 6.0:
        draw.rectangle([(120, 320), (500, 360)], fill=(5, 150, 105))
        draw.text((150, 332), "FLUSH TOPS PROVE: 1/2 = 2/4 = 4/8", fill=(255, 255, 255), font=fonts['sub'])


def render_frac_denominators(draw, fonts, t):
    draw.line([(60, 560), (700, 560)], fill=(71, 85, 105), width=2)
    # Stacking 1/2 (150px) + 1/4 (75px) = 225px total (y = 560 - 225 = 335)
    draw.line([(60, 335), (700, 335)], fill=(245, 158, 11), width=1)
    draw.text((80, 315), "TARGET SUM HEIGHT: 63.0mm (3/4)", fill=(245, 158, 11), font=fonts['tag'])

    # Tower 1: 1/2 + 1/4
    draw.rectangle([(160, 410), (250, 560)], fill=(2, 132, 199), outline=(56, 189, 248), width=2)
    draw.text((190, 475), "1/2", fill=(255, 255, 255), font=fonts['bold'])
    draw.rectangle([(160, 335), (250, 410)], fill=(217, 119, 6), outline=(251, 191, 36), width=2)
    draw.text((190, 365), "1/4", fill=(255, 255, 255), font=fonts['mono'])

    # Tower 2: Three 1/4 blocks matching beside it
    for i in range(2):
        by = 560 - (i + 1) * 75
        draw.rectangle([(320, by), (410, by + 75)], fill=(217, 119, 6), outline=(251, 191, 36), width=2)
        draw.text((350, by + 28), "1/4", fill=(255, 255, 255), font=fonts['mono'])

    if t > 3.0:
        prog = min(1.0, (t - 3.0) * 1.5)
        y_curr = int(180 + (335 - 180) * ease_out_cubic(prog))
    else:
        y_curr = 180
    draw.rectangle([(320, y_curr), (410, y_curr + 75)], fill=(217, 119, 6), outline=(251, 191, 36), width=2)
    draw.text((350, y_curr + 28), "1/4", fill=(255, 255, 255), font=fonts['mono'])

    if t > 5.5:
        draw.rectangle([(140, 240), (520, 285)], fill=(5, 150, 105))
        draw.text((160, 254), "COMMON DENOMINATOR: 1/2 + 1/4 = 3/4", fill=(255, 255, 255), font=fonts['sub'])


def render_ten_subitizing(draw, fonts, t):
    # Draw Ten-Frame tray (2x5 grid)
    tx, ty = 120, 240
    cw, ch = 90, 90
    draw.rectangle([(tx - 10, ty - 10), (tx + 5 * cw + 10, ty + 2 * ch + 10)], fill=(17, 24, 38), outline=(71, 85, 105), width=2)
    for r in range(2):
        for c in range(5):
            draw.rectangle([(tx + c * cw, ty + r * ch), (tx + (c + 1) * cw, ty + (r + 1) * ch)], outline=(30, 41, 59), width=1)

    # Top row: 5 red counters fill
    num_top = 5 if t > 1.0 else int(t * 5)
    for c in range(num_top):
        cx = tx + c * cw + cw // 2
        cy = ty + ch // 2
        draw.ellipse([(cx - 32, cy - 32), (cx + 32, cy + 32)], fill=(225, 29, 72), outline=(251, 113, 133), width=2)

    # Bottom row: 2 yellow counters slide in
    if t > 3.0:
        prog = min(1.0, (t - 3.0) * 1.5)
        for c in range(2):
            cx = tx + c * cw + cw // 2
            cy = ty + ch + ch // 2
            draw.ellipse([(cx - 32, cy - 32), (cx + 32, cy + 32)], fill=(234, 179, 8), outline=(253, 224, 71), width=2)

    if t > 5.0:
        draw.rectangle([(140, 480), (540, 530)], fill=(2, 132, 199))
        draw.text((160, 495), "SUBITIZE: 5 (TOP) + 2 (BOTTOM) = 7", fill=(255, 255, 255), font=fonts['sub'])


def render_ten_make_ten(draw, fonts, t):
    # Two Ten-frames side by side
    # Frame 1 has 8, Frame 2 has 5
    tx1, ty = 80, 200
    tx2 = 380
    cw, ch = 52, 52
    draw.rectangle([(tx1 - 5, ty - 5), (tx1 + 5 * cw + 5, ty + 2 * ch + 5)], fill=(17, 24, 38), outline=(71, 85, 105), width=2)
    draw.rectangle([(tx2 - 5, ty - 5), (tx2 + 5 * cw + 5, ty + 2 * ch + 5)], fill=(17, 24, 38), outline=(71, 85, 105), width=2)
    draw.text((tx1 + 60, ty - 30), "FRAME 1: [8]", fill=(56, 189, 248), font=fonts['tag'])
    draw.text((tx2 + 60, ty - 30), "FRAME 2: [5]", fill=(245, 158, 11), font=fonts['tag'])

    # Frame 1: 8 blue counters
    for i in range(8):
        r, c = divmod(i, 5)
        cx = tx1 + c * cw + cw // 2
        cy = ty + r * ch + ch // 2
        draw.ellipse([(cx - 18, cy - 18), (cx + 18, cy + 18)], fill=(2, 132, 199))

    # Frame 2: 3 counters remain, 2 migrate if t > 3.0
    for i in range(3):
        r, c = divmod(i, 5)
        cx = tx2 + c * cw + cw // 2
        cy = ty + r * ch + ch // 2
        draw.ellipse([(cx - 18, cy - 18), (cx + 18, cy + 18)], fill=(245, 158, 11))

    # Migrating 2 counters into Frame 1 spots (1,3) and (1,4)
    prog = min(1.0, max(0.0, (t - 3.0) * 1.5))
    for idx, (target_c, orig_c) in enumerate([(3, 3), (4, 4)]):
        dest_x = tx1 + target_c * cw + cw // 2
        dest_y = ty + ch + ch // 2
        orig_x = tx2 + orig_c * cw + cw // 2
        orig_y = ty + ch // 2
        cur_x = int(orig_x + (dest_x - orig_x) * ease_in_out(prog))
        cur_y = int(orig_y + (dest_y - orig_y) * ease_in_out(prog))
        draw.ellipse([(cur_x - 18, cur_y - 18), (cur_x + 18, cur_y + 18)], fill=(245, 158, 11), outline=(253, 224, 71), width=2)

    if t > 5.5:
        draw.rectangle([(100, 360), (560, 410)], fill=(5, 150, 105))
        draw.text((120, 375), "MAKE TEN: 8 + 5 = 10 (FULL) + 3 = 13", fill=(255, 255, 255), font=fonts['sub'])


def render_domino_doubles(draw, fonts, t):
    # Dominos [6|6]
    dx, dy = 200, 200
    dw, dh = 140, 280
    draw.rectangle([(dx, dy), (dx + dw, dy + dh)], fill=(248, 250, 252), outline=(15, 23, 42), width=3)
    draw.line([(dx + 10, dy + dh // 2), (dx + dw - 10, dy + dh // 2)], fill=(15, 23, 42), width=3)

    # 6 pips top
    pips = [(35, 35), (35, 70), (35, 105), (105, 35), (105, 70), (105, 105)]
    for px, py in pips:
        draw.ellipse([(dx + px - 8, dy + py - 8), (dx + px + 8, dy + py + 8)], fill=(15, 23, 42))
    # 6 pips bottom
    for px, py in pips:
        draw.ellipse([(dx + px - 8, dy + dh // 2 + py - 8), (dx + px + 8, dy + dh // 2 + py + 8)], fill=(15, 23, 42))

    draw.text((dx + 160, dy + 50), "TOP: 6 PIPS", fill=(56, 189, 248), font=fonts['mono'])
    draw.text((dx + 160, dy + dh // 2 + 50), "BOTTOM: 6 PIPS", fill=(56, 189, 248), font=fonts['mono'])

    if t > 3.0:
        draw.rectangle([(160, 520), (560, 570)], fill=(2, 132, 199))
        draw.text((180, 535), "DOUBLES ANCHOR: 6 + 6 = 12", fill=(255, 255, 255), font=fonts['sub'])


def render_domino_near_doubles(draw, fonts, t):
    # Domino [6|7] or [6|6] + 1
    dx, dy = 160, 200
    dw, dh = 120, 240
    # Left tile: [6|6]
    draw.rectangle([(dx, dy), (dx + dw, dy + dh)], fill=(248, 250, 252), outline=(15, 23, 42), width=2)
    draw.line([(dx + 5, dy + dh // 2), (dx + dw - 5, dy + dh // 2)], fill=(15, 23, 42), width=2)
    draw.text((dx + 30, dy + dh // 2 - 15), "[6|6]", fill=(15, 23, 42), font=fonts['bold'])
    draw.text((dx + 25, dy + dh + 10), "SUM: 12", fill=(56, 189, 248), font=fonts['tag'])

    # Right tile: [6|7] (or 6+6 +1 pip)
    dx2 = 340
    draw.rectangle([(dx2, dy), (dx2 + dw, dy + dh)], fill=(248, 250, 252), outline=(15, 23, 42), width=2)
    draw.line([(dx2 + 5, dy + dh // 2), (dx2 + dw - 5, dy + dh // 2)], fill=(15, 23, 42), width=2)
    draw.text((dx2 + 30, dy + dh // 2 - 15), "[6|7]", fill=(15, 23, 42), font=fonts['bold'])
    draw.text((dx2 + 20, dy + dh + 10), "SUM: 13 (+1)", fill=(245, 158, 11), font=fonts['tag'])

    if t > 4.0:
        draw.rectangle([(120, 490), (560, 540)], fill=(5, 150, 105))
        draw.text((140, 505), "NEAR-DOUBLES: 6 + 7 = (6+6) + 1 = 13", fill=(255, 255, 255), font=fonts['sub'])


def render_tiles_scaling(draw, fonts, t):
    # 12 tiles in a row equaling 84.0mm whole
    draw.line([(60, 360), (660, 360)], fill=(71, 85, 105), width=2)
    draw.line([(60, 310), (660, 310)], fill=(16, 185, 129), width=1)
    draw.text((80, 280), "FRACTION STUDIO DATUM: 84.0mm WHOLE", fill=(16, 185, 129), font=fonts['tag'])

    start_x = 100
    tile_w = 40
    num_tiles = min(12, int(t * 2.5))
    for i in range(num_tiles):
        tx = start_x + i * tile_w
        draw.rectangle([(tx, 320), (tx + tile_w - 2, 360)], fill=(2, 132, 199), outline=(56, 189, 248), width=1)
        draw.text((tx + 12, 335), str(i + 1), fill=(255, 255, 255), font=fonts['tag'])

    if num_tiles == 12:
        draw.text((start_x + 120, 380), "12 TILES x 7.0mm = 84.0mm (1/1)", fill=(56, 189, 248), font=fonts['mono'])


def render_tiles_distributive(draw, fonts, t):
    # 7x8 array broken into 5x8 and 2x8
    ox, oy = 140, 200
    tw = 30
    # 5x8 green tiles
    for r in range(7):
        for c in range(8):
            color = (5, 150, 105) if r < 5 else (217, 119, 6)
            draw.rectangle([(ox + c * tw, oy + r * tw), (ox + (c + 1) * tw - 2, oy + (r + 1) * tw - 2)], fill=color)

    # Dividing line
    draw.line([(ox - 10, oy + 5 * tw - 1), (ox + 8 * tw + 10, oy + 5 * tw - 1)], fill=(255, 255, 255), width=2)
    draw.text((ox + 8 * tw + 20, oy + 40), "5 x 8 = 40", fill=(52, 211, 153), font=fonts['tag'])
    draw.text((ox + 8 * tw + 20, oy + 160), "2 x 8 = 16", fill=(251, 191, 36), font=fonts['tag'])

    if t > 4.5:
        draw.rectangle([(100, 450), (560, 500)], fill=(2, 132, 199))
        draw.text((120, 465), "DISTRIBUTIVE: 7x8 = 40 + 16 = 56", fill=(255, 255, 255), font=fonts['sub'])


def render_prime_fundamental(draw, fonts, t):
    # Slide rule scale & prime blocks 2 and 3
    draw.line([(120, 160), (120, 560)], fill=(148, 163, 184), width=2)
    # Ticks for 1, 2, 3, 4, 6
    for val, y in [(1, 540), (2, 450), (3, 395), (6, 270)]:
        draw.line([(110, y), (130, y)], fill=(148, 163, 184), width=1)
        draw.text((80, y - 8), f"{val}", fill=(148, 163, 184), font=fonts['tag'])

    # Tower A: [2] block (y: 540 to 450) + [3] block (y: 450 to 270)
    draw.rectangle([(180, 450), (280, 540)], fill=(2, 132, 199), outline=(56, 189, 248), width=2)
    draw.text((220, 485), "[2]", fill=(255, 255, 255), font=fonts['bold'])
    
    if t > 2.5:
        prog = min(1.0, (t - 2.5) * 1.5)
        top_y = int(180 + (270 - 180) * ease_out_cubic(prog))
    else:
        top_y = 180
    draw.rectangle([(180, top_y), (280, top_y + 180)], fill=(217, 119, 6), outline=(251, 191, 36), width=2)
    draw.text((220, top_y + 80), "[3]", fill=(255, 255, 255), font=fonts['bold'])

    # Block [6] beside it
    if t > 5.0:
        draw.rectangle([(320, 270), (420, 540)], fill=(5, 150, 105), outline=(52, 211, 153), width=2)
        draw.text((360, 395), "[6]", fill=(255, 255, 255), font=fonts['bold'])
        draw.line([(130, 270), (430, 270)], fill=(251, 191, 36), width=2)
        draw.text((150, 210), "LOG STACKING: 2 x 3 = 6 (FLUSH)", fill=(251, 191, 36), font=fonts['sub'])


def render_prime_lcm_gcd(draw, fonts, t):
    # Towers 12 = 2*2*3 and 18 = 2*3*3
    draw.text((140, 180), "TOWER 12: [2][2][3]", fill=(56, 189, 248), font=fonts['tag'])
    draw.text((340, 180), "TOWER 18: [2][3][3]", fill=(245, 158, 11), font=fonts['tag'])

    # Tower 12 blocks
    draw.rectangle([(140, 460), (220, 520)], fill=(2, 132, 199))
    draw.text((170, 480), "2", fill=(255, 255, 255), font=fonts['tag'])
    draw.rectangle([(140, 400), (220, 460)], fill=(2, 132, 199))
    draw.text((170, 420), "2", fill=(255, 255, 255), font=fonts['tag'])
    draw.rectangle([(140, 310), (220, 400)], fill=(217, 119, 6))
    draw.text((170, 345), "3", fill=(255, 255, 255), font=fonts['tag'])

    # Tower 18 blocks
    draw.rectangle([(340, 460), (420, 520)], fill=(2, 132, 199))
    draw.text((370, 480), "2", fill=(255, 255, 255), font=fonts['tag'])
    draw.rectangle([(340, 370), (420, 460)], fill=(217, 119, 6))
    draw.text((370, 405), "3", fill=(255, 255, 255), font=fonts['tag'])
    draw.rectangle([(340, 280), (420, 370)], fill=(217, 119, 6))
    draw.text((370, 315), "3", fill=(255, 255, 255), font=fonts['tag'])

    if t > 4.5:
        draw.rectangle([(100, 540), (520, 585)], fill=(5, 150, 105))
        draw.text((120, 552), "INTERSECTION (GCD): 2 x 3 = 6", fill=(255, 255, 255), font=fonts['sub'])


def render_clock_gearing(draw, fonts, t):
    # Clock Face centered at 340, 360
    cx, cy, r = 340, 360, 160
    draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=(17, 24, 38), outline=(71, 85, 105), width=3)
    # 12 Hour markings
    for h in range(1, 13):
        ang = math.radians(h * 30 - 90)
        hx = cx + (r - 25) * math.cos(ang)
        hy = cy + (r - 25) * math.sin(ang)
        draw.text((hx - 6, hy - 8), str(h), fill=(248, 250, 252), font=fonts['tag'])

    # Animated rotation: minute hand rotates, hour hand rotates 1/12th
    min_deg = (t * 90) % 360
    hr_deg = (t * 90 / 12) + 60 # Starts around 2 o'clock

    # Hour hand
    ang_hr = math.radians(hr_deg - 90)
    draw.line([(cx, cy), (cx + 80 * math.cos(ang_hr), cy + 80 * math.sin(ang_hr))], fill=(56, 189, 248), width=5)
    # Minute hand
    ang_min = math.radians(min_deg - 90)
    draw.line([(cx, cy), (cx + 125 * math.cos(ang_min), cy + 125 * math.sin(ang_min))], fill=(245, 158, 11), width=3)
    draw.ellipse([(cx - 8, cy - 8), (cx + 8, cy + 8)], fill=(255, 255, 255))

    draw.text((220, 540), "12:1 CONTINUOUS PLANETARY GEARING", fill=(56, 189, 248), font=fonts['tag'])


def render_clock_elapsed(draw, fonts, t):
    # Clock face with 15-min pie wedges
    cx, cy, r = 340, 360, 150
    draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=(17, 24, 38), outline=(71, 85, 105), width=2)
    # Fill pie wedges from 12 to 9 (45 mins)
    num_wedges = min(3, int(t * 0.75))
    for w in range(num_wedges):
        # 15 min sector
        ang_start = w * 90
        ang_end = (w + 1) * 90
        draw.pieslice([(cx - r + 5, cy - r + 5), (cx + r - 5, cy + r - 5)], ang_start - 90, ang_end - 90, fill=(2, 132, 199, 100), outline=(56, 189, 248))

    draw.text((200, 530), f"ELAPSED TIME: {num_wedges * 15} MINUTES", fill=(251, 191, 36), font=fonts['sub'])


def render_algebra_foil(draw, fonts, t):
    # Area model for (x+2)(x+1) = x^2 + 3x + 2
    ox, oy = 180, 220
    xw = 160
    uw = 50
    # x^2 square (160x160)
    draw.rectangle([(ox, oy), (ox + xw, oy + xw)], fill=(2, 132, 199), outline=(56, 189, 248), width=2)
    draw.text((ox + 65, oy + 70), "x^2", fill=(255, 255, 255), font=fonts['large'])

    # 1 x-bar right (50x160)
    draw.rectangle([(ox + xw + 4, oy), (ox + xw + 4 + uw, oy + xw)], fill=(5, 150, 105), outline=(52, 211, 153), width=2)
    draw.text((ox + xw + 20, oy + 70), "x", fill=(255, 255, 255), font=fonts['bold'])

    # 2 x-bars bottom (160x50 and 160x50)
    draw.rectangle([(ox, oy + xw + 4), (ox + xw, oy + xw + 4 + uw)], fill=(5, 150, 105), outline=(52, 211, 153), width=2)
    draw.text((ox + 75, oy + xw + 18), "x", fill=(255, 255, 255), font=fonts['bold'])
    draw.rectangle([(ox, oy + xw + uw + 8), (ox + xw, oy + xw + 2 * uw + 8)], fill=(5, 150, 105), outline=(52, 211, 153), width=2)
    draw.text((ox + 75, oy + xw + uw + 22), "x", fill=(255, 255, 255), font=fonts['bold'])

    # 2 unit squares bottom-right (50x50 each)
    if t > 3.0:
        draw.rectangle([(ox + xw + 4, oy + xw + 4), (ox + xw + 4 + uw, oy + xw + 4 + uw)], fill=(217, 119, 6), outline=(251, 191, 36), width=2)
        draw.text((ox + xw + 22, oy + xw + 18), "1", fill=(255, 255, 255), font=fonts['bold'])
        draw.rectangle([(ox + xw + 4, oy + xw + uw + 8), (ox + xw + 4 + uw, oy + xw + 2 * uw + 8)], fill=(217, 119, 6), outline=(251, 191, 36), width=2)
        draw.text((ox + xw + 22, oy + xw + uw + 22), "1", fill=(255, 255, 255), font=fonts['bold'])

    if t > 5.0:
        draw.rectangle([(120, 520), (560, 570)], fill=(124, 58, 237))
        draw.text((140, 535), "AREA: (x+2)(x+1) = x^2 + 3x + 2", fill=(255, 255, 255), font=fonts['sub'])


def render_algebra_factoring(draw, fonts, t):
    # Trinomial factoring on L-frame: x^2 + 5x + 6 = (x+2)(x+3)
    ox, oy = 180, 200
    # Outer L-frame
    draw.line([(ox - 15, oy - 15), (ox - 15, oy + 280)], fill=(251, 191, 36), width=4)
    draw.line([(ox - 15, oy - 15), (ox + 320, oy - 15)], fill=(251, 191, 36), width=4)
    draw.text((ox + 80, oy - 40), "LENGTH: (x + 3)", fill=(251, 191, 36), font=fonts['tag'])
    draw.text((ox - 110, oy + 120), "WIDTH:\n(x + 2)", fill=(251, 191, 36), font=fonts['tag'])

    # Tiles in place
    draw.rectangle([(ox, oy), (ox + 140, oy + 140)], fill=(2, 132, 199))
    draw.text((ox + 50, oy + 60), "x^2", fill=(255, 255, 255), font=fonts['large'])

    if t > 4.0:
        draw.rectangle([(100, 510), (580, 560)], fill=(5, 150, 105))
        draw.text((120, 525), "FACTORS FOUND: (x + 2)(x + 3)", fill=(255, 255, 255), font=fonts['sub'])


def render_dice_large_numbers(draw, fonts, t):
    # Bar chart of 6 outcomes converging to 16.7%
    bx, by = 120, 240
    bw = 60
    gap = 25
    draw.line([(bx - 10, by + 240), (bx + 6 * (bw + gap), by + 240)], fill=(148, 163, 184), width=2)
    # Expected line
    draw.line([(bx - 10, by + 80), (bx + 6 * (bw + gap), by + 80)], fill=(251, 191, 36), width=1)
    draw.text((bx + 6 * (bw + gap) - 100, by + 55), "THEORETICAL: 16.7%", fill=(251, 191, 36), font=fonts['tag'])

    for i in range(6):
        # Progressively smooth heights
        noise = math.sin(i * 3 + t * 4) * max(0.0, (1.0 - t / 7.0)) * 50
        h_bar = int(160 + noise)
        x = bx + i * (bw + gap)
        draw.rectangle([(x, by + 240 - h_bar), (x + bw, by + 240)], fill=(2, 132, 199), outline=(56, 189, 248))
        draw.text((x + 24, by + 250), f"[{i+1}]", fill=(255, 255, 255), font=fonts['tag'])

    draw.text((160, 530), "EMPIRICAL PROBABILITY CONVERGES (N=1,000)", fill=(56, 189, 248), font=fonts['tag'])


def render_dice_sum_dist(draw, fonts, t):
    # Two-dice sum triangle
    bx, by = 100, 240
    for s in range(2, 13):
        ways = 6 - abs(s - 7)
        h_bar = ways * 30
        x = bx + (s - 2) * 44
        color = (245, 158, 11) if s == 7 else (2, 132, 199)
        draw.rectangle([(x, by + 200 - h_bar), (x + 36, by + 200)], fill=color)
        draw.text((x + 8, by + 210), str(s), fill=(255, 255, 255), font=fonts['tag'])

    draw.text((bx + 5 * 44 - 10, by - 10), "PEAK: 7 (6/36)", fill=(245, 158, 11), font=fonts['tag'])
    draw.text((140, 500), "TRIANGULAR SUM DISTRIBUTION (2 TO 12)", fill=(56, 189, 248), font=fonts['sub'])


def render_volvelle_coordinates(draw, fonts, t):
    # Unit circle with rotating angle arm
    cx, cy, r = 340, 360, 150
    draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=(71, 85, 105), width=2)
    draw.line([(cx - r - 20, cy), (cx + r + 20, cy)], fill=(51, 65, 85))
    draw.line([(cx, cy - r - 20), (cx, cy + r + 20)], fill=(51, 65, 85))

    # Angle 30 deg (pi/6)
    ang = math.radians(30)
    px = cx + r * math.cos(ang)
    py = cy - r * math.sin(ang)
    draw.line([(cx, cy), (px, py)], fill=(245, 158, 11), width=3)
    # Right triangle
    draw.line([(px, cy), (px, py)], fill=(16, 185, 129), width=2)
    draw.line([(cx, cy), (px, cy)], fill=(2, 132, 199), width=2)

    draw.text((px + 10, py - 10), "(sqrt(3)/2, 1/2)", fill=(248, 250, 252), font=fonts['mono'])
    draw.text((180, 540), "ROTARY APERTURE: theta=30 deg (pi/6)", fill=(56, 189, 248), font=fonts['sub'])


def render_volvelle_tangent(draw, fonts, t):
    cx, cy, r = 340, 360, 140
    draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=(71, 85, 105), width=2)
    # 90 deg vertical line
    draw.line([(cx, cy), (cx, cy - r)], fill=(225, 29, 72), width=4)
    draw.text((cx + 15, cy - r), "(0, 1) -> tan(90) UNDEFINED", fill=(244, 63, 94), font=fonts['bold'])
    draw.text((160, 530), "SLOPE = 1/0 -> VERTICAL ASYMPTOTE", fill=(244, 63, 94), font=fonts['sub'])


def render_sc32_stack(draw, fonts, t):
    # SC-32 4-line LCD screen visualization
    lx, ly = 120, 200
    lw, lh = 440, 240
    draw.rectangle([(lx, ly), (lx + lw, ly + lh)], fill=(20, 30, 25), outline=(71, 85, 105), width=3)
    # 4 lines: T, Z, Y, X
    draw.text((lx + 20, ly + 25), "T:          0.0000", fill=(148, 163, 184), font=fonts['mono'])
    draw.text((lx + 20, ly + 75), "Z:          0.0000", fill=(148, 163, 184), font=fonts['mono'])
    
    val_y = "         20.0000" if t > 3.0 else "          0.0000"
    val_x = "        200.0000" if t > 5.5 else ("         10.0000" if t > 3.0 else "         12.0000")
    
    draw.text((lx + 20, ly + 125), f"Y: {val_y}", fill=(56, 189, 248), font=fonts['mono'])
    draw.text((lx + 20, ly + 175), f"X: {val_x}", fill=(52, 211, 153), font=fonts['large'])

    draw.text((140, 480), "KEYSTROKES: [12] ENTER [8] + [15] ENTER [5] - [*]", fill=(245, 158, 11), font=fonts['tag'])
    draw.text((180, 520), "RESULT = (12+8) x (15-5) = 200.0000", fill=(52, 211, 153), font=fonts['sub'])


def render_sc32_continued_frac(draw, fonts, t):
    lx, ly = 120, 200
    lw, lh = 440, 240
    draw.rectangle([(lx, ly), (lx + lw, ly + lh)], fill=(20, 30, 25), outline=(71, 85, 105), width=3)
    draw.text((lx + 20, ly + 30), "CONTINUED FRACTION: sqrt(2)", fill=(148, 163, 184), font=fonts['tag'])
    draw.text((lx + 20, ly + 100), "RADICAL PYRAMID STACK TRACE", fill=(56, 189, 248), font=fonts['tag'])
    draw.text((lx + 20, ly + 160), "X:  1.4142135623", fill=(52, 211, 153), font=fonts['large'])
    draw.text((160, 500), "EVALUATES FROM INSIDE-OUT IN 6 KEYS", fill=(251, 191, 36), font=fonts['sub'])


def render_sc6_remainder(draw, fonts, t):
    # SC-6 Elementary division 17 / 5 = 3 R 2
    lx, ly = 120, 200
    lw, lh = 440, 240
    draw.rectangle([(lx, ly), (lx + lw, ly + lh)], fill=(13, 27, 42), outline=(71, 85, 105), width=3)
    draw.text((lx + 20, ly + 25), "SC-6 ELEMENTARY MODE [g] [÷R]", fill=(56, 189, 248), font=fonts['tag'])
    draw.text((lx + 20, ly + 80), "Y (REMAINDER R):    2", fill=(245, 158, 11), font=fonts['large'])
    draw.text((lx + 20, ly + 150), "X (QUOTIENT Q):     3", fill=(52, 211, 153), font=fonts['large'])
    draw.text((140, 480), "KEYSTROKES: [17] ENTER [5] [g] [÷R]", fill=(245, 158, 11), font=fonts['tag'])
    draw.text((160, 520), "17 ÷ 5 = 3 WHOLE (X) + 2 LEFTOVER (Y)", fill=(248, 250, 252), font=fonts['sub'])


def render_sc6_simplification(draw, fonts, t):
    # SC-6 Step-by-step SIMP 12/18 -> 6/9 -> 2/3
    lx, ly = 120, 200
    lw, lh = 440, 240
    draw.rectangle([(lx, ly), (lx + lw, ly + lh)], fill=(13, 27, 42), outline=(71, 85, 105), width=3)
    draw.text((lx + 20, ly + 25), "SC-6 FRACTION REDUCTION [SIMP]", fill=(56, 189, 248), font=fonts['tag'])
    
    if t < 3.0:
        frac_txt = "12 / 18"
        fac_txt = "FACTOR = ?"
    elif t < 5.5:
        frac_txt = " 6 /  9"
        fac_txt = "DIVIDED BY: 2"
    else:
        frac_txt = " 2 /  3"
        fac_txt = "DIVIDED BY: 3 (FULLY REDUCED)"

    draw.text((lx + 40, ly + 80), f"LCD: {frac_txt}", fill=(52, 211, 153), font=fonts['large'])
    draw.text((lx + 40, ly + 160), fac_txt, fill=(245, 158, 11), font=fonts['bold'])
    draw.text((160, 500), "STEP-BY-STEP FRACTION FACTOR DISCOVERY", fill=(56, 189, 248), font=fonts['sub'])


def render_sc6_skip_counting(draw, fonts, t):
    # SC-6 Rhythmic Skip-Counting [REP] by 7
    lx, ly = 120, 200
    lw, lh = 440, 240
    draw.rectangle([(lx, ly), (lx + lw, ly + lh)], fill=(13, 27, 42), outline=(71, 85, 105), width=3)
    draw.text((lx + 20, ly + 25), "SC-6 MULTIPLICATION LADDER [REP]", fill=(56, 189, 248), font=fonts['tag'])

    steps_7 = [7, 14, 21, 28, 35, 42]
    curr_idx = min(len(steps_7) - 1, int(t * 0.8))
    draw.text((lx + 40, ly + 80), f"MULTIPLE: 7 x {curr_idx + 1}", fill=(245, 158, 11), font=fonts['bold'])
    draw.text((lx + 40, ly + 140), f"REGISTER X: {steps_7[curr_idx]}", fill=(52, 211, 153), font=fonts['large'])
    draw.text((160, 500), "PRESS [+] REPEATEDLY TO CLIMB FACT LADDER", fill=(56, 189, 248), font=fonts['sub'])


# ==============================================================================
# LESSON CATALOG (23 Lessons Across All 11 Hardware Kits & Calculators)
# ==============================================================================

LESSONS = [
    # 1. Fraction Studio (FRAC-01)
    {
        'id': 'fraction-studio-lesson-equivalence',
        'sku': 'FRAC-01',
        'kit_name': 'FRACTION STUDIO',
        'lesson_num': 'LESSON 01',
        'title': 'Concrete Equivalence: 1/2 = 2/4 = 4/8 Flush Datum',
        'standard': 'CCSS 3.NF.A.3 • TEKS 111.5.b.3',
        'steps': [
            'Place 1/2 block (42mm) at benchmark gauge waterline.',
            'Stack two 1/4 blocks beside it (2x21mm = 42mm).',
            'Fingertips confirm: top surfaces align perfectly flush.'
        ],
        'cue': 'Hand student 1/8 and 1/2 blocks: physical height disproves "bigger denominator means bigger fraction" immediately.',
        'render': render_frac_equivalence
    },
    {
        'id': 'fraction-studio-lesson-denominators',
        'sku': 'FRAC-01',
        'kit_name': 'FRACTION STUDIO',
        'lesson_num': 'LESSON 02',
        'title': 'Tactile Addition: 1/2 + 1/4 Common Denominators',
        'standard': 'CCSS 5.NF.A.1 • TEKS 111.7.b.3',
        'steps': [
            'Combine 1/2 and 1/4 blocks into a single 63.0mm tower.',
            'Test candidate blocks until three 1/4 towers match flush.',
            'Conclude: 1/2 converts physically to 2/4, giving 3/4.'
        ],
        'cue': 'Stops "add across denominators" error: 2/6 block height visibly fails to reach the 63.0mm mark.',
        'render': render_frac_denominators
    },

    # 2. Ten-Frames & Carry Shelf (BASE-10)
    {
        'id': 'ten-frames-lesson-subitizing',
        'sku': 'BASE-10',
        'kit_name': 'TEN-FRAMES',
        'lesson_num': 'LESSON 01',
        'title': 'Instant Subitizing: Recognizing 7 as 5 + 2 (<180ms)',
        'standard': 'CCSS K.CC.B.5 • 1.OA.C.6',
        'steps': [
            'Fill top 5-cell row with red counters instantaneously.',
            'Place 2 yellow counters in bottom row.',
            'Recognize total 7 without slow one-by-one counting.'
        ],
        'cue': 'Anchor of 5 eliminates finger counting; student sees structured groupings directly.',
        'render': render_ten_subitizing
    },
    {
        'id': 'ten-frames-lesson-make-ten',
        'sku': 'BASE-10',
        'kit_name': 'TEN-FRAMES',
        'lesson_num': 'LESSON 02',
        'title': 'Make-Ten Regrouping: 8 + 5 = 10 + 3 onto Carry Shelf',
        'standard': 'CCSS 1.OA.B.3 • 2.OA.B.2',
        'steps': [
            'Load Frame 1 with 8 counters and Frame 2 with 5 counters.',
            'Slide 2 counters from Frame 2 across to complete Frame 1.',
            'Frame 1 becomes 1 Ten; 3 remainder sit on carry shelf.'
        ],
        'cue': 'Physical sliding transfers directly to the standard place-value carry algorithm.',
        'render': render_ten_make_ten
    },

    # 3. Math Dominoes (DOMI-01)
    {
        'id': 'math-dominoes-lesson-doubles',
        'sku': 'DOMI-01',
        'kit_name': 'MATH DOMINOES',
        'lesson_num': 'LESSON 01',
        'title': 'Doubles Anchors of Mental Math: 6 + 6 = 12',
        'standard': 'CCSS 1.OA.C.6 • 2.OA.B.2',
        'steps': [
            'Dock double tiles [1|1] through [6|6] in lid sockets.',
            'Observe dual symmetry of pip configurations.',
            'Memorize anchor sums: 2, 4, 6, 8, 10, 12.'
        ],
        'cue': 'Doubles serve as mental keystones; students recall 6+6 faster than any other single-digit sum.',
        'render': render_domino_doubles
    },
    {
        'id': 'math-dominoes-lesson-near-doubles',
        'sku': 'DOMI-01',
        'kit_name': 'MATH DOMINOES',
        'lesson_num': 'LESSON 02',
        'title': 'Near-Doubles Fluency: 6 + 7 = (6 + 6) + 1 = 13',
        'standard': 'CCSS 2.OA.B.2',
        'steps': [
            'Compare [6|6] tile with adjacent [6|7] tile in box well.',
            'Spot the single isolated pip difference (+1).',
            'Derive 6 + 7 by recalling 6 + 6 and adding 1.'
        ],
        'cue': 'Prevents counting up 7 fingers; builds relational decomposition thinking.',
        'render': render_domino_near_doubles
    },

    # 4. Counting Tiles (TILE-01)
    {
        'id': 'counting-tiles-lesson-scaling',
        'sku': 'TILE-01',
        'kit_name': 'COUNTING TILES',
        'lesson_num': 'LESSON 01',
        'title': '1U Fraction Scaling: 12 Counting Tiles = 84.0mm Whole',
        'standard': 'CCSS 3.MD.C.5 • 3.NF.A.1',
        'steps': [
            'Align 12 counting tiles side-by-side on the workbench.',
            'Measure row against Fraction Studio 84.0mm datum.',
            'Prove: 12 tiles x 7.0mm = 84.0mm (1/1 whole).'
        ],
        'cue': 'Bridges discrete counting tiles directly into continuous vertical fraction blocks.',
        'render': render_tiles_scaling
    },
    {
        'id': 'counting-tiles-lesson-distributive',
        'sku': 'TILE-01',
        'kit_name': 'COUNTING TILES',
        'lesson_num': 'LESSON 02',
        'title': 'Distributive Property: 7 x 8 = (5 x 8) + (2 x 8) = 56',
        'standard': 'CCSS 3.OA.B.5 • 4.NBT.B.5',
        'steps': [
            'Assemble 7 rows of 8 tiles into a rectangular area.',
            'Insert ruler divider after row 5 (splitting 5 and 2).',
            'Sum the sub-arrays: 40 + 16 = 56 tiles total.'
        ],
        'cue': 'Memorizing 7x8 is hard; splitting 7 into friendly 5 and 2 makes mental math effortless.',
        'render': render_tiles_distributive
    },

    # 5. Prime Factor Studio (PRIME-01)
    {
        'id': 'prime-factor-lesson-fundamental',
        'sku': 'PRIME-01',
        'kit_name': 'PRIME FACTOR',
        'lesson_num': 'LESSON 01',
        'title': 'Fundamental Theorem: Multiplicative Stacking 2 x 3 = 6',
        'standard': 'CCSS 6.NS.B.4 • 4.OA.B.4',
        'steps': [
            'Stack [2] and [3] logarithmic blocks on desk workbench.',
            'Read height against engraved scale: reads exactly 6.0.',
            'Verify: prime towers multiply heights, not add.'
        ],
        'cue': 'Corrects linear addition habit: blocks are scaled logarithmically so height sum = product.',
        'render': render_prime_fundamental
    },
    {
        'id': 'prime-factor-lesson-lcm-gcd',
        'sku': 'PRIME-01',
        'kit_name': 'PRIME FACTOR',
        'lesson_num': 'LESSON 02',
        'title': 'LCM & GCD Venn Stacking: Factors of 12 and 18',
        'standard': 'CCSS 6.NS.B.4',
        'steps': [
            'Build Tower 12 ([2][2][3]) and Tower 18 ([2][3][3]).',
            'Extract shared blocks to form GCD = [2][3] = 6.',
            'Combine unique blocks to form LCM = [2][2][3][3] = 36.'
        ],
        'cue': 'Replaces abstract factor trees with tactile union and intersection sets.',
        'render': render_prime_lcm_gcd
    },

    # 6. Classroom Clock (TIME-01)
    {
        'id': 'classroom-clock-lesson-gearing',
        'sku': 'TIME-01',
        'kit_name': 'CLASSROOM CLOCK',
        'lesson_num': 'LESSON 01',
        'title': '12:1 Planetary Gearing: Continuous Hand Synchronization',
        'standard': 'CCSS 2.MD.C.7 • 3.MD.A.1',
        'steps': [
            'Rotate minute hand one full 360-degree revolution.',
            'Internal 12:1 planetary gears advance hour hand 30 degrees.',
            'Observe: hour hand never points to false hour at half-past.'
        ],
        'cue': 'Eliminates "half-past 3 looks like 4" false reading caused by loose friction gears.',
        'render': render_clock_gearing
    },
    {
        'id': 'classroom-clock-lesson-elapsed',
        'sku': 'TIME-01',
        'kit_name': 'CLASSROOM CLOCK',
        'lesson_num': 'LESSON 02',
        'title': 'Elapsed Time with 15-Minute Quadrant Wedges',
        'standard': 'CCSS 3.MD.A.1 • 4.MD.A.2',
        'steps': [
            'Set clock to start time 2:15.',
            'Insert three 15-minute quadrant wedges to reach 3:00.',
            'Count total duration: 15 + 15 + 15 = 45 minutes elapsed.'
        ],
        'cue': 'Circular sector wedges make duration a visible area rather than abstract subtraction.',
        'render': render_clock_elapsed
    },

    # 7. Algebra Factoring Boxes (ALGB-01)
    {
        'id': 'algebra-boxes-lesson-foil',
        'sku': 'ALGB-01',
        'kit_name': 'ALGEBRA BOXES',
        'lesson_num': 'LESSON 01',
        'title': 'FOIL Area Model: (x + 2)(x + 1) = x^2 + 3x + 2',
        'standard': 'CCSS HSA.APR.A.1 • HSA.SSE.A.2',
        'steps': [
            'Align L-frame with length (x + 2) and width (x + 1).',
            'Fill corner with x^2 square tile; fill arms with 3 x-bars.',
            'Complete corner with 2 unit squares: area equals x^2+3x+2.'
        ],
        'cue': 'Polynomial multiplication is literally the area of a closed geometric rectangle.',
        'render': render_algebra_foil
    },
    {
        'id': 'algebra-boxes-lesson-factoring',
        'sku': 'ALGB-01',
        'kit_name': 'ALGEBRA BOXES',
        'lesson_num': 'LESSON 02',
        'title': 'Trinomial Factoring on 90-Degree L-Frame: x^2 + 5x + 6',
        'standard': 'CCSS HSA.SSE.B.3.A',
        'steps': [
            'Take 1 x^2 tile, 5 x-bars, and 6 unit squares.',
            'Rearrange pieces until they snap into a solid rectangle.',
            'Read border dimensions on L-frame: (x + 2) and (x + 3).'
        ],
        'cue': 'Factoring is the reverse of area calculation: finding dimensions from total tile count.',
        'render': render_algebra_factoring
    },

    # 8. Probability Dice & Spinner (PROB-01)
    {
        'id': 'dice-spinner-lesson-large-numbers',
        'sku': 'PROB-01',
        'kit_name': 'PROBABILITY',
        'lesson_num': 'LESSON 01',
        'title': 'Law of Large Numbers: Frequency Convergence to 16.7%',
        'standard': 'CCSS 7.SP.C.6 • 7.SP.C.7',
        'steps': [
            'Roll balanced center-of-mass die across 10, 100, 1000 trials.',
            'Track relative frequency of each face 1 through 6.',
            'Observe fluctuations smooth into uniform 1/6 (16.7%).'
        ],
        'cue': 'Proves theoretical randomness requires mass-balanced precision debossed cavities.',
        'render': render_dice_large_numbers
    },
    {
        'id': 'dice-spinner-lesson-sum-dist',
        'sku': 'PROB-01',
        'kit_name': 'PROBABILITY',
        'lesson_num': 'LESSON 02',
        'title': 'Two-Dice Triangular Sum Distribution: Why 7 Wins',
        'standard': 'CCSS 7.SP.C.8 • HSS.MD.A.1',
        'steps': [
            'Plot 6x6 grid of 36 ordered pairs (Die A, Die B).',
            'Sum diagonals from 2 (1/36) up to 12 (1/36).',
            'Identify peak at sum 7 (6 combinations = 16.7%).'
        ],
        'cue': 'Shows why 7 is 6 times more likely than rolling snake eyes or boxcars.',
        'render': render_dice_sum_dist
    },

    # 9. Unit Circle Volvelle (VOLV-01)
    {
        'id': 'volvelle-lesson-coordinates',
        'sku': 'VOLV-01',
        'kit_name': 'VOLVELLE',
        'lesson_num': 'LESSON 01',
        'title': 'Aperture Coordinate Alignment: theta = 30 deg (pi/6)',
        'standard': 'CCSS HSF.TF.A.2 • HSF.TF.A.3',
        'steps': [
            'Rotate top disc until index hairline aligns to 30 deg.',
            'Read exact coordinate pair through radial aperture window.',
            'Confirm: (cos theta, sin theta) = (sqrt(3)/2, 1/2).'
        ],
        'cue': 'Replaces rote table memorization with direct spatial angle alignment.',
        'render': render_volvelle_coordinates
    },
    {
        'id': 'volvelle-lesson-tangent',
        'sku': 'VOLV-01',
        'kit_name': 'VOLVELLE',
        'lesson_num': 'LESSON 02',
        'title': 'Tangent Slope & Undefined Asymptote at 90 deg (pi/2)',
        'standard': 'CCSS HSF.TF.A.2',
        'steps': [
            'Rotate dial to 90 degrees (pi/2 radians).',
            'Aperture displays coordinate (0, 1).',
            'Calculate tan(90) = sin/cos = 1/0 -> UNDEFINED ASYMPTOTE.'
        ],
        'cue': 'Physical vertical line has infinite/undefined slope; resolves division by zero.',
        'render': render_volvelle_tangent
    },

    # 10. SC-32 Scientific Calculator (SC-32)
    {
        'id': 'sc32-lesson-stack',
        'sku': 'SC-32',
        'kit_name': 'SC-32 RPN',
        'lesson_num': 'LESSON 01',
        'title': '4-Line Stack Dynamics & Zero-Parentheses Execution',
        'standard': 'CCSS HSN.Q.A.1 • Collegiate STEM',
        'steps': [
            'Enter first expression (12 + 8): [12] ENTER [8] [+].',
            'Enter second expression (15 - 5): [15] ENTER [5] [-].',
            'Multiply stacks with [*]: LCD displays 200.0000.'
        ],
        'cue': 'RPN evaluates inside-out; no parentheses keys needed, intermediate results visible.',
        'render': render_sc32_stack
    },
    {
        'id': 'sc32-lesson-continued-fractions',
        'sku': 'SC-32',
        'kit_name': 'SC-32 RPN',
        'lesson_num': 'LESSON 02',
        'title': 'Radical Pyramids & Continued Fractions Evaluation',
        'standard': 'Texas UIL Calculator Applications Standard',
        'steps': [
            'Evaluate nested radical sqrt(2 + sqrt(2 + sqrt(2))).',
            'Execute inside-out with single keypresses [2] [+] [sqrt].',
            'Save 350+ keystrokes per tournament exam.'
        ],
        'cue': 'UIL competitors shave 4 minutes off their sprint test using RPN register flow.',
        'render': render_sc32_continued_frac
    },

    # 11. SC-6 Elementary Calculator (SC-6)
    {
        'id': 'sc6-lesson-remainder',
        'sku': 'SC-6',
        'kit_name': 'SC-6 ELEM',
        'lesson_num': 'LESSON 01',
        'title': 'Integer Division with Remainder [g] [÷R]: 17 ÷ 5 = 3 R 2',
        'standard': 'CCSS 4.OA.A.3 • 4.NBT.B.6',
        'steps': [
            'Enter dividend and divisor: [17] ENTER [5].',
            'Press [g] [÷R] for elementary division mode.',
            'Screen displays Line X: 3 (Quotient), Line Y: 2 (Remainder).'
        ],
        'cue': 'Shows both whole cookies (3) and leftover cookies (2) without decimal confusion.',
        'render': render_sc6_remainder
    },
    {
        'id': 'sc6-lesson-simplification',
        'sku': 'SC-6',
        'kit_name': 'SC-6 ELEM',
        'lesson_num': 'LESSON 02',
        'title': 'Step-by-Step Fraction Simplification [SIMP]: 12/18 -> 2/3',
        'standard': 'CCSS 4.NF.A.1 • 5.NF.A.1',
        'steps': [
            'Enter fraction: [12] [/] [18].',
            'Press [SIMP]: displays 6/9 and identifies common factor 2.',
            'Press [SIMP] again: displays 2/3 and common factor 3.'
        ],
        'cue': 'Reveals prime factors step-by-step rather than jumping straight to the end.',
        'render': render_sc6_simplification
    },
    {
        'id': 'sc6-lesson-skip-counting',
        'sku': 'SC-6',
        'kit_name': 'SC-6 ELEM',
        'lesson_num': 'LESSON 03',
        'title': 'Rhythmic Skip-Counting & Fact Ladders [REP] by 7',
        'standard': 'CCSS 3.OA.C.7 • 3.OA.D.9',
        'steps': [
            'Enter factor step: [7] [g] [x≶y] (REP mode).',
            'Press [+] repeatedly to advance multiples: 14, 21, 28, 35...',
            'Chant multiplication cadence in sync with tactile button click.'
        ],
        'cue': 'Connects auditory rhythm with tactile key response to cement multiplication tables.',
        'render': render_sc6_skip_counting
    }
]


def render_video(lesson, fonts):
    vid_id = lesson['id']
    out_path = os.path.join(OUTPUT_DIR, f"{vid_id}.mp4")
    print(f"--> Rendering [{lesson['sku']}] {lesson['title']} -> {out_path}")

    cmd = [
        'ffmpeg', '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-s', f'{W}x{H}',
        '-pix_fmt', 'rgb24',
        '-r', str(FPS),
        '-i', '-',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'fast',
        '-crf', '20',
        out_path
    ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    for f in range(TOTAL_FRAMES):
        t = f / FPS
        img = Image.new('RGB', (W, H), (11, 15, 23))
        draw = ImageDraw.Draw(img)

        # Chrome layout
        draw_header_and_chrome(draw, fonts, lesson['sku'], lesson['kit_name'], lesson['lesson_num'], lesson['title'], lesson['standard'], t)

        # Right side cards & diagnostic cue
        draw_right_panel(draw, fonts, lesson['steps'], lesson['cue'], t)

        # Left side manipulative animation
        lesson['render'](draw, fonts, t)

        proc.stdin.write(img.tobytes())

    proc.stdin.close()
    proc.wait()
    file_size_kb = os.path.getsize(out_path) // 1024
    print(f"    Done: {out_path} ({file_size_kb} KB)")


def main():
    parser = argparse.ArgumentParser(description="Generate StackCalc animated lesson videos.")
    parser.add_argument('--all', action='store_true', help="Generate all 23 lesson videos")
    parser.add_argument('--sku', type=str, help="Generate videos for a specific SKU (e.g. FRAC-01, SC-6)")
    args = parser.parse_args()

    fonts = get_fonts()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    targets = LESSONS
    if args.sku:
        targets = [l for l in LESSONS if l['sku'].upper() == args.sku.upper()]

    print(f"Generating {len(targets)} lesson videos...")
    for idx, l in enumerate(targets):
        print(f"[{idx+1}/{len(targets)}] {l['id']}")
        render_video(l, fonts)
    print("All requested lesson videos generated successfully!")

if __name__ == '__main__':
    main()
