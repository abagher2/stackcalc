---
title: "SC-24 Cinema Optics, Broadcast Timecode & Sound Handbook"
description: "An applied guide to SMPTE drop-frame timecode, optical depth of field, exposure values, and acoustic decibel summing on the StackCalc 24."
---

# SC-24 Cinema Optics, Broadcast Timecode & Sound Handbook

> **Who this is for:** Anyone who loves photography, filmmaking, or audio production and wants to understand the exact mathematical physics connecting lenses, camera sensors, decibels, and broadcast video sync.

---

## 1. When Light and Sound Become Numbers

Every motion picture you have ever watched is an optical illusion. A projector or screen flashes twenty-four still photographs in front of your eyes every second. Because of the human brain's persistence of vision, our visual cortex fuses those discrete snapshots into the seamless illusion of continuous motion.

Our ears, by contrast, are far more sensitive to time. While our eyes are easily fooled by 24 frames a second, our hearing can detect an acoustic echo or phase delay of just a few milliseconds.

On a professional movie set or live broadcast production, these two worlds of physics—photons hitting camera sensors and sound waves striking microphones—must be synchronized down to the microsecond. A film crew operates under relentless pressure:
- When the sun is setting during "magic hour," the light drops by an entire exposure stop every five minutes.
- If a camera operator chooses the wrong f-stop, an actor leaning forward by two inches blurs completely out of focus.
- If a live sports broadcast drifts by a few frames, audio loses lip-sync, and the transmission misses satellite commercial break windows.

The **StackCalc 24 (SC-24)** puts frame-accurate SMPTE timecode arithmetic, optical depth-of-field geometry, Exposure Value ($EV$) lighting photometrics, and acoustic decibel summing onto a fast, dedicated RPN stack.

### Why Not Just Use a Phone App?

- **The Magic Hour Window:** When racing against fading daylight on an exterior film set, every minute costs thousands of dollars in crew wages. Unlocking a phone, squinting against glare, and tapping through menus wastes precious light. The SC-24 lets a 1st AC (Focus Puller) or Director of Photography calculate hyperfocal distances and neutral density filter factors in two tactile clicks.
- **Set Discipline & Silence:** Phone screens illuminate dark cinema sets and notifications distract actors during rehearsals. The SC-24 is a silent, non-radiating tool designed for professional working environments.
- **Frame-Accurate Arithmetic:** Standard calculators work in base-10 decimals, but film and broadcast video operate in mixed radices: 24 frames per second for film, 25 fps for European TV, and $29.97\text{ fps}$ for North American broadcast. Trying to add `01:14:22:18` to `00:45:10:12` on a decimal calculator requires endless manual conversions.

---

## 2. Core Concepts: How Cinematographers and Sound Engineers Think

### Concept 1: The 0.1% Color Mystery (SMPTE Drop-Frame Timecode)

Timecode is the universal coordinate system of media:

$$\mathbf{HH:MM:SS:FF} \quad (\text{Hours : Minutes : Seconds : Frames})$$

Why does North American television run at the bizarre rate of **$29.97\text{ frames per second}$** instead of an even $30.00$?

In the 1940s, black-and-white television ran at exactly $30\text{ fps}$. But in 1953, when color television was invented, engineers discovered that the new high-frequency color subcarrier ($3.58\text{ MHz}$) caused electrical interference with the audio carrier wave. To eliminate this interference, the broadcast industry decided to slow down the television frame rate by exactly **$0.1\%$**:

$$\text{Color Framerate} = \frac{30}{1.001} \approx 29.97002997\text{ fps}$$

This tiny $0.1\%$ difference creates a giant headache:
- At $30\text{ fps}$, 108,000 frames equal exactly 1 hour of wall-clock time.
- At $29.97\text{ fps}$, 108,000 frames take **1 hour, 3 seconds, and 18 frames**!

Over an hour of broadcast, video drifts nearly $3.6\text{ seconds}$ behind the wall clock. To fix this, the Society of Motion Picture and Television Engineers (SMPTE) created **Drop-Frame Timecode (DF)**:
- Every minute, the timecode counter **skips frame numbers 00 and 01**.
- **Exception:** To prevent over-correcting, it does *not* skip frames on minute numbers ending in zero (minutes 00, 10, 20, 30, 40, 50).

No actual video frames are deleted; only the numerical labels are dropped so the timecode display stays locked to real-world clocks. The SC-24 handles this drop-frame arithmetic automatically.

### Concept 2: The Slippery Edge of Focus (Depth of Field & Hyperfocal Distance)

A camera lens can only bring one exact distance into sharp mathematical focus. Points closer or farther away project onto the camera sensor as small, blurred discs of light called **Circles of Confusion ($CoC$)**.

```
              Lens
             |      |
    ---------\      /------------------- Sensor Plane
              \    /
               \  /  Focal Point
                \/
                /\   Blur Circle (Circle of Confusion)
    -----------/  \---------------------
```

As long as the circle of confusion is smaller than the human eye can distinguish at a standard viewing distance (roughly $0.03\text{ mm}$ on a Full Frame sensor, or $0.02\text{ mm}$ on Super 35mm cinema), the image appears tack-sharp. The region where blur is imperceptible is the **Depth of Field (DOF)**.

#### Hyperfocal Distance ($H$)
If you focus a lens on infinity, half the light is wasted on stars, and nearby foreground objects blur.

If you instead focus at the **Hyperfocal Distance ($H$)**, everything from **half that distance ($H/2$) all the way to infinity** remains in sharp focus:

$$H \approx \frac{f^2}{N \cdot c}$$

