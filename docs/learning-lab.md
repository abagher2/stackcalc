---
title: "StackCalc Learning Lab | 2D Virtual Manipulatives & Stack Computing"
description: "Interactive 2D virtual manipulatives lab for schools: Fraction Towers (FRAC-01), Place-Value Decimal Trays (PLACE-01), and Prime Factor Studio (PRIME-01). Build quantities with tactile blocks, push values onto the 4-line RPN stack, execute operations, and verify mathematical equivalence."
hide:
  - navigation
  - toc
---

# StackCalc Learning Lab

The Learning Lab bridges Jerome Bruner’s **Concrete-Representational-Abstract (CRA)** framework with the mechanical clarity of **Reverse Polish Notation (RPN)**:
1. **Concrete:** Physical 3D-printed math blocks and tactile kits on classroom desks.
2. **Representational (2D Interactive Lab Below):** Virtual proportional blocks and place-value trays for interactive whiteboards and 1:1 Chromebooks.
3. **Abstract:** Dedicated 4-line operational stack registers ($X, Y, Z, T$) on the **SC-6 Elementary** and **SC-32 Scientific** calculators.

---

<!-- ==========================================================================
     STACKCALC 2D VIRTUAL MANIPULATIVES LAB (CLASSROOM SIMULATOR)
     ========================================================================== -->
