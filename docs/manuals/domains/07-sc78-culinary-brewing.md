---
title: "Unit VII: Commercial Baking, Dough Thermodynamics & Brewing Science"
description: "First-principles mathematics of flour-anchored Baker's Percentages, dough mixing thermodynamics, grain mash equilibrium, wort density scales, hop isomerization, and culinary yield costing across Chapters 19–21."
---

# Unit VII: Commercial Baking, Dough Thermodynamics & Brewing Science

In domestic kitchens, recipes are traditionally recorded in volumetric scoops—two cups of flour, one cup of water, a teaspoon of salt—yet granular solids pack with variable bulk density. Depending on ambient humidity, milling particle size, and whether the grain was sifted or tamped into the measure, a standard United States cup of wheat flour ($236.6\text{ mL}$) weighs anywhere from $110\text{ g}$ to $160\text{ g}$, a $45\%$ mass variation that disrupts gluten cross-linking, yeast osmotic pressure, and charcuterie curing safety. Even after replacing volumetric scoops with gram balances, expressing a dough formula in conventional weight percentages that sum to $100\%$ ($\text{Flour } 51.49\% + \text{Water } 37.08\% + \text{Levain } 10.30\% + \text{Salt } 1.13\% = 100.00\%$) couples every ingredient together: raising water by $2\%$ to compensate for a drier winter wheat harvest forces the numerical percentages of flour, levain, and salt to shrink so the ledger still totals $100\%$. Nineteenth-century European guild and commercial bakers resolved that coupling by anchoring every ingredient mass to total flour mass fixed at $100.0\%$ ({{key:BK%}}, {{key:HYD}}, {{key:LV%}}), establishing Baker's Percentage where hydration, inoculation, and salt ratios remain independent invariants across any batch size.

Controlling biological fermentation in the bakery and brewhouse requires balancing mechanical work against sensible and latent heat. Baker's yeast (*Saccharomyces cerevisiae*) and sourdough lactic acid bacteria (*Fructilactobacillus sanfranciscensis*) roughly double their metabolic carbon-dioxide evolution for every $8^\circ\text{C}$ ($15^\circ\text{F}$) rise in dough temperature. When heavy electric spiral mixers entered twentieth-century bakeries, viscous shear between the rotating steel hook and the gluten matrix converted mechanical work into thermal energy, warming the dough during mixing. To hit a repeatable post-mix Desired Dough Temperature, bakers solve an inverse enthalpy balance ({{key:Tw}}) for the strike-water temperature—or replace part of the tap water with flake ice ({{key:ICE}}) whose $80\text{ kcal/kg}$ latent heat of fusion absorbs excess summer heat—while all-grain brewers balance the specific heat of dry malted barley against hot strike liquor ({{key:MSH}}) to land on the $64^\circ\text{C}\text{–}69^\circ\text{C}$ enzymatic saccharification rest.

Quantitative brewing science (*zymurgy*) traces its mathematical foundation to 1843 in Prague, where Bohemian chemist Carl Joseph Napoleon Balling calibrated aqueous sucrose density tables so brewers could monitor malt starch conversion and yeast attenuation with a floating hydrometer measuring Specific Gravity ({{key:▸SG}}). In 1854, Prussian civil engineer Adolf Ferdinand Wenceslaus Brix refined Balling's pycnometric tables for the beet-sugar and fermentation trades ({{key:▸Brx}}, {{key:BRX}}), and in 1900 German chemist Fritz Plato standardized the extract scale ($1^\circ\text{P} = 1\text{ g}$ sucrose per $100\text{ g}$ wort, {{key:▸°P}}) for the Imperial Normal Calibration Commission, linking the gravity drop from temperature-corrected Original Gravity ({{key:SGT}}) to Final Gravity to Alcohol by Volume ({{key:ABV}}). Nearly a century later in 1995, Oregon brewing scientist Glenn Tinseth modeled the first-order thermal isomerization kinetics of hop alpha acids (*Humulus lupulus*) across boil time and wort gravity ({{key:IBU}}). Notice the cross-domain mathematical bridge between the brewhouse and the physics laboratory: Tinseth's boil-time utilization factor $f_t(t) = (1 - e^{-0.04t})/4.15$ obeys the identical first-order exponential saturation law $1 - e^{-t/\tau}$ that governs capacitor charging across an $RC$ network in Unit III (`SC-16`), while the grain-water mash enthalpy balance ({{key:MSH}}) mirrors the first-law calorimetry equation $Q = m c \Delta T$ in Unit VI (`SC-60`).

To support commercial bakers, brewmasters, winemakers, and executive chefs without tedious algebraic inversion on the production floor, the **SC-78** integrates three architectural layers:
1. **Configurable Stack Depth ({{keycap:4-LV}}, {{keycap:8-LV}}, or {{keycap:INF}} via {{key:FLAGS}}):** Practitioners can operate in classic four-register $(X, Y, Z, T)$ RPN mode ({{keycap:4-LV}}), switch to an eight-register stack ({{keycap:8-LV}}), or enable unbounded stack depth ({{keycap:INF}}) when chaining multi-addition hop bills or multi-stage banquet cost sheets.
2. **Dual-Mode Domain Keys (Quick-Access RPN Shortcuts + Bidirectional Equation Solver Workspaces):** Pressing a domain key ({{key:BK%}}, {{key:ΣW}}, {{key:SCL}}, {{key:DIV}}, {{key:Tw}}, {{key:ICE}}, {{key:MSH}}, {{key:ABV}}, {{key:IBU}}, {{key:SRM}}, {{key:YLD}}, {{key:CST}}, {{key:PRC}}) with values on the stack executes the forward calculation immediately while reading active profile parameters such as the locked base flour weight $F$ in {{key:BK%}}. Pressing a workspace-enabled domain key ({{key:BK%}}, {{key:Tw}}, {{key:MSH}}, {{key:ABV}}, {{key:IBU}}, {{key:C₁V₁}}, {{key:CST}}) on a cleared stack (`0` in $X$ and $Y$) opens its Equation Solver Workspace, displaying the governing equation on Line 1 and binding softkeys {{keycap:LFU0}}–{{keycap:LFU4}} to its named variables so the practitioner can solve forward or backward via {{key:XEQ}} for any unknown variable—such as back-calculating required flour mass $F$ in {{key:BK%}}, or solving {{key:IBU}} backward for the exact hop mass $W$ when a new hop lot arrives with a different alpha-acid rating $A$.
3. **Utensil-Snapping Volume Converters & Live `@BK%` Recipe Ledger ({{key:▦}}):** Culinary volume keys ({{key:▸cup}}, {{key:▸pt}}, {{key:▸qt}}, {{key:▸dL}}, {{key:▸tb}}, {{key:▸tsp}}) convert fluid volumes and snap to practical kitchen fractions, while the live `@BK%` recipe ledger in {{key:▦}} tracks every ingredient's Baker's Percentage and scaled mass across the entire formula.

| Chapter | Narrative Problem | Mathematical Concepts | Faceplate & Solver Keys |
| :--- | :--- | :--- | :--- |
| **Chapter 19** | Scaling $200$ country sourdough loaves ($176.2\text{ kg}$ dough) or a constrained $85.0\text{ kg}$ mixer bowl on a July morning and tempering $9^\circ\text{C}$ spiral-mixer friction with flake ice | Flour-anchored Baker's Percentages, true pre-ferment hydration, inverse batch scaling, four-term Desired Dough Temperature balance, and latent-heat ice substitution | {{key:BK%}}, {{key:ΣW}}, {{key:SCL}}, {{key:DIV}}, {{key:Tw}}, {{key:ICE}}, {{key:HYD}}, {{key:LV%}}, {{key:▦}} |
| **Chapter 20** | Formulating mash strike liquor for a $10\text{ BBL}$ pale ale, tracking attenuation from $\text{OG } 1.056$ to $\text{FG } 1.012$, and solving hop charges for $41\text{–}42\text{ IBU}$ | First-law grain-water mash calorimetry, Balling–Brix–Plato extract polynomials, apparent attenuation, Tinseth hop isomerization kinetics, Morey color, and carbonation | {{key:MSH}}, {{key:SGT}}, {{key:BRX}}, {{key:ABV}}, {{key:IBU}}, {{key:SRM}}, {{key:CO₂}}, {{key:▸Brx}}, {{key:▸SG}}, {{key:▸°P}}, {{key:▸PRF}} |
| **Chapter 21** | Trimming $45\text{ lb}$ of whole beef tenderloin across multi-stage fabrication yields, pricing an $\$8.40$ entrée at $28\%$ food cost ($72\%$ gross margin), and auditing water activity and wine $\text{SO}_2$ | Compounding multi-stage fabrication yields, hyperbolic asymmetry between Margin and Markup, Raoult water activity, and pH-dependent molecular $\text{SO}_2$ equilibrium | {{key:YLD}}, {{key:CST}}, {{key:PRC}}, {{key:Aw}}, {{key:SO₂}}, {{key:▸cup}}, {{key:▸pt}}, {{key:▸qt}}, {{key:▸dL}}, {{key:▸tb}}, {{key:▸tsp}} |

---

# Chapter 19: Scaling Two Hundred Country Loaves on a Hot July Morning

At 4:30 a.m. on a humid July morning, the ambient air inside a stone-hearth wholesale bakery already stands at $R = 28.0^\circ\text{C}$, and the organic bread flour stored in the mezzanine silos measures $F = 26.0^\circ\text{C}$. The head baker must mix enough naturally leavened country sourdough to divide $N = 200$ loaves scaled at $W = 881\text{ g}$ ($0.881\text{ kg}$) each—a total deck-oven batch of $T = 176.2\text{ kg}$ ($176{,}200\text{ g}$) of finished dough ({{key:DIV}}, {{key:SCL}}). The bakery's master formula specifies $72.0\%$ water ({{key:HYD}}), $20.0\%$ mature liquid levain ({{key:LV%}}, maintained at $100\%$ internal hydration), and $2.2\%$ sea salt ({{key:SAL}}) anchored to $100.0\%$ mixer flour ({{key:BK%}}). Simultaneously, the pastry baker on the adjacent bench has a smaller spiral mixer whose removable stainless bowl has a maximum mechanical dough capacity of $T = 85.0\text{ kg}$ and needs to know the exact anchor flour mass $F$ required to fill that bowl to capacity when a seeded bâtard formula sums to $P = 179.2\%$ ({{key:BK%}}, {{key:ΣW}}, {{key:SCL}}).