where $f$ is focal length (in mm), $N$ is f-stop number, and $c$ is circle of confusion (in mm).

### Concept 3: The Decibel Mystery & Acoustic Summation

Why is human hearing logarithmic rather than linear?

If you hear one person talking at a dinner table, and a second person speaks at the exact same volume, your ear does *not* perceive the room as twice as loud. To sound twice as loud to a human ear, sound energy must increase by roughly **ten times**!

Sound engineers measure acoustic pressure on a logarithmic decibel scale:

$$L_p = 20 \log_{10}\left(\frac{P}{P_0}\right) \quad [\text{dBSPL}]$$

where $P_0 = 20\,\mu\text{Pa}$ is the quietest sound a human ear can detect.

#### Adding Two Sound Sources ($dB\oplus$)
If a guitar amplifier produces $90\text{ dBSPL}$, and a second identical amplifier is turned on producing $90\text{ dBSPL}$, what is the total volume?

You cannot add decibels directly ($90 + 90 \ne 180$). You must convert back to linear power, add the energies, and take the logarithm again:

$$L_{\Sigma} = 10 \log_{10}\left(10^{90/10} + 10^{90/10}\right) = 10 \log_{10}(2 \times 10^9) = 90 + 3.01 \approx \mathbf{93\text{ dBSPL}}$$

**Two identical uncorrelated sound sources always add exactly $+3\text{ dB}$.** The SC-24 features a dedicated `[dB⊕]` key that sums sound levels in one step.

---

## 3. Real-World Field Walkthroughs

### Field Case 1: Editing a 2-Hour Live Concert (`Cinematography.com`)

A post-production editor is assembling two live camera reels recorded at $29.97\text{ fps}$ Drop-Frame:
- Reel 1 Duration: `01:14:28:12`
- Reel 2 Duration: `00:52:45:20`
What is the exact combined running time of the broadcast cut?

#### How to Solve It on the SC-24
1. Set framerate to $29.97\text{ DF}$ using softkey `[ TC ]`.
2. Enter Reel 1: `01142812` `[ENTER]`.
3. Enter Reel 2: `00524520` `[+]`.
4. Register $X$ displays: **`02:07:14:02`** (2 hours, 7 minutes, 14 seconds, and 2 frames).
The editor knows the exact master duration without manually tracking dropped frames.

---

### Field Case 2: Deep-Focus Landscape Cinematography (`r/cinematography`)

A filmmaker is shooting an exterior scene with a $35\text{mm}$ lens on a Full Frame cinema sensor ($c = 0.030\text{ mm}$) at $f/8$.
1. What is the hyperfocal distance?
2. If the lens is focused at the hyperfocal distance, how close can an actor stand to the camera and still remain sharp?

#### Step-by-Step Mechanics
1. **Compute Hyperfocal Distance:**
   - Formula: $H = \frac{f^2}{N \cdot c} = \frac{35^2}{8 \times 0.030} = \frac{1225}{0.24} = 5{,}104\text{ mm} \approx \mathbf{5.10\text{ meters}}$ ($16.7\text{ feet}$).
   - On the SC-24: `35` `[x²]` `8` `[÷]` `0.03` `[÷]` $\to$ **`5104 mm`**.
2. **Compute Minimum Sharp Distance:**
   - Near limit $= H / 2 = 5.10 / 2 = \mathbf{2.55\text{ meters}}$ ($8.4\text{ feet}$).
   - Everything from $8.4\text{ feet}$ out to the distant mountains on the horizon will be in focus.

---

## 4. Try It Yourself: Practice Problems

### Problem 1: Acoustic Decibel Summing
At a live concert, three uncorrelated noise sources are measured at the soundboard:
- Main PA: $96\text{ dBSPL}$
- Crowd cheering: $92\text{ dBSPL}$
- Stage monitor bleed: $88\text{ dBSPL}$
Calculate the total combined sound pressure level at the mixing console using `[dB⊕]`.
*(Solution: $10^{9.6} + 10^{9.2} + 10^{8.8} = 3.981 \times 10^9 + 1.585 \times 10^9 + 0.631 \times 10^9 = 6.197 \times 10^9$. $10 \log_{10}(6.197 \times 10^9) = \mathbf{97.92\text{ dBSPL}}$.)*

### Problem 2: Neutral Density (ND) Filter Selection
A cinematographer is filming outdoors at ISO 100 with a shutter speed of $1/50\text{ second}$. A light meter reading indicates an Exposure Value of $EV = 15$ (which requires $f/16$ for proper exposure).
However, the director wants a shallow depth of field at **$f/2.0$** (an increase of 6 full stops of light: $f/16 \to 11 \to 8 \to 5.6 \to 4 \to 2.8 \to 2$).
What optical density ($OD$) neutral density filter is required to cut 6 stops of light?
*(Solution: Each stop is $0.3\text{ OD}$. $6\text{ stops} \times 0.3 = \mathbf{1.8\text{ ND}}$ (an ND64 filter, transmitting only $1/64 = 1.56\%$ of light).)*

### Problem 3: Sound Delay Tower Alignment
At an outdoor music festival, a secondary speaker delay tower is positioned $175\text{ feet}$ away from the main stage. The air temperature is $20^\circ\text{C}$ (speed of sound $c \approx 1{,}125\text{ ft/s}$).
Calculate the required delay in milliseconds to sync the speakers.
*(Solution: $\text{Time} = \frac{175\text{ ft}}{1125\text{ ft/s}} = 0.1555\text{ seconds} = \mathbf{155.6\text{ milliseconds}}$.)*
