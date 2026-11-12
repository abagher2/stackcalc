---
title: "Prime Factor Studio 2D Classroom Simulator | StackCalc Virtual Manipulatives"
description: "Full-page interactive 2D Prime Factor Studio virtual manipulative. Logarithmic prime blocks, prime train builder, live 4-line RPN calculator stack, and real-time FACT / GCD / LCM decomposition engines for classroom displays."
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
        <span class="vlab-sku-badge">PRIME-01 // FULL-SCREEN CLASSROOM SIMULATOR</span>
        <h1 class="vlab-title" style="font-size: 1.35rem;">Prime Factor Studio &amp; Logarithmic Slide Stage</h1>
      </div>
      <div class="vlab-controls">
        <button id="vlab-btn-sound" class="vlab-btn-icon" title="Toggle Sound">🔊 AUDIO: ON</button>
        <button id="vlab-btn-fullscreen" class="vlab-btn-icon active" title="Fullscreen Projector Mode">⛶ FULLSCREEN PROJECTOR</button>
      </div>
    </div>

    <!-- PRIME FACTOR VIEW -->
    <div id="vlab-view-primes">
      <div class="vlab-grid">
        
        <!-- Left: Prime Block Palette -->
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
