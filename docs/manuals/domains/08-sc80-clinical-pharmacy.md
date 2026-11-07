---
title: "Unit VIII: Clinical Dosing, Renal Clearance & Pharmacokinetics"
description: "First-principles mathematics of human body surface area, lean and adjusted mass partitioning, glomerular filtration kinetics, vasoactive intravenous titrations, compartment elimination, and electrolyte homeostasis across Chapters 22–24."
---

# Unit VIII: Clinical Dosing, Renal Clearance & Pharmacokinetics

In 1916, Delafield Du Bois and Eugene F. Du Bois encased hospitalized patients at the Russell Sage Institute of Pathology in New York in tight-fitting paper-and-paraffin molds to measure human skin area directly. They demonstrated that basal metabolic rate, extracellular fluid volume, cardiac output, and renal blood flow scale with two-dimensional surface area rather than raw body mass. Seven decades later, in a 1987 letter to the *New England Journal of Medicine*, biostatistician Robert D. Mosteller replaced their multi-exponent nomogram with a square-root geometric mean of stature and weight. In outpatient primary care, oral medications are routinely prescribed in fixed adult unit doses because common pharmaceuticals possess a wide therapeutic index—a generous physiological margin between the minimum effective concentration required to treat disease and the toxic threshold at which organ damage begins.

In hospital oncology wards, intensive care units, emergency resuscitation bays, and neonatal nurseries, that margin vanishes. Cytotoxic antineoplastic agents, aminoglycoside and glycopeptide antibiotics, antiarrhythmics, and vasoactive catecholamines operate within a narrow therapeutic window. Under-dosing by $15\%$ allows a systemic infection or malignancy to progress, while over-dosing by $15\%$ can induce irreversible nephrotoxicity, ototoxicity, or ventricular arrhythmias. Because two patients who both weigh $88\text{ kg}$ on a bed scale can differ substantially in skeletal stature and adipose tissue fraction, clinical pharmacology partitions total weight into Ideal Body Weight (formulated by Ben Devine in 1974), Adjusted Body Weight, Body Mass Index, and Body Surface Area, alongside Malcolm Holliday and William Segar's 1957 three-tier pediatric fluid maintenance law.

Administering an accurate initial loading dose solves only the first half of the clinical dosing problem. Recurring maintenance doses must match the speed at which the kidneys and liver clear the compound from blood plasma. In 1953, German pediatrician and pharmacologist Friedrich Hartmut Dost published *Der Blutspiegel* (*The Blood Level*), coining the term *pharmacokinetics* and modeling the human body as a mathematical compartment governed by exponential first-order elimination. Notice the cross-domain mathematical identity linking clinical pharmacology to electrical engineering (Unit III, `SC-16`) and chemical kinetics (Unit VI, `SC-60`): a drug distributing across an apparent volume of distribution $V_d$ and cleared by the kidneys at volumetric flow rate $\text{CL}$ decays as $C(t) = C_0 e^{-(\text{CL}/V_d)t}$ with biological time constant $\tau_{\text{bio}} = V_d / \text{CL}$ and half-life $t_{1/2} = \ln(2)\,V_d / \text{CL}$. That is the exact differential equation governing a capacitor $C_{\text{cap}}$ discharging through a conductance $G = 1/R$ with time constant $\tau = R C_{\text{cap}}$. Two decades after Dost, in 1976, Donald Cockcroft and Henry Gault analyzed $24\text{-hour}$ urine creatinine excretions from $249$ patients aged $18$ to $92$ at Queen Mary Veterans Hospital in Montreal. They proved that steady-state serum creatinine must be scaled by chronological age, dosing weight, and biological sex to estimate glomerular filtration as Creatinine Clearance.

The **SC-80 Clinical, Nursing, Pharmacy & Critical Care** calculator anchors every clinical equation to a persistent Patient Profile ({{keycap:PAT}}) so clinicians can verify anthropometric compartments, infusion rates, and pharmacokinetic decay without manual transcription errors. Each chapter in this Unit follows a single hospital case through three connected clinical themes:

| Chapter | Narrative Problem | Mathematical Concepts | Three Chapter Themes |
| :--- | :--- | :--- | :--- |
| **Chapter 22** | Admitting a $68$-year-old, $175\text{ cm}$, $88\text{ kg}$ patient with serum creatinine $1.6\text{ mg/dL}$ and adjusting renal antibiotic dosing and 4-2-1 maintenance fluids | Persistent Patient Profile, Mosteller Body Surface Area, Devine Ideal and $40\%$ Adjusted Body Weight, Cockcroft–Gault clearance, and Holliday–Segar fluid scaling | 1. Body Surface Area & Lean Mass Partitioning<br>2. Cockcroft–Gault Glomerular Filtration Kinetics<br>3. Pediatric 4-2-1 Fluid & Caloric Maintenance |
| **Chapter 23** | Auditing a $5\ \mu\text{g/kg/min}$ vasopressor order for an $80\text{ kg}$ ICU patient ($400\text{ mg}$ in $250\text{ mL}$), back-solving an inherited pump rate, and calibrating a $15\text{ gtt/mL}$ transport drip | Weight-based microgram-to-milligram mass flux, inverse pump-to-dose verification, gravity tubing drop factors, Mean Arterial Pressure, and Parkland burn resuscitation | 1. Weight-Based Vasoactive Drip Titrations<br>2. Inverse Infusion Pump Audits at Shift Change<br>3. Gravity Drip Calibration, MAP & Burn Resuscitation |
| **Chapter 24** | Modeling a $500\text{ mg}$ IV antibiotic ($V_d = 25\text{ L}$, $t_{1/2} = 6.0\text{ hr}$), solving hold time for a toxic trough, and auditing an ICU blood gas, QTc, and helicopter $\text{O}_2$ tank | One- and two-compartment exponential decay, steady-state accumulation, Alveolar–arterial $\text{O}_2$ gradient, anion gap, corrected $\text{Na}^+$ and $\text{Ca}^{2+}$, Bazett $\text{QT}_c$, and $\text{O}_2$ tank duration | 1. First-Order Elimination & 5-Half-Life Steady State<br>2. Arterial Blood Gases, Anion Gap & Corrected Electrolytes<br>3. Bazett $\text{QT}_c$ Normalization & Transport Oxygen |

---

# Chapter 22: Adjusting the Vancomycin Regimen for Declining Renal Function

During morning infectious-disease rounds on the medical-surgical ward, a $68$-year-old male patient standing $H = 175.0\text{ cm}$ ($5\text{ ft } 8.9\text{ in}$) tall and weighing $W = 88.0\text{ kg}$ is admitted with methicillin-resistant *Staphylococcus aureus* (MRSA) bacteremia. His morning basic metabolic panel shows that his steady-state serum creatinine has climbed from a baseline of $1.0\text{ mg/dL}$ to $S = 1.60\text{ mg/dL}$. Because intravenous vancomycin and aminoglycosides are eliminated almost entirely by glomerular filtration in the kidneys—and accumulate to nephrotoxic and ototoxic plasma concentrations when filtration slows—the clinical pharmacist must store the patient's biometrics in the **Patient Profile** and audit his anthropometric compartments and renal clearance before signing off on the maintenance dosing interval.

Evaluating the patient's chart requires resolving a fundamental tension in clinical anthropometrics. At $175.0\text{ cm}$ and $88.0\text{ kg}$ ($\text{BMI} = 28.73\text{ kg/m}^2$), the patient carries significant excess adipose mass above his lean skeletal frame. If the pharmacist plugs his raw $88.0\text{ kg}$ bed-scale weight into the Cockcroft–Gault clearance numerator, the equation treats every kilogram of poorly perfused fat tissue as creatinine-producing skeletal muscle, overestimating his kidney function at $55.0\text{ mL/min}$. Conversely, partitioning his mass into Devine Ideal Body Weight ($70.46\text{ kg}$) and $40\%$ Adjusted Body Weight ($77.48\text{ kg}$) reveals that his true glomerular filtration has fallen below the $50.0\text{ mL/min}$ clinical threshold, requiring an extension of his dosing interval.

In this chapter, we work through three connected clinical admission calculations:
1. Partition total bed-scale weight into Body Surface Area, Devine Ideal Body Weight, and $40\%$ Adjusted Body Weight.
2. Evaluate Cockcroft–Gault creatinine clearance across weight compartments, and solve backward for the exact serum creatinine threshold $S$ where clearance drops below $30.0\text{ mL/min}$.
3. Scale pediatric weight-based medication doses and Holliday–Segar 4-2-1 hourly fluid maintenance for a $26.0\text{ kg}$ child in the step-down unit.

---

## Anthropometric Mass Partitioning and Body Surface Area

Every clinical dosing protocol on the **SC-80** is anchored by the persistent **Patient Profile ({{keycap:PAT}})**, accessed from the right-hand softkey inside {{key:BSA}}, {{key:GFR}}, {{key:DOS}}, or {{key:DRP}}. The {{keycap:PAT}} profile stores patient weight $W$ (in $\text{kg}$, {{keycap:W}}), height $H$ (in $\text{cm}$, {{keycap:H}}), chronological age $A$ (in years, {{keycap:A}}), steady-state serum creatinine $S$ (in $\text{mg/dL}$, {{keycap:S}}), and biological sex ({{keycap:MALE}} or {{keycap:FEM}}), automatically pre-populating those biometric variables across every clinical Equation Workspace ({{key:BSA}}, {{key:GFR}}, {{key:DOS}}, {{key:DRP}}, {{key:BRN}}).

### Mosteller Body Surface Area and Allometric Scaling ({{key:BSA}})

Two patients who each weigh $88.0\text{ kg}$ can possess markedly different internal drug distribution volumes. A tall, muscular patient has an expansive vascular bed, high cardiac output, and large hepatic and renal parenchymal mass, whereas a shorter, sedentary patient of the same $88.0\text{ kg}$ weight carries a substantial fraction of mass as poorly perfused adipose tissue. Because extracellular fluid volume, glomerular filtration, and basal metabolic rate correlate closely with external **Body Surface Area** ({{key:BSA}}, $B$) in square meters ($\text{m}^2$, averaging $1.73\text{ m}^2$ in a reference adult), Robert D. Mosteller (1987) formulated {{key:BSA}} from patient height $H$ (in $\text{cm}$) and total body weight $W$ (in $\text{kg}$) using the dimensional normalization constant $3600 = 60^2\text{ cm}\cdot\text{kg/m}^4$:

