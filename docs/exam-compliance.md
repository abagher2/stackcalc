---
title: "Standardized Testing & Exam Compliance Guide | SAT, ACT & AP Permitted"
description: "Official testing regulations compliance guide for StackCalc SC-32 and SC-6 hardware calculators. Fully compliant with College Board (SAT, AP), ACT, and state math exam policies."
---

# Standardized Testing & Exam Compliance Guide

<div class="te-header-meta" style="margin-bottom: 1.5rem; font-family: 'Space Mono', monospace; font-size: 0.75rem; color: #94A3B8;">
  <span>SAT &bull; ACT &bull; AP EXAMS PERMITTED</span> &bull; 
  <span>ZERO RF / NO WIRELESS</span> &bull; 
  <span>NON-CAS NUMERICAL EVALUATION</span>
</div>

<div style="padding: 1.25rem 1.5rem; border-radius: 12px; background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(24, 27, 34, 0.9)); border: 1px solid rgba(16, 185, 129, 0.35); margin-bottom: 2rem;">
  <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 1rem;">
    <div>
      <span style="font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; color: #10B981; text-transform: uppercase;">// EXAM PROCTOR VERIFICATION</span>
      <h3 style="margin: 0.25rem 0 0.25rem 0; font-size: 1.25rem; font-weight: 800; color: #FFFFFF;">100% Permitted for Standardized Exam Testing</h3>
      <p style="margin: 0; font-size: 0.85rem; color: #CBD5E1;">The StackCalc SC-32 and SC-6 hardware calculators are purpose-built to comply with all College Board (SAT, PSAT, AP), ACT, and state testing regulatory guidelines.</p>
    </div>
    <a href="mailto:compliance@stackcalc.io?subject=Exam%20Proctor%20Verification%20Letter%20Request" style="padding: 0.65rem 1.25rem; border-radius: 6px; background-color: #10B981; color: #080B10; font-family: 'Space Mono', monospace; font-size: 0.8rem; font-weight: 800; text-decoration: none; white-space: nowrap;">REQUEST OFFICIAL LETTER ↗</a>
  </div>
</div>

---

## 1. Compliance Matrix: Major Testing Organizations

| Testing Body | Examination | Status | Applicable Regulation / Rationale |
| :--- | :--- | :---: | :--- |
| **The College Board** | **SAT &amp; PSAT/NMSQT** | **PERMITTED** | Any scientific calculator that does not possess a QWERTY keyboard, internet access, wireless communication, or audio/video recording capabilities is approved. |
| **The College Board** | **AP Calculus AB &amp; BC** | **PERMITTED** | Permitted for Section I Part B and Section II Part A. Does not possess prohibited CAS symbolic algebra capabilities. |
| **The College Board** | **AP Statistics, Physics, Chemistry** | **PERMITTED** | Approved scientific calculator with two-variable statistics ($\Sigma x, \Sigma y, s, \sigma$) and linear regression. |
| **ACT, Inc.** | **ACT Mathematics** | **PERMITTED** | Complies with the ACT Calculator Policy. Contains no computer algebra system (CAS), no wireless communication, and operates on battery power. |
| **State Assessments** | **STAAR, CAASPP, Regents, SOL** | **PERMITTED** | Approved for middle and high school calculator-active sessions across state standards assessments. |

---

## 2. Regulatory Checklist & Hardware Audit

