---
title: "Unit IV: Cinema Optics, Broadcast Timecode & Live Acoustics"
description: "Three narrative engineering chapters mastering SMPTE drop-frame timecode, Super 35 rectilinear lens optics, hyperfocal depth of field, logarithmic exposure photometry, and stadium acoustic delay alignment on the SC-24."
---

# Unit IV: Cinema Optics, Broadcast Timecode & Live Acoustics

On June 15, 1878, at Leland Stanford's Palo Alto Stock Farm in California, the English photographer Eadweard Muybridge lined a whitewashed wooden shed with twenty-four wet-plate stereoscopic cameras spaced twenty-one inches apart. Across the dirt track, fine linen threads stretched from each brass lens shutter to an electrical contact switch. When the trotting mare Sallie Gardner dashed through the threads at thirty-six feet per second, she tripped the electromagnetic shutters in rapid succession. Each camera froze a discrete slice of motion at an exposure shorter than one two-thousandth of a second. For millennia, painters had depicted galloping horses with both forelegs extended forward and both hind legs stretched backward like a rocking horse. Muybridge's silver-gelatin silhouettes proved that when all four hooves leave the ground simultaneously, they gather beneath the horse's belly. Projected onto a screen through his spinning glass-disk zoopraxiscope, those discrete static photographs fused in the viewer's visual cortex into continuous, living motion. Half a century later, optical sound-on-film tracks required a constant linear transport velocity past an exciter lamp. Motion-picture studios responded by standardizing theatrical projection at twenty-four frames per second, establishing the foundational temporal quantum of cinema.

While cinema remained anchored to integer mechanical sprockets, the birth of color television in 1953 forced broadcast engineers on the National Television System Committee (NTSC) into a subtle frequency compromise. Since the 1940s, North American monochrome television had scanned thirty frames per second, locked to the $60\text{ Hz}$ alternating-current utility grid so power-supply hum bars would remain stationary on cathode-ray tubes. Squeezing a $3.579545\text{ MHz}$ chrominance subcarrier beside the $4.5\text{ MHz}$ frequency-modulated audio carrier threatened to create beat interference on millions of existing black-and-white sets. To prevent that interference, engineers reduced the horizontal line rate and frame rate by one part in a thousand ($1000/1001$). Slowing the video frame rate to $30/1.001 \approx 29.97003\text{ fps}$ caused a thirty-frame-per-second counter to fall $3.6\text{ seconds}$ ($108\text{ frames}$) behind atomic wall-clock time every hour. That drift motivated the Society of Motion Picture and Television Engineers (SMPTE) in 1967 to invent mixed-radix timecode and Drop-Frame label reconciliation.

Capturing and projecting a story across space demands an equally tight coordination between refractive optics and human sensory physiology. While the visual cortex forgives discrete temporal sampling at twenty-four frames per second, its spatial acuity and brightness adaptation operate over delicate geometric and logarithmic scales. Light rays refracted through a rectilinear cinema prime project a three-dimensional scene onto a flat Super 35 or Full-Frame silicon sensor across an angular field of view. Meanwhile, object points outside the plane of focus spread into blur disks whose permissible diameter—the Circle of Confusion ($C$)—sets the hyperfocal distance and conjugate depth-of-field limits. Simultaneously, camera assistants and lighting gaffers balance iris f-stops, rotary shutter angles, neutral-density glass, and blackbody color temperatures along base-two Exposure Value stops and micro-reciprocal degrees. A striking mathematical isomorphism unites photometry, acoustics, and spectroscopy. A neutral-density filter of optical density $D = 0.3010 \times \text{stops} = -\log_{10}(T_{\text{trans}})$ obeys the same base-ten exponential attenuation law as Beer–Lambert UV-Vis absorbance $A = \varepsilon b c = -\log_{10}(I/I_0)$ in wet-lab chemistry (Unit VI) and free-space path loss in radio-frequency link budgets (Unit V).

Human hearing reverses the visual perceptual hierarchy, trading coarse angular localization for millisecond temporal discrimination. Between 1895 and 1898, Harvard physicist Wallace Clement Sabine worked through quiet midnight hours hauling hundreds of Sanders Theatre seat cushions into the reverberant Fogg Lecture Hall. By timing the decay of a $512\text{ Hz}$ organ pipe with a chronograph, he formulated the architectural reverberation law. Fifty years later, Helmut Haas demonstrated the precedence effect in 1949. When two identical sound waves arrive at a listener's ears within a window of $1\text{ ms}$ to $30\text{ ms}$, the auditory cortex fuses them into a single sonic image anchored to the first-arriving wavefront.

The **SC-24 Cinema, Broadcast, Optics & Live Acoustics** calculator unites these temporal, optical, and acoustic laws for post-production editors, camera assistants, gaffers, and front-of-house sound engineers. Each chapter in this Unit follows a single production story through three related mathematical themes—building the physical concepts and worked examples first, and then executing them on the SC-24 stack and in its Equation Solver workspaces:

| Chapter | Narrative Problem | Mathematical Concepts | Three Chapter Themes |
| :--- | :--- | :--- | :--- |
| **Chapter 10** | Reconciling a live multi-reel documentary broadcast with a $+3.6\text{ s/hr}$ NTSC drift and a $120\text{ fps}$ slow-motion wildlife insert | Mixed-radix `HH:MM:SS:FF` arithmetic, $1000/1001$ NTSC pulldown, SMPTE drop-frame rules, and overcrank speed ramps | 1. Mixed-Radix Timecode & Frame Accounting<br>2. High-Speed Overcrank & 3:2 Telecine Cadence<br>3. NTSC $1000/1001$ Drift & Drop-Frame Reconciliation |
| **Chapter 11** | Holding focus on a Super 35 Steadicam close-up at dusk while balancing shutter angle, ND filtration, and Mired color gels | Rectilinear field of view, Circle of Confusion, hyperfocal conjugates, base-$2$ Exposure Value, Mired shifts, and inverse-square lux | 1. Rectilinear Framing & Angular Field of View<br>2. Hyperfocal Distance & Depth-of-Field Conjugates<br>3. Base-2 Exposure Reciprocity, ND Stops & Mired Gels |
| **Chapter 12** | Time-aligning a $45\text{ m}$ stadium delay tower at $25^\circ\text{C}$ and mapping SPL decay, boom-mic reach, and incoherent PA summation | Thermal speed of sound, Haas precedence delay, acoustic wavelength, inverse-square decibel loss, incoherent power summation, and Sabine $RT_{60}$ | 1. Thermal Speed of Sound & Haas Delay Alignment<br>2. Inverse-Square SPL Decay & Boom-Mic Reach<br>3. Incoherent Decibel Summation & Sabine Reverberation |

---

# Chapter 10: The Missing Three-Point-Six Seconds at the Broadcast Desk

Twenty minutes before a live coast-to-coast documentary premiere goes to air in New York, the master-control transmission producer notices a discrepancy between the edit bay sheet and the network's rubidium-locked studio clock. Two documentary reels cut on a non-linear timeline—Reel A running `01:14:28:12` and Reel B running `00:52:45:20` at a nominal $30\text{ fps}$—must be joined end-to-end with a high-speed wildlife B-roll sequence shot at $120\text{ fps}$ over $180\text{ captured frames}$ and conformed to theatrical $24\text{ fps}$ playback before the live satellite commercial break triggers at the top of the hour. Yet the archival field camera that recorded the primary interview reel had its timecode generator set to $29.97\text{ fps}$ Non-Drop-Frame (NDF) rather than broadcast Drop-Frame.

On a live network feed where satellite transponders and automated local-affiliate commercial inserters switch on the millisecond, a mismatch between nominal frame labels and physical wall-clock seconds is fatal. When a $29.97\text{ fps}$ video stream is indexed by a counter that requires thirty full frames to advance its seconds digit, every nominal hour of `01:00:00:00` on the timecode display actually consumes $3603.6\text{ seconds}$ of real earth rotation. By the end of a two-hour documentary, an uncompensated Non-Drop-Frame timeline runs more than seven seconds past the top-of-the-hour network break, clipping the closing credits in mid-sentence across two hundred affiliate stations.

To rescue the broadcast rundown before the countdown reaches zero, the post-production engineer works through three coupled temporal calculations:
1. Sum the two main reel addresses across mixed sexagesimal and frame radices, and convert between packed timecode (`HH.MMSSFF`), total integer frames, and decimal seconds.
2. Scale the $120\text{ fps}$ overcranked wildlife insert to its true $24\text{ fps}$ screen duration and exposure compensation.
3. Scale the nominal program runtime through the $1000/1001$ NTSC pulldown ratio, reconcile SMPTE's minute-boundary Drop-Frame counting rule, and solve backward for the exact frame budget allowed by the network's commercial window.

---

## Mixed-Radix Frame Indexing and Overcranked Time Scaling

Every motion-picture camera and broadcast deck records time as a discrete sequence of still images. Translating between the human language of hours, minutes, and seconds and the machine language of integer frame pulses requires a mixed-radix coordinate system coupled with linear rate scaling.

### Sexagesimal Timecode Rollovers and Integer Frame Conversion

To give every individual frame on a reel a unique, human-readable address across cameras, dual-system field audio recorders, and editing timelines, the Society of Motion Picture and Television Engineers standardized an eight-digit mixed-radix index known as **Timecode**:

$$\mathbf{HH:MM:SS:FF} \qquad (\text{Hours : Minutes : Seconds : Frames})$$

In this four-field representation, the first three fields obey sexagesimal Babylonian clock arithmetic—sixty seconds per minute ($\text{SS} \in [00, 59]$) and sixty minutes per hour ($\text{MM} \in [00, 59]$)—whereas the rightmost frame field (FF) counts modulo the nominal integer frame rate $R$, cycling from $00$ up to $R - 1$ (such as $00\text{–}23$ for cinema $24\text{ fps}$, $00\text{–}24$ for European PAL/SECAM $25\text{ fps}$, or $00\text{–}29$ for North American $30\text{ fps}$ video). On the **SC-24**, a timecode address is entered as a packed decimal literal `HH.MMSSFF` (so `01:14:28:12` is keyed as `1.142812`). Any timecode address converts to a cumulative integer frame count $F$ ({{key:▸FRM}}, using the frame rate staged in Register $Y$ or the cinema default $R = 24\text{ fps}$) and back to packed timecode ({{key:▸TC}}) or decimal elapsed seconds $S$ ({{key:TC}}) by expanding the sexagesimal fields into total seconds and multiplying or dividing by the framebase $R$:

$$S = 3600 \cdot \text{HH} + 60 \cdot \text{MM} + \text{SS} + \frac{\text{FF}}{R}, \qquad F = S \times R = \left(3600 \cdot \text{HH} + 60 \cdot \text{MM} + \text{SS}\right) R + \text{FF}$$

Here $S$ is the elapsed duration in seconds ($\text{s}$), $R$ is the frame rate in frames per second ($\text{fps}$), and $F$ is the exact count of frames since `00:00:00:00`. When adding ({{key:+TC}}) or subtracting ({{key:-TC}}) two packed timecode durations $A$ and $B$, arithmetic proceeds from right to left across the four radices, carrying $+1\text{ second}$ whenever the frame sum reaches or exceeds $R$, carrying $+1\text{ minute}$ whenever seconds reach $60$, and carrying $+1\text{ hour}$ whenever minutes reach $60$.

