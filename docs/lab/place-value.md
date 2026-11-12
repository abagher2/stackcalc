---
title: "Place Value Trays 2D Classroom Simulator | StackCalc Virtual Manipulatives"
description: "Full-page interactive 2D Place Value virtual manipulative. Dual 6x2 whole number and decimal activity trays, base-10 block steppers, live 4-line RPN calculator stack, and real-time regrouping alerts for classroom projectors."
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
        <span class="vlab-sku-badge" style="background:rgba(245,158,11,0.12); color:#F59E0B; border-color:rgba(245,158,11,0.3);">PLACE-01 // FULL-SCREEN CLASSROOM SIMULATOR</span>
        <h1 class="vlab-title" style="font-size: 1.35rem;">Place Value Trays &amp; Decimal Regrouping Studio</h1>
      </div>
      <div class="vlab-controls">
        <button id="vlab-btn-sound" class="vlab-btn-icon" title="Toggle Sound">🔊 AUDIO: ON</button>
        <button id="vlab-btn-fullscreen" class="vlab-btn-icon active" title="Fullscreen Projector Mode">⛶ FULLSCREEN PROJECTOR</button>
      </div>
    </div>

    <!-- PLACE-VALUE STUDIO VIEW -->
    <div id="vlab-view-placevalue">
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
            <div class="vlab-staging-bar">
              <div class="vlab-staged-readout">
                <span class="vlab-staged-meta">ACTIVE VALUE IN REGISTER X:</span>
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
            <div class="vlab-lcd-register"><span>T:</span> <span id="vlab-reg-t">0.0000</span></div>
            <div class="vlab-lcd-register"><span>Z:</span> <span id="vlab-reg-z">0.0000</span></div>
            <div class="vlab-lcd-register" style="color:#0284C7;"><span>Y:</span> <span id="vlab-reg-y">0.0000</span></div>
            <div class="vlab-lcd-register vlab-lcd-reg-x"><span>X:</span> <span id="vlab-reg-x">0.0000_</span></div>
          </div>

          <div class="vlab-op-grid">
            <button class="vlab-btn-op" data-vlab-op="+">+</button>
            <button class="vlab-btn-op" data-vlab-op="-">&minus;</button>
            <button class="vlab-btn-op" data-vlab-op="×">&times;</button>
            <button class="vlab-btn-op" data-vlab-op="÷">&divide;</button>
          </div>

          <div style="font-size:0.72rem; color:#94A3B8; line-height:1.5; font-family:'Space Mono',monospace; background:#11141A; padding:12px; border-radius:6px; border:1px solid rgba(255,255,255,0.08);">
            <strong style="color:#FFFFFF;">CRA Workflow:</strong><br>
            1. Tap [+] to stack base-10 chips into Reg X.<br>
            2. Press [ENTER] to push 1st number to Stack (Reg Y).<br>
            3. Build 2nd number into Reg X.<br>
            4. Press [+] or [&minus;] to calculate on the stack.<br>
            5. Observe regrouping &amp; carrying!
          </div>
        </div>

      </div>
    </div>

  </div>
</div>
