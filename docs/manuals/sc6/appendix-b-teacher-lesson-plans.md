---
title: "Appendix B: Teacher Lesson Plans & Diagnostic Protocols"
description: "Twenty-five turnkey classroom station lesson scripts, teacher dialogue, student misconception diagnostic tables, and 4-tier rubrics for the StackCalc SC-6 across Kindergarten through Grade 6."
---

# Appendix B: Teacher Lesson Plans & Diagnostic Protocols

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">PEDAGOGICAL PLAYBOOK // APPENDIX B</span>
  <span class="te-viewport-status text-emerald-400">● 25 TURNKEY LESSON PLANS &bull; K–6 CURRICULUM &bull; VERBATIM SCRIPTS &bull; 4-TIER RUBRICS</span>
</div>

> CHAPTER BASELINE MODE: {{key:NUM}}
> Classroom Facilitation Playbook • Zero Mode Dependencies

<div class="admonition note">
<p class="admonition-title">Unlocked Keycaps Ribbon — Teachers, Homeschoolers &amp; Math Coaches</p>
<p>
• <strong>Classroom Scope:</strong> Twenty-five complete 45-minute station lesson plans spanning Kindergarten through Grade 6 (CCSS-M &amp; TEKS aligned).<br>
• <strong>Pedagogical Sequencing (CRA):</strong> Concrete manipulatives first, pictorial sketches second, SC-6 four-register LCD stack confirmation third.<br>
• <strong>Cognitive Integrity:</strong> Students solve problems tactilely and mentally first; the calculator functions as an immediate self-checking and cognitive confirmation instrument.
</p>
</div>

---

## Station Facilitation Model & Workshop Architecture

The StackCalc SC-6 curriculum follows the **Math Workshop Rotation Model**, grounded in Liping Ma’s profound understanding of fundamental mathematics {{cite:ma1999}}, Jerome Bruner’s CRA progression {{cite:bruner1966}}, the Singapore Ministry of Education pedagogical framework {{cite:singapore2014}}, and the Common Core State Standards {{cite:ccssm2010}}. In this structure, every mathematical concept is grounded through a tripartite Concrete-Representational-Abstract (CRA) sequence:

<div class="admonition note">
<p class="admonition-title">45-Minute Station Lesson Structure</p>

| Time Window | Phase | Activity & Student Experience |
| :---: | :--- | :--- |
| **00:00 – 05:00** | Whole-Class Concrete Launch | Pose the real-world narrative challenge and frame the question. |
| **05:00 – 20:00** | Station Investigation | Hands-on physical manipulative build at studio stations. |
| **20:00 – 35:00** | Representational & Abstract | SC-6 four-register stack verification and keystroke logging. |
| **35:00 – 45:00** | Discourse & Exit Ticket | Mathematical reflection, diagnostic check, and notebook log. |

</div>

### Four-Register Stack Elevator Mental Model
For elementary students, the four-register RPN stack ($X, Y, Z, T$) is taught as a four-story glass elevator:
- **Floor 1 (Register $X$):** The Lobby / Ground Floor where current typing happens.
- **Floor 2 (Register $Y$):** The First Balcony where numbers wait for two-number operations.
- **Floor 3 (Register $Z$):** The Second Balcony for intermediate storage.
- **Floor 4 (Register $T$):** The Penthouse / Constant Dispenser that duplicates downward during continuous operations.

---

## Kindergarten Lesson Plans (Ages 5–6)

### Lesson K.1: One-to-One Correspondence & Counting to 10
- **Standards:** CCSS.MATH.CONTENT.K.CC.B.4; TEKS K.2.B.
- **Learning Objective:** Students will place up to 10 physical counters onto a Ten-Frame Studio tray while stepping through counts on the SC-6 LCD display using Ten-Frame Mode (`{{key:▦}}`).
- **Manipulatives:** Ten-Frame Studio tray (`ten_frame_tray.scad`), 10 two-color flip counters (yellow/red).
- **Tactile Warm-Up (5 min):** "Place 4 yellow counters in the top row. Count them with your finger: one, two, three, four. Now tap one red counter into the next space. How many now?"

#### Verbatim Teacher Dialogue Script
> **Teacher:** "Hold up your SC-6 calculator. Tap the Number Rack key `{{key:COUNT}}`. Look at the glass screen. Do you see the two empty rows of five boxes, just like your wooden tray?"  
> **Students:** "Yes! It looks like our tray!"  
> **Teacher:** "Now, let us drop one counter into both trays at the same time. Place one yellow counter on your tray. At the same time, tap `1 {{key:+}}` on your calculator. What popped onto your screen?"  
> **Student (Leo):** "A little dot filled the first box!"  
> **Teacher:** "Tap `1 {{key:+}}` again. And again. Stop when your top row is full. How many counters are in the top row?"  
> **Students:** "Five!"  
> **Teacher:** "What number shows in the corner?"  
> **Students:** "5!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:COUNT}} | 0 | 0 | 0 | 0 (10F) |
| 1 {{key:+}} | 0 | 0 | 0 | 1 (10F) |
| 1 {{key:+}} | 0 | 0 | 0 | 2 (10F) |
| 1 {{key:+}} | 0 | 0 | 0 | 3 (10F) |
| 1 {{key:+}} | 0 | 0 | 0 | 4 (10F) |
| 1 {{key:+}} | 0 | 0 | 0 | 5 (10F) |

#### Student Practice Problems
1. Count out 7 counters on the tray and match with 7 dots on the SC-6 (`{{key:COUNT}} 7`).
2. Show 10 full dots on the screen. How many rows are filled? (Both rows, answer: 10).
3. Clear the frame (`{{key:C}} {{key:COUNT}}`). Enter 3 dots. How many empty boxes remain? (7 boxes).

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student taps keys rapidly, overshooting the physical counter count. | Motor impulsivity without one-to-one correspondence pairing. | "One touch on the block, one tap on the key. Say 'click' for each." |
| Student starts filling the bottom row first. | Lacks left-to-right, top-to-bottom reading orientation. | "The top row is the attic. Fill the attic from left to right first!" |

---

### Lesson K.2: Composing & Decomposing 5 (Number Bonds)
- **Standards:** CCSS.MATH.CONTENT.K.OA.A.3; TEKS K.3.A.
- **Learning Objective:** Students decompose 5 into pairs ($4+1, 3+2, 2+3, 1+4$) using two-color counters and verify that the sum remains invariant.
- **Manipulatives:** 5 two-color counters, 1 Ten-Frame Studio tray.
- **Tactile Warm-Up:** Shake 5 counters in a cup and spill them onto the desk. Count yellow vs. red.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "Spill your counters! Maya, how many yellow and how many red did you get?"  
> **Student (Maya):** "I got 3 yellow and 2 red."  
> **Teacher:** "Let us enter Maya's spill into our SC-6 elevator. Type `{{key:3}} {{key:ENTER}}`. The 3 rides up to the first balcony. Now type `{{key:2}}`. Look at Floor 1 and Floor 2. Press `{{key:+}}`. What is the total?"  
> **Students:** "5!"  
> **Teacher:** "Now spill again! David, what did you get?"  
> **Student (David):** "4 yellow and 1 red."  
> **Teacher:** "Type `{{key:4}} {{key:ENTER}} {{key:1}} {{key:+}}`. What do you get?"  
> **Students:** "Still 5!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:3}} | 0 | 0 | 0 | 3 |
| {{key:ENTER}} | 0 | 0 | 3 | 3 |
| {{key:2}} | 0 | 0 | 3 | 2 |
| {{key:+}} | 0 | 0 | 0 | 5 |

#### Student Practice Problems
1. Enter $1 + 4$: `{{key:1}} {{key:ENTER}} {{key:4}} {{key:+}}`. Display shows `5`.
2. Enter $2 + 3$: `{{key:2}} {{key:ENTER}} {{key:3}} {{key:+}}`. Display shows `5`.
3. Enter $5 + 0$: `{{key:5}} {{key:ENTER}} {{key:0}} {{key:+}}`. Display shows `5`.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student types `32 {{key:+}}` without `{{key:ENTER}}`, getting 32. | Forgets stack lift separator. | "Press `{{key:ENTER}}` so the 3 can climb into the balcony before 2 enters the lobby!" |
| Student thinks $3+2$ and $2+3$ have different totals. | Has not internalized commutativity. | "Turn your tray around $180^\circ$. Did any counters disappear?" |

---

### Lesson K.3: Comparing Quantities (More, Fewer, Same)
- **Standards:** CCSS.MATH.CONTENT.K.CC.C.6; TEKS K.2.E.
- **Learning Objective:** Students compare two towers of counting tiles using a balance scale, determine the difference, and verify on SC-6 via subtraction.
- **Manipulatives:** Equal-arm balance scale (`algebra_factoring_parts.scad`), 20 counting tiles from Counting Studio (10 blue, 10 gold).
- **Tactile Warm-Up:** Place 7 blue tiles in the left pan and 4 gold tiles in the right pan. Observe which pan drops.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "Which pan is heavier and lower?"  
> **Students:** "The blue pan with 7 tiles!"  
> **Teacher:** "How many more tiles are in the blue pan? Let us ask the calculator to find the difference. Put the bigger number in first: `{{key:7}} {{key:ENTER}}`. Now put the smaller number in: `{{key:4}}`. Press `{{key:-}}`. What is the difference?"  
> **Students:** "3!"  
> **Teacher:** "Add 3 tiles to the gold pan. What happens to the balance beam?"  
> **Students:** "It levels out! They are equal!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:7}} | 0 | 0 | 0 | 7 |
| {{key:ENTER}} | 0 | 0 | 7 | 7 |
| {{key:4}} | 0 | 0 | 7 | 4 |
| {{key:-}} | 0 | 0 | 0 | 3 |

