---
title: "SC-78 Commercial Bakery, Fermentation Science & Brewing Handbook"
description: "An applied guide to Baker's Percentages, dough temperature thermodynamics, equilibrium brining, and brewing gravity on the StackCalc 78."
---

# SC-78 Commercial Bakery, Fermentation Science & Brewing Handbook

> **Who this is for:** Anyone who loves cooking, artisan bread baking, or homebrewing, and wants to understand why professional bakeries treat flour as an immutable 100% anchor, and how dough water temperature is calculated like an engineering heat-transfer problem.

---

## 1. When the Kitchen Becomes a Laboratory

In home cooking, a recipe often reads: *"Add two cups of flour, one cup of milk, and a pinch of salt."*

If you walk into a commercial artisan bakery or craft brewery, you will never see a measuring cup. Volumetric measurements in baking are notoriously unreliable: depending on ambient humidity, how finely wheat was milled, and whether the flour was sifted or packed down, a single measuring cup of flour can weigh anywhere from **110 grams to 160 grams**—a massive $45\%$ variance!

In bread making, where the difference between a dense sandwich loaf and a light, open-crumb rustic sourdough is a matter of a few percent water content, volume is the enemy of consistency. Everything must be weighed on a scale in **grams**.

Furthermore, professional kitchens face a constant mathematical puzzle: **scaling**. If your recipe makes three loaves of bread, but tomorrow morning you need to bake four hundred and fifty loaves, how do you scale the ingredients without altering the dough's hydration or salt balance?

To solve this, professional bakers invented a brilliant mathematical coordinate system called **Baker’s Percentages ($BK\%$)**. Combined with the thermodynamics of mixer motor friction and yeast fermentation kinetics, baking is not guesswork—it is delicious applied mathematics.

The **StackCalc 78 (SC-78)** brings this commercial precision to the kitchen bench, charcuterie curing cellar, and brew kettle. It incorporates locked Baker's Percentage scaling (`@BK%`), Desired Dough Temperature solvers (`TW`), equilibrium brining formulas, and brewing specific gravity calculations into a unified RPN stack.

### Why Not Just Use a Smartphone?

- **The Flour Dust and Sticky Dough Reality:** A commercial bakery at 4:00 AM is coated in fine airborne flour dust and sticky dough residues. Trying to unlock a touchscreen phone with flour-coated thumbs or wet sourdough hands leads to missed touches, scratched glass, and dust-clogged ports. The SC-78 features tactile mechanical switches that can be operated through flour-covered palms and wiped down at the end of the shift.
- **Why Standard Math Percentages Fail:** In standard math, percentages must always sum to $100\%$. If you increase the water in a batch of bread from $65\%$ to $75\%$, standard percentages would force the flour percentage to drop, which alters the calculated percentages of salt and yeast! In Baker’s Percentages, **flour is permanently anchored at $100.0\%$**, keeping all ingredient relationships rock-solid.

---

## 2. Core Concepts: How Bakers and Brewers Think

### Concept 1: Flour is the Anchor (Baker's Percentages)

In Baker's Percentages, the total weight of the flour is always defined as **$100.0\%$**. If a formula uses multiple flours (e.g. $80\%$ bread flour and $20\%$ whole rye), their combined mass is $100.0\%$.

Every other ingredient is weighed as a direct ratio of the flour mass:

$$\text{Ingredient } \% = \left(\frac{\text{Mass of Ingredient}}{\text{Mass of Flour}}\right) \times 100$$

#### Classic Artisan Country Loaf Formula:
- **Flour Blend:** $1{,}000\text{ g} \implies \mathbf{100.0\%}$
- **Water (Hydration):** $750\text{ g} \implies \mathbf{75.0\%}$
- **Sourdough Starter (Levain):** $200\text{ g} \implies \mathbf{20.0\%}$
- **Salt:** $20\text{ g} \implies \mathbf{2.0\%}$
- **Total Formula Percent:** $100 + 75 + 20 + 2 = \mathbf{197.0\%}$

