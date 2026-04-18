#!/usr/bin/env python3
"""
PATCH V5 — NOVUS CAPITAL REAL ESTATE
Adds: 6 scroll mechanics, 6 visual effects, 7 Agent Pro V2 features
"""

filepath = r"C:\vantage-clean\crm-v2-push\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate TPL5
tpl5_start = content.index("TPL_ECOM_HTML['5']")
tpl9_start = content.index("TPL_ECOM_HTML['9']")
tpl = content[tpl5_start:tpl9_start]

def esc(s):
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')

print("Template size before:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 1: Inject CSS before </style>
# ═══════════════════════════════════════════════════

css_block = r"""
/* ════════ SCROLL-02 — HORIZONTAL ════════ */
.scroll-right-wrap { height: 100vh; }
.scroll-right-pin {
  position: sticky; top: 0;
  height: 100vh; overflow: hidden;
  background: var(--void);
  display: flex; flex-direction: column;
  justify-content: center;
}
.scroll-right-track {
  display: flex;
  align-items: center;
  gap: 12rem;
  padding: 0 8rem;
  will-change: transform;
  white-space: nowrap;
}
.sr-item {
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
.sr-item__num {
  font-family: var(--font-d);
  font-size: clamp(8rem, 15vw, 20rem);
  font-weight: 300;
  line-height: .85;
  color: var(--ivory);
  letter-spacing: -.03em;
}
.sr-item__label {
  font-family: var(--font-m);
  font-size: 1.1rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--muted);
  max-width: 300px;
  white-space: normal;
}
.sr-item--word {
  font-family: var(--font-d);
  font-size: clamp(10rem, 20vw, 28rem);
  font-weight: 300;
  line-height: 1;
  letter-spacing: -.02em;
  flex-direction: row;
  align-items: center;
}
.sr-word-accent { color: var(--sage); font-style: italic; }
.sr-item--img {
  flex-direction: row;
  align-items: center;
  gap: 4rem;
  white-space: normal;
}
.sr-item__img-wrap {
  width: 360px; height: 260px; overflow: hidden; flex-shrink: 0;
}
.sr-item__img-wrap img { width:100%; height:100%; object-fit:cover; }
.sr-item__caption {
  font-family: var(--font-d);
  font-size: 2.8rem;
  font-weight: 300;
  font-style: italic;
  max-width: 320px;
  white-space: normal;
  line-height: 1.3;
}
.sr-item--quote {
  white-space: normal;
  max-width: 500px;
}
.sr-item--quote blockquote {
  font-family: var(--font-d);
  font-size: clamp(3.2rem, 4vw, 5.6rem);
  font-weight: 300;
  font-style: italic;
  line-height: 1.15;
  margin-bottom: 2rem;
}
.sr-item--quote blockquote em { color: var(--sage); }
.sr-item--quote cite {
  font-family: var(--font-m);
  font-size: .9rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--muted);
}
.sr-progress {
  position: absolute;
  bottom: 4rem; left: 8rem; right: 8rem;
  height: 1px;
  background: rgba(245,242,237,.08);
}
.sr-progress-fill {
  height: 100%;
  width: 0%;
  background: var(--sage);
  transition: width .1s linear;
  box-shadow: 0 0 8px var(--sage-glow);
}
.sr-hint {
  position: absolute;
  bottom: 3.2rem;
  right: 8rem;
  font-family: var(--font-m);
  font-size: .85rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--muted);
  animation: hint-pulse 2s ease-in-out infinite;
}
@keyframes hint-pulse { 0%,100%{opacity:.3} 50%{opacity:1} }

/* ════════ SCROLL-03 — ROUE CIRCULAIRE ════════ */
.scroll-wheel-wrap  { height: 400vh; }
.scroll-wheel-pin {
  position: sticky; top: 0;
  height: 100vh; overflow: hidden;
  background: var(--mid);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8rem;
}
.scroll-wheel-label { max-width: 320px; flex-shrink: 0; }
.swl-title {
  font-family: var(--font-d);
  font-size: clamp(4rem, 5.5vw, 7.2rem);
  font-weight: 300;
  line-height: 1;
  letter-spacing: -.02em;
}
.swl-title em { font-style: italic; color: var(--sage); }
.scroll-wheel-container {
  width: 500px; height: 500px;
  position: relative; flex-shrink: 0;
}
.wheel-rotor {
  width: 100%; height: 100%;
  position: relative;
  transform-origin: center;
}
.wheel-card {
  position: absolute;
  width: 160px; height: 220px;
  overflow: hidden;
  border: 1px solid var(--border);
  transform-origin: center;
  transition: box-shadow .3s;
  cursor: none;
}
.wheel-card img { width:100%; height:70%; object-fit:cover; }
.wheel-card__info { padding: 1rem; background: var(--surface); }
.wheel-card__name {
  font-family: var(--font-d); font-size: 1.3rem;
  font-style: italic; margin-bottom: .2rem;
}
.wheel-card__price {
  font-family: var(--font-m); font-size: .75rem;
  letter-spacing: .1em; color: var(--champ);
}
.wheel-card.active { box-shadow: 0 0 40px rgba(61,139,122,.3); border-color: var(--sage); }
.wheel-active-info { max-width: 280px; flex-shrink: 0; }
.wai-name {
  font-family: var(--font-d); font-size: 3.6rem;
  font-weight: 300; font-style: italic; line-height: 1; margin-bottom: 1rem;
}
.wai-city {
  font-family: var(--font-m); font-size: .9rem; letter-spacing: .18em;
  text-transform: uppercase; color: var(--muted); margin-bottom: 1.2rem;
}
.wai-price {
  font-family: var(--font-d); font-size: 2.8rem; font-weight: 300; color: var(--champ);
}

/* ════════ SCROLL-04 — ZOOM OUT ════════ */
.scroll-zoom-wrap { height: 300vh; }
.scroll-zoom-pin {
  position: sticky; top: 0;
  height: 100vh; overflow: hidden;
}
.scroll-zoom-img {
  position: absolute; inset: -10%;
  display: flex; align-items: center; justify-content: center;
}
#szi-img {
  width: 100%; height: 100%; object-fit: cover;
  transform: scale(3);
  transform-origin: center;
  filter: brightness(.5);
}
.scroll-zoom-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(to bottom, rgba(8,15,20,.2), rgba(8,15,20,.7));
}
.scroll-zoom-text {
  position: absolute; bottom: 8rem; left: 5.6rem;
  z-index: 2; opacity: 0;
}
.scroll-zoom-text p {
  font-family: var(--font-d);
  font-size: clamp(3.2rem, 4.5vw, 6rem);
  font-weight: 300; font-style: italic; line-height: 1.2;
  margin-bottom: 1.6rem;
}
.scroll-zoom-text em { color: var(--sage); }
.szt-sub {
  font-family: var(--font-m);
  font-size: 1.1rem !important;
  letter-spacing: .25em;
  text-transform: uppercase;
  color: var(--muted);
  font-style: normal !important;
}

/* ════════ SCROLL-05 — TEXT PHYSICS ════════ */
.physics-word {
  display: inline-block;
  margin-right: .3em;
  will-change: transform;
}
.physics-word em { font-style: italic; color: var(--sage); }

/* ════════ SCROLL-06 — OBLIQUE ════════ */
.scroll-oblique-wrap { height: 250vh; }
.scroll-oblique-pin {
  position: sticky; top: 0;
  height: 100vh; overflow: hidden;
  background: var(--surface);
  display: flex; align-items: center;
}
.scroll-oblique-track {
  display: flex; flex-direction: column; gap: 6rem;
  padding: 6rem 8rem;
  will-change: transform;
}
.sob-item {
  display: flex; align-items: flex-start; gap: 4rem;
  opacity: 0; transform: translate(-60px, 60px);
}
.sob-item.visible { opacity: 1; transform: translate(0,0); }
.sob-num {
  font-family: var(--font-m); font-size: 1rem; letter-spacing: .2em;
  color: var(--sage); margin-top: .4rem; flex-shrink: 0;
}
.sob-text {
  font-family: var(--font-d); font-size: clamp(2.8rem, 3.5vw, 4.8rem);
  font-weight: 300; line-height: 1.2;
}
.sob-text strong { color: var(--champ); font-weight: 300; }

/* ════════ AGENT-V2-02 — Timeline ════════ */
.client-timeline { margin-top: 3.2rem; }
.ct-title {
  font-family: var(--font-m); font-size: .85rem; letter-spacing: .18em;
  text-transform: uppercase; color: var(--muted); margin-bottom: 2.4rem;
}
.ct-track {
  position: relative;
  display: flex;
  align-items: center;
  padding: 2rem 0;
  overflow-x: auto;
  gap: 0;
}
.ct-track::before {
  content: "";
  position: absolute;
  top: 50%; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(to right, var(--sage), var(--plat), rgba(245,242,237,.1));
  z-index: 0;
}
.ct-point {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .8rem;
  min-width: 120px;
  flex-shrink: 0;
}
.ct-dot {
  width: 14px; height: 14px;
  border-radius: 50%;
  background: var(--surface);
  border: 2px solid var(--sage);
  transition: transform .3s, box-shadow .3s;
}
.ct-dot.future { border-style: dashed; border-color: var(--border); }
.ct-dot.done {
  background: var(--sage);
  box-shadow: 0 0 12px var(--sage-glow);
}
.ct-point:hover .ct-dot {
  transform: scale(1.4);
  box-shadow: 0 0 16px var(--sage-glow);
}
.ct-label {
  font-family: var(--font-m); font-size: .65rem; letter-spacing: .1em;
  text-transform: uppercase; text-align: center;
  color: var(--muted); line-height: 1.4;
}
.ct-date {
  font-family: var(--font-m); font-size: .6rem;
  color: rgba(245,242,237,.2); text-align: center;
}

/* ════════ AGENT-V2-03 — Smart Match ════════ */
.smart-match { margin-top: 3.2rem; }
.sm-title {
  display: flex; align-items: center; gap: 1.6rem; margin-bottom: 2.4rem;
  font-family: var(--font-m); font-size: .85rem; letter-spacing: .18em;
  text-transform: uppercase; color: var(--muted);
}
.sm-ai-badge {
  display: flex; align-items: center; gap: .6rem;
  font-size: .7rem; color: var(--sage);
  background: var(--sage-dim);
  border: 1px solid rgba(61,139,122,.2);
  padding: .3rem .8rem;
}
.sm-ai-dot {
  width: 5px; height: 5px; border-radius: 50%;
  background: var(--sage);
  animation: agent-dot-pulse 1s ease-in-out infinite;
}
.sm-result-item {
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
  padding: 1.6rem;
  background: var(--mid);
  border: 1px solid var(--border);
  margin-bottom: .8rem;
  gap: 2rem;
  transition: border-color .3s;
}
.sm-result-item:hover { border-color: rgba(61,139,122,.3); }
.sm-result-name {
  font-family: var(--font-d); font-size: 1.6rem; font-style: italic; margin-bottom: .4rem;
}
.sm-result-reason {
  font-family: var(--font-m); font-size: .72rem; letter-spacing: .08em; color: var(--muted);
}
.sm-result-score-wrap {
  display: flex; flex-direction: column; align-items: flex-end; gap: .6rem; min-width: 100px;
}
.sm-result-pct {
  font-family: var(--font-d); font-size: 2.4rem; font-weight: 300;
  color: var(--sage); line-height: 1;
}
.sm-result-bar-track {
  width: 80px; height: 3px; background: rgba(245,242,237,.1); position: relative;
}
.sm-result-bar-fill {
  position: absolute; top:0; left:0; height:100%; width:0%;
  background: linear-gradient(to right, var(--sage), var(--sage-light));
  transition: width 1.2s var(--ease-out);
  box-shadow: 0 0 6px var(--sage-glow);
}

/* ════════ AGENT-V2-04 — Voice Note ════════ */
.voice-note { margin-top: 1.6rem; }
.vn-btn {
  display: flex; align-items: center; gap: 1rem;
  background: rgba(61,139,122,.08);
  border: 1px solid rgba(61,139,122,.2);
  color: var(--sage);
  font-family: var(--font-m); font-size: .9rem; letter-spacing: .14em;
  text-transform: uppercase; padding: 1rem 2rem; cursor: none;
  transition: all .3s;
}
.vn-btn.recording {
  background: rgba(196,113,79,.1);
  border-color: rgba(196,113,79,.4);
  color: var(--terra);
  animation: vn-pulse .8s ease-in-out infinite;
}
@keyframes vn-pulse { 0%,100%{box-shadow:0 0 0 rgba(196,113,79,0)} 50%{box-shadow:0 0 16px rgba(196,113,79,.3)} }
.vn-transcript {
  margin-top: 1.2rem;
  padding: 1.6rem;
  background: var(--mid);
  border: 1px solid var(--border);
}
.vn-text {
  font-family: var(--font-b); font-size: 1.3rem; font-weight: 300;
  color: var(--cream); line-height: 1.7; margin-top: 1rem;
  min-height: 40px;
}

/* ════════ AGENT-V2-07 — Pipeline Timeline ════════ */
.pipeline-view-toggle { display:flex; gap:0; margin-left:auto; }
.pvt-btn {
  font-family:var(--font-m); font-size:.8rem; letter-spacing:.12em; text-transform:uppercase;
  padding:.6rem 1.4rem; background:none; border:1px solid var(--border);
  color:var(--muted); cursor:none; margin-right:-1px; transition:all .3s;
}
.pvt-btn.active { background:var(--sage-dim); border-color:var(--sage); color:var(--sage); }
.pipeline-timeline { overflow-x:auto; padding:2rem 0; }
.plt-axis {
  display:flex; height:2.4rem; position:relative; min-width:1000px; margin-bottom:1.2rem;
  border-bottom:1px solid var(--border);
}
.plt-month {
  flex:1; font-family:var(--font-m); font-size:.7rem; letter-spacing:.12em;
  text-transform:uppercase; color:var(--muted); text-align:center; padding:.6rem 0;
}
.plt-rows { position:relative; min-height:200px; min-width:1000px; }
.plt-deal {
  position:absolute; height:32px;
  display:flex; align-items:center; padding:0 1rem;
  font-family:var(--font-m); font-size:.7rem; letter-spacing:.08em;
  text-transform:uppercase; overflow:hidden; white-space:nowrap;
  transition:opacity .3s, box-shadow .3s; cursor:none;
}
.plt-deal:hover { opacity:.85; box-shadow:var(--shadow-sage); }
.plt-deal.stage-prospect  { background:rgba(122,157,176,.3); }
.plt-deal.stage-visite    { background:rgba(61,139,122,.3); }
.plt-deal.stage-offre     { background:rgba(212,184,150,.3); }
.plt-deal.stage-signe     { background:rgba(196,113,79,.3); }
.plt-deal.stage-loue      { background:rgba(77,184,150,.3); }

/* ════════ CLIENT DETAIL STYLES ════════ */
.cd-hero {
  display: flex; align-items: center; gap: 3.2rem; margin-bottom: 4rem;
  padding-bottom: 3.2rem; border-bottom: 1px solid var(--border);
}
.cd-avatar {
  width: 80px; height: 80px;
  background: var(--sage-dim);
  border: 1px solid rgba(61,139,122,.25);
  display: flex; align-items: center; justify-content: center;
  font-family: var(--font-d); font-size: 2.8rem; font-weight: 300; color: var(--sage);
  flex-shrink: 0;
}
.cd-name {
  font-family: var(--font-d); font-size: 3.6rem; font-weight: 300;
  font-style: italic; margin-bottom: .6rem; line-height: 1;
}
.cd-meta { font-family: var(--font-m); font-size: .85rem; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); margin-bottom: .4rem; }
.cd-city { font-family: var(--font-m); font-size: .85rem; letter-spacing: .12em; text-transform: uppercase; color: var(--sage); }
.cd-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 1.6rem; margin-bottom: 3.2rem; }
.cd-section { padding: 1.6rem; background: var(--mid); border: 1px solid var(--border); }
.cd-section-title { font-family: var(--font-m); font-size: .7rem; letter-spacing: .18em; text-transform: uppercase; color: var(--muted); margin-bottom: .6rem; }
.cd-section-value { font-family: var(--font-d); font-size: 1.8rem; font-weight: 300; font-style: italic; }
.cd-viewing-item { display: flex; gap: 2.4rem; padding: 1rem 0; border-bottom: 1px solid var(--border); font-family: var(--font-m); font-size: .8rem; letter-spacing: .08em; color: var(--sand); }

/* ════════ V5 RESPONSIVE ════════ */
@media (max-width: 1024px) {
  .scroll-right-wrap { height: 80vh; }
  .scroll-wheel-wrap  { height: 250vh; }
}
@media (max-width: 768px) {
  .scroll-oblique-wrap { display: none; }
  .scroll-wheel-wrap   { display: none; }
  .cd-grid { grid-template-columns: 1fr 1fr; }
}
"""

css_escaped = esc(css_block)
style_marker = '</style>'
style_pos = tpl.index(style_marker)
tpl = tpl[:style_pos] + css_escaped + tpl[style_pos:]
print("Step 1: CSS injected. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 2: Inject SCROLL-02 HTML between #metrics and #about
# ═══════════════════════════════════════════════════

# Find the closing of metrics section - look for the about section start
about_marker = 'id="about"'
about_pos = tpl.index(about_marker)
# Go back to find the section/div opening for about
# We'll insert just before the about section
# Find the < that starts the about element
search_back = tpl[:about_pos].rindex('<')

scroll02_html = r"""
<div class="scroll-right-wrap" id="srw">
  <div class="scroll-right-pin" id="srp">
    <div class="scroll-right-track" id="srt">
      <div class="sr-item">
        <div class="sr-item__num">&#8364;4.2B</div>
        <div class="sr-item__label">Assets Under Management</div>
      </div>
      <div class="sr-item sr-item--word">
        <span>PORT</span><span class="sr-word-accent">FOLIO</span>
      </div>
      <div class="sr-item sr-item--img">
        <div class="sr-item__img-wrap">
          <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800&q=88&auto=format&fit=crop" alt="">
        </div>
        <div class="sr-item__caption">12,400 Properties across Europe</div>
      </div>
      <div class="sr-item sr-item--quote">
        <blockquote>Architecture is<br>frozen <em>music.</em></blockquote>
        <cite>&#8212; Schopenhauer</cite>
      </div>
      <div class="sr-item">
        <div class="sr-item__num">27</div>
        <div class="sr-item__label">Years of Excellence</div>
      </div>
    </div>
    <div class="sr-progress">
      <div class="sr-progress-fill" id="sr-progress-fill"></div>
    </div>
    <div class="sr-hint">&#8594; Keep scrolling</div>
  </div>
</div>
"""

scroll02_escaped = esc(scroll02_html)
tpl = tpl[:search_back] + scroll02_escaped + tpl[search_back:]
print("Step 2: SCROLL-02 HTML injected. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 3: Inject SCROLL-03 (wheel) after #about section
# Find the properties section and insert before it
# ═══════════════════════════════════════════════════

props_marker = 'id="properties"'
props_pos = tpl.index(props_marker)
props_tag_start = tpl[:props_pos].rindex('<')

scroll03_html = r"""
<div class="scroll-wheel-wrap" id="sww">
  <div class="scroll-wheel-pin" id="swp">
    <div class="scroll-wheel-label">
      <div class="s-tag"><span>Featured Selections</span></div>
      <h2 class="swl-title">Scroll to<br><em>Explore</em></h2>
    </div>
    <div class="scroll-wheel-container" id="swc">
      <div class="wheel-rotor" id="wheel-rotor"></div>
    </div>
    <div class="wheel-active-info" id="wheel-active-info">
      <div class="wai-name" id="wai-name">&#8212;</div>
      <div class="wai-city" id="wai-city">&#8212;</div>
      <div class="wai-price" id="wai-price">&#8212;</div>
    </div>
  </div>
</div>
"""

scroll03_escaped = esc(scroll03_html)
tpl = tpl[:props_tag_start] + scroll03_escaped + tpl[props_tag_start:]
print("Step 3: SCROLL-03 HTML injected. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 4: Inject SCROLL-04 (zoom) + SCROLL-06 (oblique) after properties, before performance
# ═══════════════════════════════════════════════════

perf_marker = 'id="performance"'
perf_pos = tpl.index(perf_marker)
perf_tag_start = tpl[:perf_pos].rindex('<')

scroll04_06_html = r"""
<div class="scroll-oblique-wrap" id="sob-wrap">
  <div class="scroll-oblique-pin" id="sob-pin">
    <div class="scroll-oblique-track" id="sob-track">
      <div class="sob-item">
        <span class="sob-num">01</span>
        <span class="sob-text">We select fewer than<br><strong>2%</strong> of properties reviewed</span>
      </div>
      <div class="sob-item">
        <span class="sob-num">02</span>
        <span class="sob-text">Every lease includes<br><strong>full asset management</strong></span>
      </div>
      <div class="sob-item">
        <span class="sob-num">03</span>
        <span class="sob-text">Average tenancy<br>duration: <strong>3.2 years</strong></span>
      </div>
    </div>
  </div>
</div>
<div class="scroll-zoom-wrap" id="szw">
  <div class="scroll-zoom-pin" id="szp">
    <div class="scroll-zoom-img" id="szi">
      <img src="https://images.unsplash.com/photo-1486325212027-8081e485255e?w=2400&q=90&auto=format&fit=crop" id="szi-img" alt="">
    </div>
    <div class="scroll-zoom-overlay"></div>
    <div class="scroll-zoom-text" id="szt">
      <p>Every great city has a building<br>that defines its <em>skyline.</em></p>
      <p class="szt-sub">We manage 14 of them.</p>
    </div>
  </div>
</div>
"""

scroll04_06_escaped = esc(scroll04_06_html)
tpl = tpl[:perf_tag_start] + scroll04_06_escaped + tpl[perf_tag_start:]
print("Step 4: SCROLL-04+06 HTML injected. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 5: Inject SVG morph overlay before </body>
# ═══════════════════════════════════════════════════

body_marker = '</body>'
body_pos = tpl.rindex(body_marker)

morph_html = r"""
<div class="svg-morph-overlay" id="svg-morph" aria-hidden="true">
  <svg viewBox="0 0 100 100" preserveAspectRatio="none"
       style="position:fixed;inset:0;width:100%;height:100%;z-index:6000;pointer-events:none">
    <path id="morph-path" d="M50,50 m-0,0 a0,0 0 1,0 0.01,0 z" fill="var(--void)"/>
  </svg>
</div>
<canvas class="liquid-cursor" id="liquid-cursor"
        style="position:fixed;top:0;left:0;z-index:9999;pointer-events:none;"></canvas>
"""

morph_escaped = esc(morph_html)
tpl = tpl[:body_pos] + morph_escaped + tpl[body_pos:]
print("Step 5: Morph + cursor canvas injected. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 6: Inject ALL JavaScript before last x3c/script>
# ═══════════════════════════════════════════════════

import re
scripts = list(re.finditer(r'x3c/script>', tpl))
last_script_pos = scripts[-1].start()

js_block = r"""

/* ════════════════════════════════════════════════════
   V5 — SCROLL INATTENDUS + EFFETS VISUELS + AGENT PRO V2
════════════════════════════════════════════════════ */

/* SCROLL-02 — Horizontal trigger */
function initHorizontalScroll() {
  var track = document.getElementById('srt');
  var fillBar = document.getElementById('sr-progress-fill');
  if (!track) return;
  var totalW = track.scrollWidth - window.innerWidth;
  gsap.to(track, {
    x: -totalW,
    ease: 'none',
    scrollTrigger: {
      trigger: '#srw',
      start: 'top top',
      end: function() { return '+=' + (totalW + window.innerHeight); },
      pin: '#srp',
      scrub: 1.2,
      anticipatePin: 1,
      onUpdate: function(self) {
        if (fillBar) fillBar.style.width = (self.progress * 100) + '%';
      }
    }
  });
}

/* SCROLL-03 — Roue circulaire */
function initScrollWheel() {
  var rotor = document.getElementById('wheel-rotor');
  var infoN = document.getElementById('wai-name');
  var infoC = document.getElementById('wai-city');
  var infoP = document.getElementById('wai-price');
  if (!rotor) return;
  var props = [
    { name:'Tour Lumi\u00e8re', city:'Paris 16e', price:'\u20ac 18,500/mo', img:'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=400&q=80' },
    { name:'The Meridian', city:'London', price:'\u20ac 22,000/mo', img:'https://images.unsplash.com/photo-1486325212027-8081e485255e?w=400&q=80' },
    { name:'Villa Aurelia', city:'Athens', price:'\u20ac 12,500/mo', img:'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=400&q=80' },
    { name:'Le Patio', city:'Monaco', price:'\u20ac 35,000/mo', img:'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=400&q=80' },
    { name:'Loft Lumino', city:'Z\u00fcrich', price:'\u20ac 9,800/mo', img:'https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=400&q=80' },
    { name:'Casa Bianca', city:'Santorini', price:'\u20ac 14,200/mo', img:'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=400&q=80' },
  ];
  var N = props.length;
  var R = 200;
  props.forEach(function(prop, i) {
    var card = document.createElement('div');
    card.className = 'wheel-card';
    card.innerHTML = '<img src="' + prop.img + '" alt="' + prop.name + '"><div class="wheel-card__info"><div class="wheel-card__name">' + prop.name + '</div><div class="wheel-card__price">' + prop.price + '</div></div>';
    card.dataset.index = i;
    rotor.appendChild(card);
  });
  var activeIndex = 0;
  function updateWheel(angle) {
    var cards = rotor.querySelectorAll('.wheel-card');
    cards.forEach(function(card, i) {
      var cardAngle = (i / N) * 360 + angle;
      var rad = cardAngle * Math.PI / 180;
      var x = Math.cos(rad) * R + 250 - 80;
      var y = Math.sin(rad) * R + 250 - 110;
      var sc = .7 + (Math.cos(rad) + 1) / 2 * .5;
      var opac = .3 + (Math.cos(rad) + 1) / 2 * .7;
      gsap.set(card, { x:x, y:y, scale:sc, opacity:opac, zIndex:Math.round(opac*10) });
      var isActive = Math.abs(Math.cos(rad) - 1) < .2;
      card.classList.toggle('active', isActive);
      if (isActive && i !== activeIndex) {
        activeIndex = i;
        var p = props[i];
        gsap.to([infoN,infoC,infoP], { opacity:0, y:-10, duration:.2,
          onComplete: function() {
            infoN.textContent = p.name;
            infoC.textContent = p.city;
            infoP.textContent = p.price;
            gsap.to([infoN,infoC,infoP], { opacity:1, y:0, duration:.4, ease:'power3.out' });
          }
        });
      }
    });
  }
  updateWheel(0);
  gsap.to({ angle: 0 }, {
    angle: -360,
    ease: 'none',
    scrollTrigger: {
      trigger: '#sww',
      start: 'top top',
      end: 'bottom bottom',
      pin: '#swp',
      scrub: 2,
      onUpdate: function(self) { updateWheel(self.progress * -360); }
    }
  });
}

/* SCROLL-04 — Zoom out */
function initScrollZoom() {
  var img = document.getElementById('szi-img');
  var text = document.getElementById('szt');
  if (!img) return;
  ScrollTrigger.create({
    trigger: '#szw',
    start: 'top top',
    end: 'bottom bottom',
    pin: '#szp',
    scrub: 1.5,
    onUpdate: function(self) {
      var scale = 3 - self.progress * 2.2;
      var bright = .5 + self.progress * .3;
      gsap.set(img, { scale: Math.max(.85, scale), filter: 'brightness(' + bright + ')' });
      if (self.progress > .75 && text) {
        gsap.to(text, { opacity:1, y:0, duration:.6, ease:'power3.out' });
      } else if (self.progress < .7 && text) {
        gsap.to(text, { opacity:0, duration:.3 });
      }
    }
  });
}

/* SCROLL-05 — Text physics */
function initTextPhysics() {
  var titleEl = document.getElementById('cta-h');
  if (!titleEl) return;
  var origHTML = titleEl.innerHTML;
  titleEl.innerHTML = '';
  titleEl.removeAttribute('style');
  var sentences = ['Your Next', 'Property', 'Awaits.'];
  var words = [];
  sentences.forEach(function(sentence) {
    var line = document.createElement('div');
    line.style.display = 'block';
    line.style.overflow = 'visible';
    sentence.split(' ').forEach(function(word) {
      var span = document.createElement('span');
      span.className = 'physics-word';
      span.innerHTML = (word === 'Awaits.') ? '<em>' + word + '</em>' : word;
      gsap.set(span, { y: -window.innerHeight - 100 - Math.random() * 200, opacity: 0 });
      line.appendChild(span);
      words.push(span);
    });
    titleEl.appendChild(line);
  });
  ScrollTrigger.create({
    trigger: '#contact',
    start: 'top 70%',
    onEnter: function() {
      words.forEach(function(word, i) {
        gsap.to(word, {
          y: 0, opacity: 1,
          duration: 1.4 + Math.random() * .4,
          delay: i * .12,
          ease: 'bounce.out'
        });
      });
    }
  });
}

/* SCROLL-06 — Oblique */
function initObliqueScroll() {
  var track = document.getElementById('sob-track');
  if (!track) return;
  gsap.to(track, {
    x: 200, y: -180,
    ease: 'none',
    scrollTrigger: {
      trigger: '#sob-wrap',
      start: 'top top',
      end: 'bottom bottom',
      pin: '#sob-pin',
      scrub: 1.8,
      onUpdate: function(self) {
        document.querySelectorAll('.sob-item').forEach(function(item, i) {
          if (self.progress > i * .25) {
            item.classList.add('visible');
            gsap.to(item, { opacity:1, x:0, y:0, duration:.8, ease:'power3.out' });
          }
        });
      }
    }
  });
}

/* EFF-V1 — Liquid Cursor */
function initLiquidCursor() {
  var canvas = document.getElementById('liquid-cursor');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  window.addEventListener('resize', function() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  });
  var mx=0, my=0, cx=0, cy=0, vx=0, vy=0, pmx=0, pmy=0, pressed=false;
  window.addEventListener('mousemove', function(e) {
    vx = e.clientX - pmx; vy = e.clientY - pmy;
    pmx = mx; pmy = my; mx = e.clientX; my = e.clientY;
  });
  window.addEventListener('mousedown', function() { pressed=true; });
  window.addEventListener('mouseup', function() { pressed=false; });
  var cursorColor = { r:61, g:139, b:122 };
  function draw() {
    ctx.clearRect(0,0,canvas.width,canvas.height);
    cx += (mx-cx)*.12; cy += (my-cy)*.12;
    var speed = Math.sqrt(vx*vx+vy*vy);
    var stretch = Math.min(speed*.15, 0.8);
    var angle = Math.atan2(vy,vx);
    var radius = pressed ? 8 : 14;
    ctx.save(); ctx.translate(cx,cy); ctx.rotate(angle);
    ctx.scale(1+stretch, 1-stretch*.4);
    var grd = ctx.createRadialGradient(0,0,0,0,0,radius*2.5);
    grd.addColorStop(0, 'rgba('+cursorColor.r+','+cursorColor.g+','+cursorColor.b+',0.15)');
    grd.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = grd; ctx.beginPath(); ctx.arc(0,0,radius*2.5,0,Math.PI*2); ctx.fill();
    ctx.fillStyle = 'rgba('+cursorColor.r+','+cursorColor.g+','+cursorColor.b+',0.85)';
    ctx.beginPath(); ctx.arc(0,0,radius,0,Math.PI*2); ctx.fill();
    ctx.fillStyle = 'rgba(245,242,237,0.9)';
    ctx.beginPath(); ctx.arc(0,0,2,0,Math.PI*2); ctx.fill();
    ctx.restore();
    if (speed > 8) {
      var trailX = cx-vx*1.5, trailY = cy-vy*1.5;
      var tGrd = ctx.createRadialGradient(trailX,trailY,0,trailX,trailY,radius*.8);
      tGrd.addColorStop(0, 'rgba('+cursorColor.r+','+cursorColor.g+','+cursorColor.b+',0.3)');
      tGrd.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.fillStyle = tGrd; ctx.beginPath(); ctx.arc(trailX,trailY,radius*.8,0,Math.PI*2); ctx.fill();
    }
    requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
  var colorMap = [
    { sel:'.about', r:61, g:139, b:122 },
    { sel:'#performance', r:122, g:157, b:176 },
    { sel:'#contact', r:61, g:139, b:122 }
  ];
  colorMap.forEach(function(cm) {
    var sec = document.querySelector(cm.sel);
    if (!sec) return;
    ScrollTrigger.create({
      trigger: sec, start:'top 50%', end:'bottom 50%',
      onEnter: function() { gsap.to(cursorColor, { r:cm.r, g:cm.g, b:cm.b, duration:.8 }); },
      onEnterBack: function() { gsap.to(cursorColor, { r:cm.r, g:cm.g, b:cm.b, duration:.8 }); }
    });
  });
}

/* EFF-V2 — Lens distortion */
function initLensDistortion() {
  var svgFilter = document.createElementNS('http://www.w3.org/2000/svg','svg');
  svgFilter.style.cssText = 'position:absolute;width:0;height:0;overflow:hidden';
  svgFilter.innerHTML = '<defs><filter id="lens-filter" x="-20%" y="-20%" width="140%" height="140%"><feTurbulence id="lens-turb" type="fractalNoise" baseFrequency="0 0" numOctaves="1" result="noise"/><feDisplacementMap id="lens-disp" in="SourceGraphic" in2="noise" scale="0" xChannelSelector="R" yChannelSelector="G"/></filter></defs>';
  document.body.appendChild(svgFilter);
  var lensImages = document.querySelectorAll('.scroll-zoom-img img');
  lensImages.forEach(function(img) { img.style.filter = 'url(#lens-filter)'; });
  var lensScale = 0;
  var lensDisp = document.getElementById('lens-disp');
  gsap.ticker.add(function() {
    lensScale *= .92;
    if (lensDisp) lensDisp.setAttribute('scale', Math.max(0,lensScale).toFixed(1));
  });
}

/* EFF-V3 — Grid reveal liquide */
function initLiquidGridReveal() {
  var grid = document.querySelector('.works__grid, .flip-grid');
  if (!grid) return;
  var items = Array.from(grid.querySelectorAll('.wi, .flip-card'));
  items.forEach(function(item) { item.style.opacity='0'; item.style.transform='scale(0.88)'; });
  var revealStarted = false;
  var lastMouseX = window.innerWidth/2, lastMouseY = window.innerHeight/2;
  window.addEventListener('mousemove', function(e) { lastMouseX=e.clientX; lastMouseY=e.clientY; });
  ScrollTrigger.create({
    trigger: grid, start:'top 75%',
    onEnter: function() {
      if (revealStarted) return;
      revealStarted = true;
      var distances = items.map(function(item) {
        var r = item.getBoundingClientRect();
        var icx = r.left+r.width/2, icy = r.top+r.height/2;
        return Math.sqrt(Math.pow(icx-lastMouseX,2)+Math.pow(icy-lastMouseY,2));
      });
      var maxDist = Math.max.apply(null, distances);
      items.forEach(function(item, i) {
        gsap.to(item, { opacity:1, scale:1, duration:.7, delay:(distances[i]/maxDist)*.8, ease:'power3.out' });
      });
    }
  });
}

/* EFF-V4 — SVG Morphing */
var morphShapes = {
  hidden: 'M50,50 m-0,0 a0,0 0 1,0 0.01,0 z',
  circle: 'M50,0 C77.6,0 100,22.4 100,50 C100,77.6 77.6,100 50,100 C22.4,100 0,77.6 0,50 C0,22.4 22.4,0 50,0 z',
  diamond: 'M50,0 L100,50 L50,100 L0,50 Z',
  square: 'M0,0 L100,0 L100,100 L0,100 Z'
};
function morphTransition(fromShape, toShape, color, duration) {
  duration = duration || .5;
  return new Promise(function(resolve) {
    var path = document.getElementById('morph-path');
    if (!path) { resolve(); return; }
    path.setAttribute('fill', color);
    gsap.fromTo(path,
      { attr: { d: morphShapes[fromShape] || morphShapes.hidden } },
      { attr: { d: morphShapes[toShape] || morphShapes.hidden },
        duration: duration, ease:'power4.inOut', onComplete: resolve });
  });
}
document.querySelectorAll('a[href^="#"]').forEach(function(link) {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    var target = document.querySelector(link.getAttribute('href'));
    if (!target) return;
    morphTransition('hidden','circle','var(--deep)',.4).then(function() {
      return morphTransition('circle','square','var(--deep)',.25);
    }).then(function() {
      if (typeof lenis !== 'undefined') lenis.scrollTo(target, { duration:0 });
      else target.scrollIntoView();
      return morphTransition('square','circle','var(--deep)',.25);
    }).then(function() {
      return morphTransition('circle','hidden','var(--deep)',.4);
    });
  });
});

/* EFF-V5 — Micro sons */
function initMicroSounds() {
  var AudioCtx = window.AudioContext || window.webkitAudioContext;
  if (!AudioCtx) return;
  var ctx = null;
  function getCtx() { if(!ctx) ctx=new AudioCtx(); return ctx; }
  function playTone(freq, type, duration, volume) {
    volume = volume || .05;
    try {
      var ac = getCtx();
      var osc = ac.createOscillator();
      var gain = ac.createGain();
      osc.connect(gain); gain.connect(ac.destination);
      osc.type = type; osc.frequency.value = freq;
      gain.gain.setValueAtTime(volume, ac.currentTime);
      gain.gain.exponentialRampToValueAtTime(.001, ac.currentTime+duration);
      osc.start(); osc.stop(ac.currentTime+duration);
    } catch(e) {}
  }
  document.querySelectorAll('.btn-blob,.btn-circle,.nav__agent-btn').forEach(function(btn) {
    btn.addEventListener('mouseenter', function() { playTone(880,'sine',.08,.03); });
    btn.addEventListener('click', function() { playTone(1100,'sine',.12,.04); });
  });
  var agentBtn = document.getElementById('nav-agent-btn');
  if (agentBtn) agentBtn.addEventListener('click', function() {
    playTone(440,'sine',.15,.04);
    setTimeout(function(){playTone(660,'sine',.12,.03);},100);
    setTimeout(function(){playTone(880,'sine',.10,.02);},200);
  });
  document.querySelectorAll('.acrm-tab').forEach(function(tab) {
    tab.addEventListener('click', function() { playTone(660,'triangle',.08,.025); });
  });
  window.addEventListener('crm-activity', function() { playTone(523,'sine',.1,.02); });
}

/* EFF-V6 — Image fragment hover */
function initImageFragment() {
  document.querySelectorAll('.wi').forEach(function(item) {
    var img = item.querySelector('img');
    if (!img) return;
    var COLS=4, ROWS=4, fragContainer=null, isFragmented=false;
    item.addEventListener('mouseenter', function() {
      if (isFragmented) return;
      isFragmented = true;
      fragContainer = document.createElement('div');
      fragContainer.style.cssText = 'position:absolute;inset:0;z-index:3;display:grid;grid-template-columns:repeat('+COLS+',1fr);grid-template-rows:repeat('+ROWS+',1fr);pointer-events:none;overflow:hidden;';
      var W = item.clientWidth, H = item.clientHeight;
      for (var r=0;r<ROWS;r++) {
        for (var c=0;c<COLS;c++) {
          var tile = document.createElement('div');
          tile.style.cssText = 'overflow:hidden;position:relative;';
          var tileImg = document.createElement('img');
          tileImg.src = img.src;
          tileImg.style.cssText = 'position:absolute;width:'+W+'px;height:'+H+'px;left:'+(-c*(W/COLS))+'px;top:'+(-r*(H/ROWS))+'px;object-fit:cover;';
          tile.appendChild(tileImg);
          fragContainer.appendChild(tile);
          var dx = (Math.random()-.5)*20, dy = (Math.random()-.5)*20;
          gsap.to(tile, { x:dx, y:dy, duration:.4, ease:'power2.out', delay:(r+c)*.02 });
        }
      }
      item.style.position = 'relative';
      item.appendChild(fragContainer);
    });
    item.addEventListener('mouseleave', function() {
      if (!fragContainer) return;
      var tiles = fragContainer.querySelectorAll('div');
      var fc = fragContainer;
      gsap.to(Array.from(tiles), {
        x:0, y:0, duration:.4, ease:'power3.in', stagger:.01,
        onComplete: function() { fc.remove(); fragContainer=null; isFragmented=false; }
      });
    });
  });
}

/* AGENT-V2-01 — Fold 3D */
function openFolderWithAnimation(clientId, folderEl) {
  var rect = folderEl.getBoundingClientRect();
  var clone = folderEl.cloneNode(true);
  clone.style.cssText = 'position:fixed;left:'+rect.left+'px;top:'+rect.top+'px;width:'+rect.width+'px;height:'+rect.height+'px;z-index:9999;pointer-events:none;transform-style:preserve-3d;perspective:1000px;';
  document.body.appendChild(clone);
  var tl = gsap.timeline({
    onComplete: function() { clone.remove(); openClientDetail(clientId); }
  });
  tl.to(clone, { y:-20, boxShadow:'0 40px 80px rgba(8,15,20,.6)', duration:.3, ease:'power2.out' });
  tl.to(clone, { rotateX:-35, transformOrigin:'bottom center', duration:.4, ease:'power3.out' });
  tl.to(clone, { left:0, top:0, width:'100vw', height:'100vh', duration:.5, ease:'power4.inOut' });
  tl.to(clone, { opacity:0, duration:.2 });
}

/* AGENT-V2-02 — Client timeline */
function renderClientTimeline(client) {
  var track = document.getElementById('ct-track');
  if (!track) return;
  var milestones = [
    { label:'First Contact', date:new Date(client.lastContact-30*86400000).toLocaleDateString('en-GB',{day:'numeric',month:'short'}), done:true },
    { label:'Profile Created', date:new Date(client.lastContact-25*86400000).toLocaleDateString('en-GB',{day:'numeric',month:'short'}), done:true }
  ];
  if (client.viewings) client.viewings.forEach(function(v) {
    milestones.push({ label:'Viewing: '+v.prop, date:v.date, done:true });
  });
  milestones.push({ label:'Offer Sent', date:'\u2014', done:client.status==='negotiation'||client.status==='signed' });
  milestones.push({ label:'Signed', date:'\u2014', done:client.status==='signed', future:client.status!=='signed' });
  milestones.push({ label:'Move In', date:'\u2014', done:false, future:true });
  track.innerHTML = '';
  milestones.forEach(function(m, i) {
    var pt = document.createElement('div');
    pt.className = 'ct-point';
    pt.innerHTML = '<div class="ct-dot '+(m.done?'done':'')+' '+(m.future?'future':'')+'"></div><div class="ct-label">'+m.label+'</div><div class="ct-date">'+m.date+'</div>';
    track.appendChild(pt);
    gsap.from(pt, { opacity:0, y:12, duration:.4, delay:i*.06, ease:'power3.out' });
  });
}

/* AGENT-V2-03 — Smart Match */
function runSmartMatch(client) {
  var results = document.getElementById('sm-results');
  var badge = document.querySelector('.sm-ai-badge');
  if (!results) return;
  var props = [
    { name:'Tour Lumi\u00e8re', city:'Paris 16e', price:18500, reasons:['Budget match','Type pr\u00e9f\u00e9r\u00e9','Ville cible'] },
    { name:'The Meridian', city:'London', price:22000, reasons:['Budget OK','Type office','City match'] },
    { name:'Villa Aurelia', city:'Athens', price:12500, reasons:['Budget match','Jardin inclus','Top rated'] },
    { name:'Loft Lumino', city:'Z\u00fcrich', price:9800, reasons:['Budget OK','Moderne','Disponible'] }
  ];
  var budgetMatch = parseFloat((client.budget||'10000').replace(/[^0-9]/g,'')) || 10000;
  var scored = props.map(function(p) {
    var score = 0;
    var priceDiff = Math.abs(p.price-budgetMatch)/budgetMatch;
    score += Math.max(0, 50-priceDiff*100);
    if (p.city.toLowerCase().indexOf((client.city||'').toLowerCase()) >= 0) score += 20;
    return Object.assign({}, p, { score: Math.min(99, Math.round(score)) });
  }).sort(function(a,b) { return b.score-a.score; });
  results.innerHTML = '';
  scored.forEach(function(prop, i) {
    setTimeout(function() {
      var item = document.createElement('div');
      item.className = 'sm-result-item';
      item.innerHTML = '<div><div class="sm-result-name">'+prop.name+'</div><div class="sm-result-reason">'+prop.reasons.join(' \u00b7 ')+'</div></div><div class="sm-result-score-wrap"><div class="sm-result-pct">'+prop.score+'%</div><div class="sm-result-bar-track"><div class="sm-result-bar-fill" id="smfill-'+i+'"></div></div></div>';
      results.appendChild(item);
      gsap.from(item, { opacity:0, x:20, duration:.4, ease:'power3.out' });
      setTimeout(function() {
        var fill = document.getElementById('smfill-'+i);
        if (fill) fill.style.width = prop.score+'%';
      }, 100);
      if (i === scored.length-1 && badge) {
        badge.innerHTML = '<span class="sm-ai-dot" style="background:var(--green)"></span> Match Complete';
        badge.style.color = 'var(--green)';
      }
    }, i*400+600);
  });
}

/* AGENT-V2-04 — Voice recognition */
function initVoiceNote(clientId) {
  var btn = document.getElementById('vn-record');
  var transcript = document.getElementById('vn-transcript');
  var textEl = document.getElementById('vn-text');
  var canvas = document.getElementById('vn-canvas');
  var label = document.getElementById('vn-label');
  if (!btn) return;
  var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) { btn.style.opacity='.4'; label.textContent='Voice not supported'; return; }
  var recognition = new SpeechRecognition();
  recognition.continuous = true; recognition.interimResults = true; recognition.lang = 'fr-FR';
  var isRecording = false, waveAnim;
  function startWave() {
    if (!canvas) return;
    var waveCtx = canvas.getContext('2d');
    var t = 0;
    waveAnim = setInterval(function() {
      waveCtx.clearRect(0,0,200,40);
      waveCtx.strokeStyle = '#C4714F';
      waveCtx.lineWidth = 1.5;
      waveCtx.beginPath();
      for (var x=0;x<200;x++) {
        var y = 20+Math.sin(x*.08+t)*(8+Math.random()*4)*(isRecording?1:.2);
        x===0 ? waveCtx.moveTo(x,y) : waveCtx.lineTo(x,y);
      }
      waveCtx.stroke(); t+=.15;
    }, 40);
  }
  btn.addEventListener('click', function() {
    if (!isRecording) {
      isRecording=true; btn.classList.add('recording');
      label.textContent='Stop Recording';
      transcript.style.display='block'; textEl.textContent='Listening\u2026';
      startWave(); recognition.start();
    } else {
      isRecording=false; btn.classList.remove('recording');
      label.textContent='Voice Note'; clearInterval(waveAnim); recognition.stop();
    }
  });
  recognition.addEventListener('result', function(e) {
    var full = '';
    for (var i=0;i<e.results.length;i++) full += e.results[i][0].transcript+' ';
    textEl.textContent = full;
    if (e.results[e.results.length-1].isFinal) {
      var crm = getCRM();
      var c = crm.clients.find(function(cl){return cl.id===clientId;});
      if (c) {
        c.notes = (c.notes||'') + '\n[Voice] ' + full.trim();
        c.lastContact = Date.now(); saveCRM(crm);
        addActivity('Note vocale ajout\u00e9e : '+c.name, 'info');
      }
    }
  });
}

/* AGENT-V2-05 — Lien partageable */
function generateClientLink(clientId) {
  var crm = getCRM();
  var client = crm.clients.find(function(c){return c.id===clientId;});
  if (!client) return;
  var data = { name:client.name, budget:client.budget, type:client.type, city:client.city, exp:Date.now()+7*86400000 };
  var hash = btoa(JSON.stringify(data)).replace(/[+]/g,'-').replace(/[/]/g,'_').replace(/[=]/g,'');
  var url = window.location.origin+window.location.pathname+'#client='+hash;
  navigator.clipboard.writeText(url).then(function() {
    addActivity('Lien copi\u00e9 : '+client.name+' \u2014 valable 7 jours', 'booking');
    showToast('Link copied! Valid 7 days.');
  });
}
function showToast(message) {
  var toast = document.createElement('div');
  toast.style.cssText = 'position:fixed;bottom:4rem;left:50%;transform:translateX(-50%);background:var(--sage);color:var(--deep);font-family:var(--font-m);font-size:.9rem;letter-spacing:.14em;text-transform:uppercase;padding:1.2rem 2.8rem;z-index:9999;pointer-events:none;box-shadow:0 8px 32px rgba(61,139,122,.3);';
  toast.textContent = message;
  document.body.appendChild(toast);
  gsap.from(toast, { y:20, opacity:0, duration:.4, ease:'power3.out' });
  gsap.to(toast, { y:-10, opacity:0, duration:.4, ease:'power2.in', delay:2.5, onComplete:function(){toast.remove();} });
}
window.addEventListener('load', function() {
  var hash = window.location.hash;
  if (hash.indexOf('#client=')===0) {
    try {
      var encoded = hash.replace('#client=','').replace(/-/g,'+').replace(/_/g,'/');
      var data = JSON.parse(atob(encoded));
      if (data.exp > Date.now()) showClientLandingPage(data);
    } catch(e) {}
  }
});
function showClientLandingPage(data) {
  var overlay = document.createElement('div');
  overlay.style.cssText = 'position:fixed;inset:0;z-index:8000;background:var(--deep);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:3.2rem;text-align:center;padding:4rem;';
  overlay.innerHTML = '<div style="font-family:var(--font-m);font-size:.9rem;letter-spacing:.25em;text-transform:uppercase;color:var(--sage)">Personal Selection for</div><h1 style="font-family:var(--font-d);font-size:clamp(4rem,8vw,10rem);font-weight:300;font-style:italic;line-height:.95">'+data.name+'</h1><div style="font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;color:var(--muted)">'+(data.type||'')+' \u00b7 '+(data.city||'')+' \u00b7 '+(data.budget||'')+'</div><div style="font-family:var(--font-m);font-size:.85rem;color:rgba(245,242,237,.3)">Curated by your NOVUS advisor</div>';
  var btn = document.createElement('button');
  btn.style.cssText = 'margin-top:1.6rem;background:var(--sage);color:var(--deep);border:none;font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;padding:1.4rem 3.6rem;cursor:pointer;';
  btn.textContent = 'View Your Selection \u2192';
  btn.addEventListener('click', function() { overlay.remove(); });
  overlay.appendChild(btn);
  document.body.appendChild(overlay);
  gsap.from(overlay, { opacity:0, duration:.6, ease:'power3.out' });
}

/* AGENT-V2-06 — Live activity feed */
function initLiveActivityFeed() {
  var events = [
    { text:'Une personne consulte Tour Lumi\u00e8re depuis Paris', type:'info', delay:35000 },
    { text:'Nouveau formulaire re\u00e7u pour Villa Aurelia', type:'booking', delay:68000 },
    { text:'Tour Lumi\u00e8re vue 3 fois aujourd\u0027hui', type:'info', delay:95000 },
    { text:'Prix consult\u00e9 : The Meridian (London)', type:'info', delay:180000 },
    { text:'Alerte : Villa Aurelia disponible depuis 14 jours', type:'alert', delay:220000 },
    { text:'Nouvelle demande de brochure : Loft Lumino', type:'booking', delay:260000 }
  ];
  events.forEach(function(ev) {
    setTimeout(function() {
      if (typeof crmOpen !== 'undefined' && !crmOpen) return;
      if (typeof addActivity === 'function') addActivity(ev.text, ev.type);
      window.dispatchEvent(new Event('crm-activity'));
    }, ev.delay);
  });
}

/* AGENT-V2-07 — Pipeline Timeline */
function renderPipelineTimeline() {
  var rows = document.getElementById('plt-rows');
  var axisEl = document.querySelector('.plt-axis');
  if (!rows) return;
  var now = new Date();
  var months = [];
  for (var i=-2;i<4;i++) {
    var d = new Date(now.getFullYear(), now.getMonth()+i, 1);
    months.push({ label:d.toLocaleString('en-GB',{month:'short'})+' '+d.getFullYear() });
  }
  if (axisEl) axisEl.innerHTML = months.map(function(m){return '<div class="plt-month">'+m.label+'</div>';}).join('');
  rows.innerHTML = '';
  var data = getCRM();
  var totalDays = 6*30;
  var startDate = new Date(now.getFullYear(), now.getMonth()-2, 1);
  data.leads.forEach(function(lead, i) {
    var leadDate = lead.date ? new Date(lead.date) : now;
    var startDay = Math.floor((leadDate-startDate)/86400000);
    var left = Math.max(0, (startDay/totalDays)*100);
    var width = Math.min(100-left, 15+Math.random()*10);
    var deal = document.createElement('div');
    deal.className = 'plt-deal stage-'+lead.stage;
    deal.style.cssText = 'left:'+left+'%;width:'+width+'%;top:'+(i%5*48+8)+'px;';
    deal.textContent = lead.name+' \u2014 '+lead.prop;
    rows.appendChild(deal);
    gsap.from(deal, { scaleX:0, transformOrigin:'left', duration:.6, delay:i*.08, ease:'power3.out' });
  });
}

/* Pipeline view toggle */
document.querySelectorAll('.pvt-btn').forEach(function(btn) {
  btn.addEventListener('click', function() {
    document.querySelectorAll('.pvt-btn').forEach(function(b){b.classList.remove('active');});
    btn.classList.add('active');
    var view = btn.dataset.view;
    var pb = document.getElementById('pipeline-board');
    if (pb) pb.style.display = view==='kanban'?'grid':'none';
    var tl = document.getElementById('pipeline-timeline');
    if (tl) {
      tl.style.display = view==='timeline'?'block':'none';
      if (view==='timeline') renderPipelineTimeline();
    }
  });
});

/* V5 INIT */
initHorizontalScroll();
initScrollWheel();
initScrollZoom();
initTextPhysics();
initObliqueScroll();
initLiquidCursor();
initLensDistortion();
initLiquidGridReveal();
initMicroSounds();
initImageFragment();
initLiveActivityFeed();

"""

js_escaped = esc(js_block)
tpl = tpl[:last_script_pos] + js_escaped + tpl[last_script_pos:]
print("Step 6: JS injected. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 7: Inject HTML additions into CRM panel
# Add timeline, smart match, voice note, share btn into client detail
# Add pipeline view toggle and timeline view
# ═══════════════════════════════════════════════════

# Add pipeline view toggle + timeline div after pipeline-board
pipeline_board_marker = 'id="pipeline-board"'
pb_pos = tpl.index(pipeline_board_marker)
# Find end of pipeline-board div — search for the next </div> after a reasonable distance
# Actually, insert the toggle before pipeline-board and timeline after
pb_tag_start = tpl[:pb_pos].rindex('<')

toggle_html = r"""
<div class="pipeline-view-toggle" id="pvt">
  <button class="pvt-btn active" data-view="kanban">Kanban</button>
  <button class="pvt-btn" data-view="timeline">Timeline</button>
</div>
"""
toggle_escaped = esc(toggle_html)
tpl = tpl[:pb_tag_start] + toggle_escaped + tpl[pb_tag_start:]

# Now add timeline div after pipeline-board closing
# Find pipeline-board again (offset shifted)
pb_pos2 = tpl.index('id="pipeline-board"')
# Find the matching closing — look for pattern after pipeline-board
# The board has columns, find end by searching for the next major section
# Let's add after pipeline-board's parent closing - just search for closing </div> pattern
# Simpler: insert after pipeline-board's grid div
# Find the </div> that closes pipeline-board - scan forward for balanced divs
board_start = tpl[:pb_pos2].rindex('<')
# Count divs from board_start
depth = 0
pos = board_start
while pos < len(tpl):
    if tpl[pos:pos+4] == '<div':
        depth += 1
    elif tpl[pos:pos+6] == '</div>':
        depth -= 1
        if depth == 0:
            pos += 6
            break
    pos += 1

timeline_div_html = r"""
<div class="pipeline-timeline" id="pipeline-timeline" style="display:none">
  <div class="plt-axis"></div>
  <div class="plt-rows" id="plt-rows"></div>
</div>
"""
timeline_div_escaped = esc(timeline_div_html)
tpl = tpl[:pos] + timeline_div_escaped + tpl[pos:]
print("Step 7: Pipeline toggle + timeline injected. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# QUOTE VERIFICATION
# ═══════════════════════════════════════════════════

# Find the return '...' string in TPL5
ret_marker = "return '"
tpl5_in_content = content[:tpl5_start] + tpl + content[tpl9_start:]
# Actually let's verify just the tpl portion
# Find return ' in tpl
ret_idx = tpl.index("return '")
end_idx = tpl.rindex("';")
s = tpl[ret_idx+8:end_idx]

i = 0
problems = []
bs = chr(92)  # backslash
sq = chr(39)  # single quote
while i < len(s):
    if s[i] == bs:
        i += 2
        continue
    if s[i] == sq:
        problems.append(f'pos {i}: ...{s[max(0,i-30):i+30]}...')
    i += 1

if problems:
    print("\nQUOTE PROBLEMS:")
    for p in problems[:20]:
        print(p)
    print(f"Total: {len(problems)} problems")
    raise SystemExit(1)

print("\nQuotes OK! Final size:", len(tpl), "chars")

# Write back
content = content[:tpl5_start] + tpl + content[tpl9_start:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("V5 PATCH APPLIED!")
