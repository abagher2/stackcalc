# Appendix C: Solutions to Chapter Practice Problems

This compendium provides complete step-by-step keystroke solutions, stack register traces, and intermediate mathematical verifications for all 135 practice problems across the 27 chapters of *The Stack in the Field*.

---

## Unit I (SC-35): Geomatics, Land Surveying & Flight Navigation

### Chapter 1: The Lost Cornerstone in the Pine Barrens

1. **Slope Reduction and Forward Coordinate Projection**
   - **Keystrokes**: `412.68` {{key:sc35:ENTER}} `6.15` {{key:sc35:▸HR}} {{key:sc35:SLP}} `47.2230` {{key:sc35:▸HR}} `410.10` {{key:sc35:TRV}} {{key:sc35:N⇄E}}
   - **Solution**: Reduces slope distance $S = 412.68\text{ ft}$ at $\nu = 6.25^\circ$ to horizontal distance $D_H = \mathbf{410.10\text{ ft}}$ in $X$ and vertical rise $\Delta V = \mathbf{44.92\text{ ft}}$ in $Y$. Staging azimuth $47.375^\circ$ and $D_H = 410.10\text{ ft}$ evaluates coordinate displacements $\Delta N = \mathbf{277.75\text{ ft}}$ in $Y$ and $\Delta E = \mathbf{301.76\text{ ft}}$ in $X$.