Scaling the ingredient masses solves only the gravimetric half of the morning's problem. Fifteen minutes of first- and second-speed kneading in the heavy spiral mixer injects $M = 9.0^\circ\text{C}$ of mechanical friction heat into the gluten network. If the baker draws municipal tap water at $21.0^\circ\text{C}$ straight from the wall hose, the dough will leave the mixer above $30^\circ\text{C}$: homofermentative and heterofermentative lactobacilli will race ahead of yeast fermentation, proteolytic enzymes will slacken the gluten matrix, and the shaped boules will puddle flat on the loader peels before reaching the steam-injected hearth decks.

To arrest runaway fermentation and hold the post-mix Desired Dough Temperature at an exact $D = 24.0^\circ\text{C}$, the baker must treat the spiral mixer as a thermodynamic calorimeter ({{key:Tw}}). First, the sensible heat of the room air, the warm silo flour, and the mechanical friction of the spiral hook dictate how cold the theoretical strike water $W$ must be. Because that required strike temperature ($9.0^\circ\text{C}$) falls well below the $21.0^\circ\text{C}$ municipal tap supply, the baker then replaces a calculated fraction of the recipe's liquid water with sub-zero flake ice ({{key:ICE}}), letting the latent heat of melting ice absorb the summer heat load during the first three minutes of incorporation.

---

## Flour-Anchored Baker's Percentages and Pre-Ferment Hydration

Commercial dough formulation rests on decoupling ingredient adjustments from one another through a single invariant mass reference. By anchoring every solid and liquid component to total flour weight rather than total batch weight, a baker can modify hydration for a thirsty spring-wheat harvest or adjust salt for ambient humidity while leaving every other ratio in the formula unchanged.

### Decoupling Ingredient Ratios Through the Flour Anchor and Total Batch Scaling

In the **Baker's Percentage** ({{key:BK%}}) coordinate system, the combined mass of all milled grain flours introduced into the mixer—high-protein bread flour, stoneground whole wheat, rye, or Khorasan—is defined as the reference flour mass $F$ and assigned $100.0\%$:

$$F = \sum_{k=1}^{m} F_k \equiv 100.0\%, \qquad P_i = \left(\frac{I_i}{F}\right) \times 100, \qquad I_i = F \times \left(\frac{P_i}{100}\right)$$

In these expressions, $P_i$ is the Baker's Percentage ({{key:BK%}}) of the $i$-th ingredient of mass $I_i$ (in grams or kilograms) relative to the anchor flour mass $F$.