$$B = \sqrt{\frac{H \cdot W}{3600}} \iff W = \frac{3600 \, B^2}{H}$$

Here $H \cdot W$ forms a two-dimensional product of linear stature and mass, and taking the square root yields a geometric mean whose behavior closely tracks the classical 1916 Du Bois & Du Bois power law ($B = 0.007184 \, W^{0.425} H^{0.725}$) across infant, pediatric, and adult populations.

For our $68$-year-old male admission measuring $H = 175.0\text{ cm}$ and weighing $W = 88.0\text{ kg}$, the product of height and weight is $175.0 \times 88.0 = 15{,}400\text{ cm}\cdot\text{kg}$. Dividing by $3600$ gives $4.27778\text{ m}^4$, and extracting the square root yields a Body Surface Area of $B = \sqrt{4.27778} = \mathbf{2.0683\text{ m}^2}$.

### Devine Ideal Body Weight ({{key:IBW}}) and Forty-Percent Adjusted Body Weight ({{key:ABW}})

When dosing hydrophilic medications that remain inside lean tissue and extracellular water, using raw total body weight ($\text{TBW} = W$) in an overweight patient causes systematic over-dosing. To estimate lean metabolically active mass from skeletal stature alone, Ben Devine (1974) established the **Ideal Body Weight** ({{key:IBW}}, in $\text{kg}$) equations for adults at least $60\text{ inches}$ ($152.4\text{ cm}$, or $5\text{ feet}$) tall, where $H_{\text{in}} = H / 2.54$ is height in inches, $50.0\text{ kg}$ (male) and $45.5\text{ kg}$ (female) are the baseline lean weights at $60\text{ inches}$, and $2.3\text{ kg/in}$ ($0.9055\text{ kg/cm}$) is the linear lean-mass increment per inch above five feet:

$$\text{IBW}_{\text{male}} = 50.0 + 2.3\left(\frac{H}{2.54} - 60\right), \qquad \text{IBW}_{\text{female}} = 45.5 + 2.3\left(\frac{H}{2.54} - 60\right)$$

When a patient's total body weight $\text{TBW}$ exceeds $\text{IBW}$ by more than $20\%$, polar antibiotics such as aminoglycosides penetrate roughly $40\%$ into excess adipose extracellular water, which clinical pharmacists capture via **Adjusted Body Weight** ({{key:ABW}}, in $\text{kg}$) using the empirical adipose distribution factor $0.40$:

$$\text{ABW} = \text{IBW} + 0.40\left(\text{TBW} - \text{IBW}\right)$$

![Anthropometric weight compartments (IBW, AdjW, and Total Body Weight) governing hydrophilic and lipophilic drug distribution.](../assets/diagrams/domains/diagram_ch08_body_weight_compartments.png)

Evaluating Devine's formula for our $H = 175.0\text{ cm}$ ($H_{\text{in}} = 175.0 / 2.54 = 68.8976\text{ in}$) male patient via {{key:IBW}} gives $\text{IBW}_{\text{male}} = 50.0 + 2.3(68.8976 - 60.0) = 50.0 + 20.4646 = \mathbf{70.4646\text{ kg}}$ (whereas a female patient of the same $175.0\text{ cm}$ stature has $\text{IBW}_{\text{female}} = 45.5 + 20.4646 = \mathbf{65.9646\text{ kg}}$). Because his actual weight of $\text{TBW} = 88.0\text{ kg}$ is $88.0 / 70.4646 = 1.2489\times$ his ideal weight ($24.9\%$ above {{key:IBW}}), pressing {{key:ABW}} adds $40\%$ of his $17.5354\text{ kg}$ excess adipose mass to yield an Adjusted Body Weight of $\text{ABW} = 70.4646 + 0.40(88.0 - 70.4646) = \mathbf{77.4787\text{ kg}}$.

---

## Glomerular Filtration Kinetics and Pediatric Maintenance Scaling

With the patient's lean and adjusted mass compartments established, the pharmacist can translate his morning serum creatinine level into a physiological volumetric clearance rate.

### The Cockcroft–Gault Creatinine Clearance Equation ({{key:GFR}})

Creatinine is a nitrogenous breakdown product of creatine phosphate in skeletal muscle, released into blood plasma at a steady daily rate proportional to muscle mass and filtered freely by the renal glomeruli into the urine. At steady state, urinary creatinine excretion matches muscle creatinine production, making **Creatinine Clearance** ({{key:GFR}}, $C$)—the volume of plasma cleared of creatinine per minute ($\text{mL/min}$)—inversely proportional to steady-state serum creatinine ($S$, in $\text{mg/dL}$). Because skeletal muscle mass and nephron count decline linearly with adult age ($A$, in years), Donald Cockcroft and Henry Gault (1976) formulated bedside {{key:GFR}} from dosing weight $W$, using the empirical constant $72$ in the denominator and a $0.85$ factor in biological females ({{keycap:FEM}} in {{keycap:PAT}}) to reflect lower average skeletal muscle mass per kilogram:

$$C_{\text{male}} = \frac{\left(140 - A\right) \cdot W}{72 \cdot S}, \qquad C_{\text{female}} = 0.85 \cdot C_{\text{male}}$$

Hospital pharmacy protocols enforce a three-tier weight selection rule for $W$ inside the Cockcroft–Gault numerator: underweight patients ($\text{TBW} < \text{IBW}$) use actual $\text{TBW}$. Normal-weight patients ($\text{IBW} \le \text{TBW} \le 1.20\,\text{IBW}$) use Devine {{key:IBW}}. And overweight or obese patients ($\text{TBW} > 1.20\,\text{IBW}$) use $40\%$ Adjusted Body Weight ({{key:ABW}}).

![Clinical Cockcroft-Gault creatinine clearance (CrCl) staging tiers for renal dose adjustment.](../assets/diagrams/domains/diagram_ch08_renal_clearance_tiers.png)

In our $68$-year-old male patient with $S = 1.60\text{ mg/dL}$, notice how the age factor $(140 - 68) = 72$ equals the denominator constant $72$, reducing $C_{\text{male}}$ to $W / S$. If a clinician uses unadjusted Total Body Weight ($W = 88.0\text{ kg}$), estimated clearance appears to be $C_{\text{TBW}} = 88.0 / 1.60 = \mathbf{55.00\text{ mL/min}}$. Substituting his obesity-corrected Adjusted Body Weight ($W = \text{ABW} = 77.4787\text{ kg}$) lowers estimated glomerular filtration to $C_{\text{ABW}} = 77.4787 / 1.60 = \mathbf{48.424\text{ mL/min}}$ (and using strict lean {{key:IBW}} of $70.4646\text{ kg}$ gives $C_{\text{IBW}} = 70.4646 / 1.60 = \mathbf{44.040\text{ mL/min}}$), confirming that his renal clearance has dropped into the $< 50\text{ mL/min}$ moderate impairment tier where vancomycin maintenance dosing must be slowed. Conversely, solving the Cockcroft–Gault equation backward via {{key:XEQ}} for {{keycap:S}} at $C = 30.0\text{ mL/min}$ ($S = (140 - A)W / (72 C) = 77.4787 / 30.0 = \mathbf{2.583\text{ mg/dL}}$) tells the medical team the exact serum creatinine threshold that marks severe renal impairment for this patient.

### Holliday–Segar Pediatric Fluid Maintenance ({{key:421}}), Resting Energy ({{key:REE}}), and Patient-Bound Dosing ({{key:DOS}})

To replace daily insensible (respiratory and cutaneous) and urinary water losses in hospitalized children and adults, Malcolm Holliday and William Segar (1957) tied basal water requirements to metabolic caloric expenditure across three body-mass tiers, establishing the **4-2-1 Maintenance Fluid Rule** ({{key:421}}), while across clinical nutrition ({{key:REE}}) and veterinary medicine ({{key:VET}}), basal caloric demand follows Max Kleiber's $3/4$-power allometric **Resting Energy Expenditure** (in $\text{kcal/day}$):

$$R_{\text{maint,mL/hr}} = \begin{cases} 4 \cdot W & \text{if } W \le 10 \\ 40 + 2\left(W - 10\right) & \text{if } 10 < W \le 20 \\ 60 + 1\left(W - 20\right) & \text{if } W > 20 \end{cases}, \qquad \text{REE}_{\text{kcal/day}} = 70 \cdot W^{0.75}$$

Here the first $10\text{ kg}$ of body weight demands $4\text{ mL/kg/hr}$ (up to $40\text{ mL/hr}$), the next $10\text{ kg}$ between $10\text{ kg}$ and $20\text{ kg}$ adds $2\text{ mL/kg/hr}$ (up to $+20\text{ mL/hr}$), and each kilogram above $20\text{ kg}$ adds $1\text{ mL/kg/hr}$. For the $W = 26.0\text{ kg}$ pediatric patient on the step-down unit, pressing `26` {{key:421}} evaluates the hourly isotonic maintenance fluid rate as $R_{\text{maint}} = 40 + 20 + 1(26.0 - 20.0) = \mathbf{66.0\text{ mL/hr}}$ ($1{,}584\text{ mL/day}$). When prescribing weight-based medications via {{key:DOS}} (`T = W × D`), the **SC-80** binds {{keycap:W}} directly to the active Patient Profile ({{keycap:PAT}}) and logs the verified total dose $T$ to the `@MAR` Medication Administration Record in {{key:▦}}—and in the {{key:DOS}} Solver Workspace, allows the clinician to solve backward via {{key:XEQ}} for the delivered $\text{mg/kg}$ dose intensity $D = T / W$ when auditing a fixed tablet or vial strength $T$.

---

## Anthropometric Sizing and Renal Clearance on the Stack and in the Solver Workspace

On the **SC-80**, storing a patient's admission parameters into the persistent **Patient Profile ({{keycap:PAT}}: {{keycap:W}}, {{keycap:H}}, {{keycap:A}}, {{keycap:S}}, {{keycap:MALE}}/{{keycap:FEM}})** automatically pre-populates {{keycap:W}}, {{keycap:H}}, {{keycap:A}}, and {{keycap:S}} into the {{key:BSA}}, {{key:GFR}}, {{key:DOS}}, {{key:DRP}}, and {{key:BRN}} Equation Solver Workspaces while updating the live biometric header in {{key:▦}}.