#### Student Practice Problems
1. Compare 9 and 5: `{{key:9}} {{key:ENTER}} {{key:5}} {{key:-}}`. Difference is `4`.
2. Compare 8 and 8: `{{key:8}} {{key:ENTER}} {{key:8}} {{key:-}}`. Difference is `0` (balanced).
3. Compare 6 and 2: `{{key:6}} {{key:ENTER}} {{key:2}} {{key:-}}`. Difference is `4`.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student enters `{{key:4}} {{key:ENTER}} {{key:7}} {{key:-}}` and gets `-3`. | Operates with smaller number first. | "In subtraction, the heavy tower enters the elevator first!" |
| Student equates physical height with numerical quantity when using mismatched objects. | Perceptual salience over unit count. | "Count the cubes one-by-one; do not just look with your eyes." |

---

## Grade 1 Lesson Plans (Ages 6–7)

### Lesson 1.1: Bridging Through 10 with the Ten-Frame
- **Standards:** CCSS.MATH.CONTENT.1.OA.C.6; TEKS 1.3.C.
- **Learning Objective:** Students solve $8 + 5$ by decomposing 5 into $2 + 3$, filling the first ten-frame, and recognizing that $8 + 5 = 10 + 3 = 13$.
- **Manipulatives:** 2 Ten-Frame Studio trays side-by-side, 20 two-color counters.
- **Tactile Warm-Up:** Place 8 counters in the first frame. Place 5 in hand. How many are needed to fill the first frame?

#### Verbatim Teacher Dialogue Script
> **Teacher:** "We have 8 yellow counters in Tray 1. We want to add 5 red counters. Where must the first 2 red counters go?"  
> **Student (Sophia):** "They must go in the empty spots of Tray 1 to make 10!"  
> **Teacher:** "Great! That makes 10. How many red counters are still in your hand?"  
> **Student (Sophia):** "3 counters!"  
> **Teacher:** "Put them in Tray 2. So 8 plus 5 is the same as 10 plus 3! Let us see this on the SC-6. Type `{{key:8}} {{key:ENTER}} {{key:5}} {{key:+}}`. What do you get?"  
> **Students:** "13!"  
> **Teacher:** "Now press `{{key:▦}}`. See the two frames on screen: one completely full (10), and the second has 3 dots!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:8}} | 0 | 0 | 0 | 8 |
| {{key:ENTER}} | 0 | 0 | 8 | 8 |
| {{key:5}} | 0 | 0 | 8 | 5 |
| {{key:+}} | 0 | 0 | 0 | 13 |
| {{key:▦}} | 0 | 0 | 0 | 13(10F) |

#### Student Practice Problems
1. Solve $9 + 6$: `{{key:9}} {{key:ENTER}} {{key:6}} {{key:+}} {{key:▦}}`. Display shows 10 + 5 = 15.
2. Solve $7 + 5$: `{{key:7}} {{key:ENTER}} {{key:5}} {{key:+}} {{key:▦}}`. Display shows 10 + 2 = 12.
3. Solve $8 + 7$: `{{key:8}} {{key:ENTER}} {{key:7}} {{key:+}} {{key:▦}}`. Display shows 10 + 5 = 15.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student counts on fingers starting from 1 ($1, 2, 3 \dots 13$). | Lacks ten-structuring automaticity. | "Lock the 8 in your mind. How many to 10? Two! Now add the rest." |
| Student places all 5 in the second frame, leaving first incomplete. | Does not recognize benchmark 10 constraint. | "A ten-frame must be full before you open a new one!" |

---

### Lesson 1.2: Commutative Property of Addition ($a + b = b + a$)
- **Standards:** CCSS.MATH.CONTENT.1.OA.B.3; TEKS 1.3.E.
- **Learning Objective:** Students construct two towers ($3+7$ and $7+3$) and use the exchange key `{{key:x⇄y}}` on the SC-6 to prove sum invariance.
- **Manipulatives:** Four-color counting tiles (blue and gold).
- **Tactile Warm-Up:** Build a tower of 3 blue tiles stacked onto 7 gold tiles. Turn the tower over.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "Enter `{{key:3}} {{key:ENTER}} {{key:7}}`. Register $Y$ has 3, Register $X$ has 7. Press `{{key:x⇄y}}`. What happened?"  
> **Students:** "They swapped places! 7 is on top, 3 is on bottom!"  
> **Teacher:** "Press `{{key:+}}`. What is the sum?"  
> **Students:** "10!"  
> **Teacher:** "Press `{{key:LASTX}} {{key:3}} {{key:+}}`. It is still 10! Flipping the order never changes the sum!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:3}} | 0 | 0 | 0 | 3 |
| {{key:ENTER}} | 0 | 0 | 3 | 3 |
| {{key:7}} | 0 | 0 | 3 | 7 |
| {{key:x⇄y}} | 0 | 0 | 7 | 3 |
| {{key:+}} | 0 | 0 | 0 | 10 |

#### Student Practice Problems
1. Test $4 + 8$ vs. $8 + 4$: `{{key:4}} {{key:ENTER}} {{key:8}} {{key:+}}` = 12; `{{key:8}} {{key:ENTER}} {{key:4}} {{key:+}}` = 12.
2. Test $2 + 9$ vs. $9 + 2$: both equal 11.
3. Test $6 + 5$ vs. $5 + 6$: both equal 11.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student assumes subtraction is also commutative ($7-3 = 3-7$). | Overgeneralizes additive symmetry to non-symmetric operations. | "Try `{{key:3}} {{key:ENTER}} {{key:7}} {{key:-}}` on your calculator. Do you get 4 or -4?" |

---

### Lesson 1.3: Number Bonds & Part-Whole Missing Addends
- **Standards:** CCSS.MATH.CONTENT.1.OA.D.8; TEKS 1.5.D.
- **Learning Objective:** Students solve missing addend problems ($? + 6 = 14$) by modeling whole-part subtraction on the SC-6.
- **Manipulatives:** 14 counting tiles from the Counting Studio; cup hiding an unknown number.
- **Tactile Warm-Up:** Place 14 tiles on desk. Teacher hides 6 under a cup. How many are visible? (8 tiles).

#### Verbatim Teacher Dialogue Script
> **Teacher:** "We started with a set of 14 tiles. I put some under this cup, and 6 are left on the desk. How do we find what is under the cup?"  
> **Student:** "Take away the 6 from the 14!"  
> **Teacher:** "Key it into the SC-6: Whole set first: `14 {{key:ENTER}}`. Visible part second: `{{key:6}}`. Take it away: `{{key:-}}`. What is in the lobby?"  
> **Students:** "8!"  
> **Teacher:** "Lift the cup! Count the tiles! Exactly 8!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 14 | 0 | 0 | 0 | 14 |
| {{key:ENTER}} | 0 | 0 | 14 | 14 |
| {{key:6}} | 0 | 0 | 14 | 6 |
| {{key:-}} | 0 | 0 | 0 | 8 |

#### Student Practice Problems
1. $? + 5 = 12$: `12 {{key:ENTER}} {{key:5}} {{key:-}}` = 7.
2. $? + 9 = 16$: `16 {{key:ENTER}} {{key:9}} {{key:-}}` = 7.
3. $? + 8 = 15$: `15 {{key:ENTER}} {{key:8}} {{key:-}}` = 7.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student adds $14 + 6$ to get 20. | Keywords trigger addition without spatial whole-part analysis. | "Can the hidden part be bigger than the whole train?" |

---

### Lesson 1.4: Place Value: Bundling 10 Ones into 1 Ten Rod
- **Standards:** CCSS.MATH.CONTENT.1.NBT.B.2; TEKS 1.2.B.
- **Learning Objective:** Students trade 10 unit cubes for 1 ten-rod and understand two-digit numbers as tens and ones.
- **Manipulatives:** Base-10 kit (`place_value_parts.scad`): unit cubes (1 cm) and ten-rods (10 cm).
- **Tactile Warm-Up:** Count out 13 single unit cubes. Lay them next to a ten-rod. Trade 10 cubes for 1 rod.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "Hold up 13 cubes. Lay 10 of them against one green rod. Do they have the exact same length?"  
> **Students:** "Yes, exactly the same!"  
> **Teacher:** "Put the 10 loose cubes back in the box and keep the green rod. Now what do you have on your desk?"  
> **Students:** "One ten and three ones!"  
> **Teacher:** "Type `13` on the SC-6. The digit 1 means 1 full rod of ten. The digit 3 means 3 loose ones!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 10 | 0 | 0 | 0 | 10 |
| {{key:ENTER}} | 0 | 0 | 10 | 10 |
| {{key:3}} | 0 | 0 | 10 | 3 |
| {{key:+}} | 0 | 0 | 0 | 13 |

#### Student Practice Problems
1. Model 2 tens and 5 ones: `20 {{key:ENTER}} {{key:5}} {{key:+}}` = 25.
2. Model 3 tens and 8 ones: `30 {{key:ENTER}} {{key:8}} {{key:+}}` = 38.
3. Model 4 tens and 0 ones: `40 {{key:ENTER}} {{key:0}} {{key:+}}` = 40.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student writes '103' for thirteen. | Writes numbers concatenating 10 and 3. | "The 1 ten already carries the 0 inside it until the 3 sits in its seat!" |

