#!/usr/bin/env python3
"""
PATCH V7 — NOVUS CAPITAL
1. New indigo palette (replace :root + all var refs + rgba refs)
2. Remove magnetic cursor + liquid cursor, add simple cursor
3. 3D buttons CSS
4. Lead card HTML + CSS + JS
5. Close buttons fix
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
# STEP 1: Replace :root block entirely
# ═══════════════════════════════════════════════════

old_root_start = tpl.index(':root{')
old_root_end = tpl.index('}', old_root_start) + 1

new_root = (":root{"
"--void:#07060F;--deep:#0D0B1F;--mid:#13102A;--surface:#1A1635;--lifted:#221E42;"
"--border:#2E2855;--border-dim:rgba(46,40,85,0.6);"
"--ivory:#F2EEF8;--cream:#E4DFEF;--sand:#BDB6D4;--muted:#7A7096;"
"--sage:#4F6EF7;--sage-light:#7090FF;--sage-pale:#B8C7FF;"
"--sage-dim:rgba(79,110,247,0.12);--sage-glow:rgba(79,110,247,0.25);"
"--cobalt:#4F6EF7;--cobalt-light:#7090FF;--cobalt-pale:#B8C7FF;"
"--cobalt-dim:rgba(79,110,247,0.12);--cobalt-glow:rgba(79,110,247,0.25);"
"--terra:#7C5CEF;--terra-light:#9B7EF8;--terra-pale:#C4B5FD;"
"--terra-dim:rgba(124,92,239,0.12);"
"--violet:#7C5CEF;--violet-light:#9B7EF8;--violet-pale:#C4B5FD;"
"--violet-dim:rgba(124,92,239,0.12);"
"--plat:#60A5FA;--plat-light:#93C5FD;--plat-dim:rgba(96,165,250,0.12);"
"--sky:#60A5FA;--sky-light:#93C5FD;--sky-dim:rgba(96,165,250,0.12);"
"--champ:#E8C97A;--champ-light:#F0D99A;--champ-dim:rgba(232,201,122,0.1);"
"--green:#34D399;--amber:#F59E0B;--rose:#F87171;"
"--font-d:\\'Cormorant Garamond\\',serif;"
"--font-b:\\'DM Sans\\',sans-serif;"
"--font-m:\\'DM Mono\\',monospace;"
"--ease-out:cubic-bezier(0.16,1,0.3,1);"
"--ease-io:cubic-bezier(0.76,0,0.24,1);"
"--ease-expo:cubic-bezier(0.19,1,0.22,1);"
"--ease-back:cubic-bezier(0.34,1.56,0.64,1);"
"--shadow-sage:0 0 40px rgba(79,110,247,0.2);"
"--shadow-cobalt:0 0 40px rgba(79,110,247,0.2);"
"--shadow-terra:0 0 40px rgba(124,92,239,0.15);"
"--shadow-violet:0 0 40px rgba(124,92,239,0.15);"
"--shadow-lift:0 24px 60px rgba(7,6,15,0.6);"
"--shadow-card:0 8px 32px rgba(7,6,15,0.5);"
"--grad-sage:linear-gradient(135deg,var(--cobalt) 0%,var(--cobalt-light) 100%);"
"--grad-terra:linear-gradient(135deg,var(--violet) 0%,var(--violet-light) 100%);"
"--grad-primary:linear-gradient(135deg,var(--cobalt) 0%,var(--violet) 100%);"
"}")

tpl = tpl[:old_root_start] + new_root + tpl[old_root_end:]
print("Step 1: :root replaced. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 2: Replace all rgba color references
# ═══════════════════════════════════════════════════

# sage green rgba(61,139,122,...) -> cobalt rgba(79,110,247,...)
tpl = tpl.replace('rgba(61,139,122,', 'rgba(79,110,247,')
# terra rgba(196,113,79,...) -> violet rgba(124,92,239,...)
tpl = tpl.replace('rgba(196,113,79,', 'rgba(124,92,239,')
# plat rgba(122,157,176,...) -> sky rgba(96,165,250,...)
tpl = tpl.replace('rgba(122,157,176,', 'rgba(96,165,250,')
# old void/deep rgba(8,15,20,...) -> new rgba(7,6,15,...)
tpl = tpl.replace('rgba(8,15,20,', 'rgba(7,6,15,')
# old dark bg rgba(11,23,32,...) -> new rgba(13,11,31,...)
tpl = tpl.replace('rgba(11,23,32,', 'rgba(13,11,31,')

# Update about--light background
tpl = tpl.replace('#EEE8DF', '#EEEAF5')
tpl = tpl.replace('#F0EBE3', '#EEEAF5')

print("Step 2: rgba colors replaced")

# ═══════════════════════════════════════════════════
# STEP 3: Remove liquid cursor canvas from HTML
# ═══════════════════════════════════════════════════

# Remove the canvas element
lc_html = '<canvas class="liquid-cursor" id="liquid-cursor"'
lc_pos = tpl.find(lc_html)
if lc_pos >= 0:
    # Find end of this tag
    lc_end = tpl.index('>', lc_pos) + 1
    # Also remove the closing </canvas> if present
    next_close = tpl.find('</canvas>', lc_end)
    if next_close >= 0 and next_close - lc_end < 5:
        lc_end = next_close + 9
    tpl = tpl[:lc_pos] + tpl[lc_end:]
    print("Step 3: Liquid cursor canvas removed. Size:", len(tpl))
else:
    print("Step 3: No liquid cursor canvas found")

# ═══════════════════════════════════════════════════
# STEP 4: Inject V7 CSS before </style>
# ═══════════════════════════════════════════════════

css_block = r"""

