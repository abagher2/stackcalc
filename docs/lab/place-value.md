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
        <span class="vlab-sku-badge" style="background:rgba(245,158,11,0.12); color:#F59E0B; border-color:rgba(245,158,11,0.3);">STACKCALC // PLACE VALUE STUDIO</span>
        <h1 class="vlab-title" style="font-size: 1.35rem;">Place Value &amp; Decimal Studio</h1>
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
            <div class="vlab-lcd-register"><span>T:</span> <span id="vlab-reg-t" class="vlab-reg-t-val">0</span></div>
            <div class="vlab-lcd-register"><span>Z:</span> <span id="vlab-reg-z" class="vlab-reg-z-val">0</span></div>
            <div class="vlab-lcd-register" style="color:#0284C7;"><span>Y:</span> <span id="vlab-reg-y" class="vlab-reg-y-val">0</span></div>
            <div class="vlab-lcd-register vlab-lcd-reg-x"><span>X:</span> <span id="vlab-reg-x" class="vlab-reg-x-val">0_</span></div>
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

  </div>
</div>
