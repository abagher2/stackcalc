---
title: "SC-50 RF Spectrum, Transmission Lines & Microwave Handbook"
description: "An applied guide to complex impedance, reflection coefficients, VSWR, and Smith chart matching on the StackCalc 50."
---

# SC-50 RF Spectrum, Transmission Lines & Microwave Handbook

> **Who this is for:** Anyone who understands complex numbers ($a + jb$) and alternating current, but wants to know why high-frequency radio waves behave like sound echoes bouncing off canyon walls, and how engineers tune antennas to prevent expensive amplifiers from melting.

---

## 1. When Wires Stop Acting Like Wires

If you shout into a wide canyon, your voice travels outward through the air until it hits the opposite cliff face. Because solid granite has a vastly different acoustic density than thin air, the rock cannot absorb the sudden wave of kinetic energy. The sound wave bounces straight back as an audible echo.

At normal household frequencies ($60\text{ Hz}$ AC), electrical current travels along a copper wire smoothly and uniformly. The electromagnetic wavelength at $60\text{ Hz}$ is over $3{,}000\text{ miles}$ long—far larger than your house—so voltage is virtually identical everywhere along the cord.

Now crank the frequency up to $1\text{ Gigahertz}$ ($1{,}000{,}000{,}000\text{ cycles per second}$), the realm of Wi-Fi, cellular 5G, and aircraft radar.

At $1\text{ GHz}$, the wavelength shrinks to just **30 centimeters** (about one foot). A coaxial cable running from a radio transmitter to an antenna on a tower is no longer a simple static connection: it is a **distributed transmission line**. The electrical signal travels along the wire as an electromagnetic wave.

When that forward-traveling wave hits the antenna terminals, one of two things happens:
1. If the antenna’s electrical impedance **matches** the cable, the wave steps cleanly into the air and radiates into space as radio waves.
2. If the impedance **does not match**, the antenna acts like the granite cliff in our canyon: it cannot absorb the energy, and a portion of the wave **bounces backward down the cable toward the transmitter**.

That reflected wave collides with the incoming wave, creating standing hot spots of voltage along the feedline. Worse, when that reflected power hits the delicate output transistors of the transmitter, it is dissipated as instant heat. In a $100\text{-watt}$ or $1{,}000\text{-watt}$ transmitter, a mismatched antenna can melt a $\$500$ Gallium-Nitride (GaN) power transistor in milliseconds.

The **StackCalc 50 (SC-50)** is designed specifically to calculate these wave reflections. It pairs a native complex-number RPN stack with dedicated reflection engines, one-touch characteristic impedance toggles ($50\,\Omega \leftrightarrow 75\,\Omega$), Friis receiver noise figure accumulators, and transmission line matching tools.

### Why Not Just Use a Phone App?

- **The Tower Climbing Reality:** When a broadcast or cellular technician is climbing a 150-foot radio tower in gusty winds, tethered to a safety harness, a delicate touchscreen smartphone is an accident waiting to happen. The SC-50 features tactile keys that can be operated reliably with one hand while tethered to a climbing lanyard.
- **The $50\,\Omega$ vs. $75\,\Omega$ Compromise:** Why is the entire RF world built on $50\,\Omega$ and $75\,\Omega$? In the 1930s, electrical researchers discovered that for coaxial cables with air insulation, minimum signal loss (attenuation) occurs at $77\,\Omega$, while maximum power-handling capability occurs at $30\,\Omega$. Radio transmitters standardized on **$50\,\Omega$** as the sweet-spot compromise between power and loss. Cable television (CATV), which carries tiny microvolt signals over long neighborhood runs, standardized on **$75\,\Omega$** to minimize attenuation. The SC-50 lets you toggle between $50\,\Omega$ and $75\,\Omega$ reference systems with a single key.

---

## 2. Core Concepts: How RF and Microwave Engineers Think

### Concept 1: The Bouncing Wave and Reflection Coefficient ($\Gamma$)

When a transmission line with characteristic impedance $Z_0$ (usually $50\,\Omega$) connects to an antenna with complex load impedance $Z_L = R + jX$, the ratio of the reflected voltage wave to the forward voltage wave is the **Voltage Reflection Coefficient ($\Gamma$, Greek gamma)**:

$$\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0} = \rho \angle \theta$$

