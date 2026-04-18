#!/usr/bin/env python3
"""
BRIEF V4 — Agent CRM + Visual Effects
Patches TPL_ECOM_HTML['5'] with:
- Agent button in navbar
- Full 5-tab CRM dashboard
- Liquid glass, holographic foil, skyline SVG, particle explosion
"""

filepath = r"C:\vantage-clean\crm-v2-push\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

tpl_start = content.index("TPL_ECOM_HTML['5']")
tpl_end = content.index("TPL_ECOM_HTML['9']")
tpl = content[tpl_start:tpl_end]
print(f"Template size before: {len(tpl)}")

def esc(s):
    """Escape a string for insertion into JS template string"""
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')

# ============================================================
# 1. ADD AGENT BUTTON IN NAVBAR (before nav__btn)
# ============================================================
# Find the nav__btn in the HTML body section (not CSS)
# We need to find the actual HTML element, not the CSS class definition
# Look for the nav button HTML - find 'class="nav__btn' in the HTML section

import re
# Find all occurrences of nav__btn in HTML context (has href or mag-btn)
nav_btn_html = tpl.find('class=\\"nav__btn mag-btn\\"')
if nav_btn_html < 0:
    nav_btn_html = tpl.find('class="nav__btn mag-btn"')
if nav_btn_html < 0:
    # Try without escaped quotes
    nav_btn_html = tpl.find("nav__btn mag-btn")
    if nav_btn_html > 0:
        # go back to find the opening tag
        tag_start = tpl.rfind('<', 0, nav_btn_html)
        if tag_start > 0:
            nav_btn_html = tag_start

print(f"nav__btn HTML found at: {nav_btn_html}")

AGENT_BTN_HTML = (
    '<button class="nav__agent-btn" id="nav-agent-btn" title="Agent Access">'
    '<span class="nav__agent-icon">'
    '<span class="nav__agent-dot"></span>'
    '<span class="nav__agent-dot"></span>'
    '<span class="nav__agent-dot"></span>'
    '<span class="nav__agent-dot"></span>'
    '</span>'
    '<span class="nav__agent-label">Agent</span>'
    '<span class="nav__agent-status" id="agent-status-dot"></span>'
    '</button>'
)

if nav_btn_html > 0:
    # Find the < before nav__btn
    insert_pos = tpl.rfind('<', 0, nav_btn_html)
    if insert_pos < 0:
        insert_pos = nav_btn_html
    agent_esc = esc(AGENT_BTN_HTML)
    tpl = tpl[:insert_pos] + agent_esc + tpl[insert_pos:]
    print("Step 1: Agent button inserted in navbar")
else:
    print("WARNING: Could not find nav__btn HTML - skipping agent button")

