---
title: "SC-14 Industrial Trades, Electrical & Mechanical Handbook"
description: "An applied guide to electrical conductor sizing, three-phase power, conduit bending geometry, and machining physics on the StackCalc 14."
---

# SC-14 Industrial Trades, Electrical & Mechanical Handbook

> **Who this is for:** Anyone who knows Ohm's Law ($V = IR$) and basic right-triangle trigonometry, but wants to understand the hidden physics behind electrical breaker panels, industrial motors, and bending steel pipes around structural obstacles.

---

## 1. When Ohm's Law Meets Heavy Copper

Have you ever noticed the lights in your home dim for a split second when the air conditioner compressor kicks on?

That momentary dip is Ohm's Law playing out along fifty feet of copper hidden behind your drywall. A copper wire is not an imaginary, zero-resistance superconductor; it is a very long, very thin resistor. When a heavy electric motor draws a sudden surge of current, that current passing through the wire's physical resistance drops voltage right in the line. The voltage at the appliance sags, and the missing energy turns directly into heat inside the wall.

In a home, an undersized wire might merely cause flickering lamps or a tripped breaker. But in a commercial hospital, a high-rise data center, or an industrial chemical plant, excessive electrical heat can melt insulation and cause electrical fires. To prevent this, the National Fire Protection Association publishes **NFPA 70**, known universally as the **National Electrical Code (NEC)**.

The NEC is essentially applied physics and geometry codified into law. Electricians, pipefitters, and precision machinists work in an environment where math must be calculated quickly, accurately, and without paper:
- Sizing a feeder cable so that a $480\text{-volt}$ industrial pump doesn't suffer brownout over a $300\text{-foot}$ run.
- Calculating how much steel conduit shrinks when bending around an overhead structural I-beam.
- Figuring out the exact spindle RPM for a carbide milling cutter so it cuts clean metal without overheating and dulling.

The **StackCalc 14 (SC-14)** puts these trade formulas, conductor tables, and mechanical calculations directly onto a rugged 4-level RPN stack.

### Why Not Just Use a Smartphone?

- **The Scissor Lift Environment:** Picture standing on a scissor lift platform thirty feet in the air, wearing leather work gloves coated in greasy wire-pulling lubricant. A glass smartphone requires bare hands, risks cracking if dropped onto concrete, and turns off its screen mid-calculation. The SC-14 is built for one-handed operation with tactile mechanical switches that click clearly even through thick gloves.
- **Scrap Conduit is Expensive:** A single 10-foot stick of 3-inch or 4-inch rigid metal pipe costs over $\$150$. If you miscalculate the offset travel or forget the shrinkage when bending around an obstacle, the pipe dog-legs, misses the junction box, and has to be thrown in the scrap bin.
- **Licensing Exams:** Journeyman and Master Electrician licensing exams strictly ban smartphones and internet-connected devices. Candidates must be able to calculate conductor ampacity, conduit fill, and three-phase motor loads on an approved standalone instrument.

---

## 2. Core Concepts: How Electricians and Machinists Think

### Concept 1: The Vanishing Volts & Circular Mils ($CM$)

Why do electricians measure wire thickness in "Circular Mils" rather than square millimeters or inches?

A mil is one-thousandth of an inch ($0.001\text{ in}$). In standard geometry, the area of a circle is $\frac{\pi}{4} d^2$. But when sizing thousands of cables, carrying $\frac{\pi}{4}$ through every calculation is tedious. 

Electrical pioneers invented a brilliant shortcut: **A Circular Mil ($CM$) is simply the diameter in mils, squared**:

$$CM = (d_{\text{mils}})^2 = (d_{\text{inches}} \times 1000)^2$$

A wire with a diameter of $0.10\text{ inches}$ is $100\text{ mils}$ thick, which means its area is simply $100^2 = 10{,}000\text{ CM}$. The circle's $\pi$ factor is baked directly into the material resistivity constant $K$:
- **Copper ($K_{\text{Cu}}$):** $\approx 12.9\,\Omega\cdot\text{cmil/ft}$ at normal operating temperatures.
- **Aluminum ($K_{\text{Al}}$):** $\approx 21.2\,\Omega\cdot\text{cmil/ft}$.

#### The Voltage Drop Formula
For a single-phase two-wire circuit carrying current $I$ over a one-way distance $L$ (total wire loop length is $2L$):

$$\text{Voltage Drop } (VD) = \frac{2 \cdot K \cdot I \cdot L}{CM}$$