![Comparison of coupled total-weight percentages (sum = 100%) versus flour-anchored Baker's Percentages (FLR = 100%).](../assets/diagrams/domains/diagram_ch07_bakers_percentage.png)

Summing all individual Baker's Percentages including the $100.0\%$ flour anchor defines the **Total Formula Percentage** $P = 100.0 + \sum_i P_i$. On the **SC-78**, entering the reference flour mass $F$ in Register $Y$ and the first ingredient mass $I_1$ in Register $X$ and pressing {{key:BK%}} locks $F$ as the active base flour weight, logs the ingredient into the live `@BK%` recipe ledger in {{key:▦}}, and returns $P_1 = (I_1 / F) \times 100$. Subsequent presses of `I_k` {{key:BK%}} log each remaining ingredient against the locked flour anchor $F$. Pressing {{key:ΣW}} recalls the cumulative dough batch weight $T = F + \sum_i I_i$ from the `@BK%` ledger, pressing {{key:SCL}} scales the entire `@BK%` ledger to a new target batch weight $T_{\text{target}}$ (or by a multiplier factor), and pressing {{key:DIV}} governs the **Dough Divider Scaling Law** linking total batch mass $T$, loaf count $N$, and unit portion weight $W$:

$$T = \frac{F \times P}{100} \iff F = \frac{100 \times T}{P}, \qquad W = \frac{T}{N} \iff N = \frac{T}{W}$$

Furthermore, opening the {{key:BK%}} Equation Solver Workspace (`P = (I / F) × 100`) binds softkeys {{keycap:P}}, {{keycap:I}}, and {{keycap:F}} so the baker can solve **backward** via {{key:XEQ}} for the exact flour mass $F$ required to yield a total batch mass $I = T$ when the total formula percentage is $P$.

In the country sourdough formula on our July production sheet, mixer flour ($100.0\%$), water ($72.0\%$), mature levain ($20.0\%$), and sea salt ($2.2\%$) sum to a Total Formula Percentage of $P = 100.0 + 72.0 + 20.0 + 2.2 = 194.2\%$. To produce $N = 200$ loaves at $W = 0.881\text{ kg}$ each ({{key:DIV}}), the required total dough batch is $T = 200 \times 0.881 = \mathbf{176.20\text{ kg}}$. Scaling the ledger via {{key:SCL}} (or solving the {{key:BK%}} relation backward for the anchor flour mass) yields $F = (100 \times 176.20) / 194.2 = \mathbf{90.7312\text{ kg}}$. Scaling each percentage against $F = 90.7312\text{ kg}$ produces $I_{\text{water}} = 90.7312 \times 0.72 = \mathbf{65.3265\text{ kg}}$ of water, $I_{\text{levain}} = 90.7312 \times 0.20 = \mathbf{18.1462\text{ kg}}$ of mature levain, and $I_{\text{salt}} = 90.7312 \times 0.022 = \mathbf{1.9961\text{ kg}}$ of sea salt, which sum to $\mathbf{176.200\text{ kg}}$ of mixed dough. Meanwhile, for the adjacent spiral mixer capped at $T = 85.0\text{ kg}$ running the seeded bâtard formula ($P = 179.2\%$), solving {{key:BK%}} backward for {{keycap:F}} gives $F = (100 \times 85.0) / 179.2 = \mathbf{47.4330\text{ kg}}$ of flour.

### Decomposing Pre-Ferment Mass and True Overall Hydration

Notice why bakers distinguish between **Mixer Formula Hydration** ($72.0\%$) and **True Overall Dough Hydration** ($\text{HYDR}_{\text{true}}$, evaluated via {{key:HYD}} or {{key:BK%}}). When a formula incorporates a pre-ferment of mass $W_{\text{pre}}$—such as a liquid levain ({{key:LV%}}, {{key:LEV}}), a $100\%$ poolish, or a stiff $55\%$ Italian biga—maintained at its own internal hydration percentage $H_{\text{pre}}$, that pre-ferment already carries pre-hydrated flour $W_{\text{pre,flour}}$ and water $W_{\text{pre,water}}$ into the mixing bowl:

$$W_{\text{pre,flour}} = \frac{W_{\text{pre}}}{1 + \left(H_{\text{pre}} / 100\right)}, \qquad W_{\text{pre,water}} = W_{\text{pre}} - W_{\text{pre,flour}}, \qquad \text{HYDR}_{\text{true}} = \left(\frac{W_{\text{water}} + W_{\text{pre,water}}}{W_{\text{flour}} + W_{\text{pre,flour}}}\right) \times 100$$

Here $W_{\text{pre,flour}}$ and $W_{\text{pre,water}}$ partition the pre-ferment mass $W_{\text{pre}}$, and $\text{HYDR}_{\text{true}}$ expresses the combined water from both the main mix and the pre-ferment as a percentage of total combined grain flour $(W_{\text{flour}} + W_{\text{pre,flour}})$.

In the $176.2\text{ kg}$ batch above, the $W_{\text{levain}} = 18.1462\text{ kg}$ of liquid levain built at $H_{\text{pre}} = 100.0\%$ hydration contains equal masses of fermented flour and water: $W_{\text{pre,flour}} = 18.1462 / 2 = \mathbf{9.0731\text{ kg}}$ and $W_{\text{pre,water}} = \mathbf{9.0731\text{ kg}}$. Adding those pre-fermented components to the main mixer additions reveals a combined grain flour mass of $90.7312 + 9.0731 = \mathbf{99.8043\text{ kg}}$ and a combined water mass of $65.3265 + 9.0731 = \mathbf{74.3996\text{ kg}}$, giving a True Overall Dough Hydration ({{key:HYD}}) of $\text{HYDR}_{\text{true}} = (74.3996 / 99.8043) \times 100 = \mathbf{74.545\%}$ ($\frac{72 + 10}{100 + 10} = \frac{82}{110} \approx 74.55\%$).

---

## Dough Mixing Thermodynamics and Latent-Heat Ice Substitution

Once the dry and liquid masses are weighed on the bench platform scale, the baker must control the thermal state of the dough leaving the spiral mixer. Because flour and ambient air temperatures cannot be altered rapidly on the production floor, water temperature serves as the bakery's primary thermal control actuator.

### The Four-Variable Desired Dough Temperature Balance (`Tw`)

To maintain a repeatable four-hour bulk fermentation schedule, mixed sourdough must exit the bowl at a target **Desired Dough Temperature** ($D$, typically $24.0^\circ\text{C}$ for country hearth loaves). Under the commercial Three-Factor Rule ({{key:Tw}}), the three thermal reservoirs that govern final dough temperature—ambient bakery room air ($R$), stored flour ($F$), and strike water ($W$)—average together alongside the mechanical temperature rise $M$ generated by viscous shear in the mixer bowl:

$$W = 3 D - R - F - M \iff M = 3 D_{\text{actual}} - R - F - W$$

In this five-variable balance (`W = 3×D - R - F - M`), all temperatures are expressed in degrees Celsius ($^\circ\text{C}$) or degrees Fahrenheit ($^\circ\text{F}$). In forward production mode, the baker knows $D, R, F,$ and $M$ and solves for the required strike-water temperature $W$. Conversely, when commissioning a new spiral mixer or testing a stiffer bagel dough, the baker runs an instrumentation batch with measured room ($R$), flour ($F$), strike water ($W$), and post-mix dough temperature ($D_{\text{actual}}$) and solves the exact same {{key:Tw}} workspace **backward** via {{key:XEQ}} for {{keycap:M}} to calibrate the mixer's mechanical friction factor.

![Three-factor Desired Dough Temperature (DDT) thermal balance and latent-heat ice substitution (IC%).](../assets/diagrams/domains/diagram_ch07_dough_thermal_balance.png)

On our July morning, the baker targets $D = 24.0^\circ\text{C}$ while facing a room temperature of $R = 28.0^\circ\text{C}$, a flour temperature of $F = 26.0^\circ\text{C}$, and a spiral-mixer friction factor of $M = 9.0^\circ\text{C}$. Evaluating {{key:Tw}} yields a required strike-water temperature of $W = 3(24.0) - 28.0 - 26.0 - 9.0 = 72.0 - 63.0 = \mathbf{9.0^\circ\text{C}}$.

### Latent Heat of Fusion and Flake-Ice Weight Calculation (`ICE`)

When the required strike-water temperature $T_{\text{target}} = W$ falls below the temperature of municipal tap water ($T_{\text{tap}} = 21.0^\circ\text{C}$) and the bakery lacks a refrigerated water chiller, the baker substitutes crushed or flake ice ({{key:ICE}}) for part of the liquid water mass $W_{\text{water}}$. Liquid water has a specific heat capacity of $c_w = 1.0\text{ kcal/(kg}\cdot{^\circ\text{C})}$, whereas solid ice at $0^\circ\text{C}$ absorbs a latent heat of fusion of $L_f = 79.72 \approx 80.0\text{ kcal/kg}$ solely to transition from crystalline solid at $0^\circ\text{C}$ into liquid water at $0^\circ\text{C}$. Dividing the sensible cooling deficit $W_{\text{water}} c_w (T_{\text{tap}} - W)$ by the $80\text{ kcal/kg}$ latent heat constant ({{key:ICE}}) determines the required flake-ice mass $W_{\text{ice}}$ and remaining tap-water mass $W_{\text{liquid}}$:

$$W_{\text{ice}} = \frac{W_{\text{water}} \cdot \left(T_{\text{tap}} - W\right)}{80}, \qquad W_{\text{liquid}} = W_{\text{water}} - W_{\text{ice}}$$

Applying {{key:ICE}} to our $W_{\text{water}} = 65.3265\text{ kg}$ of mixer water with tap water at $T_{\text{tap}} = 21.0^\circ\text{C}$ and target strike temperature $W = 9.0^\circ\text{C}$ ($\Delta T = 21.0 - 9.0 = 12.0^\circ\text{C}$ in Register $X$) gives $W_{\text{ice}} = 65.3265 \times (12.0 / 80) = 65.3265 \times 0.15 = \mathbf{9.7990\text{ kg}}$ of flake ice and $W_{\text{liquid}} = 65.3265 - 9.7990 = \mathbf{55.5275\text{ kg}}$ of $21.0^\circ\text{C}$ tap water.

---

## Dough Scaling and Thermal Balancing on the Stack and in the Solver Workspace

On the **SC-78**, entering the base flour weight in Register $Y$ and the first ingredient weight in Register $X$ before pressing {{key:BK%}} locks the base flour weight $F$ and activates the live `@BK%` recipe ledger in {{key:▦}}. Subsequent presses of {{key:BK%}} compute each ingredient's Baker's Percentage and append it to the ledger, while {{key:ΣW}}, {{key:SCL}}, {{key:DIV}}, {{key:Tw}}, and {{key:ICE}} handle batch scaling, portion dividing, and thermal balancing.

| Key / Solver | Mode | Inputs / Softkeys ({{keycap:LFU0}}–{{keycap:LFU4}}) | Governing Expression |
| :--- | :--- | :--- | :--- |
| {{key:BK%}} | Stack / Solver | Stack: $Y = F, X = I_1$ (then $X = I_k$) • Solver: {{keycap:P}} {{keycap:I}} {{keycap:F}} | $P = (I / F) \times 100$ (locks $F$ and logs each ingredient row to `@BK%` in {{key:▦}}) |
| {{key:ΣW}} | Immediate Ledger | Stack: recalls cumulative batch dough weight $T$ from `@BK%` | $T = F + \sum I_k = F \times P / 100$ |
| {{key:SCL}} | Immediate Ledger | Register $X$: Target dough mass $T_{\text{target}}$ (or multiplier factor) | Scales active flour $F$ and all `@BK%` rows in {{key:▦}} by $T_{\text{target}} / T$ |
| {{key:DIV}} | Immediate Stack | Register $Y$: Total dough mass $T$, Register $X$: Count $N$ (or unit mass $W$) | $W = T / N \iff N = T / W$ |
| {{key:Tw}} | Stack / Solver | Stack: $Y = D, X = T_{\text{avg}}$ • Solver: {{keycap:W}} {{keycap:D}} {{keycap:R}} {{keycap:F}} {{keycap:M}} | $W = 3 D - R - F - M$ (Strike Water / Mixer Friction Solver) |
| {{key:ICE}} | Immediate Stack | Register $Y$: Water mass $W_{\text{water}}$, Register $X$: Cooling $\Delta T = T_{\text{tap}} - W$ | $W_{\text{ice}} = W_{\text{water}} \cdot (\Delta T / 80)$ ($80\text{ kcal/kg}$ latent heat of fusion) |

### Immediate Stack Trace: Building and Scaling the `@BK%` Recipe Ledger

To build the country sourdough ledger from a $1000\text{ g}$ test formula (`720 g` water, `200 g` levain, `22 g` salt), recall the cumulative test-batch dough weight with {{key:ΣW}}, scale the entire recipe to $200$ loaves at $0.881\text{ kg}$ ($176.2\text{ kg}$ total dough) with {{key:SCL}}, and compute the flake-ice weight for $W = 9.0^\circ\text{C}$ strike water with {{key:ICE}}, the baker chains:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1000` {{key:ENTER}} `720` {{key:BK%}} | $0$ | $0$ | $0$ | $72.0000$ | Lock base flour $F = 1000\text{ g}$ and log water ($72.0\%$) into `@BK%` ledger in {{key:▦}} |
| `200` {{key:BK%}} `22` {{key:BK%}} | $0$ | $72.0000$ | $20.0000$ | $2.2000$ | Log levain ($20.0\%$) and sea salt ($2.2\%$) into `@BK%` (`P = 194.2%`) |
| {{key:ΣW}} | $72.0000$ | $20.0000$ | $2.2000$ | $1942.000$ | Recall cumulative test-batch dough mass $T = 1942\text{ g}$ ($194.2\%$) from `@BK%` |
| `176.2` {{key:x⇄y}} {{key:÷}} `1000` {{key:×}} | $0$ | $72.0000$ | $20.0000$ | $90.7312$ | Scale anchor flour to $176.2\text{ kg}$ batch: $F = 90.7312\text{ kg}$ |
| `0.72` {{key:×}} `12` {{key:ICE}} | $0$ | $72.0000$ | $20.0000$ | **$9.7990$** | Compute mixer water ($65.3265\text{ kg}$) and flake ice $W_{\text{ice}} = 9.7990\text{ kg}$ at $\Delta T = 12^\circ\text{C}$ |

### Bidirectional Solver Workspaces (`BK%` and `Tw`): Solving Backward for Flour Capacity and Strike Water

Now see how the Equation Workspaces eliminate manual algebra when working backward from physical equipment constraints. First, on a cleared stack ({{key:C}}), the pastry baker opens {{key:BK%}} (`P = I / F × 100`) to find the exact flour weight $F$ that fills an $85.0\text{ kg}$ mixer bowl ($I = 85.0\text{ kg}$) when the seeded bâtard formula totals $P = 179.2\%$, and uses {{key:DIV}} (`85` {{key:ENTER}} `0.85` {{key:DIV}}) to find how many $W = 0.850\text{ kg}$ loaves that $85.0\text{ kg}$ bowl yields. Second, the hearth baker opens {{key:Tw}} (`W = 3×D - R - F - M`) to solve forward for the $9.0^\circ\text{C}$ strike water temperature and backward for the mixer friction factor $M$ when a stiffer rye dough exits the mixer at $D = 25.5^\circ\text{C}$:

| Step & Action | Line 1 Workspace Formula | Softkey Legend Bar ({{keycap:LFU0}}–{{keycap:LFU4}}) | Register X Result & Physical Meaning |
| :--- | :--- | :--- | :--- |
| {{key:C}} {{key:BK%}} (open workspace) | `BK%: P = I / F × 100` | {{keycap:P}} {{keycap:I}} {{keycap:F}} | Opens Baker's Percentage / batch scaling workspace |
| `85` $\to$ {{keycap:I}}, `179.2` $\to$ {{keycap:P}}, {{key:XEQ}} $\to$ {{keycap:F}} | `F = 47.4330` | `[P=179.2]` `[I=85]` `[F=47.43]` | Solves backward for required flour $F = \mathbf{47.433\text{ kg}}$ to fill $85\text{ kg}$ mixer |
| {{key:C}} `85` {{key:ENTER}} `0.85` {{key:DIV}} | *(Normal Stack)* | *(Standard Spine)* | Divides $85.0\text{ kg}$ batch by $0.85\text{ kg}$ portion: $N = \mathbf{100.00\text{ loaves}}$ |
| {{key:C}} {{key:Tw}} (open workspace) | `TW: W = 3×D - R - F - M` | {{keycap:W}} {{keycap:D}} {{keycap:R}} {{keycap:F}} {{keycap:M}} | Opens five-variable dough thermodynamics workspace |
| `24` $\to$ {{keycap:D}}, `28` $\to$ {{keycap:R}}, `26` $\to$ {{keycap:F}}, `9` $\to$ {{keycap:M}} | `TW: W = 3×D - R - F - M` | {{keycap:W}} `[D=24]` `[R=28]` `[F=26]` `[M=9]` | Stores target $D=24^\circ\text{C}$, room $28^\circ\text{C}$, flour $26^\circ\text{C}$, friction $9^\circ\text{C}$ |
| {{key:XEQ}} $\to$ {{keycap:W}} | `W = 9.0000` | `[W=9]` `[D=24]` `[R=28]` `[F=26]` `[M=9]` | Solves forward for required strike-water temperature $W = \mathbf{9.0^\circ\text{C}}$ |
| `25.5` $\to$ {{keycap:D}}, `12` $\to$ {{keycap:W}}, {{key:XEQ}} $\to$ {{keycap:M}} | `M = 10.5000` | `[W=12]` `[D=25.5]` `[R=28]` `[F=26]` `[M=10.5]` | Solves backward for empirical mixer friction rise $M = \mathbf{10.5^\circ\text{C}}$ |

### Try It on the Stack

Practice scaling artisan dough formulas and balancing summer mixer heat across these three bakery problems:

1. **Ciabatta High-Hydration Inverse Scaling ({{key:BK%}} Solver):** A hearth ciabatta formula uses $100\%$ bread flour, $82\%$ water, $15\%$ poolish, $2.5\%$ olive oil, and $2.2\%$ salt ($P = 201.7\%$). Open the {{key:BK%}} Solver Workspace ({{key:C}} {{key:BK%}}, `P = I / F × 100`), store `80.68` $\to$ {{keycap:I}} and `201.7` $\to$ {{keycap:P}}, and press {{key:XEQ}} $\to$ {{keycap:F}} to solve backward for the flour weight needed to mix $80.68\text{ kg}$ of total dough, then multiply by $0.82$ to find the water weight. *(Verified results: $F = \mathbf{40.00\text{ kg}}$ and $I_{\text{water}} = \mathbf{32.80\text{ kg}}$.)*
2. **True Hydration with a Stiff Biga ({{key:HYD}} / {{key:BK%}}):** A panettone primo impasto combines $1{,}000\text{ g}$ main flour and $620\text{ g}$ water with $300\text{ g}$ of stiff biga maintained at $50\%$ internal hydration ($200\text{ g}$ flour and $100\text{ g}$ water). Compute True Overall Dough Hydration via `1000` {{key:ENTER}} `200` {{key:+}} `620` {{key:ENTER}} `100` {{key:+}} {{key:HYD}}. *(Verified Register $X$ result: $\text{HYDR}_{\text{true}} = \mathbf{60.00\%}$.)*
3. **Bagel Mixer Friction and Flake-Ice Cooling ({{key:Tw}} & {{key:ICE}}):** A New York bagel dough targets $D = 22.0^\circ\text{C}$ when $R = 27.0^\circ\text{C}$, $F = 25.0^\circ\text{C}$, and high-gluten spiral friction is $M = 12.0^\circ\text{C}$. In the {{key:Tw}} Solver Workspace, solve via {{key:XEQ}} for strike water {{keycap:W}}, then for $24.0\text{ kg}$ of recipe water and tap water at $20.0^\circ\text{C}$ ($\Delta T = 18.0^\circ\text{C}$), compute the flake-ice weight (`24` {{key:ENTER}} `18` {{key:ICE}}). *(Verified results: $W = \mathbf{2.0^\circ\text{C}}$ and $W_{\text{ice}} = \mathbf{5.40\text{ kg}}$.)*

Having balanced flour-anchored dough proportions and spiral-mixer thermodynamics on the bakery floor, we step across the courtyard in Chapter 20 into the brewhouse—where grain-water calorimetry, hydrometer extract density, and hop alpha-acid isomerization govern a ten-barrel pale ale.

---

# Chapter 20: Hitting Original Gravity and Bitterness in the Brewhouse Kettle

Next door to the bakery, the head brewer is mashing in a $10\text{ BBL}$ ($310\text{ U.S. gallon}$, or $1{,}173.5\text{ L}$) batch of flagship West Coast pale ale. Seven hundred pounds of crushed two-row malted barley sits in the overhead grist case at an ambient grain-room temperature of $G = 19.0^\circ\text{C}$. When the slide gate opens and the dry grist meets the hot liquor flowing through the mash hydrator at a standard thickness of $R = 1.5\text{ qt/lb}$, the combined mash must equilibrate at a single-infusion saccharification rest of $T = 66.5^\circ\text{C}$ ({{key:MSH}})—warm enough for $\alpha$-amylase to dextrinize long amylopectin chains, yet cool enough to preserve $\beta$-amylase so the finished beer remains crisp and fermentable.

Ninety minutes later, after lautering the sweet wort into the steam-jacketed kettle, the brewer draws a sample to verify extract concentration before starting the boil. An optical refractometer reading a single drop of wort reports $13.80\text{ Brix}$ ({{key:BRX}}, {{key:▸SG}}, {{key:▸Brx}}, {{key:▸°P}}). Once the brewer confirms a $20.0^\circ\text{C}$ temperature-corrected **Original Gravity** of $O = 1.0560$ ({{key:SGT}}) and pitches *Saccharomyces cerevisiae* (Chico ale strain), ten days of active fermentation will lower the density to a **Final Gravity** of $F = 1.0120$, fixing both the apparent attenuation and the finished **Alcohol by Volume** ({{key:ABV}}, {{key:▸PRF}}).

During the sixty-minute kettle boil, the brewer must hit a specification of $41.0\text{ IBU}$ ({{key:IBU}}) using a $60\text{-minute}$ bittering charge of $52.0\text{ oz}$ of Magnum pellets ($12.0\%$ alpha acids) and a $15\text{-minute}$ flavor charge of $30.0\text{ oz}$ of Cascade pellets ($10.0\%$ alpha acids)—and then solve the {{key:IBU}} Equation Workspace **backward** via {{key:XEQ}} for the exact hop charge mass $W$ in ounces and grams required to hit $42.0\text{ IBU}$ on the next brew when a fresh hop lot arrives from Yakima with an analytical alpha-acid percentage of $A = 11.8\%$.

---

## Mash Strike-Water Calorimetry and Wort Gravity Scales

All-grain brewing begins with an adiabatic enthalpy balance in the mash tun and continues by tracking the mass fraction of dissolved maltose, maltotriose, and dextrins across lautering and fermentation.

### First-Law Enthalpy Balance in the Mash Tun (`MSH`)

When dry crushed malt of mass $W_{\text{grain}}$ and specific heat capacity $c_g \approx 0.40\text{ kcal/(kg}\cdot{^\circ\text{C})}$ (or $0.40\text{ BTU/(lb}\cdot{^\circ\text{F})}$) at initial grain temperature $G$ mixes with hot strike water of mass $W_{\text{water}}$ and specific heat $c_w = 1.00\text{ kcal/(kg}\cdot{^\circ\text{C})}$ at **Mash Strike Temperature** ({{key:MSH}}, $S$), conservation of thermal energy requires the sensible heat lost by the cooling strike liquor to match the sensible heat gained by the warming grain bed at equilibrium rest temperature $T$:

$$W_{\text{water}} c_w \left(S - T\right) = W_{\text{grain}} c_g \left(T - G\right) \implies S = \frac{0.2}{R}\left(T - G\right) + T$$

In the standard American brewing convention where mash thickness $R$ is expressed in U.S. quarts of water per pound of grain ($\text{qt/lb}$), $1\text{ qt}$ of water weighs $2.085\text{ lb}$, so the thermal heat-capacity ratio $c_g / (2.085\,c_w) \approx 0.40 / 2.085 \approx 0.20$ yields the thermodynamic constant $0.2 / R$ (and when $R$ is expressed in metric $\text{L/kg}$, $0.2/R$ is replaced by $0.41/R_{\text{L/kg}}$, corresponding to an equivalent $R = 0.488 \, R_{\text{L/kg}}$).

![First-law enthalpy balance between hot strike water and dry malted grain reaching mash rest equilibrium (MSH).](../assets/diagrams/domains/diagram_ch07_mash_equilibrium.png)

For our $10\text{ BBL}$ pale ale mashed at a standard liquor-to-grist ratio of $R = 1.50\text{ qt/lb}$ with malt stored at $G = 19.0^\circ\text{C}$ and a target saccharification rest of $T = 66.5^\circ\text{C}$, the temperature differential is $T - G = 66.5 - 19.0 = 47.5^\circ\text{C}$. Multiplying by $0.2 / 1.5 = 0.13333$ gives a thermal drop of $6.333^\circ\text{C}$ during dough-in, requiring the hot liquor tank to deliver strike water at $S = 66.5 + 6.333 = \mathbf{72.833^\circ\text{C}}$.

### Extract Polynomials (`▸SG`, `▸Brx`, `▸°P`), Hydrometer Calibration (`SGT`), and Alcohol by Volume (`ABV`)

Brewers, winemakers, and distillers quantify dissolved sugar concentration using three interconvertible density scales: **Specific Gravity** ({{key:▸SG}} and {{key:BRX}}, the density ratio of wort or must to pure water at $20.0^\circ\text{C}$), **Degrees Brix** ({{key:▸Brx}}, $B$), and **Degrees Plato** ({{key:▸°P}}, grams of sucrose-equivalent extract per $100\text{ g}$ of solution). When a glass hydrometer is read in warm kettle wort at temperature $T_{^\circ\text{C}}$ rather than its $20.0^\circ\text{C}$ calibration reference, {{key:SGT}} applies thermal expansion correction ($\text{SG}_{20^\circ\text{C}} = \text{SG}_{\text{meas}} + 0.0013 \cdot (T_{^\circ\text{C}} - 20)/10$). The American Society of Brewing Chemists (ASBC) rational and cubic polynomials convert directly between extract $B$ and Specific Gravity $\text{SG}$:

$$\text{SG} = 1 + \frac{B}{258.6 - \left(\frac{B}{258.2}\right) \times 227.1}, \qquad B \approx {^\circ\text{P}} = \left(\left(182.4601 \cdot \text{SG} - 775.6821\right) \cdot \text{SG} + 1262.7794\right) \cdot \text{SG} - 669.5622$$

Once yeast ferments the wort from **Original Gravity** ($O$) down to **Final Gravity** ($F$), the fraction of gravity points consumed defines **Apparent Attenuation** ($\text{ATT}_{\%}$), and the density drop scaled by the stoichiometric ethanol-to-$\text{CO}_2$ conversion factor $131.25$ determines **Alcohol by Volume** ({{key:ABV}}, $A$) and U.S. distilled spirit proof ({{key:▸PRF}}, $\text{Proof} = 2 \times \text{ABV}_{\%}$):

$$\text{ATT}_{\%} = \left(\frac{O - F}{O - 1.000}\right) \times 100, \qquad A = \left(O - F\right) \times 131.25$$

In the $10\text{ BBL}$ brewhouse, the optical refractometer reading of $B = 13.80\text{ Brix}$ converts via {{key:▸SG}} (or {{key:BRX}}) to a calibrated Original Gravity of $O = 1 + 13.80 / (258.6 - 12.138) = \mathbf{1.0560}$. Fermenting from $O = 1.0560$ down to $F = 1.0120$ removes $44.0$ of the initial $56.0$ gravity points, yielding an Apparent Attenuation of $\text{ATT}_{\%} = (0.044 / 0.056) \times 100 = \mathbf{78.571\%}$ and a finished ethanol strength of $A = (1.0560 - 1.0120) \times 131.25 = \mathbf{5.775\%\text{ ABV}}$.

---

## Hop Alpha-Acid Isomerization, Malt Colorimetry, and Carbonation

During the kettle boil, insoluble humulones (alpha acids) inside the lupulin glands of hop cones undergo a thermal acyloin ring contraction into soluble, bitter *cis*- and *trans*-iso-alpha-acids.

### Glenn Tinseth's Gravity-Time Utilization Model (`IBU`)

One **International Bitterness Unit** ({{key:IBU}}, $I$) is defined analytically as $1.0\text{ mg}$ of isomerized alpha acids per liter of beer ($1\text{ mg/L}$). Depending on whether the brewhouse weighs hops and wort in metric units ($W_{\text{g}}$ in grams, decimal alpha-acid fraction $A \in (0, 1)$, and batch volume $V_{\text{L}}$ in liters, where $1000\text{ mg/g}$ converts grams per liter to $\text{mg/L}$) or in U.S. customary units ($W_{\text{oz}}$ in ounces, percentage alpha acid $A_{\%}$, and volume $V_{\text{gal}}$ in gallons, where $74.89 = 28{,}349.5 / (3.78541 \times 100)$), kettle bitterness $I$ and Glenn Tinseth's (1995) decimal utilization $U(t, \text{SG})$ are governed by:

$$I = \frac{W_{\text{g}} \cdot A \cdot U \cdot 1000}{V_{\text{L}}} = \frac{W_{\text{oz}} \cdot A_{\%} \cdot U \cdot 74.89}{V_{\text{gal}}}, \qquad U(t, \text{SG}) = \underbrace{\left[1.65 \times 0.000125^{\left(\text{SG} - 1\right)}\right]}_{f_G(\text{SG})} \times \underbrace{\left[\frac{1 - e^{-0.04\,t}}{4.15}\right]}_{f_t(t)}$$

Here $f_G(\text{SG})$ captures the physical inhibition of alpha-acid solubility and break-material coagulation as wort gravity $\text{SG}$ rises, while $f_t(t)$ models first-order isomerization approaching an asymptotic ceiling of $1 / 4.15 \approx 24.1\%$ as boil duration $t$ exceeds $60\text{ to }90\text{ minutes}$.

Evaluating Tinseth's equation for our $10\text{ BBL}$ ($V_{\text{gal}} = 310.0\text{ gal} = 1173.5\text{ L}$) pale ale at $\text{SG} = 1.0560$ yields a bigness factor of $f_G = 1.65 \times (0.000125)^{0.056} = \mathbf{0.9985}$. For the $t = 60\text{ min}$ Magnum addition ($W_{\text{oz}} = 52.0\text{ oz}$, $A_{\%} = 12.0\%$), $f_t(60) = (1 - e^{-2.40}) / 4.15 = 0.21910$, giving $U_{60} = 0.9985 \times 0.21910 = \mathbf{0.2188}$ ($21.88\%$) and contributing $I_{60} = (52.0 \times 12.0 \times 0.2188 \times 74.89) / 310.0 = \mathbf{32.98\text{ IBU}}$. For the $t = 15\text{ min}$ Cascade flavor addition ($W_{\text{oz}} = 30.0\text{ oz}$, $A_{\%} = 10.0\%$), $U_{15} = \mathbf{0.1086}$ ($10.86\%$), contributing $I_{15} = (30.0 \times 10.0 \times 0.1086 \times 74.89) / 310.0 = \mathbf{7.87\text{ IBU}}$, so the two additions total $I_{\text{total}} = 32.98 + 7.87 = \mathbf{40.85 \approx 41.0\text{ IBU}}$.

Conversely, suppose the brewery receives a new lot of bittering hops with alpha-acid fraction $A = 0.118$ ($A_{\%} = 11.8\%$) and wants a single $60\text{-minute}$ charge ($U = 0.2188$) to deliver $I = 42.0\text{ IBU}$ in the $V_{\text{gal}} = 310.0\text{ gal}$ ($V_{\text{L}} = 1173.5\text{ L}$) kettle. Solving the {{key:IBU}} equation backward via {{key:XEQ}} for the hop mass $W$ gives:

$$W_{\text{oz}} = \frac{I \cdot V_{\text{gal}}}{A_{\%} \cdot U \cdot 74.89} = \frac{42.0 \times 310.0}{11.8 \times 0.2188 \times 74.89} = \mathbf{67.338\text{ oz}}, \qquad W_{\text{g}} = \frac{I \cdot V_{\text{L}}}{A \cdot U \cdot 1000} = \frac{42.0 \times 1173.5}{0.118 \times 0.2188 \times 1000} = \mathbf{1908.99\text{ g}}$$

### Malt Colorimetry (`SRM`), Bright-Tank Carbonation (`CO₂`), and Coffee Extraction (`TDS`)

Alongside hop bitterness, brewers and beverage directors track Dan Morey's power-law beer color in **Standard Reference Method** ({{key:SRM}}) units from **Malt Color Units** ($\text{MCU} = \sum (W_{\text{grain,lb}} \cdot L) / V_{\text{gal}}$), bright-tank **Carbonation** ({{key:CO₂}}), and refractometric coffee **Extraction Yield** ({{key:TDS}}, $\text{EY}_{\%}$) from liquid beverage weight $W_{\text{brew}}$, **Total Dissolved Solids** ($\text{TDS}_{\%}$), and dry dose $W_{\text{dose}}$ ($18.0\text{ g}$ standard espresso dose on the stack):

$$\text{SRM} = 1.4922 \cdot \left(\text{MCU}\right)^{0.6859}, \qquad \text{EY}_{\%} = \frac{W_{\text{brew}} \cdot \text{TDS}_{\%}}{W_{\text{dose}}}$$

![Coffee extraction mass balance relating dry dose mass, beverage weight, Total Dissolved Solids (TDS), and Extraction Yield (EY%).](../assets/diagrams/domains/diagram_ch07_coffee_extraction.png)

In our $10\text{ BBL}$ ($V_{\text{gal}} = 310\text{ gal}$) pale ale mashed with $650\text{ lb}$ of two-row pale malt ($2.0^\circ\text{L}$) and $50\text{ lb}$ of Caramel $40$ malt ($40.0^\circ\text{L}$), total grain color units are $650 \times 2.0 + 50 \times 40.0 = 3300\text{ lb}\cdot{^\circ\text{L}}$, giving $\text{MCU} = 3300 / 310.0 = 10.645$ and producing a golden-copper hue of $\text{SRM} = 1.4922 \times (10.645)^{0.6859} = \mathbf{7.560\text{ SRM}}$.

---

## Brewhouse Gravity, Attenuation, and Bitterness on the Stack and in the Solver Workspace

On the **SC-78**, mash infusion thermodynamics ({{key:MSH}}), ASBC extract conversions ({{key:▸SG}}, {{key:▸Brx}}, {{key:▸°P}}, {{key:BRX}}, {{key:SGT}}), fermentation alcohol ({{key:ABV}}, {{key:▸PRF}}), hop isomerization ({{key:IBU}}), malt color ({{key:SRM}}), carbonation ({{key:CO₂}}), and coffee extraction ({{key:TDS}}) execute both as immediate two-register RPN stack operators and as multi-variable Equation Solver Workspaces ({{key:MSH}}, {{key:ABV}}, {{key:IBU}}).

| Key / Solver | Mode | Inputs / Softkeys ({{keycap:LFU0}}–{{keycap:LFU4}}) | Governing Expression |
| :--- | :--- | :--- | :--- |
| {{key:MSH}} | Stack / Solver | Stack: $Y = T, X = G$ • Solver: {{keycap:S}} `[R=1.5]` {{keycap:T}} {{keycap:G}} | $S = (0.2 / R) \cdot (T - G) + T$ ($R = 1.5\text{ qt/lb}$ default) |
| {{key:▸SG}} / {{key:▸Brx}} / {{key:▸°P}} | Immediate Stack | Register $X$: Extract $B$ ({{key:▸SG}}, {{key:BRX}}) or Specific Gravity ({{key:▸Brx}}, {{key:▸°P}}) | ASBC rational (`Brix` $\to$ `SG`) and cubic (`SG` $\to$ `Brix`/`°P`) polynomials |
| {{key:SGT}} | Immediate Stack | Register $Y$: Measured $\text{SG}$, Register $X$: Sample temp $T_{^\circ\text{C}}$ | Hydrometer thermal expansion correction $\text{SG}_{20^\circ\text{C}} = Y + 0.0013(X - 20)/10$ |
| {{key:ABV}} / {{key:▸PRF}} | Stack / Solver | Stack: $Y = O, X = F$ • Solver: {{keycap:A}} {{keycap:O}} {{keycap:F}} | $A = (O - F) \times 131.25$; {{key:▸PRF}} converts $\text{ABV}_{\%} \to 2 \times \text{ABV}_{\%}$ |
| {{key:IBU}} | Stack / Solver | Stack: $Y = W_{\text{oz}}, X = A_{\%}$ • Solver: {{keycap:I}} {{keycap:W}} {{keycap:A}} {{keycap:U}} {{keycap:V}} | $I = W \cdot A \cdot U \cdot 74.89 / V$ ($5\text{ gal}, U=0.25$ stack shortcut) |
| {{key:SRM}} / {{key:TDS}} | Immediate Stack | {{key:SRM}}: $Y = \sum(W_{\text{lb}}\cdot L), X = V_{\text{gal}}$ • {{key:TDS}}: $Y = W_{\text{brew}}, X = \text{TDS}_{\%}$ | Morey power law $\text{SRM} = 1.4922 \cdot (Y/X)^{0.6859}$; Coffee $\text{EY}_{\%} = Y \cdot X / 18$ |

### Immediate Stack Trace: Mash Strike Liquor, Refractometer Conversion, and Attenuation

Starting at the mash tun with target rest $T = 66.5^\circ\text{C}$ and grain temperature $G = 19.0^\circ\text{C}$, the brewer computes the strike-water temperature ({{key:MSH}}), converts the $13.80\text{ Brix}$ refractometer reading into calibrated Specific Gravity ({{key:▸SG}}), and evaluates Alcohol by Volume ({{key:ABV}}), Apparent Attenuation, and Morey color ({{key:SRM}}):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `66.5` {{key:ENTER}} `19` {{key:MSH}} | $0$ | $0$ | $0$ | $72.8333$ | Compute strike-water temperature $S = 72.833^\circ\text{C}$ at $R = 1.5\text{ qt/lb}$ |
| `13.8` {{key:▸SG}} | $0$ | $0$ | $72.8333$ | $1.0560$ | Convert $13.80\text{ Brix}$ wort reading to Original Gravity $O = 1.0560$ |
| {{key:ENTER}} {{key:ENTER}} `1.012` {{key:ABV}} | $72.8333$ | $1.0560$ | $1.0560$ | $5.7750$ | Duplicate $O$ and compute finished ethanol $A = 5.775\%\text{ ABV}$ at $F = 1.0120$ |
| {{key:x⇄y}} `1.012` {{key:-}} `0.056` {{key:÷}} `100` {{key:×}} | $72.8333$ | $1.0560$ | $5.7750$ | $78.5714$ | Evaluate Apparent Attenuation $\text{ATT}_{\%} = (0.044 / 0.056) \times 100 = 78.57\%$ |
| `3300` {{key:ENTER}} `310` {{key:SRM}} | $1.0560$ | $5.7750$ | $78.5714$ | **$7.5599$** | Evaluate Morey beer color $\text{SRM} = 1.4922 \times (3300/310)^{0.6859} = 7.56\text{ SRM}$ |

### Bidirectional Solver Workspaces (`MSH` and `IBU`): Solving Backward for Hop Charge Mass and Rest Temperature

When a new lot of bittering hops arrives with alpha-acid rating $A = 11.8\%$ and the brewer needs to know the exact hop mass $W$ required to hit $I = 42.0\text{ IBU}$ in the $V = 310.0\text{ gal}$ ($1173.5\text{ L}$) kettle at $60\text{-minute}$ Tinseth utilization $U = 0.2188$—or wants to check what mash rest temperature $T$ will result if thick strike liquor ($R = 1.25\text{ qt/lb}$) enters at $S = 74.0^\circ\text{C}$ into $G = 18.0^\circ\text{C}$ malt—the {{key:IBU}} and {{key:MSH}} Equation Workspaces solve both inverse problems directly via {{key:XEQ}}:

| Step & Action | Line 1 Workspace Formula | Softkey Legend Bar ({{keycap:LFU0}}–{{keycap:LFU4}}) | Register X Result & Physical Meaning |
| :--- | :--- | :--- | :--- |
| {{key:C}} {{key:IBU}} (open workspace) | `IBU: I = W×A×U×74.89/V` | {{keycap:I}} {{keycap:W}} {{keycap:A}} {{keycap:U}} {{keycap:V}} | Opens five-variable hop isomerization workspace |
| `42` $\to$ {{keycap:I}}, `11.8` $\to$ {{keycap:A}} | `IBU: I = W×A×U×74.89/V` | `[I=42]` {{keycap:W}} `[A=11.8]` {{keycap:U}} {{keycap:V}} | Stores target bitterness $I = 42.0\text{ IBU}$ and alpha acid $A = 11.8\%$ |
| `0.2188` $\to$ {{keycap:U}}, `310` $\to$ {{keycap:V}} | `IBU: I = W×A×U×74.89/V` | `[I=42]` {{keycap:W}} `[A=11.8]` `[U=.219]` `[V=310]` | Stores $60\text{-min}$ Tinseth utilization $U = 0.2188$ and volume $V = 310\text{ gal}$ |
| {{key:XEQ}} $\to$ {{keycap:W}} | `W = 67.3381` | `[I=42]` `[W=67.34]` `[A=11.8]` `[U=.219]` `[V=310]` | Solves backward for required hop charge $W = \mathbf{67.34\text{ oz}}$ ($\times 28.3495 = \mathbf{1909.0\text{ g}}$) |
| {{key:C}} {{key:MSH}} (open workspace) | `MSH: S = .2/R×(T-G)+T` | {{keycap:S}} `[R=1.5]` {{keycap:T}} {{keycap:G}} | Opens mash strike-water enthalpy workspace |
| `74` $\to$ {{keycap:S}}, `1.25` $\to$ {{keycap:R}}, `18` $\to$ {{keycap:G}}, {{key:XEQ}} $\to$ {{keycap:T}} | `T = 66.2759` | `[S=74]` `[R=1.25]` `[T=66.28]` `[G=18]` | Solves backward for equilibrium mash rest temperature $T = \mathbf{66.28^\circ\text{C}}$ |

### Try It on the Stack

Test your brewhouse stack and Solver Workspace fluency on these three zymurgy problems:

1. **Imperial Stout Mash Strike and Final Gravity Target ({{key:MSH}} & {{key:ABV}}):** A brewer mashes dark roasted grain at $G = 17.5^\circ\text{C}$ to hit a full-bodied rest of $T = 68.0^\circ\text{C}$ (`68` {{key:ENTER}} `17.5` {{key:MSH}}), then converts $22.0\text{ Brix}$ wort to Specific Gravity (`22` {{key:▸SG}}) and uses the {{key:ABV}} Solver Workspace ({{key:C}} {{key:ABV}}, `A = (O - F) × 131.25`) to solve backward via {{key:XEQ}} for the Final Gravity {{keycap:F}} required to reach $A = 9.166\%\text{ ABV}$. *(Verified results: $S = \mathbf{74.733^\circ\text{C}}$, $O = \mathbf{1.0918}$, and $F = \mathbf{1.0220}$.)*
2. **Pilot Batch Centennial Hop Bitterness and Morey Color ({{key:IBU}} & {{key:SRM}}):** In a $5.0\text{ gal}$ pilot batch ($U = 0.25$), compute kettle bitterness for $1.75\text{ oz}$ of Centennial hops at $A_{\%} = 10.5\%$ (`1.75` {{key:ENTER}} `10.5` {{key:IBU}}) and beer color in {{key:SRM}} for a $5.0\text{ gal}$ grain bill contributing $90.0\text{ lb}\cdot{^\circ\text{L}}$ (`90` {{key:ENTER}} `5` {{key:SRM}}, or $\text{MCU} = 18.0$). *(Verified Register $X$ results: $I = \mathbf{68.805\text{ IBU}}$ and $\text{SRM} = \mathbf{10.828\text{ SRM}}$.)*
3. **Inverse Hop Charge for a 15-Barrel IPA ({{key:IBU}} Solver):** A $15\text{ BBL}$ ($V = 465\text{ gal} = 1760.2\text{ L}$) West Coast IPA requires $I = 55.0\text{ IBU}$ from a single $60\text{-minute}$ Citra hop addition with $A_{\%} = 13.4\%$ ($A = 0.134$) and utilization $U = 0.225$. Solve the {{key:IBU}} Workspace backward via {{key:XEQ}} for {{keycap:W}} in ounces and convert to grams. *(Verified results: $W = \mathbf{113.065\text{ oz}} = \mathbf{3205.3\text{ g}}$.)*

From the brewhouse kettle and fermentation cellar, we move in Chapter 21 to the butcher block, the charcuterie curing room, and the executive chef's desk—where multi-stage fabrication yields, the hyperbolic geometry of margin versus markup, water activity, and sulfite equilibrium govern culinary profitability and preservation.

---

# Chapter 21: Trimming the Tenderloin and Pricing the Tasting Menu

In the butcher room of a hotel banquet kitchen, the garde-manger chef is breaking down $W_{\text{AP}} = 45.0\text{ lb}$ ($20.41\text{ kg}$) of whole vacuum-packed beef tenderloin (*psoas major*, purchased as PSMO—peeled, side muscle on) for a $120$-guest Saturday evening tasting menu. Before a single medallion can hit the porcelain plate, the raw commodity passes through a sequence of mass-reducing stages: peeling away the tough elastin silverskin membrane and detaching the fatty chain muscle on the butcher block ($80.0\%$ raw fabrication yield), followed by dry-aging and plancha searing purge ($90.0\%$ thermal cooking retention), compounding into an overall net **Edible Portion Yield** ({{key:YLD}}) of $Y_{\%} = 0.80 \times 0.90 = 72.0\%$.

The executive chef faces two coupled mathematical challenges at the butcher table. First, how many pounds and ounces of finished **Edible Portion** (`EP`) beef remain from the $45.0\text{ lb}$ delivery ($32.40\text{ lb}$, providing a $4.32\text{ oz}$ tasting-menu medallion for each of the $120$ guests), and conversely, if a wedding contract instead stipulates a full $6.0\text{ oz}$ ($0.375\text{ lb}$) cooked filet per guest ($45.0\text{ lb}$ of finished `EP` meat on the pass), how many pounds of untrimmed `AP` tenderloin must the purchasing steward order from the purveyor?

Second, because $28.0\%$ of the raw tenderloin mass disappears across fabrication and cooking, the purveyor's invoice price of $\$16.20/\text{lb}$ does not represent the true cost of the meat sitting on the plate. Dividing the invoice cost by the $0.72$ cumulative yield factor uncovers a true edible cost of $\$22.50/\text{lb}$ ($0.27\text{ lb} \times \$22.50 = \$6.075$ per tasting portion); adding $\$2.325$ for truffled pomme purée, glazed cipollini onions, and marrow bordelaise brings the plated entrée cost to $C = \$8.40$. When the hotel controller mandates a $28.0\%$ **Food Cost Percentage** ({{key:CST}}, {{key:PRC}})—equivalent to a $72.0\%$ **Gross Profit Margin**—the chef must navigate the **hyperbolic asymmetry between Margin and Markup**, while also auditing the **Water Activity** ({{key:Aw}}) of the charcuterie course and the pH-dependent **Molecular $\text{SO}_2$** ({{key:SO₂}}) of the sommelier's pairing wine.

---

## Multi-Stage Fabrication Yields and Preservation Equilibria

Every raw agricultural commodity arriving at a restaurant loading dock—whole fish, bone-in subprimals, unpeeled root vegetables, or fresh berries—loses mass across multiple sequential preparation stages before reaching the guest's fork.

### Compounding Multi-Stage Fabrication Yields (`YLD`)

In culinary cost accounting, the gross weight of an untrimmed commodity as delivered by the supplier is the **As-Purchased Mass** ($W_{\text{AP}}$), whereas the net weight of fabricated, cooked food ready for service is the **Edible Portion Mass** ($W_{\text{EP}}$). When a product undergoes $m$ sequential processing stages with individual decimal stage yields $y_1, y_2, \dots, y_m \in (0, 1]$ (where $y_k = 1 - \ell_k$ for stage fractional loss $\ell_k$), mass conservation dictates that the stage yields **multiply geometrically** rather than subtracting linearly:

$$y_{\text{cum}} = \prod_{k=1}^{m} y_k = \prod_{k=1}^{m} \left(1 - \ell_k\right), \qquad Y_{\%} = 100 \cdot y_{\text{cum}} = \left(\frac{W_{\text{EP}}}{W_{\text{AP}}}\right) \times 100, \qquad W_{\text{AP}} = \frac{W_{\text{EP}}}{Y_{\%} / 100}$$

Notice why additive mental math misleads kitchen managers: if whole tenderloin loses $\ell_1 = 20.0\%$ on the butcher table ($y_1 = 0.80$) and the trimmed steaks lose $\ell_2 = 10.0\%$ moisture during searing and resting ($y_2 = 0.90$), the cumulative yield ({{key:YLD}}) is not $100\% - (20\% + 10\%) = 70.0\%$, but rather $y_{\text{cum}} = 0.80 \times 0.90 = \mathbf{0.720}$ ($Y_{\%} = \mathbf{72.0\%}$). Conversely, if a three-stage fish fabrication involves $55\%$ filleting yield ($y_1 = 0.55$), $92\%$ skinning yield ($y_2 = 0.92$), and $88\%$ pan-roasting retention ($y_3 = 0.88$), the cumulative yield plunges to $y_{\text{cum}} = 0.55 \times 0.92 \times 0.88 = \mathbf{0.44528}$ ($44.53\%$).

When the butcher processes our $W_{\text{AP}} = 45.0\text{ lb}$ delivery of whole PSMO beef tenderloin at $Y_{\%} = 72.0\%$ cumulative yield, the Edible Portion equation gives $W_{\text{EP}} = 45.0 \times 0.72 = \mathbf{32.40\text{ lb}}$ ($32.40 \times 16 = \mathbf{518.4\text{ oz}}$), providing an exact $518.4 / 120 = \mathbf{4.32\text{ oz}}$ ($0.270\text{ lb}$) medallion per guest. Conversely, when a wedding contract requires $W_{\text{EP}} = 45.0\text{ lb}$ of finished beef on the pass ($120\text{ guests} \times 6.0\text{ oz}$), evaluating the inverse purchasing formula shows that the steward must order $W_{\text{AP}} = 45.0 / 0.72 = \mathbf{62.50\text{ lb}}$ of untrimmed tenderloin.

### Raoult Water Activity (`Aw`) and Henderson–Hasselbalch Sulfite Equilibrium (`SO₂`)

Preserving the charcuterie, pastry confections, and cellar wines that accompany the banquet menu relies on two physical-chemistry equilibria built directly into the **SC-78** keypad: **Water Activity** ({{key:Aw}}, $a_w$) and **Sulfite Addition** ({{key:SO₂}}). Unlike bulk moisture percentage, water activity $a_w$ measures the thermodynamic chemical potential (escaping tendency) of unbound water molecules via Raoult's law—the ratio of the food's equilibrium water-vapor partial pressure $P_v$ to pure water's saturation vapor pressure $P_0$ at the same temperature, which equals the Equilibrium Relative Humidity ($\text{ERH}_{\%}$) divided by $100$:

$$a_w = \frac{P_v}{P_0} = \frac{\text{ERH}_{\%}}{100} \approx \frac{n_{\text{water}}}{n_{\text{water}} + \nu \, n_{\text{solute}}}$$

Pathogenic bacteria (*Clostridium botulinum*, *Staphylococcus aureus*) cannot proliferate when osmotic solutes (sodium chloride in cured meats via {{key:SAL}} or sucrose in syrups via {{key:SYR}}) depress $a_w$ below $0.85\text{–}0.91$. In the wine cellar, potassium metabisulfite ($\text{K}_2\text{S}_2\text{O}_5$, which yields $57.6\%$ mass fraction of $\text{SO}_2$ gas in acidic must) protects wine against oxidation and *Brettanomyces* spoilage. Because only the un-ionized **molecular $\text{SO}_2$** species ($\text{SO}_2\cdot\text{H}_2\text{O}$, first acid dissociation $\text{p}K_{a1} = 1.81$) crosses microbial cell membranes, the required **Free $\text{SO}_2$** concentration (in $\text{mg/L}$, or $\text{ppm}$) to achieve a target antimicrobial molecular level $[\text{SO}_2]_{\text{mol}}$ (typically $0.80\text{ mg/L}$ for white wine or $0.50\text{ mg/L}$ for red wine) follows the Henderson–Hasselbalch power law ({{key:SO₂}}, matching the buffer physics of Unit VI):

$$\text{Free SO}_2 = \left[\text{SO}_2\right]_{\text{mol}} \cdot \left(1 + 10^{\text{pH} - 1.81}\right), \qquad W_{\text{SO}_2,\text{mg}} = \Delta\text{ppm} \times V_{\text{L}}, \qquad W_{\text{K}_2\text{S}_2\text{O}_5,\text{g}} = \frac{\Delta\text{ppm} \times V_{\text{L}}}{576}$$

At a wine $\text{pH}$ of $3.41$, $10^{3.41 - 1.81} = 10^{1.60} = 39.81$, so achieving $0.80\text{ mg/L}$ of active molecular $\text{SO}_2$ requires $\text{Free SO}_2 = 0.80 \times 40.81 = \mathbf{32.65\text{ ppm}}$; raising a $V_{\text{L}} = 225\text{ L}$ Bordeaux barrique by $\Delta\text{ppm} = 25\text{ mg/L}$ requires $25 \times 225 = \mathbf{5625\text{ mg}}$ ($5.625\text{ g}$) of pure $\text{SO}_2$, or $5625 / 576 = \mathbf{9.766\text{ g}}$ of $\text{K}_2\text{S}_2\text{O}_5$ ({{key:SO₂}}).

---

## The Hyperbolic Geometry of Margin, Markup, and Yield-Adjusted Costing

A restaurant that confuses **Markup on Cost** with **Gross Margin on Revenue**—or that prices its menu using raw supplier invoice prices rather than yield-adjusted edible costs—suffers an immediate, mathematically predictable collapse in operating profit.

### Yield-Adjusted Edible Cost Across Compounding Fabrication Stages

When an untrimmed commodity is purchased at an **As-Purchased Unit Cost** of $C_{\text{AP}}$ (in dollars per pound or kilogram) and yields a cumulative decimal fraction $y_{\text{cum}} = Y_{\%} / 100 = \prod_{k=1}^m y_k$ of edible product after fabrication and cooking, the entire invoice expenditure must be recovered across the smaller edible mass $W_{\text{EP}}$. Dividing $C_{\text{AP}}$ by $y_{\text{cum}}$ gives the true **Edible Portion Unit Cost** ($C_{\text{EP}}$) and the portion cost $C_{\text{portion}}$ for an edible serving of weight $w_{\text{portion}}$:

$$C_{\text{EP}} = \frac{C_{\text{AP}}}{Y_{\%} / 100} = \frac{C_{\text{AP}}}{\prod_{k=1}^{m} y_k}, \qquad C_{\text{portion}} = w_{\text{portion}} \cdot C_{\text{EP}}$$

Because $C_{\text{EP}}$ scales with the **reciprocal** of $y_{\text{cum}}$, low fabrication yields penalize plate cost hyperbolically: while our $72.0\%$ beef tenderloin yield multiplies the $\$16.20/\text{lb}$ invoice price by $1 / 0.72 = 1.3889\times$ to $C_{\text{EP}} = \mathbf{\$22.50/\text{lb}}$ (making each guest's $0.270\text{ lb}$ / $4.32\text{ oz}$ medallion cost $C_{\text{portion}} = 0.270 \times \$22.50 = \mathbf{\$6.075}$, and bringing the complete plated entrée with $\$2.325$ of garnish to $C = \mathbf{\$8.40}$), a flatfish with a $44.53\%$ three-stage yield multiplies the dock price by $1 / 0.4453 = 2.2458\times$.

### The Hyperbolic Asymmetry Between Food Cost (`CST` / `PRC`), Gross Margin, and Markup

Let $C$ denote the total yield-adjusted plate cost and $P$ denote the menu selling price. Commercial accounting defines three coupled dimensionless ratios—decimal **Food Cost Fraction** $f = F / 100$ ({{key:CST}} and {{key:PRC}}), decimal **Gross Margin** $m = M_{\text{margin}} / 100 = 1 - f$, and decimal **Markup on Cost** $u = M_{\text{markup}} / 100$:

$$f = \frac{C}{P}, \qquad m = \frac{P - C}{P} = 1 - f, \qquad u = \frac{P - C}{C} = \frac{P}{C} - 1$$

Although gross margin $m$ and markup $u$ share the exact same numerator—the unit gross profit dollar contribution $\Delta = P - C$—they normalize that profit against different denominators: **Margin divides by selling price $P$**, whereas **Markup divides by kitchen cost $C$**. Eliminating $P / C = 1 / (1 - m) = 1 + u$ between the two definitions reveals a **Möbius (fractional linear) hyperbolic transformation** with a vertical asymptote at $m \to 1^-$, matching the structure of the Standing Wave Ratio $S = (1 + \Gamma)/(1 - \Gamma)$ in Unit V (`SC-50`):

$$P = \frac{C}{f} = \frac{C}{1 - m} = C \left(1 + u\right), \qquad u = \frac{m}{1 - m} = \frac{1 - f}{f}, \qquad m = \frac{u}{1 + u}$$

Consider why linear intuition bankrupts kitchens when a chef mistakes markup for margin:
- To achieve our hotel controller's target **Food Cost Percentage** of $F = 28.0\%$ ($f = 0.28$), the required **Gross Margin** is $m = 1 - 0.28 = \mathbf{0.720}$ ($M_{\text{margin}} = \mathbf{72.0\%}$).
- What **Markup on Cost** $u$ is required to achieve that $72.0\%$ gross margin? Evaluating the hyperbolic mapping gives $u = \frac{0.72}{1 - 0.72} = \frac{0.72}{0.28} = \frac{18}{7} \approx \mathbf{2.57143}$, or a **$257.14\%$ markup** above plate cost ($P = \$8.40 \times (1 + 2.57143) = \$8.40 / 0.28 = \mathbf{\$30.00}$ via {{key:PRC}}, leaving $M_{\text{gross}} = \$30.00 - \$8.40 = \mathbf{\$21.60}$ per plate).
- If an untrained chef hears "we need a $72\%$ return on this $\$8.40$ plate" and applies a **$72.0\%$ markup** ($u = 0.72$) instead of a **$72.0\%$ gross margin** ($m = 0.72$), the menu price is set to $P_{\text{wrong}} = \$8.40 \times 1.72 = \mathbf{\$14.45}$. At $\$14.45$, evaluating {{key:CST}} shows that the food cost jumps to $F = \mathbf{58.14\%}$ and the actual gross margin collapses to $m = \frac{0.72}{1 + 0.72} = \mathbf{41.86\%}$, wiping out $\$15.55$ of contribution margin on every single plate served.

---

## Butcher Yield, Menu Costing, and Preservation on the Stack and in the Solver Workspace

On the **SC-78**, fabrication yield ({{key:YLD}}), food-cost percentage and pricing ({{key:CST}}, {{key:PRC}}), water activity ({{key:Aw}}), sulfite dosing ({{key:SO₂}}), and utensil-snapping volume conversions ({{key:▸cup}}, {{key:▸pt}}, {{key:▸qt}}, {{key:▸dL}}, {{key:▸tb}}, {{key:▸tsp}}) operate across both the RPN stack and the bidirectional {{key:CST}} Solver Workspace.

| Key / Solver | Mode | Inputs / Softkeys ({{keycap:LFU0}}–{{keycap:LFU2}}) | Governing Expression |
| :--- | :--- | :--- | :--- |
| {{key:YLD}} | Immediate Stack | Register $Y$: As-Purchased $W_{\text{AP}}$, Register $X$: Edible $W_{\text{EP}}$ | Trim yield percentage $Y_{\%} = (X / Y) \times 100$ |
| {{key:CST}} | Stack / Solver | Stack: $Y = C, X = P$ • Solver: {{keycap:P}} {{keycap:C}} `[F=30]` | Stack: Food cost $F_{\%} = (C / P) \times 100$; Solver: $P = C / (F / 100)$ |
| {{key:PRC}} | Immediate Stack | Register $Y$: Plate cost $C$, Register $X$: Target food cost $F_{\%}$ | Menu selling price $P = C / (F_{\%} / 100)$ (Gross margin $M_{\%} = 100 - F_{\%}$) |
| {{key:Aw}} / {{key:SO₂}} | Immediate Stack | {{key:Aw}}: $X = \text{ERH}_{\%}$ • {{key:SO₂}}: $Y = W_{\text{SO}_2,\text{mg}}, X = 576$ (or $V_{\text{L}}$) | Water activity $a_w = X / 100$; Sulfite ratio $Y / X$ |
| {{key:▸cup}} {{key:▸tb}} {{key:▸tsp}} | Immediate Stack | Register $X$: Volume in $\text{mL}$ | Converts volume to cups, tablespoons, or teaspoons with fraction snap |

### Immediate Stack Trace: Tenderloin Yield, Plate Costing, and Margin Audit

At the butcher table, the chef verifies the $72.0\%$ fabrication yield on $45.0\text{ lb}$ of tenderloin ({{key:YLD}}), calculates the $\$8.40$ yield-adjusted plate cost, prices the entrée at a $28.0\%$ food-cost target ({{key:PRC}}), and audits the achieved food cost percentage ({{key:CST}}) and gross margin ($100 - F_{\%}$) at a $\$32.00$ menu tariff:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `45` {{key:ENTER}} `32.4` {{key:YLD}} | $0$ | $0$ | $0$ | $72.0000$ | Verify cumulative trim yield $Y_{\%} = (32.4 / 45.0) \times 100 = 72.0\%$ |
| `100` {{key:÷}} `16.20` {{key:x⇄y}} {{key:÷}} | $0$ | $0$ | $0$ | $22.5000$ | Compute true Edible Portion cost $C_{\text{EP}} = \$16.20 / 0.72 = \$22.50/\text{lb}$ |
| `0.27` {{key:×}} `2.325` {{key:+}} | $0$ | $0$ | $0$ | $8.4000$ | Multiply by $0.27\text{ lb}$ ($4.32\text{ oz}$) and add $\$2.325$ garnish: $C = \$8.40$ |
| {{key:ENTER}} {{key:ENTER}} `28` {{key:PRC}} | $0$ | $8.4000$ | $8.4000$ | $30.0000$ | Price $\$8.40$ entrée at $F = 28.0\%$ food cost: $P = \$8.40 / 0.28 = \$30.00$ |
| {{key:x⇄y}} `32` {{key:CST}} `100` {{key:x⇄y}} {{key:-}} | $0$ | $0$ | $30.0000$ | **$73.7500$** | Compute food cost at $P = \$32.00$ ($26.25\%$) and Gross Margin $M_{\%} = 73.75\%$ |

### Bidirectional Solver Workspace (`CST`): Solving Backward for Maximum Plate Cost

Suppose the banquet sales director locks the printed tasting-menu price for the beef course at $P = \$29.00$ per guest while the controller enforces a strict $F = 26.0\%$ food-cost ceiling ($M = 74.0\%$ gross margin). What is the maximum allowable kitchen plate cost $C$ that the chef can spend on meat and garnish? Opening the {{key:CST}} (`P = C / (F / 100)`) Equation Workspace on a cleared stack ({{key:C}}) solves backward via {{key:XEQ}} for {{keycap:C}} in one step:

| Step & Action | Line 1 Workspace Formula | Softkey Legend Bar ({{keycap:LFU0}}–{{keycap:LFU2}}) | Register X Result & Physical Meaning |
| :--- | :--- | :--- | :--- |
| {{key:C}} {{key:CST}} (open workspace) | `CST: P = C / (F / 100)` | {{keycap:P}} {{keycap:C}} `[F=30]` | Opens food-cost pricing workspace with $F = 30.0\%$ default |
| `29` $\to$ {{keycap:P}}, `26` $\to$ {{keycap:F}} | `CST: P = C / (F / 100)` | `[P=29]` {{keycap:C}} `[F=26]` | Stores locked menu price $P = \$29.00$ and target food cost $F = 26.0\%$ |
| {{key:XEQ}} $\to$ {{keycap:C}} | `C = 7.5400` | `[P=29]` `[C=7.54]` `[F=26]` | Solves backward for maximum allowable plate cost $C = \mathbf{\$7.54}$ |
| `8.40` $\to$ {{keycap:C}}, `29` $\to$ {{keycap:P}}, {{key:XEQ}} $\to$ {{keycap:F}} | `F = 28.9655` | `[P=29]` `[C=8.4]` `[F=28.97]` | Solves backward for actual food cost $F = \mathbf{28.97\%}$ if $C = \$8.40$ is kept |

With the maximum allowable plate cost $C = \$7.54$ in Register $X$, subtracting the $\$2.325$ garnish leaves $\$5.215$ for the tenderloin medallion; dividing by $C_{\text{EP}} = \$22.50/\text{lb}$ and multiplying by $16\text{ oz/lb}$ tells the butcher to portion the medallions at $\mathbf{3.708\text{ oz}}$ instead of $4.32\text{ oz}$ to hit the $26.0\%$ cost target.

### Try It on the Stack

Consolidate your command of multi-stage fabrication yields, margin-versus-markup geometry, and preservation equilibria with these three culinary exercises:

1. **Two-Stage Atlantic Halibut Fabrication and Portion Cost ({{key:YLD}} & {{key:PRC}}):** A $35.0\text{ lb}$ whole dressed Atlantic halibut invoiced at $C_{\text{AP}} = \$14.30/\text{lb}$ yields $19.25\text{ lb}$ of skinless center-cut fillet (`35` {{key:ENTER}} `19.25` {{key:YLD}}). Find the true edible cost per pound $C_{\text{EP}}$ (`100` {{key:÷}} `14.30` {{key:x⇄y}} {{key:÷}}), the protein cost of a $6.0\text{ oz}$ ($0.375\text{ lb}$) fillet (`0.375` {{key:×}}), and the menu price required for a $25.0\%$ food cost (`25` {{key:PRC}}). *(Verified Register $X$ results: $Y_{\%} = \mathbf{55.00\%}$, $C_{\text{EP}} = \mathbf{\$26.00/\text{lb}}$, $C_{\text{portion}} = \mathbf{\$9.75}$, and $P = \mathbf{\$39.00}$.)*
2. **Hyperbolic Margin vs. Markup Audit ({{key:CST}}):** A pastry chef plates a chocolate soufflé costing $C = \$3.15$ and prices it on the dessert menu at $P = \$14.00$. Compute the Food Cost percentage (`3.15` {{key:ENTER}} `14` {{key:CST}}), subtract from $100$ (`100` {{key:x⇄y}} {{key:-}}) to find the Gross Margin percentage, and compute the Markup percentage on cost (`14` {{key:ENTER}} `3.15` {{key:Δ%}}). *(Verified Register $X$ results: $F_{\%} = \mathbf{22.50\%}$, $M_{\text{margin}} = \mathbf{77.50\%}$, and $M_{\text{markup}} = \mathbf{344.44\%}$.)*
3. **Barrique Sulfite Addition ({{key:SO₂}}) and Water Activity ({{key:Aw}}):** Compute the milligrams of pure $\text{SO}_2$ required to raise a $225\text{ L}$ wine barrel by $30\text{ ppm}$ (`30` {{key:ENTER}} `225` {{key:×}}), press `576` {{key:SO₂}} to find grams of $\text{K}_2\text{S}_2\text{O}_5$, and check the water activity of a cured sausage whose Equilibrium Relative Humidity is $\text{ERH}_{\%} = 85.0\%$ (`85` {{key:Aw}}, or `19.89` {{key:ENTER}} `23.40` {{key:÷}}). *(Verified Register $X$ results: $W_{\text{SO}_2} = \mathbf{6750\text{ mg}}$, $W_{\text{K}_2\text{S}_2\text{O}_5} = \mathbf{11.719\text{ g}}$, and $a_w = \mathbf{0.8500}$.)*

Having mastered flour-anchored dough scaling, brewhouse zymurgy, and culinary yield costing on the `SC-78`, we turn in [Unit VIII: Clinical Dosing, Renal Clearance & Pharmacokinetics](08-sc80-clinical-pharmacy.md) to the hospital ward and intensive care unit—where human body surface area, glomerular filtration, and continuous intravenous titrations govern patient dosing on the `SC-80`.