/* ════════ V7 — 3D BUTTONS ════════ */
.btn-3d {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 1.2rem;
  cursor: none;
  border: none;
  outline: none;
  font-family: var(--font-m);
  font-size: 1.1rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  user-select: none;
  border-radius: 999px;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.18),
    0 6px 0 rgba(0,0,0,.25),
    0 8px 20px rgba(0,0,0,.2);
  transform: translateY(0);
  transition: transform .12s ease, box-shadow .12s ease;
}
.btn-3d:active {
  transform: translateY(4px);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 2px 0 rgba(0,0,0,.2), 0 3px 8px rgba(0,0,0,.15);
}
.btn-3d:hover {
  transform: translateY(-2px);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.22), 0 8px 0 rgba(0,0,0,.28), 0 12px 28px rgba(0,0,0,.25);
}
.btn-3d--cobalt {
  background: linear-gradient(180deg, #7090FF 0%, #4F6EF7 50%, #3B57D4 100%);
  color: #fff;
  padding: 1.6rem 3.6rem;
}
.btn-3d--cobalt:hover {
  box-shadow: inset 0 1px 0 rgba(255,255,255,.22), 0 8px 0 rgba(59,87,212,.4), 0 12px 32px rgba(79,110,247,.35);
}
.btn-3d--violet {
  background: linear-gradient(180deg, #9B7EF8 0%, #7C5CEF 50%, #5E3ED4 100%);
  color: #fff;
  padding: 1.6rem 3.6rem;
}
.btn-3d--ghost {
  background: rgba(245,242,255,.06);
  border: 1px solid rgba(139,92,246,.3);
  color: var(--violet-light, #C4B5FD);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.08), 0 4px 0 rgba(0,0,0,.15), 0 6px 16px rgba(0,0,0,.12);
}
.btn-3d--ghost:hover { border-color: rgba(139,92,246,.6); background: rgba(139,92,246,.1); }
.btn-3d--sm { padding: 1rem 2rem; font-size: .9rem; }
.btn-3d--xl { padding: 2.2rem 6rem; font-size: 1.2rem; }

/* ════════ V7 — LEAD CARD ════════ */
.lead-card-overlay {
  position: fixed; inset: 0; z-index: 9800;
  display: none; align-items: center; justify-content: center;
  background: rgba(7,6,15,.85);
  backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
  padding: 2rem;
}
.lead-card-overlay.open { display: flex; }
.lead-card {
  width: 100%; max-width: 580px;
  background: var(--surface);
  border-radius: 20px;
  border: 1px solid rgba(79,110,247,.2);
  box-shadow: 0 2px 4px rgba(0,0,0,.2), 0 8px 16px rgba(0,0,0,.18), 0 20px 40px rgba(0,0,0,.15), inset 0 1px 0 rgba(255,255,255,.06);
  overflow: hidden;
}
.lc-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 2.4rem 2.8rem;
  border-bottom: 1px solid rgba(245,242,255,.06);
  background: rgba(79,110,247,.06);
}
.lc-header-left { display: flex; align-items: center; gap: 1.6rem; }
.lc-icon {
  width: 44px; height: 44px;
  background: rgba(79,110,247,.15); border: 1px solid rgba(79,110,247,.3);
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.4rem; color: var(--cobalt);
  transition: background .3s, border-color .3s, color .3s;
}
.lc-title {
  font-family: var(--font-d); font-size: 2.4rem; font-weight: 300;
  font-style: italic; margin-bottom: .2rem; color: var(--ivory);
}
.lc-subtitle {
  font-family: var(--font-m); font-size: .8rem; letter-spacing: .14em;
  text-transform: uppercase; color: var(--muted);
}
.lc-close {
  width: 32px; height: 32px; background: none;
  border: 1px solid rgba(245,242,255,.12); border-radius: 8px;
  color: var(--muted); cursor: none; font-size: 1.1rem;
  display: flex; align-items: center; justify-content: center;
  transition: all .25s;
}
.lc-close:hover { border-color: var(--violet); color: var(--violet); }
.lc-step { padding: 2.4rem 2.8rem; }
.lc-step-label {
  font-family: var(--font-m); font-size: .8rem; letter-spacing: .18em;
  text-transform: uppercase; color: rgba(245,242,255,.35); margin-bottom: 1.8rem;
}
.lc-types { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; }
.lc-type-btn {
  display: flex; flex-direction: column; align-items: flex-start; gap: .6rem;
  padding: 1.8rem; background: rgba(245,242,255,.03);
  border: 1px solid rgba(245,242,255,.08); border-radius: 14px;
  cursor: none; transition: all .3s; text-align: left;
}
.lc-type-btn:hover {
  background: rgba(79,110,247,.08); border-color: rgba(79,110,247,.3);
  transform: translateY(-2px); box-shadow: 0 8px 24px rgba(79,110,247,.15);
}
.lc-type-btn.selected {
  border-color: var(--cobalt); background: rgba(79,110,247,.1);
  box-shadow: 0 0 0 1px var(--cobalt);
}
.ltb-icon { font-size: 1.6rem; margin-bottom: .2rem; }
.ltb-label {
  font-family: var(--font-d); font-size: 1.6rem; font-weight: 300;
  font-style: italic; color: var(--ivory);
}
.ltb-sub {
  font-family: var(--font-m); font-size: .75rem; letter-spacing: .1em;
  text-transform: uppercase; color: var(--muted);
}
.lc-type-badge {
  display: inline-flex; align-items: center; gap: .6rem;
  padding: .4rem 1.2rem .4rem .8rem; border-radius: 999px;
  font-family: var(--font-m); font-size: .75rem; letter-spacing: .12em;
  text-transform: uppercase; margin-bottom: 2rem; border: 1px solid currentColor;
}
.lc-form { display: flex; flex-direction: column; gap: 1.2rem; }
.lc-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; }
.lc-field { display: flex; flex-direction: column; gap: .5rem; }
.lc-field--full { grid-column: 1 / -1; }
.lc-field label {
  font-family: var(--font-m); font-size: .72rem; letter-spacing: .15em;
  text-transform: uppercase; color: rgba(245,242,255,.4);
}
.lc-input {
  background: rgba(245,242,255,.04); border: none;
  border-bottom: 1px solid rgba(245,242,255,.12);
  color: var(--ivory); font-family: var(--font-b);
  font-size: 1.4rem; font-weight: 300; padding: .9rem 1rem;
  outline: none; transition: border-color .3s, background .3s;
  cursor: none; width: 100%; border-radius: 0;
}
.lc-input:focus { border-bottom-color: var(--cobalt); background: rgba(79,110,247,.04); }
.lc-input::placeholder { color: rgba(245,242,255,.2); }
.lc-select { appearance: none; -webkit-appearance: none; }
.lc-textarea { resize: none; min-height: 72px; }
.lc-nav {
  display: flex; align-items: center; justify-content: space-between;
  margin-top: 2.4rem; padding-top: 2rem;
  border-top: 1px solid rgba(245,242,255,.06);
}
.lc-back-btn {
  background: none; border: none;
  font-family: var(--font-m); font-size: .85rem; letter-spacing: .14em;
  text-transform: uppercase; color: var(--muted); cursor: none; transition: color .3s;
}
.lc-back-btn:hover { color: var(--ivory); }
.lc-next-btn {
  background: var(--cobalt); color: #fff; border: none; border-radius: 999px;
  font-family: var(--font-m); font-size: .9rem; letter-spacing: .14em;
  text-transform: uppercase; padding: 1rem 2.8rem; cursor: none;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.2), 0 4px 0 rgba(39,70,180,.4), 0 6px 16px rgba(79,110,247,.3);
  transition: transform .12s, box-shadow .12s;
}
.lc-next-btn:hover { transform: translateY(-2px); }
.lc-next-btn:active { transform: translateY(3px); box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(39,70,180,.4); }
.lc-save-btn {
  display: flex; align-items: center; gap: 1rem;
  background: linear-gradient(135deg, var(--cobalt), var(--violet)); color: #fff;
  border: none; border-radius: 999px;
  font-family: var(--font-m); font-size: .9rem; letter-spacing: .14em;
  text-transform: uppercase; padding: 1rem 2.8rem; cursor: none;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.2), 0 4px 0 rgba(60,40,180,.4), 0 8px 24px rgba(79,110,247,.35);
  transition: transform .12s, box-shadow .12s;
}
.lc-save-btn:hover { transform: translateY(-2px); }
.lc-save-btn:active { transform: translateY(3px); }
.lc-success {
  text-align: center; padding: 5.6rem 2.8rem;
  display: flex; flex-direction: column; align-items: center; gap: 1.6rem;
}
.lc-success-icon {
  width: 64px; height: 64px;
  background: rgba(79,110,247,.15); border: 2px solid var(--cobalt);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 2rem; color: var(--cobalt);
  box-shadow: 0 0 24px rgba(79,110,247,.3);
}
.lc-success-title {
  font-family: var(--font-d); font-size: 3.2rem; font-weight: 300;
  font-style: italic; color: var(--ivory);
}
.lc-success-sub {
  font-family: var(--font-m); font-size: .85rem; letter-spacing: .15em;
  text-transform: uppercase; color: var(--muted);
}