Notice that the total percentage is $197\%$, not $100\%$! This system makes scaling effortless:

#### Scaling Down from Available Flour
If you open a bin and find you have exactly $42.5\text{ kg}$ of flour left, how much water and salt do you add?
- Water: $42.5\text{ kg} \times 0.75 = \mathbf{31.88\text{ kg}}$
- Salt: $42.5\text{ kg} \times 0.02 = \mathbf{0.85\text{ kg}} = \mathbf{850\text{ grams}}$

#### Scaling Up from Target Finished Dough Weight
If you need to produce exactly $150\text{ kg}$ of finished dough to fill today's baguette orders:

$$\text{Required Flour Mass} = \frac{\text{Target Dough Mass}}{\text{Total Formula } \% / 100} = \frac{150\text{ kg}}{1.97} = \mathbf{76.14\text{ kg of Flour}}$$

Once you know the flour mass, every other ingredient scales in one keystroke on the SC-78.

### Concept 2: The Heat of the Machine (Desired Dough Temperature)

Yeast is a living biological organism. Within normal kitchen temperatures, its metabolic fermentation rate **doubles for every $15^\circ\text{F}$ ($8.3^\circ\text{C}$) rise in temperature**.

For consistent flavor and structure, artisan bread dough should exit the mixer at an ideal target temperature—typically **$76^\circ\text{F}$ to $78^\circ\text{F}$ ($24^\circ\text{C}$ to $26^\circ\text{C}$)**.

However, a commercial spiral mixer does not merely fold dough; its heavy rotating steel hook imparts intense **mechanical friction heat ($15^\circ\text{F}$ to $25^\circ\text{F}$)** directly into the dough mass. 

To achieve the target dough temperature, the baker can only control one variable: **the temperature of the water ($T_W$) poured into the mixer bowl**.

#### The Three-Factor Rule
The baker measures:
- Room Temperature ($T_{\text{room}}$)
- Flour Temperature ($T_{\text{flour}}$, measured with a probe thermometer)
- Mixer Friction Factor ($F$, determined experimentally for each mixer machine)

$$\text{Required Water Temperature } (T_W) = 3 \cdot T_{\text{desired}} - (T_{\text{room}} + T_{\text{flour}} + F)$$

If the required water temperature calculates below $32^\circ\text{F}$, tap water cannot get cold enough, and the baker must substitute a portion of the water with crushed ice!

### Concept 3: Density, Sugar, and Alcohol (Brewing Specific Gravity)

In brewing, beer is made by extracting fermentable sugars (maltose) from malted barley into hot water to create sweet liquid **wort**.

Brewers track fermentation using **Specific Gravity ($SG$)**: the density of the wort compared to pure water ($1.000\text{ at } 20^\circ\text{C}$):
- Sweet unfermented wort typically has an **Original Gravity ($OG$)** between $1.040$ and $1.080$.
- As yeast consumes sugars, it converts dense sugar into less dense ethanol ($\text{density} \approx 0.789\text{ g/mL}$) and carbon dioxide gas (which bubbles away).
- When fermentation ceases, the **Final Gravity ($FG$)** drops down to $1.008$ to $1.015$.

The percentage of **Alcohol by Volume ($ABV$)** is calculated from the gravity drop:

$$ABV\% \approx (OG - FG) \times 131.25$$

For example, a beer that starts at $OG = 1.056$ and finishes at $FG = 1.012$:
$$ABV = (1.056 - 1.012) \times 131.25 = 0.044 \times 131.25 = \mathbf{5.78\% \text{ ABV}}$$

---

## 3. Real-World Field Walkthroughs

### Field Case 1: Summer Sourdough Water Temp & Ice Replacement (`r/Sourdough`)