<div class="vlab-wrapper">
  <div id="vlab-main-container" class="vlab-container">
    
    <!-- Top Telemetry & Control Bar -->
    <div class="vlab-header">
      <div class="vlab-title-group">
        <span class="vlab-sku-badge">STACKCALC // LEARNING LAB</span>
        <h2 class="vlab-title">Virtual Manipulatives &amp; Stack Computing Lab</h2>
      </div>
      <div class="vlab-controls">
        <button id="vlab-btn-sound" class="vlab-btn-icon" title="Toggle Sound">🔊 AUDIO: ON</button>
        <button id="vlab-btn-fullscreen" class="vlab-btn-icon active" title="Fullscreen Projector Mode">⛶ FULLSCREEN PROJECTOR</button>
      </div>
    </div>

    <!-- Mode Selector Tabs -->
    <div class="vlab-nav-tabs">
      <button id="vlab-tab-fractions" class="vlab-nav-tab active">📐 Fraction Towers</button>
      <button id="vlab-tab-placevalue" class="vlab-nav-tab">🔢 Place Value Blocks</button>
      <button id="vlab-tab-primes" class="vlab-nav-tab">🔬 Prime Factors</button>
    </div>

    <!-- VIEW 1: FRACTION STUDIO -->
    <div id="vlab-view-fractions">
      
      <!-- Top Horizontal Fraction Palette Shelf -->
      <div class="vlab-palette-bar">
        <span class="vlab-palette-label">FRACTION BLOCKS:</span>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/1',n:1,d:1,mm:84.0,cls:'frac-1-1'})">
          <span class="vlab-block-chip" style="background:#334155;"></span> 1/1
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/2',n:1,d:2,mm:42.0,cls:'frac-1-2'})">
          <span class="vlab-block-chip" style="background:#0284C7;"></span> 1/2
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/3',n:1,d:3,mm:28.0,cls:'frac-1-3'})">
          <span class="vlab-block-chip" style="background:#059669;"></span> 1/3
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/4',n:1,d:4,mm:21.0,cls:'frac-1-4'})">
          <span class="vlab-block-chip" style="background:#D97706;"></span> 1/4
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/5',n:1,d:5,mm:16.8,cls:'frac-1-5'})">
          <span class="vlab-block-chip" style="background:#7C3AED;"></span> 1/5
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/6',n:1,d:6,mm:14.0,cls:'frac-1-6'})">
          <span class="vlab-block-chip" style="background:#E11D48;"></span> 1/6
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/8',n:1,d:8,mm:10.5,cls:'frac-1-8'})">
          <span class="vlab-block-chip" style="background:#0891B2;"></span> 1/8
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/10',n:1,d:10,mm:8.4,cls:'frac-1-10'})">
          <span class="vlab-block-chip" style="background:#0D9488;"></span> 1/10
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/12',n:1,d:12,mm:7.0,cls:'frac-1-12'})">
          <span class="vlab-block-chip" style="background:#4F46E5;"></span> 1/12
        </button>
      </div>

      <div class="vlab-grid">
        
        <!-- Left: Staging Stage -->
        <div class="vlab-stage-container">
          <div class="vlab-comparator-bay">
            <div class="vlab-columns-wrapper">
              
              <!-- Column 1 (Left): Register X (Active Entry / Tower) -->
              <div class="vlab-column-container">
                <div id="vlab-col-stack-x" class="vlab-column vlab-column-entry"></div>
                <div class="vlab-col-meta-box">
                  <div class="vlab-column-title" style="color:#38BDF8;">ENTRY (X)</div>
                  <div id="vlab-staged-val" class="vlab-column-sub" style="font-weight: bold; color: #FFFFFF;">0</div>
                </div>
              </div>

              <!-- Column 2 (Right): Register Y (The Stack) -->
              <div class="vlab-column-container">
                <div id="vlab-col-stack-y" class="vlab-column vlab-column-stack"></div>
                <div class="vlab-col-meta-box">
                  <div class="vlab-column-title" style="color:#0284C7;">SAVED STACK (Y)</div>
                  <div id="vlab-meta-stack-y" class="vlab-column-sub">0</div>
                </div>
              </div>

            </div>
          </div>

          <!-- Staging Action Toolbar -->
          <div class="vlab-staging-bar">
            <div class="vlab-staged-readout">
              <span class="vlab-staged-meta">ENTRY (X) VALUE:</span>
              <span id="vlab-staged-meta" class="vlab-staged-val" style="color: #38BDF8; font-weight: 800; font-size: 1.15rem;">0</span>
            </div>
            <div style="display:flex; flex-wrap:wrap; gap:8px;">
              <button id="vlab-btn-push-frac" class="vlab-btn-push">↵ ENTER (SAVE)</button>
              <button id="vlab-btn-drop-frac" class="vlab-btn-secondary" title="Remove topmost block">⌫ REMOVE TOP</button>
              <button id="vlab-btn-clear-frac" class="vlab-btn-secondary" title="Clear Register X">✕ CLEAR</button>
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
            <div class="vlab-lcd-register"><span>T:</span> <span id="vlab-reg-t" class="vlab-reg-t-val">0</span></div>
            <div class="vlab-lcd-register"><span>Z:</span> <span id="vlab-reg-z" class="vlab-reg-z-val">0</span></div>
            <div class="vlab-lcd-register" style="color:#0284C7;"><span>Y:</span> <span id="vlab-reg-y" class="vlab-reg-y-val">0</span></div>
            <div class="vlab-lcd-register vlab-lcd-reg-x"><span>X:</span> <span id="vlab-reg-x" class="vlab-reg-x-val">0_</span></div>
          </div>

          <!-- Operation Keypad -->
          <div class="vlab-op-grid">
            <button class="vlab-btn-op" data-vlab-op="+">+</button>
            <button class="vlab-btn-op" data-vlab-op="-">&minus;</button>
            <button class="vlab-btn-op" data-vlab-op="×">&times;</button>
            <button class="vlab-btn-op" data-vlab-op="÷">&divide;</button>
          </div>

          <div style="display:grid; grid-template-columns: repeat(5, 1fr); gap: 6px;">
            <button id="vlab-btn-simp" class="vlab-btn-func" title="Step-by-step fraction simplification"><span class="vlab-key-shift-blue">[g]</span>SIMP</button>
            <button id="vlab-btn-mixed" class="vlab-btn-func" title="Mixed number display (e.g. 1 1/2)">a ᵇ/c</button>
            <button id="vlab-btn-improper" class="vlab-btn-func" title="Improper fraction display (e.g. 3/2)"><span class="vlab-key-shift">[f]</span>d/c</button>
            <button id="vlab-btn-invert" class="vlab-btn-func" title="Reciprocal inversion (1/x)">1/x</button>
            <button id="vlab-btn-clx" class="vlab-btn-func" title="Clear Register X">CLEAR</button>
          </div>

          <!-- 3-Step Student Guide -->
          <div class="vlab-kid-guide">
            <div class="vlab-step-pill"><span class="vlab-step-num">1</span> <strong>Pick Blocks</strong> into Entry (X)</div>
            <div class="vlab-step-arrow">➔</div>
            <div class="vlab-step-pill"><span class="vlab-step-num">2</span> <strong>Press ENTER</strong> to save into (Y)</div>
            <div class="vlab-step-arrow">➔</div>
            <div class="vlab-step-pill"><span class="vlab-step-num">3</span> <strong>Tap + or &times;</strong> to solve!</div>
          </div>
        </div>

      </div>
    </div>

    <!-- VIEW 2: PLACE-VALUE STUDIO -->
    <div id="vlab-view-placevalue" style="display:none;">
      <div class="vlab-grid">
        
        <!-- Left & Center: Place Value Desk Tray -->
        <div class="vlab-stage-container">
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

            <!-- Shelf 0: Carry / Regroup Shelf -->
            <div class="pv-shelf-container pv-shelf-carry">
              <div class="pv-shelf-title-bar" style="color:#F59E0B;">
                <span>CARRY / REGROUP SHELF</span>
                <span style="font-size:0.65rem; color:#FCD34D;">[+1] TOKENS</span>
              </div>
              <div class="pv-grid-row">
                <div id="pv-socket-carry-100" class="pv-socket pv-socket-carry"></div>
                <div id="pv-socket-carry-10" class="pv-socket pv-socket-carry"></div>
                <div id="pv-socket-carry-1" class="pv-socket pv-socket-carry"></div>
                <div class="pv-decimal-sep">&bull;</div>
                <div id="pv-socket-carry-0.1" class="pv-socket pv-socket-carry"></div>
                <div id="pv-socket-carry-0.01" class="pv-socket pv-socket-carry"></div>
                <div id="pv-socket-carry-0.001" class="pv-socket pv-socket-carry"></div>
              </div>
            </div>

            <!-- Shelf 1: Row 1 / Waiting Shelf (Register Y) -->
            <div class="pv-shelf-container pv-shelf-y">
              <div class="pv-shelf-title-bar" style="color:#0284C7;">
                <span>ROW 1: WAITING SHELF (Y)</span>
                <span>TOTAL: <strong id="pv-row1-val" style="color:#FFFFFF; font-size:0.9rem;">0</strong></span>
              </div>
              <div class="pv-grid-row">
                <div id="pv-socket-y-100" class="pv-socket"></div>
                <div id="pv-socket-y-10" class="pv-socket"></div>
                <div id="pv-socket-y-1" class="pv-socket"></div>
                <div class="pv-decimal-sep">&bull;</div>
                <div id="pv-socket-y-0.1" class="pv-socket"></div>
                <div id="pv-socket-y-0.01" class="pv-socket"></div>
                <div id="pv-socket-y-0.001" class="pv-socket"></div>
              </div>
              <!-- Row 1 Steppers -->
              <div class="pv-controls-row">
                <div class="pv-stepper">
                  <button class="pv-btn-step" data-pv-row="1" data-pv-col="100" data-pv-delta="1">+</button>
                  <button class="pv-btn-step" data-pv-row="1" data-pv-col="100" data-pv-delta="-1">&minus;</button>
                </div>
                <div class="pv-stepper">
                  <button class="pv-btn-step" data-pv-row="1" data-pv-col="10" data-pv-delta="1">+</button>
                  <button class="pv-btn-step" data-pv-row="1" data-pv-col="10" data-pv-delta="-1">&minus;</button>
                </div>
                <div class="pv-stepper">
                  <button class="pv-btn-step" data-pv-row="1" data-pv-col="1" data-pv-delta="1">+</button>
                  <button class="pv-btn-step" data-pv-row="1" data-pv-col="1" data-pv-delta="-1">&minus;</button>
                </div>
                <div></div>
                <div class="pv-stepper">
                  <button class="pv-btn-step" data-pv-row="1" data-pv-col="0.1" data-pv-delta="1">+</button>
                  <button class="pv-btn-step" data-pv-row="1" data-pv-col="0.1" data-pv-delta="-1">&minus;</button>
                </div>
                <div class="pv-stepper">
                  <button class="pv-btn-step" data-pv-row="1" data-pv-col="0.01" data-pv-delta="1">+</button>
                  <button class="pv-btn-step" data-pv-row="1" data-pv-col="0.01" data-pv-delta="-1">&minus;</button>
                </div>
                <div class="pv-stepper">
                  <button class="pv-btn-step" data-pv-row="1" data-pv-col="0.001" data-pv-delta="1">+</button>
                  <button class="pv-btn-step" data-pv-row="1" data-pv-col="0.001" data-pv-delta="-1">&minus;</button>
                </div>
              </div>
            </div>

            <!-- Shelf 2: Row 2 / Active Desk (Register X) -->
            <div class="pv-shelf-container pv-shelf-x">
              <div class="pv-shelf-title-bar" style="color:#38BDF8;">
                <span>ROW 2: ACTIVE DESK (X)</span>
                <span>TOTAL: <strong id="pv-total-val" style="color:#FFFFFF; font-size:0.9rem;">0</strong></span>
              </div>
              <div class="pv-grid-row">
                <div id="pv-socket-100" class="pv-socket"></div>
                <div id="pv-socket-10" class="pv-socket"></div>
                <div id="pv-socket-1" class="pv-socket"></div>
                <div class="pv-decimal-sep">&bull;</div>
                <div id="pv-socket-0.1" class="pv-socket"></div>
                <div id="pv-socket-0.01" class="pv-socket"></div>
                <div id="pv-socket-0.001" class="pv-socket"></div>
              </div>
              <!-- Row 2 Steppers -->
              <div class="pv-controls-row">
                <div class="pv-stepper">
                  <button class="pv-btn-step" data-pv-row="2" data-pv-col="100" data-pv-delta="1">+</button>
                  <button class="pv-btn-step" data-pv-row="2" data-pv-col="100" data-pv-delta="-1">&minus;</button>
                </div>
                <div class="pv-stepper">
                  <button class="pv-btn-step" data-pv-row="2" data-pv-col="10" data-pv-delta="1">+</button>
                  <button class="pv-btn-step" data-pv-row="2" data-pv-col="10" data-pv-delta="-1">&minus;</button>
                </div>
                <div class="pv-stepper">
                  <button class="pv-btn-step" data-pv-row="2" data-pv-col="1" data-pv-delta="1">+</button>
                  <button class="pv-btn-step" data-pv-row="2" data-pv-col="1" data-pv-delta="-1">&minus;</button>
                </div>
                <div></div>
                <div class="pv-stepper">
                  <button class="pv-btn-step" data-pv-row="2" data-pv-col="0.1" data-pv-delta="1">+</button>
                  <button class="pv-btn-step" data-pv-row="2" data-pv-col="0.1" data-pv-delta="-1">&minus;</button>
                </div>
                <div class="pv-stepper">
                  <button class="pv-btn-step" data-pv-row="2" data-pv-col="0.01" data-pv-delta="1">+</button>
                  <button class="pv-btn-step" data-pv-row="2" data-pv-col="0.01" data-pv-delta="-1">&minus;</button>
                </div>
                <div class="pv-stepper">
                  <button class="pv-btn-step" data-pv-row="2" data-pv-col="0.001" data-pv-delta="1">+</button>
                  <button class="pv-btn-step" data-pv-row="2" data-pv-col="0.001" data-pv-delta="-1">&minus;</button>
                </div>
              </div>
            </div>

            <!-- Regroup Alert Note -->
            <div id="pv-regroup-alert" style="display:none; background:rgba(255,68,0,0.15); border:1px solid #FF4400; color:#FF9900; padding:8px 12px; border-radius:6px; font-family:'Space Mono',monospace; font-size:0.75rem;">
            </div>

            <!-- Staging Toolbar for Place Value -->
            <div class="vlab-staging-bar">
              <div class="vlab-staged-readout">
                <span class="vlab-staged-meta">ACTIVE (X):</span>
                <span id="pv-readout-x" class="vlab-staged-val">0</span>
              </div>
              <div style="display:flex; flex-wrap:wrap; gap:8px;">
                <button id="pv-btn-regroup" class="vlab-btn-secondary" style="border-color:#F59E0B; color:#F59E0B;">🔄 REGROUP (10➔1)</button>
                <button id="pv-btn-unbundle" class="vlab-btn-secondary" style="border-color:#38BDF8; color:#38BDF8;">✂️ UNBUNDLE (1➔10)</button>
                <button id="pv-btn-push" class="vlab-btn-push">↵ ENTER (SAVE X➔Y)</button>
                <button id="pv-btn-clear" class="vlab-btn-secondary">✕ CLEAR</button>
              </div>
            </div>

          </div>
        </div>

        <!-- Right Console (Shares the 4-Line RPN Stack) -->
        <div class="vlab-calc-console">
          <div class="vlab-lcd">
            <div class="vlab-lcd-annunciator">
              <span>STACKCALC // PLACE VALUE</span>
              <span>[BASE 10]</span>
            </div>
            <div class="vlab-lcd-register"><span>T:</span> <span class="vlab-reg-t-val">0</span></div>
            <div class="vlab-lcd-register"><span>Z:</span> <span class="vlab-reg-z-val">0</span></div>
            <div class="vlab-lcd-register" style="color:#0284C7;"><span>Y:</span> <span class="vlab-reg-y-val">0</span></div>
            <div class="vlab-lcd-register vlab-lcd-reg-x"><span>X:</span> <span class="vlab-reg-x-val">0_</span></div>
          </div>

          <div class="vlab-op-grid">
            <button class="vlab-btn-op" data-vlab-op="+">+</button>
            <button class="vlab-btn-op" data-vlab-op="-">&minus;</button>
            <button class="vlab-btn-op" data-vlab-op="×">&times;</button>
            <button class="vlab-btn-op" data-vlab-op="÷">&divide;</button>
          </div>

          <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap: 6px;">
            <button id="pv-console-regroup" class="vlab-btn-func"><span class="vlab-key-shift">[f]</span>REGROUP</button>
            <button id="pv-console-unbundle" class="vlab-btn-func"><span class="vlab-key-shift-blue">[g]</span>UNBUNDLE</button>
            <button id="vlab-btn-clx" class="vlab-btn-func">CLEAR</button>
          </div>

          <!-- 3-Step Student Guide -->
          <div class="vlab-kid-guide">
            <div class="vlab-step-pill"><span class="vlab-step-num">1</span> <strong>Tap + / &minus;</strong> to place base-10 blocks</div>
            <div class="vlab-step-arrow">➔</div>
            <div class="vlab-step-pill"><span class="vlab-step-num">2</span> <strong>Press ENTER</strong> to save into Row 1 (Y)</div>
            <div class="vlab-step-arrow">➔</div>
            <div class="vlab-step-pill"><span class="vlab-step-num">3</span> <strong>Tap +, &minus;, or &times;</strong> with carry/regroup!</div>
          </div>
        </div>

      </div>
    </div>

    <!-- VIEW 3: PRIME FACTOR STUDIO -->
    <div id="vlab-view-primes" style="display:none;">
      
      <!-- Top Horizontal Prime Palette Shelf -->
      <div class="vlab-palette-bar">
        <span class="vlab-palette-label">PRIME NUMBERS:</span>
        <button class="vlab-block-btn-chip" data-prime-p="2">
          <span class="vlab-block-chip" style="background:#0284C7;"></span> 2
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="3">
          <span class="vlab-block-chip" style="background:#10B981;"></span> 3
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="5">
          <span class="vlab-block-chip" style="background:#F59E0B;"></span> 5
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="7">
          <span class="vlab-block-chip" style="background:#8B5CF6;"></span> 7
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="11">
          <span class="vlab-block-chip" style="background:#EC4899;"></span> 11
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="13">
          <span class="vlab-block-chip" style="background:#06B6D4;"></span> 13
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="17">
          <span class="vlab-block-chip" style="background:#E11D48;"></span> 17
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="19">
          <span class="vlab-block-chip" style="background:#F97316;"></span> 19
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="23">
          <span class="vlab-block-chip" style="background:#64748B;"></span> 23
        </button>
      </div>

      <div class="vlab-grid">
        
        <!-- Left: Vertical Prime Factor Columns -->
        <div class="vlab-stage-container">
          <div class="vlab-comparator-bay">
            <div class="vlab-columns-wrapper">
              
              <!-- Column 1 (Left): Prime Register X (Active Entry / Tower) -->
              <div class="vlab-column-container">
                <div id="vlab-prime-stack-x" class="vlab-column vlab-column-entry"></div>
                <div class="vlab-col-meta-box">
                  <div class="vlab-column-title" style="color:#38BDF8;">ENTRY (X)</div>
                  <div id="vlab-prime-val" class="vlab-column-sub" style="font-weight: bold; color: #FFFFFF; font-size: 1.15rem;">0</div>
                </div>
              </div>

              <!-- Column 2 (Right): Prime Register Y (Stack) -->
              <div class="vlab-column-container">
                <div id="vlab-prime-stack-y" class="vlab-column vlab-column-stack"></div>
                <div class="vlab-col-meta-box">
                  <div class="vlab-column-title" style="color:#0284C7;">SAVED STACK (Y)</div>
                  <div id="vlab-prime-meta-y" class="vlab-column-sub">0</div>
                </div>
              </div>

            </div>
          </div>

          <!-- Staging Readout & Actions -->
          <div class="vlab-staging-bar">
            <div class="vlab-staged-readout">
              <span class="vlab-staged-meta">COMPOSITE VALUE (X):</span>
              <span id="vlab-prime-formula" style="color:#38BDF8; font-weight:800; font-family:'Space Mono',monospace; font-size:1.15rem;">0</span>
              <span id="vlab-prime-meta" class="vlab-staged-meta"></span>
            </div>
            <div style="display:flex; flex-wrap:wrap; gap:8px;">
              <button id="vlab-btn-push-prime" class="vlab-btn-push">↵ ENTER (SAVE)</button>
              <button id="vlab-btn-drop-prime" class="vlab-btn-secondary" title="Remove topmost prime block">⌫ REMOVE TOP</button>
              <button id="vlab-btn-clear-prime" class="vlab-btn-secondary" title="Clear prime blocks">✕ CLEAR</button>
            </div>
          </div>
        </div>

        <!-- Right: 4-Line RPN Stack & Factor Operations -->
        <div class="vlab-calc-console">
          <div class="vlab-lcd">
            <div class="vlab-lcd-annunciator">
              <span>STACKCALC // PRIME MODE</span>
              <span>[NUMBERS]</span>
            </div>
            <div class="vlab-lcd-register"><span>T:</span> <span class="vlab-reg-t-val">0</span></div>
            <div class="vlab-lcd-register"><span>Z:</span> <span class="vlab-reg-z-val">0</span></div>
            <div class="vlab-lcd-register" style="color:#0284C7;"><span>Y:</span> <span class="vlab-reg-y-val">0</span></div>
            <div class="vlab-lcd-register vlab-lcd-reg-x"><span>X:</span> <span class="vlab-reg-x-val">0_</span></div>
          </div>

          <!-- Operations Grid -->
          <div class="vlab-op-grid">
            <button class="vlab-btn-op" data-vlab-op="+">+</button>
            <button class="vlab-btn-op" data-vlab-op="-">&minus;</button>
            <button class="vlab-btn-op" data-vlab-op="×">&times;</button>
            <button class="vlab-btn-op" data-vlab-op="÷">&divide;</button>
          </div>

          <!-- Dedicated Prime & Factor Operations -->
          <div style="display:grid; grid-template-columns: repeat(2, 1fr); gap: 6px; margin-bottom: 6px;">
            <button id="vlab-btn-fact" class="vlab-btn-func" title="Factorize composite number into prime blocks"><span class="vlab-key-shift-blue">[g]</span>FACTORS</button>
            <button id="vlab-btn-cfac" class="vlab-btn-func" title="Find shared prime factors of Y and X"><span class="vlab-key-shift">[f]</span>COMMON FACTORS</button>
          </div>
          <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap: 6px;">
            <button id="vlab-btn-gcd" class="vlab-btn-func" title="Greatest Common Factor">GCF</button>
            <button id="vlab-btn-lcm" class="vlab-btn-func" title="Least Common Multiple">LCM</button>
            <button id="vlab-btn-clx" class="vlab-btn-func" title="Clear Register X">CLEAR</button>
          </div>

          <!-- 3-Step Student Guide -->
          <div class="vlab-kid-guide">
            <div class="vlab-step-pill"><span class="vlab-step-num">1</span> <strong>Pick Prime Factors</strong> into Entry (X)</div>
            <div class="vlab-step-arrow">➔</div>
            <div class="vlab-step-pill"><span class="vlab-step-num">2</span> <strong>Press ENTER</strong> to save into (Y)</div>
            <div class="vlab-step-arrow">➔</div>
            <div class="vlab-step-pill"><span class="vlab-step-num">3</span> <strong>Tap &times;, FACTORS, or GCF</strong>!</div>
          </div>
        </div>

      </div>
    </div>

  </div>
</div>

---

## Official Companion Books & Literature {: #download-the-prototype-materials }

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