---

## Grade 2 Lesson Plans (Ages 7–8)

### Lesson 2.1: Skip-Counting Ladders with Superpower 1 (`{{key:REP}}`)
- **Standards:** CCSS.MATH.CONTENT.2.NBT.A.2; TEKS 2.2.C.
- **Learning Objective:** Students generate skip-counting sequences (twos, fives, tens) using continuous stack replication (`{{key:REP}}`).
- **Manipulatives:** Counting tiles from Counting Studio stacked in towers of 5.
- **Tactile Warm-Up:** Line up six towers of 5 tiles. Skip-count aloud: 5, 10, 15, 20, 25, 30.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "Today we teach our calculator to skip-count automatically using Superpower 1: `{{key:REP}}`! Type `{{key:5}}`. Now press blue `{{key:g}}` and `{{key:REP}}`. What did `{{key:REP}}` do?"  
> **Student (Leo):** "It copied 5 into all four elevator floors: T, Z, Y, and X!"  
> **Teacher:** "Now press `{{key:+}}` once. What is on Floor 1?"  
> **Students:** "10!"  
> **Teacher:** "Tap `{{key:+}}` again! And again!"  
> **Students:** "15! 20! 25! 30!"  
> **Teacher:** "Floor $T$ at the top of the elevator keeps dispensing a fresh 5 every time you add!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:5}} | 0 | 0 | 0 | 5 |
| {{key:REP}} | 5 | 5 | 5 | 5 |
| {{key:+}} | 5 | 5 | 5 | 10 |
| {{key:+}} | 5 | 5 | 5 | 15 |
| {{key:+}} | 5 | 5 | 5 | 20 |

#### Student Practice Problems
1. Skip-count by 2 up to 16: `{{key:2}} {{key:REP}} {{key:+}} ...`
2. Skip-count by 10 up to 70: `10 {{key:REP}} {{key:+}} ...`
3. Skip-count by 3 up to 21: `{{key:3}} {{key:REP}} {{key:+}} ...`

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student taps `{{key:ENTER}}` instead of `{{key:+}}`. | Confuses stack replication with arithmetic operation. | "`{{key:ENTER}}` lifts passengers up; `{{key:+}}` brings the top passenger down to combine!" |

---

### Lesson 2.2: Two-Digit Addition with Regrouping
- **Standards:** CCSS.MATH.CONTENT.2.NBT.B.5; TEKS 2.4.B.
- **Learning Objective:** Students solve $38 + 27$ by modeling tens and ones with Base-10 blocks and confirming the regrouped sum on the SC-6.
- **Manipulatives:** Base-10 blocks: 6 ten-rods, 15 unit cubes.
- **Tactile Warm-Up:** Build 38 (3 rods, 8 cubes) and 27 (2 rods, 7 cubes). Combine the cubes: 8 + 7 = 15. Trade 10 cubes for 1 rod.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "When we combined 8 loose cubes and 7 loose cubes, we got 15 cubes. What do we do when we have more than 10 cubes?"  
> **Students:** "Trade 10 cubes for 1 ten-rod!"  
> **Teacher:** "Now count your rods: 3 rods + 2 rods + 1 traded rod = 6 rods. And 5 loose cubes remain. That is 65! Let us confirm on SC-6: `38 {{key:ENTER}} 27 {{key:+}}`."  
> **Students:** "65!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 38 | 0 | 0 | 0 | 38 |
| {{key:ENTER}} | 0 | 0 | 38 | 38 |
| 27 | 0 | 0 | 38 | 27 |
| {{key:+}} | 0 | 0 | 0 | 65 |

#### Student Practice Problems
1. $46 + 28$: `46 {{key:ENTER}} 28 {{key:+}}` = 74.
2. $57 + 35$: `57 {{key:ENTER}} 35 {{key:+}}` = 92.
3. $19 + 64$: `19 {{key:ENTER}} 64 {{key:+}}` = 83.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student adds tens and ones separately on paper and writes '515' ($3+2=5, 8+7=15$). | Fails to carry regrouped ten into the tens column. | "15 cubes has a ten inside it! Trade the 10 cubes for a rod first!" |

---

### Lesson 2.3: Two-Digit Subtraction with Decomposition
- **Standards:** CCSS.MATH.CONTENT.2.NBT.B.7; TEKS 2.4.C.
- **Learning Objective:** Students solve $52 - 26$ by decomposing 1 ten-rod into 10 unit cubes.
- **Manipulatives:** Base-10 blocks (5 ten-rods, 2 unit cubes).
- **Tactile Warm-Up:** Set out 52. Try to remove 6 unit cubes. Observe that only 2 cubes are loose.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "We have 5 rods and 2 cubes. We need to take away 26, which means 2 rods and 6 cubes. Can we take 6 cubes from 2 cubes?"  
> **Students:** "No, not enough cubes!"  
> **Teacher:** "What can we break open?"  
> **Student (Maya):** "Unbundle one of the ten-rods into 10 loose cubes!"  
> **Teacher:** "Do it! Now you have 4 rods and 12 cubes. Take away 6 cubes: 6 remain. Take away 2 rods: 2 remain. Answer: 26! Key it in: `52 {{key:ENTER}} 26 {{key:-}}`."  
> **Students:** "26!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 52 | 0 | 0 | 0 | 52 |
| {{key:ENTER}} | 0 | 0 | 52 | 52 |
| 26 | 0 | 0 | 52 | 26 |
| {{key:-}} | 0 | 0 | 0 | 26 |

#### Student Practice Problems
1. $63 - 27$: `63 {{key:ENTER}} 27 {{key:-}}` = 36.
2. $71 - 38$: `71 {{key:ENTER}} 38 {{key:-}}` = 33.
3. $80 - 45$: `80 {{key:ENTER}} 45 {{key:-}}` = 35.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student subtracts smaller from larger digit on paper ($6-2=4$, writing 34). | Avoidance of regrouping by inverting digit roles. | "The top number is what you have in the bank. You cannot steal from the bottom number!" |

---

### Lesson 2.4: Even and Odd Numbers via Equal Pairing & `{{key:÷R}}`
- **Standards:** CCSS.MATH.CONTENT.2.OA.C.3; TEKS 2.7.A.
- **Learning Objective:** Students determine if a number is even or odd by pairing counters and checking for remainder 0 vs. 1 using `{{key:÷R}}`.
- **Manipulatives:** 15 counters per student pair.
- **Tactile Warm-Up:** Pair up 11 counters in two parallel rows. Does one counter stick out alone?

#### Verbatim Teacher Dialogue Script
> **Teacher:** "Line up 11 counters in pairs of two. Is there a leftover counter without a partner?"  
> **Students:** "Yes, one counter is lonely!"  
> **Teacher:** "That means 11 is an *odd* number! Let us test with Superpower 2: `{{key:÷R}}`. Type `11 {{key:ENTER}} {{key:2}} {{key:÷R}}`."  
> **Teacher:** "Register $X$ shows 5 pairs. Now press `{{key:x⇄y}}`. What is in Register $Y$?"  
> **Students:** "1! The remainder is 1!"  
> **Teacher:** "Any number with a remainder of 1 when divided by 2 is ODD! If the remainder is 0, it is EVEN!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 11 | 0 | 0 | 0 | 11 |
| {{key:ENTER}} | 0 | 0 | 11 | 11 |
| {{key:2}} | 0 | 0 | 11 | 2 |
| {{key:÷R}} | 0 | 0 | 1 (Rem) | 5 (Quot) |
| {{key:x⇄y}} | 0 | 0 | 5 (Quot) | 1 (Rem) |

#### Student Practice Problems
1. Test 14: `14 {{key:ENTER}} {{key:2}} {{key:÷R}} {{key:x⇄y}}` $\to$ Remainder 0 (EVEN).
2. Test 17: `17 {{key:ENTER}} {{key:2}} {{key:÷R}} {{key:x⇄y}}` $\to$ Remainder 1 (ODD).
3. Test 20: `20 {{key:ENTER}} {{key:2}} {{key:÷R}} {{key:x⇄y}}` $\to$ Remainder 0 (EVEN).

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student looks only at first digit of two-digit number (e.g. thinking 16 is odd because 1 is odd). | Ignores place value significance of ones digit. | "Look only at the ones place! Can 6 ones be shared equally?" |

---

## Grade 3 Lesson Plans (Ages 8–9)

### Lesson 3.1: Arrays, Equal Groups & Area with `{{key:RECT}}`
- **Standards:** CCSS.MATH.CONTENT.3.OA.A.1, 3.MD.C.7; TEKS 3.4.D, 3.6.C.
- **Learning Objective:** Students construct a $6 \times 4$ array, compute area using `{{key:RECT}}`, and rotate it $90^\circ$ to demonstrate commutativity ($6 \times 4 = 4 \times 6 = 24$).
- **Manipulatives:** Four-Color Counting Studio (144-tile kit in 13U Gridfinity box), Gridfinity 4x4 coordinate baseplate.
- **Tactile Warm-Up:** Build a rectangle 6 tiles long and 4 tiles wide using White counting tiles on the baseplate.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "How many columns of 4 tiles did you make?"  
> **Students:** "6 columns!"  
> **Teacher:** "Count all the tiles covering the rectangle. How many?"  
> **Students:** "24 tiles!"  
> **Teacher:** "In geometry, the surface covered by tiles is called *area*. On the SC-6, we have a dedicated geometry key: `{{key:RECT}}`. Type `{{key:6}} {{key:ENTER}} {{key:4}}`."  
> **Teacher:** "Now press yellow `{{key:f}}` and `{{key:RECT}}`. What is the area?"  
> **Students:** "24!"  
> **Teacher:** "Turn the tray sideways. Now it is 4 columns of 6. Test: `{{key:4}} {{key:ENTER}} {{key:6}} {{key:RECT}}`. Still 24!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:6}} | 0 | 0 | 0 | 6 |
| {{key:ENTER}} | 0 | 0 | 6 | 6 |
| {{key:4}} | 0 | 0 | 6 | 4 |
| {{key:RECT}} | 0 | 0 | 0 | 24 |

