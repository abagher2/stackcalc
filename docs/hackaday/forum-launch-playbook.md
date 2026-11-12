---
title: "Forum & Community Launch Playbook (0-Day Account Friendly)"
description: "Copy-paste launch announcements for the Museum of HP Calculators, Hacker News (Show HN), Swift Forums, KiCad Forum, Raspberry Pi Forum, Teacher/Homeschool Forums, and Printables/MakerWorld—linked to their canonical blog posts."
---

# Synchronized Launch Playbook: Zero-Day Account Forum & Community Posts

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// LAUNCH PLANNING · HOLD UNTIL FIRST 5 HARDWARE UNITS VERIFIED</div>

> **Status:** Planning Stage — Hold all external forum and Launch Day posts until the first **5 Batch 001 calculators** arrive from PCBWay and pass the [7-Stage Board Arrival Protocol](board-arrival.md).

---

## 1. The Unifying Vision & Launch-Day Sequence (Targeting 11/10)

* **Vision:** A low-cost, kid-friendly, exam-legal RPN calculator that grows with the learner from 1st grade (`StackCalc 6` — Common Core K–6) through AP Calculus and professional engineering (`StackCalc 32`).
* **Why RPN Over Infix or CAS:**
  1. **Users Learn `Operator-Precedence Parsing`:** Instead of typing `(12 + 8) / (5 - 1) =` into an infix black box, RPN requires students to learn `operator-precedence parsing` in their own minds to decompose and enter expressions onto the visible stack—appreciating the lessons learned in the past 50 years of computing so they can build the next 50 years.
  2. **Designed to Be Allowed in Testing Situations:** Unlike CAS calculators (which are banned on the SAT, ACT, IB, UIL, NCEES FE/PE engineering exams, and university calculus midterms), StackCalc is purposefully built with zero CAS symbolic algebra, zero QWERTY keyboard, and zero wireless radios.
  3. **The \$250 Backpack Problem:** No parent wants a child carrying a \$250 boutique collector's calculator or a \$200 fragile eBay antique to school every day. We are launching our first small-batch maker units at **\$89.99** while scaling our Hardware V2 design (next 20-unit order) toward a **\$29.99 classroom target**.

### Canonical Blog Posts Mapped to Each Forum Announcement

| Community / Forum | Canonical Blog Post in Repository | Published URL on `stackcalc.io` |
| :--- | :--- | :--- |
| **1. Museum of HP Calculators Forum** | [Shipping StackCalc v1.1 (SC-6 to SC-32)](../blog/posts/2026-10-23-shipping-stackcalc-v1-1-sc32-and-sc6.md) | `https://www.stackcalc.io/blog/2026/10/23/shipping-stackcalc-v1-1-sc32-and-sc6/` |
| **2. Hacker News (`Show HN`)** | [Launch Day: Kid-Friendly RPN Calculator & Ecosystem](../blog/posts/2026-10-28-launch-day-kid-friendly-rpn-calculator-and-ecosystem.md) | `https://www.stackcalc.io/blog/2026/10/28/launch-day-kid-friendly-rpn-calculator-and-ecosystem/` |
| **3. Official Swift Forums** | [Co-Developing SwiftUI & Embedded Swift with STL Digital Twin](../blog/posts/2026-10-25-co-developing-swiftui-and-embedded-swift-with-stl-digital-twin.md) | `https://www.stackcalc.io/blog/2026/10/25/co-developing-swiftui-and-embedded-swift-with-stl-digital-twin/` |
| **4. KiCad.info Forum** & **5. Raspberry Pi Forum** | [Notes from the PCBWay Assembly Floor & `dummy_pcb.stl`](../blog/posts/2026-10-20-pcbway-dfm-photos-and-jumper-fixes.md) | `https://www.stackcalc.io/blog/2026/10/20/pcbway-dfm-photos-and-jumper-fixes/` |
| **6. Teacher / Homeschool Forums** & **7. Printables** | [84mm Fraction Towers, Logarithmic Prime Blocks & Books](../blog/posts/2026-10-26-manufacturing-math-blocks-and-reference-books.md) | `https://www.stackcalc.io/blog/2026/10/26/manufacturing-math-blocks-and-reference-books/` |
| **TPU Button 280-Condition FEA Sweep** | [We Pressed One TPU Key 280 Ways](../blog/posts/2026-09-24-tpu-keypad-280-presses.md) | `https://www.stackcalc.io/blog/2026/09/24/we-pressed-one-tpu-key-280-ways-before-the-pcb-arrived/` |

---

## 2. Copy-Paste Forum Announcements

### Post 1: The Museum of HP Calculators Forum (`hpmuseum.org/forum`)
* **Where to Post:** `General Forum` (`https://www.hpmuseum.org/forum/forum-2.html`)
* **Canonical Website Post:** [Shipping StackCalc v1.1 on the App Store: A Clean-Room RPN Calculator That Grows With Your Kid (SC-6 to SC-32)](../blog/posts/2026-10-23-shipping-stackcalc-v1-1-sc32-and-sc6.md) (`https://www.stackcalc.io/blog/2026/10/23/shipping-stackcalc-v1-1-sc32-and-sc6/`)

