---
title: "StackCalc Learning Lab | 2D Virtual Manipulatives & Stack Computing"
description: "Interactive 2D virtual manipulatives lab for schools: Fraction Towers (FRAC-01) and Prime Factor Studio (PRIME-01). Build quantities with tactile blocks, push values onto the 4-line RPN stack, execute operations, and verify mathematical equivalence."
hide:
  - navigation
  - toc
---

# StackCalc Learning Lab

The Learning Lab bridges Jerome Bruner’s **Concrete-Representational-Abstract (CRA)** framework with the mechanical clarity of **Reverse Polish Notation (RPN)**:
1. **Concrete:** Physical 3D-printed math blocks and tactile kits on classroom desks.
2. **Representational (2D Interactive Lab Below):** Virtual proportional fraction towers and vertical prime factor blocks for interactive whiteboards and 1:1 Chromebooks.
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
      <button id="vlab-tab-primes" class="vlab-nav-tab">🔬 Prime Factors</button>
    </div>

    <!-- VIEW 1: FRACTION STUDIO -->
    <div id="vlab-view-fractions">
      
      <!-- Top Horizontal Fraction Palette Shelf -->
      <div class="vlab-palette-bar">
        <span class="vlab-palette-label">FRACTION BLOCKS:</span>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/1',n:1,d:1,mm:84.0,cls:'frac-1-1'})">
          <span class="vlab-block-chip" style="background:#D49459; border: 1px solid #B37B42;"></span> 1/1
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/2',n:1,d:2,mm:42.0,cls:'frac-1-2'})">
          <span class="vlab-block-chip" style="background:#D49459; border: 1px solid #B37B42;"></span> 1/2
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/3',n:1,d:3,mm:28.0,cls:'frac-1-3'})">
          <span class="vlab-block-chip" style="background:#FF5F2D; border: 1px solid #E04B1D;"></span> 1/3
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/4',n:1,d:4,mm:21.0,cls:'frac-1-4'})">
          <span class="vlab-block-chip" style="background:#1D4ED8; border: 1px solid #3B82F6;"></span> 1/4
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/5',n:1,d:5,mm:16.8,cls:'frac-1-5'})">
          <span class="vlab-block-chip" style="background:#FFFFFF; border: 1px solid #CBD5E1;"></span> 1/5
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/6',n:1,d:6,mm:14.0,cls:'frac-1-6'})">
          <span class="vlab-block-chip" style="background:#FF5F2D; border: 1px solid #E04B1D;"></span> 1/6
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/8',n:1,d:8,mm:10.5,cls:'frac-1-8'})">
          <span class="vlab-block-chip" style="background:#1D4ED8; border: 1px solid #3B82F6;"></span> 1/8
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/9',n:1,d:9,mm:9.33,cls:'frac-1-9'})">
          <span class="vlab-block-chip" style="background:#FF5F2D; border: 1px solid #E04B1D;"></span> 1/9
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/10',n:1,d:10,mm:8.4,cls:'frac-1-10'})">
          <span class="vlab-block-chip" style="background:#FFFFFF; border: 1px solid #CBD5E1;"></span> 1/10
        </button>
        <button class="vlab-block-btn-chip" onclick="window.StackCalcLab.addFraction({label:'1/12',n:1,d:12,mm:7.0,cls:'frac-1-12'})">
          <span class="vlab-block-chip" style="background:#1D4ED8; border: 1px solid #3B82F6;"></span> 1/12
        </button>
      </div>

      <!-- Direct Fraction Input Bar -->
      <div class="vlab-direct-input-bar">
        <span class="vlab-palette-label">TYPE FRACTION:</span>
        <input type="text" id="vlab-frac-input" class="vlab-quick-input" placeholder="e.g. 3/4 or 1 1/2">
        <button id="vlab-btn-frac-add" class="vlab-btn-quick-add">+ BUILD TOWER</button>
        <span style="font-size: 0.72rem; color: #64748B; margin-left: auto;">Press Enter or click to build blocks</span>
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

    <!-- VIEW 2: PRIME FACTOR STUDIO -->
    <div id="vlab-view-primes" style="display:none;">
      
      <!-- Top Horizontal Prime Palette Shelf -->
      <div class="vlab-palette-bar">
        <span class="vlab-palette-label">PRIME NUMBERS:</span>
        <button class="vlab-block-btn-chip" data-prime-p="2">
          <span class="vlab-block-chip" style="background:#1D4ED8; border: 1px solid #3B82F6;"></span> 2
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="3">
          <span class="vlab-block-chip" style="background:#FF5F2D; border: 1px solid #E04B1D;"></span> 3
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="5">
          <span class="vlab-block-chip" style="background:#FFFFFF; border: 1px solid #CBD5E1;"></span> 5
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="7">
          <span class="vlab-block-chip" style="background:#D49459; border: 1px solid #B37B42;"></span> 7
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="11">
          <span class="vlab-block-chip" style="background:#F5C211; border: 1px solid #D5B50E;"></span> 11
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="13">
          <span class="vlab-block-chip" style="background:#F5C211; border: 1px solid #D5B50E;"></span> 13
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="17">
          <span class="vlab-block-chip" style="background:#F5C211; border: 1px solid #D5B50E;"></span> 17
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="19">
          <span class="vlab-block-chip" style="background:#F5C211; border: 1px solid #D5B50E;"></span> 19
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="23">
          <span class="vlab-block-chip" style="background:#F5C211; border: 1px solid #D5B50E;"></span> 23
        </button>
      </div>

      <!-- Direct Number Input Bar for Primes -->
      <div class="vlab-direct-input-bar">
        <span class="vlab-palette-label">TYPE NUMBER:</span>
        <input type="number" id="vlab-prime-input" class="vlab-quick-input" placeholder="e.g. 42 or 120" min="2" max="99999">
        <button id="vlab-btn-prime-add" class="vlab-btn-quick-add">+ FACTORIZE TOWER</button>
        <span style="font-size: 0.72rem; color: #64748B; margin-left: auto;">Press Enter or click to build prime blocks</span>
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