![Patient Profile (@PAT) softkey architecture linking bedside biometric inputs to automated clinical clearance indices.](../assets/diagrams/domains/diagram_ch08_patient_profile_bar.png)

| Key / Solver | Mode | Inputs / Softkeys ({{keycap:LFU0}}–{{keycap:LFU4}}) | Governing Expression |
| :--- | :--- | :--- | :--- |
| {{keycap:PAT}} | Profile Bar | Softkeys: {{keycap:W}} {{keycap:H}} {{keycap:A}} {{keycap:S}} {{keycap:MALE}}/{{keycap:FEM}} {{keycap:PAT}} | Stores persistent patient biometrics ($W, H, A, S, \text{Sex}$) and updates {{key:▦}} |
| {{key:BSA}} | Stack / Solver | Stack: $Y = H, X = W$ • Solver: {{keycap:B}} {{keycap:H}} {{keycap:W}} {{keycap:PAT}} | $B = \sqrt{H \cdot W / 3600}$ (`H` and `W` pre-populated from {{keycap:PAT}}) |
| {{key:IBW}} / {{key:ABW}} | Immediate Stack | {{key:IBW}}: $X = H$ ($\text{cm}$) • {{key:ABW}}: $Y = \text{IBW}, X = \text{TBW}$ | Devine $\text{IBW} = 50 + 2.3(H/2.54 - 60)$; $\text{ABW} = Y + 0.40(X - Y)$ |
| {{key:GFR}} | Stack / Solver | Stack: $Z = A, Y = W, X = S$ • Solver: {{keycap:C}} {{keycap:A}} {{keycap:W}} {{keycap:S}} {{keycap:PAT}} | $C = (140 - A) \cdot W / (72 \cdot S)$ (`A`, `W`, `S` pre-populated from {{keycap:PAT}}) |
| {{key:421}} / {{key:REE}} | Immediate Stack | Register $X$: Patient weight $W$ ($\text{kg}$, or uses {{keycap:PAT}} $W$) | Holliday–Segar 4-2-1 $\text{mL/hr}$ ({{key:421}}); Kleiber $70 \cdot W^{0.75}\text{ kcal/day}$ ({{key:REE}}) |
| {{key:DOS}} | Stack / Solver | Stack: $Y = W, X = D$ (or $X = D$ with {{keycap:PAT}}) • Solver: {{keycap:T}} {{keycap:W}} {{keycap:D}} {{keycap:PAT}} | $T = W \times D$ (`W` pre-populated from {{keycap:PAT}}; logs to `@MAR` in {{key:▦}}) |

### Immediate Stack Trace: Partitioning Mass Compartments and Auditing Renal Clearance

At the bedside computer cart, the pharmacist evaluates Mosteller {{key:BSA}} for the $68$-year-old male patient ($H = 175\text{ cm}$, $W = 88\text{ kg}$), chains Devine {{key:IBW}} and $40\%$ Adjusted Body Weight ({{key:ABW}}), and compares {{key:ABW}}-adjusted versus unadjusted {{key:GFR}} at $S = 1.6\text{ mg/dL}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `175` {{key:ENTER}} `88` {{key:BSA}} | $0$ | $0$ | $0$ | $2.0683$ | Compute Mosteller surface area $B = \sqrt{175 \times 88 / 3600} = 2.0683\text{ m}^2$ |
| `175` {{key:IBW}} | $0$ | $0$ | $2.0683$ | $70.4646$ | Lift {{key:BSA}} to Register $Y$; evaluate Devine $\text{IBW}_{\text{male}} = 70.4646\text{ kg}$ |
| `88` {{key:ABW}} | $0$ | $0$ | $2.0683$ | $77.4787$ | Blend $\text{IBW}$ ($Y$) and $\text{TBW} = 88\text{ kg}$ ($X$) into $\text{ABW} = 77.4787\text{ kg}$ |
| `68` {{key:x⇄y}} `1.6` {{key:GFR}} | $2.0683$ | $2.0683$ | $2.0683$ | $48.4242$ | Evaluate {{key:ABW}}-adjusted clearance $C_{\text{ABW}} = 48.42\text{ mL/min}$ ($Z=68, Y=77.48, X=1.6$) |
| `68` {{key:ENTER}} `88` {{key:ENTER}} `1.6` {{key:GFR}} | $48.4242$ | $48.4242$ | $48.4242$ | **$55.0000$** | Compare unadjusted total-weight clearance $C_{\text{TBW}} = 55.00\text{ mL/min}$ |

### Bidirectional Solver Workspaces ({{key:GFR}} and {{key:DOS}}): Pre-Populated Patient Biometrics and Inverse Clearance

Now see how the persistent Patient Profile ({{keycap:PAT}}) accelerates clinical what-if analysis in the {{key:GFR}} (`C = (140-A)W/(72×S)`) and {{key:DOS}} (`T = W × D`) Equation Workspaces. When the pharmacist opens {{key:GFR}} on a cleared stack ({{key:C}} {{key:GFR}}) after setting the patient profile via {{keycap:PAT}}, the patient's age `A = 68`, weight `W = 77.48` (updated to {{key:ABW}}), and serum creatinine `S = 1.6` are already bound on the softkey bar. The pharmacist first solves forward via {{key:XEQ}} for {{keycap:C}}, then stores `30` into {{keycap:C}} and solves **backward** via {{key:XEQ}} on {{keycap:S}} to find the exact serum creatinine level at which this patient would enter severe renal impairment ($C = 30.0\text{ mL/min}$), and finally opens {{key:DOS}} ({{key:C}} {{key:DOS}}) to back-calculate the exact $\text{mg/kg}$ dose intensity {{keycap:D}} delivered by a standard $T = 1250\text{ mg}$ vancomycin minibag:

| Step & Action | Line 1 Workspace Formula | Softkey Legend Bar ({{keycap:LFU0}}–{{keycap:LFU4}}) | Register X Result & Physical Meaning |
| :--- | :--- | :--- | :--- |
| {{key:C}} {{key:GFR}} (open workspace) | `GFR: C = (140-A)W/(72×S)` | {{keycap:C}} `[A=68]` `[W=77.48]` `[S=1.6]` {{keycap:PAT}} | Opens {{key:GFR}} workspace pre-populated from Patient Profile {{keycap:PAT}} |
| {{key:XEQ}} $\to$ {{keycap:C}} | `C = 48.4242` | `[C=48.42]` `[A=68]` `[W=77.48]` `[S=1.6]` {{keycap:PAT}} | Solves forward for {{key:ABW}} Creatinine Clearance $C = \mathbf{48.42\text{ mL/min}}$ |
| `30` $\to$ {{keycap:C}}, {{key:XEQ}} $\to$ {{keycap:S}} | `S = 2.5826` | `[C=30]` `[A=68]` `[W=77.48]` `[S=2.58]` {{keycap:PAT}} | Solves backward for critical creatinine threshold $S = \mathbf{2.58\text{ mg/dL}}$ |
| {{key:C}} {{key:DOS}} (open workspace) | `DOS: T = W × D` | {{keycap:T}} `[W=77.48]` {{keycap:D}} {{keycap:PAT}} | Opens weight-based dosing workspace with `W = 77.48 kg` pre-bound |
| `1250` $\to$ {{keycap:T}}, {{key:XEQ}} $\to$ {{keycap:D}} | `D = 16.1335` | `[T=1250]` `[W=77.48]` `[D=16.13]` {{keycap:PAT}} | Solves backward for delivered dose intensity $D = \mathbf{16.13\text{ mg/kg}}$ (within $15\text{–}20\text{ mg/kg}$) |

### Try It on the Stack

Practice anthropometric partitioning, {{keycap:PAT}}-coupled renal clearance, and inverse dosing audits across these three clinical admissions:

1. **Oncology Carboplatin & BSA Sizing ({{key:BSA}}, {{key:IBW}} & {{key:ABW}}):** A female oncology patient measures $H = 162.56\text{ cm}$ ($64.0\text{ in}$) and weighs $\text{TBW} = 84.0\text{ kg}$. Compute her Mosteller {{key:BSA}}, her female Devine {{key:IBW}} ($\text{IBW}_{\text{male}} - 4.5\text{ kg}$), and her $40\%$ Adjusted Body Weight (`162.56` {{key:ENTER}} `84` {{key:BSA}} `162.56` {{key:IBW}} `4.5` {{key:-}} `84` {{key:ABW}}). *(Verified Register $X$ results: $B = \mathbf{1.9476\text{ m}^2}$, $\text{IBW}_{\text{female}} = \mathbf{54.70\text{ kg}}$, and $\text{ABW} = \mathbf{66.42\text{ kg}}$.)*
2. **Geriatric Female Renal Clearance Comparison ({{key:GFR}}):** An $80$-year-old female patient weighs $W = 54.0\text{ kg}$ with a seemingly normal serum creatinine of $S = 1.20\text{ mg/dL}$. In the {{key:GFR}} Solver Workspace ({{key:C}} {{key:GFR}}), store `80` in {{keycap:A}}, `54` in {{keycap:W}}, and `1.2` in {{keycap:S}}, press {{key:XEQ}} $\to$ {{keycap:C}}, and multiply by the $0.85$ female factor (or toggle {{keycap:FEM}} inside {{keycap:PAT}}). *(Verified result: $C_{\text{female}} = \mathbf{31.875\text{ mL/min}}$.)*
3. **Pediatric 4-2-1 Fluid Maintenance ({{key:421}}) and Amoxicillin Dose Audit ({{key:DOS}}):** Compute the hourly Holliday–Segar maintenance fluid rate for an $18.5\text{ kg}$ toddler (`18.5` {{key:421}}), and in the {{key:DOS}} Solver Workspace ({{key:C}} {{key:DOS}}) with `W = 18.5 kg`, store `832.5` in {{keycap:T}} and press {{key:XEQ}} $\to$ {{keycap:D}} to solve backward for $\text{mg/kg/dose}$ when a clinician orders a fixed $T = 832.5\text{ mg}$ amoxicillin dose. *(Verified results: $R_{\text{maint}} = \mathbf{57.00\text{ mL/hr}}$ and $D = \mathbf{45.00\text{ mg/kg/dose}}$.)*

