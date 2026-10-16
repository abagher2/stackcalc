/* ==========================================================================
   StackCalc Ecommerce & Product Gallery Interactions
   Includes Web Audio Synthesized Mechanical Detents & Interactive Tactile Sandboxes
   100% Static & Compatible with GitHub Pages
   ========================================================================== */

// 1. Web Audio API Mechanical Click Synthesizer (Zero External Assets)
let audioCtx = null;
let soundEnabled = true;

function playSnapSound(pitch = 380, volume = 0.22) {
  if (!soundEnabled) return;
  try {
    if (!audioCtx) {
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }

    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    const filter = audioCtx.createBiquadFilter();

    osc.type = 'triangle';
    osc.frequency.setValueAtTime(pitch, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(70, audioCtx.currentTime + 0.038);

    filter.type = 'bandpass';
    filter.frequency.setValueAtTime(1400, audioCtx.currentTime);
    filter.Q.setValueAtTime(3.5, audioCtx.currentTime);

    gain.gain.setValueAtTime(volume, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.042);

    osc.connect(filter);
    filter.connect(gain);
    gain.connect(audioCtx.destination);

    osc.start();
    osc.stop(audioCtx.currentTime + 0.045);
  } catch (e) {
    // AudioContext blocked or not supported on device
  }
}

function initEcommerceInteractions() {
  // 1. Gallery Thumbnail Click & Keyboard Navigation
  const thumbs = document.querySelectorAll('.ec-gallery-thumb');
  const mainImg = document.getElementById('main-product-image');

  if (thumbs.length && mainImg) {
    thumbs.forEach(thumb => {
      if (!thumb.hasAttribute('tabindex')) {
        thumb.setAttribute('tabindex', '0');
        thumb.setAttribute('role', 'button');
      }

      thumb.onclick = function (e) {
        const img = thumb.querySelector('img');
        if (img && img.src) {
          playSnapSound(520, 0.12);
          mainImg.style.transition = 'opacity 0.15s ease';
          mainImg.style.opacity = '0.6';
          mainImg.src = img.src;
          setTimeout(() => { mainImg.style.opacity = '1'; }, 80);
          thumbs.forEach(t => t.classList.remove('active'));
          thumb.classList.add('active');
        }
      };

      thumb.onkeydown = function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          thumb.click();
        }
      };
    });
  }

  // 2. Colorway Swatch Chips Click Interactions
  const swatches = document.querySelectorAll('.ec-swatch-chip');
  if (swatches.length) {
    swatches.forEach(swatch => {
      if (!swatch.hasAttribute('tabindex')) {
        swatch.setAttribute('tabindex', '0');
        swatch.setAttribute('role', 'button');
      }

      swatch.addEventListener('click', function () {
        playSnapSound(440, 0.14);
        swatches.forEach(s => s.classList.remove('active'));
        swatch.classList.add('active');
      });

      swatch.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          swatch.click();
        }
      });
    });
  }

  // 3. Interactive Domino Doubling & Regrouping Simulator
  initDominoSimulator();

  // 4. Interactive Ten-Frame Simulator
  initTenFrameSimulator();

  // 5. Mobile Sticky Buy Bar (High-Conversion Floating Action Dock)
  initStickyBuyBar();

  // 6. Catalog Filter Nav (Safe Fallback)
  window.filterCatalog = window.filterCatalog || function (category, btn) {
    const cards = document.querySelectorAll('.te-card');
    const buttons = document.querySelectorAll('.te-filter-btn');

    buttons.forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');

    cards.forEach(card => {
      if (category === 'all') {
        card.style.display = '';
      } else {
        const cardCat = card.getAttribute('data-category');
        if (cardCat === category) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      }
    });
  };
}

