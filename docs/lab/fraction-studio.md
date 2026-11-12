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
        <span class="vlab-sku-badge">FRAC-01 // FULL-SCREEN CLASSROOM SIMULATOR</span>
        <h1 class="vlab-title" style="font-size: 1.35rem;">Fraction Towers &amp; Proportional Equivalence Studio</h1>
      </div>
      <div class="vlab-controls">
        <button id="vlab-btn-sound" class="vlab-btn-icon" title="Toggle Sound">🔊 AUDIO: ON</button>
        <button id="vlab-btn-fullscreen" class="vlab-btn-icon active" title="Fullscreen Projector Mode">⛶ FULLSCREEN PROJECTOR</button>
      </div>
    </div>

    <!-- FRACTION STUDIO VIEW -->
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
                <div class="vlab-column-title" style="color:#10B981;">3. EQUIVALENCE TARGET</div>
              </div>

            </div>
          </div>

          <!-- Staging Action Toolbar -->
          <div class="vlab-staging-bar">
            <div class="vlab-staged-readout">
              <span class="vlab-staged-meta">STAGED FRACTION:</span>
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

  </div>
</div>