Consider the two documentary reels sitting on the broadcast desk at a nominal framebase of $R = 30\text{ fps}$: Reel A spans `01:14:28:12` (`1.142812`) and Reel B spans `00:52:45:20` (`0.524520`). Summing the rightmost frame fields gives $12 + 20 = 32\text{ frames}$. Dividing by $R = 30$ leaves a remainder of `:02` frames and carries $+1\text{ s}$ into the seconds column. Summing the seconds column gives $28 + 45 + 1 = 74\text{ s}$, which leaves `:14` seconds and carries $+1\text{ min}$. Summing the minutes column gives $14 + 52 + 1 = 67\text{ min}$, which leaves `:07` minutes and carries $+1\text{ hr}$. Summing the hours column gives $01 + 00 + 1 = 02\text{ hr}$, yielding a combined master reel address of **`02:07:14:02`** (`2.071402`). Expanded into total seconds and frames at $R = 30\text{ fps}$, Reel A contains $3600(1) + 60(14) + 28 + 12/30 = 4468.40\text{ s}$ ($134{,}052\text{ frames}$) and Reel B contains $60(52) + 45 + 20/30 = 3165.667\text{ s}$ ($94{,}970\text{ frames}$), whose integer sum is $229{,}022\text{ frames}$, or $7634.067\text{ nominal seconds}$.

### Variable Frame Rate Overcranking and Speed Ramp Ratios

In early hand-cranked silent cameras, an operator who turned the crank faster than normal captured more frames per second than the theater projector later replayed, stretching brief physical events into slow motion on screen—a craft term preserved today as **overcranking**. Conversely, cranking slower than the projection rate compressed long events into fast-motion time-lapse, known as **undercranking**. When a camera captures a scene at acquisition frame rate $R_{\text{shoot}}$ over a recording duration $t_{\text{shoot}}$ (collecting $F_{\text{total}} = R_{\text{shoot}} \cdot t_{\text{shoot}}$ total frames) and the editing timeline plays those frames back one-for-one at project base rate $R_{\text{play}}$, conservation of frame count $F_{\text{total}}$ governs the screen playback duration $t_{\text{play}}$, the time-stretch magnification factor $M_{\text{ramp}}$, and the base-two exposure stop loss $\Delta\text{EV}_{\text{fps}}$ ({{key:FPS}}):

$$F_{\text{total}} = R_{\text{shoot}} \cdot t_{\text{shoot}} = R_{\text{play}} \cdot t_{\text{play}}, \qquad M_{\text{ramp}} = \frac{R_{\text{shoot}}}{R_{\text{play}}}, \qquad \Delta\text{EV}_{\text{fps}} = \log_2\left(\frac{R_{\text{shoot}}}{R_{\text{play}}}\right)$$