# ============================================================
# 2. ADD CSS
# ============================================================
NEW_CSS = r"""
/* ═══════════════════════════════════
   AGENT BUTTON — NAVBAR
═══════════════════════════════════ */
.nav__agent-btn{display:flex;align-items:center;gap:1rem;padding:1rem 2rem;background:rgba(61,139,122,.08);border:1px solid rgba(61,139,122,.3);color:var(--sage);font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;cursor:none;position:relative;overflow:hidden;transition:background .4s,border-color .4s,box-shadow .4s;}
.nav__agent-btn::before{content:'';position:absolute;inset:0;background:var(--grad-sage);opacity:0;transition:opacity .4s;}
.nav__agent-btn:hover{background:rgba(61,139,122,.18);border-color:var(--sage);box-shadow:0 0 24px rgba(61,139,122,.25);}
.nav__agent-btn:hover::before{opacity:.06;}
.nav__agent-icon{display:grid;grid-template-columns:1fr 1fr;gap:3px;width:14px;height:14px;position:relative;z-index:1;}
.nav__agent-dot{width:5px;height:5px;background:var(--sage);border-radius:50%;opacity:.5;animation:agent-dot-pulse 2s ease-in-out infinite;}
.nav__agent-dot:nth-child(1){animation-delay:0s;}.nav__agent-dot:nth-child(2){animation-delay:.2s;}.nav__agent-dot:nth-child(3){animation-delay:.4s;}.nav__agent-dot:nth-child(4){animation-delay:.6s;}
@keyframes agent-dot-pulse{0%,100%{opacity:.3;transform:scale(.8);}50%{opacity:1;transform:scale(1.2);}}
.nav__agent-btn:hover .nav__agent-dot{animation:agent-dot-wave .6s var(--ease-out) forwards;}
@keyframes agent-dot-wave{0%{transform:scale(.8);opacity:.3;}40%{transform:scale(1.5);opacity:1;}100%{transform:scale(1);opacity:.8;}}
.nav__agent-label{position:relative;z-index:1;}
.nav__agent-status{width:7px;height:7px;border-radius:50%;background:var(--green);box-shadow:0 0 8px rgba(77,184,150,.6);animation:status-live 2.4s ease-in-out infinite;position:relative;z-index:1;}
.nav__agent-status.has-alerts{background:var(--amber);box-shadow:0 0 8px rgba(212,164,90,.6);}

/* ═══════════════════════════════════
   AGENT CRM PANEL
═══════════════════════════════════ */
.agent-crm{position:fixed;inset:0;z-index:9600;display:none;}
.agent-crm.open{display:block;}
.acrm-backdrop{position:absolute;inset:0;background:rgba(8,15,20,.6);backdrop-filter:blur(8px);opacity:0;transition:opacity .4s;}
.agent-crm.open .acrm-backdrop{opacity:1;}
.acrm-panel{position:absolute;top:0;right:0;width:min(1200px,95vw);height:100vh;background:var(--deep);border-left:1px solid var(--border);display:flex;flex-direction:column;transform:translateX(100%);transition:transform .6s var(--ease-expo);box-shadow:-40px 0 120px rgba(8,15,20,.6);}
.agent-crm.open .acrm-panel{transform:translateX(0);}
.acrm-header{display:flex;align-items:center;justify-content:space-between;padding:2rem 3.2rem;border-bottom:1px solid var(--border);background:var(--void);flex-shrink:0;}
.acrm-header-left{display:flex;align-items:center;gap:3.2rem;}
.acrm-logo{display:flex;align-items:center;gap:1rem;font-family:var(--font-d);font-size:1.6rem;font-weight:400;letter-spacing:.3em;text-transform:uppercase;}
.acrm-logo-sub{font-family:var(--font-m);font-size:.75rem;letter-spacing:.2em;color:var(--muted);border-left:1px solid var(--border);padding-left:1rem;margin-left:.4rem;}
.acrm-greeting{font-family:var(--font-m);font-size:.9rem;letter-spacing:.12em;color:var(--muted);}
.acrm-header-right{display:flex;align-items:center;gap:2.4rem;}
.acrm-live-badge{display:flex;align-items:center;gap:.6rem;font-family:var(--font-m);font-size:.75rem;letter-spacing:.15em;text-transform:uppercase;color:var(--green);}
.acrm-live-dot{width:6px;height:6px;border-radius:50%;background:var(--green);box-shadow:0 0 6px var(--green);animation:status-live 2s ease-in-out infinite;}
.acrm-time{font-family:var(--font-m);font-size:1rem;letter-spacing:.12em;color:var(--sand);}
.acrm-close{width:36px;height:36px;background:none;border:1px solid var(--border);color:var(--muted);cursor:none;font-size:1.2rem;transition:all .25s;display:flex;align-items:center;justify-content:center;}
.acrm-close:hover{border-color:var(--terra);color:var(--terra);}
.acrm-tabs{display:flex;border-bottom:1px solid var(--border);background:var(--void);flex-shrink:0;overflow-x:auto;}
.acrm-tab{display:flex;align-items:center;gap:.8rem;padding:1.4rem 2.4rem;background:none;border:none;border-bottom:2px solid transparent;color:var(--muted);font-family:var(--font-m);font-size:.9rem;letter-spacing:.14em;text-transform:uppercase;cursor:none;white-space:nowrap;transition:color .3s,border-color .3s;}
.acrm-tab.active{color:var(--sage);border-bottom-color:var(--sage);}
.acrm-tab:hover:not(.active){color:var(--ivory);}
.acrm-tab-icon{font-size:1.1rem;}
.acrm-tab-badge{background:var(--sage-dim);border:1px solid rgba(61,139,122,.3);color:var(--sage);font-size:.7rem;padding:.1rem .5rem;border-radius:10px;min-width:18px;text-align:center;}
.acrm-content{flex:1;overflow:hidden;display:flex;position:relative;}
.acrm-pane{display:none;flex:1;overflow-y:auto;padding:3.2rem;scrollbar-width:thin;scrollbar-color:var(--border) transparent;}
.acrm-pane.active{display:flex;flex-direction:column;gap:2.4rem;}
.acrm-pane::-webkit-scrollbar{width:4px;}.acrm-pane::-webkit-scrollbar-thumb{background:var(--border);}

/* Pipeline */
.pipeline-header,.clients-header,.agenda-header,.rev-header{display:flex;align-items:center;justify-content:space-between;flex-shrink:0;}
.pipeline-title,.clients-title,.agenda-title,.rev-title,.sheets-title{font-family:var(--font-d);font-size:2.8rem;font-weight:300;font-style:italic;}
.pipeline-add-btn,.clients-add-btn,.sheets-sync-btn,.sheets-apply-btn{font-family:var(--font-m);font-size:.9rem;letter-spacing:.14em;text-transform:uppercase;background:var(--sage);color:var(--deep);border:none;padding:.9rem 2rem;cursor:none;transition:background .3s;}
.pipeline-add-btn:hover,.clients-add-btn:hover,.sheets-sync-btn:hover{background:var(--sage-light);}
.sheets-apply-btn{background:var(--terra);}.sheets-apply-btn:hover{background:var(--terra-light);}
.pipeline-board{display:grid;grid-template-columns:repeat(5,1fr);gap:1.6rem;flex:1;min-height:0;align-items:start;}
.pipeline-col{background:var(--mid);border:1px solid var(--border);min-height:200px;transition:border-color .3s;}
.pipeline-col.drag-over{border-color:var(--sage);background:var(--sage-dim);}
.pipeline-col-header{display:flex;align-items:center;gap:.8rem;padding:1.2rem 1.6rem;border-bottom:1px solid var(--border);font-family:var(--font-m);font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);}
.pcol-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0;}
.pcol-count{margin-left:auto;background:var(--surface);padding:.1rem .6rem;border-radius:8px;font-size:.75rem;}
.pipeline-cards{padding:1rem;display:flex;flex-direction:column;gap:.8rem;min-height:60px;}
.pipeline-card{background:var(--surface);border:1px solid var(--border);padding:1.4rem;cursor:grab;transition:box-shadow .3s,transform .2s,border-color .3s;position:relative;}
.pipeline-card:hover{box-shadow:var(--shadow-card);border-color:rgba(61,139,122,.3);transform:translateY(-2px);}
.pipeline-card.dragging{opacity:.6;transform:rotate(2deg) scale(.98);}
.pc-client{font-family:var(--font-d);font-size:1.4rem;font-style:italic;margin-bottom:.4rem;}
.pc-prop{font-family:var(--font-m);font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:.8rem;}
.pc-budget{font-family:var(--font-m);font-size:.85rem;color:var(--champ);}
.pc-date{font-family:var(--font-m);font-size:.7rem;color:var(--muted);margin-top:.6rem;}
.pc-delete{position:absolute;top:.6rem;right:.6rem;width:20px;height:20px;background:none;border:none;color:var(--muted);font-size:1rem;cursor:none;opacity:0;transition:opacity .2s,color .2s;display:flex;align-items:center;justify-content:center;}
.pipeline-card:hover .pc-delete{opacity:1;}.pc-delete:hover{color:var(--terra);}

/* Client folders */
.clients-search{flex:1;}
.crm-input{width:100%;background:var(--mid);border:1px solid var(--border);border-bottom:1px solid rgba(61,139,122,.4);color:var(--ivory);font-family:var(--font-b);font-size:1.3rem;font-weight:300;padding:.9rem 1.4rem;outline:none;transition:border-color .3s;cursor:none;}
.crm-input:focus{border-bottom-color:var(--sage);}
.crm-input--wide{max-width:600px;}
.clients-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:2rem;align-items:start;}
.client-folder{position:relative;cursor:none;perspective:1000px;height:240px;}
.client-folder__outer{position:absolute;inset:0;background:linear-gradient(145deg,#1e3040,#162535);border:1px solid var(--border);transform-style:preserve-3d;transition:transform .6s var(--ease-expo),box-shadow .4s;transform-origin:center bottom;}
.client-folder__tab{position:absolute;top:-14px;left:20px;width:70px;height:14px;background:linear-gradient(145deg,#253d50,#1e3142);border:1px solid var(--border);border-bottom:none;border-radius:3px 3px 0 0;}
.client-folder:hover .client-folder__outer{transform:rotateX(-12deg) translateY(-8px);box-shadow:0 30px 60px rgba(8,15,20,.5),0 0 20px rgba(61,139,122,.1);}
.client-folder__shine{position:absolute;inset:0;background:radial-gradient(circle at var(--shine-x,50%) var(--shine-y,50%),rgba(255,255,255,.06) 0%,transparent 60%);pointer-events:none;z-index:2;opacity:0;transition:opacity .3s;}
.client-folder:hover .client-folder__shine{opacity:1;}
.client-folder__content{position:relative;z-index:1;padding:2rem 1.8rem;height:100%;display:flex;flex-direction:column;gap:.6rem;}
.cf-avatar{width:48px;height:48px;background:var(--sage-dim);border:1px solid rgba(61,139,122,.2);display:flex;align-items:center;justify-content:center;font-family:var(--font-d);font-size:1.8rem;font-weight:300;color:var(--sage);margin-bottom:.4rem;}
.cf-name{font-family:var(--font-d);font-size:1.8rem;font-weight:300;font-style:italic;line-height:1.2;}
.cf-role{font-family:var(--font-m);font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);}
.cf-budget{font-family:var(--font-m);font-size:.9rem;color:var(--champ);margin-top:auto;}
.cf-status{display:inline-flex;align-items:center;gap:.5rem;font-family:var(--font-m);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;}
.cf-status-dot{width:5px;height:5px;border-radius:50%;}
.cf-last-contact{font-family:var(--font-m);font-size:.7rem;color:var(--muted);}
.client-folder.stale .client-folder__outer{border-color:rgba(212,164,90,.3);}
.client-detail{position:absolute;inset:0;background:var(--deep);z-index:10;overflow-y:auto;padding:2.4rem 3.2rem;}
.cd-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:3.2rem;}
.cd-back{background:none;border:none;color:var(--sage);font-family:var(--font-m);font-size:.9rem;letter-spacing:.14em;cursor:none;transition:letter-spacing .3s;}
.cd-back:hover{letter-spacing:.22em;}
.cd-actions{display:flex;gap:1.2rem;}
.cd-btn{font-family:var(--font-m);font-size:.85rem;letter-spacing:.14em;text-transform:uppercase;padding:.7rem 1.8rem;background:none;border:1px solid var(--border);color:var(--muted);cursor:none;transition:all .3s;}
.cd-btn:hover{border-color:var(--plat);color:var(--ivory);}
.cd-btn--present{background:var(--terra-dim);border-color:rgba(196,113,79,.3);color:var(--terra);}
.cd-btn--present:hover{background:var(--terra);color:var(--deep);}

/* Agenda */
.agenda-week-nav{display:flex;align-items:center;gap:1.6rem;}
.aw-btn{width:36px;height:36px;background:none;border:1px solid var(--border);color:var(--ivory);cursor:none;font-size:1.4rem;transition:border-color .3s;display:flex;align-items:center;justify-content:center;}
.aw-btn:hover{border-color:var(--sage);}
.aw-label{font-family:var(--font-m);font-size:.9rem;letter-spacing:.12em;color:var(--sand);}
.agenda-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:1.2rem;}
.agenda-day{background:var(--mid);border:1px solid var(--border);min-height:180px;}
.agenda-day.today{border-color:rgba(61,139,122,.4);background:var(--sage-dim);}
.agenda-day-header{padding:.8rem 1rem;border-bottom:1px solid var(--border);font-family:var(--font-m);font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;}
.agenda-day.today .agenda-day-header{color:var(--sage);}
.agenda-events{padding:.6rem;display:flex;flex-direction:column;gap:.4rem;}
.agenda-event{padding:.5rem .7rem;background:var(--sage-dim);border-left:2px solid var(--sage);font-family:var(--font-m);font-size:.7rem;letter-spacing:.06em;color:var(--sage-pale);cursor:none;transition:background .2s;}
.agenda-event:hover{background:rgba(61,139,122,.2);}
.agenda-event.type-visite{border-left-color:var(--terra);background:var(--terra-dim);color:var(--terra-pale);}
.agenda-upcoming{margin-top:2.4rem;}
.agenda-upcoming-title{font-family:var(--font-m);font-size:.85rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:1.2rem;}
.upcoming-item{display:grid;grid-template-columns:120px 1fr 1fr auto;align-items:center;padding:1.4rem 1.6rem;background:var(--mid);border:1px solid var(--border);margin-bottom:.8rem;transition:border-color .3s;}
.upcoming-item:hover{border-color:rgba(61,139,122,.3);}
.ui-time{font-family:var(--font-m);font-size:.85rem;color:var(--sage);letter-spacing:.1em;}
.ui-client{font-family:var(--font-d);font-size:1.4rem;font-style:italic;}
.ui-prop{font-family:var(--font-m);font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);}
.ui-status{font-family:var(--font-m);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;padding:.3rem .8rem;background:var(--sage-dim);color:var(--sage);}

/* Revenue */
.rev-period{display:flex;gap:0;}
.rev-period-btn{font-family:var(--font-m);font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;padding:.7rem 1.6rem;background:none;border:1px solid var(--border);color:var(--muted);cursor:none;margin-right:-1px;transition:all .3s;}
.rev-period-btn.active,.rev-period-btn:hover{background:var(--sage-dim);border-color:var(--sage);color:var(--sage);}
.rev-kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:1.6rem;}
.rev-kpi{padding:2rem;background:var(--mid);border:1px solid var(--border);position:relative;overflow:hidden;}
.rev-kpi::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:var(--sage);transform:scaleX(0);transform-origin:left;transition:transform .8s var(--ease-expo);}
.rev-kpi.loaded::after{transform:scaleX(1);}
.rev-kpi-v{font-family:var(--font-d);font-size:3.2rem;font-weight:300;color:var(--champ);display:block;margin-bottom:.6rem;line-height:1;}
.rev-kpi-l{font-family:var(--font-m);font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);}
.rev-kpi-delta{font-family:var(--font-m);font-size:.75rem;margin-top:.4rem;}
.rev-kpi-delta.up{color:var(--green);}.rev-kpi-delta.down{color:var(--terra);}
.rev-charts-row{display:grid;grid-template-columns:1fr 280px;gap:2.4rem;}
.rev-chart-title,.rev-goal-title{font-family:var(--font-m);font-size:.85rem;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);margin-bottom:1.6rem;}
.rev-chart-svg{width:100%;height:auto;display:block;}
.rev-goal-ring{position:relative;width:180px;margin:0 auto 2rem;}
.rev-donut{width:100%;height:auto;}
.rev-donut-center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.4rem;}
.rev-donut-center span:first-child{font-family:var(--font-d);font-size:3.2rem;font-weight:300;color:var(--sage);line-height:1;}
.rev-donut-center span:last-child{font-family:var(--font-m);font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);}
.rev-goal-detail{font-family:var(--font-m);font-size:.85rem;color:var(--sand);text-align:center;line-height:1.8;}
.rev-trans-title{font-family:var(--font-m);font-size:.85rem;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);margin-bottom:1.2rem;}
.rev-trans-item{display:grid;grid-template-columns:1fr auto auto;align-items:center;padding:1.4rem 1.6rem;background:var(--mid);border:1px solid var(--border);margin-bottom:.8rem;gap:2rem;}
.rti-prop{font-family:var(--font-d);font-size:1.4rem;font-style:italic;}
.rti-client{font-family:var(--font-m);font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);}
.rti-amount{font-family:var(--font-m);font-size:1rem;color:var(--champ);letter-spacing:.1em;}
.rti-date{font-family:var(--font-m);font-size:.75rem;color:var(--muted);}

/* Sheets */
.sheets-desc{font-size:1.4rem;color:var(--sand);line-height:1.8;max-width:600px;}
.sheets-input-row{display:flex;gap:1.2rem;margin-bottom:2.4rem;}.sheets-input-row .crm-input--wide{flex:1;}
.sfh-title{font-family:var(--font-m);font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-bottom:1rem;}
.sfh-cols{display:flex;flex-wrap:wrap;gap:.8rem;}
.sfh-cols span{font-family:var(--font-m);font-size:.75rem;letter-spacing:.1em;padding:.3rem .9rem;background:var(--mid);border:1px solid var(--border);color:var(--sand);}
.sheets-status{padding:1.6rem 2rem;border:1px solid var(--border);font-family:var(--font-m);font-size:.9rem;letter-spacing:.1em;}
.sheets-status.success{border-color:rgba(61,139,122,.3);color:var(--green);background:var(--sage-dim);}
.sheets-status.error{border-color:rgba(196,113,79,.3);color:var(--terra);background:var(--terra-dim);}
.sheets-preview-title{font-family:var(--font-m);font-size:.85rem;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);margin-bottom:1.6rem;}
.sheets-preview-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:1.2rem;margin-bottom:2.4rem;}
.sheet-preview-card{background:var(--mid);border:1px solid var(--border);padding:1.4rem;}
.spc-name{font-family:var(--font-d);font-size:1.4rem;font-style:italic;margin-bottom:.4rem;}
.spc-city{font-family:var(--font-m);font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:.8rem;}
.spc-price{font-family:var(--font-m);font-size:.9rem;color:var(--champ);}

/* Activity feed */
.acrm-activity{width:280px;border-left:1px solid var(--border);background:var(--void);display:flex;flex-direction:column;flex-shrink:0;}
.activity-header{display:flex;align-items:center;justify-content:space-between;padding:1.4rem 1.6rem;border-bottom:1px solid var(--border);}
.activity-title{font-family:var(--font-m);font-size:.8rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);}
.activity-clear{background:none;border:none;color:var(--muted);font-family:var(--font-m);font-size:.7rem;letter-spacing:.1em;cursor:none;transition:color .2s;}.activity-clear:hover{color:var(--terra);}
.activity-feed{flex:1;overflow-y:auto;padding:1rem;display:flex;flex-direction:column;gap:.6rem;}.activity-feed::-webkit-scrollbar{width:2px;}
.activity-item{padding:.9rem 1rem;background:var(--mid);border-left:2px solid var(--sage);animation:feed-in .3s var(--ease-out);}
@keyframes feed-in{from{opacity:0;transform:translateX(12px);}to{opacity:1;transform:translateX(0);}}
.ai-text{font-family:var(--font-m);font-size:.72rem;letter-spacing:.06em;color:var(--cream);line-height:1.5;}
.ai-time{font-family:var(--font-m);font-size:.65rem;color:var(--muted);margin-top:.3rem;}
.activity-item.type-alert{border-left-color:var(--amber);}
.activity-item.type-booking{border-left-color:var(--green);}
.activity-item.type-warning{border-left-color:var(--terra);}

/* Modal */
.crm-modal{position:fixed;inset:0;z-index:9700;display:flex;align-items:center;justify-content:center;background:rgba(8,15,20,.8);backdrop-filter:blur(12px);}
.crm-modal-inner{background:var(--surface);border:1px solid var(--border);padding:4rem;width:min(560px,95vw);box-shadow:var(--shadow-lift);}
.crm-modal-title{font-family:var(--font-d);font-size:2.8rem;font-weight:300;font-style:italic;margin-bottom:3.2rem;}
.crm-form{display:flex;flex-direction:column;gap:1.6rem;}
.crm-form-row{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;}
.crm-field label{display:block;font-family:var(--font-m);font-size:.75rem;letter-spacing:.15em;text-transform:uppercase;color:var(--sage);margin-bottom:.6rem;}
.crm-select{width:100%;background:var(--mid);border:1px solid var(--border);border-bottom:1px solid rgba(61,139,122,.4);color:var(--ivory);font-family:var(--font-b);font-size:1.3rem;font-weight:300;padding:.9rem 1.4rem;outline:none;appearance:none;cursor:none;}
.crm-form-actions{display:flex;gap:1.2rem;justify-content:flex-end;margin-top:.8rem;}
.crm-btn-cancel{background:none;border:1px solid var(--border);color:var(--muted);font-family:var(--font-m);font-size:.9rem;letter-spacing:.14em;text-transform:uppercase;padding:.9rem 2rem;cursor:none;transition:all .3s;}
.crm-btn-cancel:hover{border-color:var(--terra);color:var(--terra);}
.crm-btn-save{background:var(--sage);color:var(--deep);border:none;font-family:var(--font-m);font-size:.9rem;letter-spacing:.14em;text-transform:uppercase;padding:.9rem 2.8rem;cursor:none;transition:background .3s;}
.crm-btn-save:hover{background:var(--sage-light);}

/* Presentation mode */
.present-mode{position:fixed;inset:0;z-index:9800;background:var(--void);}
.pm-bg{position:absolute;inset:0;}.pm-bg img{width:100%;height:100%;object-fit:cover;filter:brightness(.4) saturate(.8);}
.pm-overlay{position:absolute;inset:0;background:linear-gradient(to right,rgba(8,15,20,.95) 0%,rgba(8,15,20,.3) 60%,rgba(8,15,20,.6) 100%);}
.pm-content{position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;padding:0 10rem;max-width:800px;}
.pm-controls{position:absolute;bottom:4rem;left:50%;transform:translateX(-50%);z-index:3;display:flex;align-items:center;gap:2rem;}
.pm-btn{width:52px;height:52px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.2);color:var(--ivory);font-size:2rem;cursor:none;display:flex;align-items:center;justify-content:center;transition:all .3s;backdrop-filter:blur(8px);}
.pm-btn:hover{border-color:var(--sage);color:var(--sage);}
.pm-counter{font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;color:rgba(245,242,237,.5);}
.pm-close-btn{font-family:var(--font-m);font-size:.85rem;letter-spacing:.15em;text-transform:uppercase;background:none;border:1px solid rgba(255,255,255,.2);color:rgba(245,242,237,.5);padding:.7rem 1.8rem;cursor:none;transition:all .3s;}
.pm-close-btn:hover{border-color:var(--terra);color:var(--terra);}

/* Liquid glass */
.glass-card{position:relative;background:rgba(23,40,56,0.6);backdrop-filter:blur(20px) saturate(180%);-webkit-backdrop-filter:blur(20px) saturate(180%);border:1px solid rgba(245,242,237,.08);overflow:hidden;}
.glass-card::before{content:'';position:absolute;top:0;left:-100%;width:60%;height:100%;background:linear-gradient(105deg,transparent 40%,rgba(245,242,237,.04) 50%,rgba(245,242,237,.02) 55%,transparent 65%);transition:left .6s var(--ease-out);pointer-events:none;z-index:3;}
.glass-card:hover::before{left:150%;}

/* Skyline */
.skyline-wrap{position:relative;overflow:hidden;height:180px;background:linear-gradient(to bottom,var(--void),var(--mid));}
.skyline-svg{position:absolute;bottom:0;}

/* Prop expand */
.prop-expand-overlay{position:fixed;inset:0;z-index:7000;display:none;overflow-y:auto;background:var(--deep);}
.prop-expand-overlay.open{display:block;}
.prop-expand-close{position:fixed;top:3rem;right:3rem;z-index:7001;width:48px;height:48px;background:rgba(8,15,20,.8);border:1px solid var(--border);color:var(--ivory);font-size:1.6rem;cursor:none;display:flex;align-items:center;justify-content:center;backdrop-filter:blur(8px);transition:border-color .3s;}
.prop-expand-close:hover{border-color:var(--terra);}
"""