/* ════════ V7 — PALETTE EFFECTS ════════ */
.gradient-text {
  background: linear-gradient(135deg, var(--cobalt-pale) 0%, var(--violet-pale) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.nav__agent-btn {
  background: rgba(79,110,247,.08) !important;
  border-color: rgba(79,110,247,.3) !important;
  color: var(--cobalt) !important;
}
.nav__agent-btn:hover {
  background: rgba(79,110,247,.18) !important;
  border-color: var(--cobalt) !important;
  box-shadow: 0 0 24px rgba(79,110,247,.25) !important;
}

@media (max-width: 600px) {
  .lc-row { grid-template-columns: 1fr; }
  .lc-types { grid-template-columns: 1fr; }
}
"""

css_escaped = esc(css_block)
style_pos = tpl.index('</style>')
tpl = tpl[:style_pos] + css_escaped + tpl[style_pos:]
print("Step 4: CSS injected. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 5: Inject lead card HTML before </body>
# ═══════════════════════════════════════════════════

lead_card_html = r"""
<div class="lead-card-overlay" id="lead-card-overlay">
  <div class="lead-card" id="lead-card">
    <div class="lc-header">
      <div class="lc-header-left">
        <span class="lc-icon" id="lc-icon">&#9670;</span>
        <div>
          <h3 class="lc-title">New Prospect</h3>
          <p class="lc-subtitle" id="lc-subtitle">Select lead type to continue</p>
        </div>
      </div>
      <button class="lc-close" id="lc-close">&#10005;</button>
    </div>
    <div class="lc-step" id="lc-step-1">
      <div class="lc-step-label">What type of lead?</div>
      <div class="lc-types">
        <button class="lc-type-btn" data-type="locataire" data-color="#4F6EF7" data-icon="&#8962;">
          <span class="ltb-icon">&#8962;</span>
          <span class="ltb-label">Tenant</span>
          <span class="ltb-sub">Looking to rent</span>
        </button>
        <button class="lc-type-btn" data-type="acheteur" data-color="#3D8B7A" data-icon="&#9670;">
          <span class="ltb-icon">&#9670;</span>
          <span class="ltb-label">Buyer</span>
          <span class="ltb-sub">Looking to purchase</span>
        </button>
        <button class="lc-type-btn" data-type="investisseur" data-color="#8B5CF6" data-icon="&#9650;">
          <span class="ltb-icon">&#9650;</span>
          <span class="ltb-label">Investor</span>
          <span class="ltb-sub">ROI focused</span>
        </button>
        <button class="lc-type-btn" data-type="corporate" data-color="#C4714F" data-icon="&#9673;">
          <span class="ltb-icon">&#9673;</span>
          <span class="ltb-label">Corporate</span>
          <span class="ltb-sub">Company / Fund</span>
        </button>
      </div>
    </div>
    <div class="lc-step" id="lc-step-2" style="display:none">
      <div class="lc-type-badge" id="lc-type-badge"></div>
      <div class="lc-step-label">Contact Information</div>
      <div class="lc-form">
        <div class="lc-row">
          <div class="lc-field"><label>First Name *</label><input type="text" id="lc-fname" placeholder="Alexandra" class="lc-input" required></div>
          <div class="lc-field"><label>Last Name *</label><input type="text" id="lc-lname" placeholder="Moreau" class="lc-input" required></div>
        </div>
        <div class="lc-row">
          <div class="lc-field"><label>Email *</label><input type="email" id="lc-email" placeholder="a.moreau@example.com" class="lc-input" required></div>
          <div class="lc-field"><label>Phone</label><input type="tel" id="lc-phone" placeholder="+33 6 00 00 00 00" class="lc-input"></div>
        </div>
        <div class="lc-row">
          <div class="lc-field"><label>Company</label><input type="text" id="lc-company" placeholder="Moreau Capital" class="lc-input"></div>
          <div class="lc-field"><label>Nationality</label><input type="text" id="lc-nationality" placeholder="Fran&#231;aise" class="lc-input"></div>
        </div>
      </div>
      <div class="lc-nav">
        <button class="lc-back-btn" id="lc-back-1">&#8592; Back</button>
        <button class="lc-next-btn" id="lc-next-2">Continue &#8594;</button>
      </div>
    </div>
    <div class="lc-step" id="lc-step-3" style="display:none">
      <div class="lc-step-label">Property Requirements</div>
      <div class="lc-form">
        <div class="lc-row">
          <div class="lc-field"><label>Property Interest</label><select id="lc-prop" class="lc-input lc-select"><option value="">Select property&#8230;</option><option>Tour Lumi&#232;re &#8212; Paris 16e</option><option>The Meridian &#8212; London</option><option>Villa Aurelia &#8212; Athens</option><option>Le Patio &#8212; Monaco</option><option>Loft Lumino &#8212; Z&#252;rich</option><option>Casa Bianca &#8212; Santorini</option><option>Other / To Define</option></select></div>
          <div class="lc-field"><label>Property Type</label><select id="lc-proptype" class="lc-input lc-select"><option value="">Any type&#8230;</option><option>Penthouse</option><option>Villa</option><option>Apartment</option><option>Office</option><option>Loft</option></select></div>
        </div>
        <div class="lc-row">
          <div class="lc-field"><label>Budget (&#8364;/month)</label><input type="text" id="lc-budget" placeholder="&#8364; 10,000 &#8211; 20,000" class="lc-input"></div>
          <div class="lc-field"><label>Target City</label><select id="lc-city" class="lc-input lc-select"><option value="">Any city&#8230;</option><option>Paris</option><option>London</option><option>Athens</option><option>Monaco</option><option>Z&#252;rich</option><option>Santorini</option><option>Multiple</option></select></div>
        </div>
        <div class="lc-row">
          <div class="lc-field"><label>Last Offer</label><input type="text" id="lc-lastoffer" placeholder="&#8364; 18,500/mo" class="lc-input"></div>
          <div class="lc-field"><label>Timeline</label><select id="lc-timeline" class="lc-input lc-select"><option>Imm&#233;diat</option><option>1 mois</option><option>3 mois</option><option>6 mois</option><option>Flexible</option></select></div>
        </div>
        <div class="lc-field lc-field--full"><label>Agent Notes</label><textarea id="lc-notes" class="lc-input lc-textarea" placeholder="Contexte, motivations, contraintes&#8230;" rows="3"></textarea></div>
      </div>
      <div class="lc-nav">
        <button class="lc-back-btn" id="lc-back-2">&#8592; Back</button>
        <button class="lc-save-btn" id="lc-save"><span>Save Prospect</span><span>&#8594;</span></button>
      </div>
    </div>
    <div class="lc-step lc-success" id="lc-success" style="display:none">
      <div class="lc-success-icon">&#10003;</div>
      <div class="lc-success-title" id="lc-success-name">Prospect Added</div>
      <div class="lc-success-sub" id="lc-success-sub">Added to pipeline</div>
    </div>
  </div>
</div>
"""

lc_escaped = esc(lead_card_html)
body_pos = tpl.rindex('</body>')
tpl = tpl[:body_pos] + lc_escaped + tpl[body_pos:]
print("Step 5: Lead card HTML injected. Size:", len(tpl))

# ═══════════════════════════════════════════════════
# STEP 6: Inject V7 JavaScript before last \x3c/script>
# ═══════════════════════════════════════════════════

scripts = list(re.finditer(re.escape('\\x3c/script>'), tpl))
last_script_pos = scripts[-1].start()

js_block = r"""

/* ════════════════════════════════════════════════════
   V7 — CURSOR SIMPLE + LEAD CARD + CLOSE FIX
════════════════════════════════════════════════════ */

/* CURSOR SIMPLE — no magnetic */
function initCursorSimple() {
  var dot = document.querySelector('.cursor__dot, .cursor__core');
  var ring = document.querySelector('.cursor__ring, .cursor__orbit');
  if (!dot && !ring) return;
  var mx=0, my=0, rx=0, ry=0;
  window.addEventListener('mousemove', function(e) {
    mx = e.clientX; my = e.clientY;
    if (dot) gsap.to(dot, { x: mx, y: my, duration: .06 });
  });
  gsap.ticker.add(function() {
    rx += (mx - rx) * .11;
    ry += (my - ry) * .11;
    if (ring) gsap.set(ring, { x: rx, y: ry });
  });
  document.querySelectorAll('a, button').forEach(function(el) {
    el.addEventListener('mouseenter', function() {
      if (ring) gsap.to(ring, { scale: 1.6, duration: .3, ease: 'power2.out' });
    });
    el.addEventListener('mouseleave', function() {
      if (ring) gsap.to(ring, { scale: 1, duration: .3, ease: 'power2.out' });
    });
  });
  document.querySelectorAll('.wi, .prop-stacked__item, .flip-card').forEach(function(el) {
    el.addEventListener('mouseenter', function() {
      if (ring) gsap.to(ring, { scale: 2.2, duration: .4, ease: 'power2.out' });
    });
    el.addEventListener('mouseleave', function() {
      if (ring) gsap.to(ring, { scale: 1, duration: .3, ease: 'power2.out' });
    });
  });
}

/* LEAD CARD LOGIC */
var selectedLeadType = null;
var selectedLeadColor = '#4F6EF7';
var selectedLeadIcon = '\u25C6';

function openLeadCard() {
  var overlay = document.getElementById('lead-card-overlay');
  if (!overlay) return;
  selectedLeadType = null;
  document.querySelectorAll('.lc-type-btn').forEach(function(b) { b.classList.remove('selected'); });
  ['lc-step-2','lc-step-3','lc-success'].forEach(function(id) {
    var el = document.getElementById(id);
    if (el) el.style.display = 'none';
  });
  var step1 = document.getElementById('lc-step-1');
  if (step1) step1.style.display = 'block';
  // Clear fields
  ['lc-fname','lc-lname','lc-email','lc-phone','lc-company','lc-nationality','lc-budget','lc-lastoffer','lc-notes'].forEach(function(id) {
    var el = document.getElementById(id);
    if (el) el.value = '';
  });
  overlay.classList.add('open');
  document.body.style.overflow = 'hidden';
  gsap.fromTo(document.getElementById('lead-card'),
    { opacity:0, y:24, scale:.97 },
    { opacity:1, y:0, scale:1, duration:.4, ease:'back.out(1.8)' });
}

function closeLeadCard() {
  var overlay = document.getElementById('lead-card-overlay');
  if (!overlay) return;
  gsap.to(document.getElementById('lead-card'), {
    opacity:0, y:16, scale:.97, duration:.25,
    onComplete: function() { overlay.classList.remove('open'); document.body.style.overflow=''; }
  });
}

function goToStep(fromId, toId) {
  var from = document.getElementById(fromId);
  var to = document.getElementById(toId);
  if (!from || !to) return;
  gsap.to(from, { opacity:0, x:-20, duration:.25, ease:'power2.in',
    onComplete: function() {
      from.style.display = 'none';
      to.style.display = 'block';
      gsap.fromTo(to, { opacity:0, x:20 }, { opacity:1, x:0, duration:.3, ease:'power3.out' });
    }
  });
}

function initLeadCard() {
  document.getElementById('lc-close')?.addEventListener('click', closeLeadCard);
  document.getElementById('lead-card-overlay')?.addEventListener('click', function(e) {
    if (e.target === document.getElementById('lead-card-overlay')) closeLeadCard();
  });

  document.querySelectorAll('.lc-type-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.lc-type-btn').forEach(function(b) { b.classList.remove('selected'); });
      btn.classList.add('selected');
      selectedLeadType = btn.dataset.type;
      selectedLeadColor = btn.dataset.color;
      selectedLeadIcon = btn.querySelector('.ltb-icon').textContent;
      var icon = document.getElementById('lc-icon');
      if (icon) {
        icon.textContent = selectedLeadIcon;
        icon.style.background = selectedLeadColor + '22';
        icon.style.borderColor = selectedLeadColor + '55';
        icon.style.color = selectedLeadColor;
      }
      gsap.from(btn, { scale:.95, duration:.25, ease:'back.out(3)' });
      setTimeout(function() { goToStep('lc-step-1', 'lc-step-2'); }, 400);
      var badge = document.getElementById('lc-type-badge');
      if (badge) {
        badge.textContent = selectedLeadIcon + ' ' + btn.querySelector('.ltb-label').textContent;
        badge.style.color = selectedLeadColor;
        badge.style.borderColor = selectedLeadColor + '55';
        badge.style.background = selectedLeadColor + '18';
      }
      var sub = document.getElementById('lc-subtitle');
      if (sub) sub.textContent = btn.querySelector('.ltb-label').textContent + ' lead';
    });
  });

  document.getElementById('lc-next-2')?.addEventListener('click', function() {
    var fname = document.getElementById('lc-fname')?.value.trim();
    var lname = document.getElementById('lc-lname')?.value.trim();
    var email = document.getElementById('lc-email')?.value.trim();
    if (!fname || !lname || !email) {
      [['lc-fname',fname],['lc-lname',lname],['lc-email',email]].forEach(function(pair) {
        if (!pair[1]) {
          var el = document.getElementById(pair[0]);
          gsap.to(el, { x:-5, duration:.05, yoyo:true, repeat:5 });
        }
      });
      return;
    }
    goToStep('lc-step-2', 'lc-step-3');
  });

  document.getElementById('lc-back-1')?.addEventListener('click', function() { goToStep('lc-step-2', 'lc-step-1'); });
  document.getElementById('lc-back-2')?.addEventListener('click', function() { goToStep('lc-step-3', 'lc-step-2'); });

  document.getElementById('lc-save')?.addEventListener('click', function() {
    var crm = getCRM();
    var fname = document.getElementById('lc-fname')?.value.trim() || '';
    var lname = document.getElementById('lc-lname')?.value.trim() || '';
    var fullName = fname + ' ' + lname;
    crm.leads.push({
      id: 'l' + Date.now(),
      name: fullName,
      email: document.getElementById('lc-email')?.value.trim(),
      phone: document.getElementById('lc-phone')?.value.trim(),
      company: document.getElementById('lc-company')?.value.trim(),
      type: selectedLeadType,
      typeColor: selectedLeadColor,
      prop: document.getElementById('lc-prop')?.value || '',
      propType: document.getElementById('lc-proptype')?.value || '',
      budget: document.getElementById('lc-budget')?.value.trim(),
      city: document.getElementById('lc-city')?.value || '',
      lastOffer: document.getElementById('lc-lastoffer')?.value.trim(),
      timeline: document.getElementById('lc-timeline')?.value || '',
      sellerNotes: document.getElementById('lc-notes')?.value.trim(),
      stage: 'prospect',
      date: new Date().toISOString().split('T')[0],
      createdAt: Date.now()
    });
    saveCRM(crm);
    if (typeof addActivity === 'function') addActivity('Nouveau ' + selectedLeadType + ' : ' + fullName, 'booking');
    goToStep('lc-step-3', 'lc-success');
    var succName = document.getElementById('lc-success-name');
    var succSub = document.getElementById('lc-success-sub');
    if (succName) succName.textContent = fullName;
    if (succSub) succSub.textContent = (selectedLeadType||'lead') + ' \u00b7 ' + (document.getElementById('lc-prop')?.value || 'No property yet');
    gsap.from('.lc-success-icon', { scale:0, duration:.5, ease:'back.out(3)' });
    setTimeout(function() {
      closeLeadCard();
      setTimeout(function() { if(typeof renderPipeline==='function') renderPipeline(); }, 300);
    }, 2000);
    if (typeof showToast === 'function') showToast(fullName + ' added to pipeline');
  });
}