From admission anthropometrics and renal clearance staging on the ward, we move in Chapter 23 to the intensive care unit at shift change—where weight-based microgram titrations, inverse infusion-pump audits, and gravity tubing drop factors govern continuous vasopressor support.

---

# Chapter 23: Titrating the ICU Norepinephrine Pump at Shift Change

At 7:00 p.m. shift change in the medical intensive care unit, an oncoming critical-care nurse takes handover on an $W = 80.0\text{ kg}$ patient in distributive septic shock. The bedside peristaltic infusion pump is actively infusing a high-alert central-venous vasopressor at a volumetric flow rate of $R = 15.0\text{ mL/hr}$ from a pharmacy bag labeled $400\text{ mg}$ dissolved in $250\text{ mL}$ of $5\%$ dextrose in water ($\text{D}_5\text{W}$, concentration $C = 1600\ \mu\text{g/mL}$). Before co-signing the shift-change medication administration record (`@MAR`), the oncoming nurse must verify the pump in **both directions**: first, given the physician's active order of $D = 5.0\ \mu\text{g/kg/min}$, confirming the forward pump rate $R = 15.0\text{ mL/hr}$. And second, when inheriting a running infusion pump in the neighboring trauma bay set to $R = 27.0\text{ mL/hr}$ on a $W = 72.0\text{ kg}$ patient from a standard norepinephrine bag ($4.0\text{ mg}$ in $250\text{ mL}$, so $C = 16.0\ \mu\text{g/mL}$), solving **backward** to verify the exact delivered dose rate in $\mu\text{g/kg/min}$.

Twenty minutes into the shift, the $80.0\text{ kg}$ patient requires an urgent computed-tomography (CT) angiogram in the basement radiology suite. To prepare a backup manual drip count in case the transport infusion pump battery fails in the elevator, the nurse checks a macro-drip intravenous administration set rated at a Drop Factor of $DF = 15\text{ gtt/mL}$ alongside a pediatric micro-drip chamber rated at $60\text{ gtt/mL}$, converting the hourly volumetric flow rate into visible drops per minute.

In this chapter, we work through three critical-care infusion and hemodynamic themes:
1. Convert weight-based vasoactive dose orders ($\mu\text{g/kg/min}$) into hourly volumetric infusion pump rates ($\text{mL/hr}$).
2. Solve running infusion pumps backward at shift change to audit the exact delivered microgram-per-kilogram-per-minute dose rate.
3. Calibrate manual gravity tubing drop rates ($\text{gtt/min}$), monitor Mean Arterial Pressure and Cardiac Output, and size a biphasic $24\text{-hour}$ Parkland burn resuscitation protocol.

---

## Weight-Based Vasoactive Titrations and Inverse Pump Verification

Critical-care catecholamines and inotropes (norepinephrine, epinephrine, dopamine, dobutamine, and milrinone) have plasma half-lives of only one to two minutes, so they must be infused continuously and titrated to the patient's real-time arterial pressure. Bridging the physician's physiological order ($D$, in $\mu\text{g/kg/min}$) and the mechanical pump's volumetric displacement rate ($R$, in $\text{mL/hr}$) requires a dimensional chain through mass flux and solution concentration.

### The Four-Variable Vasoactive Drip Law ({{key:DRP}})

When a physician orders a continuous weight-based dose $D$ (in $\mu\text{g}\cdot\text{kg}^{-1}\cdot\text{min}^{-1}$) for a patient of body mass $W$ (in $\text{kg}$, pre-populated from {{keycap:PAT}}), multiplying $D \cdot W$ gives the microgram delivery rate per minute ($\mu\text{g/min}$), and multiplying by $60\text{ min/hr}$ yields the hourly microgram flux $\dot{m}_{\text{mcg/hr}} = 60 D W$ (or dividing by $1000\ \mu\text{g/mg}$ via the immediate {{key:DRP}} stack operator gives the hourly milligram flux $\dot{m}_{\text{mg/hr}} = 0.060 D W$). Dividing the hourly microgram flux by the pharmacy bag's microgram concentration $C = 1000 \cdot (M_{\text{bag,mg}} / V_{\text{bag,mL}})$ (in $\mu\text{g/mL}$) yields the **Volumetric Infusion Pump Rate** $R$ (in $\text{mL/hr}$), while algebraic inversion in the {{key:DRP}} Solver Workspace solves backward via {{key:XEQ}} for the **Delivered Dose Rate** $D$ from an observed pump rate $R$:

$$R = \frac{D \cdot W \cdot 60}{C} \iff D = \frac{R \cdot C}{60 \cdot W}, \qquad C = \frac{1000 \cdot M_{\text{bag,mg}}}{V_{\text{bag,mL}}}$$

![Dimensional unit-cancellation chain transforming weight-based vasoactive dose orders (mcg/kg/min) into volumetric pump rates (mL/hr).](../assets/diagrams/domains/diagram_ch08_drip_dimensional_chain.png)

In our first ICU shift-change audit ($W = 80.0\text{ kg}$, $D = 5.0\ \mu\text{g/kg/min}$, and $400\text{ mg}$ in $250\text{ mL}$ $\text{D}_5\text{W}$ so $C = 1600\ \mu\text{g/mL} = 1.60\text{ mg/mL}$), the hourly drug delivery is $\dot{m} = 5.0 \times 80.0 \times 60 = 24{,}000\ \mu\text{g/hr} = \mathbf{24.00\text{ mg/hr}}$, and dividing by $C = 1600\ \mu\text{g/mL}$ sets the volumetric pump to $R = 24{,}000 / 1600 = \mathbf{15.00\text{ mL/hr}}$. Conversely, when the nurse inherits the running norepinephrine pump in the next bay set to $R = 27.0\text{ mL/hr}$ for a $W = 72.0\text{ kg}$ patient with a standard $4.0\text{ mg} / 250\text{ mL}$ bag ($C = 16.0\ \mu\text{g/mL}$), solving {{key:DRP}} backward via {{key:XEQ}} for {{keycap:D}} gives $D = (27.0 \times 16.0) / (60 \times 72.0) = 432.0 / 4320.0 = \mathbf{0.100\ \mu\text{g/kg/min}}$.

---

## Gravity Drip Calibration, Arterial Perfusion, and Burn Resuscitation

When transporting unstable patients or operating in field and disaster settings without electronic peristaltic pumps, nurses regulate intravenous flow by counting liquid drops falling through a calibrated drip chamber against the sweep second hand of a watch.

### Orifice Drop Factors and Gravity Drip Rate Calibration (gtt)

Every manual intravenous administration set manufactures its drip-chamber orifice to form drops of a fixed volumetric size, specified by the tubing **Drop Factor** ($DF_{\text{gtt/mL}}$, in drops per milliliter, $\text{gtt/mL}$). Standard adult **macro-drip** sets deliver $10$, $15$, or $20\text{ gtt/mL}$, whereas pediatric and critical-care **micro-drip** sets use a fine stainless-steel needle orifice that delivers $60\text{ gtt/mL}$. Multiplying the hourly volumetric flow rate $R_{\text{mL/hr}}$ by $DF_{\text{gtt/mL}}$ gives drops per hour, and dividing by $60\text{ min/hr}$ yields the **Gravity Drip Rate** ({{key:gtt}}, $R_{\text{gtt/min}}$, in drops per minute):

$$R_{\text{gtt/min}} = \frac{R_{\text{mL/hr}} \cdot DF_{\text{gtt/mL}}}{60}$$

Notice the geometric elegance of the $60\text{ gtt/mL}$ micro-drip chamber: when $DF_{\text{gtt/mL}} = 60$, the ratio $60 / 60$ equals unity, so $R_{\text{gtt/min}} = R_{\text{mL/hr}}$ numerically. For our ICU transport running at $R_{\text{mL/hr}} = 15.00\text{ mL/hr}$, a macro-drip set with $DF = 15\text{ gtt/mL}$ produces a drip rate via {{key:gtt}} of $R_{\text{gtt/min}} = (15.00 \times 15) / 60 = \mathbf{3.75\text{ gtt/min}}$, whereas switching to a $60\text{ gtt/mL}$ micro-drip chamber raises the drip frequency to $\mathbf{15.00\text{ gtt/min}}$ (one drop every $4.0\text{ seconds}$).

### Mean Arterial Pressure ({{key:MAP}}), Cardiac Output ({{key:ICU}}), and Parkland Burn Crystalloid Resuscitation ({{key:BRN}})

Vasoactive infusions are titrated to restore organ perfusion pressure and cardiac output, while severe thermal burns require high-volume crystalloid infusions to replace capillary plasma leakage. At resting heart rates, the cardiac ventricles spend roughly one-third of each cardiac cycle in systolic ejection ($\text{SBP}$, in $\text{mmHg}$) and two-thirds in diastolic relaxation ($\text{DBP}$, in $\text{mmHg}$), defining **Mean Arterial Pressure** ({{key:MAP}}, in $\text{mmHg}$), while multiplying heart rate $H$ ($\text{bpm}$) by stroke volume $S$ ($\text{mL/beat}$) and dividing by $1000\text{ mL/L}$ gives **Cardiac Output** ({{key:ICU}}, $Q = H \cdot S / 1000\text{ L/min}$). Simultaneously, Charles Baxter's 1968 **Parkland Formula** ({{key:BRN}}) sizes the total $24\text{-hour}$ Lactated Ringer's crystalloid resuscitation volume $V$ (in $\text{mL}$) from patient weight $W$ (pre-populated from {{keycap:PAT}}) and the percentage of Total Body Surface Area burned ($B = \%\,\text{TBSA}$, entered as a whole number such as $35$ for $35\%$):

$$\text{MAP} = \text{DBP} + \frac{1}{3}\left(\text{SBP} - \text{DBP}\right) = \frac{\text{SBP} + 2 \cdot \text{DBP}}{3}, \qquad V = 4\text{ mL} \times W \times B$$

Parkland protocol infuses the first half of $V$ over the **first $8\text{ hours}$** from the time of burn injury ($R_{1\text{st }8\text{h}} = V / 16\text{ mL/hr}$) and the second half over the **subsequent $16\text{ hours}$** ($R_{\text{next }16\text{h}} = V / 32\text{ mL/hr}$).