Because $Z_L$ is a complex number, $\Gamma$ is also a complex phasor with a magnitude ($\rho = |\Gamma| \le 1.0$) and a phase angle ($\theta$):
- **Perfect Match ($Z_L = 50\,\Omega$):** $\Gamma = \frac{50 - 50}{50 + 50} = \mathbf{0}$. Zero reflected wave; 100% of power radiates into the sky!
- **Open Circuit ($Z_L = \infty$):** $\Gamma = \mathbf{+1.0} \angle 0^\circ$. All voltage reflects back in-phase.
- **Short Circuit ($Z_L = 0$):** $\Gamma = \mathbf{-1.0} = 1.0 \angle 180^\circ$. All voltage reflects back inverted.

### Concept 2: Standing Waves (VSWR) & Return Loss

When forward and reflected waves pass through each other inside a cable, their peaks and troughs interfere constructively and destructively, creating a stationary wave pattern.

The ratio of the maximum voltage peak to the minimum voltage valley is the **Voltage Standing Wave Ratio (VSWR)**:

$$VSWR = \frac{1 + |\Gamma|}{1 - |\Gamma|} = \frac{1 + \rho}{1 - \rho}$$

- **Ideal Match:** $VSWR = \mathbf{1.0 : 1}$ (smooth, uniform voltage along the cable).
- **Good Commercial Antenna:** $VSWR \le \mathbf{1.5 : 1}$ ($4\%$ power reflected).
- **Dangerous Mismatch:** $VSWR \ge \mathbf{3.0 : 1}$ ($25\%$ or more power reflected backward into the transmitter!).

#### Return Loss ($RL$)
Engineers often prefer to express reflection efficiency on a decibel scale called **Return Loss**:

$$RL = -20 \log_{10}|\Gamma| \quad [\text{dB}]$$

A high return loss means the reflected wave has been heavily attenuated:
- $RL = 20\text{ dB} \iff |\Gamma| = 0.10 \iff 99\%$ of power is absorbed by the antenna.
- $RL = 10\text{ dB} \iff |\Gamma| = 0.316 \iff 90\%$ of power is absorbed ($10\%$ bounces back).

### Concept 3: Folding Infinity into a Circle (The Smith Chart)

In 1939, RCA engineer Phillip Smith grew tired of solving complex hyperbolic tangent equations to figure out how impedance changes as you travel along a transmission line.

He noticed something magical: if you map the infinite right half of the complex impedance plane ($R \ge 0$) onto the complex reflection coefficient $\Gamma$, **the entire infinite plane folds into a compact circular disk with a radius of 1.0**:

```
                 Short Circuit 
                   (Γ = -1)
                      *
                     / \
                    /   \     Center = 50 Ω Perfect Match (Γ = 0)
                   |  +  |
                    \   /
                     \ /
                      *
                  Open Circuit
                   (Γ = +1)
```

- The exact center of the circle is the **$50\,\Omega$ perfect match** ($\Gamma = 0$).
- The outer boundary rim is total reflection ($|\Gamma| = 1.0$).
- Moving down a coaxial cable corresponds simply to rotating clockwise around the center of the chart!

On the SC-50, pressing `[SMTH]` lets you navigate impedance transformations and design matching networks without needing paper charts.

### Concept 4: Listening to the Stars (Friis Cascaded Noise)

When a satellite dish points at deep space, the signal arriving from a spacecraft millions of miles away is unimaginably faint: often less than a billionth of a microwatt ($-120\text{ dBm}$).

Every electronic component generates natural thermal noise (random motion of electrons). To amplify a faint signal without burying it in hiss, engineers use a chain of amplifiers.

Harald Friis at Bell Labs discovered that the total noise figure ($F$) of an entire multi-stage receiver is dominated by the **very first stage**:

$$F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \dots$$

Notice the denominator: any noise added by stage 2 ($F_2$) is divided by the gain of stage 1 ($G_1$)! 

This explains why satellite dishes and cellular base stations always place a high-gain, Low Noise Amplifier (LNA) right at the antenna feedhorn on the mast, rather than down inside the warm building at the other end of a long, lossy cable.

---

## 3. Real-World Field Walkthroughs

### Field Case 1: Checking an Amateur Radio Antenna Match (`Microwaves101`)

An antenna analyzer measures the feedpoint impedance of a newly installed dipole antenna at $14.2\text{ MHz}$:
- Load impedance: $Z_L = 35 - j25\,\Omega$
- Reference line: $Z_0 = 50\,\Omega$
What is the reflection coefficient magnitude ($|\Gamma|$), the VSWR, and the Return Loss?