// Interactive Domino Doubling Simulator
function initDominoSimulator() {
  const container = document.getElementById('domino-interactive-sandbox');
  if (!container) return;

  const doubleTiles = [
    { id: '1-1', pips: 1, sum: 2, label: '1+1' },
    { id: '2-2', pips: 2, sum: 4, label: '2+2' },
    { id: '3-3', pips: 3, sum: 6, label: '3+3' },
    { id: '4-4', pips: 4, sum: 8, label: '4+4' },
    { id: '5-5', pips: 5, sum: 10, label: '5+5' },
    { id: '6-6', pips: 6, sum: 12, label: '6+6' }
  ];

  let snapped = {};

  function render() {
    const socketsEl = document.getElementById('domino-lid-sockets');
    const poolEl = document.getElementById('domino-tile-pool');
    const trayEl = document.getElementById('domino-tray-cells');
    const statusEl = document.getElementById('domino-sim-status');

    if (!socketsEl || !poolEl || !trayEl) return;

    // Render Sockets on Doubling Lid
    socketsEl.innerHTML = '';
    doubleTiles.forEach(tile => {
      const isFilled = snapped[tile.id];
      const socket = document.createElement('div');
      socket.className = 'domino-socket ' + (isFilled ? 'filled' : 'empty');
      socket.innerHTML = `
        <div class="socket-expr">${tile.label}</div>
        <div class="socket-sum">${isFilled ? tile.sum : '&bull;'}</div>
      `;
      socket.title = `Doubles Socket: ${tile.label} = ${tile.sum}`;
      if (isFilled) {
        socket.onclick = () => {
          delete snapped[tile.id];
          playSnapSound(280, 0.18);
          render();
        };
      }
      socketsEl.appendChild(socket);
    });

    // Render Unsnapped Tiles Pool
    poolEl.innerHTML = '';
    doubleTiles.forEach(tile => {
      if (!snapped[tile.id]) {
        const tBtn = document.createElement('button');
        tBtn.type = 'button';
        tBtn.className = 'domino-tile-sim';
        tBtn.innerHTML = `
          <span class="pip-cluster">${tile.pips}</span>
          <span class="divider">|</span>
          <span class="pip-cluster">${tile.pips}</span>
        `;
        tBtn.title = `Click to snap [${tile.pips}|${tile.pips}] into lid socket`;
        tBtn.onclick = () => {
          snapped[tile.id] = true;
          playSnapSound(480 + tile.pips * 40, 0.24);
          render();
        };
        poolEl.appendChild(tBtn);
      }
    });

    // Render 12-Frame Tray Cells (6x2)
    trayEl.innerHTML = '';
    // Calculate total pips from active highest snapped double or selected
    const activeSnapped = Object.keys(snapped);
    let totalPips = 0;
    if (activeSnapped.length > 0) {
      const lastKey = activeSnapped[activeSnapped.length - 1];
      const found = doubleTiles.find(t => t.id === lastKey);
      if (found) totalPips = found.sum;
    }

    for (let i = 1; i <= 12; i++) {
      const cell = document.createElement('div');
      const isFilled = i <= totalPips;
      const isBridge = i === 10;
      cell.className = 'tray-cell ' + (isFilled ? 'filled' : 'empty') + (isBridge ? ' bridge-ten' : '');
      cell.innerHTML = `
        <span class="cell-num">${i}</span>
        ${isFilled ? '<span class="cell-pip">●</span>' : ''}
      `;
      trayEl.appendChild(cell);
    }

    // Status Message
    if (statusEl) {
      const count = Object.keys(snapped).length;
      if (count === 0) {
        statusEl.innerHTML = '👉 Click any double tile to snap it into its calibrated lid socket.';
      } else if (count === 6) {
        statusEl.innerHTML = '🎉 <strong>All 6 doubles verified!</strong> 1+1 through 6+6 self-corrected with tactile mechanical detents.';
      } else {
        const lastKey = activeSnapped[activeSnapped.length - 1];
        const t = doubleTiles.find(x => x.id === lastKey);
        if (t.sum <= 10) {
          statusEl.innerHTML = `✅ <strong>${t.label} = ${t.sum}</strong> &bull; Fits within base-10 stage.`;
        } else {
          statusEl.innerHTML = `🌟 <strong>${t.label} = ${t.sum}</strong> &bull; <em>Bridges through 10!</em> (10 + ${t.sum - 10} = ${t.sum})`;
        }
      }
    }
  }

  // Audio Toggle
  const soundBtn = document.getElementById('domino-sound-toggle');
  if (soundBtn) {
    soundBtn.onclick = () => {
      soundEnabled = !soundEnabled;
      soundBtn.textContent = soundEnabled ? '🔊 Sound: ON' : '🔇 Sound: OFF';
      if (soundEnabled) playSnapSound(500, 0.2);
    };
  }

  const resetBtn = document.getElementById('domino-sim-reset');
  if (resetBtn) {
    resetBtn.onclick = () => {
      snapped = {};
      playSnapSound(220, 0.15);
      render();
    };
  }

  render();
}

