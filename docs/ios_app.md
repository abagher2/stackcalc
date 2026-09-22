# iOS & watchOS Apps: The 1:1 Digital Twin

StackCalc is engineered from day one as a dual physical-digital system. Our companion applications for Apple Watch, iPad, and iPhone share the exact same deterministic Swift package—`RPNCore`—as our bare-metal Raspberry Pi RP2350 microcontroller firmware. 

The apps share calculator semantics through RPNCore; platform capabilities and completed native regression evidence determine supported behavior.

---

## 1. Apple Watch: Pitch-Black Rapid Field

The watchOS application is designed for instant, glanceable number crunching directly on your wrist:

- **True OLED #000000 Background**: Preserves battery life and blends invisibly with Apple Watch Series 10/11 edges.
- **Edge-Glow Wayfinding Beacons**: Directional boundary pulses (Burnt Orange on the left, Blue on the right, Cyan on top) guide your finger across the keypad without looking.
- **Macro Screen-Tap ENTER**: Tap anywhere on the upper display to execute an instant stack-lift `ENTER` without targeting a tiny button.
- **Continuous Tactile Feedback**: Powered by Apple's Taptic Engine to simulate physical snap-dome switches.

---

## 2. iPhone & iPad: The 10-Column Voyager Layout

On iPad and iPhone, StackCalc expands into a spacious landscape and portrait instrument inspired by the classic HP-15C Voyager layout:

- **12-Character Segmented LCD**: Emulates the authentic EastRising ST7567 transflective display with bundled **Terminus** typography.
- **Continuous Tactile Field (HPTC)**: Zero-distance drag gestures let you slide across key seams with subtle boundary clicks, sinking into button centers for heavy mechanical actuations.
- **Expandable TUI Overlays**: Complex operations like Plotting, Integration, Equation Editing, and Tutorials smoothly expand into an authentic Text User Interface terminal.

---

## Download on the App Store

StackCalc is available on the Apple App Store for Apple Watch, iPad, and iPhone:

<div class="my-6">
  <a href="https://apps.apple.com/app/id6801788040" target="_blank" class="brutalist-button-primary px-8 py-3.5 font-mono text-sm font-bold inline-flex items-center gap-2.5 text-decoration-none">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: -3px; display: inline-block;"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.88c.61-.74 1.04-1.78.92-2.82-.93.04-2.02.63-2.65 1.37-.56.64-.99 1.69-.86 2.71 1.05.08 2.01-.54 2.59-1.26z"/></svg>
    DOWNLOAD STACKCALC: WATCH &amp; IPAD RPN
  </a>
</div>

## Surface colors and widget behavior

Watch uses one fixed black/orange/cyan functional scheme. iPhone, iPad and their widgets use the chosen material palette with direction and shape to identify shifts. System widget tint may override app colors. Ordinary widget arithmetic remains available beyond five taps; native pending feedback and an Open calculator route support handoff. Visible latency depends on the host and must be measured; no zero-latency guarantee is made.

Tutorials retain the phone calculator geometry. Watch guidance uses full-screen pages followed by its normal keypad. SC6 retains the tested vertical X/T display and correction behavior; a horizontal operand layout is not the current implementation.