2. **Inverse Bearing Between Witness Monuments**
   - **Keystrokes**: `1585.20` {{key:sc35:ENTER}} `1200` {{key:sc35:-}} `1912.60` {{key:sc35:ENTER}} `1500` {{key:sc35:-}} {{key:sc35:INV}} {{key:sc35:x⇄y}} {{key:sc35:BRG}} {{key:sc35:▸HMS}}
   - **Solution**: Calculates coordinate differences $\Delta N = 385.20\text{ ft}$ and $\Delta E = 412.60\text{ ft}$ to yield boundary distance $D = \mathbf{564.4624\text{ ft}}$, azimuth $\alpha = \mathbf{46.9669^\circ}$, and legal quadrant bearing $\mathbf{\text{N } 46^\circ 58' 01'' \text{ E}}$ (`46.5801`).
3. **Traverse Closure Precision and Acreage Conversion**
   - **Keystrokes**: `0.15` {{key:sc35:ENTER}} `0.20` {{key:sc35:+/-}} {{key:sc35:CLS}} `2500` {{key:sc35:x⇄y}} {{key:sc35:÷}} `326700` {{key:sc35:ENTER}} `43560` {{key:sc35:÷}}
   - **Solution**: Resolves linear error of closure $E_c = \sqrt{0.15^2 + (-0.20)^2} = \mathbf{0.25\text{ ft}}$, computes relative precision ratio $2500 / 0.25 = \mathbf{1 : 10{,}000}$, and converts $326{,}700\text{ ft}^2$ to $\mathbf{7.5000\text{ acres}}$.
4. **Architectural Foot-Inch Reduction and Colonial Chain Conversions**
   - **Keystrokes**: `38` {{key:sc35:ENTER}} `7` {{key:sc35:ENTER}} `5` {{key:sc35:ENTER}} `8` {{key:sc35:÷}} {{key:sc35:+}} `12` {{key:sc35:÷}} {{key:sc35:+}} `14.75` {{key:sc35:ENTER}} `66` {{key:sc35:×}}
   - **Solution**: Evaluates fractional inches and feet to yield architectural offset $L_{\text{ft}} = \mathbf{38.6354\text{ ft}}$, and multiplies $14.75\text{ chains} \times 66\text{ ft/chain}$ to yield $D = \mathbf{973.50\text{ ft}}$.
5. **State Plane Combined Grid-to-Ground Scale Reduction**
   - **Keystrokes**: `20906000` {{key:sc35:ENTER}} `20906000` {{key:sc35:ENTER}} `5280` {{key:sc35:+}} `30` {{key:sc35:-}} {{key:sc35:÷}} `0.9999450` {{key:sc35:×}} `3450` {{key:sc35:×}}
   - **Solution**: Computes elevation factor $k_{\text{elev}} = \mathbf{0.9997489}$, combined factor $k_{\text{comb}} = \mathbf{0.9996940}$, and reduced State Plane grid distance $D_{\text{grid}} = \mathbf{3{,}448.94\text{ ft}}$.

### Chapter 2: Threading the Switchback Grade Through Granite Gorge

1. **Highway Curve Layout from Radius and Deflection Angle**
   - **Keystrokes**: `1200` {{key:sc35:ENTER}} `28.5` {{key:sc35:CRV}} `1200` {{key:sc35:ENTER}} `14.25` {{key:sc35:SIN}} {{key:sc35:×}} `2` {{key:sc35:×}}
   - **Solution**: Evaluates curve parameters to place tangent distance $T = \mathbf{304.77\text{ ft}}$ in $Y$ and arc length $L = \mathbf{596.90\text{ ft}}$ in $X$, with long chord $LC = 2R\sin(14.25^\circ) = \mathbf{590.80\text{ ft}}$.
2. **Parabolic Vertical Curve and Earthwork Cut Volume**
   - **Keystrokes**: `425.00` {{key:sc35:ENTER}} `2.5` {{key:sc35:ENTER}} `1.75` {{key:sc35:+/-}} {{key:sc35:ENTER}} `8` {{key:sc35:VCV}} `250` {{key:sc35:ENTER}} `380` {{key:sc35:ENTER}} `180` {{key:sc35:CUT}}
   - **Solution**: Evaluates vertical curve equation to find midpoint elevation $\text{Elev}(4) = \mathbf{430.75\text{ ft}}$, and computes average end-area cut volume $V = \frac{250 + 380}{2} \times \frac{180}{27} = \mathbf{2{,}100.00\text{ yd}^3}$.
3. **Three-Wire Benchmark Transfer and Grade Check**
   - **Keystrokes**: `7.82` {{key:sc35:ENTER}} `5.42` {{key:sc35:ENTER}} `3.02` {{key:sc35:LVL}} `842.15` {{keycap:H}} `5.32` {{keycap:B}} `5.42` {{keycap:F}} {{key:sc35:SOLVE}} {{keycap:E}} `6` {{key:sc35:+/-}} {{key:sc35:ENTER}} `480` {{key:sc35:GR%}}
   - **Solution**: Confirms mid-wire $(7.82 + 3.02)/2 = \mathbf{5.42\text{ ft}}$ in $Y$ and stadia distance $D = 100 \times (7.82 - 3.02) = \mathbf{480.00\text{ ft}}$ in $X$. Transferred elevation is $E = \mathbf{842.05\text{ ft}}$ with grade $\text{GR\%} = \mathbf{-1.2500\%}$.
4. **Highway Superelevation Rate and Side Friction Balance**
   - **Keystrokes**: `65` {{key:sc35:x²}} `15` {{key:sc35:ENTER}} `1500` {{key:sc35:×}} {{key:sc35:÷}} `0.11` {{key:sc35:-}}
   - **Solution**: Calculates total centrifugal demand $e + f = 65^2 / (15 \times 1500) = \mathbf{0.1878\text{ ft/ft}}$, yielding required pavement superelevation $e = 0.1878 - 0.110 = \mathbf{0.0778\text{ ft/ft}}$ ($7.78\%$).
5. **Prismoidal Earthwork Correction on Tapering Rock Cut**
   - **Keystrokes**: `820` {{key:sc35:ENTER}} `240` {{key:sc35:ENTER}} `200` {{key:sc35:CUT}} `18` {{key:sc35:ENTER}} `8` {{key:sc35:-}} `64` {{key:sc35:ENTER}} `34` {{key:sc35:-}} {{key:sc35:×}} `200` {{key:sc35:×}} `324` {{key:sc35:÷}} {{key:sc35:-}}
   - **Solution**: Evaluates Average End-Area volume $V_{\text{ea}} = \mathbf{3{,}925.93\text{ yd}^3}$, prismoidal correction $C_p = \frac{200}{324}(10)(30) = \mathbf{185.19\text{ yd}^3}$, and certified volume $V_{\text{prism}} = 3925.93 - 185.19 = \mathbf{3{,}740.74\text{ yd}^3}$.

### Chapter 3: Night Approach Under a Mountain Crosswind

1. **Wind Vector Decomposition and Crab Angle**
   - **Keystrokes**: `28` {{key:sc35:ENTER}} `40` {{key:sc35:WND}} `145` {{key:sc35:÷}} {{key:sc35:ASIN}}
   - **Solution**: Resolves wind vector into headwind $V_{\text{hw}} = \mathbf{21.45\text{ kt}}$ in $Y$ and crosswind $V_{\text{xw}} = \mathbf{18.00\text{ kt}}$ in $X$. Dividing crosswind by airspeed yields crab angle $\text{WCA} = \arcsin(18/145) = \mathbf{7.13^\circ}$.
2. **Inverse Wind Angle Limit and Density Altitude**
   - **Keystrokes**: `15` {{keycap:X}} `30` {{keycap:V}} {{key:sc35:SOLVE}} {{keycap:A}} `6200` {{key:sc35:ENTER}} `28` {{key:sc35:ALT}}
   - **Solution**: Solves crosswind limit backward to find $\theta_{\max} = \arcsin(15/30) = \mathbf{30.00^\circ}$. Evaluates atmospheric expansion to find Density Altitude $\text{DA} = \mathbf{9{,}248\text{ ft}}$.
3. **Endurance Leg Check and Center of Gravity Moment**
   - **Keystrokes**: `165` {{keycap:D}} `1.25` {{keycap:T}} {{key:sc35:SOLVE}} {{keycap:S}} `350` {{key:sc35:ENTER}} `120` {{key:sc35:×}}
   - **Solution**: Solves time-speed-distance equation to yield required groundspeed $S = 165 / 1.25 = \mathbf{132.00\text{ kt}}$, and computes fuel moment $M = 350 \times 120 = \mathbf{42{,}000\text{ lb}\cdot\text{in}}$.
4. **Point of Equal Time on Headwind Route**
   - **Keystrokes**: `360` {{key:sc35:ENTER}} `170` {{key:sc35:×}} `130` {{key:sc35:ENTER}} `170` {{key:sc35:+}} {{key:sc35:÷}} `130` {{key:sc35:÷}}
   - **Solution**: Evaluates Critical Point formula $d_{\text{PET}} = \frac{D \times GS_{\text{ret}}}{GS_{\text{out}} + GS_{\text{ret}}} = \frac{360 \times 170}{300} = \mathbf{204.00\text{ NM}}$, requiring flight time $t_{\text{PET}} = 204 / 130 = \mathbf{1.5692\text{ hr}}$ ($94.15\text{ min}$).
5. **High-Altitude Summer Takeoff Roll Expansion**
   - **Keystrokes**: `7000` {{key:sc35:ENTER}} `32` {{key:sc35:ALT}} `1250` {{key:sc35:ENTER}} `10.720` {{key:sc35:ENTER}} `0.12` {{key:sc35:×}} `1` {{key:sc35:+}} {{key:sc35:×}}
   - **Solution**: Calculates Density Altitude $\text{DA} = \mathbf{10{,}720\text{ ft}}$. Evaluates takeoff expansion factor $1 + (10.720 \times 0.12) = 2.2864$, yielding expanded ground roll $S_{\text{ground}} = 1250 \times 2.2864 = \mathbf{2{,}858.00\text{ ft}}$.

## Unit II (SC-14): Electrical Power, Conduit Geometry & Industrial Trades

### Chapter 4: The Voltage Drop on Pier 14's Crane Feeder

1. **Three-Phase Line Current and Continuous Feeder Sizing**
   - **Keystrokes**: `480` {{key:sc14:ENTER}} `125` {{key:sc14:kVA}} `1.25` {{key:sc14:×}}
   - **Solution**: Calculates operating load current $I = 125{,}000 / (\sqrt{3} \times 480) = \mathbf{150.3533\text{ A}}$, requiring minimum continuous feeder rating $I_{\text{feeder}} = 1.25 \times 150.3533 = \mathbf{187.9416\text{ A}}$ (#3/0 AWG copper rated at $200\text{ A}$).
2. **Conductor Resistance and Three-Phase Voltage Drop**
   - **Keystrokes**: `480` {{key:sc14:ENTER}} `400` {{key:sc14:ENTER}} `160` {{key:sc14:ENTER}} `0.0766` {{key:sc14:AWG}}
   - **Solution**: Evaluates three-phase voltage drop $V_{\text{drop}} = \sqrt{3} \times 0.0766 \times 0.400 \times 160 = \mathbf{8.51\text{ V}}$ in $Y$, percentage drop $\mathbf{1.77\%}$ in $X$, and delivered terminal voltage $V_{\text{load}} = \mathbf{471.49\text{ V}}$ in $Z$.
3. **Power Factor Correction Capacitor Sizing**
   - **Keystrokes**: `120` {{key:sc14:ENTER}} `0.75` {{key:sc14:PF}} `0.75` {{key:sc14:ACOS}} {{key:sc14:TAN}} `0.95` {{key:sc14:ACOS}} {{key:sc14:TAN}} {{key:sc14:-}} `120` {{key:sc14:×}}
   - **Solution**: Evaluates uncorrected reactive load $Q_1 = 120 \times \tan(41.41^\circ) = \mathbf{105.8301\text{ kVAR}}$. Computes required capacitance $Q_C = 120(\tan 41.41^\circ - \tan 18.19^\circ) = \mathbf{66.4027\text{ kVAR}}$.
4. **Three-Phase Motor Inrush and Branch Fuse Sizing**
   - **Keystrokes**: `124` {{key:sc14:ENTER}} `1.25` {{key:sc14:×}} `124` {{key:sc14:ENTER}} `1.75` {{key:sc14:×}}
   - **Solution**: Computes minimum conductor ampacity $1.25 \times 124 = \mathbf{155.00\text{ A}}$, and evaluates maximum fuse threshold $1.75 \times 124 = \mathbf{217.00\text{ A}}$ (selecting standard $225\text{ A}$ time-delay fuses).
5. **Substation Available Short-Circuit Fault Current**
   - **Keystrokes**: `1500000` {{key:sc14:ENTER}} `480` {{key:sc14:÷}} `3` {{key:sc14:√x}} {{key:sc14:÷}} `0.0575` {{key:sc14:÷}}
   - **Solution**: Evaluates rated secondary current $I_{\text{FLA}} = 1{,}500{,}000 / (\sqrt{3} \times 480) = \mathbf{1{,}804.22\text{ A}}$, and computes short-circuit current $I_{\text{sc}} = 1804.22 / 0.0575 = \mathbf{31{,}377.73\text{ A}}$ (requiring $35\text{ kA}$ or $65\text{ kA}$ rated switchgear).

### Chapter 5: Bending Four Conduits Around the Boiler-Room I-Beam

1. **Conduit Offset Travel and Shrinkage Deduction**
   - **Keystrokes**: `9.5` {{key:sc14:ENTER}} `30` {{key:sc14:OFS}}
   - **Solution**: Evaluates offset geometry to place travel distance $T = 9.5 / \sin(30^\circ) = \mathbf{19.00\text{ in.}}$ in $X$ and conduit shrinkage deduction $S = 9.5 \times (1/\sin 30^\circ - 1/\tan 30^\circ) = \mathbf{2.55\text{ in.}}$ in $Y$.
2. **Compound Rolling Offset Spatial Travel**
   - **Keystrokes**: `14` {{key:sc14:ENTER}} `18` {{key:sc14:ENTER}} `45` {{key:sc14:OFS}}
   - **Solution**: Resolves spatial hypotenuse $D_{\text{spatial}} = \sqrt{14^2 + 18^2} = \mathbf{22.80\text{ in.}}$, yielding travel distance $T = 22.8035 \times \sqrt{2} = \mathbf{32.25\text{ in.}}$ in $X$ and shrinkage $S = \mathbf{9.45\text{ in.}}$ in $Y$.
3. **Three-Point Saddle Mark Layout and Shrink**
   - **Keystrokes**: `4` {{key:sc14:ENTER}} `45` {{key:sc14:FIT}}
   - **Solution**: Calculates outer mark distance from center $D = 4.0 \times 2.613 = \mathbf{10.00\text{ in.}}$ in $X$ and total conduit shrinkage deduction $S = 4.0 \times \frac{3}{16} = \mathbf{1.88\text{ in.}}$ in $Y$.
4. **Four-Bend Saddle Over Rectangular Duct**
   - **Keystrokes**: `6` {{key:sc14:ENTER}} `30` {{key:sc14:OFS}} `2` {{key:sc14:×}} `16` {{key:sc14:ENTER}} `1.608` {{key:sc14:+}}
   - **Solution**: Evaluates individual travel $T = \mathbf{12.00\text{ in.}}$ and shrinkage $S = \mathbf{1.61\text{ in.}}$ per offset. Total conduit length shrinkage across both offsets is $\mathbf{3.22\text{ in.}}$, with inside mark spacing $16.0 + 1.61 = \mathbf{17.61\text{ in.}}$.
5. **NEC Conduit Fill and Conductor Ampacity Derating**
   - **Keystrokes**: `0.864` {{key:sc14:ENTER}} `0.40` {{key:sc14:×}} `30` {{key:sc14:ENTER}} `0.70` {{key:sc14:×}}
   - **Solution**: Computes maximum allowable conductor fill area $0.864 \times 0.40 = \mathbf{0.3456\text{ in.}^2}$, and evaluates derated continuous conductor ampacity $30 \times 0.70 = \mathbf{21.00\text{ A}}$.

### Chapter 6: The Chattering Milling Cutter and the Drifting Pressure Loop

1. **Milling Spindle Speed and Table Feed Rate**
   - **Keystrokes**: `350` {{key:sc14:ENTER}} `3` {{key:sc14:SFM}} `0.006` {{key:sc14:ENTER}} `5` {{key:sc14:×}} {{key:sc14:×}}
   - **Solution**: Evaluates spindle rotation speed $N = \frac{350 \times 3.8197}{3.0} = \mathbf{445.63\text{ RPM}}$ in $X$. Multiplying by chip load and 5 flutes yields table feed rate $F = 445.63 \times 0.006 \times 5 = \mathbf{13.37\text{ in./min}}$ in $X$.
2. **Twelve-Hole Flange Bolt Circle and Inverse Cutter Diameter**
   - **Keystrokes**: `10.5` {{key:sc14:ENTER}} `12` {{key:sc14:BC}} `400` {{key:sc14:ENTER}} `1200` {{key:sc14:SFM}}
   - **Solution**: Evaluates bolt circle chord length $C = 10.5 \times \sin(15^\circ) = \mathbf{2.7176\text{ in.}}$ in $X$. Solves cutting speed equation backward to yield maximum allowable cutter diameter $D = \frac{400 \times 3.8197}{1200} = \mathbf{1.2732\text{ in.}}$.
3. **Process Loop Calibration and Inverse Valve Sizing**
   - **Keystrokes**: `175` {{key:sc14:ENTER}} `250` {{key:sc14:mA}} `85` {{key:sc14:ENTER}} `12` {{key:sc14:Cᵥ}}
   - **Solution**: Scales analog instrumentation loop to return output current $I = 4 + (16 \times 175/250) = \mathbf{15.20\text{ mA}}$ in $X$. Calculates required valve sizing coefficient $C_v = 85 / \sqrt{12} = \mathbf{24.5374}$ in $X$.
4. **CNC Milling Stability Pocket and Feed Acceleration**
   - **Keystrokes**: `800` {{key:sc14:ENTER}} `0.5` {{key:sc14:SFM}} `0.0035` {{key:sc14:ENTER}} `3` {{key:sc14:×}} {{key:sc14:×}}
   - **Solution**: Evaluates spindle rotation speed $N = \frac{800 \times 3.8197}{0.5} = \mathbf{6{,}111.55\text{ RPM}}$, yielding programmed table feed rate $F = 6111.55 \times 0.0035 \times 3 = \mathbf{64.17\text{ in./min}}$.
5. **Hydraulic Oil Valve Sizing and Pressure Inversion**
   - **Keystrokes**: `140` {{key:sc14:ENTER}} `32` {{key:sc14:ENTER}} `0.88` {{key:sc14:Cᵥ}}
   - **Solution**: Evaluates hydraulic valve equation backward to solve for pressure drop $\Delta P = 0.88 \times (140 / 32)^2 = \mathbf{16.84\text{ PSI}}$ in $X$.

## Unit III (SC-16): Digital Systems, Bitwise Logic & Embedded Timing

### Chapter 7: The Stuck Interrupt Flag in the Motor Controller

1. **Two's Complement Additive Inversion**
   - **Keystrokes**: {{key:sc16:DEC}} `8` {{key:sc16:WSZ}} `42` {{key:sc16:NEG}} {{key:sc16:HEX}} `42` {{key:sc16:DEC}} {{key:sc16:+}}
   - **Solution**: Sets 8-bit word size and negates to yield $-42_{10} = \mathbf{\text{0xD6}}$ in $X$. Adding $+42$ produces modular overflow to $\mathbf{\text{0x00}}$, confirming the two's complement additive inverse.
2. **Contiguous Bitmask Generation**
   - **Keystrokes**: {{key:sc16:HEX}} `16` {{key:sc16:WSZ}} `6` {{key:sc16:ENTER}} `9` {{key:sc16:MSK}}
   - **Solution**: Generates a 6-bit contiguous mask shifted left by 9 bit positions to return $(2^6 - 1) \ll 9 = 63 \ll 9 = \mathbf{\text{0x7E00}}$ in $X$.
3. **Logical vs. Arithmetic Right Shift**
   - **Keystrokes**: {{key:sc16:HEX}} `16` {{key:sc16:WSZ}} `C000` {{key:sc16:ENTER}} `3` {{key:sc16:≫}} {{key:sc16:DEC}} `C000` {{key:sc16:HEX}} `3` {{key:sc16:ASR}} {{key:sc16:DEC}}
   - **Solution**: Logical right shift shifts in zero bits, returning $\mathbf{8{,}192}$ (`0x1800`, corrupting the sign). Arithmetic right shift replicates the sign bit, returning exactly $\mathbf{-2{,}048}$ (`0xF800`, $-16{,}384 / 8 = -2{,}048$).
4. **Cortex-M Bit-Band Alias Address Calculation**
   - **Keystrokes**: {{key:sc16:HEX}} `32` {{key:sc16:WSZ}} `40020014` {{key:sc16:ENTER}} `40000000` {{key:sc16:-}} `32` {{key:sc16:DEC}} {{key:sc16:×}} `3` {{key:sc16:ENTER}} `4` {{key:sc16:×}} {{key:sc16:+}} `42000000` {{key:sc16:HEX}} {{key:sc16:+}}
   - **Solution**: Calculates byte offset `0x20014` ($131{,}092_{10}$), multiplies by 32, adds bit word offset $3 \times 4 = 12$, and adds alias base `0x42000000` to yield alias address $\mathbf{\text{0x4240028C}}$.
5. **Q8.8 Fixed-Point Voltage Threshold Encoding**
   - **Keystrokes**: {{key:sc16:DEC}} `16` {{key:sc16:WSZ}} `3.625` {{key:sc16:ENTER}} `256` {{key:sc16:×}} {{key:sc16:HEX}}
   - **Solution**: Multiplies floating-point voltage by scaling factor $2^8 = 256$ to yield $3.625 \times 256 = 928_{10} = \mathbf{\text{0x03A0}}$ in $X$ (integer part `0x03` = $3\text{ V}$, fraction `0xA0`/256 = $0.625\text{ V}$).

### Chapter 8: The Corrupt Sensor Packet Across the Serial Bus

1. **IEEE-754 Single-Precision Float Encoding**
   - **Keystrokes**: {{key:sc16:DEC}} `12.5` {{key:sc16:NEG}} {{key:sc16:FLT}}
   - **Solution**: Decomposes $-12.50 = -1.1001_2 \times 2^3$ into sign $s=1$, biased exponent $e = 3 + 127 = 130$ (`0x82`), and mantissa fraction `0x480000` to assemble binary word $\mathbf{\text{0xC1480000}}$ in $X$.
2. **32-Bit Endianness Reversal**
   - **Keystrokes**: {{key:sc16:HEX}} `32` {{key:sc16:WSZ}} `00409642` {{key:sc16:SWP}}
   - **Solution**: Executes 32-bit byte reversal, transposing byte sequence $[B_0, B_1, B_2, B_3] \to [B_3, B_2, B_1, B_0]$ to return $\mathbf{\text{0x42964000}}$ ($+75.125^\circ\text{C}$ in IEEE-754).
3. **CIDR /28 Subnet Sizing**
   - **Keystrokes**: {{key:sc16:HEX}} `32` {{key:sc16:WSZ}} `FFFFFFFF` {{key:sc16:ENTER}} `4` {{key:sc16:≪}} {{key:sc16:DEC}} `2` {{key:sc16:ENTER}} `4` {{key:sc16:yˣ}} `2` {{key:sc16:-}}
   - **Solution**: Shifts 32 ones left by $32 - 28 = 4$ bits to yield subnet mask $\mathbf{\text{0xFFFFFFF0}}$ (`255.255.255.240`). Total block is $2^4 = 16$ IPs, yielding $16 - 2 = \mathbf{14\text{ usable hosts}}$.
4. **16x Oversampled UART Baud Divisor on an 80 MHz Clock**
   - **Keystrokes**: `80000000` {{key:sc16:ENTER}} `16` {{key:sc16:ENTER}} `921600` {{key:sc16:×}} {{key:sc16:÷}} `5` {{key:sc16:ENTER}} `16` {{key:sc16:×}} `80000000` {{key:sc16:x⇄y}} {{key:sc16:÷}} `921600` {{key:sc16:-}} `921600` {{key:sc16:÷}} `100` {{key:sc16:×}}
   - **Solution**: Calculates ideal divisor $\text{BRR} = 80\times 10^6 / (16 \times 921{,}600) = \mathbf{5.4253}$. Rounding to integer divisor 5 yields actual baud $1{,}000{,}000\text{ bps}$, producing an intolerable error of $\mathbf{+8.51\%}$.
5. **Reflected CRC-32 Verification of a 4-Byte Payload**
   - **Keystrokes**: {{key:sc16:HEX}} `32` {{key:sc16:WSZ}} `12345678` {{key:sc16:ENTER}} `32` {{key:sc16:CRC}}
   - **Solution**: Executes reflected polynomial division over Galois Field $GF(2)$ using generator polynomial `0xEDB88320`, returning standard Ethernet/ZIP frame check sequence $\mathbf{\text{0xDF8A8A2B}}$.

### Chapter 9: Partitioning the Factory Floor Subnet and ADC Front End

1. **Precision Sixteen-Bit ADC Step Resolution and Code Inversion**
   - **Keystrokes**: `2.5` {{key:sc16:ENTER}} `65536` {{key:sc16:÷}} `1000000` {{key:sc16:×}} `35904` {{key:sc16:ENTER}} `2.5` {{key:sc16:×}} `65536` {{key:sc16:÷}}
   - **Solution**: Calculates quantization step resolution $V_{\text{LSB}} = 2.50 / 65536 = \mathbf{38.147\ \mu\text{V}}$ in $X$. Reconstructing analog input voltage yields $V_{\text{in}} = (35{,}904 / 65536) \times 2.50 = \mathbf{1.36975\text{ V}}$.
2. **CIDR Subnet Capacity and Broadcast Address Calculation**
   - **Keystrokes**: `32` {{key:sc16:ENTER}} `22` {{key:sc16:-}} `2` {{key:sc16:x⇄y}} {{key:sc16:yˣ}} `2` {{key:sc16:-}}
   - **Solution**: Calculates host address space $2^{32-22} = 2^{10} = \mathbf{1{,}024\text{ IPs}}$, yielding $1024 - 2 = \mathbf{1{,}022\text{ usable hosts}}$. Broadcast address is $\mathbf{10.240.19.255}$ (`0x0AF013FF`).
3. **Cache-Line Descriptor Alignment and Power-of-Two Ring Sizing**
   - **Keystrokes**: `128` {{key:sc14:ENTER}} `48` {{key:sc14:×}} `64` {{key:sc14:ENTER}} `6144` {{key:sc14:x⇄y}} {{key:sc14:÷}}
   - **Solution**: Calculates total raw buffer footprint $128 \times 48 = \mathbf{6{,}144\text{ bytes}}$. Because $6144 / 64 = 96.00$ divides evenly, zero padding bytes are required, aligning naturally to cache-line boundaries.
4. **High-Speed Synchronous SPI Bus Setup Timing Margin**
   - **Keystrokes**: `20` {{key:sc16:ENTER}} `12` {{key:sc16:-}} `2.5` {{key:sc16:-}} `6` {{key:sc16:-}}
   - **Solution**: Calculates remaining setup slack margin $T_{\text{slack}} = 20.0 - (12.0 + 2.5 + 6.0) = 20.0 - 20.5 = \mathbf{-0.50\text{ ns}}$, revealing a severe timing violation requiring a reduced bus clock.
5. **PWM Ultrasonic Auto-Reload Period Sizing**
   - **Keystrokes**: `120000000` {{key:sc16:ENTER}} `2` {{key:sc16:ENTER}} `20000` {{key:sc16:×}} {{key:sc16:÷}}
   - **Solution**: In center-aligned mode, the timer counts up and down, requiring period count $\text{ARR} = f_{\text{TIM}} / (2 \times f_{\text{PWM}}) = 120\times 10^6 / 40{,}000 = \mathbf{3{,}000}$ (`0x0BB8`).

## Unit IV (SC-24): Cinema, Broadcast Engineering & Concert Production

### Chapter 10: The Missing Three-Point-Six Seconds at the Broadcast Desk

1. **Two-Hour Feature NTSC Drift in Seconds and Packed Timecode**
   - **Keystrokes**: `30` {{key:sc24:ENTER}} `2.000000` {{key:sc24:▸FRM}} `30` {{key:sc24:÷}} {{key:sc24:DF}} `7200` {{key:sc24:-}} `30` {{key:sc24:×}} `30` {{key:sc24:ENTER}} `216` {{key:sc24:▸TC}}
   - **Solution**: Calculates total frame count $F = \mathbf{216{,}000\text{ frames}}$, true wall-clock duration $t_{\text{real}} = \mathbf{7207.2072\text{ s}}$, and accumulated timecode drift $\Delta F = \mathbf{216\text{ frames}}$ ($+7.2072\text{ s}$, packed `0.000706` or `00:00:07:06`).
2. **Commercial Act Trim via Packed Timecode Subtraction**
   - **Keystrokes**: `0.241218` {{key:sc24:ENTER}} `0.223000` {{key:sc24:-TC}} `30` {{key:sc24:x⇄y}} {{key:sc24:▸FRM}}
   - **Solution**: Performs packed base-60/base-30 subtraction to yield trim $\Delta t = \mathbf{\text{00:01:42:18}}$ (`0.014218`) and total frame count reduction $\Delta F = \mathbf{3{,}078\text{ frames}}$.
3. **High-Speed Phantom Overcrank at 240 fps in the Timecode Solver**
   - **Keystrokes**: `0.85` {{keycap:S}} `240` {{keycap:R}} {{key:sc24:XEQ}} {{keycap:F}} `23.976` {{keycap:R}} {{key:sc24:XEQ}} {{keycap:S}}
   - **Solution**: In the Timecode Solver Workspace ($F = S \times R$), captures $F = \mathbf{204\text{ frames}}$. Solving for screen duration at $23.976\text{ fps}$ yields $S = 204 / 23.976 = \mathbf{8.5085\text{ s}}$ of smooth slow motion.
4. **Conforming 23.976 fps Archival Master to 29.970 fps via 2:3 Pulldown**
   - **Keystrokes**: `64800` {{key:sc24:ENTER}} `23.976024` {{key:sc24:÷}} `29.970030` {{key:sc24:×}}
   - **Solution**: Evaluates continuous wall-clock run time $t = \mathbf{2702.70\text{ s}}$ ($45\text{ min } 2.7\text{ s}$) and expanded broadcast frame count $F = \mathbf{81{,}000\text{ frames}}$, confirming the exact $5/4 = 1.25\times$ telecine cadence expansion.
5. **Drop-Frame Minute-Boundary Label Skip Audit**
   - **Keystrokes**: `0.041510` {{key:sc24:ENTER}} `0.074225` {{key:sc24:+TC}} `0.031215` {{key:sc24:+TC}}
   - **Solution**: Accumulates clips via packed timecode addition to reach total duration `0.151020` ($15\text{ min } 10\text{ s } 20\text{ frames}$). At 15 elapsed minutes, skipping 2 frame numbers per minute except on tens gives $N_{\text{dropped}} = 2(15 - \lfloor 15/10 \rfloor) = 2(15 - 1) = \mathbf{28\text{ dropped labels}}$.

### Chapter 11: Holding Focus on the Steadicam Close-Up at Dusk

1. **Super 35 Portrait Prime Field of View and Hyperfocal Distance**
   - **Keystrokes**: `24.89` {{key:sc24:ENTER}} `85` {{key:sc24:FOV}} `85` {{key:sc24:ENTER}} `4` {{key:sc24:ENTER}} `0.025` {{key:sc24:DOF}}
   - **Solution**: Computes horizontal field of view $A = 2\arctan(24.89 / (2 \times 85)) = \mathbf{16.659^\circ}$. Evaluates hyperfocal distance $H = F^2 / (N \times C) = 85^2 / (4 \times 0.025) = 72{,}250\text{ mm} = \mathbf{72.25\text{ m}}$.
2. **European 25 fps Exterior Exposure and 5-Stop ND Filter**
   - **Keystrokes**: `25` {{key:sc24:ENTER}} `180` {{key:sc24:SHT}} `11` {{key:sc24:ENTER}} `0.02` {{key:sc24:EV}} `5` {{key:sc24:▸ND}}
   - **Solution**: Computes scene exposure $E = \log_2(11^2 / 0.02) = \mathbf{12.563\text{ EV}}$. Opening $5\text{ stops}$ requires neutral density optical density $D = 5 \times 0.3 = \mathbf{1.5}$ in $X$ and light reduction filter factor $2^5 = \mathbf{32\times}$ in $Y$.
3. **Follow-Spot Illuminance and Daylight-to-Tungsten Mired Shift**
   - **Keystrokes**: `48000` {{key:sc24:ENTER}} `12` {{key:sc24:x²}} {{key:sc24:÷}} {{key:sc24:▸fc}} `5600` {{key:sc24:ENTER}} `3200` {{key:sc24:GEL}}
   - **Solution**: Evaluates inverse-square illuminance $E_{\text{lx}} = 48{,}000 / 144 = \mathbf{333.333\text{ lx}}$ and converts to $E_{\text{fc}} = \mathbf{30.968\text{ fc}}$. Mired shift $\Delta M = 10^6(1/3200 - 1/5600) = \mathbf{+133.93\text{ Mireds}}$ (Full CTO).
4. **Anamorphic 2.0x Squeeze Field of View and Full-Frame Matching**
   - **Keystrokes**: `49.78` {{key:sc24:ENTER}} `40` {{key:sc24:FOV}} `63.785` {{keycap:A}} `36` {{keycap:W}} {{key:sc24:XEQ}} {{keycap:F}}
   - **Solution**: Yields horizontal angular coverage $A = 2\arctan(49.78 / 80) = \mathbf{63.785^\circ}$. Matching that coverage on a $36.0\text{ mm}$ full-frame sensor requires spherical focal length $F = \mathbf{28.93\text{ mm}}$.
5. **Micro-Reciprocal Degree Gel Stacking and Resulting Color Temperature**
   - **Keystrokes**: `6000` {{key:sc24:▸MRD}} `137` {{key:sc24:+}} `68` {{key:sc24:+}} `1000000` {{key:sc24:x⇄y}} {{key:sc24:÷}}
   - **Solution**: Sums native Mired rating $166.67$ and combined gel shift $+205\text{ Mireds}$ to reach total $371.67\text{ Mireds}$, yielding final correlated color temperature $T_{\text{final}} = 10^6 / 371.67 = \mathbf{2{,}690.5\text{ K}}$.

### Chapter 12: Aligning the Stadium Delay Towers Before Downbeat

1. **Second-Ring Stadium Delay Tower Alignment at Elevated Temperature**
   - **Keystrokes**: `80` {{key:sc24:ENTER}} `30` {{key:sc24:DLY}} `80` {{key:sc24:ENTER}} `20` {{key:sc24:DLY}} {{key:sc24:-}}
   - **Solution**: Speed of sound is $v_s = 331.3\sqrt{1 + 30/273.15} = \mathbf{349.48\text{ m/s}}$. Propagation delay is $\Delta t_{30} = 80 / 349.48 = \mathbf{228.91\text{ ms}}$. Compared to $20^\circ\text{C}$ delay ($232.74\text{ ms}$), sound arrives $\mathbf{3.83\text{ ms}}$ sooner.
2. **Three-Source Stage Noise Summation and Front-of-House Attenuation**
   - **Keystrokes**: `92` {{key:sc24:ENTER}} `90` {{key:sc24:dB}} `94` {{key:sc24:dB}} `2` {{key:sc24:ENTER}} `32` {{key:sc24:SPL}}
   - **Solution**: Incoherent decibel summation yields stage level $L_{\Sigma} = \mathbf{96.83\text{ dBSPL}}$. Spherical inverse-square attenuation over distance ratio $32/2 = 16\times$ ($20\log_{10}(16) = 24.08\text{ dB}$) reduces front-of-house level to $L_{\text{FOH}} = \mathbf{72.75\text{ dBSPL}}$.
3. **Broadcast Line-Level Voltage and Maximum PA Throw Distance**
   - **Keystrokes**: `18` {{key:sc24:▸V}} `138` {{key:sc24:ENTER}} `102` {{key:sc24:-}} `20` {{key:sc24:÷}} `10` {{key:sc24:x⇄y}} {{key:sc24:yˣ}}
   - **Solution**: Converts $+18.0\text{ dBu}$ to line voltage $V_{\text{rms}} = 0.7746 \times 10^{18/20} = \mathbf{6.153\text{ V}_{\text{rms}}}$. Allowable free-field attenuation is $138 - 102 = 36\text{ dB}$, yielding maximum throw distance $D = 10^{36/20} = \mathbf{63.10\text{ m}}$.
4. **Architectural Reverberation Sizing via Sabine's Formula**
   - **Keystrokes**: `0.161` {{key:sc24:ENTER}} `1800` {{key:sc24:×}} `217.6` {{key:sc24:÷}} `0.161` {{key:sc24:ENTER}} `1800` {{key:sc24:×}} `0.85` {{key:sc24:÷}} `217.6` {{key:sc24:-}}
   - **Solution**: Sabine's formula evaluates untreated room reverberation $RT_{60} = 0.161(1800) / 217.6 = \mathbf{1.332\text{ s}}$. Reaching target $0.85\text{ s}$ requires total absorption $340.94\text{ sabins}$, demanding an additional $\Delta A = \mathbf{123.34\text{ m}^2\text{-sabins}}$.
5. **Axial Room Mode Resonances and Comb Filtering**
   - **Keystrokes**: `343` {{key:sc24:ENTER}} `2` {{key:sc24:ENTER}} `4.25` {{key:sc24:×}} {{key:sc24:÷}} `2` {{key:sc24:×}} `3` {{key:sc24:×}} `1` {{key:sc24:ENTER}} `2` {{key:sc24:ENTER}} `0.00245` {{key:sc24:×}} {{key:sc24:÷}}
   - **Solution**: Axial modes resonate at $f_1 = \mathbf{40.35\text{ Hz}}$, $f_2 = \mathbf{80.71\text{ Hz}}$, and $f_3 = \mathbf{121.06\text{ Hz}}$. Reflection delay $\Delta t = 2.45\text{ ms}$ creates its first destructive cancellation notch at $f_{\text{null}} = 1/(2 \times 0.00245) = \mathbf{204.08\text{ Hz}}$.

## Unit V (SC-50): Radio-Frequency Engineering & Telecommunications

### Chapter 13: The Reflected Wave on the Mountain Repeater Coax

1. **75-Ohm Broadcast Coax Mismatch and Aviation Quarter-Wave Whip**
   - **Keystrokes**: `75` {{keycap:Z₀}} `50` {{key:sc50:ENTER}} `25` {{keycap:jX}} {{keycap:SWR}} `121.5` {{key:sc50:λ/L}} `4` {{key:sc50:÷}}
   - **Solution**: Evaluates load mismatch against $75\ \Omega$ to find $\text{VSWR} = \mathbf{1.768 : 1}$. Computes full-wavelength $\lambda = 2.4674\text{ m}$ at $121.5\text{ MHz}$, yielding quarter-wave whip length $\ell_{\lambda/4} = \mathbf{0.617\text{ m}}$ ($61.7\text{ cm}$).
2. **Commercial Specification Limit Return Loss and Reflected Power**
   - **Keystrokes**: `1.5` {{key:sc50:ENTER}} `1` {{key:sc50:-}} `1.5` {{key:sc50:ENTER}} `1` {{key:sc50:+}} {{key:sc50:÷}} {{key:sc50:x²}} {{key:sc50:LOG}} `10` {{key:sc50:×}}
   - **Solution**: Evaluates reflection coefficient $\Gamma = (1.5 - 1)/(1.5 + 1) = \mathbf{0.2000}$, yielding Return Loss $\text{RL} = -20\log_{10}(0.2) = \mathbf{13.98\text{ dB}}$ and reflected power fraction $P_{\text{refl}} = \Gamma^2 = \mathbf{4.00\%}$.
3. **Power Transistor L-Network Impedance Match and Backward Inductance**
   - **Keystrokes**: `50` {{key:sc50:ENTER}} `12.5` {{key:sc50:÷}} `1` {{key:sc50:-}} {{key:sc50:√x}} `12.5` {{key:sc50:×}} `144` {{key:sc50:ENTER}} `6` {{key:sc50:10ˣ}} {{key:sc50:×}} `2` {{key:sc50:×}} {{key:sc50:π}} {{key:sc50:×}} {{key:sc50:÷}} `1` {{key:sc50:ENTER}} `9` {{key:sc50:10ˣ}} {{key:sc50:×}}
   - **Solution**: Computes matching quality factor $Q = \sqrt{50/12.5 - 1} = \mathbf{1.732}$, series reactance $X_{\text{series}} = Q \times 12.5 = \mathbf{21.65\ \Omega}$, and series inductance $L = 21.65 / (2\pi \times 144\times 10^6) = \mathbf{23.93\text{ nH}}$.
4. **Skin Depth and High-Frequency AC Resistance of Copper Traces**
   - **Keystrokes**: `1` {{key:sc50:ENTER}} {{key:sc50:π}} `10` {{key:sc50:ENTER}} `9` {{key:sc50:10ˣ}} {{key:sc50:×}} {{key:sc50:×}} `4` {{key:sc50:ENTER}} {{key:sc50:π}} {{key:sc50:×}} `1` {{key:sc50:ENTER}} `7` {{key:sc50:+/-}} {{key:sc50:10ˣ}} {{key:sc50:×}} {{key:sc50:×}} `5.8` {{key:sc50:ENTER}} `7` {{key:sc50:10ˣ}} {{key:sc50:×}} {{key:sc50:×}} {{key:sc50:÷}} {{key:sc50:√x}} `1000000` {{key:sc50:×}}
   - **Solution**: Evaluates skin depth equation $\delta = 1 / \sqrt{\pi f \mu \sigma}$ at $10\text{ GHz}$ to yield $\delta = \mathbf{0.652\ \mu\text{m}}$ ($652\text{ nm}$), demonstrating that current is confined to a microscopic surface boundary.
5. **Quarter-Wave Coaxial Stub Length and RF Choke Transformation**
   - **Keystrokes**: `299792458` {{key:sc50:ENTER}} `433.92` {{key:sc50:ENTER}} `6` {{key:sc50:10ˣ}} {{key:sc50:×}} {{key:sc50:÷}} `0.66` {{key:sc50:×}} `4` {{key:sc50:÷}}
   - **Solution**: Computes free-space wavelength $\lambda_0 = c / f = \mathbf{0.6924\text{ m}}$, and applies velocity factor $0.66$ to find physical quarter-wavelength cut length $\ell_{\text{stub}} = (0.6924 \times 0.66) / 4 = \mathbf{0.1142\text{ m}}$ ($11.42\text{ cm}$).

### Chapter 14: Clearing the Ridge on a Twelve-Kilometer Microwave Backhaul

1. **Ten-Kilometer 2.4 GHz Campus Link Budget**
   - **Keystrokes**: `2400` {{key:sc50:ENTER}} `10` {{key:sc50:FSL}} `20` {{key:sc50:ENTER}} `24` {{key:sc50:+}} `24` {{key:sc50:+}} `120.04` {{key:sc50:-}}
   - **Solution**: Evaluates free-space loss $\text{FSPL} = 20\log_{10}(10) + 20\log_{10}(2400) + 32.44 = \mathbf{120.04\text{ dB}}$. Net link budget yields received power $P_{\text{rx}} = 20 + 24 + 24 - 120.04 = \mathbf{-52.04\text{ dBm}}$, delivering healthy fade margin.
2. **Six-Gigahertz Eighteen-Kilometer Fresnel Zone Clearance Audit**
   - **Keystrokes**: `6` {{key:sc50:ENTER}} `18` {{key:sc50:F₁}} `0.6` {{key:sc50:×}}
   - **Solution**: Evaluates midpoint first Fresnel radius $R_1 = 17.32\sqrt{(9 \times 9)/(6 \times 18)} = \mathbf{15.00\text{ m}}$. Mandatory $60\%$ zone clearance requires an unobstructed vertical clearance of $0.60 \times 15.00 = \mathbf{9.00\text{ m}}$ above the terrain ridge.
3. **Millimeter-Wave 28 GHz Urban Backhaul Loss**
   - **Keystrokes**: `28000` {{key:sc50:ENTER}} `0.85` {{key:sc50:FSL}} `14` {{key:sc50:ENTER}} `18` {{key:sc50:+}} `18` {{key:sc50:+}} `119.96` {{key:sc50:-}}
   - **Solution**: Computes high-frequency free-space path loss $\text{FSPL} = \mathbf{119.96\text{ dB}}$. Received signal strength is $P_{\text{rx}} = 14 + 18 + 18 - 119.96 = \mathbf{-69.96\text{ dBm}}$.
4. **Atmospheric Rain Attenuation on an 18 GHz Microwave Hop**
   - **Keystrokes**: `3.2` {{key:sc50:ENTER}} `7.5` {{key:sc50:×}}
   - **Solution**: Evaluates path attenuation $\Delta A_{\text{rain}} = \gamma \times d = 3.20 \times 7.50 = \mathbf{24.00\text{ dB}}$, requiring an additional $24\text{ dB}$ of transmitter power or antenna gain to maintain link availability.
5. **Asymmetric Fresnel Clearance at Unequal Obstacle Distances**
   - **Keystrokes**: `11` {{key:sc50:ENTER}} `4` {{key:sc50:ENTER}} `20` {{key:sc50:×}} `11` {{key:sc50:ENTER}} `24` {{key:sc50:×}} {{key:sc50:÷}} {{key:sc50:√x}} `17.32` {{key:sc50:×}}
   - **Solution**: Computes asymmetric Fresnel radius $R_1 = 17.32\sqrt{(4 \times 20)/(11 \times 24)} = 17.32\sqrt{80/264} = \mathbf{9.54\text{ m}}$, defining the required vertical clearance window.

### Chapter 15: Isolating the Mixer Spurious Products on the Tracking Generator

1. **Three-Stage Receiver Chain Noise Figure and Spurious-Free Dynamic Range**
   - **Keystrokes**: `1.2` `10` {{key:sc50:÷}} {{key:sc50:10ˣ}} `2` `10` {{key:sc50:÷}} {{key:sc50:10ˣ}} `1` {{key:sc50:-}} `20` `10` {{key:sc50:÷}} {{key:sc50:10ˣ}} {{key:sc50:÷}} {{key:sc50:+}} `6` `10` {{key:sc50:÷}} {{key:sc50:10ˣ}} `1` {{key:sc50:-}} `18` `10` {{key:sc50:÷}} {{key:sc50:10ˣ}} {{key:sc50:÷}} {{key:sc50:+}} {{key:sc50:LOG}} `10` {{key:sc50:×}} `30` {{key:sc50:ENTER}} `-174` {{key:sc50:ENTER}} `1.23` {{key:sc50:+}} `40` {{key:sc50:+}} {{key:sc50:-}} `2` {{key:sc50:×}} `3` {{key:sc50:÷}}
   - **Solution**: Friis' cascade formula evaluates total noise factor $F_{\text{casc}} = 1.328$, giving cascaded noise figure $NF_{\text{casc}} = \mathbf{1.23\text{ dB}}$. Noise floor in $10\text{ kHz}$ is $P_{\text{noise}} = -174 + 1.23 + 40 = -132.77\text{ dBm}$. Evaluating dynamic range yields $\text{SFDR} = \frac{2}{3}(OIP_3 - P_{\text{noise}}) = \frac{2}{3}(30 - (-132.77)) = \mathbf{108.51\text{ dB}}$.
2. **Wireless Local Loop Shannon Channel Capacity**
   - **Keystrokes**: `25` `10` {{key:sc50:÷}} {{key:sc50:10ˣ}} `1` {{key:sc50:+}} {{key:sc50:LOG}} `2` {{key:sc50:LOG}} {{key:sc50:÷}} `20` {{key:sc50:×}}
   - **Solution**: Converts $25\text{ dB}$ to linear ratio $S/N = 10^{2.5} = \mathbf{316.23}$. Applying Shannon's theorem $C = B\log_2(1 + S/N) = 20 \times \log_2(317.23) = \mathbf{166.19\text{ Mbps}}$.
3. **X-Band Weather Radar Doppler Shift and Velocity**
   - **Keystrokes**: `2850` {{key:sc50:ENTER}} `299792458` {{key:sc50:×}} `2` {{key:sc50:÷}} `9350000000` {{key:sc50:÷}} `2.23694` {{key:sc50:×}}
   - **Solution**: Applies radar Doppler equation $v_r = (c \times \Delta f) / (2 f_0)$ to find storm radial velocity $v_r = \mathbf{45.69\text{ m/s}}$, converting to $\mathbf{102.20\text{ mph}}$—indicating extreme tornadic wind shear.
4. **Mixer Intermodulation Overload and Spurious Distortion**
   - **Keystrokes**: `15` {{key:sc50:ENTER}} `10` {{key:sc50:+/-}} {{key:sc50:-}} `2` {{key:sc50:×}} `10` {{key:sc50:+/-}} {{key:sc50:x⇄y}} {{key:sc50:-}}
   - **Solution**: Third-order intermodulation suppression is $\Delta IM_3 = 2(IIP_3 - P_{\text{in}}) = 2(15 - (-10)) = \mathbf{50.00\text{ dBc}}$, placing spurious products at absolute power level $P_{IM3} = -10 - 50 = \mathbf{-60.00\text{ dBm}}$.
5. **Relativistic Doppler Shift on an X-Band Lunar Downlink**
   - **Keystrokes**: `11200` {{key:sc50:ENTER}} `299792458` {{key:sc50:÷}} `1` {{key:sc50:ENTER}} `3.7359` {{key:sc50:ENTER}} `5` {{key:sc50:+/-}} `10ˣ` {{key:sc50:+}} `1` {{key:sc50:ENTER}} `3.7359` {{key:sc50:ENTER}} `5` {{key:sc50:+/-}} `10ˣ` {{key:sc50:-}} {{key:sc50:÷}} {{key:sc50:√x}} `8450000000` {{key:sc50:×}} `8450000000` {{key:sc50:-}}
   - **Solution**: Computes velocity ratio $\beta = 11{,}200 / 2.998\times 10^8 = \mathbf{3.7359 \times 10^{-5}}$, giving positive Doppler frequency shift $\Delta f = \mathbf{+315.69\text{ kHz}}$ and received downlink frequency $f_{\text{rx}} = \mathbf{8.450316\text{ GHz}}$.

## Unit VI (SC-60): Analytical Chemistry & Laboratory Sciences

### Chapter 16: Formulating the Lyophilized Reagent Standard

1. **Hydrate Mass and Active Chemical Fraction**
   - **Keystrokes**: `120.366` {{key:sc60:ENTER}} `246.474` {{key:sc60:÷}} `5` {{key:sc60:x⇄y}} {{key:sc60:÷}}
   - **Solution**: Active anhydrous mass fraction is $120.366 / 246.474 = \mathbf{0.48835}$ ($48.84\%$). Weighing target is $m_{\text{hydrate}} = 5.000 / 0.48835 = \mathbf{10.2388\text{ g}}$.
2. **Volumetric Buffer Preparation from Dry Reagents**
   - **Keystrokes**: `0.25` {{key:sc60:ENTER}} `0.5` {{key:sc60:×}} `121.135` {{key:sc60:×}} `0.5` {{key:sc60:÷}}
   - **Solution**: Evaluates solute mass requirement $m = C \times V \times M = 0.2500 \times 0.5000 \times 121.135 = \mathbf{15.1419\text{ g}}$, with mass concentration $\rho = m / V = \mathbf{30.2838\text{ g/L}}$.
3. **Multi-Step Stock Aliquot Cutting and Dilution**
   - **Keystrokes**: `0.025` {{key:sc60:ENTER}} `50` {{key:sc60:×}} `10` {{key:sc60:÷}} `1000` {{key:sc60:×}} `50` {{key:sc60:ENTER}} `0.125` {{key:sc60:-}}
   - **Solution**: Applying dilution equation $C_1 V_1 = C_2 V_2$ yields aliquot volume $V_1 = (0.025 \times 50) / 10 = 0.1250\text{ mL} = \mathbf{125.0\ \mu\text{L}}$. Volume of diluent is $50.0 - 0.125 = \mathbf{49.875\text{ mL}}$.
4. **Serial Dilution Error Propagation**
   - **Keystrokes**: `1.2` {{key:sc60:x²}} `0.4` {{key:sc60:x²}} {{key:sc60:+}} {{key:sc60:√x}} `4` {{key:sc60:√x}} {{key:sc60:×}}
   - **Solution**: Single stage error is $\sigma_{\text{stage}} = \sqrt{1.2^2 + 0.4^2} = \mathbf{1.265\%}$. Propagating across four uncorrelated serial stages gives total analytical uncertainty $\sigma_{\text{total}} = \sqrt{4} \times 1.265\% = \mathbf{2.530\%}$.
5. **Cryoscopic Freezing Point Depression of Saline**
   - **Keystrokes**: `9` {{key:sc60:ENTER}} `58.443` {{key:sc60:÷}} `1.86` {{key:sc60:×}} `1.858` {{key:sc60:×}} {{key:sc60:+/-}}
   - **Solution**: Osmolality is $\xi = m \times i = 0.1540 \times 1.860 = \mathbf{0.2864\text{ Osm/kg}}$ ($286.4\text{ mOsm/kg}$). Freezing point depression is $\Delta T_f = K_f \times \xi = 1.858 \times 0.2864 = 0.5322^\circ\text{C}$, yielding freezing point $T_f = \mathbf{-0.5322^\circ\text{C}}$.

### Chapter 17: Holding pH 7.40 Against an Acid Spike

1. **Hydronium Ion Concentration and Autoionization**
   - **Keystrokes**: `7.382` {{key:sc60:+/-}} `10` {{key:sc60:x⇄y}} {{key:sc60:yˣ}} `1000000000` {{key:sc60:×}} `1` {{key:sc60:ENTER}} `14` {{key:sc60:+/-}} `10ˣ` `4.15` {{key:sc60:ENTER}} `9` {{key:sc60:+/-}} `10ˣ` {{key:sc60:÷}}
   - **Solution**: Hydronium ion concentration is $[\text{H}_3\text{O}^+] = 10^{-7.382} = 4.150 \times 10^{-8}\text{ M} = \mathbf{41.50\text{ nM}}$. Hydroxide ion concentration is $[\text{OH}^-] = K_w / [\text{H}_3\text{O}^+] = \mathbf{2.410 \times 10^{-7}\text{ M}}$ ($241.0\text{ nM}$).
2. **Acetate Buffer Ratio and pH Shift**
   - **Keystrokes**: `0.1` {{key:sc60:ENTER}} `0.05` {{key:sc60:÷}} {{key:sc60:LOG}} `4.756` {{key:sc60:+}} `0.09` {{key:sc60:ENTER}} `0.06` {{key:sc60:÷}} {{key:sc60:LOG}} `4.756` {{key:sc60:+}}
   - **Solution**: Initial Henderson–Hasselbalch pH is $\text{pH} = 4.756 + \log_{10}(2.0) = \mathbf{5.057}$. After adding $0.010\text{ M}$ acid, $[\text{A}^-] = 0.090$ and $[\text{HA}] = 0.060$, shifting pH to $4.756 + \log_{10}(1.5) = \mathbf{4.932}$ (a buffering shift of only $\mathbf{-0.125\text{ pH units}}$).
3. **Van Slyke Maximum Buffer Capacity**
   - **Keystrokes**: `2.3026` {{key:sc60:ENTER}} `0.08` {{key:sc60:×}} `0.25` {{key:sc60:×}} `2.3026` {{key:sc60:ENTER}} `0.08` {{key:sc60:×}} `0.9091` {{key:sc60:×}} `0.0909` {{key:sc60:×}}
   - **Solution**: Maximum buffer capacity at $\text{pH} = \text{p}K_a$ is $\beta_{\max} = 0.5756 \times C = \mathbf{0.04605\text{ M/pH}}$ ($46.05\text{ mM/pH}$). At $\text{pH} = 8.550$ ($\alpha_1 = 0.9091, \alpha_0 = 0.0909$), capacity drops to $\beta = \mathbf{0.01522\text{ M/pH}}$ ($15.22\text{ mM/pH}$)—a $67\%$ loss in protective buffering capacity.
4. **Volumetric Standardization of Hydrochloric Acid**
   - **Keystrokes**: `0.105` {{key:sc60:ENTER}} `28.45` {{key:sc60:×}} `25` {{key:sc60:÷}}
   - **Solution**: Equivalence stoichiometry yields acid molarity $C_{\text{HCl}} = (C_{\text{titrant}} \times V_{\text{eq}}) / V_{\text{sample}} = (0.1050 \times 28.45) / 25.00 = \mathbf{0.1195\text{ M}}$.
5. **Diprotic Carbonic Acid Blood Buffer Shift**
   - **Keystrokes**: `24` {{key:sc60:ENTER}} `1.2` {{key:sc60:÷}} {{key:sc60:LOG}} `6.1` {{key:sc60:+}} `24` {{key:sc60:ENTER}} `2.4` {{key:sc60:÷}} {{key:sc60:LOG}} `6.1` {{key:sc60:+}}
   - **Solution**: Normal arterial pH is $\text{pH} = 6.100 + \log_{10}(24.0 / 1.20) = 6.100 + 1.301 = \mathbf{7.401}$. Acute doubling of dissolved carbon dioxide acid drops pH to $6.100 + \log_{10}(10.0) = \mathbf{7.100}$—inducing severe, life-threatening uncompensated respiratory acidosis.

### Chapter 18: Reading Protein Concentration Through a Quartz Cuvette

1. **Spectrophotometric DNA Quantification and Purity**
   - **Keystrokes**: `0.45` {{key:sc60:ENTER}} `50` {{key:sc60:×}} `0.45` {{key:sc60:ENTER}} `0.245` {{key:sc60:÷}}
   - **Solution**: Calculates mass concentration $\rho = 0.450 \times 50.0 = \mathbf{22.50\ \mu\text{g/mL}}$, and purity ratio $A_{260} / A_{280} = 0.450 / 0.245 = \mathbf{1.837}$, confirming a high-purity nucleic acid preparation free of protein contamination.
2. **Arrhenius Shelf-Life Reaction Rate Acceleration**
   - **Keystrokes**: `253.15` {{key:sc60:𝑥⁻¹}} `277.15` {{key:sc60:𝑥⁻¹}} {{key:sc60:-}} `92000` {{key:sc60:×}} `8.31446` {{key:sc60:÷}} {{key:sc60:𝑒ˣ}}
   - **Solution**: Applying the Arrhenius equation $k_2 / k_1 = \exp[(E_a/R)(1/T_1 - 1/T_2)]$ reveals an acceleration factor of $\mathbf{41.42\times}$—the protein degrades more than forty times faster in refrigerated storage than in frozen containment.
3. **Centrifuge Rotor Speed Conversion**
   - **Keystrokes**: `2000` {{key:sc60:ENTER}} `1.1182` {{key:sc60:ENTER}} `5` {{key:sc60:+/-}} `10ˣ` {{key:sc60:×}} `16.5` {{key:sc60:×}} {{key:sc60:÷}} {{key:sc60:√x}}
   - **Solution**: Using conversion equation $\text{RPM} = \sqrt{\text{RCF} / (1.1182 \times 10^{-5} \times r)}$ yields rotor speed $\text{RPM} = \mathbf{3{,}291.6\text{ RPM}}$ (set to $3{,}300\text{ RPM}$ on the digital centrifuge panel).
4. **Nernst Half-Cell Electrochemical Potential**
   - **Keystrokes**: `0.01` {{key:sc60:LOG}} `0.05916` {{key:sc60:×}} `2` {{key:sc60:÷}} `1.1` {{key:sc60:x⇄y}} {{key:sc60:-}}
   - **Solution**: Applying the Nernst equation $E = E^\circ - (0.05916/n)\log_{10}(Q)$ yields $E = 1.100 - (-0.05916) = \mathbf{1.1592\text{ V}}$.
5. **Gibbs Free Energy and Chemical Equilibrium Constant**
   - **Keystrokes**: `15500` {{key:sc60:+/-}} `8.31446` {{key:sc60:÷}} `310.15` {{key:sc60:÷}} {{key:sc60:+/-}} {{key:sc60:𝑒ˣ}}
   - **Solution**: Evaluates thermodynamic equilibrium $K_{\text{eq}} = \exp(-\Delta G^\circ / (RT)) = \exp(15{,}500 / 2{,}578.7) = \mathbf{409.28}$, demonstrating that product formation is strongly favored at equilibrium.

## Unit VII (SC-78): Culinary Arts, Commercial Baking & Oenology

### Chapter 19: Scaling Two Hundred Country Loaves on a Hot July Morning

1. **Ciabatta High-Hydration Inverse Scaling**
   - **Keystrokes**: `80.68` {{keycap:I}} `201.7` {{keycap:P}} {{key:sc78:XEQ}} {{keycap:F}} `0.82` {{key:sc78:×}}
   - **Solution**: In the Baker's Percentage Workspace ($P = I / F \times 100$), solving for flour yields $F = \mathbf{40.00\text{ kg}}$. Multiplying by $82\%$ hydration requires water mass $I_{\text{water}} = \mathbf{32.80\text{ kg}}$.
2. **True Hydration with a Stiff Biga Pre-Ferment**
   - **Keystrokes**: `1000` {{key:sc78:ENTER}} `200` {{key:sc78:+}} `620` {{key:sc78:ENTER}} `100` {{key:sc78:+}} {{key:sc78:HYD}}
   - **Solution**: Total formulation flour is $1000 + 200 = 1{,}200\text{ g}$ and total water is $620 + 100 = 720\text{ g}$. Evaluating true hydration yields $\text{HYDR}_{\text{true}} = (720 / 1200) \times 100 = \mathbf{60.00\%}$.
3. **Bagel Spiral Mixer Friction and Flake-Ice Cooling**
   - **Keystrokes**: `22` {{keycap:D}} `27` {{keycap:R}} `25` {{keycap:F}} `12` {{keycap:M}} {{key:sc78:XEQ}} {{keycap:W}} `24` {{key:sc78:ENTER}} `18` {{key:sc78:×}} `80` {{key:sc78:÷}}
   - **Solution**: Evaluating strike water balance $W = 3D - (R + F + M)$ yields $W = 66.0 - 64.0 = \mathbf{2.0^\circ\text{C}}$. Applying the latent heat ice substitution formula ($W_{\text{ice}} = W_{\text{total}} \times \Delta T / 80$) yields flake-ice requirement $W_{\text{ice}} = 24.0 \times 18.0 / 80 = \mathbf{5.40\text{ kg}}$.
4. **Multi-Flour Rustic Miche with 100% Hydration Levain**
   - **Keystrokes**: `150` {{key:sc78:ENTER}} `205.2` {{key:sc78:÷}} `100` {{key:sc78:×}} `0.25` {{key:sc78:×}} `2` {{key:sc78:÷}}
   - **Solution**: Mixer flour is $F = 150 / 2.052 = \mathbf{73.099\text{ kg}}$, levain is $0.25 \times 73.099 = \mathbf{18.275\text{ kg}}$ ($9.137\text{ kg}$ flour, $9.137\text{ kg}$ water). Total system flour is $82.237\text{ kg}$ and total water is $66.155\text{ kg}$, establishing True Overall Hydration $\text{HYDR}_{\text{true}} = \mathbf{80.44\%}$.
5. **Spiral Mixer Friction Calibration and Shift Compensation**
   - **Keystrokes**: `25.2` {{keycap:D}} `23.5` {{keycap:R}} `21` {{keycap:F}} `14.5` {{keycap:W}} {{key:sc78:XEQ}} {{keycap:M}} `23` {{keycap:D}} `26` {{keycap:R}} `23` {{keycap:F}} {{key:sc78:XEQ}} {{keycap:W}}
   - **Solution**: Calibrates machine friction factor $M = 3(25.2) - (23.5 + 21.0 + 14.5) = 75.6 - 59.0 = \mathbf{16.60^\circ\text{C}}$. For the afternoon batch, required strike water temperature drops to $W = 3(23.0) - (26.0 + 23.0 + 16.6) = 69.0 - 65.6 = \mathbf{3.40^\circ\text{C}}$.

### Chapter 20: Hitting Original Gravity and Bitterness in the Brewhouse Kettle

1. **Imperial Stout Mash Strike and Final Gravity Target**
   - **Keystrokes**: `68` {{key:sc78:ENTER}} `17.5` {{key:sc78:MSH}} `22` {{key:sc78:▸SG}} `9.166` {{keycap:A}} `1.0918` {{keycap:O}} {{key:sc78:XEQ}} {{keycap:F}}
   - **Solution**: Strike water temperature is $S = (0.4/2.5)(68 - 17.5) + 68 = \mathbf{74.73^\circ\text{C}}$. Wort converts to Original Gravity $O = \mathbf{1.0918}$. In the ABV Workspace ($A = (O - F) \times 131.25$), target Final Gravity resolves to $F = 1.0918 - (9.166 / 131.25) = \mathbf{1.0220}$.
2. **Pilot Batch Centennial Hop Bitterness and Morey Color**
   - **Keystrokes**: `1.75` {{key:sc78:ENTER}} `10.5` {{key:sc78:IBU}} `90` {{key:sc78:ENTER}} `5` {{key:sc78:SRM}}
   - **Solution**: Calculates hop bitterness $I = (1.75 \times 0.105 \times 0.25 \times 7490) / 5.0 = \mathbf{68.81\text{ IBU}}$. Computes malt color units $\text{MCU} = 90 / 5 = 18.0$ and evaluates Morey equation $\text{SRM} = 1.4922 \times (18.0)^{0.6859} = \mathbf{10.83\text{ SRM}}$ (deep amber).
3. **Inverse Hop Charge for a 15-Barrel Commercial IPA**
   - **Keystrokes**: `55` {{keycap:I}} `465` {{keycap:V}} `0.134` {{keycap:A}} `0.225` {{keycap:U}} {{key:sc78:XEQ}} {{keycap:W}} `28.3495` {{key:sc78:×}}
   - **Solution**: In the IBU Workspace ($I = (W \times A \times U \times 7490) / V$), solving for hop mass yields $W = \mathbf{113.07\text{ oz}} = \mathbf{3{,}205.3\text{ g}}$ ($3.21\text{ kg}$).
4. **Real Extract and Real Degree of Fermentation in a Belgian Tripel**
   - **Keystrokes**: `1.082` {{key:sc78:ENTER}} `1.010` {{key:sc78:-}} `0.082` {{key:sc78:÷}} `100` {{key:sc78:×}} `1.082` {{key:sc78:ENTER}} `1.010` {{key:sc78:ABV}} `0.1808` {{key:sc78:ENTER}} `19.75` {{key:sc78:×}} `0.8192` {{key:sc78:ENTER}} `2.56` {{key:sc78:×}} {{key:sc78:+}} `19.75` {{key:sc78:ENTER}} `5.668` {{key:sc78:-}} `19.75` {{key:sc78:÷}} `100` {{key:sc78:×}}
   - **Solution**: Apparent Attenuation is $(0.082 - 0.010) / 0.082 = \mathbf{87.80\%}$ and alcohol strength is $\mathbf{9.45\%\text{ ABV}}$. Real Extract is $E_r = 0.1808(19.75) + 0.8192(2.56) = \mathbf{5.668^\circ\text{P}}$, establishing Real Degree of Fermentation $\text{RDF} = (19.75 - 5.668)/19.75 = \mathbf{71.30\%}$.
5. **Mash Tun Thermal Mass Compensation in an Unheated Vessel**
   - **Keystrokes**: `67` {{key:sc78:ENTER}} `15` {{key:sc78:MSH}} `80` {{key:sc78:ENTER}} `0.12` {{key:sc78:×}} `50` {{key:sc78:ENTER}} `0.4` {{key:sc78:×}} {{key:sc78:+}} `150` {{key:sc78:÷}} `67` {{key:sc78:ENTER}} `15` {{key:sc78:-}} {{key:sc78:×}} `67` {{key:sc78:+}}
   - **Solution**: Simple strike formula yields $S_{\text{simple}} = \mathbf{73.93^\circ\text{C}}$. Combining grain thermal mass ($20.0\text{ kcal/}^\circ\text{C}$) and steel vessel thermal mass ($9.6\text{ kcal/}^\circ\text{C}$) requires true strike temperature $S_{\text{tun}} = \mathbf{77.26^\circ\text{C}}$—a $+3.33^\circ\text{C}$ compensation.

### Chapter 21: Trimming the Tenderloin and Pricing the Tasting Menu

1. **Two-Stage Atlantic Halibut Fabrication and Portion Cost**
   - **Keystrokes**: `19.25` {{key:sc78:ENTER}} `35` {{key:sc78:÷}} `100` {{key:sc78:×}} `14.3` {{key:sc78:ENTER}} `0.55` {{key:sc78:÷}} `0.375` {{key:sc78:×}}
   - **Solution**: Yield percentage is $19.25 / 35.0 = \mathbf{55.00\%}$. Edible Portion cost is $C_{\text{EP}} = 14.30 / 0.55 = \mathbf{\$26.00/\text{lb}}$. A $6.0\text{-oz}$ portion costs $0.375 \times \$26.00 = \mathbf{\$9.75}$.
2. **Hyperbolic Margin versus Markup Audit**
   - **Keystrokes**: `3.15` {{key:sc78:ENTER}} `14` {{key:sc78:CST}} `14` {{key:sc78:ENTER}} `3.15` {{key:sc78:-}} `3.15` {{key:sc78:÷}} `100` {{key:sc78:×}}
   - **Solution**: Food cost percentage is $3.15 / 14.00 = \mathbf{22.50\%}$ and gross margin is $100 - 22.50 = \mathbf{77.50\%}$. Markup on cost is $(14.00 - 3.15)/3.15 = \mathbf{344.44\%}$.
3. **Barrique Sulfite Addition and Water Activity**
   - **Keystrokes**: `225` {{key:sc78:ENTER}} `35` {{key:sc78:×}} `576` {{key:sc78:÷}} `88.5` {{key:sc78:ENTER}} `100` {{key:sc78:÷}}
   - **Solution**: Evaluates sulfite addition $m_{\text{KMBS}} = (225 \times 35) / (1000 \times 0.576) = \mathbf{13.67\text{ g}}$ of KMBS. Water activity is $a_w = 88.5 / 100 = \mathbf{0.885}$ (safely below the $0.910$ pathogenic bacterial threshold).
4. **Three-Stage Pork Belly Porchetta Breakdown and Costing**
   - **Keystrokes**: `15.3` {{key:sc78:ENTER}} `18.5` {{key:sc78:÷}} `100` {{key:sc78:×}} `13.5` {{key:sc78:ENTER}} `15.3` {{key:sc78:÷}} `100` {{key:sc78:×}} `77.70` {{key:sc78:ENTER}} `18` {{key:sc78:÷}}
   - **Solution**: Raw fabrication yield is $15.3 / 18.5 = \mathbf{82.70\%}$ and cooking yield is $13.5 / 15.3 = \mathbf{88.24\%}$ (cumulative yield $72.97\%$). Dividing entire wholesale cost by 18 portions yields banquet plate cost $C_{\text{portion}} = 77.70 / 18 = \mathbf{\$4.32}$.
5. **Molecular SO2 pH Compensation Across Cellar Tank Lots**
   - **Keystrokes**: `0.8` {{key:sc78:ENTER}} `1` {{key:sc78:ENTER}} `10` {{key:sc78:ENTER}} `3.3` {{key:sc78:ENTER}} `1.81` {{key:sc78:-}} {{key:sc78:yˣ}} {{key:sc78:+}} {{key:sc78:×}} `0.8` {{key:sc78:ENTER}} `1` {{key:sc78:ENTER}} `10` {{key:sc78:ENTER}} `3.8` {{key:sc78:ENTER}} `1.81` {{key:sc78:-}} {{key:sc78:yˣ}} {{key:sc78:+}} {{key:sc78:×}}
   - **Solution**: Free $\text{SO}_2$ required is $[\text{Free}] = [\text{Mol}] \times (1 + 10^{\text{pH} - 1.81})$. For Lot A ($\text{pH } 3.30$), $[\text{Free}] = 0.8(1 + 30.90) = \mathbf{25.52\text{ mg/L}}$. For Lot B ($\text{pH } 3.80$), $[\text{Free}] = 0.8(1 + 97.72) = \mathbf{78.98\text{ mg/L}}$—requiring more than three times the sulfite dose.

## Unit VIII (SC-80): Clinical Pharmacy, Pharmacokinetics & Critical Care

### Chapter 22: Sizing the Dose to the Patient Profile

1. **Obese Male Dosing Weight Partitioning**
   - **Keystrokes**: `178` {{key:sc80:IBW}} `125` {{key:sc80:ENTER}} `72.6` {{key:sc80:-}} `0.4` {{key:sc80:×}} `72.6` {{key:sc80:+}}
   - **Solution**: Ideal Body Weight evaluates to $IBW = 50.0 + 2.3(70.08 - 60) = \mathbf{72.58\text{ kg}}$. Adjusted Dosing Weight evaluates to $ABW_{0.40} = 72.58 + 0.40(125.0 - 72.58) = \mathbf{93.55\text{ kg}}$.
2. **Geriatric Sarcopenia Creatinine Clearance Audit**
   - **Keystrokes**: `84` {{key:sc80:ENTER}} `44.5` {{key:sc80:ENTER}} `0.48` {{key:sc80:GFR}} `84` {{key:sc80:ENTER}} `44.5` {{key:sc80:ENTER}} `0.80` {{key:sc80:GFR}}
   - **Solution**: Unadjusted clearance falsely overestimates kidney filtration at $CrCl = \mathbf{44.20\text{ mL/min}}$. Applying the clinical sarcopenia floor $S_{cr} = 0.80\text{ mg/dL}$ reveals true, compromised renal clearance of $CrCl = \mathbf{26.52\text{ mL/min}}$.
3. **Pediatric Dehydration 4-2-1 Maintenance Fluid Rate**
   - **Keystrokes**: `16.5` {{key:sc80:421}}
   - **Solution**: Applies Holliday–Segar rule ($10 \times 4 = 40\text{ mL/hr}$, plus $6.5 \times 2 = 13\text{ mL/hr}$) to yield hourly maintenance infusion rate $Q = \mathbf{53.00\text{ mL/hr}}$ ($1{,}272\text{ mL/day}$).
4. **Oncology Body Surface Area Inversion in the Solver**
   - **Keystrokes**: `1.85` {{keycap:B}} `168` {{keycap:H}} {{key:sc80:XEQ}} {{keycap:W}}
   - **Solution**: In the BSA Solver Workspace, inverting Mosteller's formula yields weight $W = (BSA^2 \times 3600) / H = (1.850^2 \times 3600) / 168 = \mathbf{73.34\text{ kg}}$.
5. **Amputee Ideal Body Weight Adjustment**
   - **Keystrokes**: `75` {{key:sc80:ENTER}} `1` {{key:sc80:ENTER}} `0.059` {{key:sc80:-}} `0.007` {{key:sc80:-}} {{key:sc80:×}}
   - **Solution**: Total anatomical amputation loss is $5.9\% + 0.7\% = 6.6\%$. Corrected baseline weight is $IBW_{\text{amputee}} = 75.0 \times (1 - 0.066) = \mathbf{70.05\text{ kg}}$.

### Chapter 23: Titrating Vasoactive Infusions at the Bedside

1. **Dopamine Renal and Inotropic Titration**
   - **Keystrokes**: `5` {{key:sc80:ENTER}} `70` {{key:sc80:×}} `60` {{key:sc80:×}} `1600` {{key:sc80:÷}}
   - **Solution**: Mass delivery rate is $\dot{m} = 5.0 \times 70 \times 60 = \mathbf{21{,}000\ \mu\text{g/hr}}$ ($21.0\text{ mg/hr}$). Dividing by concentration $1{,}600\ \mu\text{g/mL}$ yields volumetric pump rate $Q = \mathbf{13.125\text{ mL/hr}}$.
2. **Pediatric Epinephrine Gravity Micro-Drip Rate**
   - **Keystrokes**: `0.05` {{key:sc80:ENTER}} `15` {{key:sc80:×}} `60` {{key:sc80:×}} `10` {{key:sc80:÷}} `60` {{key:sc80:×}} `60` {{key:sc80:÷}}
   - **Solution**: Hourly volumetric rate is $Q = (0.050 \times 15 \times 60) / 10 = \mathbf{4.50\text{ mL/hr}}$. With a $60\text{-gtt/mL}$ administration set, frequency is $N = (4.50 \times 60) / 60 = \mathbf{4.50\text{ gtt/min}}$ (one drop every $13.3\text{ seconds}$).
3. **Severe Scald Parkland Burn Resuscitation**
   - **Keystrokes**: `4` {{key:sc80:ENTER}} `65` {{key:sc80:×}} `27` {{key:sc80:×}} `2` {{key:sc80:÷}} `8` {{key:sc80:÷}} `2` {{key:sc80:÷}}
   - **Solution**: Total 24-hour resuscitation volume is $V_{24} = 4 \times 65 \times 27 = \mathbf{7{,}020\text{ mL}}$. First 8 hours delivers half ($3{,}510\text{ mL}$) at $Q_1 = \mathbf{438.75\text{ mL/hr}}$; remaining 16 hours delivers $3{,}510\text{ mL}$ at $Q_2 = \mathbf{219.38\text{ mL/hr}}$.
4. **Mean Arterial Pressure and Vasopressor Titration**
   - **Keystrokes**: `72` {{key:sc80:ENTER}} `45` {{key:sc80:MAP}} `118` {{key:sc80:ENTER}} `74` {{key:sc80:MAP}} {{key:sc80:-}}
   - **Solution**: Initial arterial pressure is $\text{MAP} = (72 + 2 \times 45) / 3 = \mathbf{54.00\text{ mmHg}}$ (severe hypoperfusion). Resuscitated pressure reaches $\text{MAP} = (118 + 2 \times 74) / 3 = \mathbf{88.67\text{ mmHg}}$, delivering net perfusion gain $\Delta\text{MAP} = \mathbf{+34.67\text{ mmHg}}$.
5. **Back-Calculating Inherited Infusion Rate on the Stack**
   - **Keystrokes**: `18` {{key:sc80:ENTER}} `200` {{key:sc80:×}} `60` {{key:sc80:÷}} `80` {{key:sc80:÷}}
   - **Solution**: Volumetric rate delivers mass rate $\dot{m} = 18.0 \times 200 = 3{,}600\ \mu\text{g/hr} = 60.0\ \mu\text{g/min}$. Dividing by patient weight yields normalized dose rate $R = 60.0 / 80.0 = \mathbf{0.375\ \mu\text{g/kg/min}}$.

### Chapter 24: Tracking the Trough Across Five Half-Lives

1. **Gentamicin Elimination Half-Life and Supratherapeutic Hold Time**
   - **Keystrokes**: `18` {{key:sc80:ENTER}} `4.5` {{key:sc80:÷}} {{key:sc80:LN}} `8.3` {{key:sc80:÷}} `0.69315` {{key:sc80:x⇄y}} {{key:sc80:÷}} `4.5` {{key:sc80:ENTER}} `1` {{key:sc80:÷}} {{key:sc80:LN}} `0.1670` {{key:sc80:÷}}
   - **Solution**: Elimination rate is $K = \ln(18/4.5) / 8.30 = \mathbf{0.1667\text{ hr}^{-1}}$, yielding half-life $T_{1/2} = \ln(2) / K = \mathbf{4.159\text{ hr}}$. Waiting for trough $1.0\text{ mg/L}$ requires hold time $T_{\text{hold}} = \ln(4.5/1.0)/0.1667 = \mathbf{9.02\text{ hr}}$.
2. **Diabetic Ketoacidosis Anion Gap and Hyperglycemic Sodium**
   - **Keystrokes**: `128` {{key:sc80:ENTER}} `92` {{key:sc80:-}} `8` {{key:sc80:-}} `4` {{key:sc80:ENTER}} `2` {{key:sc80:-}} `2.5` {{key:sc80:×}} {{key:sc80:+}} `680` {{key:sc80:ENTER}} `100` {{key:sc80:-}} `100` {{key:sc80:÷}} `1.6` {{key:sc80:×}} `128` {{key:sc80:+}}
   - **Solution**: Raw Anion Gap is $128 - (92 + 8) = \mathbf{28.00\text{ mEq/L}}$. Correcting for hypoalbuminemia ($+2.5\text{ mEq/L}$ per $\text{g/dL}$ deficit) yields true gap $\text{AG}_{\text{corr}} = 28 + 2.5(2) = \mathbf{33.00\text{ mEq/L}}$. Corrected sodium is $[\text{Na}^+]_{\text{corr}} = 128 + 1.6(5.8) = \mathbf{137.28\text{ mEq/L}}$.
3. **Severe ARDS Oxygenation Ratio and Transport Cylinder Reserve**
   - **Keystrokes**: `136` {{key:sc80:ENTER}} `0.8` {{key:sc80:÷}} `713` {{key:sc80:ENTER}} `0.8` {{key:sc80:×}} `48` {{key:sc80:ENTER}} `0.8` {{key:sc80:÷}} {{key:sc80:-}} `136` {{key:sc80:-}} `1400` {{key:sc80:ENTER}} `200` {{key:sc80:-}} `0.28` {{key:sc80:×}} `10` {{key:sc80:÷}}
   - **Solution**: Oxygenation ratio is $P/F = 136 / 0.80 = \mathbf{170.0\text{ mmHg}}$ (moderate-to-severe ARDS). Alveolar oxygen is $P_A\text{O}_2 = 0.80(713) - 48/0.8 = 510.4\text{ mmHg}$, giving massive gradient $\Delta P_{A-a}\text{O}_2 = 510.4 - 136 = \mathbf{374.4\text{ mmHg}}$. Transport cylinder provides $T = (1200 \times 0.28) / 10 = \mathbf{33.6\text{ min}}$.
4. **Multiple-Dose Steady-State Drug Accumulation**
   - **Keystrokes**: `0.08664` {{key:sc80:ENTER}} `8` {{key:sc80:×}} {{key:sc80:+/-}} {{key:sc80:𝑒ˣ}} `1` {{key:sc80:ENTER}} `0.5` {{key:sc80:-}} `1` {{key:sc80:x⇄y}} {{key:sc80:÷}} `1` {{key:sc80:ENTER}} `0.5` {{key:sc80:÷}}
   - **Solution**: Across one dosing interval, fraction remaining is $e^{-K\tau} = \mathbf{0.5000}$. Accumulation index is $R_{\text{acc}} = 1 / (1 - 0.5) = \mathbf{2.0000}$, establishing that steady-state peak and trough concentrations are exactly twice their first-dose values.
5. **Bazett versus Fridericia QTc Audit and Pseudohypocalcemia**
   - **Keystrokes**: `0.44` {{key:sc80:ENTER}} `0.6` {{key:sc80:√x}} {{key:sc80:÷}} `0.44` {{key:sc80:ENTER}} `0.6` {{key:sc80:ENTER}} `3` {{key:sc80:𝑥⁻¹}} {{key:sc80:yˣ}} {{key:sc80:÷}} `7.2` {{key:sc80:ENTER}} `0.8` {{key:sc80:ENTER}} `4` {{key:sc80:ENTER}} `2` {{key:sc80:-}} {{key:sc80:×}} {{key:sc80:+}}
   - **Solution**: Bazett's formula overcorrects at tachycardia to $QTc = \mathbf{568\text{ ms}}$ (alarmingly prolonged), while Fridericia's cube-root formula yields $QTc = \mathbf{522\text{ ms}}$. Corrected calcium is $7.2 + 0.8(4 - 2) = \mathbf{8.80\text{ mg/dL}}$—ruling out true hypocalcemia.

## Unit IX (SC-95): Quantitative Finance, Fixed Income & Metrology

### Chapter 25: Structuring the Equipment Lease and Valuing the Expansion Plant

1. **Commercial Equipment Fleet Lease Payment**
   - **Keystrokes**: `36` {{keycap:N}} `6` {{keycap:I%}} `150000` {{keycap:PV}} `-45000` {{keycap:FV}} {{key:sc95:SOLVE}} {{keycap:PMT}}
   - **Solution**: In the TVM Solver Workspace, solving for payment yields monthly cash outflow $PMT = \mathbf{-\$3{,}360.77}$.
2. **Effective Annual Rate Compounding Comparison**
   - **Keystrokes**: `1` {{key:sc95:ENTER}} `0.08` {{key:sc95:ENTER}} `4` {{key:sc95:÷}} {{key:sc95:+}} `4` {{key:sc95:yˣ}} `1` {{key:sc95:-}} `100` {{key:sc95:×}} `0.08` {{key:sc95:𝑒ˣ}} `1` {{key:sc95:-}} `100` {{key:sc95:×}}
   - **Solution**: Quarterly compounding yields $\text{EAR} = (1 + 0.08/4)^4 - 1 = \mathbf{8.243\%}$. Continuous compounding yields $\text{EAR} = e^{0.08} - 1 = \mathbf{8.329\%}$.
3. **Uneven Cash Flow Net Present Value**
   - **Keystrokes**: `80000` {{key:sc95:+/-}} `25000` {{key:sc95:ENTER}} `1.08` {{key:sc95:÷}} `35000` {{key:sc95:ENTER}} `1.08` {{key:sc95:ENTER}} `2` {{key:sc95:yˣ}} {{key:sc95:÷}} {{key:sc95:+}} `30000` {{key:sc95:ENTER}} `1.08` {{key:sc95:ENTER}} `3` {{key:sc95:yˣ}} {{key:sc95:÷}} {{key:sc95:+}} `15000` {{key:sc95:ENTER}} `1.08` {{key:sc95:ENTER}} `4` {{key:sc95:yˣ}} {{key:sc95:÷}} {{key:sc95:+}} {{key:sc95:+}}
   - **Solution**: Discounted cash inflows sum to $\$84{,}889.37$, yielding positive Net Present Value $NPV = 84{,}889.37 - 80{,}000 = \mathbf{+\$4{,}889.37}$ (approving capital investment).
4. **Target Gross Margin Pricing**
   - **Keystrokes**: `145` {{key:sc95:ENTER}} `1` {{key:sc95:ENTER}} `0.4` {{key:sc95:-}} {{key:sc95:÷}} `145` {{key:sc95:-}} `145` {{key:sc95:÷}} `100` {{key:sc95:×}}
   - **Solution**: Selling price is $P = 145.00 / (1 - 0.40) = \mathbf{\$241.67}$. Markup on cost is $(241.67 - 145.00) / 145.00 = \mathbf{66.67\%}$.
5. **Economic Order Quantity and Carrying Cost Optimization**
   - **Keystrokes**: `2` {{key:sc95:ENTER}} `24000` {{key:sc95:×}} `75` {{key:sc95:×}} `1.5` {{key:sc95:÷}} {{key:sc95:√x}} `24000` {{key:sc95:ENTER}} `1549.19` {{key:sc95:÷}} `75` {{key:sc95:×}} `1549.19` {{key:sc95:ENTER}} `2` {{key:sc95:÷}} `1.5` {{key:sc95:×}} {{key:sc95:+}}
   - **Solution**: Calculates optimal order size $EOQ = \sqrt{(2 \times 24{,}000 \times 75) / 1.5} = \mathbf{1{,}549.19\text{ units}}$ ($1{,}549\text{ fittings}$). Annual ordering and holding costs are balanced at $\$1{,}161.89$ each, giving total annual cost $\mathbf{\$2{,}323.79}$.

### Chapter 26: Hedging the Semiannual Corporate Bond Against a Rate Spike

1. **Discount Bond Valuation and Yield Pricing**
   - **Keystrokes**: `1` {{key:sc95:ENTER}} `1.03` {{key:sc95:ENTER}} `10` {{key:sc95:+/-}} {{key:sc95:yˣ}} {{key:sc95:-}} `0.03` {{key:sc95:÷}} `20` {{key:sc95:×}} `1000` {{key:sc95:ENTER}} `1.03` {{key:sc95:ENTER}} `10` {{key:sc95:+/-}} {{key:sc95:yˣ}} {{key:sc95:×}} {{key:sc95:+}}
   - **Solution**: Annuity value of coupons is $\$170.60$ and discounted par value is $\$744.09$, yielding total discount price $P = \mathbf{\$914.70}$.
2. **Zero-Coupon Bond Modified Duration**
   - **Keystrokes**: `10` {{key:sc95:ENTER}} `1.0225` {{key:sc95:÷}}
   - **Solution**: Macaulay duration is $10.00\text{ years}$. Modified duration is $D_{\text{mod}} = 10.00 / (1 + 0.0225) = \mathbf{9.7800\text{ years}}$ (a $100\text{ bps}$ rate increase causes a $9.78\%$ price drop).
3. **Black–Scholes In-the-Money Call Option Pricing**
   - **Keystrokes**: `55` {{key:sc95:ENTER}} `0.8926` {{key:sc95:×}} `50` {{key:sc95:ENTER}} `0.05` {{key:sc95:ENTER}} `0.25` {{key:sc95:×}} {{key:sc95:+/-}} {{key:sc95:𝑒ˣ}} {{key:sc95:×}} `0.8729` {{key:sc95:×}} {{key:sc95:-}}
   - **Solution**: Black–Scholes formula evaluates $C = S \cdot N(d_1) - K e^{-rT} N(d_2) = 55(0.8926) - 50(0.9876)(0.8729) = 49.09 - 43.11 = \mathbf{\$5.83}$.
4. **Protective Collar Synthetic Put Valuation via Put-Call Parity**
   - **Keystrokes**: `5.83` {{key:sc95:ENTER}} `55` {{key:sc95:-}} `49.38` {{key:sc95:+}}
   - **Solution**: Put–Call Parity yields put price $P = 5.83 - 55.00 + 49.38 = \mathbf{\$0.21}$.
5. **Two-Asset Portfolio Variance and Volatility Diversification**
   - **Keystrokes**: `0.5` {{key:sc95:ENTER}} `0.15` {{key:sc95:×}} `2` {{key:sc95:yˣ}} `0.5` {{key:sc95:ENTER}} `0.25` {{key:sc95:×}} `2` {{key:sc95:yˣ}} {{key:sc95:+}} `2` {{key:sc95:ENTER}} `0.5` {{key:sc95:×}} `0.5` {{key:sc95:×}} `0.15` {{key:sc95:×}} `0.25` {{key:sc95:×}} `0.2` {{key:sc95:×}} {{key:sc95:+}} {{key:sc95:√x}} `100` {{key:sc95:×}}
   - **Solution**: Portfolio variance is $\sigma_p^2 = 0.005625 + 0.015625 + 0.003750 = 0.02500$, yielding standard deviation $\sigma_p = \mathbf{15.81\%}$ (substantially lower than the weighted arithmetic average of $20.0\%$).

### Chapter 27: Catching the Drifting Grinding Spindle Before Scrap Happens

1. **Bivariate Tool Wear Slope and Linear Correlation**
   - **Keystrokes**: `1` {{key:sc95:ENTER}} `12.00` {{key:sc95:Σ+}} `2` {{key:sc95:ENTER}} `12.05` {{key:sc95:Σ+}} `3` {{key:sc95:ENTER}} `12.09` {{key:sc95:Σ+}} `4` {{key:sc95:ENTER}} `12.14` {{key:sc95:Σ+}} `5` {{key:sc95:ENTER}} `12.20` {{key:sc95:Σ+}} {{key:sc95:L.R.}}
   - **Solution**: Linear regression parameters yield slope $\beta_1 = \mathbf{0.04900\text{ mm/pass}}$, intercept $\beta_0 = \mathbf{11.94900\text{ mm}}$, and correlation $r = \mathbf{0.99965}$.
2. **Centered Six Sigma Process Capability Index**
   - **Keystrokes**: `50.15` {{key:sc95:ENTER}} `49.85` {{key:sc95:-}} `6` {{key:sc95:ENTER}} `0.025` {{key:sc95:×}} {{key:sc95:÷}}
   - **Solution**: Evaluates capability index $C_p = (\text{USL} - \text{LSL}) / (6\sigma) = 0.30 / 0.15 = \mathbf{2.0000}$ (world-class Six Sigma capability).
3. **Off-Center Process Capability Penalty**
   - **Keystrokes**: `50.15` {{key:sc95:ENTER}} `50.04` {{key:sc95:-}} `3` {{key:sc95:ENTER}} `0.025` {{key:sc95:×}} {{key:sc95:÷}} `50.04` {{key:sc95:ENTER}} `49.85` {{key:sc95:-}} `3` {{key:sc95:ENTER}} `0.025` {{key:sc95:×}} {{key:sc95:÷}}
   - **Solution**: Upper capability is $CPU = (50.15 - 50.04)/(3 \times 0.025) = \mathbf{1.4667}$ and lower capability is $CPL = (50.04 - 49.85)/(3 \times 0.025) = \mathbf{2.5333}$, establishing actual capability $C_{pk} = \min(CPU, CPL) = \mathbf{1.4667}$.
4. **Metrology Sample Size Determination for Prescribed Tolerance**
   - **Keystrokes**: `2.576` {{key:sc95:ENTER}} `0.004` {{key:sc95:×}} `0.001` {{key:sc95:÷}} {{key:sc95:x²}}
   - **Solution**: Calculates sample size $N = (Z \times \sigma / E)^2 = (2.576 \times 0.004 / 0.001)^2 = 10.304^2 = \mathbf{106.17} \implies \mathbf{107\text{ parts}}$.
5. **Gaussian Tail Defect Rate and DPMO Projection**
   - **Keystrokes**: `3.5` {{key:sc95:pN}} `1` {{key:sc95:x⇄y}} {{key:sc95:-}} `1000000` {{key:sc95:×}}
   - **Solution**: Cumulative normal probability is $N(3.50) = \mathbf{0.999767}$. Upper tail defect probability is $p = 1 - 0.999767 = \mathbf{0.0002326}$ ($0.0233\%$), projecting $\text{DPMO} = \mathbf{232.6\text{ DPMO}}$.