// Interactive Ten-Frame Simulator
function initTenFrameSimulator() {
  const container = document.getElementById('tenframe-interactive-sandbox');
  if (!container) return;

  let activeCount = 5;
  const maxCells = 10;

  function render() {
    const gridEl = document.getElementById('tenframe-grid-cells');
    const counterEl = document.getElementById('tenframe-count-display');
    const statusEl = document.getElementById('tenframe-sim-status');

    if (!gridEl) return;
    gridEl.innerHTML = '';

    for (let i = 1; i <= maxCells; i++) {
      const cell = document.createElement('div');
      const isFilled = i <= activeCount;
      const isTopFive = i <= 5;
      cell.className = 'tenframe-sim-cell ' + (isFilled ? 'filled' : 'empty');
      cell.innerHTML = isFilled ? `<div class="token-disc ${isTopFive ? 'ocean-teal' : 'coral'}"></div>` : '';
      cell.title = `Slot ${i}: Click to toggle token`;
      cell.onclick = () => {
        if (isFilled && i === activeCount) {
          activeCount--;
          playSnapSound(260, 0.15);
        } else {
          activeCount = i;
          playSnapSound(360 + i * 30, 0.18);
        }
        render();
      };
      gridEl.appendChild(cell);
    }

    if (counterEl) {
      counterEl.textContent = `${activeCount} / 10`;
    }

    if (statusEl) {
      if (activeCount === 10) {
        statusEl.innerHTML = '⭐ <strong>Complete Ten!</strong> Ready to lift onto the elevated carry shelf (1 ten, 0 ones).';
      } else if (activeCount === 5) {
        statusEl.innerHTML = '⚖️ <strong>Benchmark Five:</strong> First row full (5 teal tokens). Intuitive 5-anchor structure.';
      } else {
        const remaining = 10 - activeCount;
        statusEl.innerHTML = `<strong>Number Bond:</strong> ${activeCount} + ${remaining} = 10.`;
      }
    }
  }

  const addBtn = document.getElementById('tenframe-add-token');
  if (addBtn) {
    addBtn.onclick = () => {
      if (activeCount < 10) {
        activeCount++;
        playSnapSound(360 + activeCount * 30, 0.18);
        render();
      }
    };
  }

  const clearBtn = document.getElementById('tenframe-clear-tokens');
  if (clearBtn) {
    clearBtn.onclick = () => {
      activeCount = 0;
      playSnapSound(200, 0.12);
      render();
    };
  }

  render();
}

// 5. Mobile Sticky Buy Bar (High-Conversion Floating Action Dock)
function initStickyBuyBar() {
  const buyBox = document.querySelector('.ec-buybox');
  const mainImg = document.getElementById('main-product-image');
  const titleEl = document.querySelector('.ec-product-title');
  const priceEl = document.querySelector('.ec-price-current');
  const primaryBtn = document.querySelector('.ec-btn-primary');

  if (!buyBox || !primaryBtn) return;

  let bar = document.querySelector('.ec-sticky-bar');
  if (!bar) {
    bar = document.createElement('div');
    bar.className = 'ec-sticky-bar';
    const imgSrc = mainImg ? mainImg.src : '';
    const rawTitle = titleEl ? titleEl.textContent.trim() : 'Product';
    const titleMap = {
      'SC-32 Scientific RPN Maker Kit': 'SC-32 Maker Kit',
      'Fraction Studio Proportional Towers': 'Fraction Studio',
      'Ten-Frame Dual Stage & Carry Shelf': 'Ten-Frames',
      'Math Domino Studio & 12-Frame Set': 'Math Dominoes',
      'Counting Tiles & Planar Array Studio': 'Counting Tiles',
      'Sectional Classroom Planetary Clock': 'Planetary Clock',
      'Prime Factor Studio & Slide Rule Comparator': 'Prime Studio',
      'Algebra Factoring Studio & Tiles': 'Algebra Boxes',
      'Unit Circle Trigonometry Volvelle': 'Unit Circle Volvelle',
      'Probability Dice & Modular Spinner Pack': 'Dice & Spinners',
      'SC-6 Elementary Calculator': 'SC-6 Elementary'
    };
    const titleText = titleMap[rawTitle] || (rawTitle.length > 20 ? rawTitle.slice(0, 18) + '...' : rawTitle);
    const priceText = priceEl ? priceEl.textContent.trim() : '$89.00';
    const btnHref = primaryBtn.getAttribute('href') || 'https://www.etsy.com/shop/StackCalc';

    bar.innerHTML = `
      <div class="ec-sticky-info">
        ${imgSrc ? `<img src="${imgSrc}" class="ec-sticky-thumb" alt="${titleText}">` : ''}
        <div class="ec-sticky-text">
          <div class="ec-sticky-title" title="${rawTitle}">${titleText}</div>
          <div class="ec-sticky-price">${priceText}</div>
        </div>
      </div>
      <a href="${btnHref}" target="_blank" rel="noopener noreferrer" class="ec-sticky-btn">
        ORDER ON ETSY ↗
      </a>
    `;
    document.body.appendChild(bar);
  }

  // Observe primary button so floating dock pops up smoothly the instant buy CTA leaves view
  const triggerEl = primaryBtn;
  function updateStickyBar() {
    if (!triggerEl || !bar) return;
    const rect = triggerEl.getBoundingClientRect();
    if (rect.bottom < 0) {
      bar.classList.add('visible');
    } else {
      bar.classList.remove('visible');
    }
  }

  window.addEventListener('scroll', updateStickyBar, { passive: true });
  updateStickyBar();

  if ('IntersectionObserver' in window && triggerEl) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting && entry.boundingClientRect.top < 0) {
          bar.classList.add('visible');
        } else {
          bar.classList.remove('visible');
        }
      });
    }, { threshold: 0 });

    observer.observe(triggerEl);
  }
}

// Initialize on standard DOM load
document.addEventListener('DOMContentLoaded', initEcommerceInteractions);

// Hook into Material for MkDocs reactive navigation
if (typeof document$ !== 'undefined') {
  document$.subscribe(initEcommerceInteractions);
}
