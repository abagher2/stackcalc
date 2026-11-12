---
title: "Prime Factor Studio 2D Classroom Simulator | StackCalc Virtual Manipulatives"
description: "Full-page interactive 2D Prime Factor virtual manipulative. Logarithmic length prime blocks [2] through [23], 4-line RPN calculator stack, vertical prime train decomposition, GCD/LCM stack operations, and tactile number composition for classroom whiteboards."
hide:
  - navigation
  - toc
---

<div class="vlab-wrapper" style="margin: 0; max-width: 1200px; margin: 0 auto; padding: 1rem 0;">
  
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
    <a href="../../learning-lab/" style="font-family: 'Space Mono', monospace; font-size: 0.75rem; color: #38BDF8; text-decoration: none;">&larr; Back to Learning Lab</a>
    <div style="display: flex; gap: 8px;">
      <a href="https://stackcalcmath.etsy.com" target="_blank" rel="noopener noreferrer" style="font-family: 'Space Mono', monospace; font-size: 0.72rem; padding: 4px 10px; background: #FF4400; color: #FFFFFF; border-radius: 4px; text-decoration: none; font-weight: 700;">Buy Physical Kit on Etsy ↗</a>
      <a href="https://www.printables.com/@StackCalc_5593834" target="_blank" rel="noopener noreferrer" style="font-family: 'Space Mono', monospace; font-size: 0.72rem; padding: 4px 10px; background: #FA6B05; color: #FFFFFF; border-radius: 4px; text-decoration: none; font-weight: 700;">Free 3MFs (Printables) ↗</a>
    </div>
  </div>

  <div id="vlab-main-container" class="vlab-container">
    
    <!-- Top Telemetry & Control Bar -->
    <div class="vlab-header">
      <div class="vlab-title-group">
        <span class="vlab-sku-badge" style="background:rgba(16,185,129,0.12); color:#10B981; border-color:rgba(16,185,129,0.3);">STACKCALC // PRIME STUDIO</span>
        <h1 class="vlab-title" style="font-size: 1.35rem;">Prime Factor Studio</h1>
      </div>
      <div class="vlab-controls">
        <button id="vlab-btn-sound" class="vlab-btn-icon" title="Toggle Sound">🔊 AUDIO: ON</button>
        <button id="vlab-btn-fullscreen" class="vlab-btn-icon active" title="Fullscreen Projector Mode">⛶ FULLSCREEN PROJECTOR</button>
      </div>
    </div>

    <!-- PRIME FACTOR STUDIO VIEW -->
    <div id="vlab-view-primes">
      
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
            <div class="vlab-lcd-register"><span>T:</span> <span id="vlab-reg-t" class="vlab-reg-t-val">0</span></div>
            <div class="vlab-lcd-register"><span>Z:</span> <span id="vlab-reg-z" class="vlab-reg-z-val">0</span></div>
            <div class="vlab-lcd-register" style="color:#0284C7;"><span>Y:</span> <span id="vlab-reg-y" class="vlab-reg-y-val">0</span></div>
            <div class="vlab-lcd-register vlab-lcd-reg-x"><span>X:</span> <span id="vlab-reg-x" class="vlab-reg-x-val">0_</span></div>
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
