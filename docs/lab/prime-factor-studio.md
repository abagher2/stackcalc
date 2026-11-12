---
title: "Prime Factor Studio 2D Classroom Simulator | StackCalc Virtual Manipulatives"
description: "Full-page interactive 2D Prime Factor virtual manipulative. Logarithmic length prime blocks [2] through [23], 4-line RPN calculator stack, vertical prime train decomposition, GCD/LCM stack operations, and tactile number composition for classroom whiteboards."
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
        <span class="vlab-sku-badge" style="background:rgba(16,185,129,0.12); color:#10B981; border-color:rgba(16,185,129,0.3);">PRIME-01 // FULL-SCREEN CLASSROOM SIMULATOR</span>
        <h1 class="vlab-title" style="font-size: 1.35rem;">Prime Factor Studio &amp; Logarithmic Number Builder</h1>
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
        <span class="vlab-palette-label">PRIME PALETTE:</span>
        <button class="vlab-block-btn-chip" data-prime-p="2">
          <span class="vlab-block-chip" style="background:#0284C7;"></span> [2] <span class="vlab-block-spec">18mm</span>
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="3">
          <span class="vlab-block-chip" style="background:#10B981;"></span> [3] <span class="vlab-block-spec">28.5mm</span>
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="5">
          <span class="vlab-block-chip" style="background:#F59E0B;"></span> [5] <span class="vlab-block-spec">41.8mm</span>
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="7">
          <span class="vlab-block-chip" style="background:#8B5CF6;"></span> [7] <span class="vlab-block-spec">50.7mm</span>
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="11">
          <span class="vlab-block-chip" style="background:#EC4899;"></span> [11] <span class="vlab-block-spec">62.4mm</span>
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="13">
          <span class="vlab-block-chip" style="background:#06B6D4;"></span> [13] <span class="vlab-block-spec">66.8mm</span>
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="17">
          <span class="vlab-block-chip" style="background:#E11D48;"></span> [17] <span class="vlab-block-spec">73.6mm</span>
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="19">
          <span class="vlab-block-chip" style="background:#F97316;"></span> [19] <span class="vlab-block-spec">76.5mm</span>
        </button>
        <button class="vlab-block-btn-chip" data-prime-p="23">
          <span class="vlab-block-chip" style="background:#64748B;"></span> [23] <span class="vlab-block-spec">81.3mm</span>
        </button>
      </div>

      <div class="vlab-grid">
        
        <!-- Left: Vertical Prime Factor Columns -->
        <div class="vlab-stage-container">
          <div class="vlab-comparator-bay">
            <div class="vlab-columns-wrapper">
              
              <!-- Column 1: Prime Register Y (Stack) -->
              <div class="vlab-column-container">
                <div id="vlab-prime-stack-y" class="vlab-column"></div>
                <div class="vlab-col-meta-box">
                  <div class="vlab-column-title" style="color:#0284C7;">1. REGISTER Y (STACK)</div>
                  <div id="vlab-prime-meta-y" class="vlab-column-sub">Y: 0</div>
                </div>
              </div>

              <!-- Column 2: Prime Register X (Active Entry / Tower) -->
              <div class="vlab-column-container">
                <div id="vlab-prime-stack-x" class="vlab-column"></div>
                <div class="vlab-col-meta-box">
                  <div class="vlab-column-title" style="color:#38BDF8;">2. REGISTER X (ENTRY)</div>
                  <div id="vlab-prime-val" class="vlab-column-sub" style="font-weight: bold; color: #FFFFFF; font-size: 0.9rem;">0</div>
                </div>
              </div>

              <!-- Column 3: Prime Target / Decomposed Tower -->
              <div class="vlab-column-container">
                <div id="vlab-prime-target" class="vlab-column vlab-column-target"></div>
                <div class="vlab-col-meta-box">
                  <div class="vlab-column-title" style="color:#10B981;">3. TARGET / DECOMPOSED</div>
                  <div class="vlab-column-sub" style="color:#10B981;">[FACT / GCD / LCM]</div>
                </div>
              </div>

            </div>
          </div>

          <!-- Staging Readout & Actions -->
          <div class="vlab-staging-bar">
            <div class="vlab-staged-readout">
              <span class="vlab-staged-meta">PRIME FACTOR COMPOSITION:</span>
              <span id="vlab-prime-formula" style="color:#38BDF8; font-weight:800; font-family:'Space Mono',monospace; font-size:0.95rem;">No factors selected</span>
              <span id="vlab-prime-meta" class="vlab-staged-meta">Logarithmic Height: 0.0 mm • 0 Factors</span>
            </div>
            <div style="display:flex; flex-wrap:wrap; gap:8px;">
              <button id="vlab-btn-push-prime" class="vlab-btn-push">↵ PUSH TO STACK [ENTER]</button>
              <button id="vlab-btn-drop-prime" class="vlab-btn-secondary" title="Pop topmost prime block">⌫ DROP TOP</button>
              <button id="vlab-btn-clear-prime" class="vlab-btn-secondary" title="Clear prime blocks">✕ CLEAR</button>
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
            <div class="vlab-lcd-register"><span>T:</span> <span id="vlab-reg-t">0.0000</span></div>
            <div class="vlab-lcd-register"><span>Z:</span> <span id="vlab-reg-z">0.0000</span></div>
            <div class="vlab-lcd-register" style="color:#0284C7;"><span>Y:</span> <span id="vlab-reg-y">0.0000</span></div>
            <div class="vlab-lcd-register vlab-lcd-reg-x"><span>X:</span> <span id="vlab-reg-x">0.0000_</span></div>
          </div>

          <!-- Operations Grid -->
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

          <div style="font-size:0.72rem; color:#94A3B8; line-height:1.5; font-family:'Space Mono',monospace; background:#11141A; padding:12px; border-radius:6px; border:1px solid rgba(255,255,255,0.08);">
            <strong style="color:#FFFFFF;">Prime Operations:</strong><br>
            • <strong>Vertical Stacking:</strong> Blocks stack vertically with logarithmic heights ($\log a + \log b = \log ab$).<br>
            • <strong>[FACT]:</strong> Decomposes Reg X into a vertical prime tower.<br>
            • <strong>[GCD]:</strong> Greatest Common Divisor of Y and X.<br>
            • <strong>[LCM]:</strong> Least Common Multiple of Y and X.
          </div>
        </div>

      </div>
    </div>

  </div>
</div>
