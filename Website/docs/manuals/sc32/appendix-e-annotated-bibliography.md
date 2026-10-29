---
title: "Appendix E: Primary Sources & Annotated Bibliography | Thinking in the Stack (SC-32)"
description: "Primary sources and historical works in parenthesis-free logic, stack-based computer organization, floating-point numerical analysis, and physical modeling."
---

# Appendix E: Primary Sources & Annotated Bibliography

The architecture of the StackCalc SC-32 draws on four centuries of mathematical discovery and a century of research across mathematical logic, stack-oriented computer organization, numerical error analysis, human-factors engineering, and scientific instrument design. From Jan Łukasiewicz's 1924 parenthesis-free notation in Warsaw and John Napier's 1614 logarithmic tables at Merchiston Castle to Carl Friedrich Gauss's method of Least Squares, Claude Shannon's symbolic relay algebra, and Bill Hewlett's 1971 pocket-calculator specification in Palo Alto, these primary works trace the lineage of direct numerical computation.

---

## Primary Historical & Technical Sources

{{bibliography:sc32}}

---

## Thematic Reading Pathways

### Foundations of Problem-Solving, Calculus & Physical Intuition

* **Problem Formulation & Calculus:** George Pólya's *How to Solve It* (1945) formalizes heuristic reasoning—isolating unknowns, working backward, and testing limiting cases before computing. Steven Strogatz's *The Joy of x* (2012) and *Infinite Powers* (2019) trace the conceptual arc from elementary arithmetic to the infinitesimal calculus of Archimedes, Newton, and Leibniz.
* **Physical Scaling & Complex Rotation:** Richard Feynman's *Lectures on Physics* (Volume I, Chapter 22: *"Algebra"*) progresses in ten pages from integer counting to Euler's formula, $e^{i\theta} = \cos\theta + i\sin\theta$, and shows why multiplication by $\sqrt{-1}$ performs a $90^\circ$ rotation in the plane. Galileo Galilei's *Two New Sciences* (1638) establishes dimensional scaling laws, structural strength, and the parabolic trajectories of projectiles.
* **Transcendentals, Imaginary Units & Small Samples:** Eli Maor's *e: The Story of a Number* (1994) and Paul Nahin's *An Imaginary Tale* (1998) chronicle the analytic emergence of natural exponentials and complex numbers, while David Salsburg's *The Lady Tasting Tea* (2001) surveys the statistical methods of Carl Friedrich Gauss, Francis Galton, and William Sealy Gosset.

### History of Science, Navigation & Information Theory

* **Logarithms, Shadows & Navigation:** John Napier's *Mirifici Logarithmorum Canonis Descriptio* (1614, translated into English by Edward Wright) and Dava Sobel's *Longitude* (1995) show how logarithmic tables, spherical trigonometry, and marine chronometers reduced oceanic navigation to arithmetic addition and subtraction.
* **Symbolic Logic & Information Theory:** Claude Shannon's 1938 master's thesis (*"A Symbolic Analysis of Relay and Switching Circuits"*) and his 1948 monograph (*"A Mathematical Theory of Communication"*) establish the direct correspondence between Boolean switching operators (`AND`, `OR`, `XOR`) and logarithmic information entropy ($\log_2 p$).

### Computer Architecture, Numerical Analysis & Floating-Point Silicon

* **Postfix Stacks & Pocket Computation:** Jan Łukasiewicz's *Elementy logiki matematycznej* (1929), Charles Hamblin's 1957 and 1962 papers on reverse Polish hardware stacks, Edsger Dijkstra's 1961 shunting-yard algorithm, and the June 1972 *Hewlett-Packard Journal* articles by Thomas M. Whitney, France Rodé, Chung C. Tung, and David S. Cochran on the HP-35 four-register stack and CORDIC algorithms form the foundation of stack-machine evaluation, analyzed systematically in Donald Knuth's *The Art of Computer Programming* (Volumes 1 and 2).
* **Floating-Point Arithmetic & Numerical Analysis:** William Kahan's monographs on IEEE-754 floating-point design and principal branch cuts (including *"Mathematics Written in Sand"*) explain why guard digits and compensated summation prevent catastrophic cancellation, while Richard Brent's *Algorithms for Minimization Without Derivatives* (1973), Werner Romberg's 1955 quadrature paper, and William Press et al.'s *Numerical Recipes* document the root-finding and integration algorithms implemented in the SC-32 firmware.

Interactive web simulators, firmware sources, and open-source hardware schematics are available at [stackcalc.io](https://stackcalc.io).