style_end = tpl.index('</style>')
css_escaped = esc(NEW_CSS)
tpl = tpl[:style_end] + css_escaped + tpl[style_end:]
print(f"Step 2: CSS injected. Size: {len(tpl)}")

# ============================================================
# 3. ADD CRM HTML before </body>
# ============================================================
CRM_HTML = (
    '<!-- AGENT CRM -->'
    '<div class="agent-crm" id="agent-crm">'
    '<div class="acrm-backdrop" id="acrm-backdrop"></div>'
    '<div class="acrm-panel" id="acrm-panel">'
    '<div class="acrm-header"><div class="acrm-header-left"><div class="acrm-logo"><svg width="20" height="20" viewBox="0 0 32 32"><polygon points="16,2 30,28 2,28" fill="none" stroke="var(--sage)" stroke-width="1.5"/></svg><span>NOVUS</span><span class="acrm-logo-sub">Agent CRM</span></div><div class="acrm-greeting" id="acrm-greeting">Dashboard</div></div><div class="acrm-header-right"><div class="acrm-live-badge"><span class="acrm-live-dot"></span>Live</div><div class="acrm-time" id="acrm-time">--:--</div><button class="acrm-close" id="acrm-close"><span>✕</span></button></div></div>'
    '<div class="acrm-tabs">'
    '<button class="acrm-tab active" data-tab="pipeline"><span class="acrm-tab-icon">⬡</span>Pipeline<span class="acrm-tab-badge" id="badge-pipeline">0</span></button>'
    '<button class="acrm-tab" data-tab="clients"><span class="acrm-tab-icon">◈</span>Clients<span class="acrm-tab-badge" id="badge-clients">0</span></button>'
    '<button class="acrm-tab" data-tab="agenda"><span class="acrm-tab-icon">◷</span>Agenda<span class="acrm-tab-badge" id="badge-agenda">0</span></button>'
    '<button class="acrm-tab" data-tab="revenue"><span class="acrm-tab-icon">◈</span>Revenue</button>'
    '<button class="acrm-tab" data-tab="sheets"><span class="acrm-tab-icon">⬡</span>Sheets</button>'
    '</div>'
    '<div class="acrm-content" id="acrm-content">'
    # Pipeline pane
    '<div class="acrm-pane active" id="pane-pipeline"><div class="pipeline-header"><h2 class="pipeline-title">Sales Pipeline</h2><button class="pipeline-add-btn" id="pipeline-add">+ New Lead</button></div><div class="pipeline-board" id="pipeline-board">'
    '<div class="pipeline-col" data-stage="prospect"><div class="pipeline-col-header"><span class="pcol-dot" style="background:var(--plat)"></span>Prospect<span class="pcol-count" id="cnt-prospect">0</span></div><div class="pipeline-cards" id="stage-prospect"></div></div>'
    '<div class="pipeline-col" data-stage="visite"><div class="pipeline-col-header"><span class="pcol-dot" style="background:var(--sage)"></span>Visite<span class="pcol-count" id="cnt-visite">0</span></div><div class="pipeline-cards" id="stage-visite"></div></div>'
    '<div class="pipeline-col" data-stage="offre"><div class="pipeline-col-header"><span class="pcol-dot" style="background:var(--champ)"></span>Offre<span class="pcol-count" id="cnt-offre">0</span></div><div class="pipeline-cards" id="stage-offre"></div></div>'
    '<div class="pipeline-col" data-stage="signe"><div class="pipeline-col-header"><span class="pcol-dot" style="background:var(--terra)"></span>Signe<span class="pcol-count" id="cnt-signe">0</span></div><div class="pipeline-cards" id="stage-signe"></div></div>'
    '<div class="pipeline-col" data-stage="loue"><div class="pipeline-col-header"><span class="pcol-dot" style="background:var(--green)"></span>Loue<span class="pcol-count" id="cnt-loue">0</span></div><div class="pipeline-cards" id="stage-loue"></div></div>'
    '</div></div>'
    # Clients pane
    '<div class="acrm-pane" id="pane-clients"><div class="clients-header"><h2 class="clients-title">Clients</h2><div class="clients-search"><input type="text" placeholder="Search..." id="client-search" class="crm-input"></div><button class="clients-add-btn" id="client-add">+ New Client</button></div><div class="clients-grid" id="clients-grid"></div><div class="client-detail" id="client-detail" style="display:none"><div class="cd-header"><button class="cd-back" id="cd-back">← Back</button><div class="cd-actions"><button class="cd-btn" id="cd-pdf">PDF</button><button class="cd-btn cd-btn--present" id="cd-present">Present</button></div></div><div class="cd-body" id="cd-body"></div></div></div>'
    # Agenda pane
    '<div class="acrm-pane" id="pane-agenda"><div class="agenda-header"><h2 class="agenda-title">This Week</h2><div class="agenda-week-nav"><button class="aw-btn" id="agenda-prev">‹</button><span class="aw-label" id="agenda-week-label">—</span><button class="aw-btn" id="agenda-next">›</button></div></div><div class="agenda-grid" id="agenda-grid"></div><div class="agenda-upcoming" id="agenda-upcoming"><div class="agenda-upcoming-title">Upcoming Viewings</div><div class="agenda-upcoming-list" id="upcoming-list"></div></div></div>'
    # Revenue pane
    '<div class="acrm-pane" id="pane-revenue"><div class="rev-header"><h2 class="rev-title">Revenue</h2><div class="rev-period"><button class="rev-period-btn active" data-period="month">Month</button><button class="rev-period-btn" data-period="quarter">Quarter</button><button class="rev-period-btn" data-period="year">Year</button></div></div><div class="rev-kpis" id="rev-kpis"></div><div class="rev-charts-row"><div class="rev-chart-wrap"><div class="rev-chart-title">Commission Pipeline</div><svg id="rev-chart-svg" viewBox="0 0 800 260" class="rev-chart-svg"></svg></div><div class="rev-goal-wrap"><div class="rev-goal-title">Monthly Goal</div><div class="rev-goal-ring" id="rev-goal-ring"><svg viewBox="0 0 200 200" class="rev-donut"><circle cx="100" cy="100" r="80" fill="none" stroke="rgba(61,139,122,.1)" stroke-width="16"/><circle id="rev-donut-fill" cx="100" cy="100" r="80" fill="none" stroke="var(--sage)" stroke-width="16" stroke-dasharray="502.4" stroke-dashoffset="502.4" transform="rotate(-90 100 100)" stroke-linecap="round"/></svg><div class="rev-donut-center"><span id="rev-goal-pct">0%</span><span>of target</span></div></div><div class="rev-goal-detail" id="rev-goal-detail"></div></div></div><div class="rev-transactions" id="rev-transactions"><div class="rev-trans-title">Recent Transactions</div><div class="rev-trans-list" id="rev-trans-list"></div></div></div>'
    # Sheets pane
    '<div class="acrm-pane" id="pane-sheets"><div class="sheets-header"><h2 class="sheets-title">Sheets Bridge</h2><p class="sheets-desc">Paste your Google Sheet CSV URL to sync properties.</p></div><div class="sheets-connect" id="sheets-connect"><div class="sheets-input-row"><input type="url" class="crm-input crm-input--wide" id="sheets-url" placeholder="https://docs.google.com/spreadsheets/..."><button class="sheets-sync-btn" id="sheets-sync-btn"><span id="sheets-sync-label">Sync Now</span></button></div><div class="sheets-format-hint"><div class="sfh-title">Required columns:</div><div class="sfh-cols"><span>name</span><span>city</span><span>type</span><span>price</span><span>size</span><span>beds</span><span>baths</span><span>status</span></div></div><div class="sheets-status" id="sheets-status" style="display:none"></div></div><div class="sheets-preview" id="sheets-preview" style="display:none"><div class="sheets-preview-title" id="sheets-preview-title">—</div><div class="sheets-preview-grid" id="sheets-preview-grid"></div><button class="sheets-apply-btn" id="sheets-apply">Apply →</button></div></div>'
    '</div>'
    # Activity feed
    '<div class="acrm-activity" id="acrm-activity"><div class="activity-header"><span class="activity-title">Live Activity</span><button class="activity-clear" id="activity-clear">Clear</button></div><div class="activity-feed" id="activity-feed"></div></div>'
    '</div></div>'
    # Modal
    '<div class="crm-modal" id="crm-modal" style="display:none"><div class="crm-modal-inner" id="crm-modal-inner"></div></div>'
    # Present mode
    '<div class="present-mode" id="present-mode" style="display:none"><div class="pm-bg" id="pm-bg"></div><div class="pm-overlay"></div><div class="pm-content" id="pm-content"></div><div class="pm-controls"><button class="pm-btn" id="pm-prev-slide">‹</button><span class="pm-counter" id="pm-counter">1/1</span><button class="pm-btn" id="pm-next-slide">›</button><button class="pm-close-btn" id="pm-close">Exit</button></div></div>'
)