#### How to Solve It on the SC-50
1. Enter $Z_L$ on the complex stack:
   - `35` `[ENTER]` `25` `[+/-]` (Stack holds $35 - j25$).
2. Enter $Z_0$:
   - `50`
3. Tap `[SWR]`:
   - Register $X$ displays: **`1.884`** (**VSWR = $1.88 : 1$**).
   - Register $Y$ displays: **`0.3065`** (Reflection coefficient $|\Gamma| = 0.307$).
4. Tap `[f] [RL]`:
   - Register $X$ displays: **`10.27 dB`** (Return Loss).
   - About $90.6\%$ of the transmitter's power is radiating into the air, and $9.4\%$ is reflected back. A simple L-matching network can tune this to $1.0 : 1$.

---

### Field Case 2: Satellite Downlink Low-Noise Preamplifier (`EEVblog`)

A satellite ground station receiver consists of:
- Stage 1 (Masthead LNA): Noise Figure $= 0.8\text{ dB}$ ($F_1 = 1.202$), Gain $= 20\text{ dB}$ ($G_1 = 100$).
- Stage 2 (Coax Cable Run): Loss $= 3.0\text{ dB}$ ($F_2 = 2.0$, $G_2 = 0.50$).
- Stage 3 (Indoor Receiver): Noise Figure $= 6.0\text{ dB}$ ($F_3 = 3.98$).
What is the total cascaded noise figure of the receiving system?

#### Step-by-Step Mechanics
1. **Apply Friis Equation:**
   $$F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 \cdot G_2}$$
   $$F_{\text{total}} = 1.202 + \frac{2.0 - 1.0}{100} + \frac{3.98 - 1.0}{100 \times 0.50} = 1.202 + 0.010 + 0.0596 = \mathbf{1.2716}$$
2. **Convert Back to Decibels:**
   $$NF_{\text{total}} = 10 \log_{10}(1.2716) = \mathbf{1.04\text{ dB}}$$
   Even though the indoor receiver has a noisy $6\text{ dB}$ noise figure and the cable is lossy, the masthead LNA's $20\text{ dB}$ gain keeps the total system noise figure down to an ultra-clean $1.04\text{ dB}$!

---

## 4. Try It Yourself: Practice Problems

### Problem 1: Transmission Line Quarter-Wave Transformer
A high-frequency load has a purely resistive impedance $Z_L = 100\,\Omega$. You need to match it to a $50\,\Omega$ coaxial generator using a quarter-wavelength ($\lambda / 4$) section of transmission line.
Calculate the required characteristic impedance of the quarter-wave line: $Z_{\text{match}} = \sqrt{Z_0 \cdot Z_L}$.
*(Solution: $Z_{\text{match}} = \sqrt{50 \times 100} = \sqrt{5000} \approx \mathbf{70.71\,\Omega}$.)*

### Problem 2: Return Loss from Power Measurements
A forward-power directional coupler measures $100\text{ Watts}$ forward power toward an antenna and $4\text{ Watts}$ reflected power bouncing back.
1. What is the reflection coefficient magnitude $\rho = \sqrt{P_{\text{ref}} / P_{\text{fwd}}}$?
2. What is the Return Loss ($RL = -20 \log_{10}\rho$)?
3. What is the VSWR?
*(Solution: $\rho = \sqrt{4 / 100} = \mathbf{0.20}$. $RL = -20 \log_{10}(0.20) = \mathbf{13.98\text{ dB}}$. $VSWR = (1 + 0.20) / (1 - 0.20) = 1.20 / 0.80 = \mathbf{1.50 : 1}$.)*

### Problem 3: Resonant LC Tank Frequency
A resonant filter circuit consists of an inductor $L = 47\text{ nH}$ ($47 \times 10^{-9}\text{ H}$) and a capacitor $C = 10\text{ pF}$ ($10 \times 10^{-12}\text{ F}$).
Calculate the resonant frequency $f_0 = \frac{1}{2\pi\sqrt{LC}}$ in Megahertz.
*(Solution: $LC = 47 \times 10^{-9} \times 10 \times 10^{-12} = 4.7 \times 10^{-19}$. $\sqrt{LC} \approx 6.8556 \times 10^{-10}$. $2\pi\sqrt{LC} \approx 4.3075 \times 10^{-9}$. $f_0 = 1 / 4.3075 \times 10^{-9} = 232{,}150{,}000\text{ Hz} = \mathbf{232.15\text{ MHz}}$.)*