The NEC recommends that voltage drop never exceed **3%** on a branch circuit (e.g. no more than $3.6\text{ V}$ drop on a $120\text{ V}$ line). If the calculated drop is too high, you must step up to a thicker wire gauge with more circular mils.

### Concept 2: The Power of Three ($\sqrt{3} \approx 1.732$)

Why do commercial buildings and factories run on Three-Phase AC rather than the single-phase AC in our homes?

In single-phase power, voltage pulses like a heartbeat: it peaks, drops through zero, and reverses 60 times a second. A single-phase motor vibrates and needs auxiliary starting capacitors.

In three-phase power, three independent alternating voltage waves travel together, staggered evenly $120^\circ$ apart. When one wave is passing through zero, the other two are delivering strong power. The total electrical power delivered is continuous and smooth, allowing motors to be smaller, lighter, and self-starting.

Because the three waves are separated by $120^\circ$ on a circle, the line-to-line voltage is not simply double: it is multiplied by the geometric factor $\mathbf{\sqrt{3} \approx 1.732}$:

$$V_{\text{line-to-line}} = \sqrt{3} \cdot V_{\text{phase-to-neutral}} \approx 1.732 \times 120\text{ V} \approx 208\text{ V}$$
$$1.732 \times 277\text{ V} \approx 480\text{ V}$$

#### Sizing Three-Phase Motor Circuits
For a 3-phase motor delivering horsepower ($1\text{ HP} = 746\text{ Watts}$) at efficiency $\eta$ and power factor $PF$:

$$\text{Full Load Amps } (FLA) = \frac{\text{HP} \cdot 746}{\sqrt{3} \cdot V_{\text{line}} \cdot \eta \cdot PF}$$

Under NEC Article 430, because electric motors draw a heavy inductive inrush current when starting up, conductors must be sized to **$125\%$ of motor FLA**. On the SC-14, pressing `[f] [3PH÷]` automatically incorporates $\sqrt{3}$ in one keystroke.

### Concept 3: Bending Steel Pipe with Right Triangles

When routing conduit across a ceiling, electricians frequently hit obstacles: air ducts, fire sprinkler lines, or structural steel columns. To get around them, you bend the pipe out and back in an **offset bend**:

```
                       Offset Depth (D)
                      |---|
    ------------------\
                       \   Travel (Hypotenuse = D * csc θ)
                        \
                         \---------------------
```

An offset is simply two equal and opposite right triangles:
- **Travel Distance (Hypotenuse):** $\text{Travel} = \text{Depth} \cdot \csc\theta = \frac{\text{Depth}}{\sin\theta}$
- **Conduit Shrinkage:** Because the hypotenuse is longer than the straight horizontal path, bending an offset pulls the end of the pipe backward toward the bender. If you don't account for this "shrinkage," your pipe will end up too short to reach the next junction box!

$$\text{Shrinkage} = \text{Depth} \times \left(\frac{1}{\tan\theta} - \frac{1}{\sin\theta}\right)$$

#### Bending Multipliers Quick Reference
- **$30^\circ$ Bend:** Multiplier $= 2.0$ (Travel is exactly twice the depth; shrinks $1/4\text{ in}$ per inch of depth).
- **$45^\circ$ Bend:** Multiplier $= 1.414$ (Travel is $1.414 \times \text{Depth}$; shrinks $3/8\text{ in}$ per inch of depth).

### Concept 4: Machining Feeds and Speeds

In a machine shop, cutting metal on a milling machine or lathe obeys a simple physical rule: the cutting tool must slide through the workpiece at a specific linear velocity called **Surface Feet per Minute ($SFM$)**:
- Mild steel cuts at roughly $100\text{ SFM}$ with high-speed steel.
- Aluminum can be machined at $600\text{ SFM}$ or higher.

To turn linear surface feet into rotational spindle speed ($RPM$):

$$RPM = \frac{SFM \times 12}{\pi \cdot \text{Diameter}} \approx \frac{3.82 \cdot SFM}{\text{Diameter (inches)}}$$

A tiny $1/8\text{-inch}$ drill bit must spin at high RPM to achieve the proper cutting speed, while a massive $3\text{-inch}$ face mill must turn much slower to avoid overheating its carbide inserts.

---

## 3. Real-World Field Walkthroughs

### Field Case 1: Sizing a 480V Sub-Panel Feeder (`r/electricians`)

