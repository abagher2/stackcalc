---
title: "Unit V: Radio-Frequency Engineering, Transmission Lines & Link Budgets"
description: "Three narrative engineering chapters mastering transmission-line wave reflections, complex Smith Chart impedance matching, microwave link budgets, Fresnel clearance, Friis noise cascades, and Shannon capacity on the SC-50."
---

# Unit V: Radio-Frequency Engineering, Transmission Lines & Link Budgets

In the 1880s, the self-taught English physicist and former telegraph operator Oliver Heaviside formulated the *telegrapher's equations* to explain why undersea telegraph cables blurred crisp Morse code pulses into sluggish, overlapping currents. In low-frequency $60\text{ Hz}$ building wiring, where an electromagnetic wave propagating near the speed of light ($c \approx 3 \times 10^8\text{ m/s}$) spans a physical wavelength $\lambda = c / f$ of roughly five thousand kilometers, a circuit board ten centimeters wide shares a uniform instantaneous voltage and phase everywhere. Engineers can treat those conductors as simple lumped nodes. Once the operating frequency rises seven orders of magnitude into the radio-frequency (RF) and microwave spectrum—from $146\text{ MHz}$ mountain repeaters ($\lambda \approx 2.05\text{ m}$) and $5.8\text{ GHz}$ microwave backhauls ($\lambda \approx 5.17\text{ cm}$) to $28\text{ GHz}$ millimeter-wave radar ($\lambda \approx 1.07\text{ cm}$)—a coaxial feedline or circuit-board microstrip spans multiple wavelengths. At those frequencies, Heaviside's distributed series inductance $L'$ and shunt capacitance $C'$ govern wave propagation through the line's characteristic impedance $Z_0 = \sqrt{L' / C'}$.

In May 1929, Bell Telephone Laboratories engineers Lloyd Espenschied and Herman Affel patented the modern concentric coaxial transmission line for wideband long-distance telephony and television. Analyzing an air-insulated copper coaxial cylinder of outer shield inner diameter $D$ and center-conductor diameter $d$, they discovered a fundamental physical trade-off. High-voltage dielectric breakdown power peaks at a diameter ratio of $D / d \approx 1.65$ ($Z_0 \approx 30\ \Omega$), whereas resistive skin-effect attenuation in the copper conductors reaches its minimum at $D / d \approx 3.59$ ($Z_0 \approx 77\ \Omega$). Two-way radio transmitters and laboratory test instruments standardized on the geometric compromise of **$Z_0 = 50\ \Omega$**, while receive-only television broadcast and broadband cable networks adopted **$Z_0 = 75\ \Omega$** to minimize signal loss over kilometer-long runs. Whenever a forward-traveling wave on a $Z_0$ line encounters a detuned antenna whose complex load impedance $Z_L = R + jX$ differs from $Z_0$, boundary continuity of the electric and magnetic fields launches a reflected wave $\Gamma$ backward toward the transmitter, creating stationary voltage standing waves and return loss. To spare engineers tedious complex-number division when synthesizing quarter-wave transformers and reactive L-networks, RCA engineer Phillip H. Smith invented his conformal transmission-line chart in 1939, mapping every passive impedance ($R \ge 0$) inside the complex unit disk.

Once an electromagnetic wave leaves a matched antenna and radiates across open terrain or space, its power density spreads spherically across millions of square meters. During the 1940s at Bell Labs' Holmdel station in New Jersey, Danish-American radio engineer Harald T. Friis established the two foundational laws of wireless systems engineering. His 1946 **Free-Space Path Loss** transmission equation pairs with Augustin-Jean Fresnel's ellipsoidal diffraction zones to govern line-of-sight microwave links. His 1944 cascaded **Noise Factor** law proves that the noise figure and gain of the very first masthead amplifier above the Johnson–Nyquist thermal noise floor dictate the sensitivity of an entire receiving chain. Two years later, his Bell Labs colleague Claude Elwood Shannon published *A Mathematical Theory of Communication* (1948), establishing the absolute upper bound on error-free data rate that any communication channel of bandwidth $B$ can sustain in the presence of Gaussian thermal noise.

The **SC-50 RF, Microwave, Telecom & Radar** calculator brings these wave-reflection, propagation, and receiver-sensitivity laws into one field instrument. Each chapter in this Unit follows an end-to-end wireless engineering narrative through three connected mathematical themes:

| Chapter | Narrative Problem | Mathematical Concepts | Three Chapter Themes |
| :--- | :--- | :--- | :--- |
| **Chapter 13** | Diagnosing high reflected power on a $50\ \Omega$ mountain repeater coax terminated in $Z_L = 35 - j25\ \Omega$ and designing a reactive match | Decibel-milliwatt scaling, complex reflection $\Gamma$, VSWR, Return Loss, Mismatch Loss, Smith Chart L-networks, $\lambda/4$ stubs, and LC resonance | 1. Complex Impedance & Standing-Wave Reflections<br>2. Quarter-Wave Transformers & Smith Chart L-Networks<br>3. Lumped LC Tank Resonance & Tuning Solvers |
| **Chapter 14** | Closing a $5.8\text{ GHz}$ microwave backhaul across a $12\text{ km}$ forested valley and verifying mid-span pine tree clearance | Friis Free-Space Path Loss, effective isotropic radiated power, logarithmic link budgets, fade margin, and First Fresnel Zone ellipsoid clearance | 1. Spherical Wave Spreading & Free-Space Path Loss<br>2. Logarithmic Link Budgets & Rain-Fade Margins<br>3. Huygens Wavelets & 60% Fresnel Zone Clearance |
| **Chapter 15** | Placing a masthead LNA ($G_1 = 20\text{ dB}, N\!F_1 = 1.5\text{ dB}$) ahead of a $6\text{ dB}$ cable loss to rescue a weak satellite telemetry carrier | Johnson–Nyquist thermal noise floor, Friis noise cascade, IIP3/SFDR linearity, Shannon–Hartley capacity, and radar Doppler & $R^4$ range | 1. Thermal Noise Floors & Friis Amplifier Cascades<br>2. Third-Order Intermodulation & Dynamic Range<br>3. Shannon Channel Capacity, Doppler Shift & $R^4$ Radar |

---

# Chapter 13: The Reflected Wave on the Mountain Repeater Coax

After a February rime-ice storm sweeps across a nine-thousand-foot summit in the Sierra Nevada, the remote telemetry alarm on a $146.0\text{ MHz}$ search-and-rescue VHF repeater trips into high-reflected-power foldback. Driving a $50\text{ W}$ ($+47.0\text{ dBm}$) solid-state power amplifier into a $Z_0 = 50\ \Omega$ coaxial feedline, the repeater normally delivers nearly its full output into a tower-mounted dipole array. When the field engineer snowshoes into the summit shelter and connects a vector network analyzer to the bottom of the feedline, the instrument reveals that ice loading on the antenna elements has detuned the feedpoint to a complex load impedance of $Z_L = 35 - j25\ \Omega$—dropping the radiation resistance to $35\ \Omega$ while introducing $25\ \Omega$ of capacitive reactance.

On a high-frequency transmission line, an impedance mismatch does far more than reduce radiated signal strength. Because the electric and magnetic fields at the antenna terminals must satisfy Ohm's law for both the $50\ \Omega$ cable and the $35 - j25\ \Omega$ load simultaneously, a fraction of the incident voltage wave reflects backward down the coaxial line toward the transmitter. As the backward-traveling reflected wave interferes with the forward-traveling wave, it erects stationary voltage peaks and current troughs along the cable that can punch through coaxial dielectric insulation or destroy the collector junction of the output transistor.

Before climbing the icy tower or soldering an emergency matching network in the shelter, the engineer works through three connected RF analyses:
1. Convert the transmitter power into decibel-milliwatts and evaluate the complex reflection coefficient $\Gamma$, Voltage Standing Wave Ratio (VSWR), return loss, and reflected power in watts for $Z_L = 35 - j25\ \Omega$.
2. Determine the physical length of a quarter-wavelength coaxial matching section and the quality factor $Q$, series inductance, and shunt capacitance of a lumped reactive L-network.
3. Calculate the resonant frequency of an LC tank and solve backward for the exact tuning capacitance needed to cancel parasitic feedpoint inductance.

---

## Transmission-Line Reflections, Standing Waves, and Decibel Power

When radio-frequency energy travels from a transmitter output stage to an antenna feedpoint, the coaxial cable behaves as a distributed electromagnetic waveguide. Tracking forward and reflected power along that waveguide requires anchoring power measurements to the logarithmic milliwatt scale and solving the boundary equations at the load.

### Logarithmic Milliwatt Scaling and Characteristic Impedance

Because radio signals span eighteen orders of magnitude—from kilowatt broadcast transmitters down to femtowatt deep-space telemetry carriers—RF engineering anchors its absolute power scale to **one milliwatt** ($1\text{ mW} = 10^{-3}\text{ W}$). Any linear power $P_{\text{mW}}$ (in milliwatts) or $P_{\text{W}}$ (in watts) converts to decibels relative to one milliwatt ({{key:dBm}}, {{key:▸dBm}}) or one watt ({{key:▸dBW}}) through the base-ten logarithm and inverts back to linear milliwatts ({{key:▸mW}}) via base-ten exponentiation, while across a matched real characteristic impedance $Z_0$ ({{key:Z₀}}, with voltage conversions {{key:▸dBV}} and {{key:▸μV}}) the root-mean-square RF voltage $V_{\text{rms}}$ satisfies Ohm's power law:

$$P_{\text{dBm}} = 10 \log_{10}\left(\frac{P_{\text{mW}}}{1\text{ mW}}\right) = 10 \log_{10}(P_{\text{W}}) + 30, \qquad P_{\text{mW}} = 10^{P_{\text{dBm}} / 10}, \qquad V_{\text{rms}} = \sqrt{P_{\text{W}} \cdot Z_0}$$

In these expressions, $P_{\text{dBm}}$ is the absolute power level in $\text{dBm}$, $P_{\text{mW}}$ is linear power in milliwatts, $P_{\text{W}} = P_{\text{mW}} / 1000$ is linear power in watts, and $Z_0$ is the transmission-line characteristic impedance in ohms ($\Omega$, standardized at $50\ \Omega$ for transmitters and $75\ \Omega$ for video/broadcast coax).

Every $+10\text{ dB}$ step multiplies linear power tenfold and every $+3.0103\text{ dB}$ step doubles linear power: $0\text{ dBm}$ equals $\mathbf{1.0\text{ mW}}$ ($V_{\text{rms}} \approx 0.2236\text{ V}$ across $50\ \Omega$), $+20\text{ dBm}$ equals $\mathbf{100\text{ mW}}$ ($0.10\text{ W}$), $+30\text{ dBm}$ equals $1000\text{ mW} = \mathbf{1.0\text{ W}}$ ($V_{\text{rms}} \approx 7.071\text{ V}$ across $50\ \Omega$), and our mountain repeater's $P_{\text{W}} = 50\text{ W}$ ($50{,}000\text{ mW}$) output corresponds to $P_{\text{dBm}} = 10\log_{10}(50{,}000) \approx \mathbf{+46.990\text{ dBm}}$, developing a matched root-mean-square voltage of $V_{\text{rms}} = \sqrt{50 \times 50} = \mathbf{50.0\text{ V}}$ across the $50\ \Omega$ line.

### Complex Reflection Coefficient, Standing Wave Ratio, Return Loss, and Mismatch Loss

