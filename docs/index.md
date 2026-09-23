---
title: "StackCalc | RPN Across Devices and Physical Learning"
description: "A shared RPN calculator core across Apple apps, firmware emulation, teaching resources, and a physical calculator in development."
---

# StackCalc

<div style="text-align: center;">
<picture>
  <source srcset="assets/launch-stack-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="assets/launch-stack-light.svg" alt="StackCalc logo" style="width: 200px; margin-bottom: 1rem; border-radius: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);" />
</picture>
<p style="font-size: 1.2rem; color: gray;">RPN software, teaching resources, and an instrument in development.</p>
</div>

## What exists today

StackCalc is an ecosystem around one calculator model rather than a single retro-calculator replica. The same RPN ideas are explored on devices a learner already has, with physical resources that make stack behavior and mathematical relationships visible.

- **Apple apps:** The iPhone, iPad, and Apple Watch companion app is available on the [App Store](https://apps.apple.com/app/id6801788040).
- **Learning Lab:** The first collection includes a fraction studio, four-register stack stage, expression-tree board, coordinate lab, printable cards, and an eight-page teacher booklet. [Download the 0.2.0 STL pack and teacher PDFs](learning-lab.md#download-the-prototype-materials).
- **Firmware emulator:** A local browser simulator runs the compiled firmware image through an RP2350 emulator. Its generated keypad feeds a row-and-column matrix contract, and its display reads the firmware’s 132 × 65 framebuffer.
- **Physical calculator:** The tool-free chassis, faceplate, TPU membrane, and snap cap are real printed mechanical prototypes. The KiCad PCB design and manufacturing BOM are complete and fabrication is in progress; no populated, powered StackCalc board is being represented here.

## Why RPN

RPN turns a calculation into a sequence of small actions: place values on a stack, then apply an operation. It can reduce parenthesis entry, but it makes calculator state important. A person needs to see the working value, know what ENTER changes, and predict what an operation will consume.

Our design question is how a learner can see, touch, and predict the next stack action across an app, a teaching aid, a simulator, and eventually a dedicated handheld.

## Follow the current work

- Start with the [StackCalc Learning Lab](learning-lab.md) and its reproducible materials.
- Read the [engineering blog](blog/index.md) for the shared core, emulator, PCB-to-CAD relationship, printed assembly, and teaching-resource methods.
- Review the [hardware documentation](hardware.md) for the current source-to-output map and physical-validation boundary.
- Follow the staged [Hackaday project](https://hackaday.io/project/206743-stackcalc32-a-tactile-rpn-calculator) for build-log discussions. The StackCalc site remains the canonical home for source materials and downloads.
