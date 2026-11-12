/**
 * =========================================================================
 * STACKCALC 2D VIRTUAL MANIPULATIVES LAB ENGINE
 * Authentic Concrete-Representational-Abstract (CRA) Classroom Simulator
 * Fractions (FRAC-01), Place-Value Trays (PLACE-01), Prime Blocks (PRIME-01)
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

  // --- 2. Rational Math & Prime Helpers ---
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

  function lcm(a, b) {
    if (a === 0 || b === 0) return 0;
    return Math.abs(Math.round(a * b)) / gcd(a, b);
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

  function getPrimeProduct(list) {
    if (!list || list.length === 0) return 0;
    return list.reduce((acc, p) => acc * p, 1);
  }

  const primeLookupMm = {
    2: 18.0, 3: 28.5, 5: 41.8, 7: 50.7, 11: 62.4, 13: 66.8, 17: 73.6, 19: 76.5, 23: 81.3
  };

  const primeLookupColors = {
    2: '#0284C7', 3: '#10B981', 5: '#F59E0B', 7: '#8B5CF6',
    11: '#EC4899', 13: '#06B6D4', 17: '#E11D48', 19: '#F97316', 23: '#64748B'
  };

  function getPrimeMm(list) {
    if (!list || list.length === 0) return 0;
    return list.reduce((acc, p) => acc + (primeLookupMm[p] || (15 * Math.log2(p))), 0);
  }

  function formatPrimeFormula(list) {
    if (!list || list.length === 0) return '0';
    const sorted = [...list].sort((a, b) => a - b);
    const expanded = sorted.join(' × ');
    const counts = {};
    sorted.forEach(p => { counts[p] = (counts[p] || 0) + 1; });
    const hasExponents = Object.values(counts).some(c => c > 1);
    if (!hasExponents) {
      return expanded;
    }
    const expParts = Object.keys(counts).map(Number).sort((a, b) => a - b).map(p => {
      return counts[p] > 1 ? `${p}<sup>${counts[p]}</sup>` : `${p}`;
    });
    return `${expanded} &nbsp;<span style="color:#94A3B8; font-weight:normal;">(${expParts.join(' × ')})</span>`;
  }

  function getPrimeFactorsList(num) {
    let n = Math.abs(Math.round(num));
    if (n <= 1) return [];
    const factors = [];
    let d = 2;
    while (d * d <= n) {
      while (n % d === 0) {
        factors.push(d);
        n = Math.floor(n / d);
      }
      d++;
    }
    if (n > 1) factors.push(n);
    return factors;
  }

  function calcTowerSum(blocks) {
    if (!blocks || blocks.length === 0) {
      return { n: 0, d: 1, val: 0, mm: 0 };
    }
    let totalN = 0;
    let totalD = 1;
    let totalMm = 0;
    blocks.forEach(b => {
      totalN = totalN * b.d + b.n * totalD;
      totalD = totalD * b.d;
      totalMm += b.mm;
    });
    const simp = simplifyFrac(totalN, totalD);
    return {
      n: simp.n,
      d: simp.d,
      val: simp.n / simp.d,
      mm: totalMm
    };
  }

  // --- 3. Core State Architecture ---
  const state = {
    activeTab: 'fractions', // 'fractions' | 'placevalue' | 'primes'
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
      stackX: [],       // Blocks currently in Register X (Active Entry / Tower)
      stackY: [],       // Blocks currently in Register Y (The Stack)
      targetAnswer: [], // Blocks student builds to verify equivalence
      laserHeight: 0,   // Current datum height in mm
      isEquivalent: false,

      // Compatibility getters
      get staging() { return this.stackX; },
      set staging(v) { this.stackX = v; },
      get comparatorY() { return this.stackY; },
      set comparatorY(v) { this.stackY = v; }
    },

    // Place-Value Specific State
    placeValue: {
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

    // Prime Factor Studio Specific State (PRIME-01)
    primes: {
      palette: [
        { p: 2, label: '[2]', mm: 18.0, color: '#0284C7' },
        { p: 3, label: '[3]', mm: 28.5, color: '#10B981' },
        { p: 5, label: '[5]', mm: 41.8, color: '#F59E0B' },
        { p: 7, label: '[7]', mm: 50.7, color: '#8B5CF6' },
        { p: 11, label: '[11]', mm: 62.4, color: '#EC4899' },
        { p: 13, label: '[13]', mm: 66.8, color: '#06B6D4' },
        { p: 17, label: '[17]', mm: 73.6, color: '#E11D48' },
        { p: 19, label: '[19]', mm: 76.5, color: '#F97316' },
        { p: 23, label: '[23]', mm: 81.3, color: '#64748B' }
      ],
      stackX: [],       // Active prime blocks in Register X (Vertical Tower)
      stackY: [],       // Pushed prime blocks in Register Y (Vertical Tower)
      targetPrimes: [], // Comparison / Decomposed primes

      // Compatibility getters
      get staging() { return this.stackX; },
      set staging(v) { this.stackX = v; },
      get stagingProduct() { return getPrimeProduct(this.stackX); },
      get targetDecomp() { return this.targetPrimes; }
    }
  };

  // --- 4. RPN Calculator Stack Operations ---
  function rpnPushRaw(n, d, val) {
    if (val === undefined) val = n / d;
    state.stack.t = { ...state.stack.z };
    state.stack.z = { ...state.stack.y };
    state.stack.y = { ...state.stack.x };
    state.stack.x = { n, d, val };
    playPush();
  }

  function rpnClear() {
    state.stack.x = { n: 0, d: 1, val: 0 };
    if (state.activeTab === 'fractions') {
      state.fractions.stackX = [];
    } else if (state.activeTab === 'primes') {
      state.primes.stackX = [];
    } else if (state.activeTab === 'placevalue') {
      for (let k in state.placeValue.stagingCounts) {
        state.placeValue.stagingCounts[k] = 0;
      }
      checkPvRegroup();
    }
    playClick();
    renderAll();
  }

  function rpnDrop() {
    state.stack.x = { ...state.stack.y };
    state.stack.y = { ...state.stack.z };
    state.stack.z = { ...state.stack.t };
    state.stack.t = { n: 0, d: 1, val: 0 };
    if (state.activeTab === 'fractions') {
      state.fractions.stackX = [...state.fractions.stackY];
      state.fractions.stackY = [];
    } else if (state.activeTab === 'primes') {
      state.primes.stackX = [...state.primes.stackY];
      state.primes.stackY = [];
    }
    playClick();
    renderAll();
  }

  function rpnSwap() {
    const tempVal = { ...state.stack.x };
    state.stack.x = { ...state.stack.y };
    state.stack.y = tempVal;

    if (state.activeTab === 'fractions') {
      const tempBlocks = [...state.fractions.stackX];
      state.fractions.stackX = [...state.fractions.stackY];
      state.fractions.stackY = tempBlocks;
    } else if (state.activeTab === 'primes') {
      const tempPrimes = [...state.primes.stackX];
      state.primes.stackX = [...state.primes.stackY];
      state.primes.stackY = tempPrimes;
    }
    playClick();
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
      // In Fraction mode: combine physical blocks from Y and X into X!
      if (state.activeTab === 'fractions') {
        state.fractions.stackX = [...state.fractions.stackY, ...state.fractions.stackX];
        state.fractions.stackY = [];
      }
    } else if (operator === '-') {
      resN = y.n * x.d - x.n * y.d;
      resD = y.d * x.d;
      resVal = y.val - x.val;
      if (state.activeTab === 'fractions') {
        state.fractions.stackY = [];
      }
    } else if (operator === '×') {
      resN = y.n * x.n;
      resD = y.d * x.d;
      resVal = y.val * x.val;
      if (state.activeTab === 'fractions') {
        state.fractions.stackY = [];
      } else if (state.activeTab === 'primes') {
        state.primes.stackX = [...state.primes.stackY, ...state.primes.stackX].sort((a, b) => a - b);
        state.primes.stackY = [];
      }
    } else if (operator === '÷') {
      if (x.val !== 0) {
        resN = y.n * x.d;
        resD = y.d * x.n;
        resVal = y.val / x.val;
      }
      if (state.activeTab === 'fractions') {
        state.fractions.stackY = [];
      }
    }

    const simp = simplifyFrac(resN, resD);
    state.stack.x = { n: simp.n, d: simp.d, val: resVal };
    state.stack.y = { ...state.stack.z };
    state.stack.z = { ...state.stack.t };
    state.stack.t = { n: 0, d: 1, val: 0 };

    playOp();
    renderAll();
  }

  // --- 5. Fraction Studio Actions ---
  function addFractionToX(blockSpec) {
    state.fractions.stackX.push({
      ...blockSpec,
      id: Date.now() + Math.random()
    });
    // Immediately update Register X on the LCD!
    const res = calcTowerSum(state.fractions.stackX);
    state.stack.x = { n: res.n, d: res.d, val: res.val };
    playClick();
    renderAll();
  }

  function removeFractionFromX(index) {
    if (index >= 0 && index < state.fractions.stackX.length) {
      state.fractions.stackX.splice(index, 1);
      const res = calcTowerSum(state.fractions.stackX);
      state.stack.x = { n: res.n, d: res.d, val: res.val };
      playClick();
      renderAll();
    }
  }

  function dropTopFractionFromX() {
    if (state.fractions.stackX.length > 0) {
      state.fractions.stackX.pop();
      const res = calcTowerSum(state.fractions.stackX);
      state.stack.x = { n: res.n, d: res.d, val: res.val };
      playClick();
      renderAll();
    }
  }

  function clearFractionX() {
    state.fractions.stackX = [];
    state.stack.x = { n: 0, d: 1, val: 0 };
    playClick();
    renderAll();
  }

  function pushFractionToStack() {
    if (state.fractions.stackX.length === 0 && state.stack.x.val === 0) return;

    // Push stack registers
    state.stack.t = { ...state.stack.z };
    state.stack.z = { ...state.stack.y };
    state.stack.y = { ...state.stack.x };
    state.stack.x = { n: 0, d: 1, val: 0 };

    // Move visual blocks from X into Y
    state.fractions.stackY = [...state.fractions.stackX];
    state.fractions.stackX = [];

    playPush();
    renderAll();
  }

  function addTargetFraction(blockSpec) {
    state.fractions.targetAnswer.push({
      ...blockSpec,
      id: Date.now() + Math.random()
    });
    playClick();
    renderAll();
  }

  function removeTargetFraction(index) {
    if (index >= 0 && index < state.fractions.targetAnswer.length) {
      state.fractions.targetAnswer.splice(index, 1);
      playClick();
      renderAll();
    }
  }

  function clearTargetFractions() {
    state.fractions.targetAnswer = [];
    playClick();
    renderAll();
  }

  // --- 6. Prime Factor Studio Actions ---
  function addPrimeToX(p) {
    state.primes.stackX.push(p);
    const prod = getPrimeProduct(state.primes.stackX);
    // Immediately update Register X on the LCD!
    state.stack.x = { n: prod, d: 1, val: prod };
    playClick();
    renderAll();
  }

  function removePrimeFromX(index) {
    if (index >= 0 && index < state.primes.stackX.length) {
      state.primes.stackX.splice(index, 1);
      const prod = getPrimeProduct(state.primes.stackX);
      state.stack.x = { n: prod, d: 1, val: prod };
      playClick();
      renderAll();
    }
  }

  function dropTopPrimeFromX() {
    if (state.primes.stackX.length > 0) {
      state.primes.stackX.pop();
      const prod = getPrimeProduct(state.primes.stackX);
      state.stack.x = { n: prod, d: 1, val: prod };
      playClick();
      renderAll();
    }
  }

  function clearPrimeX() {
    state.primes.stackX = [];
    state.stack.x = { n: 0, d: 1, val: 0 };
    playClick();
    renderAll();
  }

  function pushPrimeToStack() {
    if (state.primes.stackX.length === 0 && state.stack.x.val === 0) return;

    state.stack.t = { ...state.stack.z };
    state.stack.z = { ...state.stack.y };
    state.stack.y = { ...state.stack.x };
    state.stack.x = { n: 0, d: 1, val: 0 };

    state.primes.stackY = [...state.primes.stackX];
    state.primes.stackX = [];

    playPush();
    renderAll();
  }

  function primeGcd() {
    const yVal = Math.round(state.stack.y.val);
    const xVal = Math.round(state.stack.x.val);
    if (yVal > 0 && xVal > 0) {
      const g = gcd(yVal, xVal);
      const factorsG = getPrimeFactorsList(g);
      state.primes.stackX = factorsG;
      state.primes.stackY = [];
      state.primes.targetPrimes = factorsG;
      state.stack.x = { n: g, d: 1, val: g };
      state.stack.y = { ...state.stack.z };
      state.stack.z = { ...state.stack.t };
      state.stack.t = { n: 0, d: 1, val: 0 };
      playOp();
      renderAll();
    }
  }

  function primeLcm() {
    const yVal = Math.round(state.stack.y.val);
    const xVal = Math.round(state.stack.x.val);
    if (yVal > 0 && xVal > 0) {
      const l = lcm(yVal, xVal);
      const factorsL = getPrimeFactorsList(l);
      state.primes.stackX = factorsL;
      state.primes.stackY = [];
      state.primes.targetPrimes = factorsL;
      state.stack.x = { n: l, d: 1, val: l };
      state.stack.y = { ...state.stack.z };
      state.stack.z = { ...state.stack.t };
      state.stack.t = { n: 0, d: 1, val: 0 };
      playOp();
      renderAll();
    }
  }

  function primeFactorizeX() {
    const xVal = Math.round(state.stack.x.val);
    if (xVal > 1) {
      const factors = getPrimeFactorsList(xVal);
      state.primes.stackX = factors;
      state.primes.targetPrimes = factors;
      playOp();
      renderAll();
    }
  }

  // --- 7. Place-Value Studio Actions ---
  function changePvCount(colKey, delta) {
    const val = parseFloat(colKey);
    const curr = state.placeValue.stagingCounts[val] || 0;
    const next = Math.max(0, curr + delta);
    state.placeValue.stagingCounts[val] = next;

    // Immediately update Register X on the LCD!
    const total = getPvTotal();
    state.stack.x = {
      n: Math.round(total * 1000),
      d: 1000,
      val: total
    };

    playClick();
    checkPvRegroup();
    renderAll();
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
      const total = getPvTotal();
      state.stack.x = {
        n: Math.round(total * 1000),
        d: 1000,
        val: total
      };
      checkPvRegroup();
      renderAll();
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
    if (total === 0 && state.stack.x.val === 0) return;

    state.stack.t = { ...state.stack.z };
    state.stack.z = { ...state.stack.y };
    state.stack.y = { ...state.stack.x };
    state.stack.x = { n: 0, d: 1, val: 0 };

    for (let k in state.placeValue.stagingCounts) {
      state.placeValue.stagingCounts[k] = 0;
    }

    playPush();
    checkPvRegroup();
    renderAll();
  }

  // --- 8. DOM Rendering & UI Presentation ---
  function renderStackLcd() {
    const regT = document.getElementById('vlab-reg-t');
    const regZ = document.getElementById('vlab-reg-z');
    const regY = document.getElementById('vlab-reg-y');
    const regX = document.getElementById('vlab-reg-x');

    const fmt = (item, isRegX) => {
      if (!item) return isRegX ? '0.0000_' : '0.0000';
      if (state.activeTab === 'fractions' && state.fdisp) {
        if (item.val === 0) return isRegX ? '0_' : '0';
        return `${formatFrac(item.n, item.d)} &nbsp;<span style="color:#64748B; font-size:0.7em;">(${item.val.toFixed(4)})</span>${isRegX ? '_' : ''}`;
      } else if (state.activeTab === 'primes') {
        if (item.val === 0) return isRegX ? '0_' : '0';
        const factors = getPrimeFactorsList(item.val);
        const formula = formatPrimeFormula(factors);
        return `${Math.round(item.val)} &nbsp;<span style="color:#64748B; font-size:0.7em;">[${formula}]</span>${isRegX ? '_' : ''}`;
      } else {
        if (item.val === 0) return isRegX ? '0.0000_' : '0.0000';
        return `${item.val.toFixed(4)}${isRegX ? '_' : ''}`;
      }
    };

    if (regT) regT.innerHTML = fmt(state.stack.t, false);
    if (regZ) regZ.innerHTML = fmt(state.stack.z, false);
    if (regY) regY.innerHTML = fmt(state.stack.y, false);
    if (regX) regX.innerHTML = fmt(state.stack.x, true);
  }

  function renderFractions() {
    // 1. Render Column 1: Register Y (The Stack)
    const colY = document.getElementById('vlab-col-stack-y');
    const metaY = document.getElementById('vlab-meta-stack-y');
    if (colY) {
      colY.innerHTML = '';
      if (state.fractions.stackY.length === 0) {
        colY.innerHTML = '<div class="vlab-empty-hint">Stack Y Empty<br>(Press [ENTER] to push)</div>';
        if (metaY) metaY.textContent = 'Y: 0 (0.0 mm)';
      } else {
        const sumY = calcTowerSum(state.fractions.stackY);
        state.fractions.stackY.forEach((b) => {
          const blk = document.createElement('div');
          blk.className = `frac-block-2d ${b.cls}`;
          blk.style.height = `${Math.max(18, b.mm * 2.8)}px`;
          blk.setAttribute('data-height', `${b.mm.toFixed(1)}mm`);
          blk.textContent = b.label;
          colY.appendChild(blk);
        });
        if (metaY) metaY.textContent = `Y: ${formatFrac(sumY.n, sumY.d)} (${sumY.mm.toFixed(1)} mm)`;
      }
    }

    // 2. Render Column 2: Register X (Active Entry / Tower)
    // Support both id 'vlab-col-stage' and 'vlab-col-stack-x' for compatibility
    const colX = document.getElementById('vlab-col-stack-x') || document.getElementById('vlab-col-stage');
    const metaX = document.getElementById('vlab-meta-stack-x') || document.getElementById('vlab-staged-val');
    const metaXSub = document.getElementById('vlab-staged-meta');
    if (colX) {
      colX.innerHTML = '';
      if (state.fractions.stackX.length === 0) {
        colX.innerHTML = '<div class="vlab-empty-hint">Entry X Empty<br>(Tap blocks to stack)</div>';
        if (metaX) metaX.textContent = '0';
        if (metaXSub) metaXSub.textContent = 'Height: 0.0 mm • Val: 0.000';
      } else {
        const sumX = calcTowerSum(state.fractions.stackX);
        state.fractions.stackX.forEach((b, idx) => {
          const blk = document.createElement('div');
          blk.className = `frac-block-2d ${b.cls} removable`;
          blk.style.height = `${Math.max(18, b.mm * 2.8)}px`;
          blk.setAttribute('data-height', `${b.mm.toFixed(1)}mm`);
          blk.setAttribute('title', 'Click to remove this block');
          blk.textContent = b.label;
          blk.onclick = (e) => {
            e.stopPropagation();
            removeFractionFromX(idx);
          };
          colX.appendChild(blk);
        });
        if (metaX) metaX.textContent = formatFrac(sumX.n, sumX.d);
        if (metaXSub) metaXSub.textContent = `Height: ${sumX.mm.toFixed(1)} mm • Val: ${sumX.val.toFixed(3)}`;
      }
    }

    // 3. Render Column 3: Verification Target
    const colTarget = document.getElementById('vlab-col-target');
    const metaTarget = document.getElementById('vlab-meta-target');
    if (colTarget) {
      colTarget.innerHTML = '';
      if (state.fractions.targetAnswer.length === 0) {
        colTarget.innerHTML = '<div class="vlab-empty-hint">Target Empty<br>(Build comparison)</div>';
        if (metaTarget) metaTarget.textContent = 'Target: 0 mm';
      } else {
        const sumT = calcTowerSum(state.fractions.targetAnswer);
        state.fractions.targetAnswer.forEach((b, idx) => {
          const blk = document.createElement('div');
          blk.className = `frac-block-2d ${b.cls} removable`;
          blk.style.height = `${Math.max(18, b.mm * 2.8)}px`;
          blk.setAttribute('data-height', `${b.mm.toFixed(1)}mm`);
          blk.setAttribute('title', 'Click to remove this block');
          blk.textContent = b.label;
          blk.onclick = (e) => {
            e.stopPropagation();
            removeTargetFraction(idx);
          };
          colTarget.appendChild(blk);
        });
        if (metaTarget) metaTarget.textContent = `Target: ${formatFrac(sumT.n, sumT.d)} (${sumT.mm.toFixed(1)} mm)`;
      }
    }

    // 4. Update Equivalence Datum Laser Line
    checkEquivalence();
  }

  function checkEquivalence() {
    const sumX = calcTowerSum(state.fractions.stackX);
    const sumT = calcTowerSum(state.fractions.targetAnswer);
    const laserEl = document.getElementById('vlab-laser-line');
    const statusEl = document.getElementById('vlab-check-status');

    const effectiveHeightX = sumX.mm > 0 ? sumX.mm : (state.stack.x.val > 0 ? state.stack.x.val * 84.0 : 0);
    const effectiveHeightT = sumT.mm;

    if (laserEl) {
      if (effectiveHeightX > 0) {
        const hPx = Math.min(300, effectiveHeightX * 2.8);
        laserEl.style.bottom = `${hPx + 4}px`;
        laserEl.style.display = 'block';
      } else {
        laserEl.style.display = 'none';
      }
    }

    if (statusEl) {
      if (effectiveHeightX === 0 && effectiveHeightT === 0) {
        statusEl.textContent = 'Awaiting block entry...';
        statusEl.style.color = '#94A3B8';
        if (laserEl) laserEl.classList.remove('active');
      } else if (effectiveHeightX > 0 && effectiveHeightT === 0) {
        statusEl.textContent = `Datum line set at ${effectiveHeightX.toFixed(1)} mm. Build verification tower to match.`;
        statusEl.style.color = '#38BDF8';
        if (laserEl) laserEl.classList.remove('active');
      } else if (Math.abs(effectiveHeightX - effectiveHeightT) < 0.2 && effectiveHeightX > 0) {
        statusEl.innerHTML = '🎉 <strong>EXACT MATCH // PROVED!</strong>';
        statusEl.style.color = '#10B981';
        if (laserEl) laserEl.classList.add('active');
        playSuccess();
      } else {
        const delta = effectiveHeightX - effectiveHeightT;
        statusEl.textContent = `Δ Height: ${delta > 0 ? '+' : ''}${delta.toFixed(1)} mm (Tower difference)`;
        statusEl.style.color = '#F59E0B';
        if (laserEl) laserEl.classList.remove('active');
      }
    }
  }

  function renderPrimes() {
    // 1. Column 1: Prime Register Y (The Stack)
    const colY = document.getElementById('vlab-prime-stack-y');
    const metaY = document.getElementById('vlab-prime-meta-y');
    if (colY) {
      colY.innerHTML = '';
      if (state.primes.stackY.length === 0) {
        colY.innerHTML = '<div class="vlab-empty-hint">Prime Stack Y Empty<br>(Press [ENTER] to push)</div>';
        if (metaY) metaY.textContent = 'Y: 0';
      } else {
        const prodY = getPrimeProduct(state.primes.stackY);
        const mmY = getPrimeMm(state.primes.stackY);
        state.primes.stackY.forEach((p) => {
          const blk = document.createElement('div');
          blk.className = 'prime-block-2d-vert';
          const mm = primeLookupMm[p] || 20;
          blk.style.height = `${Math.max(22, mm * 2.2)}px`;
          blk.style.backgroundColor = primeLookupColors[p] || '#0284C7';
          blk.innerHTML = `<span>[${p}]</span><span>${mm.toFixed(1)}mm</span>`;
          colY.appendChild(blk);
        });
        if (metaY) metaY.textContent = `Y: ${prodY} (Log: ${mmY.toFixed(1)}mm)`;
      }
    }

    // 2. Column 2: Prime Register X (Active Entry / Tower)
    // Support both 'vlab-prime-stack-x' and 'vlab-prime-stage'
    const colX = document.getElementById('vlab-prime-stack-x') || document.getElementById('vlab-prime-stage');
    const valEl = document.getElementById('vlab-prime-val');
    const formulaEl = document.getElementById('vlab-prime-formula');
    const metaEl = document.getElementById('vlab-prime-meta');

    const prodX = getPrimeProduct(state.primes.stackX);
    const mmX = getPrimeMm(state.primes.stackX);

    if (colX) {
      colX.innerHTML = '';
      if (state.primes.stackX.length === 0) {
        colX.innerHTML = '<div class="vlab-empty-hint">Prime Entry X Empty<br>(Tap prime blocks below)</div>';
      } else {
        state.primes.stackX.forEach((p, idx) => {
          const blk = document.createElement('div');
          blk.className = 'prime-block-2d-vert removable';
          const mm = primeLookupMm[p] || 20;
          blk.style.height = `${Math.max(22, mm * 2.2)}px`;
          blk.style.backgroundColor = primeLookupColors[p] || '#0284C7';
          blk.setAttribute('title', 'Click to remove this prime block');
          blk.innerHTML = `<span>[${p}]</span><span>${mm.toFixed(1)}mm</span>`;
          blk.onclick = (e) => {
            e.stopPropagation();
            removePrimeFromX(idx);
          };
          colX.appendChild(blk);
        });
      }
    }

    if (valEl) valEl.textContent = prodX > 0 ? `${prodX}` : '0';
    if (formulaEl) formulaEl.innerHTML = prodX > 0 ? formatPrimeFormula(state.primes.stackX) : 'No factors selected';
    if (metaEl) metaEl.textContent = `Logarithmic Height: ${mmX.toFixed(1)} mm • ${state.primes.stackX.length} Factors`;

    // 3. Column 3: Prime Target / Decomposed Tower
    const colTarget = document.getElementById('vlab-prime-target');
    if (colTarget) {
      colTarget.innerHTML = '';
      if (state.primes.targetPrimes.length === 0) {
        colTarget.innerHTML = '<div class="vlab-empty-hint">Target Tower Empty<br>(Press [FACT] on Reg X)</div>';
      } else {
        state.primes.targetPrimes.forEach((p) => {
          const blk = document.createElement('div');
          blk.className = 'prime-block-2d-vert';
          const mm = primeLookupMm[p] || 20;
          blk.style.height = `${Math.max(22, mm * 2.2)}px`;
          blk.style.backgroundColor = primeLookupColors[p] || '#10B981';
          blk.innerHTML = `<span>[${p}]</span><span>${mm.toFixed(1)}mm</span>`;
          colTarget.appendChild(blk);
        });
      }
    }
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

    const valEl = document.getElementById('pv-total-val');
    if (valEl) valEl.textContent = getPvTotal().toFixed(3);

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
    } else if (state.activeTab === 'placevalue') {
      renderPlaceValue();
    } else if (state.activeTab === 'primes') {
      renderPrimes();
    }
  }

  function toggleFullscreen() {
    const container = document.getElementById('vlab-main-container');
    if (!container) return;

    if (!document.fullscreenElement) {
      if (container.requestFullscreen) container.requestFullscreen();
      else if (container.webkitRequestFullscreen) container.webkitRequestFullscreen();
    } else {
      if (document.exitFullscreen) document.exitFullscreen();
      else if (document.webkitExitFullscreen) document.webkitExitFullscreen();
    }
  }

  function setActiveTab(tab) {
    state.activeTab = tab;
    const tabFrac = document.getElementById('vlab-tab-fractions');
    const tabPv = document.getElementById('vlab-tab-placevalue');
    const tabPrimes = document.getElementById('vlab-tab-primes');

    const viewFrac = document.getElementById('vlab-view-fractions');
    const viewPv = document.getElementById('vlab-view-placevalue');
    const viewPrimes = document.getElementById('vlab-view-primes');

    [tabFrac, tabPv, tabPrimes].forEach(t => t && t.classList.remove('active'));
    [viewFrac, viewPv, viewPrimes].forEach(v => v && (v.style.display = 'none'));

    if (tab === 'fractions') {
      if (tabFrac) tabFrac.classList.add('active');
      if (viewFrac) viewFrac.style.display = 'block';
    } else if (tab === 'placevalue') {
      if (tabPv) tabPv.classList.add('active');
      if (viewPv) viewPv.style.display = 'block';
    } else if (tab === 'primes') {
      if (tabPrimes) tabPrimes.classList.add('active');
      if (viewPrimes) viewPrimes.style.display = 'block';
    }
    playClick();
    renderAll();
  }

  // --- 9. DOM Initialization & Event Handlers ---
  function initLab() {
    // Mode Switcher Tabs
    const tabFrac = document.getElementById('vlab-tab-fractions');
    const tabPv = document.getElementById('vlab-tab-placevalue');
    const tabPrimes = document.getElementById('vlab-tab-primes');

    const viewFrac = document.getElementById('vlab-view-fractions');
    const viewPv = document.getElementById('vlab-view-placevalue');
    const viewPrimes = document.getElementById('vlab-view-primes');

    // Auto-detect active tab on standalone pages
    if (!viewFrac) {
      if (viewPrimes) {
        state.activeTab = 'primes';
      } else if (viewPv) {
        state.activeTab = 'placevalue';
      }
    }

    if (tabFrac) tabFrac.onclick = () => setActiveTab('fractions');
    if (tabPv) tabPv.onclick = () => setActiveTab('placevalue');
    if (tabPrimes) tabPrimes.onclick = () => setActiveTab('primes');

    // Telemetry & Control Bar
    const soundBtn = document.getElementById('vlab-btn-sound');
    if (soundBtn) {
      soundBtn.onclick = () => {
        soundEnabled = !soundEnabled;
        state.soundOn = soundEnabled;
        soundBtn.textContent = soundEnabled ? '🔊 AUDIO: ON' : '🔇 AUDIO: OFF';
      };
    }

    const fsBtn = document.getElementById('vlab-btn-fullscreen');
    if (fsBtn) {
      fsBtn.onclick = toggleFullscreen;
    }

    // Fraction Buttons
    const pushFracBtn = document.getElementById('vlab-btn-push-frac');
    if (pushFracBtn) pushFracBtn.onclick = pushFractionToStack;

    const dropFracBtn = document.getElementById('vlab-btn-drop-frac');
    if (dropFracBtn) dropFracBtn.onclick = dropTopFractionFromX;

    const clearFracBtn = document.getElementById('vlab-btn-clear-frac');
    if (clearFracBtn) clearFracBtn.onclick = clearFractionX;

    const checkFracBtn = document.getElementById('vlab-btn-check-frac');
    if (checkFracBtn) checkFracBtn.onclick = checkEquivalence;

    const clearTargetBtn = document.getElementById('vlab-btn-clear-target');
    if (clearTargetBtn) clearTargetBtn.onclick = clearTargetFractions;

    // Operation Keypads (All Tabs)
    const opBtns = document.querySelectorAll('[data-vlab-op]');
    opBtns.forEach(btn => {
      btn.onclick = () => {
        const op = btn.getAttribute('data-vlab-op');
        rpnOp(op);
      };
    });

    const swapBtns = document.querySelectorAll('#vlab-btn-swap');
    swapBtns.forEach(b => { b.onclick = rpnSwap; });

    const dropBtns = document.querySelectorAll('#vlab-btn-drop');
    dropBtns.forEach(b => { b.onclick = rpnDrop; });

    const clxBtns = document.querySelectorAll('#vlab-btn-clx');
    clxBtns.forEach(b => { b.onclick = rpnClear; });

    const fdispBtns = document.querySelectorAll('#vlab-btn-fdisp');
    fdispBtns.forEach(b => {
      b.onclick = () => {
        state.fdisp = !state.fdisp;
        playClick();
        renderAll();
      };
    });

    // Place-Value Buttons
    const pvPushBtn = document.getElementById('pv-btn-push');
    if (pvPushBtn) pvPushBtn.onclick = pushPvToStack;

    const pvRegroupBtn = document.getElementById('pv-btn-regroup');
    if (pvRegroupBtn) pvRegroupBtn.onclick = autoRegroupPv;

    const pvSteps = document.querySelectorAll('[data-pv-col]');
    pvSteps.forEach(btn => {
      btn.onclick = () => {
        const col = btn.getAttribute('data-pv-col');
        const delta = parseInt(btn.getAttribute('data-pv-delta'), 10);
        changePvCount(col, delta);
      };
    });

    // Prime Factor Buttons
    const pushPrimeBtn = document.getElementById('vlab-btn-push-prime');
    if (pushPrimeBtn) pushPrimeBtn.onclick = pushPrimeToStack;

    const dropPrimeBtn = document.getElementById('vlab-btn-drop-prime');
    if (dropPrimeBtn) dropPrimeBtn.onclick = dropTopPrimeFromX;

    const clearPrimeBtn = document.getElementById('vlab-btn-clear-prime');
    if (clearPrimeBtn) clearPrimeBtn.onclick = clearPrimeX;

    const factBtn = document.getElementById('vlab-btn-fact');
    if (factBtn) factBtn.onclick = primeFactorizeX;

    const gcdBtn = document.getElementById('vlab-btn-gcd');
    if (gcdBtn) gcdBtn.onclick = primeGcd;

    const lcmBtn = document.getElementById('vlab-btn-lcm');
    if (lcmBtn) lcmBtn.onclick = primeLcm;

    const primeBtns = document.querySelectorAll('[data-prime-p]');
    primeBtns.forEach(btn => {
      btn.onclick = () => {
        const p = parseInt(btn.getAttribute('data-prime-p'), 10);
        addPrimeToX(p);
      };
    });

    // Fraction Palette Block Buttons (Delegation or attribute)
    const fracPaletteBtns = document.querySelectorAll('[data-frac-spec]');
    fracPaletteBtns.forEach(btn => {
      btn.onclick = () => {
        try {
          const spec = JSON.parse(btn.getAttribute('data-frac-spec'));
          addFractionToX(spec);
        } catch (e) {
          // parse error
        }
      };
    });

    // Initial Render
    renderAll();
  }

  // Initialize on DOMContentLoaded or immediate
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLab);
  } else {
    initLab();
  }

  // Public Interface for Browser Tests & Inline Clicks
  window.StackCalcLab = {
    state: state,
    addFraction: addFractionToX,
    removeFractionFromX: removeFractionFromX,
    dropTopFraction: dropTopFractionFromX,
    clearStagingFractions: clearFractionX,
    clearFractions: clearFractionX,
    addTargetFraction: addTargetFraction,
    removeTargetFraction: removeTargetFraction,
    clearTargetFractions: clearTargetFractions,
    pushFraction: pushFractionToStack,

    changePvCount: changePvCount,
    autoRegroupPv: autoRegroupPv,
    getPvTotal: getPvTotal,
    pushPvToStack: pushPvToStack,

    addPrime: addPrimeToX,
    removePrimeFromX: removePrimeFromX,
    removeLastPrime: dropTopPrimeFromX,
    dropTopPrime: dropTopPrimeFromX,
    clearPrimes: clearPrimeX,
    pushPrimes: pushPrimeToStack,
    factorizeStackX: primeFactorizeX,
    calcGcd: primeGcd,
    calcLcm: primeLcm,

    pushValue: (v) => rpnPushRaw(v, 1, v),
    setActiveTab: setActiveTab,
    op: rpnOp,
    swap: rpnSwap,
    drop: rpnDrop,
    clearStack: rpnClear,
    toggleFullscreen: toggleFullscreen
  };
})();