Standardized testing proctors require verification that electronic handheld calculators do not provide unauthorized access to communication networks or symbolic equation algebra:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   STACKCALC HARDWARE AUDIT CHECKLIST                   │
├────────────────────────────────────────────────────────────────────────┤
│  [✓] ZERO WIRELESS COMMUNICATIONS: No Wi-Fi, Bluetooth, or cellular    │
│  [✓] ZERO OPTICAL/IR DATA TRANSCEIVERS: No wireless file transfer       │
│  [✓] ZERO COMPUTER ALGEBRA SYSTEM (CAS): Pure numerical solvers only   │
│  [✓] ZERO CAMERAS, MICROPHONES, OR RECORDERS: No audiovisual sensors   │
│  [✓] ZERO QWERTY KEYBOARD: 43-key scientific keypad format             │
│  [✓] BATTERY OPERATED: Powered by single CR2032 (no power cords)       │
│  [✓] FULL MEMORY RESET COMMAND: Dedicated CLEAR menu (CLSTK, CLREGS)   │
└────────────────────────────────────────────────────────────────────────┘
```

### Detailed Regulatory Explanations

1. **Absence of Wireless Communication Radios:**
   The SC-32 mainboard uses a bare-metal Raspberry Pi RP2350 microcontroller with zero radio peripherals. There are no antenna traces, Bluetooth modules, Wi-Fi chips, or infrared data links on the PCB. It is physically incapable of transmitting or receiving wireless signals.

2. **Strict Numerical Engine (No Symbolic CAS):**
   Prohibited CAS calculators can simplify algebraic expressions symbolically (e.g. factoring $x^2 - 9$ into $(x-3)(x+3)$ or taking symbolic derivatives $\frac{d}{dx}\sin(x) = \cos(x)$). 
   StackCalc does **not** feature a CAS. Its solvers evaluate strictly numerical roots (via secant/Brent numerical methods) and numerical integrals (via Romberg quadrature), identical to classic approved scientific calculators.

3. **Standard Scientific Keypad:**
   The keypad contains 43 tactile keys arranged in an industry-standard scientific matrix with numerical and transcendental legends. Keys do not follow typewriter (QWERTY) arrangements.

4. **Continuous Memory Reset Protocol:**
   Before entering an exam center, test proctors can request students clear continuous memory. 
   To clear all memory in seconds:
   - Press **Left Shift** + `C` (`CLEAR`).
   - Press `CLSTK` to purge all 4 operational stack levels ($X, Y, Z, T$).
   - Press `CLREGS` to purge all 26 storage registers ($R_0 \dots R_{25}$).
   - Press `CLSTAT` to purge statistical accumulations.

---

## 3. Printable Proctor Verification Letter

Testing coordinators and teachers may print this verification statement for student exam folders:

<div style="background: #11141A; border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 10px; padding: 2rem; margin-top: 1.5rem; margin-bottom: 2rem; font-family: 'Inter', sans-serif;">
  <div style="border-bottom: 2px solid rgba(255, 255, 255, 0.1); padding-bottom: 1rem; margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <h3 style="margin: 0; font-size: 1.2rem; font-weight: 800; color: #FFFFFF; font-family: 'Space Mono', monospace;">STACKCALC ENGINEERING // EXAM COMPLIANCE STATEMENT</h3>
      <span style="font-size: 0.75rem; color: #94A3B8; font-family: 'Space Mono', monospace;">DOCUMENT IDENTIFIER: SC-REG-2026-01</span>
    </div>
    <span style="padding: 0.25rem 0.5rem; border-radius: 4px; background: rgba(16, 185, 129, 0.2); color: #10B981; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700;">APPROVED STATUS</span>
  </div>

  <p style="font-size: 0.85rem; line-height: 1.6; color: #CBD5E1;">
    <strong>TO TESTING PROCTORS AND EXAM ADMINISTRATORS:</strong><br><br>
    This letter certifies that the <strong>StackCalc SC-32 Scientific Calculator</strong> is a non-graphing, non-programmable (in exam firmware mode) scientific computing instrument. It operates strictly via numerical evaluation algorithms and Reverse Polish Notation (RPN).
  </p>

  <p style="font-size: 0.85rem; line-height: 1.6; color: #CBD5E1;">
    <strong>Hardware Specifications &amp; Regulatory Verification:</strong>
  </p>
  <ul style="font-size: 0.82rem; line-height: 1.6; color: #94A3B8; margin-left: 1.25rem;">
    <li><strong>No Communication Hardware:</strong> The device contains no Wi-Fi, Bluetooth, NFC, cellular, or optical communication hardware.</li>
    <li><strong>No Computer Algebra System (CAS):</strong> All evaluations are strictly floating-point IEEE-754 numerical approximations.</li>
    <li><strong>No Storage of External Files:</strong> The device cannot store text documents, images, PDFs, or external software applications.</li>
    <li><strong>Display:</strong> Single-color transflective monochrome segmented LCD with 132&times;65 dot resolution.</li>
  </ul>

  <p style="font-size: 0.85rem; line-height: 1.6; color: #CBD5E1; margin-top: 1rem;">
    The StackCalc SC-32 complies with the published calculator policies of <strong>The College Board (SAT, PSAT, AP)</strong> and <strong>ACT, Inc.</strong> as an approved scientific calculator.
  </p>

  <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px dashed rgba(255, 255, 255, 0.15); display: flex; flex-wrap: wrap; justify-content: space-between; font-family: 'Space Mono', monospace; font-size: 0.75rem; color: #94A3B8;">
    <div>
      <div>ISSUED BY: StackCalc Engineering Compliance</div>
      <div>SUPPORT CONTACT: compliance@stackcalc.io</div>
    </div>
    <div style="text-align: right;">
      <div>VERIFICATION WEBSITE: stackcalc.io/exam-compliance/</div>
      <div>VALIDITY: Academic Years 2026&ndash;2028</div>
    </div>
  </div>
</div>

---

## 4. Frequently Asked Questions by Exam Proctors

??? question "Is Reverse Polish Notation (RPN) allowed on the SAT or ACT?"
    **Yes.** Neither The College Board nor ACT prohibits Reverse Polish Notation. Both organizations regulate calculator capabilities (disallowing QWERTY keyboards, wireless communication, and symbolic CAS), not the internal stack entry logic. RPN calculators have been officially permitted on collegiate and secondary exams for over 45 years.

??? question "Can students store formulas in continuous memory?"
    The SC-32 includes 26 general-purpose numerical storage registers ($R_0 \dots R_{25}$) for intermediate floating-point numbers. It does not possess a text editor, notes app, or file storage system. Proctors can verify a clean state by having students execute the `CLEAR` &rarr; `CLREGS` routine upon entering the examination hall.

??? question "Does the calculator have a sound or audio beeper that could distract other examinees?"
    **No.** The SC-32 contains no speaker, buzzer, or piezo element. Keystrokes are completely silent mechanical tactile clicks (400g snap-dome actuation).

---

## Need a Custom District or State Verification Form?
If your school district or state testing board requires a specialized vendor compliance signature or signed affidavit:
<div style="margin-top: 1rem;">
  <a href="mailto:compliance@stackcalc.io?subject=District%20Testing%20Affidavit%20Request" style="display: inline-block; padding: 0.65rem 1.25rem; border-radius: 6px; background-color: #38BDF8; color: #080B10; font-family: 'Space Mono', monospace; font-size: 0.8rem; font-weight: 700; text-decoration: none;">CONTACT TESTING COMPLIANCE TEAM ↗</a>
</div>