When a forward-traveling electromagnetic wave with voltage phasor $V^+$ and current phasor $I^+ = V^+ / Z_0$ propagates down a lossless transmission line of real characteristic impedance $Z_0$ and reaches an antenna of complex load impedance $Z_L = R + jX$ ({{keycap:jX}} in {{key:CMPLX}}, where $R$ is series resistance and $X$ is inductive $+jX$ or capacitive $-jX$ reactance in ohms), boundary continuity requires total terminal voltage $V_L = V^+ + V^-$ and total terminal current $I_L = (V^+ - V^-) / Z_0$ to satisfy $V_L / I_L = Z_L$. Solving that boundary condition defines the complex **Voltage Reflection Coefficient** $\Gamma$ ({{keycap:Γ}}, inverted back to complex impedance via {{keycap:Z←Γ}}):

$$\Gamma = \frac{V^-}{V^+} = \frac{Z_L - Z_0}{Z_L + Z_0} = \frac{(R - Z_0) + jX}{(R + Z_0) + jX} = |\Gamma| \angle \theta, \qquad |\Gamma| = \sqrt{\frac{(R - Z_0)^2 + X^2}{(R + Z_0)^2 + X^2}}$$

![Superposition of forward and reflected traveling waves along a transmission line forming a voltage standing wave envelope (VSWR).](../assets/diagrams/domains/diagram_ch05_vswr_standing_wave.png)

As the reflected voltage wave $V^-$ travels backward and superposes with the incident wave $V^+$, constructive interference at half-wavelength ($\lambda / 2$) intervals produces stationary voltage maxima $V_{\max} = |V^+|(1 + |\Gamma|)$, while destructive interference shifted by a quarter-wavelength ($\lambda / 4$) produces voltage minima $V_{\min} = |V^+|(1 - |\Gamma|)$. The ratio of peak to trough voltage defines the dimensionless **Voltage Standing Wave Ratio** ({{key:SWR}}, {{keycap:SWR}}), the decibel attenuation of the reflected power fraction $|\Gamma|^2$ defines the **Return Loss** ({{keycap:RL}}, in $\text{dB}$), and the decibel reduction in forward power actually delivered into the load ($1 - |\Gamma|^2$) defines the **Mismatch Loss** ($\text{ML}_{\text{dB}}$, in $\text{dB}$):

$$\text{VSWR} = \frac{V_{\max}}{V_{\min}} = \frac{1 + |\Gamma|}{1 - |\Gamma|} \iff |\Gamma| = \frac{\text{VSWR} - 1}{\text{VSWR} + 1}$$

$$\text{RL}_{\text{dB}} = -10 \log_{10}\left(|\Gamma|^2\right) = -20 \log_{10}|\Gamma|, \qquad \text{ML}_{\text{dB}} = -10 \log_{10}\left(1 - |\Gamma|^2\right)$$

For our ice-detuned mountain repeater antenna with $Z_L = 35 - j25\ \Omega$ on a $Z_0 = 50\ \Omega$ coaxial feedline, the numerator impedance difference is $Z_L - Z_0 = -15 - j25\ \Omega$, whose magnitude is $\sqrt{(-15)^2 + (-25)^2} = \sqrt{225 + 625} = \sqrt{850} \approx 29.1548\ \Omega$. The denominator impedance sum is $Z_L + Z_0 = 85 - j25\ \Omega$, whose magnitude is $\sqrt{85^2 + (-25)^2} = \sqrt{7225 + 625} = \sqrt{7850} \approx 88.6002\ \Omega$. Dividing numerator by denominator gives the reflection magnitude and phase:

$$|\Gamma| = \frac{\sqrt{850}}{\sqrt{7850}} = \sqrt{\frac{17}{157}} \approx \mathbf{0.3291}, \qquad \theta = \operatorname{atan2}(-25, -15) - \operatorname{atan2}(-25, 85) = -120.96^\circ - (-16.39^\circ) = \mathbf{-104.57^\circ}$$

Substituting $|\Gamma| \approx 0.3291$ into the standing-wave, return-loss, and mismatch-loss relations yields:

$$\text{VSWR} = \frac{1 + 0.3291}{1 - 0.3291} = \frac{1.3291}{0.6709} \approx \mathbf{1.981 : 1}, \qquad \text{RL}_{\text{dB}} = -20 \log_{10}(0.3291) \approx \mathbf{9.654\text{ dB}}, \qquad \text{ML}_{\text{dB}} = -10 \log_{10}\left(1 - 0.3291^2\right) \approx \mathbf{0.498\text{ dB}}$$

Because the reflected power fraction is $|\Gamma|^2 = 17 / 157 \approx \mathbf{10.828\%}$, our $50\text{ W}$ repeater transmitter suffers $50\text{ W} \times 0.10828 \approx \mathbf{5.414\text{ W}}$ ($+37.335\text{ dBm}$) of reflected power slamming back into the amplifier output stage, while $50\text{ W} - 5.414\text{ W} = \mathbf{44.586\text{ W}}$ ($89.172\%$) enters the antenna:

| `{{key:SWR}}` | Reflection $\lvert\Gamma\rvert$ | Return Loss `{{keycap:RL}}` ($\text{dB}$) | Mismatch Loss $\text{ML}$ ($\text{dB}$) | Reflected Power $\lvert\Gamma\rvert^2$ ($\%$) | Transmitted Power $1-\lvert\Gamma\rvert^2$ ($\%$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $1.00 : 1$ | $0.0000$ | $\infty\text{ dB}$ | $0.000\text{ dB}$ | $0.00\%$ | $100.00\%$ |
| $1.20 : 1$ | $0.0909$ | $20.83\text{ dB}$ | $0.036\text{ dB}$ | $0.83\%$ | $99.17\%$ |
| $1.50 : 1$ | $0.2000$ | $13.98\text{ dB}$ | $0.177\text{ dB}$ | $4.00\%$ | $96.00\%$ |
| $1.98 : 1$ | $0.3291$ | $9.65\text{ dB}$ | $0.498\text{ dB}$ | $10.83\%$ | $89.17\%$ |
| $3.00 : 1$ | $0.5000$ | $6.02\text{ dB}$ | $1.249\text{ dB}$ | $25.00\%$ | $75.00\%$ |
| $6.00 : 1$ | $0.7143$ | $2.92\text{ dB}$ | $3.100\text{ dB}$ | $51.02\%$ | $48.98\%$ |

---

## Conformal Smith Chart Transformations and Reactive Matching Networks

To eliminate the reflected wave and restore a $1.00 : 1$ standing wave ratio on the main $50\ \Omega$ feedline, the engineer must insert a lossless impedance-matching network between the coaxial trunk and the antenna terminals.

### Normalized Impedance Mapping and Quarter-Wave Transformers

Dividing any complex load impedance $Z_L = R + jX$ by the system reference impedance $Z_0$ produces the dimensionless normalized impedance $z = Z_L / Z_0 = (R / Z_0) + j(X / Z_0) = r + jx$ (for our $35 - j25\ \Omega$ repeater load on a $50\ \Omega$ line, $r = 35/50 = \mathbf{0.70}$ and $x = -25/50 = \mathbf{-0.50}$). Under the bilinear Möbius transformation $\Gamma = (z - 1) / (z + 1)$, Phillip H. Smith showed in 1939 that the entire right half-plane of passive resistances ($r \ge 0$) maps conformally into the unit circle $|\Gamma| \le 1$ on the **Smith Chart** ({{key:Γ}}, {{key:▦}}).

![Complex reflection-coefficient plane and normalized impedance loci of the Smith Chart.](../assets/diagrams/domains/diagram_ch05_smith_chart.png)

At the center origin of the Smith Chart ($\Gamma = 0 + j0$), the normalized impedance is $z = 1 + j0$ ($Z_L = Z_0$). Moving a physical distance $\ell$ along a lossless transmission line of wavelength $\lambda$ ({{key:λ/L}}) rotates the reflection phasor $\Gamma$ clockwise around the origin at constant radius $|\Gamma|$ through an electrical phase angle of $2\beta\ell = 4\pi\ell / \lambda$. When the line section has an electrical length of one quarter-wavelength ($\ell = \lambda / 4$), the rotation angle is $2\beta(\lambda / 4) = \pi\text{ radians}$ ($180^\circ$), which inverts normalized impedance ($z_{\text{in}} = 1 / z_L$) so that a **Quarter-Wave Transformer** ({{key:TLN}}, and {{key:Γ}} opening the {{key:Z₀}} workspace `Z = √(S × L)`) of characteristic impedance $Z_{\text{match}}$ matches a real source impedance $Z_S$ to a real load resistance $Z_L$:

$$\lambda = \frac{c}{f} = \frac{299.792458}{f_{\text{MHz}}}\quad [\text{m}], \qquad \ell_{\lambda/4} = \frac{\lambda}{4} \cdot \text{VF}, \qquad Z_{\text{match}} = \sqrt{Z_S \cdot Z_L}$$

Here $f_{\text{MHz}}$ is the operating frequency in megahertz, $\lambda$ is the free-space wavelength in meters, $\text{VF} = 1 / \sqrt{\varepsilon_r}$ is the coaxial cable velocity factor, and $Z_{\text{match}}$ is the geometric-mean characteristic impedance in ohms. At the repeater frequency of $f = 146.0\text{ MHz}$, the free-space wavelength is $\lambda = 299.792458 / 146.0 \approx \mathbf{2.0534\text{ m}}$ and a free-space quarter-wave whip measures $\ell_{\lambda/4} = 2.0534 / 4 \approx \mathbf{0.5133\text{ m}}$ ($51.33\text{ cm}$). Cut from foam-dielectric coaxial cable with velocity factor $\text{VF} = 0.82$, the physical quarter-wave stub length is $0.5133 \times 0.82 \approx \mathbf{0.4209\text{ m}}$ ($42.1\text{ cm}$). To match a $Z_S = 50\ \Omega$ line to a $Z_L = 112.5\ \Omega$ antenna resistance, the required quarter-wave section impedance is $Z_{\text{match}} = \sqrt{50 \times 112.5} = \sqrt{5625} = \mathbf{75.0\ \Omega}$, allowing standard $75\ \Omega$ video coax to serve as an exact quarter-wave transformer.

### Lumped L-Network Synthesis and Resonant Tank Circuits

When matching a lower resistance $R_{\text{low}}$ up to a higher resistance $R_{\text{high}}$ at VHF or HF frequencies using compact lumped inductors and capacitors, a two-element reactive **L-network** ({{key:Γ}}) places a reactive element $X_{\text{series}}$ in series with $R_{\text{low}}$ and a complementary opposite-sign reactive element $X_{\text{shunt}}$ in parallel across $R_{\text{high}}$. Equivalence of series and parallel resistance-reactance networks defines the nodal **Quality Factor** $Q$, while inside RF filters and oscillators an inductance $L$ (in henries, $\text{H}$) and capacitance $C$ (in farads, $\text{F}$) resonate at frequency $f_0$ ({{key:f₀}}, with reactance {{key:XLC}} and RC cutoff frequency {{key:fc}} given by $f_c = 1 / (2\pi R C)$):

$$Q = \sqrt{\frac{R_{\text{high}}}{R_{\text{low}}} - 1}, \qquad |X_{\text{series}}| = Q \cdot R_{\text{low}}, \qquad |X_{\text{shunt}}| = \frac{R_{\text{high}}}{Q}, \qquad f_0 = \frac{1}{2\pi \sqrt{L \cdot C}}$$

![Lossless reactive L-network impedance matching topology transforming a low load resistance to 50 ohms.](../assets/diagrams/domains/diagram_ch05_l_network.png)

Consider matching our repeater's resistive component $R_{\text{low}} = 35\ \Omega$ up to $R_{\text{high}} = 50\ \Omega$ at $f = 146.0\text{ MHz}$. The required nodal quality factor is $Q = \sqrt{(50 / 35) - 1} = \sqrt{0.42857} \approx \mathbf{0.6547}$, which specifies a net series inductive reactance of $|X_{\text{series}}| = 0.6547 \times 35 \approx \mathbf{22.91\ \Omega}$ and a shunt capacitive reactance of $|X_{\text{shunt}}| = 50 / 0.6547 \approx \mathbf{76.38\ \Omega}$. Because the iced antenna already exhibits $-j25\ \Omega$ of series capacitive reactance, the series inductor must simultaneously cancel that $-25\ \Omega$ reactance and supply $+22.91\ \Omega$ of net inductive reactance, requiring a total inductive reactance of $X_L = 25 + 22.91 = \mathbf{47.91\ \Omega}$ ($L = 47.91 / (2\pi \times 146 \times 10^6) \approx \mathbf{52.23\text{ nH}}$) paired with a shunt capacitor of $C = 1 / (2\pi \times 146 \times 10^6 \times 76.38) \approx \mathbf{14.27\text{ pF}}$. Similarly, when stepping a $R_{\text{low}} = 10\ \Omega$ power-transistor collector up to $R_{\text{high}} = 50\ \Omega$, the nodal quality factor is $Q = \sqrt{(50/10) - 1} = \mathbf{2.00}$, giving $|X_{\text{series}}| = \mathbf{20.0\ \Omega}$ and $|X_{\text{shunt}}| = \mathbf{25.0\ \Omega}$.

---

## Diagnosing Mismatches and Synthesizing Matching Networks on the Stack

The **SC-50** combines **Native Complex RF Mode** ({{key:CMPLX}}, activating the six top-row softkeys {{keycap:Γ}}, {{keycap:Z←Γ}}, {{keycap:jX}}, {{keycap:SWR}}, {{keycap:RL}}, {{keycap:Z₀}}) for complex load impedances $Z_L = R + jX$ against toggleable system impedance {{key:Z₀}} ($50\ \Omega \leftrightarrow 75\ \Omega$), automatic Smith Chart parameter logging ({{key:▦}}), decibel-milliwatt scaling ({{key:dBm}}, {{key:▸dBm}}, {{key:▸mW}}, {{key:▸dBW}}), and matching primitives ({{key:SWR}}, {{key:Γ}}, {{key:TLN}}, {{key:f₀}}, {{key:fc}}, {{key:XLC}}, {{key:λ/L}}) with the **Bidirectional Equation Solver Workspaces** ({{key:SOLVE}} / {{key:XEQ}}) on {{key:SWR}} (`S = (1 + G) / (1 - G)`, softkeys {{keycap:S}}, {{keycap:G}}), {{key:Γ}} (`ZMAT: Z = √(S × L)`, softkeys {{keycap:Z}}, {{keycap:S}}, {{keycap:L}}), and {{key:f₀}} (`F0: F = 1 / (2π√(L×C))`, softkeys {{keycap:F}}, {{keycap:L}}, {{keycap:C}}):

| Button / Menu | Operation | Register Z | Register Y | Register X | Governing Expression & Solver Schema |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `{{key:dBm}}` / `{{key:▸dBm}}` | Linear Power to dBm | — | — | Power $P_{\text{mW}}$ ($\text{mW}$) | $P_{\text{dBm}} = 10 \log_{10}(P_{\text{mW}})$ (paired with `{{key:▸dBW}}`, `{{key:▸dBV}}`, `{{key:▸μV}}`) |
| `{{key:▸mW}}` | dBm to Linear Power | — | — | Power $P_{\text{dBm}}$ ($\text{dBm}$) | $P_{\text{mW}} = 10^{P_{\text{dBm}} / 10}$ |
| `{{key:CMPLX}}` | Native Complex RF Menu | — | Resistance $R$ ($\Omega$) | Reactance $X$ ($\Omega$) | Softkeys: `{{keycap:Γ}}` `{{keycap:Z←Γ}}` `{{keycap:jX}}` `{{keycap:SWR}}` `{{keycap:RL}}` `{{keycap:Z₀}}` ($Z_L = R + jX \leftrightarrow \Gamma$) |
| `{{key:SWR}}` | Standing Wave Ratio | — | — | $\lvert\Gamma\rvert$ or $Z_L = R + jX$ | Stack: $\text{VSWR} = \frac{1 + \lvert\Gamma\rvert}{1 - \lvert\Gamma\rvert}$ (fills `{{key:▦}}`); Solver: `S = (1+G)/(1-G)` (`{{keycap:S}}`,`{{keycap:G}}`) |
| `{{keycap:RL}}` | Return Loss ($\text{dB}$) | — | — | $\Gamma$ or $Z_L$ | Softkey in `{{key:CMPLX}}`: $\text{RL}_{\text{dB}} = -20 \log_{10}\lvert\Gamma\rvert$ |
| `{{key:Γ}}` | Smith Match & {{key:Z₀}} Solver | — | Source $Z_S$ ($\Omega$) | Load $Z_L$ ($\Omega$) | Stack: $Q = \sqrt{(R_{\text{high}} / R_{\text{low}}) - 1}$; Opens {{key:Z₀}} (`Z = √(S×L)`, `{{keycap:Z}}`,`{{keycap:S}}`,`{{keycap:L}}`) |
| `{{key:TLN}}` | $\lambda/4$ Transformer Impedance | — | Source $Z_S$ ($\Omega$) | Load $Z_L$ ($\Omega$) | Immediate stack: $Z_{\text{match}} = \sqrt{Z_S \cdot Z_L}$ |
| `{{key:f₀}}` / `{{key:fc}}` | LC Resonance & RC Cutoff | — | Inductance $L$ ($\text{H}$) | Capacitance $C$ ($\text{F}$) | Stack: $f_0 = \frac{1}{2\pi\sqrt{L \cdot C}}$; Solver: `F = 1 / (2π√(L×C))` (`{{keycap:F}}`,`{{keycap:L}}`,`{{keycap:C}}`) |
| `{{key:λ/L}}` | Free-Space Wavelength | — | — | Frequency $f_{\text{MHz}}$ | $\lambda = 299.792458 / f_{\text{MHz}}$ ($\text{m}$) |

### Evaluating Complex Repeater Mismatch, Return Loss, and Reflected Watts on the Stack

Inside the mountain repeater shelter, the engineer opens Native Complex Mode ({{key:CMPLX}}), packs the VNA measurement $Z_L = 35 - j25\ \Omega$ into Register $X$ with softkey {{keycap:jX}}, presses {{keycap:Γ}} / {{keycap:SWR}} (or primary {{key:SWR}}) to evaluate $\text{VSWR}$ and populate the Smith Chart table {{key:▦}} (`|GAMMA| = 0.3291`, `GAMMA ANG = -104.57°`, `VSWR = 1.981`, `RET LOSS = 9.654 dB`, `r/z0 = 0.70`, `x/z0 = -0.50`), presses softkey {{keycap:RL}} for Return Loss, and checks the reflected power for the $50{,}000\text{ mW}$ ($50\text{ W}$) transmitter:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `{{key:CMPLX}} 35 {{key:ENTER}} 25 {{key:+/-}} {{keycap:jX}} {{key:+}}` | $0$ | $0$ | $0$ | $35 - j25$ | Pack complex load impedance $Z_L = 35 - j25\ \Omega$ into Register $X$ |
| `{{keycap:SWR}}` | $0$ | $0$ | $0$ | $1.981$ | Evaluate $\text{VSWR} = 1.981 : 1$ against $Z_0 = 50\ \Omega$ (`{{keycap:Z₀}}`) and fill Smith table `{{key:▦}}` |
| `35 {{key:ENTER}} 25 {{key:+/-}} {{keycap:jX}} {{key:+}} {{keycap:RL}}` | $0$ | $0$ | $1.981$ | $9.653$ | Compute Return Loss $\text{RL} = 9.653\text{ dB}$ from complex load ($\lvert\Gamma\rvert = 0.3291$) |
| `50000 {{key:▸dBm}} {{key:x⇄y}} {{key:-}}` | $0$ | $0$ | $1.981$ | $37.337$ | Subtract $9.653\text{ dB}$ return loss from $+46.990\text{ dBm}$ ($50\text{ W}$) to get reflected dBm |
| `{{key:▸mW}} 1000 {{key:÷}}` | $0$ | $0$ | $1.981$ | **$5.416$** | Convert $+37.337\text{ dBm}$ to milliwatts ($5416\text{ mW}$) and divide by $1000$ for $5.416\text{ W}$ |

The stack confirms that $\mathbf{5.42\text{ W}}$ of RF power is reflecting back down the line at $\text{VSWR} = \mathbf{1.981 : 1}$, explaining why the repeater's protection circuit triggered.

### Designing Quarter-Wave Stubs, L-Networks, and Resonant Tanks on the Stack

Next, the engineer evaluates the $146.0\text{ MHz}$ wavelength and quarter-wave dimension ({{key:λ/L}}), computes the quarter-wave transformer impedance for a $50\ \Omega$ to $112.5\ \Omega$ port ({{key:TLN}}), solves an L-network match from $10\ \Omega$ to $50\ \Omega$ ({{key:Γ}}), and checks a $100\text{ nH} / 10\text{ pF}$ harmonic trap ({{key:f₀}}):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `146 {{key:λ/L}} 4 {{key:÷}}` | $0$ | $0$ | $0$ | $0.5133$ | Compute free-space $\lambda = 2.0534\text{ m}$ at $146\text{ MHz}$ and divide by $4$ for $\ell_{\lambda/4} = 0.5133\text{ m}$ |
| `50 {{key:ENTER}} 112.5 {{key:TLN}}` | $0$ | $0$ | $0.5133$ | $75$ | Quarter-wave transformer impedance $Z_{\text{match}} = \sqrt{50 \times 112.5} = 75.0\ \Omega$ |
| `50 {{key:ENTER}} 10 {{key:Γ}}` | $0.51334$ | $0.5133$ | $75$ | $2$ | L-network nodal quality factor $Q = \sqrt{(50/10) - 1} = 2.00$ (and opens {{key:Z₀}} workspace) |
| `1 {{key:E}} 7 {{key:+/-}} {{key:ENTER}} 1 {{key:E}} 11 {{key:+/-}} {{key:f₀}}` | $75$ | $75$ | $2$ | **$1.5915\text{e}8$** | Resonant frequency $f_0 = 159.155\text{ MHz}$ for $L = 100\text{ nH}$ and $C = 10\text{ pF}$ |

Multiplying the L-network quality factor $Q = 2.00$ by $R_{\text{low}} = 10\ \Omega$ gives series reactance $|X_{\text{series}}| = \mathbf{20.0\ \Omega}$, while dividing $R_{\text{high}} = 50\ \Omega$ by $Q = 2.00$ gives shunt reactance $|X_{\text{shunt}}| = \mathbf{25.0\ \Omega}$.

### Back-Solving Resonant Tuning Capacitance and Reflection Limits in the Solver Workspace

Suppose an auxiliary $433.92\text{ MHz}$ ($4.3392 \times 10^8\text{ Hz}$) UHF telemetry link exhibits $L = 18.5\text{ nH}$ ($1.85 \times 10^{-8}\text{ H}$) of parasitic feedpoint inductance and the engineer must select the exact series capacitor $C$ that resonates the feedpoint at $433.92\text{ MHz}$, while also verifying the maximum reflection magnitude $|\Gamma|$ ({{keycap:G}}) allowed by a $\text{VSWR} \le 1.50 : 1$ ({{keycap:S}}) specification. Opening the {{key:f₀}} (`F = 1 / (2π√(L×C))`) and {{key:SWR}} (`S = (1 + G) / (1 - G)`) Solver Workspaces solves both inverse problems directly:

| Keystroke | Solver Display / Register X | What Happens in the `{{key:f₀}}` & `{{key:SWR}}` Solver Workspaces |
| :--- | :---: | :--- |
| `{{key:f₀}}` | `F=1/(2π√(L×C))` | Open the LC Resonance ({{key:f₀}}) Solver Workspace with softkeys `{{keycap:F}}`, `{{keycap:L}}`, `{{keycap:C}}` |
| `4.3392 {{key:E}} 8 {{keycap:F}}` | $4.3392 \times 10^8$ | Store target resonant frequency $F = 433.92\text{ MHz}$ into softkey `{{keycap:F}}` (`{{keycap:LFU0}}`) |
| `1.85 {{key:E}} 8 {{key:+/-}} {{keycap:L}}` | $1.8500 \times 10^{-8}$ | Store parasitic inductance $L = 18.5\text{ nH}$ into softkey `{{keycap:L}}` (`{{keycap:LFU1}}`) |
| `{{key:SOLVE}} {{keycap:C}}` | **$7.2856 \times 10^{-12}$** | Solve backward for matching capacitance $C = 1 / ((2\pi F)^2 L) = \mathbf{7.2856\text{ pF}}$ |
| `{{key:SWR}}` | `S=(1+G)/(1-G)` | Open the Standing Wave Ratio ({{key:SWR}}) Solver Workspace with softkeys `{{keycap:S}}`, `{{keycap:G}}` |
| `1.5 {{keycap:S}}` | $1.5000$ | Store specification limit $S = 1.50$ into softkey `{{keycap:S}}` (`{{keycap:LFU0}}`) |
| `{{key:SOLVE}} {{keycap:G}}` | **$0.2000$** | Solve backward for reflection magnitude $\lvert\Gamma\rvert = (1.5 - 1)/(1.5 + 1) = \mathbf{0.2000}$ |

### Try It on the Stack

Practice complex transmission-line diagnostics, quarter-wave stub sizing, and reactive matching on the stack and in the Solver Workspace with these three RF workbench exercises:

1. **75-Ohm Broadcast Coax Mismatch and Aviation Quarter-Wave Whip:** Open {{key:CMPLX}}, toggle the reference impedance to $75\ \Omega$ ({{keycap:Z₀}}), pack load impedance $Z_L = 50 + j25\ \Omega$ (`50` {{key:ENTER}} `25` {{keycap:jX}}), and evaluate {{keycap:SWR}} (then press {{keycap:Z₀}} again to restore $50\ \Omega$). Next, compute the quarter-wave whip length at the $121.5\text{ MHz}$ aviation emergency frequency (`121.5` {{key:λ/L}} `4` {{key:÷}}). *(Verified Register $X$ results: $\text{VSWR} \approx \mathbf{1.768 : 1}$ and $\ell_{\lambda/4} \approx \mathbf{0.617\text{ m}}$.)*
2. **Commercial Specification Limit Return Loss and Reflected Power:** A commercial cellular sector antenna specifies a maximum reflection magnitude of $|\Gamma| = 0.20$. Compute its standing wave ratio (`0.2` {{key:SWR}}), return loss (`0.2` {{key:LOG}} `20` {{key:+/-}} {{key:×}}), and reflected power in watts when driven by a $40\text{ W}$ ($40{,}000\text{ mW}$) base station (`40000` {{key:▸dBm}} {{key:x⇄y}} {{key:-}} {{key:▸mW}} `1000` {{key:÷}}). *(Verified Register $X$ results: $\text{VSWR} = \mathbf{1.50 : 1}$, $\text{RL} \approx \mathbf{13.979\text{ dB}}$, and $P_{\text{refl}} = \mathbf{1.60\text{ W}}$.)*
3. **Power Transistor L-Network and Backward Tank Inductance:** Find the L-network quality factor $Q$ and series reactance $|X_{\text{series}}|$ required to match a $12.5\ \Omega$ transistor output to $50\ \Omega$ (`50` {{key:ENTER}} `12.5` {{key:Γ}} `12.5` {{key:×}}), then open {{key:f₀}}, store `159.155` {{key:E}} `6` {{keycap:F}} and `40` {{key:E}} `12` {{key:+/-}} {{keycap:C}}, and press {{key:SOLVE}} {{keycap:L}} to find the required tank inductance $L$. *(Verified Register $X$ results: $Q \approx \mathbf{1.732}$, $|X_{\text{series}}| \approx \mathbf{21.651\ \Omega}$, and $L = \mathbf{250.0\text{ nH}}$.)*

With the repeater feedline matched to $50\ \Omega$ and full forward power radiating from the tower, we follow the electromagnetic wave into open air in Chapter 14 to close a twelve-kilometer microwave backhaul across a forested mountain valley.

---

# Chapter 14: Clearing the Ridge on a Twelve-Kilometer Microwave Backhaul

To link the mountain repeater shelter back to the county emergency operations center without paying for leased fiber across wilderness terrain, the communications team is commissioning a point-to-point unlicensed $f = 5800\text{ MHz}$ ($5.8\text{ GHz}$) microwave backhaul across a $d = 12.0\text{ km}$ forested valley. At each end of the path, a tower crew mounts a parabolic dish antenna delivering $+26.0\text{ dBi}$ of isotropic gain ($G = G_{\text{tx}} + G_{\text{rx}} = 52.0\text{ dB}$ combined net antenna gain after short waveguide jumpers), driven by a microwave transceiver with transmitter output power $P_{\text{tx}} = 250\text{ mW}$ ($+23.979\text{ dBm}$). To sustain $256\text{-QAM}$ modulation with a $25\text{ dB}$ rain-fade margin above its $-78.0\text{ dBm}$ threshold, the receiver at the far end of the valley requires an unfaded signal level of at least $P_{\text{rx}} \ge -55.0\text{ dBm}$.

Standing on the transmit tower platform with binoculars, the lead engineer spots a potential hazard halfway across the valley ($d_{\text{mid}} = 6.0\text{ km}$ from either tower): a granite ridge crowned with eighty-foot ponderosa pines rises just below the optical sightline between the two dishes. A casual observer might assume that as long as a laser pointer aimed from one dish to the other clears the treetops, the microwave link will suffer no obstruction loss. In wave optics and radio propagation, however, energy does not travel along an infinitely thin geometric pencil ray. Instead, it propagates as an expanding wavefront whose constructive phase coherence fills a cigar-shaped volume of space around the sightline known as the **First Fresnel Zone**.

If the mid-span pine needles intrude into that three-dimensional ellipsoid, waves grazing the treetops travel roughly half a wavelength ($\lambda / 2 \approx 2.58\text{ cm}$ at $5.8\text{ GHz}$) farther than the direct optical ray, arriving $180^\circ$ out of phase at the receiving dish and canceling the direct signal by $6\text{ dB}$ to $15\text{ dB}$. Before bolting the dishes at their current tower height, the engineer works through three propagation problems:
1. Calculate the Friis Free-Space Path Loss across the $12.0\text{ km}$ valley at $5800\text{ MHz}$.
2. Evaluate the complete logarithmic link budget and fade margin, and solve backward for maximum hop range and required transmitter power.
3. Compute the First Fresnel Zone radius at mid-span to verify that the sightline clears the pine ridge by the $60\%$ diffraction-free criterion.

---

## Spherical Wave Spreading and the Friis Transmission Equation

When an electromagnetic wave leaves a transmitting antenna and travels through unobstructed air or vacuum, no energy is dissipated as heat in the vacuum. Instead, the signal weakens with distance because a fixed number of watts is spread over an ever-larger spherical surface while the receiving antenna intercepts only a tiny patch of that sphere.

### Isotropic Effective Aperture and Free-Space Path Loss

Imagine a hypothetical **isotropic radiator** emitting total radio-frequency power $P_{\text{tx}}$ uniformly in all directions. At distance $d$ (in meters), that radiated power is distributed evenly over a sphere of surface area $4\pi d^2$, producing a power flux density of $S = P_{\text{tx}} / (4\pi d^2)\text{ W/m}^2$. By electromagnetic reciprocity and thermodynamics, an isotropic receiving antenna immersed in a wave of wavelength $\lambda = c / f$ ({{key:c}} $= 299{,}792{,}458\text{ m/s}$) captures an **effective aperture area** of $A_{\text{eff,iso}} = \lambda^2 / (4\pi)$. Multiplying the incident flux density $S$ by $A_{\text{eff,iso}}$ yields Harald T. Friis's 1946 free-space transmission ratio:

$$\frac{P_{\text{rx,iso}}}{P_{\text{tx,iso}}} = \left(\frac{\lambda}{4\pi d}\right)^2 = \left(\frac{c}{4\pi d f}\right)^2, \qquad \text{FSPL} = \left(\frac{4\pi d f}{c}\right)^2$$

Notice why higher-frequency microwave links suffer higher path loss between isotropic antennas even though vacuum is non-absorptive: as frequency $f$ increases and wavelength $\lambda = c / f$ shrinks, the electrical capture area $\lambda^2 / (4\pi)$ of an isotropic antenna shrinks with the square of wavelength. Converting the dimensionless inverse ratio $\text{FSPL}$ into decibels and expressing path length $d_{\text{km}}$ in kilometers ($d = 10^3 d_{\text{km}}$) and carrier frequency $f_{\text{MHz}}$ in megahertz ($f = 10^6 f_{\text{MHz}}$), where $20\log_{10}(4\pi \times 10^9 / 299{,}792{,}458) \approx 32.4418\text{ dB}$, gives the engineering **Free-Space Path Loss** ({{key:FSL}}) equation:

$$\text{FSPL}_{\text{dB}} = 20 \log_{10}(d_{\text{km}}) + 20 \log_{10}(f_{\text{MHz}}) + 32.44$$

In this expression, $d_{\text{km}}$ is the line-of-sight hop distance in kilometers, $f_{\text{MHz}}$ is the carrier frequency in megahertz, and $\text{FSPL}_{\text{dB}}$ is the positive isotropic path attenuation in decibels. Doubling either the hop distance $d_{\text{km}}$ or the carrier frequency $f_{\text{MHz}}$ adds $20\log_{10}(2) \approx \mathbf{6.02\text{ dB}}$ of path loss.

For our mountain valley backhaul spanning $d_{\text{km}} = 12.0\text{ km}$ at $f_{\text{MHz}} = 5800\text{ MHz}$, the distance term contributes $20\log_{10}(12.0) \approx 21.584\text{ dB}$ and the frequency term contributes $20\log_{10}(5800) \approx 75.269\text{ dB}$. Summing the three terms yields the free-space path loss across the valley:

$$\text{FSPL}_{\text{dB}} = 21.584 + 75.269 + 32.44 = \mathbf{129.292\text{ dB}}$$

An attenuation of $129.292\text{ dB}$ means that an isotropic receiving antenna $12\text{ km}$ away would capture only $10^{-12.9292} \approx 1.177 \times 10^{-13}$ (roughly one ten-trillionth) of the transmitted power.

### Logarithmic Link Budgets and Fade Margin Accounting

To overcome that thirteen-order-of-magnitude free-space spreading loss, microwave engineers collimate the transmitted wave and enlarge the receiving capture aperture using high-gain parabolic dish antennas. Because logarithms turn multiplication and division of linear power ratios into addition and subtraction of decibels, the **Effective Isotropic Radiated Power** ($\text{EIRP}_{\text{dBm}} = P_{\text{tx,dBm}} + G_{\text{tx,dBi}} - L_{\text{line,dB}}$) and end-to-end **Link Budget** ({{key:LNK}}) combine transmitter output power $P_{\text{tx}}$ (in $\text{dBm}$), total net antenna and amplifier gains $G = G_{\text{tx}} + G_{\text{rx}}$ (in $\text{dBi}$), and total link losses $L = \text{FSPL}_{\text{dB}} + L_{\text{misc}}$ (in $\text{dB}$):

$$P_{\text{rx,dBm}} = P_{\text{tx,dBm}} + G_{\text{dB}} - L_{\text{dB}}, \qquad M_{\text{fade}} = P_{\text{rx,dBm}} - S_{\text{min,dBm}}$$

Here $P_{\text{rx,dBm}}$ is the unfaded received signal power in $\text{dBm}$, $S_{\text{min,dBm}}$ is the receiver's minimum sensitivity threshold for a target modulation scheme and bit-error rate, and $M_{\text{fade}}$ is the link's **Fade Margin** in $\text{dB}$ against heavy rain, snow, or atmospheric multipath ducting.

On our $12.0\text{ km}$, $5800\text{ MHz}$ link, the $P_{\text{tx}} = 250\text{ mW}$ transmitter delivers $10\log_{10}(250) \approx \mathbf{+23.979\text{ dBm}}$ (and an $\text{EIRP}$ of $23.979 + 26.0 = \mathbf{+49.979\text{ dBm}}$). Adding the combined $+52.0\text{ dB}$ dish gain and subtracting the $129.292\text{ dB}$ free-space path loss yields the unfaded received signal level:

$$P_{\text{rx,dBm}} = 23.979\text{ dBm} + 52.0\text{ dB} - 129.292\text{ dB} = \mathbf{-53.313\text{ dBm}}$$

Compared against the receiver's $-78.0\text{ dBm}$ demodulation threshold, the link achieves an unfaded fade margin of $M_{\text{fade}} = -53.313 - (-78.0) = \mathbf{24.687\text{ dB}}$ (and meets the $-55.0\text{ dBm}$ design target with $1.69\text{ dB}$ to spare)—provided the mid-span pine ridge does not introduce diffraction loss.

---

## Huygens Wavelets and Fresnel Zone Diffraction Clearance

Why does an obstacle that lies *below* the straight-line optical path between two antennas still attenuate a microwave signal? In 1818, the French physicist Augustin-Jean Fresnel answered that question by combining Christiaan Huygens's principle of secondary spherical wavelets with phase interference.

### Ellipsoidal Phase Zones and Half-Wavelength Destructive Interference

At any intermediate plane perpendicular to the straight line of sight of length $d = d_1 + d_2$ between a transmitter and a receiver, the advancing wavefront can be decomposed into concentric annular rings—**Fresnel Zones**—defined by the excess path length $\Delta d = (r_{\text{tx}} + r_{\text{rx}}) - d$ that a secondary wavelet travels from the transmitter through a point at radial offset $r_n$ to the receiver. The boundary of the $n\text{th}$ Fresnel Zone is the locus of points where that excess path length equals $n$ half-wavelengths ($\Delta d = n \lambda / 2$). At the midpoint of a link of total distance $d_{\text{km}}$ (in kilometers, where $d_1 = d_2 = d_{\text{km}} / 2$) operating at frequency $f_{\text{GHz}}$ (in gigahertz), paraxial geometry ($\Delta d \approx r_1^2 / (2 d_1) + r_1^2 / (2 d_2) = 2 r_1^2 / d = \lambda / 2$) yields the midpoint radius $r_1$ of the **First Fresnel Zone** ({{key:F₁}}, in meters):

$$r_1 = \sqrt{\frac{\lambda \cdot d}{4}} = 17.32 \sqrt{\frac{d_{\text{km}}}{4 f_{\text{GHz}}}} = 8.656 \sqrt{\frac{d_{\text{km}}}{f_{\text{GHz}}}}\quad [\text{m}]$$

In this expression, $d_{\text{km}}$ is the total hop length in kilometers, $f_{\text{GHz}}$ is the carrier frequency in gigahertz, and $r_1$ is the midpoint cross-sectional radius in meters of the first phase-coherent ellipsoid.

![First Fresnel Zone prolate ellipsoid clearance radius r1 between line-of-sight microwave antennas.](../assets/diagrams/domains/diagram_ch05_fresnel_zone.png)

Every Huygens wavelet passing *inside* the First Fresnel Zone ($r < r_1$) travels less than $\lambda / 2$ farther than the direct axial ray, so its phase shift is less than $180^\circ$ and it interferes **constructively** at the receiving dish. If a sharp granite ridge or dense canopy of wet pine needles rises right up to the optical sightline (grazing incidence, $0\text{ m}$ clearance), it blocks the entire bottom half of the First Fresnel Zone and introduces $\mathbf{6.0\text{ dB}}$ of knife-edge diffraction loss, cutting received power to one quarter. Even worse, if a smooth ridge or rooftop sits precisely at the boundary $r_1$ and reflects the wave with a $180^\circ$ reflection phase reversal plus the $180^\circ$ ($\lambda / 2$) path-length delay, or if an obstacle blocks the inner $60\%$ of the zone, destructive interference can gouge $10\text{ dB}$ to $20\text{ dB}$ out of the link budget.

### Sixty-Percent Clearance Criteria and Earth-Bulge Ridge Audits

In microwave path engineering, free-space propagation ($\approx 0\text{ dB}$ diffraction loss) is achieved whenever the optical sightline clears all terrain, foliage, and building obstacles by at least **$60\%$ of the First Fresnel Zone radius** ($h_{\text{clear}} \ge 0.60\,r_1$) after accounting for atmospheric refraction and Earth curvature:

$$h_{\text{clear,min}} = 0.60 \cdot r_1 = 0.60 \times 17.32 \sqrt{\frac{d_{\text{km}}}{4 f_{\text{GHz}}}}, \qquad h_{\text{earth,m}} = \frac{d_1 \cdot d_2}{2 K R_{\oplus}} \approx \frac{d_{\text{km}}^2}{68.0}$$

Here $h_{\text{clear,min}}$ is the required obstacle-free radius in meters for zero diffraction loss, and $h_{\text{earth,m}}$ is the midpoint vertical bulge of the spherical Earth in meters under a standard $K = 4/3$ effective Earth-radius atmosphere ($R_{\oplus} \approx 6371\text{ km}$).

For our $d_{\text{km}} = 12.0\text{ km}$ valley hop at $f_{\text{GHz}} = 5.8\text{ GHz}$, the midpoint First Fresnel Zone radius is:

$$r_1 = 17.32 \sqrt{\frac{12.0}{4 \times 5.8}} = 17.32 \sqrt{\frac{12.0}{23.2}} = 17.32 \sqrt{0.51724} \approx \mathbf{12.457\text{ m}}$$

Applying the $60\%$ diffraction-free rule specifies a minimum treetop clearance of $h_{\text{clear,min}} = 0.60 \times 12.457 \approx \mathbf{7.474\text{ m}}$ ($24.5\text{ ft}$) below the optical line of sight at mid-span, plus an Earth-curvature bulge of $h_{\text{earth}} \approx 12.0^2 / 68.0 \approx 2.12\text{ m}$. Because the transit survey shows the eighty-foot mid-span pines sitting $14.0\text{ m}$ below the optical sightline, the link clears the entire First Fresnel Zone ($14.0\text{ m} > 12.457\text{ m}$) and the $-53.313\text{ dBm}$ free-space link budget holds intact.

---

## Closing the Valley Link Budget and Clearing the Ridge on the Stack

The **SC-50** chains logarithmic milliwatt conversions ({{key:dBm}}, {{key:▸dBm}}, {{key:▸mW}}), Friis Free-Space Path Loss ({{key:FSL}}), three-register Link Budget summation ({{key:LNK}}, taking $P_{\text{tx}}$ in Register $Z$, net antenna gain $G$ in Register $Y$, and total path loss $L$ in Register $X$ computed in place by {{key:FSL}}), and First Fresnel Zone clearance ({{key:F₁}}) directly across the RPN stack, while also providing **Bidirectional Equation Solver Workspaces** ({{key:SOLVE}} / {{key:XEQ}}) for {{key:FSL}} (`L = 20LOG(D)+20LOG(F)+32.44`, softkeys {{keycap:L}}, {{keycap:D}}, {{keycap:F}}) and {{key:LNK}} (`R = P + G - L`, softkeys {{keycap:R}}, {{keycap:P}}, {{keycap:G}}, {{keycap:L}}):

| Button | Operation | Register Z | Register Y | Register X | Governing Expression & Solver Schema |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `{{key:FSL}}` | Free-Space Path Loss | — | Distance $d_{\text{km}}$ ($\text{km}$) | Frequency $f_{\text{MHz}}$ ($\text{MHz}$) | Stack: $20\log_{10}(d) + 20\log_{10}(f) + 32.44$; Solver: `{{keycap:L}}`,`{{keycap:D}}`,`{{keycap:F}}` |
| `{{key:LNK}}` | Link Budget Rx Power | Tx Power $P_{\text{tx}}$ ($\text{dBm}$) | Net Gain $G$ ($\text{dB}$) | Total Loss $L$ ($\text{dB}$) | Stack: $P_{\text{rx}} = P_{\text{tx}} + G - L$; Solver: `R = P + G - L` (`{{keycap:R}}`,`{{keycap:P}}`,`{{keycap:G}}`,`{{keycap:L}}`) |
| `{{key:F₁}}` | 1st Fresnel Zone Radius | — | Distance $d_{\text{km}}$ ($\text{km}$) | Frequency $f_{\text{GHz}}$ ($\text{GHz}$) | Immediate stack: $r_1 = 17.32 \sqrt{d / (4 f)} = 8.656 \sqrt{d / f}$ ($\text{m}$) |
| `{{key:COX}}` / `{{key:PAD}}` | Coax Loss & Resistive Pad | — | Base Loss ($\text{dB}$) | Freq Ratio / Attenuation | $\alpha(f) = \alpha_0 \sqrt{f/f_0}$ (`{{key:COX}}`); $50\ \Omega$ Pi/Tee attenuator (`{{key:PAD}}`) |
| `{{key:c}}` | Vacuum Speed of Light | — | — | — | Pushes $c = 299{,}792{,}458\text{ m/s}$ onto Register $X$ |

### Computing Free-Space Loss and Received Signal Power Across the Valley on the Stack

To close the $12.0\text{ km}$, $5800\text{ MHz}$ valley link on the stack, the engineer first converts $P_{\text{tx}} = 250\text{ mW}$ to $+23.979\text{ dBm}$ ({{key:▸dBm}}), loads the $+52.0\text{ dB}$ combined dish gain, evaluates the $129.292\text{ dB}$ free-space path loss in place with {{key:FSL}}, and presses {{key:LNK}} to resolve the received signal power $P_{\text{rx}}$:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `250 {{key:▸dBm}} 52 {{key:ENTER}}` | $0$ | $23.979$ | $52$ | $52$ | Convert $250\text{ mW}$ to $+23.979\text{ dBm}$ in $Z$; load dish gain $52\text{ dB}$ into $Y$ |
| `12 {{key:ENTER}} 5800 {{key:FSL}}` | $23.9794$ | $23.979$ | $52$ | $129.292$ | Evaluate $\text{FSPL} = 129.292\text{ dB}$ at $12\text{ km}, 5800\text{ MHz}$; $P_{\text{tx}}$ in $Z$, $G$ in $Y$ |
| `{{key:LNK}}` | $23.9794$ | $23.9794$ | $23.9794$ | **$-53.313$** | Evaluate link budget $P_{\text{rx}} = 23.979 + 52 - 129.292 = -53.313\text{ dBm}$ |

Notice how {{key:FSL}} consumes $d_{\text{km}} = 12$ and $f_{\text{MHz}} = 5800$ from Registers $Y$ and $X$, dropping $P_{\text{tx}} = 23.979\text{ dBm}$ into Register $Z$ and $G = 52\text{ dB}$ into Register $Y$ so that pressing {{key:LNK}} resolves $P_{\text{rx}} = \mathbf{-53.313\text{ dBm}}$ in a single keystroke.

### Auditing Mid-Span Pine Tree Clearance and Back-Solving Link Range & Power in the Solver Workspace

With $P_{\text{rx}} = -53.313\text{ dBm}$ sitting in Register $X$, the engineer evaluates the midpoint First Fresnel Zone radius $r_1$ at $d_{\text{km}} = 12.0\text{ km}$ and $f_{\text{GHz}} = 5.8\text{ GHz}$ using {{key:F₁}} (`12` {{key:ENTER}} `5.8` {{key:F₁}} `0.6` {{key:×}}), and then opens the {{key:FSL}} (`L = 20LOG(D)+20LOG(F)+32.44`) and {{key:LNK}} (`R = P + G - L`) Solver Workspaces to answer two inverse planning questions: first, what is the maximum line-of-sight hop distance $D$ ({{keycap:D}}) if rain-fade margin allows a maximum free-space path loss of $L = 132.44\text{ dB}$ at $F = 5800\text{ MHz}$. Second, what transmitter power $P$ ({{keycap:P}}) is required on an auxiliary telemetry link ($L = 118\text{ dB}, G = 34\text{ dBi}$) to achieve $R = -80.0\text{ dBm}$:

| Keystroke | Solver Display / Register X | What Happens on the Stack & in the `{{key:FSL}}` / `{{key:LNK}}` Solver Workspaces |
| :--- | :---: | :--- |
| `12 {{key:ENTER}} 5.8 {{key:F₁}} 0.6 {{key:×}}` | **$7.474$** | Evaluate $r_1 = 12.457\text{ m}$ via `{{key:F₁}}` and multiply by $0.60$ for $7.474\text{ m}$ clearance |
| `{{key:FSL}}` | `L=20LOG(D×F)+32.44` | Open the Free-Space Path Loss ({{key:FSL}}) Solver Workspace with softkeys `{{keycap:L}}`, `{{keycap:D}}`, `{{keycap:F}}` |
| `132.44 {{keycap:L}}` | $132.4400$ | Store maximum allowable path loss $L = 132.44\text{ dB}$ into softkey `{{keycap:L}}` (`{{keycap:LFU0}}`) |
| `5800 {{keycap:F}}` | $5{,}800.0000$ | Store carrier frequency $F = 5800\text{ MHz}$ into softkey `{{keycap:F}}` (`{{keycap:LFU2}}`) |
| `{{key:SOLVE}} {{keycap:D}}` | **$17.2414$** | Solve backward for maximum hop distance $D = 10^{(132.44-32.44)/20} / 5800 = \mathbf{17.2414\text{ km}}$ |
| `{{key:LNK}}` | `R=P+G-L` | Open the Link Budget ({{key:LNK}}) Solver Workspace with softkeys `{{keycap:R}}`, `{{keycap:P}}`, `{{keycap:G}}`, `{{keycap:L}}` |
| `80 {{key:+/-}} {{keycap:R}} 34 {{keycap:G}} 118 {{keycap:L}}` | $118.0000$ | Store target $R = -80\text{ dBm}$, gain $G = 34\text{ dB}$, and loss $L = 118\text{ dB}$ |
| `{{key:SOLVE}} {{keycap:P}} {{key:▸mW}}` | **$2.5119$** | Solve backward for $P = +4.00\text{ dBm}$ and convert to $\mathbf{2.5119\text{ mW}}$ |

### Try It on the Stack

Consolidate your mastery of free-space path loss, logarithmic link budgets, and Fresnel diffraction zones with these three field-engineering exercises:

1. **2.4 GHz Ten-Kilometer Campus Link Budget:** A $P_{\text{tx}} = 100\text{ mW}$ ($+20\text{ dBm}$) bridge operates at $f = 2400\text{ MHz}$ ($2.4\text{ GHz}$) across a $d = 10.0\text{ km}$ link using two $+24\text{ dBi}$ dishes ($G = 48\text{ dB}$). Find the free-space path loss and received power (`100` {{key:▸dBm}} `48` {{key:ENTER}} `10` {{key:ENTER}} `2400` {{key:FSL}} {{key:LNK}}). *(Verified Register $X$ results: $\text{FSPL} \approx \mathbf{120.044\text{ dB}}$ and $P_{\text{rx}} \approx \mathbf{-52.044\text{ dBm}}$.)*
2. **Six-Gigahertz Eighteen-Kilometer Fresnel Clearance Audit:** Evaluate the full First Fresnel Zone radius $r_1$ and the $60\%$ minimum obstacle clearance at mid-span across an $18.0\text{ km}$ hop operating at $6.0\text{ GHz}$ (`18` {{key:ENTER}} `6` {{key:F₁}} {{key:ENTER}} `0.6` {{key:×}}), and verify the inverse hop length from $r_1 = 15.0\text{ m}$ at $6.0\text{ GHz}$ (`15` {{key:ENTER}} `8.656` {{key:÷}} {{key:x²}} `6` {{key:×}}). *(Verified Register $X$ results: $r_1 \approx \mathbf{15.000\text{ m}}$, $0.6 r_1 \approx \mathbf{9.000\text{ m}}$, and $D = \mathbf{18.000\text{ km}}$.)*
3. **Millimeter-Wave 28 GHz Urban Backhaul Loss:** Compute the Free-Space Path Loss over a short $d = 2.5\text{ km}$ urban rooftop hop at $f = 28{,}000\text{ MHz}$ ($28\text{ GHz}$) and determine the received power for $P_{\text{tx}} = +15\text{ dBm}$ and $G = 70\text{ dB}$ combined dish gain (`15` {{key:ENTER}} `70` {{key:ENTER}} `2.5` {{key:ENTER}} `28000` {{key:FSL}} {{key:LNK}}). *(Verified Register $X$ results: $\text{FSPL} \approx \mathbf{129.339\text{ dB}}$ and $P_{\text{rx}} \approx \mathbf{-44.339\text{ dBm}}$.)*

Having delivered an electromagnetic wavefront across a mountain valley to the receiving antenna, we step inside the receiver front-end in Chapter 15 to rescue a weak satellite telemetry carrier from thermal electron noise and compute the channel's Shannon capacity.

---

# Chapter 15: Pulling a Weak Telemetry Signal Out of Thermal Noise

At a university satellite ground station, an engineering team is attempting to demodulate a weak $437.0\text{ MHz}$ telemetry carrier transmitted by a low-Earth-orbit CubeSat passing overhead at a radial closure velocity of $v = 7500\text{ m/s}$ over a $B = 1.0\text{ MHz}$ ($10^6\text{ Hz}$) receiver channel. In the station's initial cabling layout, the roof-mounted Yagi antenna feeds $30\text{ meters}$ of coaxial cable having $6.0\text{ dB}$ of passive insertion loss before reaching the equipment rack indoors. Downstairs on the bench sit a low-noise amplifier ($G_{\text{LNA}} = 20\text{ dB}$, noise figure $N\!F_1 = 1.5\text{ dB}$) and a software-defined radio receiver ($N\!F_{\text{rx}} = 8.0\text{ dB}$). With the LNA mounted *downstairs* at the rack after the $6.0\text{ dB}$ cable run, the telemetry waterfall display shows nothing but snow: the downlink signal is buried beneath the receiver system's noise floor.

Why does placing a $20\text{ dB}$ amplifier at the bottom of the coaxial run fail to rescue the signal, whereas climbing onto the roof and bolting that identical amplifier at the antenna masthead *ahead* of the $6.0\text{ dB}$ coaxial cable brings the telemetry packets into crystal-clear lock? Both configurations have the identical net system gain ($+20\text{ dB} - 6\text{ dB} = +14\text{ dB}$), yet their signal-to-noise ratios differ by more than a factor of three.

As Harald T. Friis proved in 1944, passive coaxial loss placed ahead of the first amplifier attenuates the delicate satellite signal while injecting room-temperature Johnson–Nyquist thermal noise. Moving the LNA to the masthead boosts the signal by $100\times$ ($+20\text{ dB}$) *before* the cable attenuation occurs, dividing the noise contribution of the cable and downstream receiver by one hundred. In this chapter, we follow three connected receiver-design themes:
1. Evaluate the Johnson–Nyquist thermal noise floor across a $1.0\text{ MHz}$ channel and compare the Friis cascaded noise figure with the LNA downstairs versus at the antenna masthead.
2. Quantify third-order intermodulation distortion ($\text{IIP}_3$) and Spurious-Free Dynamic Range ($\text{SFDR}$) when a strong nearby paging transmitter threatens to overload the LNA.
3. Calculate the Shannon–Hartley channel capacity limit in megabits per second, and track orbital Doppler shift and monostatic $R^4$ radar return.

---

## Thermal Noise Floors, Cascaded Amplifiers, and Receiver Linearity

Every radio receiver is ultimately bounded at the bottom of its dynamic range by the random thermal motion of electrons inside its own conductors, and bounded at the top by non-linear distortion in its active transistors and mixers.

### Johnson-Nyquist Thermal Agitation and the Friis Noise Cascade Law

In 1928, Bell Labs physicists John B. Johnson and Harry Nyquist demonstrated through statistical mechanics and fluctuation-dissipation theory that the random thermal agitation of charge carriers inside any matched resistor at absolute temperature $T_0$ ({{key:T₀}}) delivers an available noise power spectral density of $k_B T_0$ watts per hertz of bandwidth, independent of resistance value or frequency across the RF spectrum. At the IEEE standard reference temperature of $T_0 = 290\text{ K}$ ($16.85^\circ\text{C}$) with Boltzmann's constant $k_B = 1.380649 \times 10^{-23}\text{ J/K}$ ({{key:kB}}), the thermal noise power per hertz is $k_B T_0 \approx 4.0039 \times 10^{-21}\text{ W/Hz} = 4.0039 \times 10^{-18}\text{ mW/Hz}$, whose base-ten logarithm is $10\log_{10}(4.0039 \times 10^{-18}) \approx -173.977\text{ dBm/Hz} \approx -174\text{ dBm/Hz}$. Integrating across an effective receiver noise bandwidth $B_{\text{Hz}}$ (in hertz) defines the **Thermal Noise Floor** ({{key:Pₙ}}, in $\text{dBm}$):

$$N_{\text{floor,dBm}} = 10 \log_{10}(k_B T_0 \cdot 1000) + 10 \log_{10}(B_{\text{Hz}}) \approx -173.977 + 10 \log_{10}(B_{\text{Hz}})$$

When a signal passes through a cascade of amplifier, cable, and mixer stages having linear noise factors $F_i = \text{SNR}_{\text{in},i} / \text{SNR}_{\text{out},i} = 10^{N\!F_i / 10}$ and linear available power gains $G_i = 10^{\text{Gain}_i / 10}$, Harald Friis's 1944 cascade formula ({{key:NF}}) determines the overall linear **Total Noise Factor** $F_{\text{tot}}$ and decibel **Noise Figure** $N\!F_{\text{tot}} = 10\log_{10}(F_{\text{tot}})$:

$$F_{\text{tot}} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \dots, \qquad N\!F_{\text{tot,dB}} = 10 \log_{10}(F_{\text{tot}})$$

In this equation, $F_1$ and $G_1$ are the linear noise factor and linear power gain of the very first component following the antenna, and each subsequent stage's excess noise $(F_k - 1)$ is divided by the product of all preceding linear gains $G_1 G_2 \cdots G_{k-1}$. Notice also that a passive lossy component (such as a coaxial cable of insertion loss $L_{\text{dB}}$ at $290\text{ K}$) has linear gain $G_{\text{cable}} = 10^{-L_{\text{dB}} / 10} < 1$ and linear noise factor $F_{\text{cable}} = 1 / G_{\text{cable}} = 10^{+L_{\text{dB}} / 10}$.

Compare the two cabling configurations at our satellite ground station ($B_{\text{Hz}} = 1.0\text{ MHz} = 10^6\text{ Hz}$, where the thermal noise floor is $N_{\text{floor}} = -173.977 + 10\log_{10}(10^6) \approx \mathbf{-113.98\text{ dBm}}$):
- **Configuration A (Masthead LNA at the antenna, ahead of the $6\text{ dB}$ cable and $8\text{ dB}$ receiver):** Stage 1 is the LNA ($N\!F_1 = 1.5\text{ dB} \implies F_1 = 1.4125$, $G_1 = 20\text{ dB} \implies 100$). The $6.0\text{ dB}$ cable ($G_2 = 0.2512, F_2 = 3.9811$) and $8.0\text{ dB}$ receiver ($F_3 = 6.3096$) have a combined downstream noise factor of $F_{23} = F_2 + (F_3 - 1)/G_2 = 3.9811 + 5.3096 / 0.2512 \approx \mathbf{25.119}$ ($14.0\text{ dB}$). Because the masthead LNA precedes them with $G_1 = 100$, the total system noise factor is:

$$F_{\text{tot,masthead}} = 1.4125 + \frac{25.119 - 1}{100} = 1.4125 + 0.2412 = \mathbf{1.6537} \quad \left(N\!F_{\text{tot}} = 10\log_{10}(1.6537) \approx \mathbf{2.185\text{ dB}}\right)$$

- **Configuration B (Coaxial cable first, LNA downstairs in the shack):** Stage 1 is the $6.0\text{ dB}$ passive cable ($F_1 = 3.9811, G_1 = 0.2512$), followed by the LNA ($F_2 = 1.4125, G_2 = 100$) and receiver ($F_3 = 6.3096$). Dividing by $G_1 = 0.2512$ *multiplies* the downstream noise by $3.9811$:

$$F_{\text{tot,shack}} = 3.9811 + \frac{1.4125 - 1}{0.2512} + \frac{6.3096 - 1}{0.2512 \times 100} = 3.9811 + 1.6422 + 0.2114 = \mathbf{5.8347} \quad \left(N\!F_{\text{tot}} \approx \mathbf{7.660\text{ dB}}\right)$$

Moving the LNA to the masthead improves the system noise figure from $7.660\text{ dB}$ down to $2.185\text{ dB}$—a $\mathbf{5.475\text{ dB}}$ ($3.53\times$) improvement in signal-to-noise ratio that pulls the CubeSat telemetry carrier out of the snow!

### Third-Order Intermodulation Intercepts and Spurious-Free Dynamic Range

While high LNA gain improves weak-signal sensitivity, excessive gain can overload downstream mixers when strong adjacent broadcast or pager transmitters are present. When two strong interfering tones at frequencies $f_1$ and $f_2$ pass through a weakly non-linear amplifier, cubic distortion generates **third-order intermodulation products** at $2f_1 - f_2$ and $2f_2 - f_1$ that fall right back inside the receiver passband and grow $3\text{ dB}$ for every $1\text{ dB}$ increase in input power.

![Receiver linearity plot showing fundamental (1:1) and third-order intermodulation (3:1) power slopes, IIP3 intercept, and SFDR.](../assets/diagrams/domains/diagram_ch05_iip3_sfdr.png)

Extrapolating the $1:1$ fundamental power line and the $3:1$ third-order distortion line on a log-log plot defines the **Input Third-Order Intercept Point** ({{key:IP3}}, in $\text{dBm}$), which bounds the receiver's **Spurious-Free Dynamic Range** ({{key:FDR}}, in $\text{dB}$) above the effective noise floor $N_{\text{floor,dBm}}$:

$$\text{SFDR}_{\text{dB}} = \frac{2}{3}\left(\text{IIP3}_{\text{dBm}} - N_{\text{floor,dBm}}\right)$$

For a receiver front-end with $\text{IIP3} = +5.0\text{ dBm}$ and an effective noise floor of $N_{\text{floor}} = -100.0\text{ dBm}$, the spurious-free dynamic range spans $\text{SFDR} = \frac{2}{3}(5.0 - (-100.0)) = \mathbf{70.0\text{ dB}}$.

---

## Shannon-Hartley Channel Capacity and Radar Doppler Propagation

Once the masthead LNA delivers a clean Signal-to-Noise Power Ratio ($\text{SNR}$) to the demodulator, information theory and relativistic wave kinematics govern how many bits per second the channel can carry and how the satellite's orbital velocity shifts the carrier frequency.

### Spectral Efficiency and the Noisy-Channel Coding Limit

In his landmark 1948 theorem, Claude Shannon proved that for a communication channel of bandwidth $B$ (in hertz) perturbed by additive white Gaussian noise where the received signal power is $P_{\text{signal}}$ and the total in-band noise power is $P_{\text{noise}}$ (giving linear signal-to-noise ratio $\text{SNR} = P_{\text{signal}} / P_{\text{noise}} = 10^{\text{SNR}_{\text{dB}} / 10}$), there exist error-correcting codes that can transmit information with arbitrarily small error probability at any rate up to the **Shannon–Hartley Channel Capacity** $C$ ({{key:C/B}}, in bits per second, $\text{bps}$):

$$C = B \log_2\left(1 + \text{SNR}\right) \quad [\text{bps}], \qquad \eta = \frac{C}{B} = \log_2\left(1 + \text{SNR}\right) \quad \left[\frac{\text{bits/s}}{\text{Hz}}\right]$$

Here $B$ is the channel bandwidth in hertz, $\text{SNR}$ is the dimensionless linear signal-to-noise power ratio, $C$ is the maximum theoretical error-free data rate in $\text{bps}$, and $\eta = C / B$ is the **spectral efficiency** in $\text{bits/s/Hz}$. At high signal-to-noise ratios ($\text{SNR} \gg 1$), spectral efficiency grows as $\eta \approx \log_2(\text{SNR}) = \text{SNR}_{\text{dB}} / (10\log_{10} 2) = \text{SNR}_{\text{dB}} / 3.0103\text{ bits/s/Hz}$ per power ratio (or $\text{SNR}_{\text{dB}} / 6.0206$ amplitude bits per sample)—the exact information-theoretic dual of the Effective Number of Bits $\text{ENOB} = (\text{SINAD}_{\text{dB}} - 1.7609) / 6.0206$ of a mixed-signal Analog-to-Digital Converter in [Unit III: Digital Systems, Bitwise Logic & Embedded Timing](03-sc16-systems-cyber.md).

On our CubeSat ground station's $B = 1.0\text{ MHz}$ ($10^6\text{ Hz}$) channel, if the masthead LNA upgrade raises the linear signal-to-noise ratio to $\text{SNR} = 15.0$ ($\text{SNR}_{\text{dB}} = 10\log_{10}(15) \approx 11.76\text{ dB}$), the spectral efficiency reaches $\eta = \log_2(1 + 15) = \log_2(16) = \mathbf{4.00\text{ bits/s/Hz}}$, supporting a theoretical error-free channel capacity of $C = 10^6 \times 4.00 = \mathbf{4.00\text{ Mbps}}$ ($4{,}000{,}000\text{ bps}$). Even when a deep-space probe operates below the noise floor at $\text{SNR} = 0.25$ ($-6.02\text{ dB}$), $\log_2(1.25) \approx 0.3219\text{ bits/s/Hz}$ still permits $321.9\text{ kbps}$ across a $1\text{ MHz}$ spread-spectrum channel.

### Monostatic Fourth-Power Radar Range and Relativistic Doppler Shift

When a ground station or monostatic radar tracks a moving spacecraft or aircraft of radial velocity $v$ (in $\text{m/s}$) and radar cross-section $\sigma$ (in $\text{m}^2$) at range $R$, wave compression shifts the carrier frequency $f_0$ ({{key:Δf}}, which takes carrier frequency $f_0$ in Register $Y$ and closing velocity $v$ in Register $X$ to return the one-way Doppler shift $\Delta f_{\text{1-way}} = f_0 v / c$ in Register $X$ and the two-way monostatic radar Doppler shift $\Delta f_{\text{2-way}} = 2 f_0 v / c$ in Register $Y$), while two-way spherical spreading ($1 / (4\pi R^2)$ outbound and $1 / (4\pi R^2)$ inbound) causes the radar echo power $P_{\text{echo}}$ to fall off inversely with the **fourth power of range** ({{key:RCS}}):

$$\Delta f_{\text{1-way}} = \frac{f_0 \cdot v}{c}, \qquad \Delta f_{\text{2-way}} = \frac{2 \cdot f_0 \cdot v}{c}, \qquad P_{\text{echo}} = \frac{P_{\text{tx}} G^2 \lambda^2 \sigma}{(4\pi)^3 R^4} \implies \text{Radar Factor} = \frac{\sigma}{(4\pi)^3 R^4}$$

For our CubeSat transmitting at $f_0 = 437.0\text{ MHz}$ ($4.37 \times 10^8\text{ Hz}$) with a radial closure speed of $v = 7500\text{ m/s}$ (`437` {{key:ENTER}} `7500` {{key:Δf}}), the one-way telemetry downlink shift in Register $X$ is $\Delta f_{\text{1-way}} = (4.37 \times 10^8 \times 7500) / 299{,}792{,}458 \approx \mathbf{10{,}932.6\text{ Hz}}$ ($10.93\text{ kHz}$), and the two-way monostatic radar shift in Register $Y$ is $\Delta f_{\text{2-way}} \approx \mathbf{21{,}865.1\text{ Hz}}$ ($21.87\text{ kHz}$). Because two-way radar return scales with $\sigma / ((4\pi)^3 R^4)$ ({{key:RCS}} with range $R$ in Register $Y$ and cross-section $\sigma$ in Register $X$), doubling a radar's maximum detection range $R_{\max}$ requires increasing transmitter power sixteen-fold ($2^4 = 16$, or $+12.04\text{ dB}$).

---

## Rescuing Weak Telemetry Signals and Auditing Channel Capacity on the Stack

The **SC-50** executes two-stage and multi-stage Friis noise cascades ({{key:NF}} taking $F_1$ in Register $Z$, $F_2$ in Register $Y$, and linear gain $G_1$ in Register $X$), thermal noise floor evaluation ({{key:Pₙ}}, {{key:T₀}}, {{key:kB}}), third-order intermodulation and spurious-free dynamic range ({{key:IP3}}, {{key:FDR}}), Shannon–Hartley channel capacity ({{key:C/B}}), and Doppler / monostatic radar cross-section scaling ({{key:Δf}}, {{key:RCS}}) directly on the RPN stack, while providing **Bidirectional Equation Solver Workspaces** ({{key:SOLVE}} / {{key:XEQ}}) for {{key:NF}} (`F = A + (B - 1) / G`, softkeys {{keycap:F}}, {{keycap:A}}, {{keycap:B}}, {{keycap:G}}) and {{key:C/B}} (`C = B × LN(1 + S) / LN(2)`, softkeys {{keycap:C}}, {{keycap:B}}, {{keycap:S}}):

| Button | Operation | Register Z | Register Y | Register X | Governing Expression & Solver Schema |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `{{key:NF}}` | 2-Stage Friis Factor | Linear $F_1$ | Linear $F_2$ | Linear Gain $G_1$ | Stack: $F_1 + (F_2 - 1) / G_1$; Solver: `F = A + (B - 1) / G` (`{{keycap:F}}`,`{{keycap:A}}`,`{{keycap:B}}`,`{{keycap:G}}`) |
| `{{key:Pₙ}}` | Thermal Noise Floor | — | — | Bandwidth $B_{\text{Hz}}$ ($\text{Hz}$) | Immediate stack: $-173.977 + 10\log_{10}(B_{\text{Hz}})$ ($\text{dBm}$) |
| `{{key:T₀}}` / `{{key:kB}}` | Thermal Reference & Boltzmann | — | — | — | Pushes $T_0 = 290\text{ K}$ (`{{key:T₀}}`) or $k_B = 1.380649 \times 10^{-23}\text{ J/K}$ (`{{key:kB}}`) |
| `{{key:FDR}}` / `{{key:IP3}}` | Spurious-Free Dynamic Range | — | $\text{IIP3}$ ($\text{dBm}$) | $N_{\text{floor}}$ ($\text{dBm}$) | $\text{SFDR}_{\text{dB}} = \frac{2}{3}(\text{IIP3} - N_{\text{floor}})$ (`{{key:FDR}}`); cascaded IIP3 (`{{key:IP3}}`) |
| `{{key:C/B}}` | Shannon–Hartley Capacity | — | Bandwidth $B$ ($\text{Hz}$) | Linear $\text{SNR}$ | Stack: $C = B \log_2(1 + \text{SNR})$; Solver: `C = B × LOG2(1 + S)` (`{{keycap:C}}`,`{{keycap:B}}`,`{{keycap:S}}`) |
| `{{key:Δf}}` | One-Way & Two-Way Doppler | — | Carrier $f_0$ ($\text{MHz}$/$\text{Hz}$) | Velocity $v$ ($\text{m/s}$) | $X' = f_0 v / c$ (1-way $\text{Hz}$), $Y' = 2 f_0 v / c$ (2-way radar $\text{Hz}$) |
| `{{key:RCS}}` | Monostatic Radar Factor | — | Range $R$ ($\text{m}$) | Cross-Section $\sigma$ ($\text{m}^2$) | Two-way geometric factor $\sigma / ((4\pi)^3 R^4)$ (and dB in $Y$) |

### Comparing Masthead LNA Placement Against Coaxial Cable Loss on the Stack

To verify the masthead LNA upgrade on the stack, the engineer evaluates the downstream cable-plus-receiver noise factor ($F_2 = 3.9811, G_2 = 0.2512$ for the $6\text{ dB}$ cable ahead of $F_3 = 6.3096$ for the $8\text{ dB}$ receiver, giving $F_{23} = 25.119$), and then computes the total linear noise factor $F_{\text{tot}}$ with the masthead LNA ($F_1 = 1.4125, G_1 = 100$) placed first versus placing a $3\text{ dB}$ cable ($F = 2.0, G = 0.5$) before an LNA ($F = 1.25, G = 20$):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `3.9811 {{key:ENTER}} 6.3096 {{key:ENTER}} 0.2512 {{key:NF}}` | $0$ | $0$ | $0$ | $25.118$ | Cable ($6\text{ dB}$) + Receiver ($8\text{ dB}$) combined factor $F_{23} = 25.118$ ($14.0\text{ dB}$) |
| `1.4125 {{key:x⇄y}} 100 {{key:NF}}` | $0$ | $0$ | $0$ | $1.654$ | Masthead LNA ($F_1 = 1.4125, G_1 = 100$) ahead of $F_{23}$ yields $F_{\text{tot}} = 1.654$ ($2.18\text{ dB}$) |
| `1.25 {{key:ENTER}} 2 {{key:ENTER}} 20 {{key:NF}}` | $1.6537$ | $1.6537$ | $1.654$ | $1.3$ | Reference check: LNA ($F=1.25, G=20$) before $3\text{ dB}$ coax ($F=2$) gives $F_{\text{tot}} = 1.30$ |
| `2 {{key:ENTER}} 1.25 {{key:ENTER}} 0.5 {{key:NF}}` | $1.3$ | $1.3$ | $1.3$ | **$2.5$** | Reversing order ($3\text{ dB}$ coax before LNA) degrades noise factor to $F_{\text{tot}} = 2.50$ |

### Evaluating Thermal Noise, Shannon Capacity, and Orbital Doppler Shift on the Stack

Next, the engineer evaluates the thermal noise floor over the $B = 1.0\text{ MHz}$ ($10^6\text{ Hz}$) downlink channel ({{key:Pₙ}}), checks the receiver's Spurious-Free Dynamic Range for $\text{IIP3} = +8.0\text{ dBm}$ ({{key:FDR}}), calculates the Shannon–Hartley channel capacity at linear $\text{SNR} = 15$ ({{key:C/B}}), and finds the one-way and two-way Doppler shifts at $f_0 = 437\text{ MHz}$ and $v = 7500\text{ m/s}$ ({{key:Δf}}):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `8 {{key:ENTER}} 1000000 {{key:Pₙ}}` | $0$ | $0$ | $8$ | $-113.977$ | Thermal noise floor $N_{\text{floor}} = -113.98\text{ dBm}$ at $B = 1\text{ MHz}$; $\text{IIP3} = 8$ in $Y$ |
| `{{key:FDR}}` | $0$ | $0$ | $0$ | $81.318$ | Spurious-Free Dynamic Range $\text{SFDR} = \frac{2}{3}(8 - (-113.977)) = 81.32\text{ dB}$ |
| `1000000 {{key:ENTER}} 15 {{key:C/B}}` | $0$ | $0$ | $81.318$ | $4000000$ | Shannon capacity $C = 10^6 \log_2(1 + 15) = 4.00\text{ Mbps}$ ($4{,}000{,}000\text{ bps}$) |
| `437 {{key:ENTER}} 7500 {{key:Δf}}` | $81.318$ | $4000000$ | $21865.1$ | **$10932.6$** | One-way downlink shift $\Delta f = 10{,}932.6\text{ Hz}$ in $X$; two-way radar shift $21{,}865.1\text{ Hz}$ in $Y$ |

### Back-Solving Required SNR and Maximum Stage Noise Factor in the Solver Workspace

Suppose a high-speed X-band payload downlink must deliver a target error-free data rate of $C = 50\text{ Mbps}$ ($5 \times 10^7\text{ bps}$) across a channel bandwidth of $B = 20\text{ MHz}$ ($2 \times 10^7\text{ Hz}$), and the engineer needs the minimum required linear Signal-to-Noise Ratio $S$ ({{keycap:S}}), while also solving backward in the {{key:NF}} workspace (`F = A + (B - 1) / G`) for the maximum allowable second-stage noise factor $B$ ({{keycap:B}}) when $F_{\text{tot}} = 1.6537$, $A = 1.4125$, and $G = 100$. Opening the {{key:C/B}} and {{key:NF}} Solver Workspaces resolves both inverse requirements directly:

| Keystroke | Solver Display / Register X | What Happens in the `{{key:C/B}}` & `{{key:NF}}` Solver Workspaces |
| :--- | :---: | :--- |
| `{{key:C/B}}` | `C=B×LN(1+S)/LN(2)` | Open the Shannon–Hartley ({{key:C/B}}) Solver Workspace with softkeys `{{keycap:C}}`, `{{keycap:B}}`, `{{keycap:S}}` |
| `5 {{key:E}} 7 {{keycap:C}}` | $5.0000 \times 10^7$ | Store required data rate $C = 50\text{ Mbps}$ ($5 \times 10^7\text{ bps}$) into softkey `{{keycap:C}}` (`{{keycap:LFU0}}`) |
| `2 {{key:E}} 7 {{keycap:B}}` | $2.0000 \times 10^7$ | Store channel bandwidth $B = 20\text{ MHz}$ ($2 \times 10^7\text{ Hz}$) into softkey `{{keycap:B}}` (`{{keycap:LFU1}}`) |
| `{{key:SOLVE}} {{keycap:S}}` | **$4.6569$** | Solve backward for minimum linear $\text{SNR} = 2^{50/20} - 1 = 2^{2.5} - 1 = \mathbf{4.6569}$ ($6.68\text{ dB}$) |
| `{{key:NF}}` | `F=A+(B-1)/G` | Open the Friis Noise Factor ({{key:NF}}) Solver Workspace with softkeys `{{keycap:F}}`, `{{keycap:A}}`, `{{keycap:B}}`, `{{keycap:G}}` |
| `1.6537 {{keycap:F}} 1.4125 {{keycap:A}} 100 {{keycap:G}}` | $100.0000$ | Store target $F_{\text{tot}} = 1.6537$, LNA $F_1 = 1.4125$, and LNA gain $G_1 = 100$ |
| `{{key:SOLVE}} {{keycap:B}}` | **$25.1200$** | Solve backward for maximum downstream noise factor $F_{23} = \mathbf{25.12}$ ($14.0\text{ dB}$) |

### Try It on the Stack

Test your command of Friis receiver cascades, dynamic range, Shannon capacity, and radar Doppler scaling with these three telemetry and radar exercises:

1. **Three-Stage Receiver Chain and Narrowband SFDR:** Evaluate a three-stage receiver with Stage 1 ($F_1 = 1.25, G_1 = 20$), Stage 2 ($F_2 = 2.0, G_2 = 0.5$), and Stage 3 ($F_3 = 4.0$) by cascading Stage 2 + Stage 3 first (`2` {{key:ENTER}} `4` {{key:ENTER}} `0.5` {{key:NF}}) and then placing Stage 1 ahead of that result (`1.25` {{key:x⇄y}} `20` {{key:NF}}). Then compute the thermal noise floor and $\text{SFDR}$ for $\text{IIP3} = +12.0\text{ dBm}$ over a $B = 200\text{ kHz}$ channel (`12` {{key:ENTER}} `200000` {{key:Pₙ}} {{key:FDR}}). *(Verified Register $X$ results: $F_{\text{tot}} = \mathbf{1.60}$, $N_{\text{floor}} \approx \mathbf{-120.97\text{ dBm}}$, and $\text{SFDR} \approx \mathbf{88.65\text{ dB}}$.)*
2. **20 MHz Wireless Local Loop Shannon Capacity:** A $B = 20\text{ MHz}$ ($2 \times 10^7\text{ Hz}$) wireless backhaul operates at a linear Signal-to-Noise Ratio of $\text{SNR} = 31.0$ ($14.91\text{ dB}$). Find the theoretical Shannon capacity in megabits per second (`2` {{key:E}} `7` {{key:ENTER}} `31` {{key:C/B}} `1` {{key:E}} `6` {{key:÷}}). *(Verified Register $X$ result: $C = \mathbf{100.0\text{ Mbps}}$ at $5.0\text{ bits/s/Hz}$.)*
3. **X-Band Weather Radar Doppler Shift and Cross-Section Factor:** An X-band radar at $f_0 = 10.0\text{ GHz}$ ($10{,}000\text{ MHz}$) tracks an aircraft of cross-section $\sigma = 2.5\text{ m}^2$ at range $R = 5000\text{ m}$ moving at radial speed $v = 150\text{ m/s}$. Compute the one-way and two-way Doppler shifts (`10000` {{key:ENTER}} `150` {{key:Δf}}) and the two-way geometric radar factor (`5000` {{key:ENTER}} `2.5` {{key:RCS}}). *(Verified Register $X$ and $Y$ results: $\Delta f_{\text{1-way}} \approx \mathbf{5{,}003.5\text{ Hz}}$, $\Delta f_{\text{2-way}} \approx \mathbf{10{,}006.9\text{ Hz}}$, and geometric factor $\sigma / ((4\pi)^3 R^4) \approx \mathbf{2.016 \times 10^{-18}}$ or $\mathbf{-176.96\text{ dB}}$.)*

Having traced electromagnetic waves from coaxial matching networks through free-space Fresnel zones and low-noise receiver cascades in Unit V, we step into the analytical wet lab in [Unit VI: Stoichiometry, Chemical Equilibrium & Wet-Lab Analytics](06-sc60-chemistry-wetlab.md) to count molecules by weighing grams, stabilize enzymatic buffers, and measure protein concentration with ultraviolet light.
