# Apple Ecosystem & Desktop App: Mac, iPad, iPhone & Watch

StackCalc is engineered from day one as a unified physical-digital system. Our companion applications for **macOS, iPadOS, iOS, and watchOS** share the exact same deterministic Swift package—`RPNCore`—as our bare-metal Raspberry Pi RP2350 microcontroller firmware. 

The apps share calculator semantics through RPNCore; platform capabilities and completed native regression evidence determine supported behavior.

---

## 1. Apple Watch: Pitch-Black Rapid Field

The watchOS application is designed for instant, glanceable number crunching directly on your wrist:

- **True OLED #000000 Background**: Preserves battery life and blends invisibly with Apple Watch Series 10/11 edges.
- **Edge-Glow Wayfinding Beacons**: Directional boundary pulses (Burnt Orange on the left, Blue on the right, Cyan on top) guide your finger across the keypad without looking.
- **Macro Screen-Tap ENTER**: Tap anywhere on the upper display to execute an instant stack-lift `ENTER` without targeting a tiny button.
- **Continuous Tactile Feedback**: Powered by Apple's Taptic Engine to simulate physical snap-dome switches.

---

## 2. iPhone & iPad: The 10-Column Landscape Layout

On iPad and iPhone, StackCalc expands into a spacious landscape and portrait instrument inspired by classic 1980s landscape scientific computing layouts:

- **12-Character Segmented LCD**: Emulates the authentic EastRising ST7567 transflective display with bundled **Terminus** typography.
- **Continuous Tactile Field (HPTC)**: Zero-distance drag gestures let you slide across key seams with subtle boundary clicks, sinking into button centers for heavy mechanical actuations.
- **Expandable TUI Overlays**: Complex operations like Plotting, Integration, Equation Editing, and Tutorials smoothly expand into an authentic Text User Interface terminal.

---

## 3. macOS Desktop App: Physical Keyboard Ergonomics & Multi-Register Studio

On Mac, StackCalc becomes an indispensable engineering workstation instrument for macOS:

- **Native macOS Binary**: Universal build optimized for Apple Silicon (M1/M2/M3/M4) and Intel Macs, launching with zero startup latency.
- **Physical Keyboard & Numpad Mapping**: Full physical keyboard ergonomics. The numeric keypad `Enter` executes RPN stack commit, standard arithmetic keys (`+`, `-`, `*`, `/`) trigger operations, `Space` or `Return` lifts the stack, and arrow keys cycle through registers.
- **Side-by-Side Multi-Register Inspector**: On desktop monitors, expand the auxiliary side panel to inspect all operational stack levels ($X, Y, Z, T$), global storage registers ($R_0 \dots R_{25}$), and statistical accumulation registers ($\Sigma$) simultaneously.
- **Menu Bar Quick Calculator**: Global keyboard shortcut summons a lightweight RPN scratchpad directly from the macOS menu bar for rapid calculations while writing code or LaTeX documents.

---

## Download on the App Store

StackCalc is available as a **Universal Purchase** on the Apple App Store for Mac, iPad, iPhone, and Apple Watch:

<div class="my-6">
  <a href="https://apps.apple.com/app/id6801788040" target="_blank" rel="noopener noreferrer" class="brutalist-button-primary px-8 py-3.5 font-mono text-sm font-bold inline-flex items-center gap-2.5 text-decoration-none">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: -3px; display: inline-block;"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.88c.61-.74 1.04-1.78.92-2.82-.93.04-2.02.63-2.65 1.37-.56.64-.99 1.69-.86 2.71 1.05.08 2.01-.54 2.59-1.26z"/></svg>
    DOWNLOAD STACKCALC: MAC, IPAD &amp; WATCH RPN
  </a>
</div>

## 4. Visual Design & Color Scheme System

StackCalc implements an authentic **1:1 Digital Twin** architecture across native Apple surfaces, matching real-world 3D-printed thermoplastics and 1064nm pulsed infrared laser markings:

### Physical Hardware Twins (7 Production Editions)
All physical digital twins feature **Tactile Light Gray TPU 95A (`#94999E`)** keycaps with recessed laser-ablated legends and high-contrast direct laser micro-foaming:

1. **Stealth Industrial:** Technical Matte Black PLA (`#101114`) with stark white foamed nomenclature and gold/cyan shifts.
2. **Cosmos (Champion):** Monolithic Sunlu Midnight Navy PLA 2.0+ (`#28334A`) with **15.2:1 AAA** stark white micro-foaming.
3. **Voyager:** Deep Midnight Navy chassis (`#28334A`) paired with an Elegoo Space Gray faceplate (`#4B4E54`) and celestial gold/cyan shifts.
4. **Avionics Slate Gray:** Anodized cockpit aesthetic in Elegoo Space Gray (`#4B4E54`) with aviation amber and flight cyan indicators.
5. **Heritage Pioneer:** Sunlu Dark Chestnut PLA (`#3B1F17`) with antique cream foamed legends (`#F5F0E6`) and classic heritage amber/blue accents.
6. **Earth-Tone (Espresso):** Organic Sunlu Coffee Brown PLA (`#4A2E1B`) with warm chalk-white markings (`#F8F6F0`) and ochre/teal indicators.
7. **Synthwave (Signature):** Black PLA chassis (`#101114`) with Purple+Black Dual Silk faceplate (`#695CC7`), Archimedean chords surface sheen, and silver-frost foamed legends (`#E8EAF0`).

### In-App Heritage Editions (3 Virtual Themes)
Dedicated virtual themes celebrating landmark historical designs:
1. **RetroFuturism:** Dieter Rams / 1980s Braun aesthetic in warm aerospace cream (`#F5F5F3`) with deep navy markings (`#142240`) and antique bronze accents (`#784408`).
2. **Pioneer Brown:** Faithful software recreation of the iconic 1988 Corvallis release in matte brown (`#2E241C`) with golden amber and cyan legends.
3. **Pioneer Black:** Software recreation of the 1990s updated industrial design in matte black (`#1F1F21`) with emerald green and orchid purple legends.

### Display Palette & Surface Physics
- **132:65 Reflective LCD:** Reflective polarization matrix background (`#E2E6EE`) with dense carbon-black liquid crystal segments (`#181A1B`) delivering a 14.1:1 AAA contrast ratio.
- **Surface Textures:** Procedural simulation of 10% monotonic ironed PLA/PETG and Archimedean chords concentric diffraction patterns on silk faceplates.
- **Dynamic Appearance:** Automatically defaults to **RetroFuturism** in iOS Light Mode and **Stealth Industrial** in iOS Dark Mode, with instant sequential theme cycling via the quick-switch menu pill.
- **Apple Watch Independence:** The watchOS app permanently uses its specialized pitch-black OLED `#000000` canvas with peripheral wayfinding beacons (Burnt Orange, Electric Blue, Cyan) for rapid wrist scanning, independent of iOS theme selection.

---

## 5. Widget Architecture & Tutorial Integration

Watch uses one fixed black/orange/cyan functional scheme. iPhone, iPad and their widgets use the chosen material palette with direction and shape to identify shifts. System widget tint may override app colors. Ordinary widget arithmetic remains available beyond five taps; native pending feedback and an Open calculator route support handoff. Visible latency depends on the host and must be measured; no zero-latency guarantee is made.

Tutorials retain the phone calculator geometry. Watch guidance uses full-screen pages followed by its normal keypad. SC6 retains the tested vertical X/T display and correction behavior; a horizontal operand layout is not the current implementation.