**Title:**
`StackCalc 32: Why I Built a Kid-Friendly, Clean-Room HP-32SII Successor (and Ecosystem) After Training My Kids on a DM41CC`

**Body:**
```text
Hello everyone,

I have been lurking here for years and wanted to share a project that grew directly out of teaching my own kids RPN—and invite feedback from this community.

First, a bit of personal background: I fell in love with RPN on an HP-32SII in high school and was heartbroken when I no longer had it. Over the years I bought a few vintage HP-32SII units off eBay, but the aging switch feel and build quality were disappointing. Like many of you, I turned to SwissMicros: I own a DM42 (which I converted to a C47, including printing and cutting the overlays), a DM32, a DM41CC, and a DM15CC.

I actually trained my kids on my DM41CC. They picked up the stack effortlessly—which proved to me that kids don't struggle with RPN; they struggle with infix parentheses! Better yet, because a postfix stack has no hidden infix parser, **students actually learn operator-precedence parsing in their own minds** to enter expressions onto the stack, seeing every intermediate result step by step. And unlike CAS calculators (which are banned on the SAT, ACT, IB, and university/FE exams), our hardware is purposefully designed to be allowed in testing situations (no CAS, no QWERTY keyboard, and no wireless radios). But there was no way I was going to send a child to school every day with a $250 boutique calculator or a $200 vintage eBay antique in their backpack. Our long-term goal is a durable, kid-friendly RPN calculator at a $29.99 classroom price point (we are launching our first small maker batch at $89.99 while we scale up volume).

### Why the HP-32SII Architecture Instead of the HP-15C or HP-42S?
When designing StackCalc 32 (`SC-32`), I thought hard about whether to model the workflow on the 15C, 42S, or 32SII:
- Why not the HP-42S / C47? As much as I love my C47 and 42S on the bench, burying everyday functions inside multi-layer softkey menus slows down learners and hides what the instrument can do.
- Why not the HP-15C? The landscape form factor and memorized numeric matrix/label codes are iconic, but less approachable for a student's first scientific instrument.
- Why the HP-32SII? The 32SII hit the ergonomics sweet spot: almost every essential scientific operation lives directly on the primary or shifted keys (zero menu diving for daily math), while a single-line context menu cleanly handles `CLEAR`, `STAT`, `SOLVE`, and `INTG`.

### Not an Emulator: A Clean-Room Engine (`RPNCore`) with Deliberate Upgrades
StackCalc 32 is not a ROM emulator or microcode wrapper. It is a clean-room engine written from scratch in Swift (`RPNCore`) that compiles both to our iPhone/iPad/standalone Apple Watch app and to bare-metal silicon on the Raspberry Pi RP2350. Writing our own engine let us keep the classic 4-level stack (`X, Y, Z, T`), `LASTx`, and 26 lettered registers (`A–Z`) while adding features I always wished the 32SII had:
1. Harmonic Mean (`H.M.`) alongside arithmetic and weighted means in `STAT`.
2. Built-in Time Value of Money (`TVM`) solver (`N`, `I%YR`, `PV`, `PMT`, `FV`).
3. Dedicated Quadratic & Cubic Polynomial Root Solver (`POLY`) with complex root support.
4. Interactive Function & Scatter-Plot Graphing (`PLOT`) on the app and 132×65 graphic LCD.

### Growing With the Student: `StackCalc 6` (Common Core K–6) & The Tactile Ecosystem
To help kids start before high school, our app and firmware also include `StackCalc 6` (`SC-6`)—an elementary RPN mode covering every key operation in Common Core math up through 6th grade:
- Whole-number integer division with remainder (`÷R`), prime factorization (`[PRIME]`), `GCD`/`LCM`, ratio tables, and elapsed clock time.
- Step-by-Step Fraction Simplification (`[SIMP]`): Instead of silently jumping from `12/18` to `2/3`, pressing `[SIMP]` in `SC-6` factors out one prime divisor per press so a student sees *how* the fraction reduces.
- Live dot-matrix visualizations: Ten-Frames, a 20-bead Rekenrek rack, and proportional Number Lines.

Surrounding the calculator is a complete learning ecosystem:
- Physical 3D-Printed Math Blocks (available free on Printables or pre-printed on Etsy): Fraction Studio Proportional Towers, Prime Factor Studio & Slide Rule, Place Value Regrouping Trays, and Ten-Frames that dock onto 42mm Gridfinity desk lids.
- Unit-Test-Verified Books & Workbooks: Complete SC-32 and SC-6 Owner's Manuals plus 590+ graded problems (339-problem SC-32 Casebook, 253-problem SC-6 Workbook, and 24 UIL speed-calculation exams), compiled with an automated verification pipeline that executes every worked keystroke sequence against the calculator engine in unit tests so there are zero typos.

We just got our first 5 physical RP2350 calculators running on the bench (and wrote a blog post with the factory DFM photos PCBWay sent us when they caught our rear header pins colliding with a front softkey).

Links:
- Full Article on Why We Chose the HP-32SII Architecture (SC-32 & SC-6): https://www.stackcalc.io/blog/2026/10/23/shipping-stackcalc-v1-1-sc32-and-sc6/
- PCBWay Assembly Floor DFM & Switch Jumper Post: https://www.stackcalc.io/blog/2026/10/20/pcbway-dfm-photos-and-jumper-fixes/
- Main Site, Free Curriculum & Manuals: https://www.stackcalc.io
- App Store (iOS, iPadOS & 100% Standalone Apple Watch App): https://apps.apple.com/app/id6801788040
- Etsy Storefront (Founder's Batch Hardware & 3D-Printed Manipulative Block Kits): https://stackcalcmath.etsy.com
- Companion Books on Amazon: https://link.amazon/B0f5cP0Ur (SC-6) / https://link.amazon/B07DqTRR5 (SC-32)
- Hackaday.io Build Logs & Free STLs: https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator

I would love to hear your thoughts—especially from fellow 32SII, DM32, and C47 users!
```

