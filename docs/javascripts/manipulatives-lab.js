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

  function formatMixedFrac(n, d) {
    const s = simplifyFrac(n, d);
    if (s.d === 1) return `${s.n}`;
    if (s.n === 0) return '0';
    const absN = Math.abs(s.n);
    const absD = Math.abs(s.d);
    const sign = (s.n * s.d < 0) ? '-' : '';
    const whole = Math.floor(absN / absD);
    const rem = absN % absD;
    if (whole > 0 && rem > 0) {
      return `${sign}${whole} ${rem}/${absD}`;
    } else if (whole > 0 && rem === 0) {
      return `${sign}${whole}`;
    }
    return `${sign}${rem}/${absD}`;
  }

  function numberToPvCounts(num) {
    const counts = { 100: 0, 10: 0, 1: 0, 0.1: 0, 0.01: 0, 0.001: 0 };
    let n = Math.abs(Math.round(num * 1000) / 1000);
    if (n === 0) return counts;

    counts[100] = Math.floor(n / 100);
    n = Math.round((n % 100) * 1000) / 1000;

    counts[10] = Math.floor(n / 10);
    n = Math.round((n % 10) * 1000) / 1000;

    counts[1] = Math.floor(n);
    n = Math.round((n - counts[1]) * 1000) / 1000;

    counts[0.1] = Math.floor(n * 10);
    n = Math.round((n - counts[0.1] * 0.1) * 1000) / 1000;

    counts[0.01] = Math.floor(n * 100);
    n = Math.round((n - counts[0.01] * 0.01) * 1000) / 1000;

    counts[0.001] = Math.round(n * 1000);
    return counts;
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
    return sorted.join(' × ');
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
    stackLift: false, // RPN Stack Lift flag: true after operations to auto-lift on next entry

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
      stackX: [],       // Blocks in Register X (Column 1 - Active Entry)
      stackY: [],       // Blocks in Register Y (Column 2 - Stack)
      stackZ: [],       // Blocks in Register Z (Stack Level 3)
      stackT: [],       // Blocks in Register T (Stack Level 4)
      targetAnswer: [], // Compatibility shim
      mixedMode: false, // Mixed number display format (a b/c)

      // Compatibility getters
      get staging() { return this.stackX; },
      set staging(v) { this.stackX = v; },
      get comparatorY() { return this.stackY; },
      set comparatorY(v) { this.stackY = v; }
    },

    // Place-Value Specific State (PLACE-01 Multi-Row Desk)
    placeValue: {
      carryCounts: {
        100: 0,
        10: 0,
        1: 0,
        0.1: 0,
        0.01: 0,
        0.001: 0
      },
      row1Counts: {
        100: 0,
        10: 0,
        1: 0,
        0.1: 0,
        0.01: 0,
        0.001: 0
      },
      row2Counts: {
        100: 0,
        10: 0,
        1: 0,
        0.1: 0,
        0.01: 0,
        0.001: 0
      },
      get stagingCounts() { return this.row2Counts; },
      set stagingCounts(v) { this.row2Counts = v; },
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
      stackX: [],       // Prime blocks in Register X (Column 1 - Active Entry)
      stackY: [],       // Prime blocks in Register Y (Column 2 - Stack)
      stackZ: [],       // Prime blocks in Register Z (Stack Level 3)
      stackT: [],       // Prime blocks in Register T (Stack Level 4)
      targetPrimes: [], // Compatibility shim

      // Compatibility getters
      get staging() { return this.stackX; },
      set staging(v) { this.stackX = v; },
      get stagingProduct() { return getPrimeProduct(this.stackX); },
      get targetDecomp() { return this.targetPrimes; }
    }
  };

  // --- 4. RPN Calculator Stack Operations & Stack Lift ---
  function prepareForEntry() {
    if (state.stackLift) {
      // Automatic RPN Stack Lift on new number/block entry following an operation
      state.stack.t = { ...state.stack.z };
      state.stack.z = { ...state.stack.y };
      state.stack.y = { ...state.stack.x };
      state.stack.x = { n: 0, d: 1, val: 0 };

      if (state.activeTab === 'fractions') {
        state.fractions.stackT = [...state.fractions.stackZ];
        state.fractions.stackZ = [...state.fractions.stackY];
        state.fractions.stackY = [...state.fractions.stackX];
        state.fractions.stackX = [];
      } else if (state.activeTab === 'primes') {
        state.primes.stackT = [...state.primes.stackZ];
        state.primes.stackZ = [...state.primes.stackY];
        state.primes.stackY = [...state.primes.stackX];
        state.primes.stackX = [];
      } else if (state.activeTab === 'placevalue') {
        for (let k in state.placeValue.stagingCounts) {
          state.placeValue.stagingCounts[k] = 0;
        }
      }

      state.stackLift = false;
    }
  }

  function rpnPushRaw(n, d, val) {
    if (val === undefined) val = n / d;
    state.stack.t = { ...state.stack.z };
    state.stack.z = { ...state.stack.y };
    state.stack.y = { ...state.stack.x };
    state.stack.x = { n, d, val };
    state.stackLift = false;
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
    state.stackLift = false;
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
      state.fractions.stackY = [...state.fractions.stackZ];
      state.fractions.stackZ = [...state.fractions.stackT];
      state.fractions.stackT = [];
    } else if (state.activeTab === 'primes') {
      state.primes.stackX = [...state.primes.stackY];
      state.primes.stackY = [...state.primes.stackZ];
      state.primes.stackZ = [...state.primes.stackT];
      state.primes.stackT = [];
    }
    state.stackLift = true;
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
    state.stackLift = true;
    playClick();
    renderAll();
  }

  function rpnOp(operator) {
    if (state.activeTab === 'placevalue') {
      if (operator === '+') {
        addPvRows();
        return;
      } else if (operator === '-') {
        subtractPvRows();
        return;
      } else if (operator === '×') {
        multiplyPvRows();
        return;
      } else if (operator === '÷') {
        const yVal = getPvTotal(1) || state.stack.y.val;
        const xVal = getPvTotal(2) || state.stack.x.val;
        if (xVal !== 0) {
          const quot = Math.round((yVal / xVal) * 1000) / 1000;
          state.placeValue.row2Counts = numberToPvCounts(quot);
          for (let k in state.placeValue.row1Counts) state.placeValue.row1Counts[k] = 0;
          for (let k in state.placeValue.carryCounts) state.placeValue.carryCounts[k] = 0;
          state.stack.x = { n: Math.round(quot * 1000), d: 1000, val: quot };
          state.stack.y = { ...state.stack.z };
          state.stack.z = { ...state.stack.t };
          state.stack.t = { n: 0, d: 1, val: 0 };
          state.stackLift = true;
          playOp();
          checkPvRegroup();
          renderAll();
        }
        return;
      }
    }

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
        state.fractions.stackY = [...state.fractions.stackZ];
        state.fractions.stackZ = [...state.fractions.stackT];
        state.fractions.stackT = [];
      }
    } else if (operator === '-') {
      resN = y.n * x.d - x.n * y.d;
      resD = y.d * x.d;
      resVal = y.val - x.val;
      if (state.activeTab === 'fractions') {
        state.fractions.stackY = [...state.fractions.stackZ];
        state.fractions.stackZ = [...state.fractions.stackT];
        state.fractions.stackT = [];
      }
    } else if (operator === '×') {
      resN = y.n * x.n;
      resD = y.d * x.d;
      resVal = y.val * x.val;
      if (state.activeTab === 'fractions') {
        state.fractions.stackY = [...state.fractions.stackZ];
        state.fractions.stackZ = [...state.fractions.stackT];
        state.fractions.stackT = [];
      } else if (state.activeTab === 'primes') {
        state.primes.stackX = [...state.primes.stackY, ...state.primes.stackX].sort((a, b) => a - b);
        state.primes.stackY = [...state.primes.stackZ];
        state.primes.stackZ = [...state.primes.stackT];
        state.primes.stackT = [];
      }
    } else if (operator === '÷') {
      if (x.val !== 0) {
        resN = y.n * x.d;
        resD = y.d * x.n;
        resVal = y.val / x.val;
      }
      if (state.activeTab === 'fractions') {
        state.fractions.stackY = [...state.fractions.stackZ];
        state.fractions.stackZ = [...state.fractions.stackT];
        state.fractions.stackT = [];
      }
    }

    const simp = simplifyFrac(resN, resD);
    state.stack.x = { n: simp.n, d: simp.d, val: resVal };
    state.stack.y = { ...state.stack.z };
    state.stack.z = { ...state.stack.t };
    state.stack.t = { n: 0, d: 1, val: 0 };

    state.stackLift = true; // Results trigger automatic stack lift on subsequent number entry!
    playOp();
    renderAll();
  }

  // --- 5. Fraction Studio Actions ---
  function reconstructFracBlocks(n, d) {
    state.fractions.stackX = [];
    if (n <= 0) return;
    const paletteMap = {
      1: { label: '1/1', n: 1, d: 1, mm: 84.0, cls: 'frac-1-1' },
      2: { label: '1/2', n: 1, d: 2, mm: 42.0, cls: 'frac-1-2' },
      3: { label: '1/3', n: 1, d: 3, mm: 28.0, cls: 'frac-1-3' },
      4: { label: '1/4', n: 1, d: 4, mm: 21.0, cls: 'frac-1-4' },
      5: { label: '1/5', n: 1, d: 5, mm: 16.8, cls: 'frac-1-5' },
      6: { label: '1/6', n: 1, d: 6, mm: 14.0, cls: 'frac-1-6' },
      8: { label: '1/8', n: 1, d: 8, mm: 10.5, cls: 'frac-1-8' },
      10: { label: '1/10', n: 1, d: 10, mm: 8.4, cls: 'frac-1-10' },
      12: { label: '1/12', n: 1, d: 12, mm: 7.0, cls: 'frac-1-12' }
    };
    const spec = paletteMap[d] || { label: `1/${d}`, n: 1, d: d, mm: Math.max(7, 84 / d), cls: 'frac-custom' };
    const count = Math.min(n, 24);
    for (let i = 0; i < count; i++) {
      state.fractions.stackX.push({ ...spec, id: Date.now() + Math.random() });
    }
  }

  function fractionSimp() {
    const x = state.stack.x;
    if (x.n === 0) return;
    const g = gcd(Math.abs(x.n), Math.abs(x.d));
    if (g > 1) {
      let p = g;
      for (let factor of [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) {
        if (g % factor === 0) {
          p = factor;
          break;
        }
      }
      const newN = x.n / p;
      const newD = x.d / p;
      state.stack.x = { n: newN, d: newD, val: newN / newD };
      reconstructFracBlocks(newN, newD);
      state.stackLift = true;
      playOp();
      renderAll();

      const metaX = document.getElementById('vlab-staged-meta');
      if (metaX) {
        metaX.innerHTML = `<span style="color:#10B981;">SIMP (÷${p}) ➔ ${newN}/${newD}</span>`;
      }
    } else {
      playSuccess();
      const metaX = document.getElementById('vlab-staged-meta');
      if (metaX) {
        metaX.innerHTML = `<span style="color:#F59E0B;">LOWEST TERMS</span>`;
      }
    }
  }

  function fractionMixedToggle() {
    state.fractions.mixedMode = true;
    playClick();
    renderAll();
  }

  function fractionImproper() {
    state.fractions.mixedMode = false;
    playClick();
    renderAll();
  }

  function fractionInvert() {
    const x = state.stack.x;
    if (x.n === 0) return;
    const newN = x.d;
    const newD = x.n;
    const simp = simplifyFrac(newN, newD);
    state.stack.x = { n: simp.n, d: simp.d, val: simp.n / simp.d };
    reconstructFracBlocks(simp.n, simp.d);
    state.stackLift = true;
    playOp();
    renderAll();
  }
  function addFractionToX(blockSpec) {
    prepareForEntry();
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
    state.stackLift = false;
    playClick();
    renderAll();
  }

  function pushFractionToStack() {
    if (state.fractions.stackX.length === 0 && state.stack.x.val === 0) return;

    // Push 4-line stack registers
    state.stack.t = { ...state.stack.z };
    state.stack.z = { ...state.stack.y };
    state.stack.y = { ...state.stack.x };
    state.stack.x = { n: 0, d: 1, val: 0 };

    // Move visual block towers through stack registers
    state.fractions.stackT = [...state.fractions.stackZ];
    state.fractions.stackZ = [...state.fractions.stackY];
    state.fractions.stackY = [...state.fractions.stackX];
    state.fractions.stackX = [];

    state.stackLift = false;
    playPush();
    renderAll();
  }

  function addTargetFraction(blockSpec) {
    // Compatibility stub
  }

  function removeTargetFraction(index) {
    // Compatibility stub
  }

  function clearTargetFractions() {
    // Compatibility stub
  }

  // --- 6. Prime Factor Studio Actions ---
  function addPrimeToX(p) {
    prepareForEntry();
    state.primes.stackX.push(p);
    const prod = getPrimeProduct(state.primes.stackX);
    // Immediately update Register X on the LCD with the composite number!
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
    state.stackLift = false;
    playClick();
    renderAll();
  }

  function pushPrimeToStack() {
    if (state.primes.stackX.length === 0 && state.stack.x.val === 0) return;

    state.stack.t = { ...state.stack.z };
    state.stack.z = { ...state.stack.y };
    state.stack.y = { ...state.stack.x };
    state.stack.x = { n: 0, d: 1, val: 0 };

    state.primes.stackT = [...state.primes.stackZ];
    state.primes.stackZ = [...state.primes.stackY];
    state.primes.stackY = [...state.primes.stackX];
    state.primes.stackX = [];

    state.stackLift = false;
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
      state.primes.stackY = [...state.primes.stackZ];
      state.primes.stackZ = [...state.primes.stackT];
      state.primes.stackT = [];
      state.stack.x = { n: g, d: 1, val: g };
      state.stack.y = { ...state.stack.z };
      state.stack.z = { ...state.stack.t };
      state.stack.t = { n: 0, d: 1, val: 0 };
      state.stackLift = true;
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
      state.primes.stackY = [...state.primes.stackZ];
      state.primes.stackZ = [...state.primes.stackT];
      state.primes.stackT = [];
      state.stack.x = { n: l, d: 1, val: l };
      state.stack.y = { ...state.stack.z };
      state.stack.z = { ...state.stack.t };
      state.stack.t = { n: 0, d: 1, val: 0 };
      state.stackLift = true;
      playOp();
      renderAll();
    }
  }

  function primeFactorizeX() {
    const xVal = Math.round(state.stack.x.val);
    if (xVal > 1) {
      const factors = getPrimeFactorsList(xVal);
      state.primes.stackX = factors;
      state.stackLift = true;
      playOp();
      renderAll();
    }
  }

  function primeCommonFactors() {
    const yVal = Math.round(state.stack.y.val);
    const xVal = Math.round(state.stack.x.val);
    if (yVal > 0 && xVal > 0) {
      const fY = getPrimeFactorsList(yVal);
      const fX = getPrimeFactorsList(xVal);
      const common = [];
      const tempY = [...fY];
      for (let p of fX) {
        const idx = tempY.indexOf(p);
        if (idx !== -1) {
          common.push(p);
          tempY.splice(idx, 1);
        }
      }
      state.primes.stackX = common;
      const commonProd = getPrimeProduct(common);
      state.stack.x = { n: commonProd, d: 1, val: commonProd };
      state.stackLift = true;
      playOp();
      renderAll();

      const formEl = document.getElementById('vlab-prime-formula');
      if (formEl) {
        if (common.length > 0) {
          formEl.textContent = `COMMON: ${common.join(' × ')} = ${commonProd} (GCF)`;
        } else {
          formEl.textContent = 'NO COMMON FACTORS (RELATIVELY PRIME)';
        }
      }
    }
  }

  // --- 7. Place-Value Studio Actions (PLACE-01 Multi-Row Desk) ---
  function changePvCount(colKey, delta, row = 2) {
    prepareForEntry();
    const val = parseFloat(colKey);
    const counts = (row === 1) ? state.placeValue.row1Counts : state.placeValue.row2Counts;
    const curr = counts[val] || 0;
    const next = Math.max(0, curr + delta);
    counts[val] = next;

    if (row === 2) {
      const total = getPvTotal(2);
      state.stack.x = {
        n: Math.round(total * 1000),
        d: 1000,
        val: total
      };
    } else if (row === 1) {
      const totalY = getPvTotal(1);
      state.stack.y = {
        n: Math.round(totalY * 1000),
        d: 1000,
        val: totalY
      };
    }

    playClick();
    checkPvRegroup();
    renderAll();
  }

  function removePvBlock(row, colKey) {
    changePvCount(colKey, -1, row);
  }

  function checkPvRegroup() {
    let hasExceed = false;
    let note = '';
    const r2 = state.placeValue.row2Counts;
    const carry = state.placeValue.carryCounts;

    for (let k of [0.001, 0.01, 0.1, 1, 10, 100]) {
      if ((carry[k] || 0) > 0) {
        hasExceed = true;
        note = `⚠️ Carried tokens waiting! Tap REGROUP to bundle into the next column.`;
        break;
      }
      if ((r2[k] || 0) >= 10) {
        hasExceed = true;
        const numVal = parseFloat(k);
        const nextVal = (numVal * 10).toFixed(3);
        note = `⚠️ ${r2[k]} units in [${k}] column! Tap REGROUP to bundle 10 blocks into [${parseFloat(nextVal)}]!`;
        break;
      }
    }
    state.placeValue.hasCarry = hasExceed;
    state.placeValue.regroupNote = note;
  }

  function autoRegroupPv() {
    const counts = state.placeValue.row2Counts;
    const carry = state.placeValue.carryCounts;
    const keys = [0.001, 0.01, 0.1, 1, 10, 100];
    let changed = false;

    // Merge carry tokens
    keys.forEach(k => {
      if ((carry[k] || 0) > 0) {
        counts[k] = (counts[k] || 0) + carry[k];
        carry[k] = 0;
        changed = true;
      }
    });

    // Bundle 10 units into 1 of the next column
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
      const total = getPvTotal(2);
      state.stack.x = {
        n: Math.round(total * 1000),
        d: 1000,
        val: total
      };
      checkPvRegroup();
      renderAll();
    }
  }

  function unbundlePv(colKey) {
    const counts = state.placeValue.row2Counts;
    const keys = [0.001, 0.01, 0.1, 1, 10, 100];
    let targetIdx = -1;

    if (colKey !== undefined) {
      targetIdx = keys.indexOf(parseFloat(colKey));
    } else {
      for (let i = 1; i < keys.length; i++) {
        if ((counts[keys[i]] || 0) > 0) {
          targetIdx = i;
          break;
        }
      }
    }

    if (targetIdx > 0 && (counts[keys[targetIdx]] || 0) > 0) {
      counts[keys[targetIdx]] -= 1;
      const lowerKey = keys[targetIdx - 1];
      counts[lowerKey] = (counts[lowerKey] || 0) + 10;
      playClick();
      const total = getPvTotal(2);
      state.stack.x = {
        n: Math.round(total * 1000),
        d: 1000,
        val: total
      };
      checkPvRegroup();
      renderAll();
    }
  }

  function getPvTotal(row = 2) {
    const counts = (row === 1) ? state.placeValue.row1Counts : state.placeValue.row2Counts;
    let total = 0;
    for (let k in counts) {
      total += parseFloat(k) * (counts[k] || 0);
    }
    return Math.round(total * 1000) / 1000;
  }

  function pushPvToStack() {
    const total = getPvTotal(2);
    if (total === 0 && state.stack.x.val === 0) return;

    state.stack.t = { ...state.stack.z };
    state.stack.z = { ...state.stack.y };
    state.stack.y = { ...state.stack.x };
    state.stack.x = { n: 0, d: 1, val: 0 };

    state.placeValue.row1Counts = { ...state.placeValue.row2Counts };
    state.placeValue.row2Counts = { 100: 0, 10: 0, 1: 0, 0.1: 0, 0.01: 0, 0.001: 0 };
    state.placeValue.carryCounts = { 100: 0, 10: 0, 1: 0, 0.1: 0, 0.01: 0, 0.001: 0 };

    playPush();
    checkPvRegroup();
    renderAll();
  }

  function clearPv(row) {
    if (row === 1) {
      state.placeValue.row1Counts = { 100: 0, 10: 0, 1: 0, 0.1: 0, 0.01: 0, 0.001: 0 };
    } else if (row === 2) {
      state.placeValue.row2Counts = { 100: 0, 10: 0, 1: 0, 0.1: 0, 0.01: 0, 0.001: 0 };
      state.stack.x = { n: 0, d: 1, val: 0 };
    } else {
      state.placeValue.row1Counts = { 100: 0, 10: 0, 1: 0, 0.1: 0, 0.01: 0, 0.001: 0 };
      state.placeValue.row2Counts = { 100: 0, 10: 0, 1: 0, 0.1: 0, 0.01: 0, 0.001: 0 };
      state.placeValue.carryCounts = { 100: 0, 10: 0, 1: 0, 0.1: 0, 0.01: 0, 0.001: 0 };
      state.stack.x = { n: 0, d: 1, val: 0 };
    }
    state.stackLift = false;
    playClick();
    checkPvRegroup();
    renderAll();
  }

  function addPvRows() {
    if (getPvTotal(1) === 0 && state.stack.y.val > 0) {
      state.placeValue.row1Counts = numberToPvCounts(state.stack.y.val);
    }
    if (getPvTotal(2) === 0 && state.stack.x.val > 0) {
      state.placeValue.row2Counts = numberToPvCounts(state.stack.x.val);
    }

    const r1 = state.placeValue.row1Counts;
    const r2 = state.placeValue.row2Counts;
    const carry = state.placeValue.carryCounts;
    const keys = [0.001, 0.01, 0.1, 1, 10, 100];

    keys.forEach((k, idx) => {
      const sum = (r1[k] || 0) + (r2[k] || 0) + (carry[k] || 0);
      carry[k] = 0;
      if (sum >= 10 && idx + 1 < keys.length) {
        const carryOver = Math.floor(sum / 10);
        const rem = sum % 10;
        r2[k] = rem;
        carry[keys[idx + 1]] = carryOver;
      } else {
        r2[k] = sum;
      }
    });

    for (let k in r1) r1[k] = 0;

    let totalSum = getPvTotal(2);
    keys.forEach(k => { totalSum += (carry[k] || 0) * k; });
    const roundedSum = Math.round(totalSum * 1000) / 1000;

    state.stack.x = {
      n: Math.round(roundedSum * 1000),
      d: 1000,
      val: roundedSum
    };
    state.stack.y = { ...state.stack.z };
    state.stack.z = { ...state.stack.t };
    state.stack.t = { n: 0, d: 1, val: 0 };
    state.stackLift = true;

    playOp();
    checkPvRegroup();
    renderAll();
  }

  function subtractPvRows() {
    if (getPvTotal(1) === 0 && state.stack.y.val > 0) {
      state.placeValue.row1Counts = numberToPvCounts(state.stack.y.val);
    }
    if (getPvTotal(2) === 0 && state.stack.x.val > 0) {
      state.placeValue.row2Counts = numberToPvCounts(state.stack.x.val);
    }

    const yVal = getPvTotal(1);
    const xVal = getPvTotal(2);
    const diff = Math.round((yVal - xVal) * 1000) / 1000;

    if (diff >= 0) {
      state.placeValue.row2Counts = numberToPvCounts(diff);
    } else {
      state.placeValue.row2Counts = { 100: 0, 10: 0, 1: 0, 0.1: 0, 0.01: 0, 0.001: 0 };
    }
    for (let k in state.placeValue.row1Counts) state.placeValue.row1Counts[k] = 0;
    for (let k in state.placeValue.carryCounts) state.placeValue.carryCounts[k] = 0;

    state.stack.x = {
      n: Math.round(diff * 1000),
      d: 1000,
      val: diff
    };
    state.stack.y = { ...state.stack.z };
    state.stack.z = { ...state.stack.t };
    state.stack.t = { n: 0, d: 1, val: 0 };
    state.stackLift = true;

    playOp();
    checkPvRegroup();
    renderAll();
  }

  function multiplyPvRows() {
    if (getPvTotal(1) === 0 && state.stack.y.val > 0) {
      state.placeValue.row1Counts = numberToPvCounts(state.stack.y.val);
    }
    if (getPvTotal(2) === 0 && state.stack.x.val > 0) {
      state.placeValue.row2Counts = numberToPvCounts(state.stack.x.val);
    }

    const yVal = getPvTotal(1);
    const xVal = getPvTotal(2);
    const prod = Math.round((yVal * xVal) * 1000) / 1000;

    state.placeValue.row2Counts = numberToPvCounts(prod);
    for (let k in state.placeValue.row1Counts) state.placeValue.row1Counts[k] = 0;
    for (let k in state.placeValue.carryCounts) state.placeValue.carryCounts[k] = 0;

    state.stack.x = {
      n: Math.round(prod * 1000),
      d: 1000,
      val: prod
    };
    state.stack.y = { ...state.stack.z };
    state.stack.z = { ...state.stack.t };
    state.stack.t = { n: 0, d: 1, val: 0 };
    state.stackLift = true;

    playOp();
    checkPvRegroup();
    renderAll();
  }

  // --- 8. DOM Rendering & UI Presentation ---
  function renderStackLcd() {
    const fmt = (item, isRegX) => {
      if (!item) return isRegX ? '0_' : '0';
      if (state.activeTab === 'fractions') {
        if (item.val === 0) return isRegX ? '0_' : '0';
        if (state.fractions.mixedMode) {
          return `<strong style="font-size:1.25em; color:#FFFFFF;">${formatMixedFrac(item.n, item.d)}</strong>${isRegX ? '_' : ''}`;
        }
        if (state.fdisp) {
          return `<strong style="font-size:1.25em; color:#FFFFFF;">${formatFrac(item.n, item.d)}</strong>${isRegX ? '_' : ''}`;
        } else {
          return `<strong style="font-size:1.25em; color:#FFFFFF;">${Number(item.val.toFixed(2))}</strong>${isRegX ? '_' : ''}`;
        }
      } else if (state.activeTab === 'primes') {
        if (item.val === 0) return isRegX ? '0_' : '0';
        const intVal = Math.round(item.val);
        const factors = getPrimeFactorsList(intVal);
        const formula = factors.length > 1 ? factors.join(' × ') : '';
        if (formula) {
          return `<strong style="font-size:1.25em; color:#FFFFFF;">${intVal}</strong> <span style="color:#38BDF8; font-size:0.8em; margin-left:8px;">(${formula})</span>${isRegX ? '_' : ''}`;
        }
        return `<strong style="font-size:1.25em; color:#FFFFFF;">${intVal}</strong>${isRegX ? '_' : ''}`;
      } else {
        if (item.val === 0) return isRegX ? '0_' : '0';
        const cleanNum = Number(item.val.toFixed(3));
        return `<strong style="font-size:1.25em; color:#FFFFFF;">${cleanNum}</strong>${isRegX ? '_' : ''}`;
      }
    };

    // Update all instances across the page (handles tabbed and standalone pages)
    document.querySelectorAll('.vlab-reg-t-val').forEach(el => el.innerHTML = fmt(state.stack.t, false));
    document.querySelectorAll('.vlab-reg-z-val').forEach(el => el.innerHTML = fmt(state.stack.z, false));
    document.querySelectorAll('.vlab-reg-y-val').forEach(el => el.innerHTML = fmt(state.stack.y, false));
    document.querySelectorAll('.vlab-reg-x-val').forEach(el => el.innerHTML = fmt(state.stack.x, true));

    // Fallback updates for elements with IDs
    const regT = document.getElementById('vlab-reg-t');
    const regZ = document.getElementById('vlab-reg-z');
    const regY = document.getElementById('vlab-reg-y');
    const regX = document.getElementById('vlab-reg-x');
    if (regT) regT.innerHTML = fmt(state.stack.t, false);
    if (regZ) regZ.innerHTML = fmt(state.stack.z, false);
    if (regY) regY.innerHTML = fmt(state.stack.y, false);
    if (regX) regX.innerHTML = fmt(state.stack.x, true);
  }

  function renderFractions() {
    // 1. Column 1 (Left): Register X (Active Entry / Tower)
    const colX = document.getElementById('vlab-col-stack-x') || document.getElementById('vlab-col-stage');
    const metaX = document.getElementById('vlab-meta-stack-x') || document.getElementById('vlab-staged-val');
    const metaXSub = document.getElementById('vlab-staged-meta');
    if (colX) {
      colX.innerHTML = '';
      if (state.fractions.stackX.length === 0) {
        colX.innerHTML = '<div class="vlab-empty-hint">Build your number here<br><span style="color:#64748B; font-size:0.85em;">Tap fraction blocks above</span></div>';
        if (metaX) metaX.textContent = '0';
        if (metaXSub) metaXSub.textContent = '0';
      } else {
        const sumX = calcTowerSum(state.fractions.stackX);
        state.fractions.stackX.forEach((b, idx) => {
          const blk = document.createElement('div');
          blk.className = `frac-block-2d ${b.cls} removable`;
          blk.style.height = `${Math.max(26, b.mm * 2.8)}px`;
          blk.setAttribute('title', 'Tap to remove block');
          blk.textContent = b.label;
          blk.onclick = (e) => {
            e.stopPropagation();
            removeFractionFromX(idx);
          };
          colX.appendChild(blk);
        });
        const fracStr = formatFrac(sumX.n, sumX.d);
        if (metaX) metaX.textContent = fracStr;
        if (metaXSub) metaXSub.textContent = fracStr;
      }
    }

    // 2. Column 2 (Right): Register Y (The Stack)
    const colY = document.getElementById('vlab-col-stack-y');
    const metaY = document.getElementById('vlab-meta-stack-y');
    if (colY) {
      colY.innerHTML = '';
      if (state.fractions.stackY.length === 0) {
        colY.innerHTML = '<div class="vlab-empty-hint">Saved number appears here<br><span style="color:#64748B; font-size:0.85em;">Press [ENTER] to save</span></div>';
        if (metaY) metaY.textContent = '0';
      } else {
        const sumY = calcTowerSum(state.fractions.stackY);
        state.fractions.stackY.forEach((b) => {
          const blk = document.createElement('div');
          blk.className = `frac-block-2d ${b.cls}`;
          blk.style.height = `${Math.max(26, b.mm * 2.8)}px`;
          blk.textContent = b.label;
          colY.appendChild(blk);
        });
        if (metaY) metaY.textContent = formatFrac(sumY.n, sumY.d);
      }
    }

    // 3. Dynamic Stack Z & T support if elements exist
    const colZ = document.getElementById('vlab-col-stack-z');
    const metaZ = document.getElementById('vlab-meta-stack-z');
    const containerZ = document.getElementById('vlab-container-stack-z');
    if (colZ) {
      colZ.innerHTML = '';
      if (state.fractions.stackZ && state.fractions.stackZ.length > 0) {
        if (containerZ) containerZ.style.display = 'flex';
        const sumZ = calcTowerSum(state.fractions.stackZ);
        state.fractions.stackZ.forEach((b) => {
          const blk = document.createElement('div');
          blk.className = `frac-block-2d ${b.cls}`;
          blk.style.height = `${Math.max(26, b.mm * 2.8)}px`;
          blk.textContent = b.label;
          colZ.appendChild(blk);
        });
        if (metaZ) metaZ.textContent = `Z: ${formatFrac(sumZ.n, sumZ.d)}`;
      } else {
        if (containerZ) containerZ.style.display = 'none';
      }
    }
  }

  function renderPrimes() {
    // 1. Column 1 (Left): Prime Register X (Active Entry / Tower)
    const colX = document.getElementById('vlab-prime-stack-x') || document.getElementById('vlab-prime-stage');
    const valEl = document.getElementById('vlab-prime-val');
    const formulaEl = document.getElementById('vlab-prime-formula');
    const metaEl = document.getElementById('vlab-prime-meta');

    const prodX = getPrimeProduct(state.primes.stackX);

    if (colX) {
      colX.innerHTML = '';
      if (state.primes.stackX.length === 0) {
        colX.innerHTML = '<div class="vlab-empty-hint">Build your number here<br><span style="color:#64748B; font-size:0.85em;">Tap prime numbers above</span></div>';
      } else {
        state.primes.stackX.forEach((p, idx) => {
          const blk = document.createElement('div');
          blk.className = 'prime-block-2d-vert removable';
          const mm = primeLookupMm[p] || 20;
          blk.style.height = `${Math.max(26, mm * 2.2)}px`;
          blk.style.backgroundColor = primeLookupColors[p] || '#0284C7';
          blk.setAttribute('title', 'Tap to remove prime block');
          blk.innerHTML = `<span style="font-size:1.15em; font-weight:800;">${p}</span>`;
          blk.onclick = (e) => {
            e.stopPropagation();
            removePrimeFromX(idx);
          };
          colX.appendChild(blk);
        });
      }
    }

    const effectiveValX = prodX > 0 ? prodX : (state.stack.x.val > 0 ? Math.round(state.stack.x.val) : 0);
    if (valEl) valEl.textContent = effectiveValX > 0 ? `${effectiveValX}` : '0';
    if (formulaEl) {
      if (state.primes.stackX.length > 0) {
        const factors = state.primes.stackX.sort((a, b) => a - b);
        formulaEl.innerHTML = factors.length > 1 ? `${prodX} <span style="font-size:0.85em; color:#94A3B8;">(${factors.join(' × ')})</span>` : `${prodX}`;
      } else if (effectiveValX > 1) {
        const factors = getPrimeFactorsList(effectiveValX);
        formulaEl.innerHTML = factors.length > 1 ? `${effectiveValX} <span style="font-size:0.85em; color:#94A3B8;">(${factors.join(' × ')})</span>` : `${effectiveValX}`;
      } else {
        formulaEl.innerHTML = '0';
      }
    }
    if (metaEl) {
      const count = state.primes.stackX.length;
      metaEl.textContent = count > 0 ? `${count} ${count === 1 ? 'Prime Factor' : 'Prime Factors'}` : '';
    }

    // 2. Column 2 (Right): Prime Register Y (The Stack)
    const colY = document.getElementById('vlab-prime-stack-y');
    const metaY = document.getElementById('vlab-prime-meta-y');
    if (colY) {
      colY.innerHTML = '';
      if (state.primes.stackY.length === 0) {
        colY.innerHTML = '<div class="vlab-empty-hint">Saved number appears here<br><span style="color:#64748B; font-size:0.85em;">Press [ENTER] to save</span></div>';
        if (metaY) metaY.textContent = '0';
      } else {
        const prodY = getPrimeProduct(state.primes.stackY);
        state.primes.stackY.forEach((p) => {
          const blk = document.createElement('div');
          blk.className = 'prime-block-2d-vert';
          const mm = primeLookupMm[p] || 20;
          blk.style.height = `${Math.max(26, mm * 2.2)}px`;
          blk.style.backgroundColor = primeLookupColors[p] || '#0284C7';
          blk.innerHTML = `<span style="font-size:1.15em; font-weight:800;">${p}</span>`;
          colY.appendChild(blk);
        });
        if (metaY) metaY.textContent = `${prodY}`;
      }
    }

    // Dynamic Stack Z & T support if elements exist
    const colZ = document.getElementById('vlab-prime-stack-z');
    const metaZ = document.getElementById('vlab-prime-meta-z');
    const containerZ = document.getElementById('vlab-prime-container-z');
    if (colZ) {
      colZ.innerHTML = '';
      if (state.primes.stackZ && state.primes.stackZ.length > 0) {
        if (containerZ) containerZ.style.display = 'flex';
        const prodZ = getPrimeProduct(state.primes.stackZ);
        state.primes.stackZ.forEach((p) => {
          const blk = document.createElement('div');
          blk.className = 'prime-block-2d-vert';
          const mm = primeLookupMm[p] || 20;
          blk.style.height = `${Math.max(26, mm * 2.2)}px`;
          blk.style.backgroundColor = primeLookupColors[p] || '#0284C7';
          blk.innerHTML = `<span style="font-size:1.15em; font-weight:800;">${p}</span>`;
          colZ.appendChild(blk);
        });
        if (metaZ) metaZ.textContent = `Z: ${prodZ}`;
      } else {
        if (containerZ) containerZ.style.display = 'none';
      }
    }
  }

  function renderPlaceValue() {
    const keys = [100, 10, 1, 0.1, 0.01, 0.001];

    const blockSpecs = {
      100: { name: 'Hundreds Flat (100)', cls: 'pv-block-100', label: '100' },
      10: { name: 'Tens Rod (10)', cls: 'pv-block-10', label: '10' },
      1: { name: 'Unit Cube (1)', cls: 'pv-block-1', label: '1' },
      0.1: { name: 'Tenths Strip (.1)', cls: 'pv-block-0-1', label: '.1' },
      0.01: { name: 'Hundredths Tile (.01)', cls: 'pv-block-0-01', label: '.01' },
      0.001: { name: 'Thousandths Token (.001)', cls: 'pv-block-0-001', label: '' }
    };

    // 1. Render Top Carry Shelf (+1 Regroup Tokens)
    keys.forEach(k => {
      const socketCarry = document.getElementById(`pv-socket-carry-${k}`);
      if (socketCarry) {
        socketCarry.innerHTML = '';
        const carryCount = state.placeValue.carryCounts[k] || 0;
        for (let i = 0; i < carryCount; i++) {
          const blk = document.createElement('div');
          blk.className = 'pv-block pv-block-carry';
          blk.textContent = '+1';
          blk.title = `Carried +1 token in [${k}] (tap to trade)`;
          blk.onclick = (e) => {
            e.stopPropagation();
            state.placeValue.carryCounts[k]--;
            state.placeValue.row2Counts[k] = (state.placeValue.row2Counts[k] || 0) + 1;
            playClick();
            checkPvRegroup();
            renderAll();
          };
          socketCarry.appendChild(blk);
        }
      }
    });

    // 2. Render Row 1: Waiting Shelf / Register Y (Top Addend / Minuend)
    keys.forEach(k => {
      const socketY = document.getElementById(`pv-socket-y-${k}`);
      if (socketY) {
        socketY.innerHTML = '';
        const count = state.placeValue.row1Counts[k] || 0;
        const spec = blockSpecs[k];
        for (let i = 0; i < count; i++) {
          const blk = document.createElement('div');
          blk.className = `pv-block ${spec.cls}`;
          blk.textContent = spec.label;
          blk.title = `Row 1: ${spec.name} (tap to remove)`;
          blk.onclick = (e) => {
            e.stopPropagation();
            removePvBlock(1, k);
          };
          socketY.appendChild(blk);
        }
      }
    });

    // 3. Render Row 2: Active Desk / Register X (Bottom Addend / Subtrahend)
    keys.forEach(k => {
      const socketX = document.getElementById(`pv-socket-x-${k}`) || document.getElementById(`pv-socket-${k}`);
      if (socketX) {
        socketX.innerHTML = '';
        const count = state.placeValue.row2Counts[k] || 0;
        const spec = blockSpecs[k];

        if (count >= 10) {
          socketX.classList.add('has-carry');
        } else {
          socketX.classList.remove('has-carry');
        }

        for (let i = 0; i < count; i++) {
          const blk = document.createElement('div');
          blk.className = `pv-block ${spec.cls}`;
          blk.textContent = spec.label;
          blk.title = `Row 2: ${spec.name} (tap to remove)`;
          blk.onclick = (e) => {
            e.stopPropagation();
            removePvBlock(2, k);
          };
          socketX.appendChild(blk);
        }
      }
    });

    // Update Totals and Readouts
    const row1ValEl = document.getElementById('pv-row1-val');
    if (row1ValEl) {
      const tot1 = getPvTotal(1);
      row1ValEl.textContent = tot1 === 0 ? '0' : Number(tot1.toFixed(3));
    }

    const row2ValEl = document.getElementById('pv-total-val');
    if (row2ValEl) {
      const tot2 = getPvTotal(2);
      row2ValEl.textContent = tot2 === 0 ? '0' : Number(tot2.toFixed(3));
    }

    const readoutXEl = document.getElementById('pv-readout-x');
    if (readoutXEl) {
      const tot2 = getPvTotal(2);
      readoutXEl.textContent = tot2 === 0 ? '0' : Number(tot2.toFixed(3));
    }

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

    const simpFracBtn = document.getElementById('vlab-btn-simp');
    if (simpFracBtn) simpFracBtn.onclick = fractionSimp;

    const mixedFracBtn = document.getElementById('vlab-btn-mixed');
    if (mixedFracBtn) mixedFracBtn.onclick = fractionMixedToggle;

    const improperFracBtn = document.getElementById('vlab-btn-improper');
    if (improperFracBtn) improperFracBtn.onclick = fractionImproper;

    const invertFracBtn = document.getElementById('vlab-btn-invert');
    if (invertFracBtn) invertFracBtn.onclick = fractionInvert;

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

    const pvConsoleRegroup = document.getElementById('pv-console-regroup');
    if (pvConsoleRegroup) pvConsoleRegroup.onclick = autoRegroupPv;

    const pvUnbundleBtn = document.getElementById('pv-btn-unbundle');
    if (pvUnbundleBtn) pvUnbundleBtn.onclick = () => unbundlePv();

    const pvConsoleUnbundle = document.getElementById('pv-console-unbundle');
    if (pvConsoleUnbundle) pvConsoleUnbundle.onclick = () => unbundlePv();

    const pvClearBtn = document.getElementById('pv-btn-clear');
    if (pvClearBtn) pvClearBtn.onclick = () => clearPv(2);

    const pvSteps = document.querySelectorAll('[data-pv-col]');
    pvSteps.forEach(btn => {
      btn.onclick = () => {
        const col = btn.getAttribute('data-pv-col');
        const delta = parseInt(btn.getAttribute('data-pv-delta'), 10);
        const row = parseInt(btn.getAttribute('data-pv-row') || '2', 10);
        changePvCount(col, delta, row);
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

    const cfacBtn = document.getElementById('vlab-btn-cfac');
    if (cfacBtn) cfacBtn.onclick = primeCommonFactors;

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
    simpFraction: fractionSimp,
    toggleMixed: fractionMixedToggle,
    toggleImproper: fractionImproper,
    invertFraction: fractionInvert,

    changePvCount: changePvCount,
    removePvBlock: removePvBlock,
    autoRegroupPv: autoRegroupPv,
    unbundlePv: unbundlePv,
    clearPv: clearPv,
    getPvTotal: getPvTotal,
    pushPvToStack: pushPvToStack,
    addPvRows: addPvRows,
    subtractPvRows: subtractPvRows,
    multiplyPvRows: multiplyPvRows,

    addPrime: addPrimeToX,
    removePrimeFromX: removePrimeFromX,
    removeLastPrime: dropTopPrimeFromX,
    dropTopPrime: dropTopPrimeFromX,
    clearPrimes: clearPrimeX,
    pushPrimes: pushPrimeToStack,
    factorizeStackX: primeFactorizeX,
    commonFactors: primeCommonFactors,
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
