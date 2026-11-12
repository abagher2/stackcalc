---
title: "StackCalc Learning Lab | 2D Virtual Manipulatives & Stack Computing"
description: "Interactive 2D virtual manipulatives lab for schools: Fraction Towers (FRAC-01) and Place-Value Decimal Trays (PLACE-01). Build quantities with tactile blocks, push values onto the 4-line RPN stack, execute operations, and verify mathematical equivalence."
---

# StackCalc Learning Lab

The Learning Lab bridges Jerome Bruner’s **Concrete-Representational-Abstract (CRA)** framework with the mechanical clarity of **Reverse Polish Notation (RPN)**:
1. **Concrete:** Physical 3D-printed Gridfinity math manipulatives on classroom desks.
2. **Representational (2D Interactive Lab Below):** Virtual proportional blocks and place-value trays for interactive whiteboards and 1:1 Chromebooks.
3. **Abstract:** Dedicated 4-line operational stack registers on the **SC-6 Elementary** and **SC-32 Scientific** handheld calculators.

---

<!-- ==========================================================================
     STACKCALC 2D VIRTUAL MANIPULATIVES LAB (CLASSROOM SIMULATOR)
     ========================================================================== -->
<div class="vlab-wrapper">
  <div id="vlab-main-container" class="vlab-container">
    
    <!-- Top Telemetry & Control Bar -->
    <div class="vlab-header">
      <div class="vlab-title-group">
        <span class="vlab-sku-badge">CRA DIGITAL TWIN // 2D LAB</span>
        <h2 class="vlab-title">Virtual Manipulatives &amp; Stack Computing Lab</h2>
      </div>
      <div class="vlab-controls">
        <button id="vlab-btn-sound" class="vlab-btn-icon" title="Toggle Sound">🔊 AUDIO: ON</button>
        <button id="vlab-btn-fullscreen" class="vlab-btn-icon active" title="Fullscreen Projector Mode">⛶ FULLSCREEN PROJECTOR</button>
      </div>
    </div>

    <!-- Mode Selector Tabs -->
    <div class="vlab-nav-tabs">
      <button id="vlab-tab-fractions" class="vlab-nav-tab active">📐 Fraction Towers (FRAC-01)</button>
      <button id="vlab-tab-placevalue" class="vlab-nav-tab">🔢 Place Value Trays (PLACE-01)</button>
      <button id="vlab-tab-primes" class="vlab-nav-tab">🔬 Prime Factor Studio (PRIME-01)</button>
    </div>

    <!-- VIEW 1: FRACTION STUDIO -->
    <div id="vlab-view-fractions">
      <div class="vlab-grid">
        
        <!-- Left: Fraction Rack / Palette -->
        <div class="vlab-panel">
          <div class="vlab-panel-header">
            <span>Fraction Palette</span>
            <span>84mm Ref</span>
          </div>
          <div id="vlab-frac-rack" class="vlab-rack-list">
            <div class="vlab-block-btn" onclick="window.StackCalcLab.addFraction({label:'1/1',n:1,d:1,mm:84.0,cls:'frac-1-1'})">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#334155;"></span><span class="vlab-block-label">1/1</span></div>
              <span class="vlab-block-spec">84.0 mm</span>
            </div>
            <div class="vlab-block-btn" onclick="window.StackCalcLab.addFraction({label:'1/2',n:1,d:2,mm:42.0,cls:'frac-1-2'})">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#0284C7;"></span><span class="vlab-block-label">1/2</span></div>
              <span class="vlab-block-spec">42.0 mm</span>
            </div>
            <div class="vlab-block-btn" onclick="window.StackCalcLab.addFraction({label:'1/3',n:1,d:3,mm:28.0,cls:'frac-1-3'})">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#059669;"></span><span class="vlab-block-label">1/3</span></div>
              <span class="vlab-block-spec">28.0 mm</span>
            </div>
            <div class="vlab-block-btn" onclick="window.StackCalcLab.addFraction({label:'1/4',n:1,d:4,mm:21.0,cls:'frac-1-4'})">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#D97706;"></span><span class="vlab-block-label">1/4</span></div>
              <span class="vlab-block-spec">21.0 mm</span>
            </div>
            <div class="vlab-block-btn" onclick="window.StackCalcLab.addFraction({label:'1/5',n:1,d:5,mm:16.8,cls:'frac-1-5'})">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#7C3AED;"></span><span class="vlab-block-label">1/5</span></div>
              <span class="vlab-block-spec">16.8 mm</span>
            </div>
            <div class="vlab-block-btn" onclick="window.StackCalcLab.addFraction({label:'1/6',n:1,d:6,mm:14.0,cls:'frac-1-6'})">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#E11D48;"></span><span class="vlab-block-label">1/6</span></div>
              <span class="vlab-block-spec">14.0 mm</span>
            </div>
            <div class="vlab-block-btn" onclick="window.StackCalcLab.addFraction({label:'1/8',n:1,d:8,mm:10.5,cls:'frac-1-8'})">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#0891B2;"></span><span class="vlab-block-label">1/8</span></div>
              <span class="vlab-block-spec">10.5 mm</span>
            </div>
            <div class="vlab-block-btn" onclick="window.StackCalcLab.addFraction({label:'1/10',n:1,d:10,mm:8.4,cls:'frac-1-10'})">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#0D9488;"></span><span class="vlab-block-label">1/10</span></div>
              <span class="vlab-block-spec">8.4 mm</span>
            </div>
            <div class="vlab-block-btn" onclick="window.StackCalcLab.addFraction({label:'1/12',n:1,d:12,mm:7.0,cls:'frac-1-12'})">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#4F46E5;"></span><span class="vlab-block-label">1/12</span></div>
              <span class="vlab-block-spec">7.0 mm</span>
            </div>
          </div>
          <div style="margin-top: 1rem; font-size: 0.68rem; color: #64748B; font-family: 'Space Mono', monospace;">
            Tap blocks above to construct numbers in the Staging Column.
          </div>
        </div>

        <!-- Center: Staging Bay & Comparison Stage -->
        <div class="vlab-stage-container">
          <div class="vlab-comparator-bay">
            <div id="vlab-laser-line" class="vlab-laser-line"></div>
            <div class="vlab-columns-wrapper">
              
              <!-- Column 1: Staging Builder -->
              <div>
                <div id="vlab-col-stage" class="vlab-column"></div>
                <div class="vlab-column-title">1. STAGING TOWER</div>
              </div>

              <!-- Column 2: Live Calculator Result (Register X) -->
              <div>
                <div id="vlab-col-stack-x" class="vlab-column"></div>
                <div class="vlab-column-title" style="color:#38BDF8;">2. STACK (REG X)</div>
              </div>

              <!-- Column 3: Verification Target -->
              <div>
                <div id="vlab-col-target" class="vlab-column vlab-column-target"></div>
                <div class="vlab-column-title" style="color:#10B981;">3. VERIFICATION TARGET</div>
              </div>

            </div>
          </div>

          <!-- Staging Action Toolbar -->
          <div class="vlab-staging-bar">
            <div class="vlab-staged-readout">
              <span class="vlab-staged-meta">STAGED NUMBER VALUE:</span>
              <span id="vlab-staged-val" class="vlab-staged-val">0</span>
              <span id="vlab-staged-meta" class="vlab-staged-meta">Height: 0.0 mm • Val: 0.000</span>
            </div>
            <div style="display:flex; flex-wrap:wrap; gap:8px;">
              <button id="vlab-btn-push-frac" class="vlab-btn-push">↵ PUSH TO STACK [ENTER]</button>
              <button id="vlab-btn-drop-frac" class="vlab-btn-secondary">⌫ DROP TOP</button>
              <button id="vlab-btn-clear-frac" class="vlab-btn-secondary">✕ CLEAR</button>
            </div>
          </div>
        </div>

        <!-- Right: 4-Line RPN Stack & Operational Console -->
        <div class="vlab-calc-console">
          <div class="vlab-lcd">
            <div class="vlab-lcd-annunciator">
              <span>STACKCALC // RPN ENGINE</span>
              <span>[↰ FDISP: ON]</span>
            </div>
            <div class="vlab-lcd-register"><span>T:</span> <span id="vlab-reg-t">0.0000</span></div>
            <div class="vlab-lcd-register"><span>Z:</span> <span id="vlab-reg-z">0.0000</span></div>
            <div class="vlab-lcd-register" style="color:#0284C7;"><span>Y:</span> <span id="vlab-reg-y">0.0000</span></div>
            <div class="vlab-lcd-register vlab-lcd-reg-x"><span>X:</span> <span id="vlab-reg-x">0.0000_</span></div>
          </div>

          <!-- Operation Keypad -->
          <div class="vlab-op-grid">
            <button class="vlab-btn-op" data-vlab-op="+">+</button>
            <button class="vlab-btn-op" data-vlab-op="-">&minus;</button>
            <button class="vlab-btn-op" data-vlab-op="×">&times;</button>
            <button class="vlab-btn-op" data-vlab-op="÷">&divide;</button>
          </div>

          <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
            <button id="vlab-btn-swap" class="vlab-btn-func">x⇄y</button>
            <button id="vlab-btn-drop" class="vlab-btn-func">DROP</button>
            <button id="vlab-btn-clx" class="vlab-btn-func">CLx</button>
            <button id="vlab-btn-fdisp" class="vlab-btn-func">FDISP</button>
          </div>

          <!-- Verification Trigger Box -->
          <div style="background:#11141A; border:1px solid rgba(255,255,255,0.08); border-radius:8px; padding:12px;">
            <div style="font-family:'Space Mono',monospace; font-size:0.7rem; color:#94A3B8; margin-bottom:8px; font-weight:700;">
              VERIFICATION ENGINE
            </div>
            <div id="vlab-check-status" style="font-family:'Space Mono',monospace; font-size:0.75rem; color:#94A3B8; margin-bottom:10px;">
              Awaiting calculation...
            </div>
            <div style="display:flex; gap:6px;">
              <button id="vlab-btn-check-frac" class="vlab-btn-verify" style="flex:1;">CHECK EQUIVALENCE</button>
              <button id="vlab-btn-clear-target" class="vlab-btn-secondary">RESET</button>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- VIEW 2: PLACE-VALUE STUDIO -->
    <div id="vlab-view-placevalue" style="display:none;">
      <div class="vlab-grid">
        
        <!-- Left & Center: 12-Column Place Value Desk Tray -->
        <div style="grid-column: span 2;" class="vlab-panel">
          <div class="vlab-panel-header">
            <span>Place Value Desk Tray (Whole Numbers &amp; Decimals)</span>
            <span>Base-10 Regrouping</span>
          </div>

          <div class="pv-tray">
            <!-- Headers -->
            <div class="pv-grid-header">
              <div class="pv-col-header">100<br><span style="font-size:0.55rem; color:#94A3B8;">HUNDREDS</span></div>
              <div class="pv-col-header">10<br><span style="font-size:0.55rem; color:#94A3B8;">TENS</span></div>
              <div class="pv-col-header">1<br><span style="font-size:0.55rem; color:#94A3B8;">ONES</span></div>
              <div class="pv-decimal-sep">&bull;</div>
              <div class="pv-col-header decimal">.1<br><span style="font-size:0.55rem; color:#94A3B8;">TENTHS</span></div>
              <div class="pv-col-header decimal">.01<br><span style="font-size:0.55rem; color:#94A3B8;">HUNDREDTHS</span></div>
              <div class="pv-col-header decimal">.001<br><span style="font-size:0.55rem; color:#94A3B8;">THOUSANDTHS</span></div>
            </div>

            <!-- Block Sockets -->
            <div class="pv-grid-row">
              <div id="pv-socket-100" class="pv-socket"></div>
              <div id="pv-socket-10" class="pv-socket"></div>
              <div id="pv-socket-1" class="pv-socket"></div>
              <div class="pv-decimal-sep">&bull;</div>
              <div id="pv-socket-0.1" class="pv-socket"></div>
              <div id="pv-socket-0.01" class="pv-socket"></div>
              <div id="pv-socket-0.001" class="pv-socket"></div>
            </div>

            <!-- Add/Subtract Steppers -->
            <div class="pv-controls-row">
              <div class="pv-stepper">
                <button class="pv-btn-step" data-pv-col="100" data-pv-delta="1">+</button>
                <button class="pv-btn-step" data-pv-col="100" data-pv-delta="-1">&minus;</button>
              </div>
              <div class="pv-stepper">
                <button class="pv-btn-step" data-pv-col="10" data-pv-delta="1">+</button>
                <button class="pv-btn-step" data-pv-col="10" data-pv-delta="-1">&minus;</button>
              </div>
              <div class="pv-stepper">
                <button class="pv-btn-step" data-pv-col="1" data-pv-delta="1">+</button>
                <button class="pv-btn-step" data-pv-col="1" data-pv-delta="-1">&minus;</button>
              </div>
              <div></div>
              <div class="pv-stepper">
                <button class="pv-btn-step" data-pv-col="0.1" data-pv-delta="1">+</button>
                <button class="pv-btn-step" data-pv-col="0.1" data-pv-delta="-1">&minus;</button>
              </div>
              <div class="pv-stepper">
                <button class="pv-btn-step" data-pv-col="0.01" data-pv-delta="1">+</button>
                <button class="pv-btn-step" data-pv-col="0.01" data-pv-delta="-1">&minus;</button>
              </div>
              <div class="pv-stepper">
                <button class="pv-btn-step" data-pv-col="0.001" data-pv-delta="1">+</button>
                <button class="pv-btn-step" data-pv-col="0.001" data-pv-delta="-1">&minus;</button>
              </div>
            </div>

            <!-- Regroup Alert Note -->
            <div id="pv-regroup-alert" style="display:none; background:rgba(255,68,0,0.15); border:1px solid #FF4400; color:#FF9900; padding:8px 12px; border-radius:6px; font-family:'Space Mono',monospace; font-size:0.75rem;">
            </div>

            <!-- Staging Toolbar for Place Value -->
            <div class="vlab-staging-bar" style="margin-top:1rem;">
              <div class="vlab-staged-readout">
                <span class="vlab-staged-meta">CURRENT NUMBER BUILDER:</span>
                <span id="pv-total-val" class="vlab-staged-val">0.000</span>
              </div>
              <div style="display:flex; flex-wrap:wrap; gap:8px;">
                <button id="pv-btn-regroup" class="vlab-btn-secondary" style="border-color:#F59E0B; color:#F59E0B;">🔄 AUTO-REGROUP (+1)</button>
                <button id="pv-btn-push" class="vlab-btn-push">↵ PUSH TO STACK [ENTER]</button>
              </div>
            </div>

          </div>
        </div>

        <!-- Right Console (Shares the 4-Line RPN Stack) -->
        <div class="vlab-calc-console">
          <div class="vlab-lcd">
            <div class="vlab-lcd-annunciator">
              <span>STACKCALC // PV MODE</span>
              <span>[123 DECIMAL]</span>
            </div>
            <div class="vlab-lcd-register"><span>T:</span> <span>0.0000</span></div>
            <div class="vlab-lcd-register"><span>Z:</span> <span>0.0000</span></div>
            <div class="vlab-lcd-register" style="color:#0284C7;"><span>Y:</span> <span>0.0000</span></div>
            <div class="vlab-lcd-register vlab-lcd-reg-x"><span>X:</span> <span>0.0000_</span></div>
          </div>

          <div class="vlab-op-grid">
            <button class="vlab-btn-op" data-vlab-op="+">+</button>
            <button class="vlab-btn-op" data-vlab-op="-">&minus;</button>
            <button class="vlab-btn-op" data-vlab-op="×">&times;</button>
            <button class="vlab-btn-op" data-vlab-op="÷">&divide;</button>
          </div>

          <div style="font-size:0.75rem; color:#94A3B8; line-height:1.5; font-family:'Space Mono',monospace; background:#11141A; padding:12px; border-radius:6px; border:1px solid rgba(255,255,255,0.08);">
            <strong style="color:#FFFFFF;">CRA Workflow:</strong><br>
            1. Tap [+] to add base-10 chips.<br>
            2. Push 1st number to stack.<br>
            3. Build 2nd number &amp; push.<br>
            4. Press [+] or [&minus;] to calculate.<br>
            5. Observe regrouping / carrying!
          </div>
        </div>

      </div>
    </div>

    <!-- VIEW 3: PRIME FACTOR STUDIO -->
    <div id="vlab-view-primes" style="display:none;">
      <div class="vlab-grid">
        
        <!-- Left: Prime Palette -->
        <div class="vlab-panel">
          <div class="vlab-panel-header">
            <span>Prime Block Palette</span>
            <span>Log(p) Ref</span>
          </div>
          <div class="vlab-rack-list">
            <div class="vlab-block-btn" data-prime-p="2">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#0284C7;"></span><span class="vlab-block-label">[2]</span></div>
              <span class="vlab-block-spec">18.0 mm</span>
            </div>
            <div class="vlab-block-btn" data-prime-p="3">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#10B981;"></span><span class="vlab-block-label">[3]</span></div>
              <span class="vlab-block-spec">28.5 mm</span>
            </div>
            <div class="vlab-block-btn" data-prime-p="5">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#F59E0B;"></span><span class="vlab-block-label">[5]</span></div>
              <span class="vlab-block-spec">41.8 mm</span>
            </div>
            <div class="vlab-block-btn" data-prime-p="7">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#8B5CF6;"></span><span class="vlab-block-label">[7]</span></div>
              <span class="vlab-block-spec">50.7 mm</span>
            </div>
            <div class="vlab-block-btn" data-prime-p="11">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#EC4899;"></span><span class="vlab-block-label">[11]</span></div>
              <span class="vlab-block-spec">62.4 mm</span>
            </div>
            <div class="vlab-block-btn" data-prime-p="13">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#06B6D4;"></span><span class="vlab-block-label">[13]</span></div>
              <span class="vlab-block-spec">66.8 mm</span>
            </div>
            <div class="vlab-block-btn" data-prime-p="17">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#E11D48;"></span><span class="vlab-block-label">[17]</span></div>
              <span class="vlab-block-spec">73.6 mm</span>
            </div>
            <div class="vlab-block-btn" data-prime-p="19">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#F97316;"></span><span class="vlab-block-label">[19]</span></div>
              <span class="vlab-block-spec">76.5 mm</span>
            </div>
            <div class="vlab-block-btn" data-prime-p="23">
              <div style="display:flex; align-items:center;"><span class="vlab-block-chip" style="background:#64748B;"></span><span class="vlab-block-label">[23]</span></div>
              <span class="vlab-block-spec">81.3 mm</span>
            </div>
          </div>
          <div style="margin-top: 1rem; font-size: 0.68rem; color: #64748B; font-family: 'Space Mono', monospace;">
            Lengths scale logarithmically: Log(a) + Log(b) = Log(a×b).
          </div>
        </div>

        <!-- Center: Prime Factor Rails -->
        <div class="vlab-stage-container">
          <div class="prime-rail-container">
            <div>
              <div class="prime-rail-title">
                <span>1. Staged Prime Factor Train (Active Product)</span>
                <span id="vlab-prime-formula" style="color: #38BDF8;">No factors</span>
              </div>
              <div id="vlab-prime-stage" class="prime-rail"></div>
            </div>

            <div>
              <div class="prime-rail-title">
                <span>2. Target / Decomposed Register X Prime Train</span>
                <span style="color: #10B981;">[FACT / GCD / LCM]</span>
              </div>
              <div id="vlab-prime-target" class="prime-rail"></div>
            </div>
          </div>

          <!-- Staging Readout & Actions -->
          <div class="vlab-staging-bar">
            <div class="vlab-staged-readout">
              <span class="vlab-staged-meta">COMPOSITE PRODUCT VALUE:</span>
              <span id="vlab-prime-val" class="vlab-staged-val">0</span>
              <span id="vlab-prime-meta" class="vlab-staged-meta">Logarithmic Length: 0.0 mm • 0 Factors</span>
            </div>
            <div style="display:flex; flex-wrap:wrap; gap:8px;">
              <button id="vlab-btn-push-prime" class="vlab-btn-push">↵ PUSH TO STACK [ENTER]</button>
              <button id="vlab-btn-drop-prime" class="vlab-btn-secondary">⌫ DROP LAST PRIME</button>
              <button id="vlab-btn-clear-prime" class="vlab-btn-secondary">✕ CLEAR</button>
            </div>
          </div>
        </div>

        <!-- Right: 4-Line RPN Stack & Factor Operations -->
        <div class="vlab-calc-console">
          <div class="vlab-lcd">
            <div class="vlab-lcd-annunciator">
              <span>STACKCALC // PRIME MODE</span>
              <span>[PRIME-01]</span>
            </div>
            <div class="vlab-lcd-register"><span>T:</span> <span>0.0000</span></div>
            <div class="vlab-lcd-register"><span>Z:</span> <span>0.0000</span></div>
            <div class="vlab-lcd-register" style="color:#0284C7;"><span>Y:</span> <span>0.0000</span></div>
            <div class="vlab-lcd-register vlab-lcd-reg-x"><span>X:</span> <span>0.0000_</span></div>
          </div>

          <!-- Standard Operations -->
          <div class="vlab-op-grid">
            <button class="vlab-btn-op" data-vlab-op="+">+</button>
            <button class="vlab-btn-op" data-vlab-op="-">&minus;</button>
            <button class="vlab-btn-op" data-vlab-op="×">&times;</button>
            <button class="vlab-btn-op" data-vlab-op="÷">&divide;</button>
          </div>

          <!-- Dedicated Prime & Factor Operations -->
          <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap: 6px;">
            <button id="vlab-btn-fact" class="vlab-btn-func" style="background: rgba(16, 185, 129, 0.2); border-color: #10B981; color: #10B981; font-weight: bold;">FACT</button>
            <button id="vlab-btn-gcd" class="vlab-btn-func" style="background: rgba(56, 189, 248, 0.2); border-color: #38BDF8; color: #38BDF8; font-weight: bold;">GCD</button>
            <button id="vlab-btn-lcm" class="vlab-btn-func" style="background: rgba(245, 158, 11, 0.2); border-color: #F59E0B; color: #F59E0B; font-weight: bold;">LCM</button>
          </div>

          <div style="margin-top: 0.75rem; font-size:0.75rem; color:#94A3B8; line-height:1.5; font-family:'Space Mono',monospace; background:#11141A; padding:12px; border-radius:6px; border:1px solid rgba(255,255,255,0.08);">
            <strong style="color:#FFFFFF;">Prime Operations:</strong><br>
            • <strong>[FACT]:</strong> Decomposes Reg X into prime blocks.<br>
            • <strong>[GCD]:</strong> Greatest Common Divisor of Y and X.<br>
            • <strong>[LCM]:</strong> Least Common Multiple of Y and X.
          </div>
        </div>

      </div>
    </div>

  </div>