---

### Post 2: Hacker News (`news.ycombinator.com/submit`) — `Show HN`
* **Where to Post:** `https://news.ycombinator.com/submit` (Tuesday morning, 6:30–8:30 AM PT)
* **Canonical Website Post:** [Launch Day: Why the World Needs a Kid-Friendly RPN Calculator That Grows With Them](../blog/posts/2026-10-28-launch-day-kid-friendly-rpn-calculator-and-ecosystem.md) (`https://www.stackcalc.io/blog/2026/10/28/launch-day-kid-friendly-rpn-calculator-and-ecosystem/`)

**Title (Under 80 chars):**
`Show HN: StackCalc – Using AI to build an open RPN calculator and math lab`

**URL:**
`https://www.stackcalc.io`

**First Comment to Post Immediately After Submitting:**
```text
Hi HN! I’m a software/AI engineer, and over the past year I used AI coding agents to help me cross into physical hardware engineering—designing a 4-layer RP2350 PCB, parametric OpenSCAD 3D-printed enclosures, 280-run FEA keypad physics simulations, and automated Blender studio renders.

The irony isn't lost on me: I used AI to build a deterministic, 100% offline pocket calculator and physical block set because I strongly believe that **despite the availability of AI, students still need to know math**.

Why build a stack-based RPN calculator for kids instead of just handing them a $20 infix Casio/TI calculator—or a CAS graphing calculator?
- First, an infix calculator hides order-of-operations inside a black box: the student types `(12 + 8) / (5 - 1) =`, sees zero intermediate state, and blindly trusts whatever pops out at the end. On a stack-based postfix calculator, **users have to learn operator-precedence parsing themselves** in order to decompose and enter expressions onto the stack. While the original 1970s motivation for RPN may have been hardware constraints, we want kids to appreciate the lessons learned in the past 50 years of computing (stack machines, AST post-order traversal, Forth/JVM/Wasm) so they can build the next 50 years.
- Second, handing students a CAS calculator doesn't work when **CAS calculators are banned on tests** (now banned on both the SAT and ACT, as well as IB, NCEES FE/PE engineering exams, and university calculus midterms). Our physical calculator is purposefully designed to be **allowed in testing situations**—strictly numeric/scientific with zero CAS symbolic algebra, zero QWERTY keyboard, and zero wireless transceivers. (And for parents who already love RPN, sending a kid to school with a $250 collector's DM41/DM42 isn't practical—so we are launching our small-batch maker units at $89.99 on a hardware roadmap toward a $29.99 student price point.)

Here is how we built the stack and what we’re launching today:

1. One Clean-Room Swift Core (`RPNCore`) + 40 Hz Differential Fuzzer:
We wrote a zero-dependency RPN engine in Swift that compiles to iOS, iPadOS, a 100% standalone watchOS app, and bare-metal Raspberry Pi RP2350 silicon (via Embedded Swift). To guarantee the bare-metal C/Swift firmware never diverges from the host engine, a grammar-based differential fuzzer hammers both surfaces at 40 Hz with random and adversarial postfix sequences.

2. Physics Simulations for the TPU Membrane Buttons & Screwless Enclosure:
Because 3D-printed calculator buttons often feel mushy or bind when pressed on a corner, we modeled our 43-key Shore 95A TPU keypad membrane in parametric OpenSCAD and ran a **280-condition Finite Element Analysis (FEA) physics sweep** (7 off-axis thumb angles up to 15° × 8 compass directions × 5 strike offsets):
- We simulated off-center corner presses to tune our faceplate aperture chamfers and membrane webbing thickness—guaranteeing that even a 15° diagonal thumb strike transmits clean vertical force to the SMD tactile switch plunger underneath without wedging against the wall or causing parasitic cross-talk on neighboring keys: https://www.stackcalc.io/blog/2026/09/24/we-pressed-one-tpu-key-280-ways-before-the-pcb-arrived/
- We also ran structural FEA on our 4-part screwless sliding enclosure to design a zero-preload serpentine top latch (0.0 MPa static stress when closed so PLA never creeps over time) and used KiCad's `pcbnew` Python API to generate a 3D-printable `dummy_pcb.stl` for physical fit checks—which helped us catch a factory floor DFM collision when PCBWay sent us photos of our rear Pico 2 header pins poking between the front SMD pads of a softkey: https://www.stackcalc.io/blog/2026/10/20/pcbway-dfm-photos-and-jumper-fixes/

3. 3D-Printed Math Blocks Engineered Around Mathematical Invariants:
To bridge physical intuition with the calculator's stack (especially in our `StackCalc 6` Common Core K–6 mode), we designed a modular suite of 42mm Gridfinity manipulatives manufactured in-house and on Slant3D (with free STLs on Printables):
- **84mm Datum Fraction Towers:** Standard plastic fraction bars drift when stacked due to decimal thicknesses. We chose an **84mm Whole (`1/1`) height datum** because 84 is divisible by 1, 2, 3, 4, 6, 7, and 12 into exact integer millimeters (42mm, 28mm, 21mm, 14mm, 12mm, 7mm)—eliminating 0.20mm FDM slicer rounding drift. Students stack `1/2 + 1/3` (70mm) against five `1/6` blocks in a comparator trough, then enter `.1.2 [ENTER] .1.3 [+]` on the calculator (or use `[SIMP]` in `SC-6` to factor out one prime divisor per key press).
- **Logarithmic Prime Factor Slide Rule:** We scaled our prime number blocks (`2, 3, 5, 7`) logarithmically (`Length ∝ log(p)`). Because `log(a) + log(b) = log(a × b)`, snapping a `2` block and a `3` block end-to-end inside the rail physically equals the exact length of the `6` marker—turning prime factorization (`[PRIME]`), `GCD`, and `LCM` into a physical length-matching puzzle.

4. Compiling Textbooks Like Firmware (`book_engine.py`):
We wrote two owner's manuals and 590+ graded workbook problems (covering `SC-6` Common Core K–6 visual math and `SC-32` scientific/calculus). Our `Makefile` extracts every worked keystroke sequence from the Markdown prose, runs it as an `XCTest` unit test against `RPNCore`, and auto-renders the exact 132×65 LCD screenshots and STL orthographic diagrams. If a book example disagrees with the engine, the build fails.

Explore the launch:
- Launch Day Engineering Post: https://www.stackcalc.io/blog/2026/10/28/launch-day-kid-friendly-rpn-calculator-and-ecosystem/
- App Store (v1.1 — iOS, iPadOS & Standalone watchOS, $0 subscriptions/ads): https://apps.apple.com/app/id6801788040
- Etsy Store (Batch 001 Hardware & 3D-Printed Manipulative Block Kits): https://stackcalcmath.etsy.com
- Companion Books on Amazon: https://link.amazon/B0f5cP0Ur (SC-6) / https://link.amazon/B07DqTRR5 (SC-32)
- Free STLs & Printables / Hackaday Logs: https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator

Happy to answer questions on Embedded Swift on RP2350, using AI for KiCad/OpenSCAD/FEA workflows, or teaching kids RPN!
```