An electrician is running a continuous $65\text{-amp}$ balanced 3-phase load from a main switchboard to a sub-panel located $220\text{ feet}$ away. The supply voltage is $480\text{ V}$ 3-phase copper.
1. What minimum ampacity wire is required under the NEC $125\%$ continuous load rule?
2. If using #4 AWG copper wire ($41{,}740\text{ CM}$), what is the expected voltage drop and percentage drop?

#### How to Solve It on the SC-14
1. **Apply the 125% Continuous Rule (NEC 210.20):**
   - `65` `[ENTER]` `1.25` `[×]` $\to$ **`81.25 Amps`**.
   - Looking at NEC Table 310.16 via `[TBL]`: #4 AWG copper (rated for $85\text{ A}$ at $75^\circ\text{C}$) is required.
2. **Calculate 3-Phase Voltage Drop:**
   - Formula: $VD = \frac{\sqrt{3} \cdot K \cdot I \cdot L}{CM}$ ($K = 12.9$ for Cu, $I = 65\text{ A}$, $L = 220\text{ ft}$, $CM = 41740$).
   - `1.732` `[ENTER]` `12.9` `[×]` `65` `[×]` `220` `[×]`
   - Stack displays: `319485`
   - `41740` `[÷]` $\to$ **`7.65 Volts`**.
3. **Calculate Percentage Drop:**
   - `7.65` `[ENTER]` `480` `[÷]` `100` `[×]` $\to$ **`1.59%`**.
   - Since $1.59\% < 3.0\%$, the wire easily satisfies code requirements without excessive heat.

---

### Field Case 2: Bending a 4-Inch Offset Around an I-Beam (`Practical Machinist`)

An electrician running $1\text{-inch}$ EMT conduit must clear a steel ceiling beam that hangs $4\text{ inches}$ lower than the roof deck. The electrician chooses a standard $30^\circ$ offset.
1. How far apart should the two bend marks be made on the pipe (Travel)?
2. How much will the pipe shrink toward the bender?

#### Step-by-Step Mechanics
1. **Compute Travel Distance:**
   - Multiplier for $30^\circ$ is $\frac{1}{\sin(30^\circ)} = 2.0$.
   - `4` `[ENTER]` `30` `[SIN]` `[÷]` $\to$ **`8.00 inches`**.
   - The electrician places the two bend arrows exactly $8\text{ inches}$ apart on the conduit.
2. **Compute Pipe Shrinkage:**
   - For $30^\circ$, shrink is $1/4\text{ inch}$ per inch of offset depth.
   - `4` `[ENTER]` `0.25` `[×]` $\to$ **`1.00 inch`**.
   - The electrician shifts the first bend mark forward by $1\text{ inch}$ so the final end lands flush in the junction box.

---

## 4. Try It Yourself: Practice Problems

### Problem 1: Motor Full Load Current
A three-phase $480\text{-volt}$ induction motor produces $25\text{ HP}$ on a factory conveyor line. The motor nameplate lists an operating efficiency of $88\%$ ($\eta = 0.88$) and a power factor of $0.85$ ($PF = 0.85$).
Calculate the motor Full Load Amps ($FLA$).
*(Solution: $25 \times 746 = 18{,}650\text{ W}$. Denominator $= 1.732 \times 480 \times 0.88 \times 0.85 = 622.3$. $FLA = 18650 / 622.3 = \mathbf{29.97\text{ Amps}}$. Branch conductors must be sized to $125\% \times 29.97 = \mathbf{37.5\text{ A}}$.)*

### Problem 2: Conduit Raceway Fill
Under NEC Chapter 9 Table 1, a conduit raceway with more than two conductors may be filled to a maximum of **40%** of its cross-sectional area.
A $1\text{-inch}$ EMT conduit has an internal cross-sectional area of $0.864\text{ sq in}$.
If each #10 THHN conductor has a cross-sectional area of $0.0211\text{ sq in}$, what is the maximum number of #10 wires allowed in this pipe?
*(Solution: Usable area $= 0.864 \times 0.40 = 0.3456\text{ sq in}$. Max wires $= 0.3456 / 0.0211 = 16.38 \implies \mathbf{16\text{ wires}}$.)*

### Problem 3: CNC Spindle Speed
A machinist is facing an aluminum block ($SFM = 500$) using a $2.5\text{-inch}$ diameter carbide face mill.
Calculate the proper spindle speed in $RPM$.
*(Solution: $RPM = 3.82 \times 500 / 2.5 = \mathbf{764\text{ RPM}}$.)*
