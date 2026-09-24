---
title: "Log 05: Tactile Math: The 3D-Printed Learning Lab & Expression Trees"
description: "Upright fraction towers, four-register stack stages, and binary tree manipulatives."
---

# Log 05: Tactile Math: The 3D-Printed Learning Lab & Expression Trees

<div class="inline-block px-3 py-1 mb-6 border border-accentCyan text-accentCyan font-mono text-xs tracking-wider">// HACKADAY BUILD LOG 05 · TACTILE MANIPULATIVES</div>

**Canonical Articles:**  
- [Making the Four-Level Stack Visible](../../blog/posts/2026-09-22-making-the-four-level-stack-visible.md)  
- [Reading an Expression Tree as a Postfix Program](../../blog/posts/2026-09-22-reading-an-expression-tree-as-a-postfix-program.md)  
- [Teaching Fractions as an RPN Sequence](../../blog/posts/2026-09-22-teaching-fractions-as-an-rpn-sequence.md)  
**Topic:** Educational Hardware, Physical Manipulatives & Binary Trees  
**Artifact:** Learning Lab 3D Print Pack & Lesson Plan (Collection 01, rev 0.2.0)

---

## 1. The Engineering Lesson
Why do students struggle with Reverse Polish Notation? Because algebraic notation has conditioned them to think of expressions as static text strings wrapped in parentheses.

To make postfix intuition natural and intuitive, we designed **The StackCalc Learning Lab**: a suite of physical 3D-printed and laser-engraved classroom manipulatives.

### 1. The Stack Stage (`stack_board.stl`)
A rigid 4-register desktop tray representing registers $T, Z, Y,$ and $X$. Blank writable tiles represent numeric values. When students press `ENTER`, they physically duplicate tile $X$ into slot $Y$. When an operator is evaluated, two operand tiles are removed and the calculated result is placed in $X$.

### 2. Upright Fraction Towers (`fraction_blocks.stl`)
Traditional fraction strips lie flat and make comparison clumsy. Our towers have a fixed $24 \times 24\text{ mm}$ footprint and proportional vertical heights ($96/n\text{ mm}$):
- Whole ($n=1$): $96\text{ mm}$
- Half ($n=2$): $48\text{ mm}$
- Third ($n=3$): $32\text{ mm}$
- Quarter ($n=4$): $24\text{ mm}$
- Sixth ($n=6$): $16\text{ mm}$
- Eighth ($n=8$): $12\text{ mm}$

Two halves or four quarters stack to the exact physical height of one whole block. Contact surfaces are completely flat with no embossed text; legends are laser-marked on top faces.

![StackCalc Fraction Studio Tray](../../assets/learning-lab-fraction-tray.png)
*Figure 1: The Fraction Studio tray mapping tactile heights to dot-notation keystroke sequences.*

### 3. Binary Expression Tree Board (`tree_board.stl`)
To evaluate $(a + b) \times (c - d)$, students place tokens into a structured binary tree. Moving from leaves to root in **postorder traversal** (Left, Right, Node) yields the exact RPN keystroke sequence:
$$\text{Keystrokes: } a \rightarrow b \rightarrow + \rightarrow c \rightarrow d \rightarrow - \rightarrow \times$$

---

## 2. Concrete Artifact
All 13 STL plates containing 79 separate solids and four printable classroom teacher guides are downloadable free from the [StackCalc Learning Lab](../../learning-lab.md#download-the-prototype-materials).

---

## 3. Community Discussion Invitation
**To the Hackaday Community:**  
Did you learn RPN on an HP calculator, in a computer science data structures class (stack evaluation), or via Forth? How would you explain the operational stack to a middle school student without confusing them with compiler terminology?