body_end = tpl.index('</body>')
html_esc = esc(CRM_HTML)
tpl = tpl[:body_end] + html_esc + tpl[body_end:]
print(f"Step 3: CRM HTML injected. Size: {len(tpl)}")

# ============================================================
# 4. ADD ALL JS before last script close
# ============================================================

# The JS is very large - write it to a separate file and read it
js_file = r"C:\vantage-clean\crm-v2-push\_crm_js_temp.js"

JS_CODE = """
/* ═══════════════════════════════════════════════
   AGENT CRM — COMPLETE JS
═══════════════════════════════════════════════ */
var CRM_KEY='novus_crm_v2';
function getCRM(){try{return JSON.parse(localStorage.getItem(CRM_KEY))||getDefaultCRM();}catch(e){return getDefaultCRM();}}
function saveCRM(data){localStorage.setItem(CRM_KEY,JSON.stringify(data));}
function getDefaultCRM(){return{clients:[{id:'c1',name:'Jean-Pierre Moreau',role:'Managing Partner',company:'Moreau Capital',budget:'15K-25K/mo',city:'Paris',type:'Penthouse',status:'active',lastContact:Date.now()-172800000,notes:'Interested in Tour Lumiere.',favorites:['Tour Lumiere'],viewings:[{prop:'Tour Lumiere',date:'2025-04-12',feedback:'Very positive'}]},{id:'c2',name:'Sarah Mitchell',role:'Director',company:'Atlas Fund',budget:'8K-12K/mo',city:'London',type:'Office',status:'active',lastContact:Date.now()-691200000,notes:'Looking for commercial space.',favorites:['The Meridian'],viewings:[]},{id:'c3',name:'Stavros P.',role:'Family Office',company:'Independent',budget:'10K-20K/mo',city:'Athens',type:'Villa',status:'negotiation',lastContact:Date.now()-86400000,notes:'Villa Aurelia in discussion.',favorites:['Villa Aurelia'],viewings:[{prop:'Villa Aurelia',date:'2025-04-10',feedback:'Offer pending'}]}],leads:[{id:'l1',name:'Alice Fontaine',prop:'Tour Lumiere',budget:'18,000',stage:'prospect',date:'2025-04-15'},{id:'l2',name:'Marco Ricci',prop:'Villa Aurelia',budget:'12,500',stage:'visite',date:'2025-04-12'},{id:'l3',name:'Emma Clarke',prop:'The Meridian',budget:'22,000',stage:'offre',date:'2025-04-08'},{id:'l4',name:'Youssef Benali',prop:'Loft Lumino',budget:'9,800',stage:'signe',date:'2025-04-01'},{id:'l5',name:'Anna Schmidt',prop:'Tour Lumiere',budget:'18,500',stage:'loue',date:'2025-03-28'}],bookings:JSON.parse(localStorage.getItem('novus_bookings')||'[]'),revenue:{target:45000,current:31200,transactions:[{prop:'Tour Lumiere',client:'Anna Schmidt',amount:3700,date:'2025-03-28'},{prop:'Villa Aurelia',client:'S. Papadimitriou',amount:2500,date:'2025-04-05'},{prop:'The Meridian',client:'Emma Clarke',amount:4400,date:'2025-04-08'}]},activity:[]};}

var crmOpen=false;
function openAgentDashboard(){var crm=document.getElementById('agent-crm');crm.classList.add('open');crmOpen=true;document.body.style.overflow='hidden';updateCRMTime();renderAllPanes();addActivity('Dashboard opened','info');var h=new Date().getHours();var greet=h<12?'Good morning':h<17?'Good afternoon':'Good evening';var g=document.getElementById('acrm-greeting');if(g)g.textContent=greet+' — Dashboard';}
function closeAgentDashboard(){var crm=document.getElementById('agent-crm');gsap.to(document.getElementById('acrm-panel'),{x:'100%',duration:.5,ease:'power3.in',onComplete:function(){crm.classList.remove('open');document.getElementById('acrm-panel').style.transform='';document.body.style.overflow='';crmOpen=false;}});gsap.to(document.getElementById('acrm-backdrop'),{opacity:0,duration:.4});}
document.getElementById('nav-agent-btn')&&document.getElementById('nav-agent-btn').addEventListener('click',function(){openAgentDashboard();});
document.getElementById('acrm-close')&&document.getElementById('acrm-close').addEventListener('click',closeAgentDashboard);
document.getElementById('acrm-backdrop')&&document.getElementById('acrm-backdrop').addEventListener('click',closeAgentDashboard);

document.querySelectorAll('.acrm-tab').forEach(function(tab){tab.addEventListener('click',function(){document.querySelectorAll('.acrm-tab').forEach(function(t){t.classList.remove('active');});document.querySelectorAll('.acrm-pane').forEach(function(p){p.classList.remove('active');});tab.classList.add('active');var pane=document.getElementById('pane-'+tab.dataset.tab);if(pane)pane.classList.add('active');});});

function updateCRMTime(){var now=new Date();var el=document.getElementById('acrm-time');if(el)el.textContent=now.toLocaleTimeString('fr-FR',{hour:'2-digit',minute:'2-digit',second:'2-digit'});}
setInterval(function(){if(crmOpen)updateCRMTime();},1000);

function addActivity(text,type){var feed=document.getElementById('activity-feed');if(!feed)return;var item=document.createElement('div');item.className='activity-item type-'+(type||'info');var now=new Date();item.innerHTML='<div class="ai-text">'+text+'</div><div class="ai-time">'+now.toLocaleTimeString('fr-FR',{hour:'2-digit',minute:'2-digit'})+'</div>';feed.insertBefore(item,feed.firstChild);while(feed.children.length>20)feed.lastChild.remove();}
document.getElementById('activity-clear')&&document.getElementById('activity-clear').addEventListener('click',function(){var feed=document.getElementById('activity-feed');if(feed){feed.innerHTML='';addActivity('Feed cleared','info');}});

function renderPipeline(){var data=getCRM();var stages=['prospect','visite','offre','signe','loue'];stages.forEach(function(stage){var container=document.getElementById('stage-'+stage);var countEl=document.getElementById('cnt-'+stage);if(!container)return;var leads=data.leads.filter(function(l){return l.stage===stage;});container.innerHTML='';if(countEl)countEl.textContent=leads.length;leads.forEach(function(lead){var card=document.createElement('div');card.className='pipeline-card';card.draggable=true;card.dataset.leadId=lead.id;card.innerHTML='<div class="pc-client">'+lead.name+'</div><div class="pc-prop">'+lead.prop+'</div><div class="pc-budget">'+lead.budget+'</div><div class="pc-date">'+lead.date+'</div><button class="pc-delete" data-id="'+lead.id+'">✕</button>';card.addEventListener('dragstart',function(e){card.classList.add('dragging');e.dataTransfer.setData('text/plain',lead.id);});card.addEventListener('dragend',function(){card.classList.remove('dragging');});card.querySelector('.pc-delete').addEventListener('click',function(e){e.stopPropagation();var crm=getCRM();crm.leads=crm.leads.filter(function(l){return l.id!==lead.id;});saveCRM(crm);addActivity('Lead removed: '+lead.name,'warning');renderPipeline();});container.appendChild(card);});});var bp=document.getElementById('badge-pipeline');if(bp)bp.textContent=data.leads.length;document.querySelectorAll('.pipeline-col').forEach(function(col){col.addEventListener('dragover',function(e){e.preventDefault();col.classList.add('drag-over');});col.addEventListener('dragleave',function(){col.classList.remove('drag-over');});col.addEventListener('drop',function(e){e.preventDefault();col.classList.remove('drag-over');var leadId=e.dataTransfer.getData('text/plain');var newStage=col.dataset.stage;var crm=getCRM();var lead=crm.leads.find(function(l){return l.id===leadId;});if(lead){lead.stage=newStage;saveCRM(crm);addActivity(lead.name+' moved to '+newStage,'booking');renderPipeline();}});});}

document.getElementById('pipeline-add')&&document.getElementById('pipeline-add').addEventListener('click',function(){openModal({title:'New Lead',fields:[{name:'name',label:'Client Name',type:'text'},{name:'prop',label:'Property',type:'text'},{name:'budget',label:'Budget',type:'text'},{name:'stage',label:'Stage',type:'select',options:['prospect','visite','offre','signe','loue']}],onSave:function(d){var crm=getCRM();crm.leads.push({id:'l'+Date.now(),name:d.name,prop:d.prop,budget:d.budget,stage:d.stage||'prospect',date:new Date().toISOString().split('T')[0]});saveCRM(crm);addActivity('New lead: '+d.name,'booking');renderPipeline();}});});

function renderClients(filter){var data=getCRM();var grid=document.getElementById('clients-grid');if(!grid)return;filter=filter||'';var clients=data.clients.filter(function(c){return c.name.toLowerCase().indexOf(filter.toLowerCase())>-1||(c.company||'').toLowerCase().indexOf(filter.toLowerCase())>-1;});grid.innerHTML='';var bc=document.getElementById('badge-clients');if(bc)bc.textContent=data.clients.length;clients.forEach(function(client){var days=Math.floor((Date.now()-client.lastContact)/86400000);var isStale=days>7;var folder=document.createElement('div');folder.className='client-folder'+(isStale?' stale':'');var initials=client.name.split(' ').map(function(w){return w[0];}).join('').slice(0,2);var statusColors={active:'var(--green)',negotiation:'var(--amber)',closed:'var(--muted)'};var dotColor=statusColors[client.status]||'var(--muted)';folder.innerHTML='<div class="client-folder__tab"></div><div class="client-folder__outer"><div class="client-folder__shine"></div><div class="client-folder__content"><div class="cf-avatar">'+initials+'</div><div class="cf-name">'+client.name+'</div><div class="cf-role">'+(client.role||'')+'</div><div class="cf-budget">'+client.budget+'</div><div class="cf-status"><span class="cf-status-dot" style="background:'+dotColor+'"></span>'+client.status+'</div><div class="cf-last-contact">'+(days===0?'Today':days+' days ago')+(isStale?' ⚠':'')+'</div></div></div>';folder.addEventListener('mousemove',function(e){var r=folder.getBoundingClientRect();var x=((e.clientX-r.left)/r.width)*100;var y=((e.clientY-r.top)/r.height)*100;var rx=(e.clientY-r.top-r.height/2)/r.height*-16;var ry=(e.clientX-r.left-r.width/2)/r.width*16;var outer=folder.querySelector('.client-folder__outer');var shine=folder.querySelector('.client-folder__shine');gsap.to(outer,{rotateX:rx,rotateY:ry,duration:.4,ease:'power2.out',transformPerspective:800});shine.style.setProperty('--shine-x',x+'%');shine.style.setProperty('--shine-y',y+'%');});folder.addEventListener('mouseleave',function(){gsap.to(folder.querySelector('.client-folder__outer'),{rotateX:0,rotateY:0,duration:.7,ease:'elastic.out(1,.6)'});});folder.addEventListener('click',function(){openClientDetail(client.id);});grid.appendChild(folder);});}
document.getElementById('client-search')&&document.getElementById('client-search').addEventListener('input',function(e){renderClients(e.target.value);});
function openClientDetail(clientId){var data=getCRM();var client=data.clients.find(function(c){return c.id===clientId;});if(!client)return;var detail=document.getElementById('client-detail');var body=document.getElementById('cd-body');if(!detail||!body)return;var initials=client.name.split(' ').map(function(w){return w[0];}).join('').slice(0,2);body.innerHTML='<div style="display:flex;gap:2.4rem;align-items:center;margin-bottom:3.2rem"><div class="cf-avatar" style="width:64px;height:64px;font-size:2.4rem">'+initials+'</div><div><h2 style="font-family:var(--font-d);font-size:3.2rem;font-weight:300;font-style:italic">'+client.name+'</h2><div style="font-family:var(--font-m);font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)">'+(client.role||'')+' '+(client.company?'— '+client.company:'')+'</div></div></div><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.6rem;margin-bottom:3.2rem"><div style="padding:1.6rem;background:var(--mid);border:1px solid var(--border)"><div style="font-family:var(--font-m);font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--sage);margin-bottom:.6rem">Budget</div><div style="font-family:var(--font-d);font-size:2rem;font-weight:300;color:var(--champ)">'+client.budget+'</div></div><div style="padding:1.6rem;background:var(--mid);border:1px solid var(--border)"><div style="font-family:var(--font-m);font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--sage);margin-bottom:.6rem">Type</div><div style="font-family:var(--font-d);font-size:2rem;font-weight:300">'+(client.type||'—')+'</div></div><div style="padding:1.6rem;background:var(--mid);border:1px solid var(--border)"><div style="font-family:var(--font-m);font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--sage);margin-bottom:.6rem">Status</div><div style="font-family:var(--font-d);font-size:2rem;font-weight:300">'+client.status+'</div></div></div><div style="margin-bottom:2.4rem"><div style="font-family:var(--font-m);font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--sage);margin-bottom:.8rem">Notes</div><div style="font-family:var(--font-b);font-size:1.3rem;color:var(--sand);line-height:1.8;padding:1.6rem;background:var(--mid);border:1px solid var(--border)">'+(client.notes||'No notes.')+'</div></div>';detail.style.display='block';gsap.from(detail,{opacity:0,x:40,duration:.4,ease:'power3.out'});addActivity('Opened: '+client.name,'info');}
document.getElementById('cd-back')&&document.getElementById('cd-back').addEventListener('click',function(){document.getElementById('client-detail').style.display='none';});
document.getElementById('client-add')&&document.getElementById('client-add').addEventListener('click',function(){openModal({title:'New Client',fields:[{name:'name',label:'Full Name',type:'text'},{name:'role',label:'Role',type:'text'},{name:'company',label:'Company',type:'text'},{name:'budget',label:'Budget',type:'text'},{name:'city',label:'City',type:'text'},{name:'type',label:'Type',type:'select',options:['Penthouse','Villa','Apartment','Office','Any']}],onSave:function(d){var crm=getCRM();crm.clients.push({id:'c'+Date.now(),name:d.name,role:d.role,company:d.company,budget:d.budget,city:d.city,type:d.type,status:'active',lastContact:Date.now(),notes:'',favorites:[],viewings:[]});saveCRM(crm);addActivity('New client: '+d.name,'booking');renderClients();}});});

var agendaOffset=0;
function renderAgenda(){var grid=document.getElementById('agenda-grid');var label=document.getElementById('agenda-week-label');var upcoming=document.getElementById('upcoming-list');if(!grid)return;var data=getCRM();var today=new Date();var start=new Date(today);start.setDate(today.getDate()-today.getDay()+1+agendaOffset*7);var days=['Mo','Tu','We','Th','Fr','Sa','Su'];var months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];var endDate=new Date(start);endDate.setDate(start.getDate()+6);if(label)label.textContent=start.getDate()+' '+months[start.getMonth()]+' — '+endDate.getDate()+' '+months[endDate.getMonth()];grid.innerHTML='';for(var d=0;d<7;d++){var date=new Date(start);date.setDate(start.getDate()+d);var isToday=date.toDateString()===today.toDateString();var dateStr=date.toISOString().split('T')[0];var bookings=data.bookings.filter(function(b){return b.date&&b.date.startsWith(dateStr);});var col=document.createElement('div');col.className='agenda-day'+(isToday?' today':'');col.innerHTML='<div class="agenda-day-header">'+days[d]+' '+date.getDate()+'</div><div class="agenda-events">'+bookings.map(function(b){return '<div class="agenda-event type-visite">'+(b.time||'—')+' · '+(b.prop||b.email||'—')+'</div>';}).join('')+'</div>';grid.appendChild(col);}var ba=document.getElementById('badge-agenda');if(ba)ba.textContent=data.bookings.length;if(upcoming){upcoming.innerHTML='';data.bookings.slice(-5).reverse().forEach(function(b){var d=b.date?new Date(b.date).toLocaleDateString('en-GB',{day:'numeric',month:'short'}):'—';upcoming.innerHTML+='<div class="upcoming-item"><span class="ui-time">'+d+' · '+(b.time||'')+'</span><span class="ui-client">'+(b.email||'—')+'</span><span class="ui-prop">'+(b.prop||'—')+'</span><span class="ui-status">Pending</span></div>';});}}
document.getElementById('agenda-prev')&&document.getElementById('agenda-prev').addEventListener('click',function(){agendaOffset--;renderAgenda();});
document.getElementById('agenda-next')&&document.getElementById('agenda-next').addEventListener('click',function(){agendaOffset++;renderAgenda();});

function renderRevenue(){var data=getCRM();var rev=data.revenue;var kpisData=[{v:'€'+rev.current.toLocaleString('fr-FR'),l:'Revenue MTD',delta:'+12%',up:true},{v:'€'+(rev.target-rev.current).toLocaleString('fr-FR'),l:'To Target'},{v:data.leads.filter(function(l){return l.stage==='loue';}).length,l:'Deals Closed'},{v:data.clients.length,l:'Active Clients'}];var kpisEl=document.getElementById('rev-kpis');if(kpisEl){kpisEl.innerHTML=kpisData.map(function(k){return '<div class="rev-kpi"><span class="rev-kpi-v">'+k.v+'</span><span class="rev-kpi-l">'+k.l+'</span>'+(k.delta?'<div class="rev-kpi-delta '+(k.up?'up':'')+'">▲ '+k.delta+'</div>':'')+'</div>';}).join('');setTimeout(function(){document.querySelectorAll('.rev-kpi').forEach(function(k){k.classList.add('loaded');});},200);}var pct=Math.min(rev.current/rev.target,1);var circ=2*Math.PI*80;var fill=document.getElementById('rev-donut-fill');var pctEl=document.getElementById('rev-goal-pct');if(fill)gsap.to(fill,{attr:{strokeDashoffset:circ*(1-pct)},duration:1.8,ease:'power3.out'});if(pctEl)gsap.to({v:0},{v:Math.round(pct*100),duration:1.8,ease:'power2.out',snap:{v:1},onUpdate:function(){pctEl.textContent=Math.floor(this.targets()[0].v)+'%';}});var goalDetail=document.getElementById('rev-goal-detail');if(goalDetail)goalDetail.innerHTML='<strong style="color:var(--champ)">€'+rev.current.toLocaleString('fr-FR')+'</strong> of <strong>€'+rev.target.toLocaleString('fr-FR')+'</strong>';var transList=document.getElementById('rev-trans-list');if(transList)transList.innerHTML=rev.transactions.map(function(t){return '<div class="rev-trans-item"><div><div class="rti-prop">'+t.prop+'</div><div class="rti-client">'+t.client+'</div></div><div class="rti-amount">€'+t.amount.toLocaleString('fr-FR')+'</div><div class="rti-date">'+t.date+'</div></div>';}).join('');}

function openModal(opts){var modal=document.getElementById('crm-modal');var inner=document.getElementById('crm-modal-inner');if(!modal||!inner)return;var fieldHTML=opts.fields.map(function(f){if(f.type==='select')return '<div class="crm-field"><label>'+f.label+'</label><select class="crm-select" name="'+f.name+'">'+f.options.map(function(o){return '<option value="'+o+'">'+o+'</option>';}).join('')+'</select></div>';return '<div class="crm-field"><label>'+f.label+'</label><input type="'+f.type+'" class="crm-input" name="'+f.name+'" placeholder="'+f.label+'"></div>';});var rows=[];for(var i=0;i<fieldHTML.length;i+=2){if(fieldHTML[i+1])rows.push('<div class="crm-form-row">'+fieldHTML[i]+fieldHTML[i+1]+'</div>');else rows.push(fieldHTML[i]);}inner.innerHTML='<h2 class="crm-modal-title">'+opts.title+'</h2><div class="crm-form" id="crm-form-dynamic">'+rows.join('')+'<div class="crm-form-actions"><button class="crm-btn-cancel" id="modal-cancel">Cancel</button><button class="crm-btn-save" id="modal-save">Save →</button></div></div>';modal.style.display='flex';gsap.from(inner,{opacity:0,scale:.96,y:20,duration:.4,ease:'back.out(2)'});document.getElementById('modal-cancel').addEventListener('click',function(){gsap.to(inner,{opacity:0,scale:.96,duration:.25,onComplete:function(){modal.style.display='none';}});});document.getElementById('modal-save').addEventListener('click',function(){var form=document.getElementById('crm-form-dynamic');var result={};form.querySelectorAll('[name]').forEach(function(el){result[el.name]=el.value;});opts.onSave(result);gsap.to(inner,{opacity:0,scale:.96,duration:.25,onComplete:function(){modal.style.display='none';}});});}

function renderAllPanes(){renderPipeline();renderClients();renderAgenda();renderRevenue();var data=getCRM();var stale=data.clients.filter(function(c){return Date.now()-c.lastContact>7*86400000;});if(stale.length)addActivity(stale.length+' client(s) need attention','alert');if(data.bookings.length)addActivity(data.bookings.length+' bookings in system','booking');addActivity('System initialized','info');if(stale.length>0){var sd=document.getElementById('agent-status-dot');if(sd)sd.classList.add('has-alerts');}}

/* VIS-05 — Particle explosion on hero click */
function initParticleExplosion(){var hero=document.getElementById('hero');if(!hero)return;hero.addEventListener('click',function(e){for(var i=0;i<24;i++){var p=document.createElement('div');p.style.cssText='position:fixed;left:'+e.clientX+'px;top:'+e.clientY+'px;width:'+(Math.random()*5+3)+'px;height:'+(Math.random()*5+3)+'px;border-radius:50%;background:'+(Math.random()>.5?'var(--sage)':'var(--terra)')+';pointer-events:none;z-index:9990;transform:translate(-50%,-50%);';document.body.appendChild(p);var angle=(i/24)*Math.PI*2;var speed=Math.random()*180+60;gsap.to(p,{x:Math.cos(angle)*speed,y:Math.sin(angle)*speed,scale:0,opacity:0,duration:.8+Math.random()*.6,ease:'power2.out',onComplete:function(){this.targets()[0].remove();}});}});}
initParticleExplosion();
"""

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(JS_CODE)

# Read and escape
with open(js_file, 'r', encoding='utf-8') as f:
    js_raw = f.read()

import os
os.remove(js_file)

# Find last x3c/script> before </body>
body_end = tpl.index('</body>')
last_script = tpl.rfind('x3c/script>', 0, body_end)
# Go back to find the start of this tag
insert_before = tpl.rfind('\\', 0, last_script)

js_escaped = esc(js_raw)
tpl = tpl[:insert_before] + js_escaped + tpl[insert_before:]
print(f"Step 4: JS injected. Size: {len(tpl)}")

# ============================================================
# VERIFY QUOTES
# ============================================================
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
        problems.append(f'pos {i}: ...{s[max(0,i-20):i+20]}...')
    i += 1

if problems:
    print(f"\nQUOTE PROBLEMS ({len(problems)}):")
    for p in problems[:30]:
        print(p)
    print("ABORTING!")
    import sys; sys.exit(1)

print(f"\nQuotes OK! Final size: {len(tpl)} chars")

content = content[:tpl_start] + tpl + content[tpl_end:]
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("V4 PATCH APPLIED!")
