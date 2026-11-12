---
title: "Fraction Towers 2D Classroom Simulator | StackCalc Virtual Manipulatives"
description: "Full-page interactive 2D Fraction Towers virtual manipulative. Proportional 84mm reciprocal towers, drag-and-drop comparator, live 4-line RPN calculator stack, and real-time equivalence laser datum line for interactive classroom displays."
hide:
  - navigation
  - toc
---

<div class="vlab-wrapper" style="margin: 0; max-width: 1200px; margin: 0 auto; padding: 1rem 0;">
  
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
    <a href="../learning-lab/" style="font-family: 'Space Mono', monospace; font-size: 0.75rem; color: #38BDF8; text-decoration: none;">&larr; Back to Learning Lab</a>
    <div style="display: flex; gap: 8px;">
      <a href="https://stackcalcmath.etsy.com" target="_blank" rel="noopener noreferrer" style="font-family: 'Space Mono', monospace; font-size: 0.72rem; padding: 4px 10px; background: #FF4400; color: #FFFFFF; border-radius: 4px; text-decoration: none; font-weight: 700;">Buy Physical Kit on Etsy ↗</a>
      <a href="https://www.printables.com/@StackCalc_5593834" target="_blank" rel="noopener noreferrer" style="font-family: 'Space Mono', monospace; font-size: 0.72rem; padding: 4px 10px; background: #FA6B05; color: #FFFFFF; border-radius: 4px; text-decoration: none; font-weight: 700;">Free 3MFs (Printables) ↗</a>
    </div>
  </div>

  <div id="vlab-main-container" class="vlab-container">
    
    <!-- Top Telemetry & Control Bar -->
    <div class="vlab-header">
      <div class="vlab-title-group">
        <span class="vlab-sku-badge">STACKCALC // FRACTION STUDIO</span>
        <h1 class="vlab-title" style="font-size: 1.35rem;">Fraction Towers Studio</h1>
      </div>
      <div class="vlab-controls">
        <button id="vlab-btn-sound" class="vlab-btn-icon" title="Toggle Sound">🔊 AUDIO: ON</button>
        <button id="vlab-btn-fullscreen" class="vlab-btn-icon active" title="Fullscreen Projector Mode">⛶ FULLSCREEN PROJECTOR</button>
      </div>
    </div>

    <!-- FRACTION STUDIO VIEW -->
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

      <!-- Direct Fraction Input Bar -->
      <div class="vlab-direct-input-bar">
        <span class="vlab-palette-label">TYPE FRACTION:</span>
        <input type="text" id="vlab-frac-input" class="vlab-quick-input" placeholder="e.g. 3/4 or 1 1/2">
        <button id="vlab-btn-frac-add" class="vlab-btn-quick-add">+ BUILD TOWER</button>
        <span style="font-size: 0.72rem; color: #64748B; margin-left: auto;">Press Enter or click to build blocks</span>
      </div>

      <div class="vlab-grid">
        
        <!-- Left: Staging & Comparison Stage -->
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

  </div>
</div>