#### Student Practice Problems
1. $7 \times 5$ rug: `{{key:7}} {{key:ENTER}} {{key:5}} {{key:RECT}}` = 35 square units.
2. $8 \times 3$ garden bed: `{{key:8}} {{key:ENTER}} {{key:3}} {{key:RECT}}` = 24 square units.
3. $9 \times 4$ patio: `{{key:9}} {{key:ENTER}} {{key:4}} {{key:RECT}}` = 36 square units (built with all 36 Radiant Red+Gold tiles!).

#### Classroom Station Partner Game: "Capture the Rectangle"
* **Materials:** Four-Color Counting Tiles (Player 1 in Archival White, Player 2 in Cobalt Red+Blue Silk, with Player 3 in Radiant Red+Gold Silk and Player 4 in Slate Blue-Gray PLA), SC-6 Calculator, 2 Polyhedral Dice (or roll via `{{key:🎲}}`).
* **Gameplay:** Player 1 rolls two factors (e.g., 5 and 4). Player 1 calculates area on the SC-6 (`5 {{key:ENTER}} 4 {{key:×}} = 20`), assembles a $5 \times 4$ rectangle in their color, and claims their territory on the table. Player 2 rolls, computes, assembles, and places their rectangle adjacent to Player 1.
* **The Four-Color Challenge Rule:** Placed rectangles of the same color cannot touch along a side! The SC-6 calculator serves as the referee: if a challenged player computes an area incorrectly, they forfeit their turn.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student confuses perimeter with area. | Conflates boundary fence with surface tiles. | "Trace the fence with your finger—that is perimeter. Lay your hand over the blocks—that is area!" |

---

### Lesson 3.2: Division as Fair Sharing vs. Grouping (`{{key:÷R}}`)
- **Standards:** CCSS.MATH.CONTENT.3.OA.A.2; TEKS 3.4.H.
- **Learning Objective:** Students model dividing 23 tiles among 4 Gridfinity holding bays, finding quotient 5 and remainder 3 using `{{key:÷R}}`.
- **Manipulatives:** 23 Four-Color Counting Tiles, 4 Gridfinity sorting trays/bays.
- **Tactile Warm-Up:** Deal 23 counting tiles one by one into the 4 trays until no more equal rounds can be dealt.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "How many cookies ended up in each cup?"  
> **Students:** "5 cookies!"  
> **Teacher:** "How many cookies are left on the table that cannot be shared equally?"  
> **Students:** "3 cookies!"  
> **Teacher:** "Let us verify with the SC-6 quotient and remainder engine. Dividend first: `23 {{key:ENTER}}`. Divisor second: `{{key:4}}`. Superpower 2: {{key:÷R}}. What is in Register $X$?"  
> **Students:** "5! The quotient!"  
> **Teacher:** "Press `{{key:x⇄y}}`. What is in Register $Y$?"  
> **Students:** "3! The remainder!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 23 | 0 | 0 | 0 | 23 |
| {{key:ENTER}} | 0 | 0 | 23 | 23 |
| {{key:4}} | 0 | 0 | 23 | 4 |
| {{key:÷R}} | 0 | 0 | 3 (Rem) | 5 (Quot) |
| {{key:x⇄y}} | 0 | 0 | 5 (Quot) | 3 (Rem) |

#### Student Practice Problems
1. 19 markers shared among 3 pencil cases: `19 {{key:ENTER}} {{key:3}} {{key:÷R}}` $\to$ $Q=6, R=1$.
2. 31 apples packed into bags of 6: `31 {{key:ENTER}} {{key:6}} {{key:÷R}}` $\to$ $Q=5, R=1$.
3. 35 tiles partitioned into teams of 4: `35 {{key:ENTER}} {{key:4}} {{key:÷R}}` $\to$ $Q=8, R=3$.

#### Classroom Station Partner Game: "Remainder Race to Bank"
* **Materials:** 36 Counting Tiles, 1 Die, SC-6 Calculator.
* **Gameplay:** Players start with a shared pool of 36 tiles. Player 1 rolls a die (e.g., 5) and keys `36 {{key:ENTER}} 5 {{key:÷R}}`. Line $X$ displays quotient 7 (which returns to the supply depot), and line $Y$ (`{{key:x⇄y}}`) displays remainder 1! Player 1 takes the 1 remainder tile into their personal bank.
* **Winning:** Players alternate turns with the remaining tiles. The player who banks the most remainder tiles wins the round.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student writes $23 \div 4 = 5.75$ and doesn't know what to do with the leftover cookies. | Standard decimal division obscures integer remainder context. | "Can you hand a guest $0.75$ of an unwrapped cookie at a party? Give them 5 cookies and keep 3 in the box!" |

---

### Lesson 3.3: Introduction to Unit Fractions with Fraction Studio
- **Standards:** CCSS.MATH.CONTENT.3.NF.A.1; TEKS 3.3.A.
- **Learning Objective:** Students compare physical fraction towers ($\frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \frac{1}{6}, \frac{1}{8}$) against the $84.0\text{ mm}$ whole tower and understand that larger denominators produce smaller unit pieces.
- **Manipulatives:** Fraction Studio tower set (`fraction_studio_parts.scad`).
- **Tactile Warm-Up:** Place the 1-Whole tower ($84\text{ mm}$) on desk. Stack two $\frac{1}{2}$ blocks next to it. Observe equal heights.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "Hold up a $\frac{1}{2}$ block and a $\frac{1}{8}$ block. Which block is taller?"  
> **Students:** "The $\frac{1}{2}$ block is much taller!"  
> **Teacher:** "Why is $\frac{1}{8}$ smaller if 8 is a bigger number than 2?"  
> **Student (David):** "Because you had to cut the same candy bar into 8 pieces instead of just 2 pieces! Each slice is tiny!"  
> **Teacher:** "Brilliant! The denominator tells us how many equal pieces the whole was cut into. Enter $\frac{1}{2}$ on the SC-6: `{{key:.}} 1 {{key:.}} 2 {{key:ENTER}}`. Enter $\frac{1}{8}$: `{{key:.}} 1 {{key:.}} 8`. Now press `{{key:-}}`. The difference is positive: $\frac{1}{2}$ is $\frac{3}{8}$ larger!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:.}} 1 {{key:.}} 2` | 0 | 0 | 0 | 1/2 |
| {{key:ENTER}} | 0 | 0 | 1/2 | 1/2 |
| `{{key:.}} 1 {{key:.}} 8` | 0 | 0 | 1/2 | 1/8 |
| {{key:-}} | 0 | 0 | 0 | 3/8 |

#### Student Practice Problems
1. Show that three $\frac{1}{3}$ blocks equal 1 whole: `{{key:.}} 1 {{key:.}} 3 {{key:ENTER}} {{key:3}} {{key:×}}` = 1.
2. Compare $\frac{1}{4}$ and $\frac{1}{2}$: `{{key:.}} 1 {{key:.}} 2 {{key:ENTER}} {{key:.}} 1 {{key:.}} 4 {{key:-}}` = $\frac{1}{4}$.
3. Show that four $\frac{1}{8}$ blocks equal $\frac{1}{2}$: `{{key:.}} 1 {{key:.}} 8 {{key:ENTER}} {{key:4}} {{key:×}}` = $\frac{1}{2}$.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student believes $\frac{1}{8} > \frac{1}{4}$ because $8 > 4$. | Whole-number bias applied to denominators. | "Place the physical $\frac{1}{8}$ tower next to the $\frac{1}{4}$ tower. Which one touches the ceiling first?" |

---

### Lesson 3.4: Perimeter of Polygons vs. Area using `{{key:Σ+}}`
- **Standards:** CCSS.MATH.CONTENT.3.MD.D.8; TEKS 3.7.B.
- **Learning Objective:** Students find the perimeter of an irregular 5-sided polygon by accumulating sides with `{{key:Σ+}}`, distinguishing it from internal area.
- **Manipulatives:** Geoboard with rubber bands (`counting_tiles_parts.scad`), ruler.
- **Tactile Warm-Up:** Stretch a rubber band around pins at $(0,0), (6,0), (6,4), (3,7), (0,4)$ to form a pentagon.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "To find the perimeter, we walk all the way around the outer boundary fence. Let us add the sides using our SC-6 statistical accumulator key `{{key:Σ+}}`! First, clear memory: {{key:CLΣ}}."  
> **Teacher:** "Side 1 is 6 cm: `{{key:6}} {{key:Σ+}}`. Side 2 is 4 cm: `{{key:4}} {{key:Σ+}}`. Side 3 is 4.2 cm: `4.2 {{key:Σ+}}`. Side 4 is 4.2 cm: `4.2 {{key:Σ+}}`. Side 5 is 4 cm: `{{key:4}} {{key:Σ+}}`."  
> **Teacher:** "How many sides did we measure? $n = 5$! Now press `{{key:Σx}}`. What is the total perimeter?"  
> **Students:** "22.4 centimeters!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:CLΣ}} | 0 | 0 | 0 | 0 |
| {{key:6}} {{key:Σ+}} | 0 | 0 | 0 | n = 1 |
| {{key:4}} {{key:Σ+}} | 0 | 0 | 0 | n = 2 |
| `4.2` {{key:Σ+}} | 0 | 0 | 0 | n = 3 |
| `4.2` {{key:Σ+}} | 0 | 0 | 0 | n = 4 |
| {{key:4}} {{key:Σ+}} | 0 | 0 | 0 | n = 5 |
| {{key:Σx}} | 0 | 0 | 0 | 22.4 |

