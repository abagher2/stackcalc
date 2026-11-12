/**
 * =========================================================================
 * STACKCALC 2D VIRTUAL MANIPULATIVES LAB ENGINE
 * Authentic Concrete-Representational-Abstract (CRA) Classroom Simulator
 * Fraction Towers (FRAC-01) & Prime Factor Studio (PRIME-01)
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

  function playPop() {
    playTone(420, 0.05, 'sine', 0.16);
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
    playTone(523.25, 0.18, 'triangle', 0.2);
    setTimeout(() => playTone(659.25, 0.22, 'triangle', 0.2), 70);
    setTimeout(() => playTone(783.99, 0.26, 'triangle', 0.2), 140);
    setTimeout(() => playTone(1046.50, 0.38, 'triangle', 0.25), 210);
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
    return a || 1;
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

  function formatImproperFrac(n, d) {
    const s = simplifyFrac(n, d);
    if (s.d === 1) return `${s.n}`;
    if (s.n === 0) return '0';
    return `${s.n}/${s.d}`;
  }

  function parseFractionString(str) {
    if (!str) return null;
    str = str.trim();
    // Mixed number e.g. "1 1/2" or "2 3/4"
    if (str.includes(' ')) {
      const parts = str.split(/\s+/);
      if (parts.length === 2 && parts[1].includes('/')) {
        const whole = parseInt(parts[0], 10);
        const [n, d] = parts[1].split('/').map(x => parseInt(x, 10));
        if (!isNaN(whole) && !isNaN(n) && !isNaN(d) && d > 0) {
          const totalN = whole * d + n;
          return { n: totalN, d: d, whole: whole, remN: n };
        }
      }
    }
    // Simple fraction e.g. "3/4"
    if (str.includes('/')) {
      const [n, d] = str.split('/').map(x => parseInt(x, 10));
      if (!isNaN(n) && !isNaN(d) && d > 0) {
        return { n, d, whole: Math.floor(n / d), remN: n % d };
      }
    }
    // Plain integer e.g. "2"
    const val = parseInt(str, 10);
    if (!isNaN(val)) {
      return { n: val, d: 1, whole: val, remN: 0 };
    }
    return null;
  }

  function getPrimeProduct(list) {
    if (!list || list.length === 0) return 0;
    return list.reduce((acc, p) => acc * p, 1);
  }

  const primeLookupMm = {
    2: 18.0, 3: 28.5, 5: 41.8, 7: 50.7, 11: 62.4, 13: 66.8, 17: 73.6, 19: 76.5, 23: 81.3
  };

  const primeLookupColors = {
    2: '#1D4ED8', // PLA Matte Blue
    3: '#FF5F2D', // PLA Matte Muted Red
    5: '#FFFFFF', // PLA White
    7: '#D49459', // PLA Tan
    11: '#F5C211', // PLA Yellow
    13: '#F5C211',
    17: '#F5C211',
    19: '#F5C211',
    23: '#F5C211'
  };

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

  // Standard fraction palette definitions (Matching Slant 3D Physical Kits)
  const PALETTE_FRAC = {
    1: { label: '1/1', n: 1, d: 1, mm: 84.0, cls: 'frac-1-1' },
    2: { label: '1/2', n: 1, d: 2, mm: 42.0, cls: 'frac-1-2' },
    3: { label: '1/3', n: 1, d: 3, mm: 28.0, cls: 'frac-1-3' },
    4: { label: '1/4', n: 1, d: 4, mm: 21.0, cls: 'frac-1-4' },
    5: { label: '1/5', n: 1, d: 5, mm: 16.8, cls: 'frac-1-5' },
    6: { label: '1/6', n: 1, d: 6, mm: 14.0, cls: 'frac-1-6' },
    8: { label: '1/8', n: 1, d: 8, mm: 10.5, cls: 'frac-1-8' },
    9: { label: '1/9', n: 1, d: 9, mm: 9.33, cls: 'frac-1-9' },
    10: { label: '1/10', n: 1, d: 10, mm: 8.4, cls: 'frac-1-10' },
    12: { label: '1/12', n: 1, d: 12, mm: 7.0, cls: 'frac-1-12' }
  };

  // --- 3. Core State Architecture ---
  const state = {
    activeTab: 'fractions', // 'fractions' | 'primes'
    soundOn: true,
    fdisp: true, // Fraction display mode
    stackLift: false, // RPN Stack Lift: true after an operation/result, auto-lifts on next entry

    // 4-Line RPN Stack (Stores rational objects: { n, d, val })
    stack: {
      t: { n: 0, d: 1, val: 0 },
      z: { n: 0, d: 1, val: 0 },
      y: { n: 0, d: 1, val: 0 },
      x: { n: 0, d: 1, val: 0 }
    },

    // Fraction Studio Specific State
    fractions: {
      palette: Object.values(PALETTE_FRAC),
      stackX: [],       // Blocks in Register X (Column 1 - Active Entry)
      stackY: [],       // Blocks in Register Y (Column 2 - Saved Stack)
      stackZ: [],       // Blocks in Register Z (Level 3)
      stackT: [],       // Blocks in Register T (Level 4)
      mixedMode: false, // Mixed number display format (a b/c)

      // Compatibility getters
      get staging() { return this.stackX; },
      set staging(v) { this.stackX = v; },
      get comparatorY() { return this.stackY; },
      set comparatorY(v) { this.stackY = v; }
    },

    // Prime Factor Studio Specific State (PRIME-01 Slant 3D Eratosthenes Palette)
    primes: {
      palette: [
        { p: 2, label: '[2]', mm: 18.0, color: '#1D4ED8' },
        { p: 3, label: '[3]', mm: 28.5, color: '#FF5F2D' },
        { p: 5, label: '[5]', mm: 41.8, color: '#FFFFFF' },
        { p: 7, label: '[7]', mm: 50.7, color: '#D49459' },
        { p: 11, label: '[11]', mm: 62.4, color: '#F5C211' },
        { p: 13, label: '[13]', mm: 66.8, color: '#F5C211' },
        { p: 17, label: '[17]', mm: 73.6, color: '#F5C211' },
        { p: 19, label: '[19]', mm: 76.5, color: '#F5C211' },
        { p: 23, label: '[23]', mm: 81.3, color: '#F5C211' }
      ],
      stackX: [],       // Prime blocks in Register X (Column 1 - Active Entry)
      stackY: [],       // Prime blocks in Register Y (Column 2 - Saved Stack)
      stackZ: [],       // Prime blocks in Register Z (Level 3)
      stackT: [],       // Prime blocks in Register T (Level 4)

      // Compatibility getters
      get staging() { return this.stackX; },
      set staging(v) { this.stackX = v; },
      get stagingProduct() { return getPrimeProduct(this.stackX); }
    }
  };

  // --- 4. RPN Calculator Stack Operations & Automatic Stack Lift ---
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
    const x = state.stack.x;
    const y = state.stack.y;
    let resN = 0, resD = 1, resVal = 0;

    if (operator === '+') {
      resN = y.n * x.d + x.n * y.d;
      resD = y.d * x.d;
      resVal = y.val + x.val;
      if (state.activeTab === 'fractions') {
        // Physical CRA Addition: combine physical blocks from Y and X into X!
        state.fractions.stackX = [...state.fractions.stackY, ...state.fractions.stackX];
        state.fractions.stackY = [...state.fractions.stackZ];
        state.fractions.stackZ = [...state.fractions.stackT];
        state.fractions.stackT = [];
      } else if (state.activeTab === 'primes') {
        const sumInt = Math.round(resVal);
        state.primes.stackX = getPrimeFactorsList(sumInt);
        state.primes.stackY = [...state.primes.stackZ];
        state.primes.stackZ = [...state.primes.stackT];
        state.primes.stackT = [];
      }
    } else if (operator === '-') {
      resN = y.n * x.d - x.n * y.d;
      resD = y.d * x.d;
      resVal = y.val - x.val;
      if (state.activeTab === 'fractions') {
        const simp = simplifyFrac(resN, resD);
        reconstructFracBlocks(simp.n, simp.d);
        state.fractions.stackY = [...state.fractions.stackZ];
        state.fractions.stackZ = [...state.fractions.stackT];
        state.fractions.stackT = [];
      } else if (state.activeTab === 'primes') {
        const diffInt = Math.max(0, Math.round(resVal));
        state.primes.stackX = getPrimeFactorsList(diffInt);
        state.primes.stackY = [...state.primes.stackZ];
        state.primes.stackZ = [...state.primes.stackT];
        state.primes.stackT = [];
      }
    } else if (operator === '×') {
      resN = y.n * x.n;
      resD = y.d * x.d;
      resVal = y.val * x.val;
      if (state.activeTab === 'fractions') {
        const simp = simplifyFrac(resN, resD);
        reconstructFracBlocks(simp.n, simp.d);
        state.fractions.stackY = [...state.fractions.stackZ];
        state.fractions.stackZ = [...state.fractions.stackT];
        state.fractions.stackT = [];
      } else if (state.activeTab === 'primes') {
        // Prime multiplication combines all prime factors together!
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
        const simp = simplifyFrac(resN, resD);
        reconstructFracBlocks(simp.n, simp.d);
        state.fractions.stackY = [...state.fractions.stackZ];
        state.fractions.stackZ = [...state.fractions.stackT];
        state.fractions.stackT = [];
      } else if (state.activeTab === 'primes') {
        const quotInt = Math.round(resVal);
        state.primes.stackX = getPrimeFactorsList(quotInt);
        state.primes.stackY = [...state.primes.stackZ];
        state.primes.stackZ = [...state.primes.stackT];
        state.primes.stackT = [];
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
    
    // Decompose whole units into 1/1 blocks first
    let whole = Math.floor(n / d);
    let remN = n % d;

    for (let i = 0; i < Math.min(whole, 4); i++) {
      state.fractions.stackX.push({ ...PALETTE_FRAC[1], id: Date.now() + Math.random() });
    }

    if (remN > 0) {
      const spec = PALETTE_FRAC[d] || { label: `1/${d}`, n: 1, d: d, mm: Math.max(7, 84 / d), cls: 'frac-custom' };
      const count = Math.min(remN, 16);
      for (let i = 0; i < count; i++) {
        state.fractions.stackX.push({ ...spec, id: Date.now() + Math.random() });
      }
    }
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
      playPop();
      renderAll();
    }
  }

  function removeFractionFromY(index) {
    if (index >= 0 && index < state.fractions.stackY.length) {
      state.fractions.stackY.splice(index, 1);
      const res = calcTowerSum(state.fractions.stackY);
      state.stack.y = { n: res.n, d: res.d, val: res.val };
      playPop();
      renderAll();
    }
  }

  function dropTopFractionFromX() {
    if (state.fractions.stackX.length > 0) {
      state.fractions.stackX.pop();
      const res = calcTowerSum(state.fractions.stackX);
      state.stack.x = { n: res.n, d: res.d, val: res.val };
      playPop();
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

  function fractionSimp() {
    const x = state.stack.x;
    if (x.n === 0) return;
    const g = gcd(Math.abs(x.n), Math.abs(x.d));
    if (g > 1) {
      // Find smallest prime factor to simplify step-by-step
      let p = g;
      for (let factor of [2, 3, 5, 7, 11, 13, 17, 19, 23]) {
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
      playSuccess();
      renderAll();

      const metaX = document.getElementById('vlab-staged-meta');
      if (metaX) {
        metaX.innerHTML = `<span style="color:#10B981; font-weight:800;">SIMP (÷${p}) ➔ ${newN}/${newD}</span>`;
      }
    } else {
      // Already lowest terms: if tower had multiple disparate blocks, rebuild into single canonical representation
      reconstructFracBlocks(x.n, x.d);
      playSuccess();
      renderAll();
      const metaX = document.getElementById('vlab-staged-meta');
      if (metaX) {
        metaX.innerHTML = `<span style="color:#F59E0B; font-weight:800;">LOWEST TERMS</span>`;
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

  function loadFractionDirect(inputStr) {
    const parsed = parseFractionString(inputStr);
    if (!parsed) return;
    prepareForEntry();
    reconstructFracBlocks(parsed.n, parsed.d);
    const res = calcTowerSum(state.fractions.stackX);
    state.stack.x = { n: res.n, d: res.d, val: res.val };
    playSuccess();
    renderAll();
  }

  // --- 6. Prime Factor Studio Actions ---
  function addPrimeToX(p) {
    prepareForEntry();
    state.primes.stackX.push(p);
    const prod = getPrimeProduct(state.primes.stackX);
    // Immediately update Register X on the LCD with the composite product!
    state.stack.x = { n: prod, d: 1, val: prod };
    playClick();
    renderAll();
  }

  function removePrimeFromX(index) {
    if (index >= 0 && index < state.primes.stackX.length) {
      state.primes.stackX.splice(index, 1);
      const prod = getPrimeProduct(state.primes.stackX);
      state.stack.x = { n: prod, d: 1, val: prod };
      playPop();
      renderAll();
    }
  }

  function removePrimeFromY(index) {
    if (index >= 0 && index < state.primes.stackY.length) {
      state.primes.stackY.splice(index, 1);
      const prod = getPrimeProduct(state.primes.stackY);
      state.stack.y = { n: prod, d: 1, val: prod };
      playPop();
      renderAll();
    }
  }

  function dropTopPrimeFromX() {
    if (state.primes.stackX.length > 0) {
      state.primes.stackX.pop();
      const prod = getPrimeProduct(state.primes.stackX);
      state.stack.x = { n: prod, d: 1, val: prod };
      playPop();
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

  function primeFactorizeX() {
    const xVal = Math.round(state.stack.x.val);
    if (xVal > 1) {
      const factors = getPrimeFactorsList(xVal);
      state.primes.stackX = factors;
      state.stackLift = true;
      playSuccess();
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
      playSuccess();
      renderAll();

      const formEl = document.getElementById('vlab-prime-formula');
      if (formEl) {
        if (common.length > 0) {
          formEl.innerHTML = `<span style="color:#10B981;">COMMON: ${common.join(' × ')} = ${commonProd} (GCF)</span>`;
        } else {
          formEl.innerHTML = `<span style="color:#F59E0B;">NO COMMON FACTORS (RELATIVELY PRIME)</span>`;
        }
      }
    }
  }

  function primeGcd() {
    const yVal = Math.round(state.stack.y.val);
    const xVal = Math.round(state.stack.x.val);
    if (yVal > 0 && xVal > 0) {
      const g = gcd(yVal, xVal);
      state.primes.stackX = getPrimeFactorsList(g);
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
      state.primes.stackX = getPrimeFactorsList(l);
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

  function loadPrimeDirect(numStr) {
    const parsed = parseInt(numStr, 10);
    if (isNaN(parsed) || parsed <= 1) return;
    prepareForEntry();
    state.primes.stackX = getPrimeFactorsList(parsed);
    const prod = getPrimeProduct(state.primes.stackX);
    state.stack.x = { n: prod, d: 1, val: prod };
    playSuccess();
    renderAll();
  }

  // --- 7. DOM Rendering & UI Presentation ---
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
          return `<strong style="font-size:1.25em; color:#FFFFFF;">${intVal}</strong> <span style="color:#38BDF8; font-size:0.75em; margin-left:6px;">(${formula})</span>${isRegX ? '_' : ''}`;
        }
        return `<strong style="font-size:1.25em; color:#FFFFFF;">${intVal}</strong>${isRegX ? '_' : ''}`;
      }
      return `${item.val || 0}`;
    };

    // Update all LCD registers across all views
    document.querySelectorAll('.vlab-reg-t-val').forEach(el => el.innerHTML = fmt(state.stack.t, false));
    document.querySelectorAll('.vlab-reg-z-val').forEach(el => el.innerHTML = fmt(state.stack.z, false));
    document.querySelectorAll('.vlab-reg-y-val').forEach(el => el.innerHTML = fmt(state.stack.y, false));
    document.querySelectorAll('.vlab-reg-x-val').forEach(el => el.innerHTML = fmt(state.stack.x, true));

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
          blk.className = `frac-block-2d ${b.cls}`;
          // Base height: 84mm = 140px, min 22px so label is legible
          blk.style.height = `${Math.max(22, b.mm * 1.66)}px`;
          blk.setAttribute('title', 'Tap to remove block');
          blk.textContent = b.label;
          blk.onclick = (e) => {
            e.stopPropagation();
            removeFractionFromX(idx);
          };
          colX.appendChild(blk);
        });
        const fracStr = state.fractions.mixedMode ? formatMixedFrac(sumX.n, sumX.d) : formatFrac(sumX.n, sumX.d);
        if (metaX) metaX.textContent = fracStr;
        if (metaXSub) metaXSub.textContent = fracStr;
      }
    }

    // 2. Column 2 (Right): Register Y (Saved Stack)
    const colY = document.getElementById('vlab-col-stack-y');
    const metaY = document.getElementById('vlab-meta-stack-y');
    if (colY) {
      colY.innerHTML = '';
      if (state.fractions.stackY.length === 0) {
        colY.innerHTML = '<div class="vlab-empty-hint">Saved number appears here<br><span style="color:#64748B; font-size:0.85em;">Press [ENTER] to save</span></div>';
        if (metaY) metaY.textContent = '0';
      } else {
        const sumY = calcTowerSum(state.fractions.stackY);
        state.fractions.stackY.forEach((b, idx) => {
          const blk = document.createElement('div');
          blk.className = `frac-block-2d ${b.cls}`;
          blk.style.height = `${Math.max(22, b.mm * 1.66)}px`;
          blk.setAttribute('title', 'Tap to remove block from saved stack');
          blk.textContent = b.label;
          blk.onclick = (e) => {
            e.stopPropagation();
            removeFractionFromY(idx);
          };
          colY.appendChild(blk);
        });
        const fracStrY = state.fractions.mixedMode ? formatMixedFrac(sumY.n, sumY.d) : formatFrac(sumY.n, sumY.d);
        if (metaY) metaY.textContent = fracStrY;
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
          const pClass = p === 2 ? 'prime-p-2' : (p === 3 ? 'prime-p-3' : (p === 5 ? 'prime-p-5' : (p === 7 ? 'prime-p-7' : 'prime-p-higher')));
          blk.className = `prime-block-2d-vert ${pClass}`;
          const mm = primeLookupMm[p] || 20;
          // Scale: 2=36px, 3=54px, 5=78px, 7=96px, etc.
          blk.style.height = `${Math.max(28, mm * 1.8)}px`;
          blk.style.backgroundColor = primeLookupColors[p] || (p >= 11 ? '#F5C211' : '#1D4ED8');
          if (p === 5 || p >= 11) {
            blk.style.color = '#0F172A';
            blk.style.border = p === 5 ? '1px solid #CBD5E1' : '1px solid #D5B50E';
          } else if (p === 7) {
            blk.style.color = '#FFFFFF';
            blk.style.border = '1px solid #B37B42';
          } else if (p === 3) {
            blk.style.color = '#FFFFFF';
            blk.style.border = '1px solid #E04B1D';
          } else {
            blk.style.color = '#FFFFFF';
            blk.style.border = '1px solid #3B82F6';
          }
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
        const factors = [...state.primes.stackX].sort((a, b) => a - b);
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

    // 2. Column 2 (Right): Prime Register Y (Saved Stack)
    const colY = document.getElementById('vlab-prime-stack-y');
    const metaY = document.getElementById('vlab-prime-meta-y');
    if (colY) {
      colY.innerHTML = '';
      if (state.primes.stackY.length === 0) {
        colY.innerHTML = '<div class="vlab-empty-hint">Saved number appears here<br><span style="color:#64748B; font-size:0.85em;">Press [ENTER] to save</span></div>';
        if (metaY) metaY.textContent = '0';
      } else {
        const prodY = getPrimeProduct(state.primes.stackY);
        state.primes.stackY.forEach((p, idx) => {
          const blk = document.createElement('div');
          const pClass = p === 2 ? 'prime-p-2' : (p === 3 ? 'prime-p-3' : (p === 5 ? 'prime-p-5' : (p === 7 ? 'prime-p-7' : 'prime-p-higher')));
          blk.className = `prime-block-2d-vert ${pClass}`;
          const mm = primeLookupMm[p] || 20;
          blk.style.height = `${Math.max(28, mm * 1.8)}px`;
          blk.style.backgroundColor = primeLookupColors[p] || (p >= 11 ? '#F5C211' : '#1D4ED8');
          if (p === 5 || p >= 11) {
            blk.style.color = '#0F172A';
            blk.style.border = p === 5 ? '1px solid #CBD5E1' : '1px solid #D5B50E';
          } else if (p === 7) {
            blk.style.color = '#FFFFFF';
            blk.style.border = '1px solid #B37B42';
          } else if (p === 3) {
            blk.style.color = '#FFFFFF';
            blk.style.border = '1px solid #E04B1D';
          } else {
            blk.style.color = '#FFFFFF';
            blk.style.border = '1px solid #3B82F6';
          }
          blk.setAttribute('title', 'Tap to remove prime block from saved stack');
          blk.innerHTML = `<span style="font-size:1.15em; font-weight:800;">${p}</span>`;
          blk.onclick = (e) => {
            e.stopPropagation();
            removePrimeFromY(idx);
          };
          colY.appendChild(blk);
        });
        if (metaY) metaY.textContent = `${prodY}`;
      }
    }
  }

  function renderAll() {
    renderStackLcd();
    if (state.activeTab === 'fractions') {
      renderFractions();
    } else if (state.activeTab === 'primes') {
      renderPrimes();
    }
  }

  function setActiveTab(tab) {
    if (tab !== 'fractions' && tab !== 'primes') return;
    state.activeTab = tab;

    // Toggle Tab Buttons
    const tabFrac = document.getElementById('vlab-tab-fractions');
    const tabPrimes = document.getElementById('vlab-tab-primes');
    if (tabFrac) tabFrac.classList.toggle('active', tab === 'fractions');
    if (tabPrimes) tabPrimes.classList.toggle('active', tab === 'primes');

    // Toggle Views
    const viewFrac = document.getElementById('vlab-view-fractions');
    const viewPrimes = document.getElementById('vlab-view-primes');
    if (viewFrac) viewFrac.style.display = (tab === 'fractions') ? 'block' : 'none';
    if (viewPrimes) viewPrimes.style.display = (tab === 'primes') ? 'block' : 'none';

    playClick();
    renderAll();
  }

  function toggleFullscreen() {
    const container = document.getElementById('vlab-main-container');
    if (!container) return;
    if (!document.fullscreenElement) {
      if (container.requestFullscreen) {
        container.requestFullscreen();
      } else if (container.webkitRequestFullscreen) {
        container.webkitRequestFullscreen();
      }
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
      }
    }
  }

  // --- 8. DOM Initialization & Event Handlers ---
  function initLab() {
    // Mode Switcher Tabs
    const tabFrac = document.getElementById('vlab-tab-fractions');
    const tabPrimes = document.getElementById('vlab-tab-primes');

    const viewFrac = document.getElementById('vlab-view-fractions');
    const viewPrimes = document.getElementById('vlab-view-primes');

    // Auto-detect active tab on standalone pages
    if (!viewFrac && viewPrimes) {
      state.activeTab = 'primes';
    } else {
      state.activeTab = 'fractions';
    }

    if (tabFrac) tabFrac.onclick = () => setActiveTab('fractions');
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

    const simpFracBtn = document.getElementById('vlab-btn-simp');
    if (simpFracBtn) simpFracBtn.onclick = fractionSimp;

    const mixedFracBtn = document.getElementById('vlab-btn-mixed');
    if (mixedFracBtn) mixedFracBtn.onclick = fractionMixedToggle;

    const improperFracBtn = document.getElementById('vlab-btn-improper');
    if (improperFracBtn) improperFracBtn.onclick = fractionImproper;

    const invertFracBtn = document.getElementById('vlab-btn-invert');
    if (invertFracBtn) invertFracBtn.onclick = fractionInvert;

    // Fraction Direct Type Bar
    const fracInput = document.getElementById('vlab-frac-input');
    const fracBtnAdd = document.getElementById('vlab-btn-frac-add');
    if (fracInput) {
      fracInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          loadFractionDirect(fracInput.value);
          fracInput.value = '';
        }
      });
    }
    if (fracBtnAdd && fracInput) {
      fracBtnAdd.onclick = () => {
        loadFractionDirect(fracInput.value);
        fracInput.value = '';
      };
    }

    // Operations Keypads (All Tabs)
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

    // Prime Direct Type Bar
    const primeInput = document.getElementById('vlab-prime-input');
    const primeBtnAdd = document.getElementById('vlab-btn-prime-add');
    if (primeInput) {
      primeInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          loadPrimeDirect(primeInput.value);
          primeInput.value = '';
        }
      });
    }
    if (primeBtnAdd && primeInput) {
      primeBtnAdd.onclick = () => {
        loadPrimeDirect(primeInput.value);
        primeInput.value = '';
      };
    }

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
    removeFractionFromY: removeFractionFromY,
    dropTopFraction: dropTopFractionFromX,
    clearStagingFractions: clearFractionX,
    clearFractions: clearFractionX,
    pushFraction: pushFractionToStack,
    simpFraction: fractionSimp,
    toggleMixed: fractionMixedToggle,
    toggleImproper: fractionImproper,
    invertFraction: fractionInvert,
    loadFractionDirect: loadFractionDirect,

    addPrime: addPrimeToX,
    removePrimeFromX: removePrimeFromX,
    removePrimeFromY: removePrimeFromY,
    removeLastPrime: dropTopPrimeFromX,
    dropTopPrime: dropTopPrimeFromX,
    clearPrimes: clearPrimeX,
    pushPrimes: pushPrimeToStack,
    factorizeStackX: primeFactorizeX,
    commonFactors: primeCommonFactors,
    calcGcd: primeGcd,
    calcLcm: primeLcm,
    loadPrimeDirect: loadPrimeDirect,

    pushValue: (v) => rpnPushRaw(v, 1, v),
    setActiveTab: setActiveTab,
    op: rpnOp,
    swap: rpnSwap,
    drop: rpnDrop,
    clearStack: rpnClear,
    toggleFullscreen: toggleFullscreen,

    // No-op compatibility stubs for legacy tests
    changePvCount: () => {},
    setPvNumber: () => {},
    removePvBlock: () => {},
    autoRegroupPv: () => {},
    unbundlePv: () => {},
    clearPv: () => {},
    getPvTotal: () => 0,
    pushPvToStack: () => {},
    addPvRows: () => {},
    subtractPvRows: () => {},
    multiplyPvRows: () => {}
  };
})();