![Parkland 24-hour biphasic crystalloid resuscitation infusion profile (50% in the first 8 hours, 50% over the next 16 hours).](../assets/diagrams/domains/diagram_ch08_parkland_burn.png)

When the $80.0\text{ kg}$ ICU patient's arterial line reads $106 / 52\text{ mmHg}$ on $5.0\ \mu\text{g/kg/min}$ of vasopressor, pressing {{key:MAP}} shows that his perfusion pressure is $\text{MAP} = 52 + \frac{1}{3}(106 - 52) = 52 + 18 = \mathbf{70.0\text{ mmHg}}$, safely above the $65\text{ mmHg}$ autoregulatory threshold. In the adjacent trauma bay, an $W = 80.0\text{ kg}$ firefighter with second- and third-degree burns across $B = 35\%\text{ TBSA}$ requires a $24\text{-hour}$ Parkland volume ({{key:BRN}}) of $V = 4 \times 80.0 \times 35 = \mathbf{11{,}200\text{ mL}}$, setting the volumetric infusion pump ({{key:IV}}: `R = V / T`) to $5{,}600 / 8 = \mathbf{700.0\text{ mL/hr}}$ for the first $8\text{ hours}$ and $5{,}600 / 16 = \mathbf{350.0\text{ mL/hr}}$ for the following $16\text{ hours}$.

---

## Vasopressor Titrations and Inverse Pump Audits on the Stack and in the Solver Workspace

On the **SC-80**, vasoactive drip titration ({{key:DRP}}), volumetric pump rate ({{key:IV}}), gravity drip calibration ({{key:gtt}}), Mean Arterial Pressure ({{key:MAP}}), Parkland burn resuscitation ({{key:BRN}}), and hemodynamic cardiac output ({{key:ICU}}) operate both on the RPN stack and in {{keycap:PAT}}-linked Equation Solver Workspaces.

| Key / Solver | Mode | Inputs / Softkeys ({{keycap:LFU0}}–{{keycap:LFU4}}) | Governing Expression |
| :--- | :--- | :--- | :--- |
| {{key:DRP}} | Stack / Solver | Stack: $Y = D, X = W$ • Solver: {{keycap:R}} {{keycap:D}} {{keycap:W}} {{keycap:C}} {{keycap:PAT}} | Stack: $\dot{m}_{\text{mg/hr}} = D \cdot W \cdot 60 / 1000$; Solver: $R = D \cdot W \cdot 60 / C$ |
| {{key:IV}} | Stack / Solver | Stack: $Y = V_{\text{mL}}, X = T_{\text{hr}}$ • Solver: {{keycap:R}} {{keycap:V}} {{keycap:T}} | $R = V / T \iff T = V / R$ (Volumetric pump rate & bag duration) |
| {{key:gtt}} | Immediate Stack | Register $Y$: Flow rate $R_{\text{mL/hr}}$, Register $X$: Drop factor $DF$ | Gravity drip rate $R_{\text{gtt/min}} = (Y \cdot X) / 60$ |
| {{key:MAP}} | Immediate Stack | Register $Y$: Systolic $\text{SBP}$, Register $X$: Diastolic $\text{DBP}$ | $\text{MAP} = X + (Y - X) / 3 = (Y + 2X) / 3$ ($\text{mmHg}$) |
| {{key:BRN}} | Stack / Solver | Stack: $Y = W, X = B$ • Solver: {{keycap:V}} {{keycap:W}} {{keycap:B}} | Parkland 24-hr volume $V = 4 \cdot W \cdot B$ (`W` pre-populated from {{keycap:PAT}}) |
| {{key:ICU}} | Stack / Solver | Stack: $Y = H_{\text{bpm}}, X = S_{\text{mL}}$ • Solver: {{keycap:Q}} {{keycap:H}} {{keycap:S}} | Cardiac output $Q = H \cdot S / 1000$ ($\text{L/min}$) |

### Immediate Stack Trace: Auditing the Vasopressor Pump, Gravity Drip, and Burn Resuscitation

During the shift-change double check, the nurse evaluates the hourly mass flux ({{key:DRP}}), divides by the bag concentration ($400\text{ mg} / 250\text{ mL} = 1.60\text{ mg/mL}$) to obtain the volumetric pump rate (`15.00 mL/hr`), calibrates the $15\text{ gtt/mL}$ macro-drip set ({{key:gtt}}), verifies {{key:MAP}} at $106 / 52\text{ mmHg}$, and computes the Parkland burn infusion rates ({{key:BRN}}, {{key:IV}}):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `5` {{key:ENTER}} `80` {{key:DRP}} | $0$ | $0$ | $0$ | $24.0000$ | Compute vasopressor mass delivery $\dot{m} = 24.00\text{ mg/hr}$ ($24{,}000\ \mu\text{g/hr}$) |
| `400` {{key:ENTER}} `250` {{key:÷}} {{key:÷}} | $0$ | $0$ | $0$ | $15.0000$ | Divide by bag concentration $1.60\text{ mg/mL}$: pump rate $R = 15.00\text{ mL/hr}$ |
| {{key:ENTER}} {{key:ENTER}} `15` {{key:gtt}} | $0$ | $0$ | $15.0000$ | $3.7500$ | Preserve $R = 15.00\text{ mL/hr}$ in $Y$ and compute $15\text{ gtt/mL}$ drip: $3.75\text{ gtt/min}$ |
| `106` {{key:ENTER}} `52` {{key:MAP}} | $15$ | $15.0000$ | $3.7500$ | $70.0000$ | Evaluate Mean Arterial Pressure $\text{MAP} = 52 + (106 - 52)/3 = 70.0\text{ mmHg}$ |
| `80` {{key:ENTER}} `35` {{key:BRN}} `16` {{key:IV}} | $3.75$ | $3.7500$ | $70.0000$ | **$700.000$** | Compute $24\text{-hr}$ Parkland volume ($11{,}200\text{ mL}$) and first-$8\text{-hr}$ rate $700.0\text{ mL/hr}$ |

### Bidirectional Solver Workspaces ({{key:DRP}} and {{key:IV}}): Back-Calculating Delivered Dose from an Inherited Pump

Now see how the {{key:DRP}} Equation Workspace (`R = D × W × 60 / C`) protects patient safety at shift change when a nurse inherits an infusion pump already running at $R\text{ mL/hr}$. With patient weight {{keycap:W}} automatically pre-populated from {{keycap:PAT}}, the nurse opens {{key:DRP}} on a cleared stack ({{key:C}} {{key:DRP}}), confirms the forward pump rate $R = 15.0\text{ mL/hr}$ for the $80.0\text{ kg}$ patient ($D = 5.0\ \mu\text{g/kg/min}$, $C = 1600\ \mu\text{g/mL}$), and then audits the inherited norepinephrine pump running at $R = 27.0\text{ mL/hr}$ on the $W = 72.0\text{ kg}$ patient ($4.0\text{ mg} / 250\text{ mL} \implies C = 16.0\ \mu\text{g/mL}$) by pressing {{key:XEQ}} on {{keycap:D}}:

| Step & Action | Line 1 Workspace Formula | Softkey Legend Bar ({{keycap:LFU0}}–{{keycap:LFU4}}) | Register X Result & Physical Meaning |
| :--- | :--- | :--- | :--- |
| {{key:C}} {{key:DRP}} (open workspace) | `DRP: R = D × W × 60 / C` | {{keycap:R}} {{keycap:D}} `[W=80]` {{keycap:C}} {{keycap:PAT}} | Opens vasoactive drip solver with `W = 80 kg` pre-bound from {{keycap:PAT}} |
| `5` $\to$ {{keycap:D}}, `1600` $\to$ {{keycap:C}}, {{key:XEQ}} $\to$ {{keycap:R}} | `R = 15.0000` | `[R=15]` `[D=5]` `[W=80]` `[C=1600]` {{keycap:PAT}} | Solves forward for volumetric pump rate $R = \mathbf{15.00\text{ mL/hr}}$ |
| `27` $\to$ {{keycap:R}}, `72` $\to$ {{keycap:W}}, `16` $\to$ {{keycap:C}} | `DRP: R = D × W × 60 / C` | `[R=27]` {{keycap:D}} `[W=72]` `[C=16]` {{keycap:PAT}} | Stores inherited pump rate $R = 27\text{ mL/hr}$, $W = 72\text{ kg}$, $C = 16\ \mu\text{g/mL}$ |
| {{key:XEQ}} $\to$ {{keycap:D}} | `D = 0.1000` | `[R=27]` `[D=0.1]` `[W=72]` `[C=16]` {{keycap:PAT}} | Solves backward for delivered norepinephrine dose $D = \mathbf{0.100\ \mu\text{g/kg/min}}$ |
| {{key:C}} {{key:IV}}, `250` $\to$ {{keycap:V}}, `27` $\to$ {{keycap:R}}, {{key:XEQ}} $\to$ {{keycap:T}} | `T = 9.2593` | `[R=27]` `[V=250]` `[T=9.26]` | Solves {{key:IV}} (`R = V / T`) backward for time until bag empty $T = \mathbf{9.26\text{ hr}}$ |

### Try It on the Stack

Verify these three critical-care infusion and hemodynamic calculations on the stack and in the {{key:DRP}} / {{key:IV}} Solver Workspaces:

1. **Inverse Epinephrine Pump Audit ({{key:DRP}} Solver):** An oncoming ICU nurse inherits an epinephrine infusion running at $R = 21.0\text{ mL/hr}$ on a $W = 70.0\text{ kg}$ patient from a standard bag of $4.0\text{ mg}$ in $250\text{ mL}$ ($C = 16.0\ \mu\text{g/mL}$). In the {{key:DRP}} Solver Workspace ({{key:C}} {{key:DRP}}), store `21` in {{keycap:R}}, `70` in {{keycap:W}}, and `16` in {{keycap:C}}, and press {{key:XEQ}} $\to$ {{keycap:D}} to solve backward for the delivered dose rate. *(Verified result: $D = \mathbf{0.080\ \mu\text{g/kg/min}}$.)*
2. **Dobutamine Inotropic Infusion and Macro-Drip Count ({{key:DRP}} & {{key:gtt}}):** A $W = 90.0\text{ kg}$ heart-failure patient receives dobutamine at $D = 7.5\ \mu\text{g/kg/min}$ from a $500\text{ mg}$ in $250\text{ mL}$ bag ($C = 2000\ \mu\text{g/mL} = 2.0\text{ mg/mL}$). Compute the pump rate in $\text{mL/hr}$ and the gravity drop rate through a $20\text{ gtt/mL}$ tubing set (`7.5` {{key:ENTER}} `90` {{key:DRP}} `2` {{key:÷}} `20` {{key:gtt}}). *(Verified Register $X$ results: $R = \mathbf{20.25\text{ mL/hr}}$ and $R_{\text{gtt}} = \mathbf{6.75\text{ gtt/min}}$.)*
3. **Vancomycin Minibag Duration ({{key:IV}}) and Mean Arterial Pressure ({{key:MAP}}):** In the {{key:IV}} Solver Workspace ({{key:C}} {{key:IV}}, `R = V / T`), store minibag volume `250` $\to$ {{keycap:V}} ($\text{mL}$) and maximum safe vancomycin infusion rate `166.67` $\to$ {{keycap:R}} ($\text{mL/hr}$), press {{key:XEQ}} $\to$ {{keycap:T}} to solve backward for minimum infusion time in hours, and check {{key:MAP}} for an arterial pressure of $92 / 50\text{ mmHg}$ (`92` {{key:ENTER}} `50` {{key:MAP}}). *(Verified results: $T = \mathbf{1.50\text{ hr}}$ ($90\text{ min}$) and $\text{MAP} = \mathbf{64.00\text{ mmHg}}$.)*

Having mastered continuous intravenous pump titrations and hemodynamic monitoring in Chapter 23, we turn in Chapter 24 to therapeutic drug monitoring, arterial blood gas and electrolyte interpretation, and aeromedical transport oxygen budgeting.

---

# Chapter 24: Tracking the Trough Across Five Half-Lives

Twelve hours after receiving an initial $500\text{ mg}$ intravenous bolus of a renally cleared antibiotic regimen, an ICU patient's blood is drawn for therapeutic drug monitoring (TDM) alongside an arterial blood gas (ABG), a 12-lead electrocardiogram (ECG), and a comprehensive metabolic panel. Pharmacokinetic population modeling for this patient estimates an **Apparent Volume of Distribution** of $V = 25.0\text{ L}$ and a biological **Elimination Half-Life** of $T_{1/2} = 6.0\text{ hours}$. Before ordering the next $500\text{ mg}$ maintenance dose on an every-$12\text{-hour}$ ($\tau = 12.0\text{ hr}$) schedule, the clinical pharmacist must calculate the initial post-bolus peak concentration $C_0$, the first-order elimination rate constant $K$, the $12\text{-hour}$ pre-dose trough concentration $C(12)$, and the steady-state peak and trough levels that will be reached after five half-lives ($30.0\text{ hours}$) of repeated dosing. When a neighboring renal-failure patient returns a supratherapeutic vancomycin trough of $C_0 = 32.0\text{ mg/L}$ ($K = 0.05776\text{ hr}^{-1}$, $T_{1/2} = 12.0\text{ hr}$), the pharmacist also solves the exponential decay equation **backward** for the exact hold time $T$ required for the serum level to decay safely to $C = 15.0\text{ mg/L}$.

Simultaneously, the patient's chemistry panel, arterial blood gas, and ECG return from the laboratory with $[\text{Na}^+] = 140\text{ mEq/L}$, $[\text{Cl}^-] = 102\text{ mEq/L}$, $[\text{HCO}_3^-] = 14\text{ mEq/L}$, measured total calcium $\text{Ca}_{\text{meas}} = 7.6\text{ mg/dL}$ with severe hypoalbuminemia of $\text{Albumin} = 2.0\text{ g/dL}$, blood glucose $350\text{ mg/dL}$, inspired oxygen $F_i\text{O}_2 = 0.40$ with arterial $P_a\text{O}_2 = 110\text{ mmHg}$ and $P_a\text{CO}_2 = 28\text{ mmHg}$, and a measured ECG $\text{QT}$ interval of $420\text{ ms}$ at heart rate $96\text{ bpm}$. Finally, before transferring the patient by helicopter for a $T = 70.0\text{-minute}$ flight using an E-cylinder pressurized to $P = 1950\text{ psi}$, the respiratory therapist must solve for the maximum safe oxygen flow rate $F$ in $\text{L/min}$.

This chapter weaves together three critical-care diagnostic themes:
1. Model first-order exponential drug elimination, steady-state accumulation across five half-lives, and inverse hold-time calculations for supratherapeutic troughs.
2. Evaluate pulmonary oxygenation ($P/F$ ratio and Alveolar–arterial $\text{O}_2$ gradient), metabolic acid-base status (anion gap), and corrected serum calcium, sodium, and osmolality.
3. Normalize cardiac repolarization ($\text{QT}_c$) across heart rate and budget compressed oxygen cylinder duration for aeromedical transport.

---

## Multi-Compartment Elimination and Steady-State Superposition

In linear pharmacokinetics, the body is modeled either as a single well-mixed fluid volume $V$ (one-compartment model) or as a central vascular compartment $V_1$ exchanging drug reversibly with a peripheral tissue compartment $V_2$ before renal and hepatic elimination:

$$C_{\text{2-comp}}(t) = A \, e^{-\alpha t} + B \, e^{-\beta t} \xrightarrow{t \gg 1/\alpha} B \, e^{-\beta t}, \qquad C(t) = C_0 \, e^{-K t}$$

For glycopeptides and aminoglycosides sampled after the rapid $\alpha$-distribution phase ($30\text{–}60\text{ minutes}$ post-infusion) has equilibrated, plasma concentrations follow a single terminal exponential governed by the elimination rate constant $K = \beta$ and apparent volume of distribution $V$ ({{key:PK}}).

### Exponential Decay, Rate Constants, and Elimination Half-Life ({{key:PK}})

When an intravenous bolus dose of mass $D$ (in $\text{mg}$) mixes across the **Apparent Volume of Distribution** ($V$, in liters $\text{L}$) cleared at volumetric **Systemic Clearance** rate $C_{\text{CL}}$ (in $\text{L/hr}$), it establishes an initial peak concentration $C_0 = D / V$ (in $\text{mg/L}$). Because the rate of drug elimination $-dM/dt = C_{\text{CL}} \cdot C(t)$ is proportional to instantaneous concentration $C(t)$, plasma concentration decays exponentially according to the first-order **Elimination Rate Constant** ($K$, in $\text{hr}^{-1}$) and **Elimination Half-Life** ($T_{1/2}$, in hours), where $\ln(2) \approx 0.693147$ ({{key:PK}}):

$$T_{1/2} = \frac{\ln(2) \cdot V}{C_{\text{CL}}} = \frac{\ln(2)}{K}, \qquad C(T) = C_0 \, e^{-K T} \iff T = \frac{\ln\left(C_0 / C\right)}{K}$$

![Multi-dose pharmacokinetic plasma accumulation profile approaching steady state within the narrow therapeutic window between MEC and MTC.](../assets/diagrams/domains/diagram_ch08_therapeutic_window.png)

In our ICU patient receiving a $D = 500\text{ mg}$ intravenous antibiotic bolus into $V = 25.0\text{ L}$ with $T_{1/2} = 6.0\text{ hr}$, the initial peak plasma concentration is $C_0 = 500 / 25.0 = \mathbf{20.00\text{ mg/L}}$. Pressing `6` {{key:PK}} divides $\ln(2) = 0.693147$ by $T_{1/2} = 6.0\text{ hr}$ to give a first-order elimination rate constant of $K = 0.693147 / 6.0 = \mathbf{0.11552\text{ hr}^{-1}}$ and a systemic clearance of $C_{\text{CL}} = K \cdot V = 0.11552 \times 25.0 = \mathbf{2.8881\text{ L/hr}}$. At $T = 12.0\text{ hr}$ ($2.0$ half-lives), the plasma concentration decays to $C(12) = 20.00 \times e^{-0.11552 \times 12.0} = 20.00 \times (0.5)^2 = \mathbf{5.00\text{ mg/L}}$. Conversely, for the neighboring patient whose vancomycin trough returned supratherapeutic at $C_0 = 32.0\text{ mg/L}$ with $T_{1/2} = 12.0\text{ hr}$ ($K = \ln(2)/12 = 0.057762\text{ hr}^{-1}$), solving the decay law backward for the hold time $T$ needed to reach a safe target trough of $C = 15.0\text{ mg/L}$ gives $T = \ln(32.0 / 15.0) / 0.057762 = 0.75769 / 0.057762 = \mathbf{13.117\text{ hr}}$ (or at $T_{1/2} = 6.0\text{ hr}$, $K = 0.11552\text{ hr}^{-1} \implies T = \mathbf{6.559\text{ hr}}$).

### Superposition and Steady-State Accumulation Across Five Half-Lives

When the same maintenance dose $D$ is repeated at a fixed dosing interval $\tau$ (in hours), each new dose adds $C_0 = D / V$ on top of the residual trough remaining from all prior doses. After $n$ doses, the finite geometric series $\sum_{j=0}^{n-1} r^j = (1 - r^n)/(1 - r)$ with per-interval survival ratio $r = e^{-K \tau} = 2^{-\tau / T_{1/2}}$ converges as $n \to \infty$ to the **Steady-State Accumulation Factor** $R_{\text{acc}}$, determining the **Steady-State Peak** ($C_{\text{ss,max}}$), **Steady-State Trough** ($C_{\text{ss,min}}$), and **Average Steady-State Concentration** ($C_{\text{ss,avg}}$, which equals $\text{AUC}_{0\to\tau} / \tau$):

$$R_{\text{acc}} = \sum_{j=0}^{\infty} e^{-j K \tau} = \frac{1}{1 - e^{-K \tau}}, \qquad C_{\text{ss,max}} = \frac{C_0}{1 - e^{-K \tau}}, \qquad C_{\text{ss,min}} = \frac{C_0 \, e^{-K \tau}}{1 - e^{-K \tau}}, \qquad C_{\text{ss,avg}} = \frac{D}{C_{\text{CL}} \cdot \tau}$$

