#!/usr/bin/env python3
"""
PATCH V6 — NOVUS CAPITAL LUXE
Rounded cards, light sections, luxury signals, button logic, ticker fix
"""
import re, sys

filepath = r"C:\vantage-clean\crm-v2-push\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

tpl5_start = content.index("TPL_ECOM_HTML['5']")
tpl9_start = content.index("TPL_ECOM_HTML['9']")
tpl = content[tpl5_start:tpl9_start]

def esc(s):
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')

print("Template size before:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 1: Inject V6 CSS before </style>
# ═══════════════════════════════════════════════════

css_block = r"""

/* ════════ V6 — CREAM VARIABLES ════════ */
:root {
  --cream-bg: #F0EBE3;
  --cream-text: #1a2535;
  --cream-muted: #7a8a9a;
  --r-sm: 6px;
  --r-md: 12px;
  --r-lg: 18px;
  --r-xl: 24px;
  --r-full: 999px;
  --ticker-h: 3.6rem;
  --nav-h: 7rem;
  --space-section: 16rem;
}

/* ════════ SECTION CLAIRE ════════ */
.about--light {
  background: #EEE8DF !important;
  color: #0B1720;
  position: relative;
}
.about--light .about__h { color: #0B1720; }
.about--light .about__h em { color: var(--sage); font-style: italic; }
.about--light .about__p { color: rgba(11,23,32,.55); }
.about--light .s-tag::before { background: var(--sage); }
.about--light .s-tag span { color: var(--sage); }
.about--light .i-stat__n { color: var(--sage); }
.about--light .i-stat__l { color: rgba(11,23,32,.4); }
.about--light .a-tag {
  background: rgba(11,23,32,.06);
  border-color: rgba(11,23,32,.12);
  color: rgba(11,23,32,.55);
}
.about--light .about__img {
  box-shadow: 0 24px 60px rgba(11,23,32,.15), 0 8px 20px rgba(11,23,32,.1);
}
.about--light .watermark-num {
  -webkit-text-stroke: 1px rgba(11,23,32,.04);
}

.section-transition-top {
  height: 120px;
  background: linear-gradient(to bottom, var(--deep) 0%, #EEE8DF 100%);
}
.section-transition-bottom {
  height: 120px;
  background: linear-gradient(to bottom, #EEE8DF 0%, var(--deep) 100%);
}

/* ════════ LAYERED SHADOWS ════════ */
.shadow-depth-sm {
  box-shadow:
    0 1px 2px rgba(8,15,20,.1),
    0 2px 4px rgba(8,15,20,.08),
    0 4px 8px rgba(8,15,20,.06),
    0 8px 16px rgba(8,15,20,.04);
  transition: box-shadow .4s var(--ease-out), transform .4s var(--ease-out);
}
.shadow-depth-sm:hover {
  box-shadow:
    0 2px 4px rgba(8,15,20,.12),
    0 4px 8px rgba(8,15,20,.1),
    0 8px 16px rgba(8,15,20,.08),
    0 16px 32px rgba(8,15,20,.06),
    0 0 0 1px rgba(61,139,122,.15);
  transform: translateY(-4px);
}
.shadow-depth-lg {
  box-shadow:
    0 1px 2px rgba(8,15,20,.15),
    0 4px 8px rgba(8,15,20,.12),
    0 8px 16px rgba(8,15,20,.1),
    0 16px 32px rgba(8,15,20,.08),
    0 32px 64px rgba(8,15,20,.06),
    inset 0 1px 0 rgba(245,242,237,.06);
  transition: box-shadow .5s var(--ease-out), transform .5s var(--ease-out);
}
.shadow-depth-lg:hover {
  box-shadow:
    0 2px 4px rgba(8,15,20,.18),
    0 8px 16px rgba(8,15,20,.14),
    0 16px 32px rgba(8,15,20,.12),
    0 32px 64px rgba(8,15,20,.1),
    0 48px 96px rgba(8,15,20,.06),
    0 0 40px rgba(61,139,122,.12),
    inset 0 1px 0 rgba(245,242,237,.08);
  transform: translateY(-6px);
}

/* ════════ LUXURY BORDER ════════ */
.card-luxury-border { position: relative; }
.card-luxury-border::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(135deg,
    rgba(245,242,237,.18) 0%,
    rgba(61,139,122,.2) 30%,
    rgba(245,242,237,.04) 60%,
    rgba(196,113,79,.1) 100%
  );
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
  pointer-events: none;
  z-index: 1;
}

/* ════════ ROUNDED CARDS ════════ */
.prop-stacked__item { border-radius: var(--r-lg); overflow: hidden; }
.psi__img-wrap { border-radius: var(--r-lg) var(--r-lg) 0 0; overflow: hidden; }
.wi { border-radius: var(--r-md); overflow: hidden; }
.flip-card__front, .flip-card__back { border-radius: var(--r-lg); }
.flip-card__inner { border-radius: var(--r-lg); }
.pipeline-card { border-radius: var(--r-sm); }
.client-folder__outer { border-radius: var(--r-md); }
.client-folder__tab { border-radius: 4px 4px 0 0; }
.hero__card { border-radius: var(--r-xl); box-shadow: 0 8px 32px rgba(8,15,20,.4), inset 0 1px 0 rgba(245,242,237,.08); }
.metric-block { border-radius: var(--r-md); }
.i-stat { border-radius: var(--r-sm); }
.crm-modal-inner { border-radius: var(--r-xl); }
.acrm-panel { border-radius: var(--r-xl) 0 0 var(--r-xl); }
.testi__layout { border-radius: var(--r-lg); overflow: hidden; }
.activity-item { border-radius: var(--r-sm); }
.booking-widget { border-radius: var(--r-md); }
.s-tag, .hero__eyebrow, .prop-card__tag, .psi__type-tag, .psi__avail-tag, .featured__tag {
  border-radius: var(--r-full);
  padding-left: 1.4rem;
  padding-right: 1.4rem;
}
.btn-blob, .btn-circle, .nav__btn, .nav__agent-btn { border-radius: var(--r-full); }
.btn-mag, .btn-cut, .pipeline-add-btn { border-radius: var(--r-sm); }

/* ════════ SECTION ORNAMENT ════════ */
.section-ornament {
  display: flex;
  align-items: center;
  gap: 1.6rem;
  padding: 2.4rem 5.6rem;
}
.so-line {
  flex: 1;
  height: 1px;
  background: linear-gradient(to right, transparent, rgba(61,139,122,.2), rgba(61,139,122,.4), rgba(61,139,122,.2), transparent);
}
.so-diamond {
  width: 8px;
  height: 8px;
  background: var(--sage);
  transform: rotate(45deg);
  flex-shrink: 0;
  box-shadow: 0 0 12px rgba(61,139,122,.4);
}

/* ════════ TRUST BAR ════════ */
.trust-bar {
  display: flex;
  align-items: center;
  gap: 4rem;
  padding: 2.4rem 5.6rem;
  border-top: 1px solid rgba(245,242,237,.05);
  border-bottom: 1px solid rgba(245,242,237,.05);
  background: var(--void);
  overflow: hidden;
}
.trust-bar__label {
  font-family: var(--font-m);
  font-size: .8rem;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: rgba(245,242,237,.2);
  flex-shrink: 0;
  white-space: nowrap;
}
.trust-bar__logos {
  display: flex;
  align-items: center;
  gap: 3.2rem;
  flex: 1;
}
.trust-logo {
  font-family: var(--font-m);
  font-size: 1rem;
  letter-spacing: .25em;
  text-transform: uppercase;
  color: rgba(245,242,237,.25);
  transition: color .4s;
  white-space: nowrap;
}
.trust-logo:hover { color: rgba(245,242,237,.55); }
.trust-sep {
  width: 1px;
  height: 16px;
  background: rgba(245,242,237,.1);
  flex-shrink: 0;
}

/* ════════ PRICE LUXURY ════════ */
.price-luxury {
  display: flex;
  align-items: baseline;
  gap: .4rem;
}
.price-luxury__currency {
  font-family: var(--font-m);
  font-size: .7em;
  letter-spacing: .1em;
  color: var(--champ);
  opacity: .7;
}
.price-luxury__amount {
  font-family: var(--font-d);
  font-size: 1em;
  font-weight: 300;
  color: var(--champ);
}
.price-luxury__period {
  font-family: var(--font-m);
  font-size: .55em;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: rgba(212,184,150,.5);
}

/* ════════ WATERMARK NUMBER ════════ */
.watermark-num {
  position: absolute;
  font-family: var(--font-d);
  font-size: 28vw;
  font-weight: 300;
  line-height: 1;
  color: transparent;
  -webkit-text-stroke: 1px rgba(61,139,122,.06);
  pointer-events: none;
  user-select: none;
  z-index: 0;
  white-space: nowrap;
}
section:hover .watermark-num {
  -webkit-text-stroke: 1px rgba(61,139,122,.1);
}

/* ════════ TICKER SMART HIDE ════════ */
.stock-ticker.hidden {
  transform: translateY(-100%) !important;
  pointer-events: none;
}
.header.ticker-hidden {
  top: 0 !important;
}

/* ════════ TYPOGRAPHY HIERARCHY ════════ */
p, .about__p, .featured__desc { max-width: 52ch; }

/* ════════ KEN BURNS ════════ */
.hero__right-img img, .pb__bg img {
  animation: ken-burns-v6 20s ease-in-out infinite alternate;
  transform-origin: center;
}
@keyframes ken-burns-v6 {
  0%   { transform: scale(1) translateX(0) translateY(0); }
  25%  { transform: scale(1.06) translateX(-1%) translateY(-1%); }
  50%  { transform: scale(1.04) translateX(1%) translateY(-2%); }
  75%  { transform: scale(1.07) translateX(-2%) translateY(1%); }
  100% { transform: scale(1.05) translateX(.5%) translateY(-.5%); }
}
.hero__right-img:hover img { animation-play-state: paused; }

/* ════════ WI HOVER EFFECTS ════════ */
.wi img {
  transition: transform .9s cubic-bezier(.16,1,.3,1), filter .5s ease;
  filter: saturate(.75) brightness(.85);
}
.wi:hover img {
  transform: scale(1.06);
  filter: saturate(1.1) brightness(1) contrast(1.05);
}
.wi::before {
  content: "";
  position: absolute;
  top: 0; left: -100%;
  width: 50%; height: 100%;
  background: linear-gradient(105deg, transparent 40%, rgba(245,242,237,.06) 50%, rgba(245,242,237,.03) 55%, transparent 65%);
  z-index: 3; transition: left .7s ease; pointer-events: none;
}
.wi:hover::before { left: 160%; }

/* ════════ HERO GRAIN ════════ */
.hero__right::after {
  content: "";
  position: absolute;
  inset: 0; z-index: 3; pointer-events: none;
  opacity: .045;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23g)'/%3E%3C/svg%3E");
  background-size: 160px 160px;
  animation: grain-shift-v6 .5s steps(2) infinite;
}
@keyframes grain-shift-v6 {
  0%   { background-position: 0 0; }
  25%  { background-position: 40px 60px; }
  50%  { background-position: -60px 40px; }
  75%  { background-position: 80px -40px; }
  100% { background-position: -40px 80px; }
}

/* ════════ V6 RESPONSIVE ════════ */
@media (max-width: 768px) {
  .trust-bar { flex-direction: column; gap: 1.6rem; padding: 2rem 3rem; }
  .section-ornament { padding: 1.6rem 3rem; }
  .section-transition-top, .section-transition-bottom { height: 60px; }
}
"""

css_escaped = esc(css_block)
style_marker = '</style>'
style_pos = tpl.index(style_marker)
tpl = tpl[:style_pos] + css_escaped + tpl[style_pos:]
print("Step 1: CSS injected. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 2: Add about--light class to about section
# ═══════════════════════════════════════════════════

old_about = 'class="about" id="about"'
new_about = 'class="about about--light" id="about"'
tpl = tpl.replace(old_about, new_about, 1)
print("Step 2: about--light class added")

# ═══════════════════════════════════════════════════
# STEP 3: Insert transition divs + ornaments around about
# ═══════════════════════════════════════════════════

# Insert transition-top before about section
about_section_pos = tpl.index('class="about about--light"')
about_tag_start = tpl[:about_section_pos].rindex('<')

transition_top = esc('\n<div class="section-transition-top"></div>\n<div class="section-ornament" aria-hidden="true"><div class="so-line"></div><div class="so-diamond"></div><div class="so-line"></div></div>\n')
tpl = tpl[:about_tag_start] + transition_top + tpl[about_tag_start:]
print("Step 3a: Transition top + ornament before about. Size:", len(tpl))

# Find the end of about section to add transition-bottom
# About ends at next <section or <div class="scroll-wheel
# Let's find what comes after about
props_marker = 'id="properties"'
props_pos = tpl.index(props_marker)
props_tag = tpl[:props_pos].rindex('<')

# But there's a scroll-wheel-wrap between about and properties (from V5)
# Let's find scroll-wheel-wrap
wheel_marker = 'id="sww"'
try:
    wheel_pos = tpl.index(wheel_marker)
    wheel_tag = tpl[:wheel_pos].rindex('<')
    insert_after_about = wheel_tag
except ValueError:
    insert_after_about = props_tag

transition_bottom = esc('\n<div class="section-ornament" aria-hidden="true"><div class="so-line"></div><div class="so-diamond"></div><div class="so-line"></div></div>\n<div class="section-transition-bottom"></div>\n')
tpl = tpl[:insert_after_about] + transition_bottom + tpl[insert_after_about:]
print("Step 3b: Transition bottom after about. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 4: Insert trust bar after hero section
# ═══════════════════════════════════════════════════

# Find end of hero - look for the section or div after hero
# Hero ends before the metrics section or the horizontal scroll section
metrics_marker = 'id="hero-metrics"'
try:
    metrics_pos = tpl.index(metrics_marker)
    metrics_tag = tpl[:metrics_pos].rindex('<')
except ValueError:
    metrics_marker = 'id="metrics"'
    metrics_pos = tpl.index(metrics_marker)
    metrics_tag = tpl[:metrics_pos].rindex('<')

trust_bar = esc('\n<div class="trust-bar"><div class="trust-bar__label">Trusted by</div><div class="trust-bar__logos"><span class="trust-logo">EURONEXT</span><div class="trust-sep"></div><span class="trust-logo">SIIC</span><div class="trust-sep"></div><span class="trust-logo">INREV</span><div class="trust-sep"></div><span class="trust-logo">AMF</span><div class="trust-sep"></div><span class="trust-logo">RICS</span></div></div>\n')
tpl = tpl[:metrics_tag] + trust_bar + tpl[metrics_tag:]
print("Step 4: Trust bar inserted after hero. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 5: Add ornaments between other sections
# ═══════════════════════════════════════════════════

ornament = esc('\n<div class="section-ornament" aria-hidden="true"><div class="so-line"></div><div class="so-diamond"></div><div class="so-line"></div></div>\n')

# Before performance
perf_marker = 'id="performance"'
perf_pos = tpl.index(perf_marker)
perf_tag = tpl[:perf_pos].rindex('<')
tpl = tpl[:perf_tag] + ornament + tpl[perf_tag:]
print("Step 5a: Ornament before performance. Size:", len(tpl))

# Before contact/CTA
contact_marker = 'id="contact"'
contact_pos = tpl.index(contact_marker)
contact_tag = tpl[:contact_pos].rindex('<')
tpl = tpl[:contact_tag] + ornament + tpl[contact_tag:]
print("Step 5b: Ornament before contact. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 6: Inject V6 JavaScript before last \x3c/script>
# ═══════════════════════════════════════════════════

# Find the last \x3c/script>
scripts = list(re.finditer(re.escape('\\x3c/script>'), tpl))
if not scripts:
    print("ERROR: No script close found!")
    sys.exit(1)
last_script_pos = scripts[-1].start()

js_block = r"""

/* ════════════════════════════════════════════════════
   V6 LUXE — TICKER + SPOTLIGHT + BUTTONS + DEPTH
════════════════════════════════════════════════════ */

/* TICKER SMART HIDE/SHOW */
function initSmartTickerFinal() {
  var ticker = document.querySelector('.stock-ticker');
  var header = document.querySelector('.header');
  if (!ticker || !header) return;
  var lastY = 0;
  var isHidden = false;
  var THRESHOLD = 10;
  var HYSTERESIS = 60;
  function update() {
    var currentY = (typeof lenis !== 'undefined') ? lenis.animatedScroll : window.scrollY;
    if (currentY <= 5) {
      if (isHidden) {
        ticker.classList.remove('hidden');
        header.classList.remove('ticker-hidden');
        isHidden = false;
      }
      lastY = currentY;
      return;
    }
    var delta = currentY - lastY;
    if (delta > THRESHOLD && !isHidden) {
      ticker.classList.add('hidden');
      header.classList.add('ticker-hidden');
      isHidden = true;
    } else if (delta < -HYSTERESIS && isHidden) {
      ticker.classList.remove('hidden');
      header.classList.remove('ticker-hidden');
      isHidden = false;
    }
    lastY = currentY;
  }
  var rafPending = false;
  function onScroll() {
    if (!rafPending) {
      requestAnimationFrame(function() { update(); rafPending = false; });
      rafPending = true;
    }
  }
  if (typeof lenis !== 'undefined') {
    lenis.on('scroll', onScroll);
  } else {
    window.addEventListener('scroll', onScroll, { passive: true });
  }
}

/* SECTION SPOTLIGHT */
function initSectionSpotlight() {
  var spotlight = document.createElement('div');
  spotlight.style.cssText = 'position:fixed;width:800px;height:800px;border-radius:50%;background:radial-gradient(circle,rgba(61,139,122,.04) 0%,transparent 70%);pointer-events:none;z-index:0;transform:translate(-50%,-50%);will-change:transform;';
  document.body.appendChild(spotlight);
  var sx = window.innerWidth / 2;
  var sy = window.innerHeight / 2;
  window.addEventListener('mousemove', function(e) {
    sx += (e.clientX - sx) * .03;
    sy += (e.clientY - sy) * .03;
    gsap.set(spotlight, { x: sx, y: sy });
  });
}

/* BUTTON TEXT UPGRADE */
function upgradeButtonTexts() {
  var upgrades = [
    ['.nav__btn', 'Private Access \u2192'],
    ['#pipeline-add', '+ Add Prospect'],
    ['#client-add', '+ Open Client File'],
    ['.bw-confirm-btn', 'Reserve This Date \u2192'],
    ['.su-submit', 'Find My Property \u2192'],
    ['.vtour-btn', '3D Walkthrough \u2B21']
  ];
  upgrades.forEach(function(u) {
    document.querySelectorAll(u[0]).forEach(function(el) {
      if (el.children.length === 0) el.textContent = u[1];
    });
  });
}

/* BUTTON ACTIONS */
function assignButtonActions() {
  var heroFill = document.querySelector('.hero__actions .btn--fill');
  if (heroFill) heroFill.addEventListener('click', function(e) {
    e.preventDefault();
    if (typeof lenis !== 'undefined') lenis.scrollTo('#properties', { offset: -80, duration: 1.4 });
  });
  var heroLine = document.querySelector('.hero__actions .btn--line');
  if (heroLine) heroLine.addEventListener('click', function(e) {
    e.preventDefault();
    if (typeof lenis !== 'undefined') lenis.scrollTo('#performance', { offset: -80, duration: 1.4 });
  });
}

/* SPECULAR HIGHLIGHT on featured/hero card */
function initFeaturedCardShine() {
  var cards = document.querySelectorAll('.hero__card, .featured__main-img');
  cards.forEach(function(card) {
    var shine = document.createElement('div');
    shine.style.cssText = 'position:absolute;inset:0;pointer-events:none;z-index:5;opacity:0;transition:opacity .3s;background:radial-gradient(circle at var(--sx,50%) var(--sy,50%),rgba(245,242,237,.12) 0%,rgba(245,242,237,.04) 30%,transparent 60%);';
    card.style.position = 'relative';
    card.style.overflow = 'hidden';
    card.appendChild(shine);
    card.addEventListener('mousemove', function(e) {
      var r = card.getBoundingClientRect();
      shine.style.setProperty('--sx', ((e.clientX - r.left) / r.width * 100) + '%');
      shine.style.setProperty('--sy', ((e.clientY - r.top) / r.height * 100) + '%');
      shine.style.opacity = '1';
    });
    card.addEventListener('mouseleave', function() { shine.style.opacity = '0'; });
  });
}

/* DEPTH OF FIELD on stacked properties */
function initDepthOfField() {
  var items = document.querySelectorAll('.prop-stacked__item');
  if (!items.length) return;
  items.forEach(function(item) {
    ScrollTrigger.create({
      trigger: item,
      start: 'top 60%',
      end: 'bottom 40%',
      onEnter: function() { focusItem(item, true); },
      onLeave: function() { focusItem(item, false); },
      onEnterBack: function() { focusItem(item, true); },
      onLeaveBack: function() { focusItem(item, false); }
    });
  });
  function focusItem(activeItem, focus) {
    items.forEach(function(item) {
      var img = item.querySelector('.psi__img img');
      if (!img) return;
      if (item === activeItem) {
        gsap.to(img, { filter: 'blur(0px) saturate(1) brightness(1)', duration: .6 });
        gsap.to(item, { opacity: 1, duration: .4 });
      } else {
        gsap.to(img, { filter: 'blur(2px) saturate(.6) brightness(.7)', duration: .6 });
        gsap.to(item, { opacity: focus ? .5 : 1, duration: .4 });
      }
    });
  }
}

/* COLOR GRADING on images */
function initImageColorGrading() {
  var wraps = document.querySelectorAll('.hero__right-img, .psi__img-wrap, .wi, .pb');
  wraps.forEach(function(wrap) {
    var overlay = document.createElement('div');
    overlay.style.cssText = 'position:absolute;inset:0;pointer-events:none;z-index:2;mix-blend-mode:color;background:transparent;transition:background 1.2s ease;';
    wrap.style.position = 'relative';
    wrap.appendChild(overlay);
    ScrollTrigger.create({
      trigger: wrap,
      start: 'top bottom',
      end: 'bottom top',
      onUpdate: function(self) {
        var p = self.progress;
        var intensity = Math.sin(p * Math.PI) * 0.15;
        var r = Math.round(61 * intensity);
        var g = Math.round(139 * intensity);
        var b = Math.round(122 * intensity);
        overlay.style.background = 'rgba(' + r + ',' + g + ',' + b + ',' + intensity + ')';
      }
    });
  });
}

/* V6 INIT */
initSmartTickerFinal();
initSectionSpotlight();
upgradeButtonTexts();
assignButtonActions();
initFeaturedCardShine();
initDepthOfField();
initImageColorGrading();

"""

js_escaped = esc(js_block)
tpl = tpl[:last_script_pos] + js_escaped + tpl[last_script_pos:]
print("Step 6: JS injected. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# QUOTE VERIFICATION
# ═══════════════════════════════════════════════════

ret_idx = tpl.index("return '")
end_idx = tpl.rindex("';")
s = tpl[ret_idx+8:end_idx]

i = 0
problems = []
bs = chr(92)
sq = chr(39)
while i < len(s):
    if s[i] == bs:
        i += 2
        continue
    if s[i] == sq:
        problems.append(f'pos {i}: ...{repr(s[max(0,i-30):i+30])}...')
    i += 1

if problems:
    print(f"\nQUOTE PROBLEMS: {len(problems)}")
    for p in problems[:10]:
        print(p)
    sys.exit(1)

# Also check for stray \\\n sequences (the V5 bug)
stray = list(re.finditer(r'\\\\\\\\n\\n', tpl))
if stray:
    print(f"\nWARNING: {len(stray)} potential stray backslash sequences")
    for s in stray[:3]:
        print(f"  @{s.start()}: {repr(tpl[s.start()-20:s.start()+20])}")

print(f"\nQuotes OK! Final size: {len(tpl)} chars")

content = content[:tpl5_start] + tpl + content[tpl9_start:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("V6 PATCH APPLIED!")