#### Student Practice Problems
1. Triangle with sides 5, 7, 8: `{{key:CLΣ}} {{key:5}} {{key:Σ+}} {{key:7}} {{key:Σ+}} {{key:8}} {{key:Σ+}} {{key:Σx}}` = 20.
2. Rectangle perimeter ($8 + 5 + 8 + 5$): `{{key:Σx}}` = 26.
3. Hexagon with sides 3, 3, 4, 4, 5, 5: `{{key:Σx}}` = 24.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student forgets to clear statistical memory before starting problem 2. | Persistent accumulator contamination. | "Always check $n$. If $n$ is not zero, press {{key:CLΣ}} before walking your fence!" |

---

## Grade 4 Lesson Plans (Ages 9–10)

### Lesson 4.1: Long Division with Remainders (`{{key:÷R}}`)
- **Standards:** CCSS.MATH.CONTENT.4.OA.A.3; TEKS 4.4.F.
- **Learning Objective:** Students solve a multi-step hiking trail provisioning problem ($89\text{ oz}$ water distributed into $16\text{ oz}$ flasks) using `{{key:÷R}}`.
- **Manipulatives:** Graduated cylinders, counting tile measuring sticks (`UNIF-01`).
- **Tactile Warm-Up:** Assemble an 89-unit bar using counting tiles. Break off 16-unit chunks. Count full chunks and leftovers.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "We have 89 fluid ounces of water. Each water bottle holds 16 fluid ounces. How many full bottles can we pack, and how many ounces are left over?"  
> **Student (Maya):** "Type `89 {{key:ENTER}} 16 {{key:÷R}}`!"  
> **Teacher:** "What is on your screen?"  
> **Students:** "5!"  
> **Teacher:** "That is 5 full flasks! Now swap registers: press `{{key:x⇄y}}`. What is in Register $Y$?"  
> **Students:** "9! 9 ounces left over!"  
> **Teacher:** "Check your answer: 5 bottles times 16 oz is 80 oz, plus 9 oz equals 89 oz! Perfect!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 89 | 0 | 0 | 0 | 89 |
| {{key:ENTER}} | 0 | 0 | 89 | 89 |
| 16 | 0 | 0 | 89 | 16 |
| {{key:÷R}} | 0 | 0 | 9 (Rem) | 5 (Quot) |
| {{key:x⇄y}} | 0 | 0 | 5 (Quot) | 9 (Rem) |

#### Student Practice Problems
1. 145 campers into cabins of 12: `145 {{key:ENTER}} 12 {{key:÷R}}` $\to$ $Q=12$ cabins, $R=1$ camper.
2. 250 eggs packed in cartons of 12: `250 {{key:ENTER}} 12 {{key:÷R}}` $\to$ $Q=20$ cartons, $R=10$ eggs.
3. 500 pencils in packs of 24: `500 {{key:ENTER}} 24 {{key:÷R}}` $\to$ $Q=20$ packs, $R=20$ pencils.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student interprets remainder 9 as $0.9$ bottles. | Confuses integer discrete leftovers with decimal fraction. | "Is that 9 tenths of a bottle, or 9 whole ounces in the bottom of the pot? Remember the units!" |

---

### Lesson 4.2: Equivalent Fractions & Simplification (`{{key:SIMP}}`)
- **Standards:** CCSS.MATH.CONTENT.4.NF.A.1; TEKS 4.3.C.
- **Learning Objective:** Students build equivalent fraction models ($\frac{6}{8} = \frac{3}{4}$) and reduce them on the SC-6 using Superpower 3 (`{{key:SIMP}}`).
- **Manipulatives:** Fraction Studio towers ($\frac{1}{8}$ and $\frac{1}{4}$ blocks).
- **Tactile Warm-Up:** Line up six $\frac{1}{8}$ blocks in the channel. Find which group of $\frac{1}{4}$ blocks matches the exact length.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "How many $\frac{1}{4}$ blocks match six $\frac{1}{8}$ blocks?"  
> **Students:** "Three $\frac{1}{4}$ blocks!"  
> **Teacher:** "So $\frac{6}{8}$ is equivalent to $\frac{3}{4}$. Now let us watch the SC-6 simplify it step-by-step. Enter six-eighths: `{{key:.}} 6 {{key:.}} 8 {{key:ENTER}}`. Press blue `{{key:g}}` and `{{key:SIMP}}`. What does the screen show?"  
> **Students:** "`3/4`!"  
> **Teacher:** "What factor did the calculator divide out from top and bottom?"  
> **Student (Leo):** "It divided both numbers by 2!"  
> **Teacher:** "Now press {{key:SIMP}} again. What does it say?"  
> **Students:** "`LOWEST TERMS`! It cannot be simplified any further because 3 is prime!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:.}} 6 {{key:.}} 8` | 0 | 0 | 0 | 6/8 |
| {{key:ENTER}} | 0 | 0 | 6/8 | 6/8 |
| {{key:SIMP}} | 0 | 0 | 6/8 | 3/4 |
| {{key:SIMP}} | 0 | 0 | 6/8 | 3/4 (LOWEST) |

#### Student Practice Problems
1. Simplify $\frac{8}{12}$: `{{key:.}} 8 {{key:.}} 12 {{key:ENTER}} {{key:SIMP}}` = $\frac{2}{3}$.
2. Simplify $\frac{10}{25}$: `{{key:.}} 10 {{key:.}} 25 {{key:ENTER}} {{key:SIMP}}` = $\frac{2}{5}$.
3. Simplify $\frac{18}{24}$: `{{key:.}} 18 {{key:.}} 24 {{key:ENTER}} {{key:SIMP}}` = $\frac{3}{4}$.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student divides numerator by 2 and denominator by 3 ($\frac{6 \div 2}{8 \div 4}$). | Fails to recognize that scaling requires multiplying or dividing by $\frac{n}{n} = 1$. | "You must treat the top and bottom with equal justice! Divide both by the exact same number!" |

---

### Lesson 4.3: Adding & Subtracting Fractions with Unlike Denominators
- **Standards:** CCSS.MATH.CONTENT.4.NF.B.3; TEKS 4.3.E.
- **Learning Objective:** Students solve $\frac{1}{2} + \frac{1}{4}$ and $\frac{2}{3} - \frac{1}{6}$ using Fraction Studio blocks and SC-6 fraction arithmetic.
- **Manipulatives:** Fraction Studio towers.
- **Tactile Warm-Up:** Put one $\frac{1}{2}$ block and one $\frac{1}{4}$ block end-to-end. Measure total length with $\frac{1}{4}$ blocks.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "How many fourths fit across $\frac{1}{2} + \frac{1}{4}$?"  
> **Students:** "Three fourths!"  
> **Teacher:** "Enter it on the SC-6: `{{key:.}} 1 {{key:.}} 2 {{key:ENTER}} {{key:.}} 1 {{key:.}} 4 {{key:+}}`. What is the result?"  
> **Students:** "`3/4`!"  
> **Teacher:** "Now try a subtraction: $\frac{5}{6} - \frac{1}{3}$. Key: `{{key:.}} 5 {{key:.}} 6 {{key:ENTER}} {{key:.}} 1 {{key:.}} 3 {{key:-}}`. What do you get?"  
> **Students:** "`1/2`!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:.}} 1 {{key:.}} 2` | 0 | 0 | 0 | 1/2 |
| {{key:ENTER}} | 0 | 0 | 1/2 | 1/2 |
| `{{key:.}} 1 {{key:.}} 4` | 0 | 0 | 1/2 | 1/4 |
| {{key:+}} | 0 | 0 | 0 | 3/4 |

#### Student Practice Problems
1. $\frac{1}{3} + \frac{1}{6}$: `{{key:.}} 1 {{key:.}} 3 {{key:ENTER}} {{key:.}} 1 {{key:.}} 6 {{key:+}}` = $\frac{1}{2}$.
2. $\frac{3}{4} - \frac{1}{8}$: `{{key:.}} 3 {{key:.}} 4 {{key:ENTER}} {{key:.}} 1 {{key:.}} 8 {{key:-}}` = $\frac{5}{8}$.
3. $\frac{2}{5} + \frac{3}{10}$: `{{key:.}} 2 {{key:.}} 5 {{key:ENTER}} {{key:.}} 3 {{key:.}} 10 {{key:+}}` = $\frac{7}{10}$.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student adds across numerators and denominators ($\frac{1}{2} + \frac{1}{4} = \frac{2}{6}$). | Treats numerator and denominator as independent whole numbers. | "Look at your blocks! Is $\frac{2}{6}$ bigger than $\frac{1}{2}$? No! You cannot add pieces of different sizes until they share a common name!" |