During repeated maintenance dosing or a constant-rate infusion, plasma levels climb to $1 - 2^{-n}$ of steady state: $50\%$ after $1\,T_{1/2}$, $75\%$ after $2\,T_{1/2}$, $87.5\%$ after $3\,T_{1/2}$, $93.75\%$ after $4\,T_{1/2}$, and $96.875\%$ (clinical steady state) after **$5\,T_{1/2}$** ($5 \times 6.0 = 30.0\text{ hours}$). For our $D = 500\text{ mg}$ regimen given every $\tau = 12.0\text{ hr}$ ($2.0$ half-lives, so $e^{-K\tau} = 0.25$), the accumulation factor is $R_{\text{acc}} = 1 / (1 - 0.25) = \mathbf{1.3333}$, stabilizing at $C_{\text{ss,max}} = 20.00 \times 1.3333 = \mathbf{26.67\text{ mg/L}}$ and $C_{\text{ss,min}} = 26.67 \times 0.25 = \mathbf{6.67\text{ mg/L}}$.

---

## Serum Electroneutrality, Pulmonary Gas Exchange, and Oxygen Transport

Beyond drug kinetics, critical-care physiology rests on four conservation and equilibrium laws mapped directly to the **SC-80** keypad: serum electroneutrality ({{key:AG}}), macromolecular and osmotic ion corrections ({{key:Ca²⁺}}, {{key:Na⁺}}, {{key:OSM}}), alveolar-arterial gas exchange and cardiac repolarization ({{key:ABG}}, {{key:QTc}}), and compressed-gas cylinder depletion ({{key:O₂}}).

### Anion Gap ({{key:AG}}), Corrected Calcium ({{key:Ca²⁺}}), and Hyperglycemic Sodium ({{key:Na⁺}})

Subtracting measured extracellular anions ($[\text{Cl}^-] + [\text{HCO}_3^-]$) from sodium ($[\text{Na}^+]$) defines the **Serum Anion Gap** ({{key:AG}}, normally $8\text{–}12\text{ mEq/L}$), which James Figge, Thomas Fenichel, and Vladimir Jabor (1998) corrected for hypoalbuminemia by adding $2.5\text{ mEq/L}$ per $1.0\text{ g/dL}$ albumin deficit below $4.0\text{ g/dL}$, alongside Albert Winter's (1967) respiratory compensation law:

$$\text{AG} = \left[\text{Na}^+\right] - \left(\left[\text{Cl}^-\right] + \left[\text{HCO}_3^-\right]\right), \qquad \text{AG}_{\text{corr}} = \text{AG} + 2.5\left(4.0 - \text{Alb}\right), \qquad P_a\text{CO}_2 = 1.5\left[\text{HCO}_3^-\right] + 8 \pm 2$$

![Serum electrolyte Gamblegram illustrating macroscopic cation-anion electroneutrality and the unmeasured Anion Gap (AGAP).](../assets/diagrams/domains/diagram_ch08_serum_gamblegram.png)

Simultaneously, Robert Payne's (1973) **Albumin-Corrected Calcium** ({{key:Ca²⁺}}) restores protein-bound calcium in hypoalbuminemia, while Marvin Katz's (1973) **Hyperglycemic Sodium Correction** ({{key:Na⁺}}) accounts for osmotic water translocated from the intracellular space by elevated extracellular glucose ($\text{Glc}$, in $\text{mg/dL}$), and {{key:OSM}} evaluates effective serum osmolality ($2[\text{Na}^+] + \text{Glc}/18$):

$$\text{Ca}_{\text{corr}} = \text{Ca}_{\text{meas}} + 0.8\left(4.0 - \text{Alb}\right), \qquad \text{Na}_{\text{corr}} = \text{Na}_{\text{meas}} + 0.016\left(\text{Glc} - 100\right)$$

For our ICU patient ($\text{Na}^+ = 140$, $\text{Cl}^- = 102$, $\text{HCO}_3^- = 14\text{ mEq/L}$, $\text{Ca}_{\text{meas}} = 7.6\text{ mg/dL}$, $\text{Alb} = 2.0\text{ g/dL}$, and $\text{Glc} = 350\text{ mg/dL}$), the uncorrected anion gap ({{key:AG}}) is $\text{AG} = 140 - 116 = \mathbf{24.0\text{ mEq/L}}$ and the albumin-corrected gap is $\text{AG}_{\text{corr}} = 24.0 + 2.5(2.0) = \mathbf{29.0\text{ mEq/L}}$; Payne's calcium ({{key:Ca²⁺}}) is $\text{Ca}_{\text{corr}} = 7.6 + 0.8(2.0) = \mathbf{9.20\text{ mg/dL}}$. And Katz's corrected sodium ({{key:Na⁺}}) is $\text{Na}_{\text{corr}} = 140 + 0.016(250) = \mathbf{144.0\text{ mEq/L}}$.

### Arterial Blood Gas Oxygenation ({{key:ABG}}), Bazett {{key:QTc}}, and Transport Oxygen ({{key:O₂}})

In mechanical ventilation and ARDS staging, {{key:ABG}} computes the **Horowitz Oxygenation Index ($P_a\text{O}_2 / F_i\text{O}_2$ ratio)** from arterial oxygen tension $P_a\text{O}_2$ in Register $Y$ and inspired oxygen fraction $F_i\text{O}_2$ in Register $X$ (where $P/F < 300\text{ mmHg}$ indicates acute lung injury), while the **Alveolar Gas Equation** computes alveolar oxygen tension $P_A\text{O}_2$ at barometric pressure $P_{\text{atm}} = 760\text{ mmHg}$, $37^\circ\text{C}$ water-vapor pressure $P_{\text{H}_2\text{O}} = 47\text{ mmHg}$ ($P_{\text{atm}} - P_{\text{H}_2\text{O}} = 713\text{ mmHg}$), and respiratory quotient $R = 0.80$, and subtracts measured arterial $P_a\text{O}_2$ to obtain the **A–a Gradient** ($\Delta P_{A-a}\text{O}_2$). Alongside blood gas analysis, Henry Cuthbert Bazett's (1920) **Corrected QT Interval** ({{key:QTc}}, in $\text{ms}$) normalizes ventricular repolarization time $\text{QT}_{\text{ms}}$ to a $60\text{ bpm}$ ($RR = 1.0\text{ s}$) reference via $\sqrt{RR} = \sqrt{60 / \text{HR}}$, and the **Compressed Oxygen Cylinder Law** ({{key:O₂}}) relates remaining tank pressure $P_{\text{psi}}$ (above the $200\text{ psi}$ safe residual cushion) and cylinder conversion factor $k_{\text{tank}}$ ($0.28\text{ L/psi}$ for a portable E-cylinder; $3.14\text{ L/psi}$ for a bulk H-cylinder) to flow rate $F$ ($\text{L/min}$) and transport duration $T$ ($\text{min}$):

$$\frac{P_a\text{O}_2}{F_i\text{O}_2} = \frac{Y}{X}, \qquad \Delta P_{A-a}\text{O}_2 = \left[F_i\text{O}_2\left(713\right) - \frac{P_a\text{CO}_2}{0.8}\right] - P_a\text{O}_2, \qquad \text{QT}_c = \frac{\text{QT}_{\text{ms}}}{\sqrt{60 / \text{HR}}}, \qquad T = \frac{\left(P_{\text{psi}} - 200\right) \times 0.28}{F}$$

At $F_i\text{O}_2 = 0.40$, $P_a\text{CO}_2 = 28\text{ mmHg}$, and $P_a\text{O}_2 = 110\text{ mmHg}$, pressing `110` {{key:ENTER}} `0.40` {{key:ABG}} gives a Horowitz $P/F$ ratio of $\mathbf{275.0\text{ mmHg}}$, while alveolar oxygen is $P_A\text{O}_2 = 0.40(713) - 28/0.8 = 285.2 - 35.0 = 250.2\text{ mmHg}$, giving $\Delta P_{A-a}\text{O}_2 = 250.2 - 110 = \mathbf{140.2\text{ mmHg}}$. On the ECG monitor ($\text{QT} = 420\text{ ms}$ at $\text{HR} = 96\text{ bpm}$, so $RR = 60/96 = 0.625\text{ s}$), pressing `420` {{key:ENTER}} `96` {{key:QTc}} gives $\text{QT}_c = 420 / \sqrt{0.625} = \mathbf{531.26\text{ ms}}$ (alerting the team to pause QT-prolonging antiarrhythmics). Finally, because $T$ and $F$ are reciprocally symmetric in $T \cdot F = (P_{\text{psi}} - 200) \times 0.28$, for the $T = 70.0\text{-minute}$ helicopter transfer with an E-cylinder at $P_{\text{psi}} = 1950\text{ psi}$, pressing `1950` {{key:ENTER}} `70` {{key:O₂}} directly yields the maximum safe oxygen flow rate $F = (1950 - 200) \times 0.28 / 70.0 = 490.0 / 70.0 = \mathbf{7.00\text{ L/min}}$.

---

## Compartment Kinetics, Blood Gases, and Transport Oxygen on the Stack and in the Solver Workspace

On the **SC-80**, pharmacokinetic elimination ({{key:PK}}), acid-base and electrolyte corrections ({{key:AG}}, {{key:Ca²⁺}}, {{key:Na⁺}}, {{key:OSM}}), cardiopulmonary indices ({{key:ABG}}, {{key:QTc}}, {{key:ICU}}), and oxygen tank budgeting ({{key:O₂}}) execute both on the RPN stack and in bidirectional Equation Solver Workspaces.