---

### Post 3: Official Swift Forums (`forums.swift.org`)
* **Where to Post:** `Community Showcase` (`https://forums.swift.org/c/community-showcase/`) & `Embedded`
* **Canonical Website Post:** [Co-Developing an App Store App and Bare-Metal RP2350 Firmware with a Shared Swift Core and STL-Backed Digital Twin](../blog/posts/2026-10-25-co-developing-swiftui-and-embedded-swift-with-stl-digital-twin.md) (`https://www.stackcalc.io/blog/2026/10/25/co-developing-swiftui-and-embedded-swift-with-stl-digital-twin/`)

**Title:**
`StackCalc: Co-Developing an App Store App and Bare-Metal RP2350 Firmware with a Shared Swift Core and STL-Backed Digital Twin`

**Body:**
```markdown
Hi Swift community!

I’d love to share **StackCalc**, a project where we co-developed an iOS/iPadOS/standalone watchOS app and a physical Raspberry Pi RP2350 pocket RPN calculator from a single shared Swift package (`RPNCore`).

### 1. One Swift Codebase Across Apple Silicon and Bare-Metal RP2350
`RPNCore` is architected with zero external dependencies and deterministic value-type state so the exact same Swift code runs on:
- **iOS, iPadOS & Standalone watchOS (`StackCalc v1.1`):** Powering both `StackCalc 32` (4-level scientific RPN, numerical solver, Simpson integration, polynomial root finder, TVM, and curve plotting) and `StackCalc 6` (a K–6 Common Core visual stack that renders live Ten-Frames, Rekenrek bead racks, and number lines).
- **Bare-Metal RP2350 Firmware (Embedded Swift):** Compiled for `armv8m.main-none-eabi` and linked with a thin C hardware layer (`hardware_wrapper.c`) that scans our 43-key tactile switch matrix and drives a 132×65 ST7567 monochrome LCD over SPI.

### 2. Using Our Production STLs and Laser Decals for 1:1 Firmware/Hardware Co-Development
Waiting for PCB fabrication and 3D prints usually slows down firmware UX iteration. To solve this, we wired our hardware CAD pipeline directly into our Swift workspace:
- Our OpenSCAD generator (`generate_scad.py`) and laser decal scripts (`generate_laser_svg.py`) export the exact physical button geometry, keycap travel envelopes, and key legends into JSON layout registries (`layout_data.json` and `layout_data_sc6.json`).
- Inside the app (`HardwareReplicaView.swift` and `LCDDisplayView.swift`), SwiftUI renders an exact dimensional and pixel-level replica of the physical calculator—driving the identical 132×65 dot-matrix framebuffer (`RetroUI.swift`) and simulating physical switch boundaries via `CoreHaptics`.
- Our test suite (`SwiftUIVisualFuzzTests.swift` and our 40 Hz differential grammar fuzzer) runs keystroke sequences across the replica and exports live screenshots directly into our 590-problem companion workbooks and owner's manuals.

### Links & Resources
- **Full Swift + STL Digital Twin Architecture Post:** https://www.stackcalc.io/blog/2026/10/25/co-developing-swiftui-and-embedded-swift-with-stl-digital-twin/
- **App Store (Universal iOS, iPadOS & watchOS):** https://apps.apple.com/app/id6801788040
- **Hackaday Project & Open-Source STLs:** https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator
- **Etsy Storefront (Hardware & 3D-Printed Math Block Kits):** https://stackcalcmath.etsy.com
- **Companion Books on Amazon:** https://link.amazon/B0f5cP0Ur (SC-6) / https://link.amazon/B07DqTRR5 (SC-32)

Happy to dive into any details on sharing code between SwiftUI and Embedded Swift or automating textbook verification with `XCTest`!
```