In these relations, $R_{\text{play}}$ is the base delivery timeline frame rate staged in Register $Y$ (such as $24\text{ fps}$), $R_{\text{shoot}}$ is the camera sensor acquisition rate staged in Register $X$ (such as $60\text{ fps}$ or $120\text{ fps}$), $M_{\text{ramp}}$ is the dimensionless slow-motion playback factor deposited in Register $X$ by {{key:FPS}}, and $\Delta\text{EV}_{\text{fps}}$ is the exposure stop loss deposited in Register $Y$ by {{key:FPS}} (because raising the frame rate at a fixed rotary shutter angle shortens each frame's integration time proportionally).

For the documentary's high-speed wildlife B-roll shot—where a peregrine falcon strike was captured at $R_{\text{shoot}} = 120\text{ fps}$ for $t_{\text{shoot}} = 1.50\text{ s}$, yielding $F_{\text{total}} = 120 \times 1.50 = 180\text{ frames}$—conforming those $180\text{ frames}$ onto a theatrical $R_{\text{play}} = 24\text{ fps}$ timeline (`24` {{key:ENTER}} `120` {{key:FPS}}) stretches the time axis by $M_{\text{ramp}} = 120 / 24 = \mathbf{5.0\times}$ in Register $X$ (with an overcrank exposure loss of $\log_2(5) \approx \mathbf{2.3219\text{ EV}}$ in Register $Y$, or $60 / 24 = \mathbf{2.5\times}$ and $\log_2(2.5) \approx \mathbf{1.3219\text{ EV}}$ for a $60\text{ fps}$ shot), producing a screen playback duration of $t_{\text{play}} = 180 / 24 = \mathbf{7.50\text{ s}}$ (`00:00:07:12`, or `0.000712` at $24\text{ fps}$). If that same $180\text{-frame}$ burst is dropped directly onto the network's $30\text{ fps}$ broadcast master timeline, the time magnification becomes $M_{\text{ramp}} = 120 / 30 = \mathbf{4.0\times}$ and the insert runs for $t_{\text{play}} = 180 / 30 = \mathbf{6.00\text{ s}}$ (`00:00:06:00`).

---

## NTSC Subcarrier Pulldown and Drop-Frame Reconciliation

When a broadcast facility operates on North American fractional frame rates ($23.976\text{ fps}$, $29.97\text{ fps}$, or $59.94\text{ fps}$), the rate at which frames pass through the switcher no longer equals a whole integer per second. Reconciling integer frame labels with continuous atomic time requires tracking the $1000/1001$ frequency offset ({{key:DF}}) and applying SMPTE's deterministic label-skipping algorithm.

### The 1953 Color Subcarrier Offset and Wall-Clock Drift

When the NTSC added color to black-and-white television in 1953, engineers needed to interleave a high-frequency color burst subcarrier ($f_{\text{sc}}$) inside the existing $6\text{ MHz}$ channel without causing audible buzz in the $4.5\text{ MHz}$ sound carrier or visible dot crawl on monochrome screens. Choosing the sound carrier to equal $286$ times the horizontal line rate $f_H$ required pulling the horizontal scan rate down by a factor of $1000/1001$ (from $15{,}750\text{ Hz}$ to $15{,}734.2657\text{ Hz}$), which pulled the vertical field rate down from $60\text{ Hz}$ to $60/1.001 \approx 59.94\text{ Hz}$ and the frame rate down from $30\text{ fps}$ to $R_{\text{NTSC}}$:

$$R_{\text{NTSC}} = \frac{30}{1.001} = \frac{30{,}000}{1001} \approx 29.97002997\text{ fps}, \qquad t_{\text{real}} = t_{\text{nominal}} \times 1.001, \qquad \Delta t_{\text{drift}} = t_{\text{nominal}} \times 0.001$$

In this pulldown relationship, $t_{\text{nominal}} = F / 30$ is the apparent duration indicated by a Non-Drop-Frame (NDF) counter that increments one second every $30$ frames, $t_{\text{real}} = F / R_{\text{NTSC}}$ is the true wall-clock elapsed time in seconds ({{key:DF}}), and $\Delta t_{\text{drift}} = t_{\text{real}} - t_{\text{nominal}}$ is the cumulative clock error. Similarly, when theatrical $24\text{ fps}$ cinema masters are transferred to NTSC video via $2:3$ telecine pulldown ({{key:3:2}}), the cinema frame rate is pulled down by $1000/1001$ to $24 / 1.001 \approx 23.976024\text{ fps}$.

Because each physical NTSC video frame lasts $1.001 / 30 \approx 33.3667\text{ ms}$ instead of $33.3333\text{ ms}$, every $1000\text{ seconds}$ of nominal Non-Drop-Frame timecode actually takes $1001\text{ seconds}$ of wall-clock time to play out. Over a nominal one-hour program ($t_{\text{nominal}} = 3600\text{ s}$, or $F = 3600 \times 30 = 108{,}000\text{ frames}$), the true elapsed wall-clock duration is $t_{\text{real}} = 3600 \times 1.001 = \mathbf{3603.6\text{ s}}$. When the Non-Drop-Frame studio monitor reads `01:00:00:00`, the actual broadcast has run $\Delta t_{\text{drift}} = +3.6\text{ seconds}$ ($3.6\text{ s} \times 30\text{ fps} = \mathbf{108\text{ frames}}$) past the top of the hour. Across our documentary's two-reel nominal runtime of $t_{\text{nominal}} = 7634.067\text{ s}$ (`02:07:14:02`), playing those $229{,}022\text{ frames}$ at $29.97003\text{ fps}$ consumes $t_{\text{real}} = 7634.067 \times 1.001 = \mathbf{7641.701\text{ s}}$ of real time—an accumulated drift of $+7.634\text{ seconds}$ ($229\text{ frames}$).

### The SMPTE Drop-Frame Counting Rule Across Minute Boundaries

To force the eight-digit timecode display to match wall-clock time at $29.97\text{ fps}$ without cutting or deleting a single recorded image from the video stream, SMPTE invented **Drop-Frame** ({{key:DF}}) timecode. Because an NDF counter accumulates $+108\text{ extra frames}$ of lag every hour ($60\text{ minutes}$), the counter must skip ahead by $108$ numerical frame labels per hour, or $108 / 60 = 1.8\text{ frame labels per minute}$. Since a timecode display can only skip whole integer labels, skipping $2\text{ frame labels}$ at the start of every minute would drop $2 \times 60 = 120\text{ labels}$ per hour—overcorrecting by $12\text{ labels}$. Dropping $2\text{ labels}$ on nine out of every ten minutes removes $2 \times 9 = 18\text{ labels}$ every ten minutes, or $18 \times 6 = 108\text{ labels}$ per hour:

$$N_{\text{dropped}} = 2 \times \left(M_{\text{total}} - \left\lfloor \frac{M_{\text{total}}}{10} \right\rfloor\right), \qquad F_{\text{DF}} = 107{,}892 \cdot \text{HH} + 1798 \cdot \text{MM} + 2\left\lfloor \frac{\text{MM}}{10} \right\rfloor + 30 \cdot \text{SS} + \text{FF}$$

Here $M_{\text{total}} = 60 \cdot \text{HH} + \text{MM}$ is the total number of elapsed minute boundaries, $N_{\text{dropped}}$ is the cumulative count of skipped frame numbers (labels `:00` and `:01` omitted at the start of every minute except minutes `00`, `10`, `20`, `30`, `40`, and `50`), and $F_{\text{DF}}$ is the exact physical frame index corresponding to a Drop-Frame address `HH:MM:SS;FF` (written by convention with a semicolon before the frame field).

![SMPTE 29.97 drop-frame timecode minute-boundary label reconciliation across regular minutes and every tenth minute.](../assets/diagrams/domains/diagram_ch04_drop_frame.png)

At the end of the first minute, a Drop-Frame counter advances directly from `00:00:59;29` to `00:01:00;02`, skipping the numbers `:00` and `:01` while every recorded video frame remains intact. At the tenth minute boundary, it counts normally from `00:09:59;29` to `00:10:00;00`. Over one full hour (`01:00:00;00`), $M_{\text{total}} = 60$ and $N_{\text{dropped}} = 2(60 - 6) = 108\text{ dropped labels}$, so `01:00:00;00` corresponds to physical frame $F_{\text{DF}} = 108{,}000 - 108 = \mathbf{107{,}892\text{ frames}}$. At the true NTSC rate of $30{,}000 / 1001\text{ fps}$, those $107{,}892\text{ frames}$ occupy $107{,}892 \times 1.001 / 30 = \mathbf{3599.9964\text{ s}}$, locking the studio timecode display to atomic time within $3.6\text{ milliseconds}$ ($0.1\text{ frame}$) per hour.

---

## Synchronizing Broadcast Timelines on the Stack and in the Solver Workspace

On the **SC-24**, packed `HH.MMSSFF` timecode arithmetic ({{key:+TC}}, {{key:-TC}}), immediate frame-to-timecode conversions ({{key:▸FRM}}, {{key:▸TC}}), overcrank playback and exposure scaling ({{key:FPS}}), Drop-Frame drift scaling ({{key:DF}}), and the bidirectional {{key:TC}} Equation Solver Workspace (`F = S × R`, equivalently `S = F / R`) work together across any configured stack depth ({{keycap:4-LV}}, {{keycap:8-LV}}, or {{keycap:INF}} via {{key:FLAGS}}) while logging cue points to the `@CUES` edit decision list in {{key:▦}}.

| Key / Solver | Mode | Inputs / Softkeys (`{{keycap:LFU0}}`–`{{keycap:LFU2}}`) | Governing Expression |
| :--- | :--- | :--- | :--- |
| `{{key:FPS}}` | Immediate Stack | Register $Y$: Base rate $R_{\text{play}}$, Register $X$: Capture rate $R_{\text{shoot}}$ | $X' = R_{\text{shoot}} / R_{\text{play}}$ (playback factor), $Y' = \log_2(R_{\text{shoot}} / R_{\text{play}})$ (EV stop loss) |
| `{{key:+TC}}` | Immediate Stack | Register $Y$: `HH.MMSSFF` $A$, Register $X$: `HH.MMSSFF` $B$ | Mixed-radix sum $A + B$ (logs cue to `@CUES` in `{{key:▦}}`) |
| `{{key:-TC}}` | Immediate Stack | Register $Y$: `HH.MMSSFF` $A$, Register $X$: `HH.MMSSFF` $B$ | Mixed-radix difference $A - B$ with sexagesimal/frame borrow |
| `{{key:▸FRM}}` | Immediate Stack | Register $Y$: Rate $R$ (or $24\text{ fps}$ default), Register $X$: `HH.MMSSFF` | Expands `HH.MMSSFF` into integer frame count $F$ |
| `{{key:▸TC}}` | Immediate Stack | Register $Y$: Rate $R$ (or $24\text{ fps}$ default), Register $X$: Frame count $F$ | Packs integer frame count $F$ into `HH.MMSSFF` |
| `{{key:DF}}` | Immediate Stack | Register $X$: Nominal NDF duration $t_{\text{nom}}$ | Scales by $1.001$ NTSC pulldown: $t_{\text{real}} = 1.001 \cdot X$ |
| `{{key:TC}}` | Stack / Solver | Softkeys: `{{keycap:F}}` Frames, `{{keycap:S}}` Seconds, `{{keycap:R}}` Rate | Bidirectional solver for $F = S \times R$ ($S = F / R$; default $R = 24$) |

### Immediate Stack Trace: Packed Timecode Rollovers, Overcrank Scaling, and NTSC Drift

At the broadcast desk, the producer keys Reel A (`1.142812` for `01:14:28:12`) and Reel B (`0.524520` for `00:52:45:20`), sums them across mixed radices with {{key:+TC}}, expands the combined `HH.MMSSFF` address into integer frames at $30\text{ fps}$ with {{key:▸FRM}}, evaluates the $1.001$ NTSC wall-clock overrun with {{key:DF}}, and checks a $60\text{ fps}$ overcranked B-roll clip against $24\text{ fps}$ playback with {{key:FPS}}:

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `1.142812 {{key:ENTER}} 0.524520 {{key:+TC}}` | $0$ | $0$ | $0$ | $2.071402$ | Sum Reel A and Reel B across mixed radices to `02:07:14:02` (`2.071402` at $30\text{ fps}$) |
| `30 {{key:x⇄y}} {{key:▸FRM}}` | $0$ | $0$ | $0$ | $229022$ | Expand `02:07:14:02` at $R = 30\text{ fps}$ into $F = 229{,}022\text{ total frames}$ |
| `30 {{key:÷}}` | $0$ | $0$ | $0$ | $7634.0667$ | Convert frame total into nominal NDF seconds $t_{\text{nom}} = 7634.067\text{ s}$ |
| `{{key:DF}}` | $0$ | $0$ | $0$ | $7641.7007$ | Scale by $1.001$ NTSC pulldown: true wall-clock runtime $t_{\text{real}} = 7641.701\text{ s}$ |
| `24 {{key:ENTER}} 60 {{key:FPS}}` | $0$ | $7641.7007$ | $1.3219$ | **$2.5000$** | Compute $60/24 = 2.5\times$ slow-motion factor in $X$ and $1.3219\text{ EV}$ stop loss in $Y$ |

Subtracting $t_{\text{nom}} = 7634.067\text{ s}$ from $t_{\text{real}} = 7641.701\text{ s}$ reveals the $+7.634\text{ s}$ ($229\text{-frame}$) Non-Drop-Frame overrun, which the editor converts directly into a packed $30\text{ fps}$ trim duration via `30` {{key:ENTER}} `229` {{key:▸TC}} $\to$ **`0.000719`** (`00:00:07:19`).

### Bidirectional Solver Workspace ({{key:TC}}): Solving Backward for Frame Budgets

Suppose the network's automated satellite switcher allocates a strict broadcast act window of $S = 1650.0\text{ seconds}$ ($27\text{ minutes } 30\text{ seconds}$ of real atomic time), and the editor needs to know the exact total frame budget $F$ available when delivering at fractional NTSC $R = 29.97003\text{ fps}$ versus cinema $R = 23.976024\text{ fps}$, and then solve forward for the playback duration $S$ of the $F = 180\text{-frame}$ falcon slow-motion insert at $R = 24\text{ fps}$. Pressing {{key:TC}} opens the `TC: TIMECODE` Equation Workspace on Line 1 (`F = S × R`, equivalently `S = F / R`) and binds softkeys {{keycap:LFU0}}–{{keycap:LFU2}} to {{keycap:F}}, {{keycap:S}}, and {{keycap:R}}:

| Step & Action | Line 1 Workspace Formula | Softkey Legend Bar (`{{keycap:LFU0}}`–`{{keycap:LFU2}}`) | Register X Result & Physical Meaning |
| :--- | :--- | :--- | :--- |
| `{{key:TC}}` (open workspace) | `TC: F = S × R` | `{{keycap:F}}` `{{keycap:S}}` `{{keycap:R}}`=24 | Opens `{{key:TC}}` solver with cinema default $R = 24.0\text{ fps}$ pre-bound |
| `1650` $\to$ `{{keycap:S}}` | `TC: F = S × R` | `{{keycap:F}}` `{{keycap:S}}`=1650 `{{keycap:R}}`=24 | Stores broadcast act duration $S = 1650.0\text{ s}$ |
| `29.97003` $\to$ `{{keycap:R}}` | `TC: F = S × R` | `{{keycap:F}}` `{{keycap:S}}`=1650 `{{keycap:R}}`=29.97 | Stores fractional NTSC broadcast frame rate $R = 29.97003\text{ fps}$ |
| `{{key:XEQ}}` $\to$ `{{keycap:F}}` | `F = 49450.55` | `{{keycap:F}}`=49451 `{{keycap:S}}`=1650 `{{keycap:R}}`=29.97 | Solves for exact NTSC act capacity $F = \mathbf{49{,}450.5\text{ frames}}$ (`00:27:30;00` DF) |
| `23.976024` $\to$ `{{keycap:R}}`, `{{key:XEQ}}` $\to$ `{{keycap:F}}` | `F = 39560.44` | `{{keycap:F}}`=39560 `{{keycap:S}}`=1650 `{{keycap:R}}`=23.98 | Re-solves at $23.976\text{ fps}$ for cinema pulldown budget $F = \mathbf{39{,}560.4\text{ frames}}$ |
| `180` $\to$ `{{keycap:F}}`, `24` $\to$ `{{keycap:R}}`, `{{key:XEQ}}` $\to$ `{{keycap:S}}` | `S = 7.5000` | `{{keycap:F}}`=180 `{{keycap:S}}`=7.5 `{{keycap:R}}`=24 | Solves backward for $24\text{ fps}$ playback duration $S = 180 / 24 = \mathbf{7.50\text{ s}}$ |

Because {{keycap:S}}, {{keycap:R}}, and {{keycap:F}} remain bound in the workspace, changing a single delivery specification—such as switching {{keycap:R}} from `29.97003` to `23.976024` or `25` for European PAL delivery—recomputes the frame budget in two keystrokes without re-entering the segment duration.

### Try It on the Stack

Practice mixed-radix timecode rollovers, NTSC drop-frame reconciliation, and bidirectional {{key:TC}} solver workflows with these three broadcast desk exercises:

1. **Two-Hour Feature NTSC Drift in Seconds and Packed Timecode:** A feature film transfer runs for a nominal $2\text{ hours}$ (`2.000000` = $7200\text{ s}$) on a $30\text{ fps}$ Non-Drop-Frame timeline. Compute the integer frame count (`30` {{key:ENTER}} `2.000000` {{key:▸FRM}}), the true wall-clock duration at $29.97\text{ fps}$ (`30` {{key:÷}} {{key:DF}}), and the accumulated drift in frames (`7200` {{key:-}} `30` {{key:×}}). *(Verified Register $X$ results: $F = \mathbf{216{,}000\text{ frames}}$, $t_{\text{real}} = \mathbf{7207.2\text{ s}}$, and drift $\Delta F = \mathbf{216\text{ frames}}$ = `0.000706` via `30` {{key:ENTER}} `216` {{key:▸TC}}.)*
2. **Commercial Act Trim via Packed Timecode Subtraction:** An act must fit inside a `00:22:30:00` (`0.223000`) broadcast window at $30\text{ fps}$, but the current cut runs `00:24:12:18` (`0.241218`). Find the required trim as packed timecode and total frames (`0.241218` {{key:ENTER}} `0.223000` {{key:-TC}} `30` {{key:x⇄y}} {{key:▸FRM}}). *(Verified Register $X$ results: packed trim `0.014218` (`00:01:42:18`) and $\Delta F = \mathbf{3078\text{ frames}}$.)*
3. **High-Speed Phantom Overcrank at 240 fps in the {{key:TC}} Solver:** A tabletop liquid-pour commercial is shot at $R_{\text{shoot}} = 240\text{ fps}$ for $S = 0.85\text{ s}$ and played back at $R_{\text{play}} = 23.976\text{ fps}$. In the {{key:TC}} Solver Workspace, store `0.85` in {{keycap:S}} and `240` in {{keycap:R}}, solve via {{key:XEQ}} $\to$ {{keycap:F}}, then store `23.976` in {{keycap:R}} and solve via {{key:XEQ}} $\to$ {{keycap:S}}. *(Verified results: $F = \mathbf{204\text{ frames}}$ and screen playback duration $S \approx \mathbf{8.5085\text{ s}}$.)*

With the broadcast master clock and frame counters locked to atomic time, we move from the edit suite onto the exterior location set in Chapter 11 to hold optical focus and balance twilight exposure on a moving Steadicam close-up.

---

# Chapter 11: Holding Focus on the Steadicam Close-Up at Dusk

Out on a coastal bluff twenty minutes after sunset, a Steadicam operator and first assistant camera (1st AC) are preparing the final dramatic close-up of the shooting day. The camera body holds an ANSI/SMPTE Super 35 digital cinema sensor of active horizontal width $W = 24.89\text{ mm}$ (permissible Circle of Confusion $C = 0.025\text{ mm}$ for critical $4\text{K}$ Super 35 acquisition, or $C = 0.029\text{ mm}$–$0.030\text{ mm}$ on Full-Frame $36\text{ mm}$ reference gates) fitted with an $F = 50\text{ mm}$ prime lens set wide enough for twilight at aperture $f/2.8$ ($N = 2.8$). As the actor walks along a cliff path at a nominal focus distance of $s = 3.00\text{ m}$ ($3000\text{ mm}$) while the camera glides backward at $24\text{ fps}$ with a $180^\circ$ rotary shutter ($T = 1/48\text{ s}$), the 1st AC must know the horizontal field of view, the hyperfocal distance, and the exact near and far focus boundaries down to the centimeter so the actor's eyes never soften into blur. Immediately afterward, the operator switches to an $F = 35\text{ mm}$ wide-angle prime for a running tracking shot and asks what exact f-stop $N$ will lock the hyperfocal distance at $H = 4.50\text{ m}$ ($4500\text{ mm}$) so everything from $2.25\text{ m}$ to the horizon stays sharp without pulling focus.

At the same time, the director of photography and gaffer are racing the dropping horizon light. Ten minutes earlier, while shooting against the bright western sky, the camera carried an $\text{ND } 0.9$ neutral-density filter in the matte box to cut three stops of daylight so the lens could stay at $f/2.8$. Now, as twilight deepens, the gaffer brings up a $5600\text{ K}$ daylight HMI Fresnel fixture on a condor lift and a $3200\text{ K}$ tungsten practical lantern inside the cabin window, requiring a micro-reciprocal degree gel calculation to match the two blackbody sources and a rotary shutter check against the $60\text{ Hz}$ generator feeding the set.

Every decision on that bluff couples geometric optics to logarithmic photometry:
1. Determine the horizontal angular field of view across the Super 35 sensor and its Full-Frame equivalent focal length.
2. Calculate the hyperfocal distance and near/far sharpness boundaries around the actor at $3.00\text{ m}$, then solve backward for the f-stop that locks hyperfocal focus at $4.50\text{ m}$ on the $35\text{ mm}$ tracking shot.
3. Balance rotary shutter integration time, base-two Exposure Value stops, neutral-density optical attenuation, and Mired color-correction gels.

---

## Rectilinear Framing, Circle of Confusion, and Depth of Field

A motion-picture prime lens acts as a geometric transformer between three-dimensional set space and the flat two-dimensional plane of the film gate or silicon sensor. Two right-triangle relationships govern what the audience sees: the chief-ray field-of-view triangle across the sensor width $W$, and the marginal-ray blur cone across the iris aperture diameter $D_{\text{iris}} = F / N$.

### Sensor Format Geometry, Crop Factors, and Angular Field of View

When chief rays from a distant scene pass through the rear nodal point of a rectilinear lens focused at infinity, they form an inverted planar image at axial distance $F$ (the lens focal length, in millimeters, $\text{mm}$) behind the nodal point.

![Rectilinear pinhole lens projection mapping sensor width W and focal length f to angular field of view theta.](../assets/diagrams/domains/diagram_ch04_lens_fov.png)

The optical axis bisects the horizontal width $W$ (in $\text{mm}$) of the active sensor or film aperture into two congruent right triangles, each having an opposite leg of half-width $W / 2$ and an adjacent leg of focal length $F$. Doubling the half-angle inverse tangent defines the horizontal angular **Field of View** ({{key:FOV}}), denoted $A$ in degrees ($^\circ$), while the ratio of the $36\text{ mm}\times 24\text{ mm}$ Full-Frame diagonal ($43.2666\text{ mm}$) or horizontal width to a smaller format's dimension defines the format **Crop Factor** ({{key:▸35}}, {{key:▸16}}, and aspect ratio {{key:W:H}}):

$$A = 2 \arctan\left(\frac{W}{2F}\right), \qquad W_{\text{scene}} = 2 s \tan\left(\frac{A}{2}\right) = s \left(\frac{W}{F}\right), \qquad F_{\text{equiv}} = F \times K_{\text{crop}}$$

In these expressions, $W$ is the active horizontal sensor width in $\text{mm}$, $F$ is the lens focal length in $\text{mm}$, $A$ is the horizontal coverage angle in degrees, $s$ is the subject distance along the optical axis, and $K_{\text{crop}}$ scales focal length to its $35\text{ mm}$ Full-Frame ({{key:▸35}}, $K_{\text{crop}} \approx 1.5\times$ from Super 35) or Super 16 ({{key:▸16}}, $K_{\text{crop}} \approx 2.88\times$) equivalent angle of view.

On our Steadicam's ANSI/SMPTE Super 35 sensor ($W = 24.89\text{ mm}$) fitted with an $F = 50\text{ mm}$ prime lens, the half-width tangent ratio is $W / (2F) = 24.89 / 100 = 0.2489$. Taking the inverse tangent gives half-angle $\arctan(0.2489) \approx 13.977^\circ$, which doubles to a horizontal angular field of view of $A \approx \mathbf{27.954^\circ}$. At the actor's distance of $s = 3.00\text{ m}$, the frame spans a horizontal scene width of $W_{\text{scene}} = 3.00 \times (24.89 / 50) = \mathbf{1.493\text{ m}}$—a classic medium close-up with breathing room for the cliff horizon. On a Full-Frame VistaVision sensor ($W = 36.0\text{ mm}$), that same $50\text{ mm}$ lens opens up to $A = 2\arctan(36 / 100) \approx \mathbf{39.598^\circ}$, whereas matching the Super 35 framing on Full-Frame requires scaling focal length by $36.0 / 24.89 \approx 1.4464$ to an $F \approx \mathbf{72.3\text{ mm}}$ lens.

### Hyperfocal Distance and Conjugate Sharpness Boundaries

While the nodal chief rays set the framing angle $A$, the outer marginal rays passing through the finite iris diameter $D_{\text{iris}} = F / N$ (where $N$ is the dimensionless aperture f-number or T-stop) govern sharpness along the depth axis. In paraxial Gaussian optics, a lens focused at distance $s$ brings only object points lying on that exact plane to a mathematical point on the sensor. Points closer or farther than $s$ converge slightly behind or in front of the sensor plane, intersecting the silicon surface as a circular blur disk known as the **Circle of Confusion** ($C$).

![Optical ray-cone convergence through aperture diameter D = f/N forming a blur circle of confusion c on the sensor plane.](../assets/diagrams/domains/diagram_ch04_circle_of_confusion.png)

Because human visual acuity is finite when viewing a theater screen from a standard seating distance, any blur disk smaller than a critical diameter $C$ (standardized at $C = 0.029\text{ mm}$–$0.030\text{ mm}$ for $35\text{ mm}$ Full-Frame reference gates and $C = 0.025\text{ mm}$ for Super 35 cinema work) appears indistinguishable from a sharp point. The axial distance $H$ at which focusing the lens places the far boundary of acceptable sharpness at optical infinity ($\infty$) is the **Hyperfocal Distance** ({{key:DOF}}, {{key:HFD}}), which governs the **near focus limit** $D_{\text{near}}$, **far focus limit** $D_{\text{far}}$, and total **Depth of Field** $\Delta D = D_{\text{far}} - D_{\text{near}}$ for any subject distance $s < H$:

$$H = \frac{F^2}{N \cdot C}, \qquad D_{\text{near}} = \frac{H \cdot s}{H + s}, \qquad D_{\text{far}} = \frac{H \cdot s}{H - s}, \qquad \Delta D = D_{\text{far}} - D_{\text{near}} = \frac{2 H s^2}{H^2 - s^2}$$

Here $F$ is the focal length in $\text{mm}$, $N$ is the f-stop number, $C$ is the Circle of Confusion diameter in $\text{mm}$, $H$ is the hyperfocal distance (in $\text{mm}$ in the {{key:DOF}} solver workspace, or divided by $1000$ in meters on the immediate stack), and $s$ is the focus distance in the same length units as $H$. When the focus ring is set directly to the hyperfocal mark ($s = H$), the denominator of $D_{\text{far}}$ vanishes ($H - H = 0 \implies D_{\text{far}} \to \infty$) while $D_{\text{near}}$ reduces to $H^2 / (2H) = H / 2$, rendering everything from half the hyperfocal distance to the horizon acceptably sharp.

![Hyperfocal focus geometry (s = H) extending continuous acceptable sharpness from H/2 to optical infinity.](../assets/diagrams/domains/diagram_ch04_hyperfocal_zone.png)

On our Steadicam close-up with $F = 50\text{ mm}$ and $N = 2.8$ using the $C = 0.030\text{ mm}$ reference criterion (`50` {{key:ENTER}} `2.8` {{key:ENTER}} `0.03` {{key:DOF}}), the hyperfocal distance is $H = 50^2 / (2.8 \times 0.030) = 2500 / 0.084 \approx \mathbf{29{,}761.9\text{ mm}} \approx \mathbf{29.762\text{ m}}$ (or $H \approx \mathbf{30.788\text{ m}}$ with the 2-argument default $C = 0.029\text{ mm}$). With the lens focused on the actor at $s = 3.00\text{ m}$, the conjugate sharpness boundaries lie at:

$$D_{\text{near}} = \frac{29.762 \times 3.00}{29.762 + 3.00} = \frac{89.286}{32.762} \approx \mathbf{2.725\text{ m}}, \qquad D_{\text{far}} = \frac{29.762 \times 3.00}{29.762 - 3.00} = \frac{89.286}{26.762} \approx \mathbf{3.336\text{ m}}$$

The total depth-of-field window around the actor at $3.00\text{ m}$ spans $\Delta D = 3.336 - 2.725 = \mathbf{0.611\text{ m}}$ ($61.1\text{ cm}$)—extending $27.5\text{ cm}$ in front of the actor's eyes and $33.6\text{ cm}$ behind them. Conversely, when the operator mounts an $F = 35\text{ mm}$ prime on the Super 35 body ($C = 0.025\text{ mm}$) and wants to lock the hyperfocal distance at $H = 4.50\text{ m} = 4500\text{ mm}$, solving $H = F^2 / (N \cdot C)$ backward for $N$ yields $N = F^2 / (H \cdot C) = 35^2 / (4500 \times 0.025) = 1225 / 112.5 = \mathbf{10.889}$ (just under $f/11$).

---

## Logarithmic Exposure Reciprocity, Rotary Shutters, and Color Mireds

Once the focal length $F$ and aperture $N$ are chosen to establish framing and depth of field, the camera and lighting crews must regulate photon flux and spectral color temperature so the sensor records balanced exposure and uniform white point as dusk settles.

### Base-Two Exposure Value, Shutter Angles, Neutral Density, and Flicker-Free Windows

Because human brightness perception and silicon photo-site well capacity scale geometrically, cinematography measures exposure changes in base-two **stops**, where each $+1\text{ stop}$ step doubles photon exposure and each $-1\text{ stop}$ step halves it. Combining relative aperture irradiance ($\propto 1/N^2$) and frame integration time $T$ (in seconds) onto a unified base-two logarithmic scale defines **Exposure Value** ({{key:EV}}, {{key:▸EV}} at ISO $100$), while a spinning motion-picture rotary shutter of open sector angle $\theta_{\text{shutter}}$ ({{key:SHT}}, where $180^\circ$ is standard) sets integration time $T$ as a fraction of the frame period $1 / \text{FPS}$, and gray **Neutral Density** ({{key:▸ND}}) filters attenuate excess light according to base-ten optical density $D$:

$$N^2 = T \cdot 2^E \iff E = \log_2\left(\frac{N^2}{T}\right), \qquad T = \frac{\theta_{\text{shutter}}}{360^\circ \cdot \text{FPS}}, \qquad D = -\log_{10}(T_{\text{trans}}) = \log_{10}(2) \times \text{stops} \approx 0.30103 \times \text{stops}$$

In these photometric equations, $N$ is the lens f-number, $T$ is the exposure integration time in seconds, $E$ is the Exposure Value ($\text{EV}_{100}$), $\theta_{\text{shutter}} \in (0^\circ, 360^\circ]$ is the rotary shutter angle, $D$ is the dimensionless neutral-density filter rating ({{key:▸ND}} converts stops $s$ in Register $X$ into optical density $D = 0.3 \times s$ in Register $X$ and filter factor $2^s$ in Register $Y$), and $T_{\text{trans}} = 2^{-\text{stops}} = 10^{-D}$ is the fractional light transmittance. Notice the exact mathematical bridge between cinematography and analytical chemistry: just as an $\text{ND } 0.9$ filter ($D = 0.9$) reduces transmitted irradiance by $3\text{ stops}$ to $T_{\text{trans}} = 2^{-3} = 0.125$, a biochemical sample with UV-Vis absorbance $A = 0.903$ in Unit VI (`SC-60`) transmits $10^{-0.903} = 12.5\%$ of incident monochromatic light.

When filming under alternating-current discharge lamps or LED pulse-width-modulated drivers operating at line frequency $f_{\text{line}}$ ($60\text{ Hz}$ in North America or $50\text{ Hz}$ in Europe), the lamp intensity pulses at $2 f_{\text{line}}$ ($120\text{ Hz}$ or $100\text{ Hz}$). Avoiding rolling exposure bands across the frame ({{key:FLK}}) requires choosing a shutter integration time $T$ that integrates an integer number $k \in \{1, 2, 3, \dots\}$ of half-cycles:

$$T_{\text{flicker-free}} = \frac{k}{2 f_{\text{line}}}, \qquad \theta_{\text{flicker-free}} = 360^\circ \cdot \text{FPS} \cdot \left(\frac{k}{2 f_{\text{line}}}\right)$$

On our Steadicam setup rolling at $\text{FPS} = 24\text{ fps}$ with a standard $\theta_{\text{shutter}} = 180^\circ$ rotary shutter (`24` {{key:ENTER}} `180` {{key:SHT}}), the frame integration time is $T = 180^\circ / (360^\circ \times 24) = 1/48\text{ s} \approx \mathbf{0.020833\text{ s}}$ in Register $X$ with denominator $48$ in Register $Y$. Under an unballasted $60\text{ Hz}$ source ($120\text{ Hz}$ ripple), choosing $k = 2$ half-cycles sets $T = 1/60\text{ s}$, corresponding to a flicker-free shutter angle of $\theta_{\text{shutter}} = 360^\circ \times 24 / 60 = \mathbf{144^\circ}$. At $f/2.8$ ($N = 2.8$) and $T = 1/48\text{ s}$, the camera's native Exposure Value at ISO $100$ is $E = \log_2(2.8^2 \times 48) = \log_2(376.32) \approx \mathbf{8.556\text{ EV}}$. When the matte box held an $\text{ND } 0.9$ filter (`3` {{key:▸ND}} $\to D = 0.9$ in $X$ and filter factor $8\times$ in $Y$, cutting $\mathbf{3.0\text{ stops}}$), the lens accommodated a bright dusk sky at $8.556 + 3.0 = \mathbf{11.556\text{ EV}}$ without stopping down the iris.

### Inverse-Square Set Illuminance, Footcandles, and Mired Gel Shifts

To supplement the fading sky once the $\text{ND } 0.9$ filter is pulled from the matte box, the gaffer positions a spotlight of axial luminous intensity $I$ (in candelas, $\text{cd}$) at throw distance $D$ (in meters) from the actor, delivering incident metric **illuminance** $E_{\text{lx}}$ ({{key:LUX}}, {{key:▸lux}}, in lux, $\text{lm/m}^2$) or imperial **footcandles** $E_{\text{fc}}$ ({{key:▸fc}}, in $\text{lm/ft}^2$, where $1\text{ fc} = 10.76391\text{ lx}$) across a conical beam diameter $W_{\text{beam}}$ ({{key:BM°}}):

$$E_{\text{lx}} = \frac{I}{D^2}, \qquad E_{\text{fc}} = \frac{E_{\text{lx}}}{10.76391}, \qquad W_{\text{beam}} = 2 D \tan\left(\frac{\theta_{\text{beam}}}{2}\right)$$

![Inverse-square illuminance falloff and conical beam diameter W = 2d tan(theta/2) over throw distance d.](../assets/diagrams/domains/diagram_ch04_luminaire_beam.png)

Simultaneously, the gaffer must reconcile the spectral color temperature of the $3200\text{ K}$ tungsten cabin lantern with the $5600\text{ K}$ daylight twilight and HMI key light. Because Wien's radiation displacement law ties peak blackbody wavelength to the reciprocal of absolute temperature $T_K$, scaling $1 / T_K$ by one million defines **Micro-Reciprocal Degrees** ({{key:▸MRD}}, $M = 10^6 / T_K$) and the linear **Mired filter shift** $\Delta M$ ({{key:GEL}}) required to convert source temperature $T_{\text{source}}$ to target temperature $T_{\text{target}}$:

$$M = \frac{10^6}{T_K}, \qquad \Delta M = \frac{10^6}{T_{\text{target}}} - \frac{10^6}{T_{\text{source}}}$$

Here a positive shift ($\Delta M > 0$) calls for an amber **Color Temperature Orange** (CTO) gel to warm a daylight source toward tungsten, whereas a negative shift ($\Delta M < 0$) calls for a blue **Color Temperature Blue** (CTB) gel to cool a $T_{\text{source}} = 3200\text{ K}$ tungsten lamp ($M_{\text{source}} = 10^6 / 3200 = 312.50\text{ Mireds}$) up to $T_{\text{target}} = 5600\text{ K}$ daylight ($M_{\text{target}} = 10^6 / 5600 = 178.57\text{ Mireds}$), yielding $\Delta M = 178.57 - 312.50 = \mathbf{-133.93\text{ Mireds}}$ (a Full CTB gel).

---

## Pulling Focus and Balancing Dusk Exposure on the Stack and in the Solver Workspace

On the **SC-24**, optical framing ({{key:FOV}}, {{key:W:H}}, {{key:▸35}}, {{key:▸16}}), hyperfocal depth of field ({{key:DOF}}, {{key:HFD}}), exposure reciprocity ({{key:EV}}, {{key:SHT}}, {{key:▸EV}}, {{key:▸ND}}), and lighting photometry ({{key:LUX}}, {{key:▸lux}}, {{key:▸fc}}, {{key:GEL}}, {{key:▸MRD}}) operate both as immediate RPN stack shortcuts and as bidirectional Equation Solver Workspaces ({{key:FOV}}, {{key:DOF}}, {{key:EV}}, {{key:LUX}}).

| Key / Solver | Mode | Inputs / Softkeys (`{{keycap:LFU0}}`–`{{keycap:LFU3}}`) | Governing Expression |
| :--- | :--- | :--- | :--- |
| `{{key:FOV}}` | Stack / Solver | Stack: $Y = W$, $X = F$ • Solver: `{{keycap:A}}` `{{keycap:W}}`=36 `{{keycap:F}}` | $A = 2 \arctan(W / (2F))$ (Full-Frame $W = 36\text{ mm}$ default) |
| `{{key:DOF}}` | Stack / Solver | Stack: $Z = F, Y = N, X = C$ (or $Y = F, X = N$) • Solver: `{{keycap:H}}` `{{keycap:F}}` `{{keycap:N}}` `{{keycap:C}}` | $H = F^2 / (N \cdot C) / 1000\text{ m}$ on stack ($H = F^2 / (N \cdot C)\text{ mm}$ in solver) |
| `{{key:EV}}` | Stack / Solver | Stack: $Y = N$, $X = T$ • Solver: `{{keycap:N}}` `{{keycap:E}}` `{{keycap:T}}` | $N^2 = 2^E \cdot T \iff E = \log_2(N^2 / T)$ |
| `{{key:SHT}}` | Immediate Stack | Register $Y$: Frame rate $\text{fps}$, Register $X$: Shutter angle $\theta^\circ$ | $X' = (\theta / 360^\circ) / \text{fps}$ ($\text{s}$), $Y' = 1 / X'$ (shutter denominator) |
| `{{key:▸ND}}` / `{{key:▸EV}}` | Immediate Stack | Register $X$: Attenuation in stops (`{{key:▸ND}}`) or lux (`{{key:▸EV}}`) | $X' = 0.3 \times \text{stops}, Y' = 2^{\text{stops}}$ (`{{key:▸ND}}`); $\text{EV}_{100} = \log_2(\text{lx}/2.5)$ (`{{key:▸EV}}`) |
| `{{key:LUX}}` / `{{key:▸lux}}` / `{{key:▸fc}}` | Stack / Solver | Stack: $Y = I, X = D$ (`{{key:LUX}}`) • Solver: `{{keycap:E}}` `{{keycap:I}}` `{{keycap:D}}` | $E = I / D^2$ (`{{key:LUX}}`); unit conversion $1\text{ fc} = 10.7639\text{ lx}$ (`{{key:▸lux}}`, `{{key:▸fc}}`) |
| `{{key:GEL}}` / `{{key:▸MRD}}` | Immediate Stack | Register $Y$: Source $T_{\text{src}}$ ($\text{K}$), Register $X$: Target $T_{\text{dst}}$ ($\text{K}$) | Mired shift $\Delta M = 10^6/X - 10^6/Y$ (`{{key:GEL}}`); $M = 10^6/X$ (`{{key:▸MRD}}`) |

### Immediate Stack Trace: Super 35 Framing, Conjugate Limits, and Dusk Photometry

Before calling camera roll on the $50\text{ mm}$ Steadicam close-up, the 1st AC and gaffer evaluate the Super 35 horizontal field of view ($W = 24.89\text{ mm}$, $F = 50\text{ mm}$), the hyperfocal distance in meters at $f/2.8$ with $C = 0.030\text{ mm}$ (`50` {{key:ENTER}} `2.8` {{key:ENTER}} `0.03` {{key:DOF}} $\to 29.762\text{ m}$), the shutter integration time (`24` {{key:ENTER}} `180` {{key:SHT}} $\to 0.020833\text{ s}$) and native Exposure Value ({{key:EV}}), the $\text{ND } 0.9$ filter density (`3` {{key:▸ND}}), and the $3200\text{ K} \to 5600\text{ K}$ Mired shift ({{key:GEL}}):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `24.89 {{key:ENTER}} 50 {{key:FOV}}` | $0$ | $0$ | $0$ | $27.9542$ | Super 35 horizontal field of view $A = 27.954^\circ$ at $F = 50\text{ mm}$ |
| `50 {{key:ENTER}} 2.8 {{key:ENTER}} 0.03 {{key:DOF}}` | $27.9538$ | $27.9538$ | $27.9542$ | $29.7619$ | Hyperfocal distance $H = 50^2 / (2.8 \times 0.03 \times 1000) = 29.762\text{ m}$ at $f/2.8$ |
| `24 {{key:ENTER}} 180 {{key:SHT}}` | $27.9538$ | $29.7619$ | $48$ | $0.020833$ | $180^\circ$ shutter at $24\text{ fps}$ gives $t = 0.020833\text{ s}$ in $X$ and denominator $48$ in $Y$ |
| `2.8 {{key:x⇄y}} {{key:EV}}` | $29.7619$ | $29.7619$ | $48$ | $8.5558$ | Native Exposure Value $E = \log_2(2.8^2 / 0.020833) = 8.556\text{ EV}$ at $1/48\text{ s}$ |
| `3 {{key:▸ND}}` | $29.7619$ | $48$ | $8$ | $0.9000$ | Convert $3\text{ stops}$ into neutral density $D = 0.9$ in $X$ and filter factor $8\times$ in $Y$ |
| `3200 {{key:ENTER}} 5600 {{key:GEL}}` | $8$ | $8$ | $0.9000$ | **$-133.9286$** | Mired gel shift $\Delta M = -133.93\text{ Mireds}$ (Full CTB) for $3200\text{ K} \to 5600\text{ K}$ |

### Bidirectional Solver Workspaces ({{key:DOF}}, {{key:FOV}}, and {{key:EV}}): Solving Backward for Aperture and Focal Length

Now the Steadicam operator switches to an $F = 35\text{ mm}$ prime for the running cliffside tracking shot on the Super 35 sensor ($C = 0.025\text{ mm}$) and asks for the exact T-stop / f-number $N$ that locks the hyperfocal distance at $H = 4.50\text{ m}$ ($4500\text{ mm}$), followed by the exact focal length $F$ required on Full-Frame ($W = 36.0\text{ mm}$) to match a $27.954^\circ$ horizontal field of view. Opening the {{key:DOF}} and {{key:FOV}} Equation Workspaces solves both inverse optical problems directly without manual algebra:

| Step & Action | Line 1 Workspace Formula | Softkey Legend Bar (`{{keycap:LFU0}}`–`{{keycap:LFU3}}`) | Register X Result & Physical Meaning |
| :--- | :--- | :--- | :--- |
| `{{key:DOF}}` (open workspace) | `DOF: H = F² / (N × C)` | `{{keycap:H}}` `{{keycap:F}}` `{{keycap:N}}` `{{keycap:C}}` | Opens hyperfocal depth-of-field solver workspace |
| `4500` $\to$ `{{keycap:H}}`, `35` $\to$ `{{keycap:F}}` | `DOF: H = F² / (N × C)` | `{{keycap:H}}`=4500 `{{keycap:F}}`=35 `{{keycap:N}}` `{{keycap:C}}` | Stores target $H = 4500\text{ mm}$ ($4.50\text{ m}$) and lens $F = 35\text{ mm}$ |
| `0.025` $\to$ `{{keycap:C}}` | `DOF: H = F² / (N × C)` | `{{keycap:H}}`=4500 `{{keycap:F}}`=35 `{{keycap:N}}` `{{keycap:C}}`=.025 | Stores Super 35 critical Circle of Confusion $C = 0.025\text{ mm}$ |
| `{{key:XEQ}}` $\to$ `{{keycap:N}}` | `N = 10.8889` | `{{keycap:H}}`=4500 `{{keycap:F}}`=35 `{{keycap:N}}`=10.89 `{{keycap:C}}`=.025 | Solves backward for required f-stop $N = 35^2 / (4500 \times 0.025) = \mathbf{10.89}$ ($\approx f/11$) |
| `{{key:FOV}}` (open workspace) | `FOV: A = 2×ATAN(W/(2×F))` | `{{keycap:A}}` `{{keycap:W}}`=36 `{{keycap:F}}` | Opens lens angle workspace with Full-Frame $W = 36.0\text{ mm}$ pre-bound |
| `27.9542` $\to$ `{{keycap:A}}`, `{{key:XEQ}}` $\to$ `{{keycap:F}}` | `F = 72.3182` | `{{keycap:A}}`=27.95 `{{keycap:W}}`=36 `{{keycap:F}}`=72.32 | Solves backward for Full-Frame focal length $F = \mathbf{72.32\text{ mm}}$ matching Super 35 $50\text{ mm}$ |

Similarly, opening the {{key:EV}} workspace (`N² = 2^E × T`) allows the gaffer to store target exposure $E = 11.5558\text{ EV}$ in {{keycap:E}} and shutter time $T = 0.020833\text{ s}$ in {{keycap:T}}, then execute {{key:XEQ}} $\to$ {{keycap:N}} to find the unattenuated iris stop $N = \mathbf{7.924}$ ($f/8$, confirming that $3\text{ stops}$ of $\text{ND } 0.9$ filtration return the lens to $f/2.8$).

### Try It on the Stack

Test your mastery of cinema lens geometry, hyperfocal depth of field, base-two exposure stops, and Mired color balancing with these three on-set problems:

1. **Super 35 Portrait Prime vs. Inverse Circle of Confusion Audit:** On a Super 35 sensor ($W = 24.89\text{ mm}$), compute the horizontal field of view for an $F = 85\text{ mm}$ lens (`24.89` {{key:ENTER}} `85` {{key:FOV}}), and then use the {{key:DOF}} Solver Workspace (`H = F² / (N × C)`) with $F = 85\text{ mm}$ in {{keycap:F}}, $N = 4.0$ in {{keycap:N}}, and $C = 0.025\text{ mm}$ in {{keycap:C}} to solve via {{key:XEQ}} $\to$ {{keycap:H}} in millimeters (and on the stack in meters via `85` {{key:ENTER}} `4` {{key:ENTER}} `0.025` {{key:DOF}}). *(Verified results: $A \approx \mathbf{16.659^\circ}$ and $H = \mathbf{72{,}250\text{ mm}} = \mathbf{72.25\text{ m}}$.)*
2. **European 25 fps Exterior Exposure and 5-Stop ND Filter:** On a $25\text{ fps}$ European shoot with a $180^\circ$ shutter (`25` {{key:ENTER}} `180` {{key:SHT}} $\to T = 1/50\text{ s} = 0.02\text{ s}$) at $f/11$, evaluate the Exposure Value (`11` {{key:ENTER}} `0.02` {{key:EV}}) and find the ND filter rating and filter factor required to open the lens by $5\text{ stops}$ to $f/2.0$ (`5` {{key:▸ND}}). *(Verified Register $X$ and $Y$ results: $E \approx \mathbf{12.563\text{ EV}}$, optical density $D = \mathbf{1.5}$ in $X$, and filter factor $\mathbf{32\times}$ in $Y$ for an $\text{ND } 1.5$ filter.)*
3. **Follow-Spot Illuminance in Lux and Footcandles & Daylight-to-Tungsten Gel:** In the {{key:LUX}} Solver Workspace (`E = I / D²`), store luminous intensity $I = 48{,}000\text{ cd}$ in {{keycap:I}} and throw distance $D = 12\text{ m}$ in {{keycap:D}}, solve for illuminance via {{key:XEQ}} $\to$ {{keycap:E}} in lux, convert to footcandles via {{key:▸fc}}, and compute the Mired shift to warm a $5600\text{ K}$ lamp to $3200\text{ K}$ (`5600` {{key:ENTER}} `3200` {{key:GEL}}). *(Verified results: $E_{\text{lx}} \approx \mathbf{333.333\text{ lx}}$, $E_{\text{fc}} \approx \mathbf{30.968\text{ fc}}$, and $\Delta M \approx \mathbf{+133.929\text{ Mireds}}$ Full CTO.)*

Having locked timecode in the broadcast truck and focused the camera on set, we turn in Chapter 12 to the third physical wave domain of live production: aligning acoustic wavefronts, room-mode wavelengths, and decibel levels across an outdoor stadium and broadcast stage.

---

# Chapter 12: Aligning the Stadium Delay Towers Before Downbeat

Ninety minutes before seventy thousand fans fill an open-air football stadium for a summer concert broadcast, the front-of-house (FOH) systems engineer stands beside the mid-field mixing console with a measurement microphone and weather meter. A warm late-afternoon breeze has pushed the ambient air temperature on the turf to $T_C = 25^\circ\text{C}$ ($77^\circ\text{F}$). Hanging sixty feet above the stage, the main left-and-right line arrays deliver pristine clarity to the front half of the field, but inverse-square spherical spreading attenuates their sound pressure level long before the wave reaches the upper grandstand. To restore vocal intelligibility for the rear audience without blasting the front row at pain-threshold levels, the crew has rigged supplementary delay speaker towers $d = 45.0\text{ m}$ downfield from the main stage array.

Those downfield towers introduce a classic wave-propagation race condition. Electrical audio signals leave the mixing console over fiber-optic and copper trunks at roughly two hundred thousand kilometers per second, reaching the delay tower amplifiers in less than a microsecond. Meanwhile, the acoustic pressure wave from the main stage array crawls through the $25^\circ\text{C}$ stadium air at roughly $346\text{ meters per second}$. If the delay tower fires uncompensated, listeners in the back half of the stadium hear the delay tower more than a tenth of a second *before* the main stage wave arrives—shattering the rhythmic pocket into a cavernous slap-back echo and pulling perceived vocal localization away from the performers on stage toward the rigging scaffold overhead.

Before the headliner's downbeat, the systems engineer and broadcast sound mixer must solve three acoustic problems:
1. Compute the thermal speed of sound at $25^\circ\text{C}$, the acoustic wavelength of low-frequency subwoofer and room modes, and the digital signal processor (DSP) delay time for the $45.0\text{ m}$ tower including a psychoacoustic Haas precedence offset.
2. Trace the inverse-square Sound Pressure Level decay of a stage source both forward to the mix position and **backward** to find the maximum boom-mic reach $D_2$ before dialogue drops below the broadcast noise floor.
3. Sum the incoherent acoustic power of dual PA arrays in decibels, convert console line levels between decibels and volts, and verify reverberation decay ($RT_{60}$).

---

## Acoustic Wave Propagation, Precedence, and Room Decay

Unlike electromagnetic light and radio waves, which travel through vacuum at $c \approx 3 \times 10^8\text{ m/s}$, sound is a longitudinal mechanical compression wave whose propagation velocity depends directly on the kinetic translational energy—and therefore the absolute temperature—of air molecules.

### Thermal Speed of Sound, Delay Tower Transit Time, and the Haas Window

In dry air treated as an ideal diatomic gas ($\gamma = 1.40$, molar mass $M \approx 0.02897\text{ kg/mol}$), Laplace's adiabatic wave law sets the speed of sound $v_s$ proportional to the square root of absolute Kelvin temperature: $v_s = 331.3\sqrt{1 + T_C / 273.15}\text{ m/s}$. Linearizing that square root across ambient outdoor and indoor temperatures ($-20^\circ\text{C}$ to $+40^\circ\text{C}$) yields the standard acoustic velocity law ({{key:vₛ}}), the propagation transit time $\Delta t_{\text{ms}}$ ({{key:DLY}}) across a downfield throw distance $d$ (in meters), and the acoustic wavelength $\lambda$ ({{key:λ}}) at frequency $f$ (in hertz):

$$v_s(T_C) = 331.3 + 0.606 \cdot T_C \quad \left[\frac{\text{m}}{\text{s}}\right], \qquad \Delta t_{\text{ms}} = \frac{d}{v_s} \times 1000, \qquad \lambda = \frac{v_s}{f}$$

In these expressions, $T_C$ is the ambient air temperature in degrees Celsius ($^\circ\text{C}$), $v_s$ is the acoustic phase velocity in $\text{m/s}$ (evaluating to $343.42\text{ m/s} \approx 343\text{ m/s}$ at the standard $20^\circ\text{C}$ room reference recalled by {{key:vₛ}}), $d$ is the physical distance from the main stage array to the delay tower in meters, $\Delta t_{\text{ms}}$ is the acoustic transit delay in milliseconds ($\text{ms}$), and $\lambda$ is the physical wavelength in meters.

![Time-aligned festival sound reinforcement coordinating acoustic air travel from the main stage array with DSP delay towers.](../assets/diagrams/domains/diagram_ch04_acoustic_delay.png)

At our stadium's turf temperature of $T_C = 25^\circ\text{C}$, the speed of sound rises to $v_s(25^\circ\text{C}) = 331.3 + 0.606(25) = 331.3 + 15.15 = \mathbf{346.45\text{ m/s}}$. Over the $d = 45.0\text{ m}$ air path to the delay tower (`45` {{key:ENTER}} `25` {{key:DLY}}), the main stage wavefront requires a transit time of:

$$\Delta t_{\text{25}^\circ\text{C}} = \frac{45.0}{346.45} \times 1000 \approx \mathbf{129.889\text{ ms}}$$

Compare that thermal result with the standard $20^\circ\text{C}$ reference velocity ($v_s = 343.0\text{ m/s}$ via `45` {{key:DLY}}), where the geometric delay is $\Delta t_{\text{20}^\circ\text{C}} = (45.0 / 343.0) \times 1000 \approx \mathbf{131.195\text{ ms}}$. That $1.31\text{ ms}$ thermal shortening across a $5^\circ\text{C}$ afternoon warming corresponds to $0.45\text{ m}$ of acoustic path length—a full $180^\circ$ phase cancellation ($\lambda / 2 = 0.45\text{ m} \implies \lambda = 0.90\text{ m}$) at $f = 346.45 / 0.90 \approx \mathbf{385\text{ Hz}}$ right in the vocal fundamental region. Furthermore, by **Helmut Haas's 1949 precedence effect**, if the delay tower fires at the exact geometric arrival time ($129.89\text{ ms}$), fans standing near the louder delay tower localize the singer's voice up in the delay rigging rather than on stage. Adding a $+12.0\text{ ms}$ **Haas precedence offset** (setting the DSP to $129.89 + 12.0 = \mathbf{141.89\text{ ms}}$) ensures the main stage wavefront reaches the listener's ears $12\text{ ms}$ before the louder delay wave. The auditory cortex fuses both arrivals inside the $30\text{ ms}$ Haas integration window and locks spatial localization onto the stage.

### Sabine Reverberation Decay and Room Standing-Wave Modes

Inside the enclosed concrete-and-glass VIP broadcast studio beneath the stadium bowl, sound waves reflect repeatedly off parallel walls of spacing $L_{\text{room}}$, exciting axial standing-wave room modes whenever $L_{\text{room}}$ equals an integer multiple of half a wavelength ($f_n = n \cdot v_s / (2 L_{\text{room}})$, or $\lambda_1 = 2 L_{\text{room}}$). Simultaneously, Wallace Clement Sabine's 1898 architectural law sets the **Reverberation Time** $RT_{60}$ (in seconds)—the time required for reverberant sound energy in a room of volume $V$ ($\text{m}^3$) and total absorption area $A = \sum S_i \alpha_i$ (metric sabins, $\text{m}^2$) to decay by $60\text{ dB}$:

$$RT_{60} = \frac{0.161 \cdot V}{A} = \frac{0.161 \cdot V}{\sum_{i} S_i \alpha_i}, \qquad \lambda = \frac{v_s}{f}$$

For a broadcast studio of volume $V = 2400\text{ m}^3$ treated with acoustic baffles providing $A = 480\text{ metric sabins}$ of absorption, Sabine's formula predicts a tight decay time of $RT_{60} = (0.161 \times 2400) / 480 = \mathbf{0.805\text{ s}}$, while an $f = 68.6\text{ Hz}$ bass note at $v_s = 343\text{ m/s}$ has an acoustic wavelength of $\lambda = 343 / 68.6 = \mathbf{5.00\text{ m}}$ (`68.6` {{key:λ}}).

---

## Spherical Spreading Attenuation and Incoherent Decibel Summation

To size the power amplifiers for the stadium arrays and position shotgun boom microphones on the broadcast stage, the engineer must calculate how acoustic pressure decays with distance across open air and how multiple speaker arrays combine in decibels.

### Inverse-Square Pressure Falloff and Maximum Boom-Mic Distance

Because human hearing responds logarithmically to acoustic pressure across six orders of magnitude—from the quietest audible threshold at reference pressure $P_0 = 20\,\mu\text{Pa}$ ($0\text{ dBSPL}$) to $20\text{ Pa}$ ($120\text{ dBSPL}$)—acoustics defines **Sound Pressure Level** ($L$, in $\text{dBSPL}$) as $20\log_{10}(P_{\text{rms}} / P_0)$. As an acoustic wave expands spherically into free space from a compact source, its acoustic intensity ($I \propto P_{\text{rms}}^2$) falls off inversely with the sphere's surface area ($1 / (4\pi D^2)$), so root-mean-square sound pressure falls inversely with distance ($P_{\text{rms}} \propto 1/D$). Expressing that inverse-distance pressure ratio in decibels yields the **Spherical Spreading Attenuation Law** ({{key:SPL}}) in both its 3-operand level form ($L_1$ in $Z$, $D_1$ in $Y$, $D_2$ in $X$) and its inverse target-distance form:

$$L_2 = L_1 - 20 \log_{10}\left(\frac{D_2}{D_1}\right) \iff D_2 = D_1 \cdot 10^{\left(L_1 - L_2\right) / 20}$$

Here $L_1$ is the known Sound Pressure Level in $\text{dBSPL}$ at reference distance $D_1$, and $L_2$ is the Sound Pressure Level at distance $D_2$ (when called with two arguments $D_1$ in $Y$ and $D_2$ in $X$, {{key:SPL}} returns the relative decibel attenuation $\Delta L = -20\log_{10}(D_2 / D_1)$). Notice the exact mathematical bridge to radio-frequency engineering in Unit V (`SC-50`): the distance term $-20\log_{10}(D_2/D_1)$ in acoustic {{key:SPL}} is identical to the $-20\log_{10}(D)$ inverse-square spreading term in the Friis Free-Space Path Loss equation ({{key:sc50:FSL}}). Every doubling of distance ($D_2 / D_1 = 2$) reduces sound pressure level by $20\log_{10}(2) \approx \mathbf{6.0206\text{ dB}}$.

In our stadium check, a reference cabinet produces $L_1 = 104.0\text{ dBSPL}$ at $D_1 = 1.0\text{ m}$. Projecting that wavefront out to $D_2 = 32.0\text{ m}$ ($2^5$, five doublings of distance via `104` {{key:ENTER}} `1` {{key:ENTER}} `32` {{key:SPL}}) attenuates the level by $20\log_{10}(32) \approx 30.103\text{ dB}$ to $L_2 = 104.0 - 30.103 = \mathbf{73.897\text{ dBSPL}}$. Conversely, on the interview stage, if an actor speaks at $L_1 = 74.0\text{ dBSPL}$ measured at $D_1 = 0.50\text{ m}$ and the broadcast sound mixer requires at least $L_2 = 63.5\text{ dBSPL}$ at the hypercardioid boom capsule to maintain a $45\text{ dB}$ signal-to-noise margin above the stadium crowd rumble, solving backward for the maximum boom-mic distance $D_2$ yields $D_2 = 0.50 \times 10^{(74.0 - 63.5)/20} = 0.50 \times 10^{0.525} = 0.50 \times 3.3497 = \mathbf{1.675\text{ m}}$.

### Combining Uncorrelated Acoustic Power and Analog Line Levels

When multiple loudspeakers or stage sources radiate into the same listening zone, the combined decibel level depends on whether the waves are **incoherent** (uncorrelated random phases across broadband frequencies) or **coherent** (phase-locked low-frequency waves). Because acoustic power is proportional to pressure squared ($W \propto P_{\text{rms}}^2 \propto 10^{L_i / 10}$), summing independent acoustic sources of decibel levels $L_1$ and $L_2$ requires adding their linear power ratios and taking $10\log_{10}$ of the sum via the decibel prefix key {{key:dB}} followed by {{key:+}} (e.g., `94` {{key:ENTER}} `94` {{key:dB}} {{key:+}} $\to \mathbf{97.0103\text{ dB}}$), while analog broadcast consoles reference signal voltage $V_{\text{rms}}$ to $V_0 = \sqrt{0.600\,\Omega \times 1\text{ mW}} \approx 0.774597\text{ V}_{\text{rms}}$ in **dBu** ({{key:▸dBu}}, {{key:▸V}}):

$$L_{\Sigma,\text{incoherent}} = 10 \log_{10}\left(10^{L_1 / 10} + 10^{L_2 / 10}\right), \qquad L_{\text{dBu}} = 20 \log_{10}\left(\frac{V_{\text{rms}}}{0.774597}\right), \qquad V_{\text{rms}} = 0.774597 \times 10^{L_{\text{dBu}} / 20}$$

When two uncorrelated broadband PA hangs each deliver $73.897\text{ dBSPL}$ at the $32.0\text{ m}$ mix position (`73.897` {{key:ENTER}} `73.897` {{key:dB}} {{key:+}}), their acoustic powers add ($W_{\text{total}} = 2 W_1$), increasing the level by $10\log_{10}(2) \approx \mathbf{+3.0103\text{ dB}}$ to $L_{\Sigma} = \mathbf{76.9073\text{ dBSPL}}$ (just as two $94.0\text{ dBSPL}$ stage monitors sum via `94` {{key:ENTER}} `94` {{key:dB}} {{key:+}} to $\mathbf{97.0103\text{ dBSPL}}$). Meanwhile, a professional broadcast console outputting $+4.0\text{ dBu}$ drives the fiber-optic stage-box input with $V_{\text{rms}} = 0.774597 \times 10^{4/20} = \mathbf{1.2276\text{ V}_{\text{rms}}}$ (`4` {{key:▸V}}).

---

## Time-Aligning Arrays and Evaluating Sound Levels on the Stack and in the Solver Workspace

On the **SC-24**, acoustic delay alignment ({{key:DLY}}), reference sound velocity ({{key:vₛ}}), acoustic wavelength ({{key:λ}}), spherical spreading attenuation ({{key:SPL}}), incoherent decibel summation ({{key:dB}} {{key:+}}), analog studio voltage conversions ({{key:▸dBu}}, {{key:▸V}}), and uncompressed broadcast stream data rates ({{key:BIT}}) execute directly on the RPN stack and in the bidirectional Solver Workspace.

| Key / Solver | Mode | Inputs / Softkeys (`{{keycap:LFU0}}`–`{{keycap:LFU3}}`) | Governing Expression |
| :--- | :--- | :--- | :--- |
| `{{key:DLY}}` | Immediate Stack | Stack: $X = d$ ($\text{m}$) or $Y = d, X = T_C$ ($^\circ\text{C}$) | $\Delta t = d / 343 \times 1000\text{ ms}$ (or $d / (331.3 + 0.606 T_C) \times 1000\text{ ms}$) |
| `{{key:vₛ}}` | Constant / Stack | Pushes reference acoustic speed $v_s$ | $v_s = 343.0\text{ m/s}$ ($20^\circ\text{C}$ dry air reference) |
| `{{key:λ}}` | Immediate Stack | Stack: $X = f$ ($\text{Hz}$) or $Y = v_s, X = f$ ($\text{Hz}$) | Acoustic wavelength $\lambda = v_s / f$ ($\text{m}$, $v_s = 343\text{ m/s}$ default) |
| `{{key:SPL}}` | Immediate Stack | Stack: $Z = L_1, Y = D_1, X = D_2$ (or $Y = D_1, X = D_2$) | $L_2 = L_1 - 20 \log_{10}(D_2 / D_1)$ (or $\Delta L = -20\log_{10}(D_2/D_1)$) |
| `{{key:dB}}` `{{key:+}}` | Prefix + Stack | Register $Y$: Level $L_1$ ($\text{dB}$), Register $X$: Level $L_2$ ($\text{dB}$) | Incoherent power sum $L_{\Sigma} = 10 \log_{10}(10^{Y/10} + 10^{X/10})$ |
| `{{key:▸dBu}}` / `{{key:▸V}}` | Immediate Stack | Register $X$: Voltage $V_{\text{rms}}$ (`{{key:▸dBu}}`) or level $L_{\text{dBu}}$ (`{{key:▸V}}`) | $L_{\text{dBu}} = 20 \log_{10}(V / 0.7746)$ and $V = 0.7746 \times 10^{L/20}$ |
| `{{key:BIT}}` | Stack / Solver | Stack: $Y = B, X = F$ • Solver: `{{keycap:R}}` `{{keycap:B}}` `{{keycap:F}}` | Uncompressed stream rate $R = B \times F / 8\text{ MB/s}$ |

### Immediate Stack Trace: Thermal Delay Alignment, SPL Falloff, and Dual-Array Summation

Standing at the front-of-house console, the systems engineer evaluates the transit delay across $d = 45.0\text{ m}$ at turf temperature $T_C = 25^\circ\text{C}$ (`45` {{key:ENTER}} `25` {{key:DLY}}), adds the $+12.0\text{ ms}$ Haas precedence offset, projects the $104.0\text{ dBSPL}$ cabinet from $D_1 = 1.0\text{ m}$ out to $D_2 = 32.0\text{ m}$ (`104` {{key:ENTER}} `1` {{key:ENTER}} `32` {{key:SPL}}), sums two uncorrelated hangs via {{key:dB}} {{key:+}} (just like `94` {{key:ENTER}} `94` {{key:dB}} {{key:+}} $\to 97.0103\text{ dB}$), and checks the $68.6\text{ Hz}$ bass wavelength ({{key:λ}}):

| Keystroke | Register T | Register Z | Register Y | Register X | What Happens on the Stack |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `45 {{key:ENTER}} 25 {{key:DLY}}` | $0$ | $0$ | $0$ | $129.8889$ | Transit delay across $45\text{ m}$ at $25^\circ\text{C}$ ($v_s = 346.45\text{ m/s}$) $= 129.889\text{ ms}$ |
| `12 {{key:+}}` | $0$ | $0$ | $0$ | $141.8889$ | Add $+12.0\text{ ms}$ Haas precedence offset $= 141.889\text{ ms}$ DSP delay |
| `104 {{key:ENTER}} 1 {{key:ENTER}} 32 {{key:SPL}}` | $141.89$ | $141.89$ | $141.8889$ | $73.8970$ | Project $104\text{ dBSPL}$ at $1\text{ m}$ out to $32\text{ m}$: $L_2 = 73.897\text{ dBSPL}$ |
| `{{key:ENTER}} {{key:dB}} {{key:+}}` | $141.89$ | $141.89$ | $141.8889$ | $76.9073$ | Incoherent power sum of two $73.897\text{ dBSPL}$ hangs $= 76.9073\text{ dBSPL}$ |
| `68.6 {{key:λ}}` | $141.89$ | $141.8889$ | $76.9073$ | **$5.0000$** | Compute acoustic wavelength $\lambda = 343 / 68.6 = 5.00\text{ m}$ at $20^\circ\text{C}$ reference |

### Bidirectional Solver Workspaces ({{key:EQN}} and {{key:BIT}}): Boom-Mic Reach and Broadcast Trunk Bandwidth

When the broadcast audio supervisor asks how far back the boom operator can hold the hypercardioid shotgun microphone ($D$) before an actor speaking at $S = 74.0\text{ dBSPL}$ at reference distance $R = 0.50\text{ m}$ drops below the minimum acceptable dialogue threshold of $L = 63.5\text{ dBSPL}$ (stored in {{key:EQN}} as `L = S - 20×LOG(D/R)` with single-letter softkeys {{keycap:L}}, {{keycap:S}}, {{keycap:D}}, {{keycap:R}}), and what uncompressed data rate {{keycap:R}} ({{key:BIT}}) is required to record the concert film's $16\text{ Mb/frame}$ RAW stream at $24\text{ fps}$, the engineer solves both directly in the Equation Workspace:

| Step & Action | Line 1 Workspace Formula | Softkey Legend Bar (`{{keycap:LFU0}}`–`{{keycap:LFU3}}`) | Register X Result & Physical Meaning |
| :--- | :--- | :--- | :--- |
| `{{key:EQN}}` (`L = S - 20×LOG(D/R)`) | `L = S - 20×LOG(D/R)` | `{{keycap:L}}` `{{keycap:S}}` `{{keycap:D}}` `{{keycap:R}}` | Selects spherical spreading equation in `{{key:EQN}}` |
| `63.5` $\to$ `{{keycap:L}}`, `74` $\to$ `{{keycap:S}}` | `L = S - 20×LOG(D/R)` | `{{keycap:L}}`=63.5 `{{keycap:S}}`=74 `{{keycap:D}}` `{{keycap:R}}` | Stores target threshold $L = 63.5\text{ dBSPL}$ and source $S = 74.0\text{ dBSPL}$ |
| `0.5` $\to$ `{{keycap:R}}`, `{{key:XEQ}}` $\to$ `{{keycap:D}}` | `D = 1.6748` | `{{keycap:L}}`=63.5 `{{keycap:S}}`=74 `{{keycap:D}}`=1.67 `{{keycap:R}}`=0.5 | Solves backward for maximum boom-mic reach $D = \mathbf{1.675\text{ m}}$ |
| `{{key:BIT}}` (open workspace) | `BIT: R = B × F / 8` | `{{keycap:R}}` `{{keycap:B}}` `{{keycap:F}}` | Opens cinema/broadcast stream data-rate workspace |
| `16` $\to$ `{{keycap:B}}`, `24` $\to$ `{{keycap:F}}`, `{{key:XEQ}}` $\to$ `{{keycap:R}}` | `R = 48.0000` | `{{keycap:R}}`=48 `{{keycap:B}}`=16 `{{keycap:F}}`=24 | Solves for uncompressed capture rate $R = 16 \times 24 / 8 = \mathbf{48.00\text{ MB/s}}$ |

### Try It on the Stack

Apply thermal acoustic delay, incoherent decibel summation, inverse spherical spreading, and studio line-level conversions with these three live-sound exercises:

1. **Second-Ring Festival Delay Tower at 30°C:** A rear festival delay tower stands $d = 80.0\text{ m}$ from the main stage on a hot afternoon ($T_C = 30^\circ\text{C}$). Find the $30^\circ\text{C}$ transit delay (`80` {{key:ENTER}} `30` {{key:DLY}}), and add a $+15\text{ ms}$ Haas offset (`15` {{key:+}}). *(Verified Register $X$ results: $v_s = \mathbf{349.48\text{ m/s}}$, $\Delta t_{30} \approx \mathbf{228.912\text{ ms}}$, and $\text{DSP} \approx \mathbf{243.912\text{ ms}}$.)*
2. **Three-Source Stage Noise Sum and Front-of-House Attenuation:** Combine three uncorrelated stage sources measuring $95\text{ dBSPL}$, $91\text{ dBSPL}$, and $86\text{ dBSPL}$ at $D_1 = 2.0\text{ m}$ (`95` {{key:ENTER}} `91` {{key:dB}} {{key:+}} `86` {{key:dB}} {{key:+}}), and project the combined level to the console at $D_2 = 24.0\text{ m}$ (`2` {{key:ENTER}} `24` {{key:SPL}}). *(Verified Register $X$ results: $L_{\Sigma,2\text{m}} \approx \mathbf{96.830\text{ dBSPL}}$ and $L_{\text{FOH}} \approx \mathbf{75.246\text{ dBSPL}}$.)*
3. **Broadcast Line-Level Voltage and Maximum PA Throw Distance:** Convert a $+18.0\text{ dBu}$ digital console clipping level into RMS volts (`18` {{key:▸V}}), and compute the maximum throw distance $D_2$ at which an array producing $L_1 = 132.0\text{ dBSPL}$ at $D_1 = 1.0\text{ m}$ still delivers $L_2 = 96.0\text{ dBSPL}$ (`132` {{key:ENTER}} `96` {{key:-}} `20` {{key:÷}} `10` {{key:x⇄y}} {{key:yˣ}}). *(Verified results: $V_{\text{rms}} \approx \mathbf{6.153\text{ V}_{\text{rms}}}$ and $D_2 = 10^{36/20} \approx \mathbf{63.096\text{ m}}$.)*

Having mastered frame-accurate broadcast clocks, rectilinear cinema optics, and acoustic wave alignment in Unit IV, we ascend in [Unit V: Radio-Frequency Engineering, Transmission Lines & Link Budgets](05-sc50-rf-spectrum.md) from mechanical sound waves to high-frequency electromagnetic waves, complex impedance matching, and microwave link budgets.