## Physical Manipulative Studios {: #physical-manipulative-studios }

Bring these interactive mathematical concepts into real hands with our launched tactile kits:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.25rem; margin: 1.5rem 0 2.5rem 0;">

  <!-- Card 1: Fraction Studio -->
  <div style="background: #11141A; border: 1px solid rgba(255, 107, 44, 0.35); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <span style="font-family: 'Space Mono', monospace; font-size: 0.7rem; color: #FF6B2C; font-weight: 700; text-transform: uppercase;">GRADES 2–6 &bull; FRAC-01</span>
      <h3 style="margin: 0.35rem 0; font-size: 1.15rem; color: #FFFFFF;">Fraction Studio Towers</h3>
      <p style="font-size: 0.84rem; color: #94A3B8; margin-bottom: 1.25rem; line-height: 1.5;">
        Interlocking fraction bars ($1$ to $1/12$) with calibrated millimeter heights and dual fraction/decimal faces for hands-on equivalence.
      </p>
    </div>
    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
      <a href="../products/fraction-studio/" style="flex: 1; min-width: 100px; text-align: center; padding: 0.55rem 0.5rem; background: #FF6B2C; color: #FFFFFF; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 800; text-decoration: none;">
        EXPLORE KIT &rarr;
      </a>
      <a href="https://stackcalcmath.etsy.com" target="_blank" rel="noopener noreferrer" style="flex: 1; min-width: 100px; text-align: center; padding: 0.55rem 0.5rem; background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); color: #FFFFFF; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; text-decoration: none;">
        ETSY ↗
      </a>
    </div>
  </div>

  <!-- Card 2: Prime Factor Studio -->
  <div style="background: #11141A; border: 1px solid rgba(16, 185, 129, 0.35); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <span style="font-family: 'Space Mono', monospace; font-size: 0.7rem; color: #10B981; font-weight: 700; text-transform: uppercase;">GRADES 3–8 &bull; PRIME-01</span>
      <h3 style="margin: 0.35rem 0; font-size: 1.15rem; color: #FFFFFF;">Prime Factor Studio</h3>
      <p style="font-size: 0.84rem; color: #94A3B8; margin-bottom: 1.25rem; line-height: 1.5;">
        Color-coded prime rods ($2, 3, 5, 7$) and interlocking factor blocks that turn composite multiplication, GCF, and LCM into physical 3D towers.
      </p>
    </div>
    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
      <a href="../products/prime-factor-studio/" style="flex: 1; min-width: 100px; text-align: center; padding: 0.55rem 0.5rem; background: #10B981; color: #0F172A; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 800; text-decoration: none;">
        EXPLORE KIT &rarr;
      </a>
      <a href="https://stackcalcmath.etsy.com" target="_blank" rel="noopener noreferrer" style="flex: 1; min-width: 100px; text-align: center; padding: 0.55rem 0.5rem; background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); color: #FFFFFF; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; text-decoration: none;">
        ETSY ↗
      </a>
    </div>
  </div>

  <!-- Card 3: Place Value Studio -->
  <div style="background: #11141A; border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <span style="font-family: 'Space Mono', monospace; font-size: 0.7rem; color: #38BDF8; font-weight: 700; text-transform: uppercase;">GRADES K–5 &bull; PLACE-01</span>
      <h3 style="margin: 0.35rem 0; font-size: 1.15rem; color: #FFFFFF;">Place Value Studio</h3>
      <p style="font-size: 0.84rem; color: #94A3B8; margin-bottom: 1.25rem; line-height: 1.5;">
        Modular base-10 counting trays, unit cubes, tens rods, and hundred flats for regrouping, carrying, and multi-digit arithmetic.
      </p>
    </div>
    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
      <a href="../products/place-value/" style="flex: 1; min-width: 100px; text-align: center; padding: 0.55rem 0.5rem; background: #38BDF8; color: #0F172A; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 800; text-decoration: none;">
        EXPLORE KIT &rarr;
      </a>
      <a href="https://stackcalcmath.etsy.com" target="_blank" rel="noopener noreferrer" style="flex: 1; min-width: 100px; text-align: center; padding: 0.55rem 0.5rem; background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); color: #FFFFFF; border-radius: 6px; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; text-decoration: none;">
        ETSY ↗
      </a>
    </div>
  </div>

</div>