---

### Post 4: KiCad.info Forum (`forum.kicad.info`)
* **Where to Post:** `Projects` (`https://forum.kicad.info/c/projects/12`)
* **Canonical Website Post:** [Notes from the PCBWay Assembly Floor: Header Pins, JST Footprints, and Switch Jumper Routing](../blog/posts/2026-10-20-pcbway-dfm-photos-and-jumper-fixes.md) (`https://www.stackcalc.io/blog/2026/10/20/pcbway-dfm-photos-and-jumper-fixes/`)

**Title:**
`StackCalc 32: Generating 3D-Printable Dummy PCBs from pcbnew for Test-Fitting + Real PCBWay Assembly Floor DFM Photos`

**Body:**
```markdown
Hello KiCad community,

I wanted to share two workflows that saved us a ton of enclosure rework on **StackCalc 32**, our open-hardware RP2350 scientific RPN calculator:

### 1. Exporting `dummy_pcb.scad` from `pcbnew` to 3D-Print Physical Fit-Check Boards
Our calculator uses a 4-part, 100% screwless sliding rail enclosure (`chassis`, `unified_faceplate`, `tpu_membrane`, and snap-fit `top_cap`) with tight clearances ($0.40\text{ mm}$ lateral PCB rail allowance and $0.10\text{ mm}$ front switch datum).

Rather than waiting weeks for fabricated fiberglass boards to discover a mechanical collision, we wrote `Hardware/generate_scad.py` using KiCad's Python API (`pcbnew`). Every time `make layout` runs, it inspects `calculator.kicad_pcb` and generates two OpenSCAD files:
- `pcb_layout_generated.scad`: Exports the exact $(X, Y)$ centers of all 43 tactile switches, the internal `Edge.Cuts` LCD FPC ribbon slot, and the rear component sweeps.
- `dummy_pcb.scad` $\rightarrow$ `dummy_pcb.stl`: A complete 3D-printable plastic replica of the populated PCB—including the $1.6\text{ mm}$ FR-4 substrate, all 43 switch bodies and stems, the rear `MCU1` Pico 2 envelope, the `J1` 0.5mm ZIF socket, `JST1`, and the `C1`–`C8` charge-pump capacitors.

By printing `dummy_pcb.stl` in PLA on our desktop printer, we could slide the populated "board" into the chassis rails, verify that all 43 TPU membrane plungers met the switch tops cleanly, and check top-cap battery wire clearances before ordering a single PCB.

### 2. What Software DRC Missed (Caught by PCBWay's Assembly Line Photos)
Even with zero DRC errors and a perfect `dummy_pcb` fit, our first turnkey PCBA run at PCBWay caught three real-world BOM/footprint traps (documented with factory bench photos in our blog post below):
1. **Rear Header Pins vs. Front Switch `SOFT6`:** Our BOM accidentally called out `SC1632` (Pico 2 with pre-soldered through-hole headers) with PTH pads on `B.Cu`. The pins poked straight through the board between the four SMD pads of front switch `SOFT6`. We wrote `fix_mcu_pads.py` to convert `MCU1` to pure bottom-side castellated SMD pads (`B.Cu`, zero drill) and switched to `SC1631`.
2. **JST Footprint Mismatch & Stranded Silkscreen:** Updated `JST1` from through-hole `S2B-PH-K-S` to SMD `S2B-PH-SM4-TB` and wrote `fix_silkscreen.py` to move stranded `F.Silkscreen` graphics inside flipped footprints to `B.Silkscreen`.
3. **4-Pad Tactile Switch Internal Jumpers:** Disabled implicit pass-through switch jumpers (`(duplicate_pad_numbers_are_jumpers no)`), marked the mechanical anchor pads `NC`, and routed explicit $0.25\text{ mm}$ copper buses across the matrix.

### Links & Files
- **PCBWay DFM Bench Photos & `pcbnew` Scripts Post:** https://www.stackcalc.io/blog/2026/10/20/pcbway-dfm-photos-and-jumper-fixes/
- **Hardware CAD Reference & Free Enclosure STLs:** https://www.stackcalc.io/hardware/
- **Full Project & Storefront:** https://www.stackcalc.io
```