/* OVERRIDE pipeline-add to use lead card */
var origPipelineAdd = document.getElementById('pipeline-add');
if (origPipelineAdd) {
  var newBtn = origPipelineAdd.cloneNode(true);
  origPipelineAdd.parentNode.replaceChild(newBtn, origPipelineAdd);
  newBtn.addEventListener('click', openLeadCard);
}

/* CLOSE BUTTONS FIX */
function initAllCloseButtons() {
  document.getElementById('acrm-close')?.addEventListener('click', function() {
    if (typeof closeAgentDashboard === 'function') closeAgentDashboard();
  });
  document.getElementById('vtour-close')?.addEventListener('click', function() {
    var ov = document.getElementById('vtour-overlay');
    if (ov) gsap.to(ov, { opacity:0, duration:.4, onComplete:function(){ ov.classList.remove('open'); ov.style.opacity=''; } });
    document.body.style.overflow = '';
  });
  document.getElementById('pm-close')?.addEventListener('click', function() {
    var pm = document.getElementById('present-mode');
    if (pm) gsap.to(pm, { opacity:0, duration:.4, onComplete:function(){ pm.style.display='none'; pm.style.opacity=''; } });
    document.body.style.overflow = '';
  });
  document.getElementById('peo-close')?.addEventListener('click', function() {
    var ov = document.getElementById('prop-expand-overlay');
    if (ov) gsap.to(ov, { opacity:0, duration:.4, onComplete:function(){ ov.classList.remove('open'); ov.style.opacity=''; } });
  });
  document.getElementById('compare-close')?.addEventListener('click', function() {
    var m = document.getElementById('compare-modal');
    if (m) gsap.to(m, { opacity:0, duration:.3, onComplete:function(){ m.classList.remove('open'); } });
    document.body.style.overflow = '';
  });
  document.addEventListener('keydown', function(e) {
    if (e.key !== 'Escape') return;
    var pm = document.getElementById('present-mode');
    if (pm && pm.style.display !== 'none') { document.getElementById('pm-close')?.click(); return; }
    var vt = document.getElementById('vtour-overlay');
    if (vt && vt.classList.contains('open')) { document.getElementById('vtour-close')?.click(); return; }
    var lco = document.getElementById('lead-card-overlay');
    if (lco && lco.classList.contains('open')) { closeLeadCard(); return; }
    var cm = document.getElementById('crm-modal');
    if (cm && cm.style.display === 'flex') { cm.style.display = 'none'; return; }
    var comp = document.getElementById('compare-modal');
    if (comp && comp.classList.contains('open')) { document.getElementById('compare-close')?.click(); return; }
    var acrm = document.getElementById('agent-crm');
    if (acrm && acrm.classList.contains('open')) { if(typeof closeAgentDashboard==='function') closeAgentDashboard(); return; }
  });
}

/* V7 INIT */
initCursorSimple();
initLeadCard();
initAllCloseButtons();

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

i = 0; problems = []
bs = chr(92); sq = chr(39)
while i < len(s):
    if s[i] == bs: i += 2; continue
    if s[i] == sq:
        problems.append(f'pos {i}: ...{repr(s[max(0,i-30):i+30])}...')
    i += 1

if problems:
    print(f"\nQUOTE PROBLEMS: {len(problems)}")
    for p in problems[:10]: print(p)
    sys.exit(1)

print(f"\nQuotes OK! Final size: {len(tpl)} chars")

content = content[:tpl5_start] + tpl + content[tpl9_start:]
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("V7 PATCH APPLIED!")