A bakery on a warm July morning wants a finished dough temperature $T_D = 78^\circ\text{F}$.
- Room Temperature: $T_R = 76^\circ\text{F}$
- Flour Temperature: $T_F = 74^\circ\text{F}$
- Spiral Mixer Friction Factor: $F = 22^\circ\text{F}$
- Recipe calls for $15.0\text{ kg}$ total water.
1. What is the required water temperature ($T_W$)?
2. If tap water is $68^\circ\text{F}$, how many kilograms of ice must replace liquid water to reach the target temperature?

#### How to Solve It on the SC-78
1. **Calculate Required Water Temperature:**
   $$T_W = 3(78) - (76 + 74 + 22) = 234 - 172 = \mathbf{62.0^\circ\text{F}}$$
2. **Ice Mass Substitution Formula:**
   Because melting ice absorbs $144\text{ BTU/lb}$ (the latent heat of fusion):
   $$\text{Ice Fraction} = \frac{T_{\text{tap}} - T_W}{T_{\text{tap}} + 112} = \frac{68 - 62}{68 + 112} = \frac{6}{180} = 0.0333 \implies \mathbf{3.33\%}$$
   $$\text{Ice Mass} = 15.0\text{ kg} \times 0.0333 = \mathbf{0.50\text{ kg}} = \mathbf{500\text{ grams of ice}}$$
The baker weighs out $500\text{ g}$ of ice and $14.5\text{ kg}$ of tap water. When the ice melts during mixing, the dough exits the machine at exactly $78^\circ\text{F}$!

---

### Field Case 2: Equilibrium Brining for Smoked Pork Belly (*The Fresh Loaf*)

A charcutier is curing a $3.5\text{-kg}$ slab of pork belly in a vacuum bag with $1.5\text{-kg}$ of water. The recipe calls for a balanced equilibrium salinity of $2.25\%$ salt.
How many grams of curing salt are required?

#### Step-by-Step Mechanics
1. In equilibrium brining, the salt dissolves and equilibrates evenly across the combined mass of meat and water:
   $$\text{Total Mass} = 3.5\text{ kg (meat)} + 1.5\text{ kg (water)} = 5.0\text{ kg}$$
2. Calculate salt mass at $2.25\%$:
   - `5000` `[ENTER]` `2.25` `[%]`
   - Register $X$ displays: **`112.5 grams of salt`**.
The salt distributes completely through the meat with zero risk of over-salting!

---

## 4. Try It Yourself: Practice Problems

### Problem 1: Baker's Percentage Sourdough Scaling
A recipe has the following Baker's Percentages:
- Flour: $100\%$
- Water: $72\%$
- Starter: $20\%$
- Salt: $2\%$
(Total Formula $= 194\%$).
You have an open bag of flour weighing exactly $35.0\text{ kg}$. Calculate the required water mass and total expected dough yield.
*(Solution: Water $= 35.0 \times 0.72 = \mathbf{25.2\text{ kg}}$. Total dough $= 35.0 \times 1.94 = \mathbf{67.9\text{ kg}}$.)*

### Problem 2: Beer Alcohol by Volume (ABV)
A homebrewer measures a batch of Belgian Tripel with a hydrometer:
- Original Gravity: $OG = 1.082$
- Final Gravity: $FG = 1.014$
Calculate the Alcohol by Volume ($ABV\% = (OG - FG) \times 131.25$).
*(Solution: $1.082 - 1.014 = 0.068$. $0.068 \times 131.25 = \mathbf{8.925\% \text{ ABV}}$.)*

### Problem 3: Pan Volume Scaling
You have a cake recipe sized for an $8\text{-inch}$ round cake pan ($Area = \pi \cdot 4^2 = 50.27\text{ sq in}$).
You want to bake the same cake in a $9 \times 13\text{-inch}$ rectangular pan ($Area = 117.0\text{ sq in}$) at the same depth.
Calculate the scaling multiplier: $\text{Multiplier} = 117.0 / 50.27$.
*(Solution: $117.0 / 50.27 = \mathbf{2.327\times}$. Multiply every ingredient in the recipe by $2.33$!)*