---

### Post 5: Raspberry Pi Forums (`forums.raspberrypi.com`)
* **Where to Post:** `Raspberry Pi Pico / RP2350 -> Projects`
* **Canonical Website Post:** [Notes from the PCBWay Assembly Floor: Header Pins, JST Footprints, and Switch Jumper Routing](../blog/posts/2026-10-20-pcbway-dfm-photos-and-jumper-fixes.md) (`https://www.stackcalc.io/blog/2026/10/20/pcbway-dfm-photos-and-jumper-fixes/`)

**Title:**
`StackCalc 32: From Slapping a Pico 2 on the Back of the PCB (Batch 1) to Bare RP2350A Integration (Batch 2)`

**Body:**
```text
Hi everyone,

I wanted to share the hardware journey of StackCalc 32—an open-hardware pocket RPN scientific and educational calculator built around the RP2350, paired with 3D-printed Gridfinity math blocks and a companion iOS/watchOS app.

Our long-term goal is a durable, kid-friendly RPN calculator that students can toss in a backpack without their parents worrying about a $200+ calculator—starting at $89.99 for our first maker batch and driving the BOM down toward a $29.99 target.

### Batch 1 (First 5 Units): Slapping a Pico 2 onto the Back of the PCB
To get our first 5 physical calculators built and verified as fast as possible, we designed a 4-layer board where a Raspberry Pi Pico 2 (`MCU1`) solders directly onto the rear (`B.Cu`) behind the LCD area, scanning 43 tactile switches on the front (`F.Cu`) and driving a 2.5" 132×65 EastRising ST7567 transflective LCD over SPI.
- Funny DFM lesson from the factory floor: We initially listed `SC1632` (Pico 2 *with headers*) in our PCBWay BOM with through-hole pads. PCBWay sent us a photo showing the header pins poking straight through the front of the board right between the SMD pads of softkey `SOFT6`! Switching to the bare castellated Pico 2 (`SC1631`) and converting the footprint to pure bottom-side SMD pads solved it cleanly: https://www.stackcalc.io/blog/2026/10/20/pcbway-dfm-photos-and-jumper-fixes/

### Batch 2 (Next 20 Units — Hardware V2 Specification Ready): Full Bare-Silicon Integration
Now that Batch 1 proves out the 43-key matrix, TPU membrane feel, display driver, and our Embedded Swift firmware, our next 20-unit order moves to our **Hardware V2** layout—which keeps the exact same exterior enclosure and switch coordinates while eliminating the Pico 2 carrier board completely:
- **Direct QFN-60 RP2350A + Winbond W25Q32 4MB QSPI Flash + 12MHz Crystal** placed directly on `B.Cu` (dropping the MCU subsystem cost from $9.30 down to $1.22).
- **Direct CR2032 Spring Clip + Microne `ME2188` 3.3V Synchronous Boost (`Iq < 15µA`):** Replaces the wired JST battery harness and complex buck-boost power mux.
- **Strict Two-Zone Partitioning:** 100% of the ICs sit above a 6.13mm dead-band behind the LCD, leaving 100% bare ground copper behind all 43 tactile switches so key presses never flex solder joints.
- **RP2350 Erratum E9 Immunity:** Active-LOW open-drain matrix scanning (`gpio_pull_up()` on columns, High-Z inactive rows) in `hardware_wrapper.c`.

### Check Out the Launch:
- **Website, Manuals & Free Curriculum:** https://www.stackcalc.io
- **Etsy Store (Batch 001 Hardware & 3D-Printed Math Block Kits):** https://stackcalcmath.etsy.com
- **Companion Books on Amazon:** https://link.amazon/B0f5cP0Ur (SC-6) / https://link.amazon/B07DqTRR5 (SC-32)
- **Free Open-Source STLs (Enclosure + Gridfinity Math Lab):** https://www.stackcalc.io/downloads/
- **iOS, iPadOS & Standalone Apple Watch App (v1.1):** https://apps.apple.com/app/id6801788040
- **Hackaday Build Logs:** https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator
```