---

### Lesson 4.4: Angles & Rotations with the $360^\circ$ Volvelle Protractor
- **Standards:** CCSS.MATH.CONTENT.4.MD.C.6; TEKS 4.7.C.
- **Learning Objective:** Students measure acute, right, and obtuse angles using the $360^\circ$ Volvelle (`sc6_volvelle_protractor.scad`) and calculate supplementary and complementary angles.
- **Manipulatives:** Two-disc rotating Volvelle protractor, pattern blocks.
- **Tactile Warm-Up:** Align Volvelle pointer to $0^\circ$. Rotate top disc to match the corner of an orange square ($90^\circ$).

#### Verbatim Teacher Dialogue Script
> **Teacher:** "Rotate your Volvelle to match the yellow hexagon angle. What degree reading does the red cursor line up with?"  
> **Students:** "120 degrees!"  
> **Teacher:** "If two angles sit on a straight line, their sum is $180^\circ$ (supplementary). How many degrees are left to make a straight line? Calculate on SC-6: `180 {{key:ENTER}} 120 {{key:-}}`."  
> **Students:** "60 degrees!"  
> **Teacher:** "Check with your green triangle corner: it fits the $60^\circ$ gap perfectly!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 180 | 0 | 0 | 0 | 180 |
| {{key:ENTER}} | 0 | 0 | 180 | 180 |
| 120 | 0 | 0 | 180 | 120 |
| {{key:-}} | 0 | 0 | 0 | 60 |

#### Student Practice Problems
1. Complement of $35^\circ$ ($90 - 35$): `{{key:9}} {{key:0}} {{key:ENTER}} {{key:3}} {{key:5}} {{key:-}}` = $55^\circ$.
2. Supplement of $45^\circ$ ($180 - 45$): `{{key:1}} {{key:8}} {{key:0}} {{key:ENTER}} {{key:4}} {{key:5}} {{key:-}}` = $135^\circ$.
3. Sum of four angles meeting at a point ($90 + 120 + 80 + ?$): `{{key:3}} {{key:6}} {{key:0}} {{key:ENTER}} ...` = $70^\circ$.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student reads outer scale instead of inner scale on standard protractor, reporting $60^\circ$ for an obtuse angle. | Dual-scale confusion on semi-circular protractors. | "Look at the corner: is it sharper than a book corner or wider than a book corner? Obtuse must be $> 90^\circ$!" |

---

## Grade 5 Lesson Plans (Ages 10–11)

### Lesson 5.1: Volume & Total Surface Area of Prisms via `{{key:Σ+}}`
- **Standards:** CCSS.MATH.CONTENT.5.MD.C.5, 6.G.A.4; TEKS 5.6.B.
- **Learning Objective:** Students calculate the volume and total surface area of a $5 \times 4 \times 3\text{ cm}$ wooden prism using the statistical accumulator `{{key:Σ+}}` without scratch paper.
- **Manipulatives:** Wooden prism ($5 \times 4 \times 3\text{ cm}$), digital caliper.
- **Tactile Warm-Up:** Count the faces on the prism. Notice that opposite faces are identical twins (3 pairs: top/bottom, front/back, left/right).

#### Verbatim Teacher Dialogue Script
> **Teacher:** "First, let us calculate volume: Length $\times$ Width $\times$ Height. Key: `{{key:5}} {{key:ENTER}} {{key:4}} {{key:×}} {{key:3}} {{key:×}}`. Volume is $60\text{ cm}^3$."  
> **Teacher:** "Now, total surface area! We must add the areas of all 6 faces. We will use the SC-6 statistical accumulator memory: `{{key:Σ+}}`! Clear memory first: {{key:CLΣ}}."  
> **Teacher:** "Pair 1 (Top/Bottom, $5 \times 4$, two faces): `{{key:5}} {{key:ENTER}} {{key:4}} {{key:×}} {{key:2}} {{key:×}}` $\to$ 40. Press `{{key:Σ+}}`!"  
> **Teacher:** "Pair 2 (Front/Back, $5 \times 3$, two faces): `{{key:5}} {{key:ENTER}} {{key:3}} {{key:×}} {{key:2}} {{key:×}}` $\to$ 30. Press `{{key:Σ+}}`!"  
> **Teacher:** "Pair 3 (Left/Right, $4 \times 3$, two faces): `{{key:4}} {{key:ENTER}} {{key:3}} {{key:×}} {{key:2}} {{key:×}}` $\to$ 24. Press `{{key:Σ+}}`!"  
> **Teacher:** "Screen shows $n = 3$. Now press yellow `{{key:f}}` and `{{key:Σx}}`. What is the total surface area?"  
> **Students:** "94 square centimeters!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:CLΣ}} | 0 | 0 | 0 | 0 |
| `{{key:5}} {{key:ENTER}} {{key:4}} {{key:×}} {{key:2}} {{key:×}}` | 0 | 0 | 0 | 40 |
| {{key:Σ+}} | 0 | 0 | 0 | n = 1 |
| `{{key:5}} {{key:ENTER}} {{key:3}} {{key:×}} {{key:2}} {{key:×}}` | 0 | 0 | 0 | 30 |
| {{key:Σ+}} | 0 | 0 | 0 | n = 2 |
| `{{key:4}} {{key:ENTER}} {{key:3}} {{key:×}} {{key:2}} {{key:×}}` | 0 | 0 | 0 | 24 |
| {{key:Σ+}} | 0 | 0 | 0 | n = 3 |
| {{key:Σx}} | 0 | 0 | 0 | 94 |

#### Student Practice Problems
1. Box measuring $6 \times 3 \times 2\text{ cm}$: Volume = $36\text{ cm}^3$, Surface Area = $72\text{ cm}^2$.
2. Cube measuring $4 \times 4 \times 4\text{ cm}$: Volume = $64\text{ cm}^3$, Surface Area = $96\text{ cm}^2$.
3. Storage crate $10 \times 8 \times 5\text{ cm}$: Volume = $400\text{ cm}^3$, Surface Area = $340\text{ cm}^2$.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student calculates only 3 faces and forgets to multiply by 2. | Confuses the three unique face orientations with total face count. | "Every room has a ceiling AND a floor. Multiply each face pair by 2!" |

---

### Lesson 5.2: Fraction Multiplication & Division via Reciprocal (`{{key:1/x}}`)
- **Standards:** CCSS.MATH.CONTENT.5.NF.B.4, 5.NF.B.7; TEKS 5.3.I, 5.3.L.
- **Learning Objective:** Students model multiplying $\frac{2}{3} \times \frac{3}{4}$ using area grid overlays, and divide fractions by multiplying by the reciprocal using `{{key:1/x}}`.
- **Manipulatives:** Transparent grid overlay sheets, dry-erase markers.
- **Tactile Warm-Up:** Shade $\frac{3}{4}$ of a square vertically. Shade $\frac{2}{3}$ horizontally. Count overlapping squares: $\frac{6}{12} = \frac{1}{2}$.

#### Verbatim Teacher Dialogue Script
> **Teacher:** "Enter $\frac{2}{3} \times \frac{3}{4}$ on SC-6: `{{key:.}} 2 {{key:.}} 3 {{key:ENTER}} {{key:.}} 3 {{key:.}} 4 {{key:×}}`. What is the result?"  
> **Students:** "`1/2`!"  
> **Teacher:** "Now let us divide: $\frac{3}{4} \div \frac{2}{5}$. Dividing by a fraction is the same as multiplying by its flipped upside-down twin—the reciprocal! Enter $\frac{3}{4}$: `{{key:.}} 3 {{key:.}} 4 {{key:ENTER}}`. Enter $\frac{2}{5}$: `{{key:.}} 2 {{key:.}} 5`. Now tap yellow `{{key:f}}` and reciprocal `{{key:1/x}}`. What did $\frac{2}{5}$ turn into?"  
> **Students:** "`5/2`!"  
> **Teacher:** "Now press `{{key:×}}`! What is the final quotient?"  
> **Students:** "`15/8` or $1\frac{7}{8}$!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| `{{key:.}} 3 {{key:.}} 4` | 0 | 0 | 0 | 3/4 |
| {{key:ENTER}} | 0 | 0 | 3/4 | 3/4 |
| `{{key:.}} 2 {{key:.}} 5` | 0 | 0 | 3/4 | 2/5 |
| {{key:1/x}} | 0 | 0 | 3/4 | 5/2 |
| {{key:×}} | 0 | 0 | 0 | 15/8 |

#### Student Practice Problems
1. $\frac{4}{5} \times \frac{5}{8}$: `{{key:.}} 4 {{key:.}} 5 {{key:ENTER}} {{key:.}} 5 {{key:.}} 8 {{key:×}}` = $\frac{1}{2}$.
2. $\frac{1}{2} \div \frac{1}{6}$: `{{key:.}} 1 {{key:.}} 2 {{key:ENTER}} {{key:.}} 1 {{key:.}} 6 {{key:1/x}} {{key:×}}` = 3.
3. $\frac{2}{3} \div \frac{4}{9}$: `{{key:.}} 2 {{key:.}} 3 {{key:ENTER}} {{key:.}} 4 {{key:.}} 9 {{key:1/x}} {{key:×}}` = $\frac{3}{2} = 1\frac{1}{2}$.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student reciprocates the first fraction instead of the second fraction ($\frac{4}{3} \times \frac{2}{5}$). | Rote mnemonic "keep-change-flip" memorized without structural meaning. | "The divisor (the second passenger) is the one doing the dividing. That is the one that flips!" |