| Key / Solver | Mode | Inputs / Softkeys ({{keycap:LFU0}}–{{keycap:LFU2}}) | Governing Expression |
| :--- | :--- | :--- | :--- |
| {{key:PK}} | Stack / Solver | Stack: $X = T_{1/2}$ or $K$ • Solver: {{keycap:T}} {{keycap:V}} {{keycap:C}} | Stack: $K = \ln(2) / T_{1/2} \iff T_{1/2} = \ln(2) / K$; Solver: $T_{1/2} = 0.693147 \cdot V / C_{\text{CL}}$ |
| {{key:AG}} / {{key:Ca²⁺}} / {{key:Na⁺}} | Immediate Stack | {{key:AG}}: $Y = \text{Na}^+, X = \text{Cl}^- + \text{HCO}_3^-$ • {{key:Ca²⁺}}: $Y = \text{Ca}, X = \text{Alb}$ • {{key:Na⁺}}: $Y = \text{Na}, X = \text{Glc}$ | $\text{AG} = Y - X$; $\text{Ca}_{\text{corr}} = Y + 0.8(4 - X)$; $\text{Na}_{\text{corr}} = Y + 0.016(X - 100)$ |
| {{key:ABG}} / {{key:QTc}} | Immediate Stack | {{key:ABG}}: $Y = P_a\text{O}_2, X = F_i\text{O}_2$ • {{key:QTc}}: $Y = \text{QT}_{\text{ms}}, X = \text{HR}_{\text{bpm}}$ | Horowitz $P/F = Y / X$; Bazett $\text{QT}_c = Y / \sqrt{60/X}$ |
| {{key:O₂}} | Immediate Stack | Register $Y$: Pressure $P_{\text{psi}}$, Register $X$: Flow $F_{\text{L/min}}$ (or duration $T_{\text{min}}$) | E-cylinder $T = (P - 200) \times 0.28 / F \iff F = (P - 200) \times 0.28 / T$ |

### Immediate Stack Trace: Antibiotic Trough Decay, Electrolyte Corrections, and {{key:QTc}}

To evaluate the $500\text{ mg}$ IV bolus in $V = 25.0\text{ L}$ with $T_{1/2} = 6.0\text{ hr}$ at $T = 12.0\text{ hr}$ and at steady state ($\tau = 12.0\text{ hr}$), followed by the Figge–Fenichel Anion Gap ({{key:AG}}), Payne Corrected Calcium ({{key:Ca²⁺}}), Katz Corrected Sodium ({{key:Na⁺}}), and Bazett {{key:QTc}}, the clinician chains:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `500` {{key:ENTER}} `25` {{key:÷}} `6` {{key:PK}} | $0$ | $0$ | $20.0000$ | $0.1155$ | Peak $C_0 = 20.0\text{ mg/L}$ in $Y$; rate constant $K = \ln(2)/6 = 0.11552\text{ hr}^{-1}$ in $X$ |
| `12` {{key:×}} {{key:+/-}} {{key:eˣ}} {{key:×}} `0.75` {{key:÷}} | $0$ | $0$ | $0$ | $6.6667$ | First trough $C(12) = 5.0\text{ mg/L}$ scaled by $1/(1-0.25) \to C_{\text{ss,min}} = 6.67\text{ mg/L}$ |
| `140` {{key:ENTER}} `102` {{key:ENTER}} `14` {{key:+}} {{key:AG}} `5` {{key:+}} | $6.6667$ | $6.6667$ | $6.6667$ | $29.0000$ | Uncorrected $\text{AG} = 24.0$ plus $+5.0$ albumin correction $\to \text{AG}_{\text{corr}} = 29.0\text{ mEq/L}$ |
| `7.6` {{key:ENTER}} `2.0` {{key:Ca²⁺}} | $6.6667$ | $6.6667$ | $29.0000$ | $9.2000$ | Payne Albumin-Corrected Calcium $\text{Ca}_{\text{corr}} = 7.6 + 0.8(4 - 2) = 9.20\text{ mg/dL}$ |
| `420` {{key:ENTER}} `96` {{key:QTc}} | $29$ | $29.0000$ | $9.2000$ | **$531.2627$** | Bazett corrected interval $\text{QT}_c = 420 / \sqrt{60/96} = 531.26\text{ ms}$ |

### Bidirectional Solver Workspaces ({{key:PK}} and {{key:ICU}}) and Inverse Oxygen Budgeting ({{key:O₂}})

Now see how the {{key:PK}} and {{key:ICU}} Equation Workspaces and {{key:O₂}} solve critical clinical constraints backward. First, when a patient with $V = 25.0\text{ L}$ and $T_{1/2} = 6.0\text{ hr}$ ($K = 0.11552\text{ hr}^{-1}$) has a supratherapeutic trough of $C_0 = 32.0\text{ mg/L}$, the pharmacist opens {{key:PK}} ({{key:C}} {{key:PK}}) to solve via {{key:XEQ}} for systemic clearance $C_{\text{CL}} = 2.888\text{ L/hr}$ and determines the exact hold time $T = \ln(32.0/15.0)/0.11552 = \mathbf{6.559\text{ hr}}$ required before resuming dosing. Second, before loading the patient into the helicopter for a $T = 70.0\text{-minute}$ flight with an E-cylinder at $P = 1950\text{ psi}$, the respiratory therapist evaluates `1950` {{key:ENTER}} `70` {{key:O₂}} to find the maximum safe oxygen flow rate $F = \mathbf{7.00\text{ L/min}}$, and uses the {{key:ICU}} Solver Workspace (`Q = H × S / 1000`) to solve backward for stroke volume {{keycap:S}} given cardiac output $Q = 5.28\text{ L/min}$ at heart rate $H = 96\text{ bpm}$:

| Step & Action | Line 1 Workspace Formula | Softkey Legend Bar ({{keycap:LFU0}}–{{keycap:LFU2}}) | Register X Result & Physical Meaning |
| :--- | :--- | :--- | :--- |
| {{key:C}} {{key:PK}} (open workspace) | `PK: T = .69315 × V / C` | {{keycap:T}} {{keycap:V}} {{keycap:C}} | Opens compartment pharmacokinetic workspace |
| `6` $\to$ {{keycap:T}}, `25` $\to$ {{keycap:V}}, {{key:XEQ}} $\to$ {{keycap:C}} | `C = 2.8881` | `[T=6]` `[V=25]` `[C=2.89]` | Solves backward for systemic clearance $C_{\text{CL}} = \mathbf{2.888\text{ L/hr}}$ |
| {{key:C}} `32` {{key:ENTER}} `15` {{key:÷}} {{key:LN}} `6` {{key:PK}} {{key:÷}} | *(Normal Stack)* | *(Standard Spine)* | Solves exponential decay backward for hold time $T = \mathbf{6.559\text{ hr}}$ |
| `1950` {{key:ENTER}} `70` {{key:O₂}} | *(Normal Stack)* | *(Standard Spine)* | Solves E-cylinder law for maximum safe oxygen flow rate $F = \mathbf{7.00\text{ L/min}}$ |
| {{key:C}} {{key:ICU}}, `5.28` $\to$ {{keycap:Q}}, `96` $\to$ {{keycap:H}}, {{key:XEQ}} $\to$ {{keycap:S}} | `S = 55.0000` | `[Q=5.28]` `[H=96]` `[S=55]` | Solves {{key:ICU}} (`Q = H × S / 1000`) backward for stroke volume $S = \mathbf{55.0\text{ mL/beat}}$ |

### Try It on the Stack

Reinforce your command of compartment pharmacokinetics, blood-gas homeostasis, and transport oxygen budgeting with these three clinical problems:

1. **Gentamicin Half-Life ({{key:PK}}) and Supratherapeutic Hold Time:** A septic patient has $V = 18.0\text{ L}$ and renal clearance $C_{\text{CL}} = 3.00\text{ L/hr}$. In the {{key:PK}} Solver Workspace ({{key:C}} {{key:PK}}), store `18` in {{keycap:V}} and `3` in {{keycap:C}} and press {{key:XEQ}} $\to$ {{keycap:T}} to solve for half-life $T_{1/2}$, then find the hold time required for a toxic serum concentration of $C_0 = 14.0\text{ mg/L}$ to decay to $C = 2.0\text{ mg/L}$ (`14` {{key:ENTER}} `2` {{key:÷}} {{key:LN}} `4.1589` {{key:PK}} {{key:÷}}). *(Verified results: $T_{1/2} = \mathbf{4.1589\text{ hr}}$, $K = \mathbf{0.1667\text{ hr}^{-1}}$, and $T_{\text{hold}} = \mathbf{11.676\text{ hr}}$.)*
2. **Diabetic Ketoacidosis Anion Gap ({{key:AG}}) and Hyperglycemic Sodium ({{key:Na⁺}}):** A patient in diabetic ketoacidosis presents with $[\text{Na}^+] = 131\text{ mEq/L}$, $[\text{Cl}^-] = 95\text{ mEq/L}$, $[\text{HCO}_3^-] = 8\text{ mEq/L}$, and blood glucose $\text{Glc} = 600\text{ mg/dL}$. Compute the Serum Anion Gap (`131` {{key:ENTER}} `95` {{key:ENTER}} `8` {{key:+}} {{key:AG}}) and Katz Corrected Sodium (`131` {{key:ENTER}} `600` {{key:Na⁺}}). *(Verified Register $X$ results: $\text{AG} = \mathbf{28.00\text{ mEq/L}}$ and $\text{Na}_{\text{corr}} = \mathbf{139.0\text{ mEq/L}}$.)*
3. **Blood Gas Oxygenation ({{key:ABG}}) and Transport Cylinder Reserve ({{key:O₂}}):** Evaluate the Horowitz $P/F$ oxygenation index (`85` {{key:ENTER}} `0.50` {{key:ABG}}) and A–a oxygen gradient for a ventilated patient on $F_i\text{O}_2 = 0.50$ with $P_a\text{CO}_2 = 40\text{ mmHg}$ and $P_a\text{O}_2 = 85\text{ mmHg}$ (`0.50` {{key:ENTER}} `713` {{key:×}} `40` {{key:ENTER}} `0.8` {{key:÷}} {{key:-}} `85` {{key:-}}), and compute the E-cylinder duration at $P = 1700\text{ psi}$ and $F = 10.0\text{ L/min}$ (`1700` {{key:ENTER}} `10` {{key:O₂}}). *(Verified results: $P/F = \mathbf{170.0\text{ mmHg}}$, $\Delta P_{A-a}\text{O}_2 = \mathbf{221.5\text{ mmHg}}$, and $T = \mathbf{42.00\text{ min}}$.)*

With clinical anthropometrics, vasoactive infusion titrations, and compartment pharmacokinetics established on the `SC-80`, we turn in [Unit IX: Quantitative Finance, Fixed-Income Valuation & Six Sigma Quality](09-sc95-finance-statistics.md) to our ninth and final domain instrument—the `SC-95`—where compound discounting, derivative pricing, and statistical process capability govern capital and manufacturing quality.