---

### Post 6: Teacher, Homeschool & STEM Co-Op Forums (`Well-Trained Mind Forum` / Math Educator Groups)
* **Where to Post:** `The Well-Trained Mind Community` (`K-8 Curriculum` / `High School` boards), Homeschool Co-op networks, and UIL Coach groups
* **Canonical Website Post:** [From OpenSCAD to the Classroom Desk: 84mm Fraction Towers, Logarithmic Prime Blocks, and Unit-Tested Books](../blog/posts/2026-10-26-manufacturing-math-blocks-and-reference-books.md) (`https://www.stackcalc.io/blog/2026/10/26/manufacturing-math-blocks-and-reference-books/`)

**Title:**
`Why the World Needs a Kid-Friendly Calculator That Grows With Them (Plus Our 3D-Printed Fraction & Prime Number Blocks)`

**Body:**
```text
Hello fellow parents and educators,

Whenever I tell people we built a new calculator, the first question is understandably: "Why does the world need another calculator?"

Here is the problem I ran into with my own kids:
In early elementary school, kids learn math with physical blocks on a desk. If they want to add 2 and 3, they put down 2 blocks, put down 3 blocks, and push them together. That natural order—quantities first, action second—is called Postfix (or Reverse Polish Notation, RPN).

Then around 4th grade, we take away the blocks and hand them an infix school calculator where they type nested parentheses `(12 + 8) / (5 - 1) =` into a black box that hides every intermediate step until they press `=`. With a stack-based RPN calculator, **students actually internalize operator-precedence parsing** because they have to break expressions down in the right order of operations to enter them onto the stack, seeing every intermediate result along the way. And unlike CAS (Computer Algebra System) calculators—which are banned on the SAT, ACT, IB, UIL, and college math exams—our calculator is purposefully designed to be **allowed in testing situations** (no CAS symbolic solver, no QWERTY keyboard, and no Wi-Fi/Bluetooth on the hardware).

We built **StackCalc** as a kid-friendly mathematical instrument that grows with a student from 1st grade (`StackCalc 6` — covering Common Core math through 6th grade) all the way to AP Calculus and engineering (`StackCalc 32`), paired with physical desk blocks and unit-tested workbooks. (Nobody wants to send a kid to school with a $250 collector's RPN calculator or a $200 vintage antique—so our initial small-batch hardware launches at $89.99 while we scale manufacturing toward a $29.99 student target, and our universal iPhone/iPad/Apple Watch app is available today with zero ads and zero subscriptions.)

### How the Physical Blocks and the Calculator Work Together

Every physical kit we manufacture is built around a 42mm Gridfinity storage box whose lid turns into an active math stage on the student's desk:

1. **Fraction Studio Proportional Towers (`1/1` through `1/12`):**
   - **What the blocks do:** Our Whole (`1/1`) tower is exactly 84mm tall—a composite length chosen so that halves (42mm), thirds (28mm), fourths (21mm), sixths (14mm), and twelfths (7mm) all divide into exact integer millimeters. When a child wants to add `1/2 + 1/3`, they drop the `1/2` and `1/3` towers into the left slot of the Twin Comparator Stage (reaching 70mm). In the right slot, they stack `1/6` blocks until the heights match flush at 5 sixths (`5/6`), physically discovering why a common denominator is needed!
   - **What the calculator does:** On StackCalc, the child enters `.1.2 [ENTER] .1.3 [+]` and sees `5/6`. Even better, in `StackCalc 6`, if they have an unreduced fraction like `12/18` (`.12.18`), pressing our `[SIMP]` key does *not* just jump to `2/3` like a black-box calculator—it factors out **one prime divisor at a time** (showing the common factor `2`, reducing to `6/9`, and letting the student press `[SIMP]` again to factor out `3` to reach `2/3`).

2. **Prime Factor Studio & Logarithmic Slide Rule Comparator:**
   - **What the blocks do:** Instead of memorizing factor trees on paper, students snap physical prime-number blocks (`2`, `3`, `5`, `7`) end-to-end inside a dual comparison rail. Because the block lengths are scaled logarithmically, placing a `2` block and a `3` block end-to-end physically equals the length of `6`! To find the **Greatest Common Divisor (GCD)** or **Least Common Multiple (LCM)** of 12 (`2 × 2 × 3`) and 18 (`2 × 3 × 3`), students line up both prime trains side by side and immediately see the shared prime backbone (`2 × 3 = 6`).
   - **What the calculator does:** In `StackCalc 6`, students verify their physical trains directly with dedicated one-touch `[PRIME]` (prime factorization), `[GCD]`, `[LCM]`, and `[÷R]` (integer division with remainder) keys, alongside live on-screen Ten-Frames, a 20-bead Rekenrek rack, a proportional Number Line, and a 5-level Adaptive Mental Math Quiz (`?`).

### Explore the Ecosystem (Free Downloads & Printed Kits)
- **Full Article on Our 84mm Fraction Towers, Prime Blocks & Books:** https://www.stackcalc.io/blog/2026/10/26/manufacturing-math-blocks-and-reference-books/
- **Free 43-Page Teacher Curriculum Guide & 120 Station Worksheets (PDF):** https://www.stackcalc.io/curriculum/
- **253-Problem SC-6 Elementary Workbook & 339-Problem SC-32 Casebook:** https://www.stackcalc.io/manuals/
- **Etsy Store (Pre-Printed Multi-Color Fraction & Prime Kits + Hardware):** https://www.etsy.com/shop/StackCalc
- **Have a 3D Printer? Download the Open-Source 3MF/STL Files Free:** https://www.stackcalc.io/downloads/
- **App Store (iPhone, iPad & Standalone Apple Watch — 100% Offline, No Ads/Subs):** https://apps.apple.com/app/id6801788040

I would love to hear what math concepts give your students the most trouble and how we can add more station worksheets to help!
```