---

### Lesson 5.3: Order of Operations without Parentheses (Stack Architecture)
- **Standards:** CCSS.MATH.CONTENT.5.OA.A.1; TEKS 5.4.F.
- **Learning Objective:** Students evaluate complex multi-step expressions like $(8 + 4) \times (9 - 3)$ and $15 + 4 \times (12 - 7)$ using the 4-register RPN stack with zero parentheses keys.
- **Manipulatives:** Expression cards, 4-story physical elevator cardboard model.
- **Tactile Warm-Up:** Analyze $(8 + 4) \times (9 - 3)$. What must be solved first? The two parenthetical groups!

#### Verbatim Teacher Dialogue Script
> **Teacher:** "On ordinary calculators, students get lost in tangled parentheses like `( ( 8 + 4 ) * ( 9 - 3 ) )`. If you forget one parenthesis, you get a syntax error. On the SC-6 RPN elevator, we solve inside-out naturally! Evaluate group 1: `{{key:8}} {{key:ENTER}} {{key:4}} {{key:+}}` $\to$ 12. Keep it in the elevator! Now evaluate group 2:`{{key:9}} {{key:ENTER}} {{key:3}} {{key:-}}` $\to$ 6. Look at your screen: Register $Y$ holds 12, Register $X$ holds 6. What operation combines them?"  
> **Students:** "Multiplication! Press `{{key:×}}`!"  
> **Teacher:** "Tap `{{key:×}}`. What is the answer?"  
> **Students:** "72!"  
> **Teacher:** "Zero parentheses keys used! The stack holds intermediate answers automatically!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:8}} {{key:ENTER}} {{key:4}} | 0 | 0 | 8 | 4 |
| {{key:+}} | 0 | 0 | 0 | 12 |
| {{key:9}} | 0 | 0 | 12 | 9 |
| {{key:ENTER}} | 0 | 12 | 9 | 9 |
| {{key:3}} | 0 | 12 | 9 | 3 |
| {{key:-}} | 0 | 0 | 12 | 6 |
| {{key:×}} | 0 | 0 | 0 | 72 |

#### Student Practice Problems
1. $(14 + 6) \div (7 - 2)$: `14 {{key:ENTER}} {{key:6}} {{key:+}} {{key:7}} {{key:ENTER}} {{key:2}} {{key:-}} {{key:÷}}` = 4.
2. $50 - (4 \times 8) + 6$: `50 {{key:ENTER}} {{key:4}} {{key:ENTER}} {{key:8}} {{key:×}} {{key:-}} {{key:6}} {{key:+}}` = 24.
3. $(3 + 5)^2 - 10$: `{{key:3}} {{key:ENTER}} {{key:5}} {{key:+}} {{key:x²}} 10 {{key:-}}` = 54.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student keys in numbers sequentially from left to right without respecting operator precedence. | Linear reading habit overriding algebraic hierarchy. | "RPN processes operators from the inside out. Build your building blocks first, then combine them!" |

---

## Grade 6 Lesson Plans (Ages 11–12)

### Lesson 6.1: Negative Numbers, Zero Pairs & `{{key:+/-}}`
- **Standards:** CCSS.MATH.CONTENT.6.NS.C.5, 6.NS.C.6; TEKS 6.2.B.
- **Learning Objective:** Students model integer addition and subtraction using two-color counters (yellow $= +1$, red $= -1$), cancel zero pairs, and verify signed arithmetic on SC-6 using `{{key:+/-}}`.
- **Manipulatives:** 30 two-color counters (15 yellow, 15 red).
- **Tactile Warm-Up:** Place 7 yellow counters ($+7$) and 4 red counters ($-4$) on desk. Pair them up. What is left? (+3).

#### Verbatim Teacher Dialogue Script
> **Teacher:** "What happens when $+1$ meets $-1$?"  
> **Students:** "They make a zero pair and cancel out!"  
> **Teacher:** "Now let us model $-8 + 5$. Lay out 8 red counters and 5 yellow counters. Pair up 5 zero pairs. How many counters remain?"  
> **Students:** "3 red counters! So the answer is $-3$!"  
> **Teacher:** "Now key it into the SC-6. Type `{{key:8}}`. To make it negative, press the sign toggle key `{{key:+/-}}`. Look at the screen—a minus sign appears before the 8. Press `{{key:ENTER}}`. Now type `{{key:5}}` and press `{{key:+}}`. What is the result?"  
> **Students:** "$-3$!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| {{key:8}} | 0 | 0 | 0 | 8 |
| {{key:+/-}} | 0 | 0 | 0 | -8 |
| {{key:ENTER}} | 0 | 0 | -8 | -8 |
| {{key:5}} | 0 | 0 | -8 | 5 |
| {{key:+}} | 0 | 0 | 0 | -3 |

#### Student Practice Problems
1. Solve $-12 + (-7)$: `{{key:1}} {{key:2}} {{key:+/-}} {{key:ENTER}} {{key:7}} {{key:+/-}} {{key:+}}` = $-19$.
2. Solve $15 - (-6)$: `{{key:1}} {{key:5}} {{key:ENTER}} {{key:6}} {{key:+/-}} {{key:-}}` = 21.
3. Solve $(-4) \times (-8)$: `{{key:4}} {{key:+/-}} {{key:ENTER}} {{key:8}} {{key:+/-}} {{key:×}}` = 32.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student presses the operation key `{{key:-}}` instead of sign toggle key `{{key:+/-}}`. | Conflates binary subtraction operator with unary negative sign. | "`{{key:-}}` is an action combining two numbers. `{{key:+/-}}` is a label stuck onto one number!" |

---

### Lesson 6.2: Prime Factorization, GCF & LCM (`{{key:PRIME}}`, `{{key:FACT}}`)
- **Standards:** CCSS.MATH.CONTENT.6.NS.B.4; TEKS 6.7.A.
- **Learning Objective:** Students test numbers for primality using `{{key:PRIME}}`, decompose composite numbers into prime factor trees using `{{key:FACT}}`, and physically verify factor products using the Prime Factor Studio logarithmic slide rule comparator and Counting Studio rectangular arrays.
- **Manipulatives:** StackCalc Prime Factor Studio (13U Gridfinity Enclosure `PRIME-01` with Logarithmic Slide Rule Comparator and 29 Proportional Blocks) and Counting & Array Studio (144 Four-Color Tiles, `UNIF-01`).
- **Tactile Warm-Up:** 
  1. *Counting Tile Array Test:* Take 24 counting tiles. Can they form a rectangular array with row and column dimensions $\ge 2$? (Yes: $2 \times 12, 3 \times 8, 4 \times 6$). Now take 23 tiles. Try every width: 2 leaves 1 leftover; 3 leaves 2 leftover; 4 leaves 3 leftover. 23 tiles can ONLY form a straight line $1 \times 23$! A prime number has no rectangular matrix factorization.
  2. *Napierian Slide Rule Stacking:* Place a Blue Block {{key:2}} and an Amber/Green Block {{key:3}} from the Prime Studio onto the desk next to the box. Stack Block {{key:3}} on top of Block {{key:2}}. Look at the back-wall slide rule scale: the top edge aligns EXACTLY with tick mark **6**! Adding logarithmic lengths multiplies factors: $h(2) + h(3) = 12.64\text{ mm} + 20.04\text{ mm} = 32.68\text{ mm} = h(6)$!

#### Verbatim Teacher Dialogue Script
> **Teacher:** "Take 23 counting tiles from your Counting Studio. Try to build a rectangle that is 2 tiles wide, or 3 tiles wide. Can anyone do it without leftovers?"  
> **Students:** "No! 23 only forms a single straight line of 23 tiles!"  
> **Teacher:** "Enter 23 on the SC-6. Press yellow `{{key:f}}` and `{{key:PRIME}}`. What does the display show?"  
> **Students:** "`23 IS PRIME`!"  
> **Teacher:** "Now let's examine 60. Can 60 tiles form rectangles? Yes, many! Enter 60 and press {{key:PRIME}}. What does it say?"  
> **Students:** "`NOT PRIME`!"  
> **Teacher:** "To break 60 down into its fundamental atomic building blocks, press yellow `{{key:f}}` and `{{key:FACT}}`. What is the prime factorization?"  
> **Students:** "`2^2 * 3 * 5`!"  
> **Teacher:** "Now open your Prime Factor Studio! Take two Blue {{key:2}} blocks, one Green {{key:3}} block, and one Yellow {{key:5}} block. Stack them on the desk right next to the box's slide rule comparator wall. Where does the top of your tower land?"  
> **Students:** "It hits exactly the 60 line on the back wall!"  
> **Teacher:** "John Napier discovered that adding logarithmic heights is multiplication! Now swap the order: put the {{key:5}} block at the bottom, then {{key:3}}, then the two {{key:2}}s. Does the height change?"  
> **Students:** "No! It still hits 60 exactly! Multiplication is commutative!"  
> **Teacher:** "Now multiply them back on the SC-6: `{{key:2}} {{key:x²}} {{key:3}} {{key:×}} {{key:5}} {{key:×}}`. You get exactly 60!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 60 | 0 | 0 | 0 | 60 |
| {{key:PRIME}} | 0 | 0 | 0 | NOT PRIME |
| {{key:FACT}} | 0 | 0 | 0 | 60 (2² × 3 × 5) |

