---
template: home.html
title: "StackCalc | The Uncompromising Digital Twin"
description: "The affordable, dedicated physical RPN scientific calculator. Starting at $59, designed for students learning math and professionals solving real-world problems. With a 1:1 iOS and watchOS digital twin."
---

# The Calculator for a New Generation

<div style="text-align: center;">
<picture>
  <source srcset="assets/launch-stack-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="assets/launch-stack-light.svg" alt="StackCalc32 Logo" style="width: 200px; margin-bottom: 1rem; border-radius: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);" />
</picture>
<h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">StackCalc32</h1>
<p style="font-size: 1.2rem; color: gray;">Fast. Usable. Affordable. RPN.</p>
</div>

## The Philosophy

When I was in high school, I was the captain of the calculator team. My weapon of choice? The **HP32SII**. It was fast, tactile, and nearly perfect for everyday use. I was devastated when I had to return it upon graduating. For years, I scraped by with `dc`, MATLAB, and R, always missing the immediacy of the HP32SII. HP had long stopped making them, and I had no interest in carrying around a fragile antique.

Eventually, I discovered SwissMicros and bought their incredible modern recreations: the DM42, DM41 CC, DM15CC, and the DM32. When my daughter started middle school and was finally allowed to use a calculator in class, my first instinct was to hand her the DM41 CC. After all, she'd been trained in RPN since the first grade! But giving a child a $250+ titanium masterpiece to toss into a messy backpack just wasn't practical.

I searched the market for lower-end RPN calculators. There were none. Actually, there are several incredible projects in the community, such as OpenRPN, the PX-15C, various low-cost DIY hacks, and the ultra-premium SwissMicros calculators. However, these are generally targeted at hobbyists and wealthy professionals, rather than everyday students. We are targeting the entry-level scientific calculator market—where Texas Instruments and Casio rule—to give students a faster, better alternative to the status quo.

**So I built my own.**

StackCalc32 is not a hobbyist project or a piece designed to sit behind glass for calculator enthusiasts to marvel at. It is designed to be a **fast, everyday-use calculator** that you reach for when you need to crunch numbers.  Our mission is simple: we want to end the tyranny of in-fix calculators, unbind future generations from the shackles of parentheses, and eliminate the forced equals sign once and for all.

- **Native Apple Watch Support:** Because that's what kids have these days. It’s the perfect Trojan Horse to introduce them to RPN before graduating to the hardware or iPad app.
- **Tutorials:** For the 99.9% of people who have not yet seen the light of the RPN system, we added interactive tutorials for common operations. 
- **Reduced Feature**: We have removed many features from the HP32SII and not added features popular with other calculators for good reasons:
  - **No Programming:** Removed so it is fully compliant for ACT and SAT testing centers (and to keep things mathematically pure).
  - **Plotting (App Only):** Included in the iOS app, but  excluded from the hardware firmware for test compliance.
  - **No QWERTY or Wifi:** Full keyboards and wifi calculators are banned from testing centers. 
  - **No CAS or Algebraic Mode:** Equations are entered as RPN and the solvers are numeric. We support single-root solvers and 3rd-degree polynomial solvers.
  - **No Matrix or Vectors:** There many great computer programs for matrix calculations and entering them in a calculator is extremely cumbersome. 

Geek out over the details with us. Welcome to StackCalc32.