---

### Post 7: Printables.com, Bambu MakerWorld & Lemmy (`!3dprinting@lemmy.world`)
* **Where to Post:** Upload to **Printables.com**, **Bambu MakerWorld**, and share on `!3dprinting@lemmy.world` / `!opensource@lemmy.world`
* **Canonical Website Post:** [From OpenSCAD to the Classroom Desk: 84mm Fraction Towers, Logarithmic Prime Blocks, and Unit-Tested Books](../blog/posts/2026-10-26-manufacturing-math-blocks-and-reference-books.md) (`https://www.stackcalc.io/blog/2026/10/26/manufacturing-math-blocks-and-reference-books/`)

**Title:**
`StackCalc Open-Source Tactile Math Lab (Fraction Towers, Logarithmic Prime Slide Rule, & Screwless RPN Calculator Enclosure)`

**Body:**
```markdown
### Why We Designed This
Sending a kid to school with a $250 collector's RPN calculator—or replacing an entire $60 classroom manipulative kit when one plastic block goes missing under a desk—makes no sense.

We designed the **StackCalc Tactile Math Lab** in parametric OpenSCAD so teachers, parents, and makers can print replacement blocks for pennies, dock every kit to the **42mm Gridfinity standard**, and pair hands-on blocks with our **StackCalc** RPN calculator (available today on iOS/watchOS, with our RP2350 open-hardware unit launching at $89.99 on the way to a $29.99 student target).

### Engineering Highlights in the STL / 3MF Bundle
1. **84mm Datum Fraction Studio Towers (`1/1` to `1/12`):** Engineered around an 84mm unit height so `1/2`, `1/3`, `1/4`, `1/6`, `1/7`, and `1/12` resolve to exact integer millimeter heights without slicer layer-rounding drift.
2. **Logarithmic Prime Factor Studio & Slide Rule:** Prime blocks (`2, 3, 5, 7`) scaled logarithmically so placing prime factors end-to-end physically multiplies their lengths (`log(a) + log(b) = log(a×b)`).
3. **4-Part Screwless Calculator Mechanical Prototype & Flat-Pack Puzzle Stand:** Uses 0.20mm sliding dovetail rails, a Shore 95A TPU membrane, a zero-preload serpentine snap latch (0.0 MPa static stress while latched so PLA never creeps), and a 6mm flat-packing desk stand.

### Links & Complete Ecosystem
- **Full Blog Post on How We Designed & Manufactured the Blocks:** https://www.stackcalc.io/blog/2026/10/26/manufacturing-math-blocks-and-reference-books/
- **Don't Want to Print All the Multi-Color Silk Kits Yourself?** Grab our workshop-calibrated 3D block kits and hardware on **Etsy:** https://stackcalcmath.etsy.com (plus official companion books on **Amazon:** https://link.amazon/B0f5cP0Ur)
- **Free 43-Page Curriculum Guide, 120 Worksheets & 590+ Problem Workbooks:** https://www.stackcalc.io/curriculum/
- **Universal iOS, iPadOS & Standalone Apple Watch App (v1.1):** https://apps.apple.com/app/id6801788040
- **Engineering Blog (including our PCBWay DFM Photos & FEA Sweeps):** https://www.stackcalc.io/blog/
```