#### Student Practice Problems
1. Prime factorize 84: `{{key:8}} {{key:4}} {{key:FACT}}` $\to$ $2^2 \times 3 \times 7$.
2. Prime factorize 180: `{{key:1}} {{key:8}} {{key:0}} {{key:FACT}}` $\to$ $2^2 \times 3^2 \times 5$.
3. Find GCF of 84 and 180: Shared prime factors $= 2^2 \times 3 = 12$.

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student claims 1 is a prime number. | Misunderstands definition of prime (must have exactly two distinct factors). | "A prime number must have *exactly two* factors: 1 and itself. How many factors does 1 have? Only one!" |

---

### Lesson 6.3: Ratios, Unit Rates & Golden Ratio Proportions
- **Standards:** CCSS.MATH.CONTENT.6.RP.A.2, 6.RP.A.3; TEKS 6.4.B.
- **Learning Objective:** Students calculate unit rates ($240\text{ miles}$ on $8\text{ gallons} = 30\text{ mpg}$) and compute consecutive Fibonacci ratios tending to the Golden Ratio ($\phi \approx 1.618$).
- **Manipulatives:** Double number lines, tape measures.
- **Tactile Warm-Up:** If 3 packs of gum cost \$4.50, how much does 1 pack cost? ($4.50 \div 3 = 1.50$).

#### Verbatim Teacher Dialogue Script
> **Teacher:** "A car drives 372 miles on 12 gallons of fuel. What is the unit rate in miles per gallon? Enter miles: `372 {{key:ENTER}}`. Enter gallons: `12`. Divide: `{{key:÷}}`. What is the rate?"  
> **Students:** "31 miles per gallon!"  
> **Teacher:** "Now let us investigate nature's secret ratio: the Fibonacci sequence ($1, 1, 2, 3, 5, 8, 13, 21, 34, 55$). Divide consecutive terms: $55 \div 34$: `55 {{key:ENTER}} 34 {{key:÷}}`. What do you get?"  
> **Students:** "1.6176...!"  
> **Teacher:** "Now divide $89 \div 55$: `89 {{key:ENTER}} 55 {{key:÷}}`!"  
> **Students:** "1.61818...!"  
> **Teacher:** "That is Phi ($\phi$), the Golden Ratio found in sunflower spirals, nautilus shells, and classical architecture!"

| Keystroke | Register T | Register Z | Register Y | Register X |
| :--- | :--- | :--- | :--- | :--- |
| 372 | 0 | 0 | 0 | 372 |
| {{key:ENTER}} | 0 | 0 | 372 | 372 |
| 12 | 0 | 0 | 372 | 12 |
| {{key:÷}} | 0 | 0 | 0 | 31 |

#### Student Practice Problems
1. Unit price: $\$18.60$ for 6 pairs of socks: `18.60 {{key:ENTER}} {{key:6}} {{key:÷}}` = $\$3.10$ per pair.
2. Typing rate: 385 words in 7 minutes: `385 {{key:ENTER}} {{key:7}} {{key:÷}}` = 55 wpm.
3. Fibonacci ratio $144 \div 89$: `144` {{key:ENTER}} `89` `{{key:÷}}` = $1.61797...$

#### Misconception Diagnostic Table

| Observable Student Error | Cognitive Root Cause | Targeted Remediation Prompt |
|:---|:---|:---|
| Student divides gallons by miles ($12 \div 372 = 0.032$) when asked for miles per gallon. | Ignores unit dimensional grammar. | "Say the units out loud: *miles* PER *gallon*. Miles goes in first, gallons goes in second!" |

---

## Master 4-Tier Assessment Rubric & Diagnostic Protocol

Every student interaction across the 25 lesson plans is evaluated along four observable performance criteria:

| Performance Band | Score | Concrete Manipulative Stage | Representational Drawing | Abstract RPN Stack Execution |
|:---|:---:|:---|:---|:---|
| **Exemplary** | **4 pts** | Fluidly constructs physical model with zero prompting. Explains spatial relationships and invariances clearly to peers. | Accurately sketches bar models, area arrays, or number lines with correct proportional scaling. | Keys problem into SC-6 fluently; explains register states ($X, Y, Z, T$); uses `{{key:LASTX}}` or inverse operations to self-check. |
| **Proficient** | **3 pts** | Correctly builds model after initial launch. Self-corrects minor manipulative errors without teacher intervention. | Draws recognizable visual models matching the problem context. | Enters correct keystrokes on SC-6; successfully identifies solution on Register $X$. |
| **Developing** | **2 pts** | Requires teacher prompting to begin building or select correct manipulative blocks. | Sketches disorganized diagrams that fail to preserve mathematical proportionality. | Frequently omits `{{key:ENTER}}` separator or confuses `{{key:+/-}}` with `{{key:-}}`; needs step-by-step keystroke guidance. |
| **Intervention** | **1 pt** | Unable to model problem with concrete blocks; counts by ones; exhibits persistent off-task or frustrated behavior. | Does not produce pictorial representations; writes isolated digits disconnected from meaning. | Unable to operate calculator interface; relies on wild guessing without checking screen feedback. |

---

## Student Intervention Decision Tree & Cognitive Misconceptions

When a student struggles at a workshop station, follow this structured diagnostic decision protocol:

| Observed Student Error | Diagnostic Root Cause | Immediate Remediation Action |
| :--- | :--- | :--- |
| **Concatenated Digits** (e.g., `64` instead of `6` `{{key:ENTER}}` `4`) | Omitted `{{key:ENTER}}` separator before second operand | Re-anchor the **Elevator Mental Model** (*"Lift `6` to the balcony first!"*) |
| **Nonsensical Numerical Answer** (e.g., negative area) | Reversed operand order or misapplied operation | Point to physical blocks: *"Can $4$ tiles have negative area?"* |
| **Counting One-by-One from $1$** | Subitizing benchmark not yet internalized | Revert to **Ten-Frame Subitizing Drill** (`{{key:▦}}`); focus on $5$ and $10$ benchmarks |
| **Blind Guessing in Quiz Mode** | Cognitive overload from pace or difficulty tier | Drop down two difficulty levels; re-engage tactile blocks before restarting timer |

---

## Cognitive Science of Fluency, Spaced Retrieval & Quiz Engine Architecture

### Spaced Retrieval Practice & The Ebbinghaus Forgetting Curve
Why does passive flashcard drilling fail so often in elementary classrooms? The answer lies in Hermann Ebbinghaus's pioneering work on the **Forgetting Curve** and modern cognitive research on **Retrieval-Induced Facilitation** (Roediger & Karpicke, 2006). Actively *retrieving* a mathematical fact from memory alters its neural representation, making it exponentially more durable than passively re-reading multiplication charts:

| Review Milestone | Scheduled Interval | Typical Memory Retention Floor |
| :--- | :--- | :--- |
| **Initial Acquisition** | Day 1 | $100\% \to 40\%$ without review |
| **1st Spaced Retrieval** | Day 2 | Restores to $100\%$; floor rises to $60\%$ |
| **2nd Spaced Retrieval** | Day 4 | Restores to $100\%$; floor rises to $80\%$ |
| **3rd Spaced Retrieval** | Day 8 | Restores to $100\%$; floor rises to $90\%$ |
| **Long-Term Automaticity** | Day 16+ | Consolidated in permanent semantic memory |

### The Leitner Stack Algorithm in Calculator Silicon
The SC-6 Quiz Engine (`{{key:?}}`) incorporates a modified **Leitner Spaced Retrieval Queue** directly into its memory registers:
- When a student answers a challenge correctly within the fast latency threshold ($T < T_{\text{max}}$), the question moves up to the highest stability tier and does not reappear for at least $30$ problem cycles.
- When a student answers incorrectly, the problem is tagged as an **active learning defect** and re-inserted at queue positions $+3$ and $+7$, cementing the neural pathway while the solution is still fresh in working memory.

| Student Evaluation (`{{key:≠}}`) | Queue Transition | Scoring & Cooldown Policy |
| :--- | :--- | :--- |
| **Accurate & Fast ($T < T_{\text{max}}$)** | Promoted to **Tier 3 (Mastered)** | Cooldown of $30$ problem cycles; streak incremented |
| **Inaccurate or Slow** | Tagged as **Defect Re-Queue** | Re-inserted at queue positions $+3$ and $+7$; $-10\text{ pt}$ penalty |

### Quiz PRNG, Keypress Entropy & Continuous EEPROM Partitioning
To guarantee unpredictable practice drills across classroom stations, the quiz engine uses a 32-bit Linear Congruential Generator ($X_{n+1} = (1664525 \cdot X_n + 1013904223) \pmod{2^{32}}$) continuously re-seeded by microsecond timing jitter from the student's physical keystrokes on the $400\text{ g}$ snap-dome matrix. A dedicated 64-byte EEPROM partition preserves unlocked levels (`0x01`), active session scores (`0x02`), high scores per level (`0x06`), fastest latencies (`0x1E`), and the 26-byte Leitner active defect re-queue ring (`0x2A`) across power cycles.

---

For printable student companion station worksheets and practice forms, proceed to [Curriculum Station Worksheets Library](../../curriculum/worksheets.md). For foundational formula references and prime catalogs, see [Appendix C: Formulas, Conversions & Prime Catalogs](appendix-c-formulas-and-conversions.md).
