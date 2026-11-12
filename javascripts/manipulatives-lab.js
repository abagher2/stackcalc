/**
 * =========================================================================
 * STACKCALC 2D VIRTUAL MANIPULATIVES LAB ENGINE
 * Authentic Concrete-Representational-Abstract (CRA) Classroom Simulator
 * Fractions (FRAC-01) & Place-Value Trays (PLACE-01)
 * =========================================================================
 */

(function () {
  'use strict';

  // --- 1. Acoustic Synthesizer (Web Audio API) ---
  let audioCtx = null;
  let soundEnabled = true;

  function initAudio() {
    if (!audioCtx) {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (AudioContextClass) {
        audioCtx = new AudioContextClass();
      }
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
  }

  function playTone(freq, duration, type, volume) {
    if (!soundEnabled) return;
    try {
      initAudio();
      if (!audioCtx) return;
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = type || 'sine';
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
      gain.gain.setValueAtTime(volume || 0.15, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + duration);
    } catch (e) {
      // Audio fallback
    }
  }

  function playClick() {
    playTone(680, 0.04, 'triangle', 0.18);
  }

  function playPush() {
    playTone(520, 0.08, 'sine', 0.22);
    setTimeout(() => playTone(780, 0.12, 'sine', 0.2), 60);
  }

  function playOp() {
    playTone(600, 0.06, 'triangle', 0.2);
    setTimeout(() => playTone(440, 0.1, 'sine', 0.18), 40);
  }

  function playSuccess() {
    // Triumphant major chord (C5 - E5 - G5 - C6)
    playTone(523.25, 0.2, 'triangle', 0.2);
    setTimeout(() => playTone(659.25, 0.25, 'triangle', 0.2), 80);
    setTimeout(() => playTone(783.99, 0.3, 'triangle', 0.2), 160);
    setTimeout(() => playTone(1046.50, 0.45, 'triangle', 0.25), 240);
  }

  // --- 2. Exact Fraction Rational Math Helpers ---
  function gcd(a, b) {
    a = Math.abs(Math.round(a));
    b = Math.abs(Math.round(b));
    while (b) {
      const t = b;
      b = a % b;
      a = t;
    }
    return a;
  }

  function simplifyFrac(n, d) {
    if (d === 0) return { n: 0, d: 1 };
    const g = gcd(n, d);
    let sn = n / g;
    let sd = d / g;
    if (sd < 0) {
      sn = -sn;
      sd = -sd;
    }
    return { n: sn, d: sd };
  }

  function formatFrac(n, d) {
    const s = simplifyFrac(n, d);
    if (s.d === 1) return `${s.n}`;
    if (s.n === 0) return '0';
    return `${s.n}/${s.d}`;
  }

  // --- 3. Core State Architecture ---
  const state = {
    activeTab: 'fractions', // 'fractions' | 'placevalue'
    soundOn: true,
    fdisp: true, // Fraction display mode

    // 4-Line RPN Stack (Stores rational objects: { n, d, val })
    stack: {
      t: { n: 0, d: 1, val: 0 },
      z: { n: 0, d: 1, val: 0 },
      y: { n: 0, d: 1, val: 0 },
      x: { n: 0, d: 1, val: 0 }
    },

    // Fraction Studio Specific State
    fractions: {
      // Available inventory definition
      palette: [
        { label: '1/1', n: 1, d: 1, mm: 84.0, cls: 'frac-1-1' },
        { label: '1/2', n: 1, d: 2, mm: 42.0, cls: 'frac-1-2' },
        { label: '1/3', n: 1, d: 3, mm: 28.0, cls: 'frac-1-3' },
        { label: '1/4', n: 1, d: 4, mm: 21.0, cls: 'frac-1-4' },
        { label: '1/5', n: 1, d: 5, mm: 16.8, cls: 'frac-1-5' },
        { label: '1/6', n: 1, d: 6, mm: 14.0, cls: 'frac-1-6' },
        { label: '1/8', n: 1, d: 8, mm: 10.5, cls: 'frac-1-8' },
        { label: '1/10', n: 1, d: 10, mm: 8.4, cls: 'frac-1-10' },
        { label: '1/12', n: 1, d: 12, mm: 7.0, cls: 'frac-1-12' }
      ],
      staging: [],     // Blocks currently in user's staging builder
      comparatorX: [], // Blocks matching Reg X
      comparatorY: [], // Blocks matching Reg Y
      targetAnswer: [],// Blocks student builds to verify equivalence
      laserHeight: 0   // Current height of comparison in mm
    },

    // Place-Value Specific State
    placeValue: {
      // Active columns: [hundreds, tens, ones, tenths, hundredths, thousandths]
      stagingCounts: {
        100: 0,
        10: 0,
        1: 0,
        0.1: 0,
        0.01: 0,
        0.001: 0
      },
      hasCarry: false,
      regroupNote: ''
    },

    // Challenge & Verification Engine
    challengeIndex: 0,
    challenges: [
      {
        type: 'fraction',
        prompt: 'Build 1/2 and 1/4 onto the stack, then execute [+]. Verify the equivalent tower!',
        targetN: 3,
        targetD: 4,
        targetMm: 63.0
      },
      {
        type: 'fraction',
        prompt: 'Master common denominators: Compute 1/3 + 1/6 on the stack. What single block matches?',
        targetN: 1,
        targetD: 2,
        targetMm: 42.0
      },
      {
        type: 'fraction',
        prompt: 'Subtraction on the stack: Build 3/4 and 1/2, then execute [-].',
        targetN: 1,
        targetD: 4,
        targetMm: 21.0
      },
      {
        type: 'placevalue',
        prompt: 'Place Value Addition: Build 24.5 and 13.7. Execute [+] and verify decimal regrouping!',
        targetVal: 38.2
      }
    ]
  };

  // --- 4. RPN Stack Operations ---
  function rpnPush(n, d, val) {
    if (val === undefined) val = n / d;
    state.stack.t = { ...state.stack.z };
    state.stack.z = { ...state.stack.y };
    state.stack.y = { ...state.stack.x };
    state.stack.x = { n, d, val };
    playPush();
    renderAll();
  }

  function rpnOp(operator) {
    const x = state.stack.x;
    const y = state.stack.y;
    let resN = 0, resD = 1, resVal = 0;

    if (operator === '+') {
      resN = y.n * x.d + x.n * y.d;
      resD = y.d * x.d;
      resVal = y.val + x.val;
    } else if (operator === '-') {
      resN = y.n * x.d - x.n * y.d;
      resD = y.d * x.d;
      resVal = y.val - x.val;
    } else if (operator === '×') {
      resN = y.n * x.n;
      resD = y.d * x.d;
      resVal = y.val * x.val;
    } else if (operator === '÷') {
      if (x.val !== 0) {
        resN = y.n * x.d;
        resD = y.d * x.n;
        resVal = y.val / x.val;
      }
    }

    const simp = simplifyFrac(resN, resD);
    state.stack.x = { n: simp.n, d: simp.d, val: resVal };
    state.stack.y = { ...state.stack.z };
    state.stack.z = { ...state.stack.t };
    state.stack.t = { n: 0, d: 1, val: 0 };

    playOp();
    updateLaserAlignment();
    renderAll();
  }

  function rpnSwap() {
    const temp = { ...state.stack.x };
    state.stack.x = { ...state.stack.y };
    state.stack.y = temp;
    playClick();
    renderAll();
  }

  function rpnDrop() {
    state.stack.x = { ...state.stack.y };
    state.stack.y = { ...state.stack.z };
    state.stack.z = { ...state.stack.t };
    state.stack.t = { n: 0, d: 1, val: 0 };
    playClick();
    renderAll();
  }

  function rpnClear() {
    state.stack.t = { n: 0, d: 1, val: 0 };
    state.stack.z = { n: 0, d: 1, val: 0 };
    state.stack.y = { n: 0, d: 1, val: 0 };
    state.stack.x = { n: 0, d: 1, val: 0 };
    playClick();
    renderAll();
  }

  // --- 5. Fraction Studio Logic ---
  function addStagingFraction(blockSpec) {
    state.fractions.staging.push({ ...blockSpec, id: Date.now() + Math.random() });
    playClick();
    renderFractions();
  }

  function removeTopStagingFraction() {
    if (state.fractions.staging.length > 0) {
      state.fractions.staging.pop();
      playClick();
      renderFractions();
    }
  }

  function clearStagingFractions() {
    state.fractions.staging = [];
    playClick();
    renderFractions();
  }

  function pushStagedFractionToStack() {
    if (state.fractions.staging.length === 0) return;

    // Calculate total rational sum
    let totalN = 0;
    let totalD = 1;
    let totalVal = 0;

    state.fractions.staging.forEach(b => {
      totalN = totalN * b.d + b.n * totalD;
      totalD = totalD * b.d;
      totalVal += b.n / b.d;
    });

    const simp = simplifyFrac(totalN, totalD);

    // If Reg X already has a value, copy staging to comparator Y before pushing new X
    state.fractions.comparatorY = [...state.fractions.comparatorX];
    state.fractions.comparatorX = [...state.fractions.staging];

    rpnPush(simp.n, simp.d, totalVal);
    state.fractions.staging = [];
    renderFractions();
  }

  function addTargetFraction(blockSpec) {
    state.fractions.targetAnswer.push({ ...blockSpec, id: Date.now() + Math.random() });
    playClick();
    renderFractions();
    checkEquivalence();
  }

  function clearTargetFractions() {
    state.fractions.targetAnswer = [];
    playClick();
    renderFractions();
    checkEquivalence();
  }

  function updateLaserAlignment() {
    const regX = state.stack.x;
    if (regX.val > 0) {
      state.fractions.laserHeight = regX.val * 84.0; // 84.0mm = 1 whole
    } else {
      state.fractions.laserHeight = 0;
    }
  }

  function checkEquivalence() {
    const regX = state.stack.x;
    let targetTotalVal = 0;
    state.fractions.targetAnswer.forEach(b => targetTotalVal += b.n / b.d);

    const diff = Math.abs(regX.val - targetTotalVal);
    const laserEl = document.getElementById('vlab-laser-line');
    const statusEl = document.getElementById('vlab-check-status');

    if (laserEl) {
      if (regX.val > 0) {
        const hPx = Math.min(280, regX.val * 84.0 * 2.8);
        laserEl.style.bottom = `${hPx + 4}px`;
      }
    }

    if (regX.val > 0 && diff < 0.001) {
      if (laserEl) laserEl.classList.add('active');
      if (statusEl) {
        statusEl.textContent = '🎉 EXACT MATCH // PROVED!';
        statusEl.style.color = '#10B981';
      }
      playSuccess();
    } else {
      if (laserEl) laserEl.classList.remove('active');
      if (statusEl) {
        if (targetTotalVal === 0 && regX.val === 0) {
          statusEl.textContent = 'Awaiting verification tower...';
          statusEl.style.color = '#94A3B8';
        } else if (regX.val === 0) {
          statusEl.textContent = 'Push staged fraction to Stack to set datum line.';
          statusEl.style.color = '#94A3B8';
        } else if (targetTotalVal === 0) {
          statusEl.textContent = `Datum line at ${(regX.val * 84.0).toFixed(1)} mm. Build verification tower to match.`;
          statusEl.style.color = '#38BDF8';
        } else {
          const deltaMm = (regX.val - targetTotalVal) * 84.0;
          statusEl.textContent = `Δ Height: ${deltaMm > 0 ? '+' : ''}${deltaMm.toFixed(1)} mm`;
          statusEl.style.color = '#F59E0B';
        }
      }
    }
  }

  // --- 6. Place-Value Studio Logic ---
  function changePvCount(colKey, delta) {
    const val = parseFloat(colKey);
    const curr = state.placeValue.stagingCounts[val] || 0;
    const next = Math.max(0, curr + delta);
    state.placeValue.stagingCounts[val] = next;
    playClick();

    // Check carry / regroup conditions
    checkPvRegroup();
    renderPlaceValue();
  }

  function checkPvRegroup() {
    let hasExceed = false;
    let note = '';
    const counts = state.placeValue.stagingCounts;

    for (let key in counts) {
      if (counts[key] >= 10) {
        hasExceed = true;
        const numVal = parseFloat(key);
        const nextVal = (numVal * 10).toFixed(3);
        note = `⚠️ ${counts[key]} units in [${key}] column! Stack a [+1] Carry Token into [${parseFloat(nextVal)}]!`;
        break;
      }
    }
    state.placeValue.hasCarry = hasExceed;
    state.placeValue.regroupNote = note;
  }

  function autoRegroupPv() {
    const counts = state.placeValue.stagingCounts;
    const keys = [0.001, 0.01, 0.1, 1, 10, 100];
    let changed = false;

    keys.forEach((k, idx) => {
      if (counts[k] >= 10) {
        const carryOver = Math.floor(counts[k] / 10);
        counts[k] = counts[k] % 10;
        if (idx + 1 < keys.length) {
          const nextK = keys[idx + 1];
          counts[nextK] = (counts[nextK] || 0) + carryOver;
          changed = true;
        }
      }
    });

    if (changed) {
      playSuccess();
      checkPvRegroup();
      renderPlaceValue();
    }
  }

  function getPvTotal() {
    const counts = state.placeValue.stagingCounts;
    let total = 0;
    for (let k in counts) {
      total += parseFloat(k) * counts[k];
    }
    return Math.round(total * 1000) / 1000;
  }

  function pushPvToStack() {
    const total = getPvTotal();
    if (total === 0) return;
    rpnPush(Math.round(total * 1000), 1000, total);

    // Clear staging counts
    for (let k in state.placeValue.stagingCounts) {
      state.placeValue.stagingCounts[k] = 0;
    }
    checkPvRegroup();
    renderPlaceValue();
  }

  // --- 7. Fullscreen Toggle ---
  function toggleFullscreen() {
    const container = document.getElementById('vlab-main-container');
    if (!container) return;

    if (!document.fullscreenElement) {
      if (container.requestFullscreen) container.requestFullscreen();
      else if (container.webkitRequestFullscreen) container.webkitRequestFullscreen();
    } else {
      if (document.exitFullscreen) document.exitFullscreen();
    }
  }

  // --- 8. UI Rendering Subroutines ---
  function renderStackLcd() {
    const regIds = ['t', 'z', 'y', 'x'];
    regIds.forEach(id => {
      const el = document.getElementById(`vlab-reg-${id}`);
      if (!el) return;
      const reg = state.stack[id];
      if (state.fdisp && reg.d !== 1 && reg.n !== 0) {
        el.textContent = `${formatFrac(reg.n, reg.d)} (${reg.val.toFixed(3)})`;
      } else {
        el.textContent = reg.val.toFixed(4);
      }
    });
  }

  function renderFractions() {
    // 1. Render Palette
    const rackEl = document.getElementById('vlab-frac-rack');
    if (rackEl && rackEl.children.length === 0) {
      rackEl.innerHTML = '';
      state.fractions.palette.forEach(p => {
        const btn = document.createElement('div');
        btn.className = 'vlab-block-btn';
        btn.innerHTML = `
          <div style="display:flex; align-items:center;">
            <span class="vlab-block-chip" style="background:var(--col);"></span>
            <span class="vlab-block-label">${p.label}</span>
          </div>
          <span class="vlab-block-spec">${p.mm.toFixed(1)} mm</span>
        `;
        btn.onclick = () => addStagingFraction(p);
        rackEl.appendChild(btn);
      });
    }

    // 2. Render Staging Bay Column
    const stageCol = document.getElementById('vlab-col-stage');
    if (stageCol) {
      stageCol.innerHTML = '';
      let sumN = 0, sumD = 1, sumVal = 0, sumMm = 0;

      state.fractions.staging.forEach(b => {
        sumN = sumN * b.d + b.n * sumD;
        sumD = sumD * b.d;
        sumVal += b.n / b.d;
        sumMm += b.mm;

        const blk = document.createElement('div');
        blk.className = `frac-block-2d ${b.cls}`;
        // Scale: 1mm = 2.8px
        blk.style.height = `${Math.max(16, b.mm * 2.8)}px`;
        blk.setAttribute('data-height', `${b.mm.toFixed(1)}mm`);
        blk.textContent = b.label;
        stageCol.appendChild(blk);
      });

      // Update Staging Readout
      const valEl = document.getElementById('vlab-staged-val');
      const metaEl = document.getElementById('vlab-staged-meta');
      if (valEl) valEl.textContent = state.fractions.staging.length > 0 ? formatFrac(sumN, sumD) : '0';
      if (metaEl) metaEl.textContent = `Height: ${sumMm.toFixed(1)} mm • Val: ${sumVal.toFixed(3)}`;
    }

    // 3. Render Visual Stack Tower (Result of Register X)
    const resultCol = document.getElementById('vlab-col-stack-x');
    if (resultCol) {
      resultCol.innerHTML = '';
      const regX = state.stack.x;
      if (regX.val > 0) {
        // Display representation
        const blk = document.createElement('div');
        blk.className = 'frac-block-2d frac-1-2';
        blk.style.background = '#38BDF8';
        blk.style.border = '1px solid #FFFFFF';
        blk.style.height = `${Math.min(280, regX.val * 84.0 * 2.8)}px`;
        blk.setAttribute('data-height', `${(regX.val * 84.0).toFixed(1)}mm`);
        blk.textContent = formatFrac(regX.n, regX.d);
        resultCol.appendChild(blk);
      }
    }

    // 4. Render Target Answer Column
    const targetCol = document.getElementById('vlab-col-target');
    if (targetCol) {
      targetCol.innerHTML = '';
      let targetMm = 0;
      state.fractions.targetAnswer.forEach(b => {
        targetMm += b.mm;
        const blk = document.createElement('div');
        blk.className = `frac-block-2d ${b.cls}`;
        blk.style.height = `${Math.max(16, b.mm * 2.8)}px`;
        blk.setAttribute('data-height', `${b.mm.toFixed(1)}mm`);
        blk.textContent = b.label;
        targetCol.appendChild(blk);
      });
    }

    // 5. Update Laser Datum Line & Equivalence Status
    checkEquivalence();
  }

  function renderPlaceValue() {
    const keys = [100, 10, 1, 0.1, 0.01, 0.001];
    keys.forEach(k => {
      const socket = document.getElementById(`pv-socket-${k}`);
      if (!socket) return;
      socket.innerHTML = '';
      const count = state.placeValue.stagingCounts[k] || 0;

      if (count >= 10) {
        socket.classList.add('has-carry');
      } else {
        socket.classList.remove('has-carry');
      }

      for (let i = 0; i < count; i++) {
        const chip = document.createElement('div');
        chip.className = `pv-chip pv-chip-${k}`;
        chip.textContent = k >= 1 ? `${k}` : `${k}`.replace('0.', '.');
        socket.appendChild(chip);
      }
    });

    // Update Staged Value readout
    const valEl = document.getElementById('pv-total-val');
    if (valEl) valEl.textContent = getPvTotal().toFixed(3);

    // Update Regroup Note Alert
    const noteEl = document.getElementById('pv-regroup-alert');
    if (noteEl) {
      if (state.placeValue.hasCarry) {
        noteEl.textContent = state.placeValue.regroupNote;
        noteEl.style.display = 'block';
      } else {
        noteEl.style.display = 'none';
      }
    }
  }

  function renderAll() {
    renderStackLcd();
    if (state.activeTab === 'fractions') {
      renderFractions();
    } else {
      renderPlaceValue();
    }
  }

  // --- 9. DOM Initialization ---
  function initLab() {
    const container = document.getElementById('vlab-main-container');
    if (!container) return;

    // Attach Tab Switching
    const tabFrac = document.getElementById('vlab-tab-fractions');
    const tabPv = document.getElementById('vlab-tab-placevalue');
    const viewFrac = document.getElementById('vlab-view-fractions');
    const viewPv = document.getElementById('vlab-view-placevalue');

    if (tabFrac && tabPv) {
      tabFrac.onclick = () => {
        state.activeTab = 'fractions';
        tabFrac.classList.add('active');
        tabPv.classList.remove('active');
        if (viewFrac) viewFrac.style.display = 'block';
        if (viewPv) viewPv.style.display = 'none';
        playClick();
        renderAll();
      };
      tabPv.onclick = () => {
        state.activeTab = 'placevalue';
        tabPv.classList.add('active');
        tabFrac.classList.remove('active');
        if (viewFrac) viewFrac.style.display = 'none';
        if (viewPv) viewPv.style.display = 'block';
        playClick();
        renderAll();
      };
    }

    // Attach Audio Toggle
    const soundBtn = document.getElementById('vlab-btn-sound');
    if (soundBtn) {
      soundBtn.onclick = () => {
        soundEnabled = !soundEnabled;
        soundBtn.textContent = soundEnabled ? '🔊 AUDIO: ON' : '🔇 AUDIO: OFF';
        if (soundEnabled) playClick();
      };
    }

    // Attach Fullscreen Toggle
    const fsBtn = document.getElementById('vlab-btn-fullscreen');
    if (fsBtn) {
      fsBtn.onclick = toggleFullscreen;
    }

    // Attach Stack Operation Buttons
    const opBtns = document.querySelectorAll('[data-vlab-op]');
    opBtns.forEach(btn => {
      btn.onclick = () => rpnOp(btn.getAttribute('data-vlab-op'));
    });

    const swapBtn = document.getElementById('vlab-btn-swap');
    if (swapBtn) swapBtn.onclick = rpnSwap;

    const dropBtn = document.getElementById('vlab-btn-drop');
    if (dropBtn) dropBtn.onclick = rpnDrop;

    const clxBtn = document.getElementById('vlab-btn-clx');
    if (clxBtn) clxBtn.onclick = rpnClear;

    const fdispBtn = document.getElementById('vlab-btn-fdisp');
    if (fdispBtn) {
      fdispBtn.onclick = () => {
        state.fdisp = !state.fdisp;
        playClick();
        renderStackLcd();
      };
    }

    // Fraction Buttons
    const pushFracBtn = document.getElementById('vlab-btn-push-frac');
    if (pushFracBtn) pushFracBtn.onclick = pushStagedFractionToStack;

    const clearFracBtn = document.getElementById('vlab-btn-clear-frac');
    if (clearFracBtn) clearFracBtn.onclick = clearStagingFractions;

    const dropFracBtn = document.getElementById('vlab-btn-drop-frac');
    if (dropFracBtn) dropFracBtn.onclick = removeTopStagingFraction;

    const checkFracBtn = document.getElementById('vlab-btn-check-frac');
    if (checkFracBtn) checkFracBtn.onclick = checkEquivalence;

    const clearTargetBtn = document.getElementById('vlab-btn-clear-target');
    if (clearTargetBtn) clearTargetBtn.onclick = clearTargetFractions;

    // Place Value Buttons
    const pushPvBtn = document.getElementById('pv-btn-push');
    if (pushPvBtn) pushPvBtn.onclick = pushPvToStack;

    const regroupBtn = document.getElementById('pv-btn-regroup');
    if (regroupBtn) regroupBtn.onclick = autoRegroupPv;

    // Place value stepper event listeners
    const pvSteps = document.querySelectorAll('[data-pv-col]');
    pvSteps.forEach(btn => {
      btn.onclick = () => {
        const col = btn.getAttribute('data-pv-col');
        const delta = parseInt(btn.getAttribute('data-pv-delta'), 10);
        changePvCount(col, delta);
      };
    });

    // Render Initial State
    renderAll();
  }

  // Initialize on DOMContentLoaded or immediate if already ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLab);
  } else {
    initLab();
  }

  // Export to window for inline calls if necessary
  window.StackCalcLab = {
    state: state,
    addFraction: addStagingFraction,
    clearStagingFractions: clearStagingFractions,
    addTargetFraction: addTargetFraction,
    clearTargetFractions: clearTargetFractions,
    pushFraction: pushStagedFractionToStack,
    changePvCount: changePvCount,
    autoRegroupPv: autoRegroupPv,
    getPvTotal: getPvTotal,
    pushPvToStack: pushPvToStack,
    op: rpnOp,
    clearStack: rpnClear,
    toggleFullscreen: toggleFullscreen
  };
})();