</div>

---

## Companion Books & Classroom Literature {: #download-the-prototype-materials }

Pair your interactive lab investigations with StackCalc's official companion books and student workbooks, available in print on **Amazon**:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.25rem; margin: 1.5rem 0 2.5rem 0;">

  <!-- Card 1: From Blocks to the Stack -->
  <div style="background: #11141A; border: 1px solid rgba(255, 153, 0, 0.35); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <span style="font-family: 'Space Mono', monospace; font-size: 0.7rem; color: #FF9900; font-weight: 700; text-transform: uppercase;">GRADES 3–6 &bull; SC-6 ELEMENTARY</span>
      <h3 style="margin: 0.35rem 0; font-size: 1.15rem; color: #FFFFFF;">From Blocks to the Stack</h3>
      <p style="font-size: 0.84rem; color: #94A3B8; margin-bottom: 1.25rem; line-height: 1.5;">
        The student handbook, parent guide, and classroom companion for the SC-6 Elementary calculator. Connects physical 3D-printed math blocks with the 4-level number stack ($X, Y, Z, T$), fraction towers, and skip-counting ladders.
      </p>
    </div>
    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
      <a href="https://link.amazon/B0f5cP0Ur" target="_blank" rel="noopener noreferrer" style="flex: 1; min-width: 120px; text-align: center; padding: 0.55rem 0.5rem; background: #FF9900; color: #111827; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 800; text-decoration: none;">
        AMAZON ($16) ↗
      </a>
      <a href="products/sc6-book.md" style="flex: 1; min-width: 100px; text-align: center; padding: 0.55rem 0.5rem; background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); color: #FFFFFF; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; text-decoration: none;">
        OVERVIEW &rarr;
      </a>
    </div>
  </div>

  <!-- Card 2: Thinking in the Stack -->
  <div style="background: #11141A; border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <span style="font-family: 'Space Mono', monospace; font-size: 0.7rem; color: #38BDF8; font-weight: 700; text-transform: uppercase;">HIGH SCHOOL &bull; SC-32 SCIENTIFIC</span>
      <h3 style="margin: 0.35rem 0; font-size: 1.15rem; color: #FFFFFF;">Thinking in the Stack</h3>
      <p style="font-size: 0.84rem; color: #94A3B8; margin-bottom: 1.25rem; line-height: 1.5;">
        The definitive operational guide to scientific computing and RPN stack dynamics on the SC-32 Scientific calculator. Covers numerical root solvers, complex phasors, Romberg calculus, TVM finance, and vector plotting.
      </p>
    </div>
    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
      <a href="https://link.amazon/B07DqTRR5" target="_blank" rel="noopener noreferrer" style="flex: 1; min-width: 120px; text-align: center; padding: 0.55rem 0.5rem; background: #38BDF8; color: #0F172A; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 800; text-decoration: none;">
        AMAZON ($16) ↗
      </a>
      <a href="products/sc32-calculator/index.md" style="flex: 1; min-width: 100px; text-align: center; padding: 0.55rem 0.5rem; background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); color: #FFFFFF; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; text-decoration: none;">
        SC-32 OVERVIEW &rarr;
      </a>
    </div>
  </div>

  <!-- Card 3: Middle School Workbook -->
  <div style="background: #11141A; border: 1px solid rgba(16, 185, 129, 0.35); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <span style="font-family: 'Space Mono', monospace; font-size: 0.7rem; color: #10B981; font-weight: 700; text-transform: uppercase;">GRADES 6–8 &bull; STUDENT WORKBOOK</span>
      <h3 style="margin: 0.35rem 0; font-size: 1.15rem; color: #FFFFFF;">Middle School Math Lab Workbook</h3>
      <p style="font-size: 0.84rem; color: #94A3B8; margin-bottom: 1.25rem; line-height: 1.5;">
        Hands-on middle school workbook connecting physical math blocks with two-method problem solving. 10 units, 45 textbook sections, 90 daily worksheets, and 900 practice problems.
      </p>
    </div>
    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
      <a href="https://link.amazon/B07bxzYKq" target="_blank" rel="noopener noreferrer" style="flex: 1; min-width: 120px; text-align: center; padding: 0.55rem 0.5rem; background: #10B981; color: #0F172A; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 800; text-decoration: none;">
        AMAZON ($14.99) ↗
      </a>
      <a href="downloads/StackCalc-Book-3-Middle-School-Math-Lab.pdf" download style="flex: 1; min-width: 100px; text-align: center; padding: 0.55rem 0.5rem; background: rgba(16, 185, 129, 0.15); border: 1px solid #10B981; color: #10B981; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; text-decoration: none;">
        WORKBOOK PDF &darr;
      </a>
    </div>
  </div>

  <!-- Card 4: Unified Master Teacher's Guide -->
  <div style="background: #11141A; border: 1px solid rgba(245, 158, 11, 0.35); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <span style="font-family: 'Space Mono', monospace; font-size: 0.7rem; color: #F59E0B; font-weight: 700; text-transform: uppercase;">GRADES K–12 &bull; TEACHER FACILITATOR</span>
      <h3 style="margin: 0.35rem 0; font-size: 1.15rem; color: #FFFFFF;">Teaching with the Stack</h3>
      <p style="font-size: 0.84rem; color: #94A3B8; margin-bottom: 1.25rem; line-height: 1.5;">
        Comprehensive teacher facilitation guide: concept-first stack pedagogy, 30-second misconception diagnostics, verbal cues, station rotation schedules, and pacing guides.
      </p>
    </div>
    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
      <a href="https://link.amazon/B05RFHqeu" target="_blank" rel="noopener noreferrer" style="flex: 1; min-width: 120px; text-align: center; padding: 0.55rem 0.5rem; background: #F59E0B; color: #0F172A; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 800; text-decoration: none;">
        AMAZON ($16) ↗
      </a>
      <a href="curriculum/teacher-guide.md" style="flex: 1; min-width: 100px; text-align: center; padding: 0.55rem 0.5rem; background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); color: #FFFFFF; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; text-decoration: none;">
        TEACHER GUIDE &rarr;
      </a>
    </div>
  </div>

</div>
