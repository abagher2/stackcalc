---
title: "Shipping StackCalc v1.1 on the App Store: Unifying Scientific Mode (SC-32) and Visual Learning Mode (SC-6)"
description: "How Version 1.1 of the universal iPhone, iPad, and standalone Apple Watch app unites a professional 4-level scientific RPN calculator with a K–8 visual math playground."
image: assets/press/sc6_product_page_header.png
date: 2026-10-23
authors:
  - abagher
categories:
  - Software
  - iOS
  - watchOS
  - Education
slug: shipping-stackcalc-v1-1-sc32-and-sc6
---

While our physical PCBs are being assembled and our 3D-printed classroom manipulatives run on the print beds, the software heart of the project—which shares the exact same `RPNCore` Swift engine as our bare-metal firmware—just reached a major milestone.

**StackCalc Calculator v1.1** is now live on the [Apple App Store](https://apps.apple.com/app/id6801788040) for **iPhone, iPad, and as a 100% standalone Apple Watch app**. Version 1.1 unifies two distinct instruments inside a single universal binary: **Scientific Mode (`StackCalc 32`)** for engineers and advanced STEM students, and the brand-new **Visual Learning Mode (`StackCalc 6`)** for K–8 foundational mathematics.

<!-- more -->

![StackCalc 6 Visual Learning Mode Hero Banner.](../../assets/press/sc6_product_page_header.png)

---

## 1. Why Put an Elementary Visual Mode Inside a Scientific RPN Calculator?

Traditional math education forces students through three disconnected mental models:
1. In early elementary school, children group physical counters, ten-frames, and fraction blocks (**Concrete**).
2. Around fourth grade, those tactile models are abruptly replaced by algebraic school calculators that hide state behind nested parentheses and an `=` key (**Opaque Syntax**).
3. Only in university engineering or computer science do students encounter stack-based postfix evaluation (**RPN**)—where operands stay visible and operations act immediately.

Yet as we explored in [The Postfix Manifesto](2026-10-12-the-postfix-manifesto.md), **a child pushing two groups of blocks together on a desk is already thinking in Reverse Polish Notation**: you place your first quantity, place your second quantity, and combine them.

By building **Visual Learning Mode (`StackCalc 6`)** directly into the same app as **Scientific Mode (`StackCalc 32`)**, a learner can start in first grade with visual Ten-Frames and graduate to complex numbers, linear regression, and numerical integration without ever unlearning how the operational stack works.

---

## 2. Inside Visual Learning Mode (`StackCalc 6`)

Opening `stackcalc://sc6` (or toggling modes in the app menu) reconfigures the interface into a focused **2-level operational stack** paired with a high-contrast dot-matrix canvas that renders numbers as live pictorial models aligned with **Singapore Math (Concrete • Pictorial • Abstract)**:

* **Ten-Frames (`10F`):** Dynamically groups quantities into $2 \times 5$ frames up to 100, letting students see "make-ten" bridging strategies as they add and subtract.
* **20-Bead Number Rack (`RACK`):** Simulates a classic two-row Rekenrek with 5-and-5 bead grouping for subitizing, doubles, and near-doubles fluency.
* **Dynamic Number Line (`LINE`):** Plots proportional jump arcs across a continuous number line to visualize addition trajectories, subtraction differences, and skip-counting multiples.
* **Synchronized Analog Clock (`🕒`):** Links the digital stack to a geared hour, minute, and second dial for elapsed time and base-60 arithmetic.
* **5-Level Adaptive Fluency Quiz Engine (`?`):** Generates targeted mental-math challenges (`L1`–`L5`) that adapt to response speed and accuracy, complete with live scoreboards and mastery banners.

---

## 3. Scientific Mode (`StackCalc 32`) & Standalone Apple Watch Refinements

![StackCalc 32 Scientific Mode Hero Banner.](../../assets/press/sc32_product_page_header.png)

Alongside `StackCalc 6`, Version 1.1 refines our flagship **Scientific Mode (`StackCalc 32`)** across iPhone, iPad, and watchOS:

* **Step-by-Step Mixed Fraction Reduction (`[SIMP]`):** Rather than silently reducing $\frac{12}{18}$ to $\frac{2}{3}$, pressing `[SIMP]` factors out one prime divisor at a time and displays the common factor on screen so students see *why* the fraction simplifies.
* **Interactive Curve Plotting & Numerical Calculus:** Real-time root inspection, inflection tracing, and shaded Simpson integration directly on the monochrome LCD canvas.
* **Continuous Tactile Field (`CoreHaptics`):** Simulates both subtle key-seam boundary pulses as your thumb glides across glass and crisp mechanical switch actuation with distinct physical weight for digits, shift keys, and `ENTER`.
* **100% Standalone Apple Watch Instrument:** Runs natively on your wrist without a paired iPhone, using the top 75% of the OLED display as a no-look `ENTER` target and the Digital Crown to scrub all four stack registers (`X, Y, Z, T`).

Best of all, StackCalc v1.1 remains **100% offline, with zero ads, zero tracking, and zero subscriptions**—ready for the classroom, lab, or workshop today while our physical hardware completes fabrication.
