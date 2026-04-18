#!/usr/bin/env python3
"""
Patch TPL_ECOM_HTML['5'] (NOVUS Capital) with 12 add-ons.
Inserts CSS before </style>, HTML sections at correct positions, JS before </body>.
"""

filepath = r"C:\vantage-clean\crm-v2-push\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract template boundaries
tpl_start = content.index("TPL_ECOM_HTML['5']")
tpl_end = content.index("TPL_ECOM_HTML['9']")
tpl = content[tpl_start:tpl_end]

# ============================================================
# ALL CSS TO ADD (before </style> in the template)
# ============================================================
ADDON_CSS = r"""
/* ============================================================
   A01 — BEFORE/AFTER SLIDER
============================================================ */
.ba-slider{position:absolute;inset:0;z-index:4;overflow:hidden;cursor:none;display:none;user-select:none;}
.ba-slider.active{display:block;}
.ba-after,.ba-before{position:absolute;inset:0;}
.ba-after img,.ba-before img{width:100%;height:100%;object-fit:cover;}
.ba-before{clip-path:inset(0 50% 0 0);transition:none;}
.ba-slider__label{position:absolute;top:2.4rem;z-index:3;font-family:var(--font-m);font-size:.85rem;letter-spacing:.18em;text-transform:uppercase;padding:.5rem 1.2rem;background:rgba(6,6,6,.65);backdrop-filter:blur(8px);}
.ba-slider__label--before{left:2.4rem;color:rgba(245,242,237,.6);}
.ba-slider__label--after{right:2.4rem;color:var(--gold);}
.ba-handle{position:absolute;top:0;bottom:0;left:50%;transform:translateX(-50%);z-index:5;display:flex;flex-direction:column;align-items:center;pointer-events:none;}
.ba-handle__line{width:1px;height:100%;background:var(--gold);box-shadow:0 0 12px rgba(184,149,63,.5);}
.ba-handle__circle{position:absolute;top:50%;transform:translateY(-50%);width:48px;height:48px;border-radius:50%;background:var(--gold);display:flex;align-items:center;justify-content:center;gap:.4rem;pointer-events:all;cursor:none;box-shadow:0 0 20px rgba(184,149,63,.4);}
.ba-handle__arrow{font-size:1.4rem;color:var(--void);line-height:1;font-weight:300;}
.ba-toggle{position:absolute;top:2.4rem;right:2.4rem;z-index:5;background:rgba(6,6,6,.75);backdrop-filter:blur(12px);border:1px solid rgba(184,149,63,.3);color:var(--gold);font-family:var(--font-m);font-size:.85rem;letter-spacing:.14em;text-transform:uppercase;padding:.8rem 1.6rem;display:flex;align-items:center;gap:.8rem;cursor:none;transition:background .3s,border-color .3s;}
.ba-toggle:hover{background:rgba(184,149,63,.15);border-color:var(--gold);}
.ba-toggle.active{background:var(--gold);color:var(--void);}
.ba-toggle__icon{font-size:1.2rem;}

/* ============================================================
   A02 — 3D CARD FLIP
============================================================ */
.flip-section{padding:13rem 5.6rem;background:var(--dark2);}
.flip-section__title{font-family:var(--font-d);font-size:clamp(3.6rem,4.5vw,6.4rem);font-weight:300;margin-bottom:6.4rem;letter-spacing:-.02em;opacity:0;transform:translateY(28px);}
.flip-section__title em{font-style:italic;color:var(--gold);}
.flip-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:3.2rem;}
.flip-card{height:520px;perspective:1200px;cursor:none;opacity:0;transform:translateY(48px);}
.flip-card__inner{width:100%;height:100%;transform-style:preserve-3d;transition:transform .85s cubic-bezier(0.76,0,0.24,1);position:relative;}
.flip-card:hover .flip-card__inner{transform:rotateY(180deg);}
.flip-card__front,.flip-card__back{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;overflow:hidden;}
.flip-card__front img{width:100%;height:100%;object-fit:cover;transition:transform .9s var(--ease-out);}
.flip-card:hover .flip-card__front img{transform:scale(1.04);}
.flip-card__front-overlay{position:absolute;inset:0;background:linear-gradient(to top,rgba(6,6,6,.85) 0%,transparent 55%);display:flex;flex-direction:column;justify-content:flex-end;padding:3.2rem;}
.flip-card__type{font-family:var(--font-m);font-size:.9rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);margin-bottom:.8rem;}
.flip-card__city{font-family:var(--font-d);font-size:2.8rem;font-weight:300;font-style:italic;margin-bottom:2rem;}
.flip-card__hint{font-family:var(--font-m);font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;color:rgba(245,242,237,.3);}
.flip-card__back{background:var(--dark3);border:1px solid rgba(245,242,237,.07);transform:rotateY(180deg);display:flex;align-items:stretch;}
.flip-card__back-content{padding:4rem;display:flex;flex-direction:column;gap:0;width:100%;}
.flip-card__back-tag{font-family:var(--font-m);font-size:.85rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gold);margin-bottom:2rem;padding-bottom:2rem;border-bottom:1px solid rgba(245,242,237,.08);}
.flip-card__back-name{font-family:var(--font-d);font-size:3.6rem;font-weight:300;font-style:italic;line-height:1;margin-bottom:.8rem;}
.flip-card__back-loc{font-family:var(--font-m);font-size:.9rem;letter-spacing:.12em;text-transform:uppercase;color:var(--silver);margin-bottom:2.4rem;}
.flip-card__back-price{font-family:var(--font-d);font-size:3.2rem;font-weight:300;color:var(--gold);margin-bottom:2rem;}
.flip-card__back-price span{font-size:1.6rem;color:var(--silver);}
.flip-card__back-specs{display:flex;gap:2rem;flex-wrap:wrap;margin-bottom:2rem;padding-bottom:2rem;border-bottom:1px solid rgba(245,242,237,.07);}
.flip-card__back-specs span{font-family:var(--font-m);font-size:.85rem;letter-spacing:.1em;text-transform:uppercase;color:var(--silver-light);}
.flip-card__back-desc{font-size:1.3rem;color:rgba(245,242,237,.45);line-height:1.8;margin-bottom:auto;flex:1;}
.flip-card__back-btn{display:inline-flex;align-items:center;gap:.8rem;margin-top:2.8rem;font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gold);border-bottom:1px solid rgba(184,149,63,.3);padding-bottom:.3rem;transition:letter-spacing .3s,border-color .3s;}
.flip-card__back-btn:hover{letter-spacing:.25em;border-color:var(--gold);}

/* ============================================================
   A03 — AMBIENT VIDEO HOVER
============================================================ */
.ambient-vid{position:absolute;inset:0;z-index:2;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .6s ease;pointer-events:none;}
.ambient-vid.playing{opacity:1;}

/* ============================================================
   A04 — CURSOR PREVIEW IMAGE
============================================================ */
.cursor-preview{position:fixed;top:0;left:0;z-index:5000;width:280px;pointer-events:none;opacity:0;transform:translate(-50%,-60%);will-change:transform;}
.cursor-preview__img-wrap{width:100%;height:188px;overflow:hidden;border:1px solid rgba(184,149,63,.2);}
.cursor-preview__img-wrap img{width:100%;height:100%;object-fit:cover;filter:saturate(.8);}
.cursor-preview__info{background:rgba(6,6,6,.85);backdrop-filter:blur(12px);padding:1.2rem 1.6rem;border:1px solid rgba(245,242,237,.06);border-top:none;display:flex;justify-content:space-between;align-items:center;}
.cursor-preview__name{font-family:var(--font-d);font-size:1.4rem;font-weight:300;font-style:italic;}
.cursor-preview__price{font-family:var(--font-m);font-size:.85rem;letter-spacing:.1em;color:var(--gold);}

/* ============================================================
   A05 — YIELD CALCULATOR
============================================================ */
.rent-calc{margin-top:3.2rem;border:1px solid rgba(184,149,63,.2);background:rgba(184,149,63,.03);}
.rent-calc__header{display:flex;align-items:center;gap:1.2rem;padding:1.8rem 2.4rem;cursor:none;}
.rent-calc__icon{font-size:1.4rem;}
.rent-calc__title{font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gold);flex:1;}
.rent-calc__toggle{background:none;border:1px solid rgba(184,149,63,.3);color:var(--gold);font-family:var(--font-m);font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;padding:.5rem 1.2rem;cursor:none;display:flex;align-items:center;gap:.6rem;transition:background .3s;}
.rent-calc__toggle:hover{background:rgba(184,149,63,.1);}
.rent-calc__toggle-icon{transition:transform .3s;}
.rent-calc.open .rent-calc__toggle-icon{transform:rotate(180deg);}
.rent-calc__body{padding:0 2.4rem 2.4rem;}
.rc-inputs{display:grid;grid-template-columns:1fr 1fr;gap:1.6rem;margin-bottom:2.4rem;}
.rc-label{display:block;font-family:var(--font-m);font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin-bottom:.8rem;}
.rc-input{width:100%;background:rgba(245,242,237,.04);border:1px solid rgba(245,242,237,.1);border-bottom:1px solid rgba(184,149,63,.4);color:var(--white);font-family:var(--font-d);font-size:1.8rem;font-weight:300;padding:1rem 1.4rem;outline:none;cursor:none;transition:border-color .3s;-moz-appearance:textfield;}
.rc-input::-webkit-outer-spin-button,.rc-input::-webkit-inner-spin-button{-webkit-appearance:none;}
.rc-input:focus{border-bottom-color:var(--gold-bright);}
.rc-results{display:grid;grid-template-columns:repeat(4,1fr);gap:1.2rem;margin-bottom:2.4rem;}
.rc-result-item{padding:1.6rem;background:rgba(245,242,237,.03);border:1px solid rgba(245,242,237,.07);text-align:center;}
.rc-result-item--highlight{background:rgba(184,149,63,.08);border-color:rgba(184,149,63,.2);}
.rc-result-label{display:block;font-family:var(--font-m);font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:var(--silver);margin-bottom:.8rem;}
.rc-result-value{display:block;font-family:var(--font-d);font-size:2.4rem;font-weight:300;color:var(--gold);}
.rc-result-item--highlight .rc-result-value{color:var(--gold-bright);}
.rc-chart-wrap{position:relative;}
.rc-chart{width:100%;height:auto;display:block;}
.rc-chart-labels{display:flex;justify-content:space-between;font-family:var(--font-m);font-size:.75rem;letter-spacing:.1em;color:rgba(245,242,237,.25);padding:.4rem 0;}

/* ============================================================
   A06 — PROPERTY COMPARATOR
============================================================ */
.compare-btn{background:none;border:1px dashed rgba(184,149,63,.3);color:rgba(184,149,63,.6);font-family:var(--font-m);font-size:.9rem;letter-spacing:.14em;text-transform:uppercase;padding:.8rem 2rem;cursor:none;margin-top:1.6rem;transition:all .3s;width:100%;}
.compare-btn:hover{border-color:var(--gold);color:var(--gold);background:rgba(184,149,63,.05);}
.compare-btn.selected{background:rgba(184,149,63,.12);border-style:solid;color:var(--gold);}
.compare-bar{position:fixed;bottom:-100px;left:5.6rem;right:5.6rem;z-index:500;background:var(--dark3);border:1px solid rgba(184,149,63,.2);padding:1.6rem 2.4rem;display:flex;align-items:center;gap:2.4rem;transition:bottom .5s var(--ease-out);backdrop-filter:blur(16px);}
.compare-bar.visible{bottom:3.2rem;}
.compare-bar__slots{display:flex;gap:1.6rem;flex:1;}
.compare-slot{display:flex;align-items:center;gap:1.2rem;padding:.8rem 1.4rem;background:rgba(245,242,237,.04);border:1px solid rgba(245,242,237,.08);min-width:200px;}
.compare-slot__name{font-family:var(--font-d);font-size:1.4rem;font-style:italic;flex:1;}
.compare-slot__remove{cursor:none;color:var(--silver);font-size:1.2rem;transition:color .2s;}
.compare-slot__remove:hover{color:var(--gold);}
.compare-bar__count{font-family:var(--font-m);font-size:.9rem;letter-spacing:.1em;color:var(--silver);}
.compare-bar__clear{background:none;border:1px solid rgba(245,242,237,.15);color:var(--silver);font-family:var(--font-m);font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;padding:.7rem 1.6rem;cursor:none;transition:all .3s;}
.compare-bar__clear:hover{border-color:var(--gold);color:var(--gold);}
.compare-bar__open{background:var(--gold);color:var(--void);border:none;font-family:var(--font-m);font-size:.9rem;letter-spacing:.15em;text-transform:uppercase;padding:.9rem 2.4rem;cursor:none;transition:background .3s;}
.compare-bar__open:hover:not(:disabled){background:var(--gold-bright);}
.compare-bar__open:disabled{opacity:.4;}
.compare-modal{position:fixed;inset:0;z-index:9000;background:rgba(6,6,6,.95);backdrop-filter:blur(24px);display:flex;align-items:stretch;justify-content:center;opacity:0;pointer-events:none;transition:opacity .4s;overflow-y:auto;}
.compare-modal.open{opacity:1;pointer-events:all;}
.compare-modal__inner{width:100%;max-width:1400px;padding:6rem 5.6rem;}
.compare-modal__header{display:flex;align-items:center;justify-content:space-between;margin-bottom:5.6rem;}
.compare-modal__title{font-family:var(--font-d);font-size:5.6rem;font-weight:300;line-height:1;letter-spacing:-.02em;}
.compare-modal__title em{font-style:italic;color:var(--gold);}
.compare-modal__close{background:none;border:1px solid rgba(245,242,237,.2);color:var(--white);width:56px;height:56px;font-size:1.8rem;cursor:none;transition:border-color .3s,color .3s;}
.compare-modal__close:hover{border-color:var(--gold);color:var(--gold);}
.compare-table-grid{display:grid;gap:0;}
.ctg-label-cell{padding:2rem 0;border-bottom:1px solid rgba(245,242,237,.06);font-family:var(--font-m);font-size:.9rem;letter-spacing:.12em;text-transform:uppercase;color:var(--silver);}
.ctg-prop-header{padding:2rem 2.4rem;border-bottom:2px solid var(--gold);border-left:1px solid rgba(245,242,237,.06);}
.ctg-prop-name{font-family:var(--font-d);font-size:2.4rem;font-style:italic;margin-bottom:.4rem;}
.ctg-prop-city{font-family:var(--font-m);font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;color:var(--silver);}
.ctg-cell{padding:1.8rem 2.4rem;border-bottom:1px solid rgba(245,242,237,.05);border-left:1px solid rgba(245,242,237,.06);font-family:var(--font-d);font-size:2rem;font-weight:300;opacity:0;transform:translateY(12px);}
.ctg-cell.highlight{color:var(--gold);}
.ctg-cell .unit{font-family:var(--font-m);font-size:.85rem;color:var(--silver);margin-left:.4rem;}

/* ============================================================
   A07 — MORTGAGE SIMULATOR
============================================================ */
.mortgage-sec{padding:13rem 5.6rem;background:var(--dark3);}
.mortgage-sec__title{font-family:var(--font-d);font-size:clamp(3.6rem,4.5vw,6.4rem);font-weight:300;margin-bottom:6.4rem;opacity:0;transform:translateY(28px);}
.mortgage-sec__title em{font-style:italic;color:var(--gold);}
.mortgage-grid{display:grid;grid-template-columns:1fr 1fr;gap:8rem;align-items:start;}
.mort-field{margin-bottom:4rem;}
.mort-label{display:block;font-family:var(--font-m);font-size:.9rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);margin-bottom:1.6rem;}
.mort-range{width:100%;-webkit-appearance:none;appearance:none;height:2px;background:rgba(245,242,237,.15);outline:none;cursor:none;}
.mort-range::-webkit-slider-thumb{-webkit-appearance:none;width:18px;height:18px;background:var(--gold);border-radius:50%;cursor:none;box-shadow:0 0 12px rgba(184,149,63,.4);transition:transform .2s;}
.mort-range::-webkit-slider-thumb:hover{transform:scale(1.3);}
.mort-range-display{display:flex;justify-content:space-between;align-items:center;margin-top:.8rem;}
.mort-range-display span{font-family:var(--font-d);font-size:2rem;font-weight:300;color:var(--white);}
.mort-sub{font-family:var(--font-m);font-size:1rem !important;color:var(--silver) !important;}
.mort-kpi-grid{display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-bottom:4rem;}
.mort-kpi{padding:2.4rem;background:rgba(245,242,237,.03);border:1px solid rgba(245,242,237,.07);}
.mort-kpi--accent{background:rgba(184,149,63,.06);border-color:rgba(184,149,63,.2);}
.mort-kpi--dim{opacity:.75;}
.mort-kpi-v{display:block;font-family:var(--font-d);font-size:3rem;font-weight:300;color:var(--gold);margin-bottom:.6rem;}
.mort-kpi-l{font-family:var(--font-m);font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;color:var(--silver);}
.mort-kpi-l small{font-size:.75rem;}
.mort-donut-wrap{display:flex;align-items:center;gap:4rem;}
.mort-donut{width:160px;height:160px;flex-shrink:0;}
.mort-donut-legend{display:flex;flex-direction:column;gap:1.6rem;}
.mort-legend-item{display:flex;align-items:center;gap:1.2rem;}
.mort-legend-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0;}
.mort-legend-label{font-family:var(--font-m);font-size:.9rem;letter-spacing:.1em;text-transform:uppercase;color:var(--silver);flex:1;}
.mort-legend-val{font-family:var(--font-d);font-size:1.8rem;font-weight:300;color:var(--gold);}

/* ============================================================
   A08 — RADAR CHART
============================================================ */
.radar-wrap{margin-top:3.2rem;padding:2.4rem;background:rgba(245,242,237,.02);border:1px solid rgba(245,242,237,.06);}
.radar-header{display:flex;align-items:center;gap:.8rem;margin-bottom:2rem;}
.radar-title{font-family:var(--font-m);font-size:.9rem;letter-spacing:.15em;text-transform:uppercase;color:var(--silver);flex:1;}
.radar-total{font-family:var(--font-d);font-size:3.2rem;font-weight:300;color:var(--gold);line-height:1;}
.radar-unit{font-family:var(--font-m);font-size:.9rem;color:var(--silver);}
.radar-svg{width:100%;max-width:280px;height:auto;display:block;margin:0 auto;}
.radar-grid{fill:none;stroke:rgba(245,242,237,.07);stroke-width:1;}
.radar-axis{stroke:rgba(245,242,237,.07);stroke-width:1;}
.radar-fill{fill:rgba(184,149,63,.18);stroke:var(--gold);stroke-width:1.5;transition:none;}
.radar-label{font-family:var(--font-m);font-size:9px;fill:rgba(245,242,237,.35);letter-spacing:.05em;}

/* ============================================================
   A09 — VIRTUAL TOUR
============================================================ */
.vtour-btn{display:inline-flex;align-items:center;gap:1rem;background:none;border:1px solid rgba(184,149,63,.3);color:var(--gold);font-family:var(--font-m);font-size:.9rem;letter-spacing:.15em;text-transform:uppercase;padding:1rem 2.4rem;cursor:none;margin-top:1.6rem;transition:all .3s;}
.vtour-btn:hover{background:rgba(184,149,63,.1);border-color:var(--gold);}
.vtour-btn__icon{font-size:1.4rem;animation:vtour-spin 6s linear infinite;}
@keyframes vtour-spin{to{transform:rotate(360deg);}}
.vtour-overlay{position:fixed;inset:0;z-index:9500;background:var(--void);opacity:0;pointer-events:none;transition:opacity .4s;}
.vtour-overlay.open{opacity:1;pointer-events:all;}
.vtour-bg{position:absolute;inset:0;}
.vtour-bg img{width:100%;height:100%;object-fit:cover;transition:none;}
.vtour-overlay-mask{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(6,6,6,.7) 0%,transparent 30%,transparent 70%,rgba(6,6,6,.7) 100%);}
.vtour-header{position:absolute;top:0;left:0;right:0;z-index:2;padding:3.2rem 5.6rem;display:flex;align-items:center;gap:3.2rem;}
.vtour-name{font-family:var(--font-d);font-size:2.4rem;font-style:italic;flex:1;}
.vtour-counter{font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;color:var(--silver);}
.vtour-close{background:none;border:1px solid rgba(245,242,237,.2);color:var(--white);width:48px;height:48px;font-size:1.6rem;cursor:none;transition:border-color .3s;}
.vtour-close:hover{border-color:var(--gold);color:var(--gold);}
.vtour-nav{position:absolute;top:50%;left:0;right:0;z-index:2;transform:translateY(-50%);display:flex;justify-content:space-between;padding:0 3.2rem;pointer-events:none;}
.vtour-prev,.vtour-next{pointer-events:all;background:none;border:1px solid rgba(245,242,237,.2);color:var(--white);width:56px;height:56px;font-size:2.4rem;cursor:none;display:flex;align-items:center;justify-content:center;transition:all .3s;}
.vtour-prev:hover,.vtour-next:hover{border-color:var(--gold);color:var(--gold);background:rgba(184,149,63,.1);}
.vtour-dots{position:absolute;bottom:5.6rem;left:50%;transform:translateX(-50%);z-index:2;display:flex;gap:1rem;}
.vtour-dot{width:6px;height:6px;border-radius:50%;background:rgba(245,242,237,.3);transition:all .3s;cursor:none;}
.vtour-dot.active{background:var(--gold);transform:scale(1.3);}
.vtour-caption{position:absolute;bottom:5.6rem;right:5.6rem;z-index:2;font-family:var(--font-m);font-size:.9rem;letter-spacing:.18em;text-transform:uppercase;color:rgba(245,242,237,.4);}

/* ============================================================
   A10 — MARKET DATA
============================================================ */
.market-sec{padding:13rem 5.6rem;background:var(--black);}
.market-sec__title{font-family:var(--font-d);font-size:clamp(3.6rem,4.5vw,6.4rem);font-weight:300;margin-bottom:4rem;opacity:0;transform:translateY(28px);}
.market-sec__title em{font-style:italic;color:var(--gold);}
.market-tabs{display:flex;gap:0;margin-bottom:5.6rem;}
.mtab{font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;padding:1.2rem 3.2rem;cursor:none;background:none;border:1px solid rgba(245,242,237,.1);color:rgba(245,242,237,.4);margin-right:-1px;transition:all .3s;}
.mtab.active,.mtab:hover{background:rgba(184,149,63,.1);border-color:var(--gold);color:var(--gold);z-index:1;}
.market-grid{display:grid;grid-template-columns:1fr 2fr;gap:6rem;align-items:start;}
.market-kpis{display:flex;flex-direction:column;gap:2.4rem;}
.mkt-kpi{padding:2.4rem;background:rgba(245,242,237,.02);border:1px solid rgba(245,242,237,.06);}
.mkt-kpi-v{display:block;font-family:var(--font-d);font-size:3.6rem;font-weight:300;color:var(--gold);line-height:1;margin-bottom:.6rem;}
.mkt-kpi-l{font-family:var(--font-m);font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;color:var(--silver);}
.market-chart-title{font-family:var(--font-m);font-size:.9rem;letter-spacing:.15em;text-transform:uppercase;color:var(--silver);margin-bottom:2rem;}
.market-chart-svg{width:100%;height:auto;display:block;}
.market-chart-months{display:flex;justify-content:space-between;padding-top:.8rem;font-family:var(--font-m);font-size:.75rem;letter-spacing:.08em;color:rgba(245,242,237,.2);}

/* ============================================================
   A11 — BOOKING WIDGET
============================================================ */
.booking-widget{margin-top:3.2rem;padding:2.8rem;background:rgba(245,242,237,.02);border:1px solid rgba(184,149,63,.2);}
.bw-header{margin-bottom:2.4rem;}
.bw-title{display:block;font-family:var(--font-m);font-size:1rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);margin-bottom:.4rem;}
.bw-subtitle{font-family:var(--font-b);font-size:1.3rem;color:rgba(245,242,237,.45);}
.bw-cal-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:1.6rem;}
.bw-cal-month{font-family:var(--font-m);font-size:1rem;letter-spacing:.12em;text-transform:uppercase;}
.bw-cal-nav{background:none;border:1px solid rgba(245,242,237,.15);color:var(--white);width:32px;height:32px;cursor:none;font-size:1.4rem;transition:border-color .3s;}
.bw-cal-nav:hover{border-color:var(--gold);}
.bw-cal-days-labels{display:grid;grid-template-columns:repeat(7,1fr);gap:.4rem;margin-bottom:.8rem;}
.bw-cal-days-labels span{font-family:var(--font-m);font-size:.75rem;letter-spacing:.1em;text-align:center;color:rgba(245,242,237,.3);padding:.4rem;}
.bw-cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:.4rem;margin-bottom:2.4rem;}
.bw-cal-day{aspect-ratio:1;display:flex;align-items:center;justify-content:center;font-family:var(--font-m);font-size:.9rem;cursor:none;border:1px solid transparent;transition:all .2s;}
.bw-cal-day:not(.empty):not(.past):hover{border-color:rgba(184,149,63,.4);background:rgba(184,149,63,.08);}
.bw-cal-day.selected{background:var(--gold);color:var(--void);border-color:var(--gold);}
.bw-cal-day.past,.bw-cal-day.empty{opacity:.2;pointer-events:none;}
.bw-cal-day.today{border-color:rgba(184,149,63,.3);}
.bw-slots-label{font-family:var(--font-m);font-size:.85rem;letter-spacing:.15em;text-transform:uppercase;color:var(--silver);display:block;margin-bottom:1.2rem;}
.bw-slots-grid{display:flex;flex-wrap:wrap;gap:.8rem;margin-bottom:2.4rem;}
.bw-slot{font-family:var(--font-m);font-size:.9rem;letter-spacing:.1em;background:none;border:1px solid rgba(245,242,237,.12);color:rgba(245,242,237,.6);padding:.6rem 1.6rem;cursor:none;transition:all .25s;}
.bw-slot:hover{border-color:rgba(184,149,63,.4);color:var(--gold);}
.bw-slot.active{background:var(--gold);color:var(--void);border-color:var(--gold);}
.bw-confirm-summary{font-family:var(--font-d);font-size:1.6rem;font-style:italic;color:var(--gold);margin-bottom:1.6rem;}
.bw-email{width:100%;background:rgba(245,242,237,.04);border:1px solid rgba(245,242,237,.12);color:var(--white);font-family:var(--font-b);font-size:1.4rem;font-weight:300;padding:1.2rem 1.6rem;outline:none;margin-bottom:1.6rem;transition:border-color .3s;}
.bw-email:focus{border-color:var(--gold);}
.bw-confirm-btn{background:var(--gold);color:var(--void);border:none;font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;padding:1.2rem 2.8rem;cursor:none;transition:background .3s;}
.bw-confirm-btn:hover{background:var(--gold-bright);}
.bw-success{text-align:center;padding:3.2rem 0;}
.bw-success-icon{display:block;font-size:3.2rem;color:#4ade80;margin-bottom:1.6rem;}
.bw-success-text{font-family:var(--font-d);font-size:1.8rem;font-style:italic;color:rgba(245,242,237,.7);line-height:1.6;}

/* ============================================================
   A12 — AGENT DASHBOARD
============================================================ */
.agent-dash{position:fixed;inset:0;z-index:9800;background:rgba(6,6,6,.97);backdrop-filter:blur(32px);display:flex;flex-direction:column;transform:translateY(-100%);transition:transform .6s var(--ease-out);overflow-y:auto;}
.agent-dash.open{transform:translateY(0);}
.ad-header{display:flex;align-items:center;justify-content:space-between;padding:2.4rem 5.6rem;border-bottom:1px solid rgba(184,149,63,.2);position:sticky;top:0;background:rgba(6,6,6,.95);z-index:1;backdrop-filter:blur(16px);}
.ad-logo{font-family:var(--font-m);font-size:1rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);display:flex;align-items:center;gap:1.2rem;}
.ad-header-right{display:flex;align-items:center;gap:1.6rem;}
.ad-live-dot{width:8px;height:8px;border-radius:50%;background:#4ade80;box-shadow:0 0 8px rgba(74,222,128,.5);animation:live-pulse 2s ease-in-out infinite;}
.ad-live-label{font-family:var(--font-m);font-size:.85rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(74,222,128,.6);}
.ad-close{background:none;border:1px solid rgba(245,242,237,.2);color:var(--white);width:40px;height:40px;font-size:1.4rem;cursor:none;transition:all .3s;}
.ad-close:hover{border-color:var(--gold);color:var(--gold);}
.ad-body{padding:4rem 5.6rem;display:flex;flex-direction:column;gap:4.8rem;}
.ad-kpis{display:grid;grid-template-columns:repeat(5,1fr);gap:2rem;}
.ad-kpi{padding:2rem;background:rgba(245,242,237,.03);border:1px solid rgba(245,242,237,.07);}
.ad-kpi-v{font-family:var(--font-d);font-size:3rem;font-weight:300;color:var(--gold);display:block;line-height:1;margin-bottom:.6rem;}
.ad-kpi-l{font-family:var(--font-m);font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--silver);}
.ad-section-title{font-family:var(--font-m);font-size:.9rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-bottom:2rem;padding-bottom:1.2rem;border-bottom:1px solid rgba(184,149,63,.15);}
.ad-bookings{display:flex;flex-direction:column;gap:1.2rem;}
.ad-booking-row{display:grid;grid-template-columns:1fr 1fr 1fr 140px;gap:2rem;align-items:center;padding:1.6rem 2rem;background:rgba(245,242,237,.02);border:1px solid rgba(245,242,237,.06);}
.ad-b-prop{font-family:var(--font-d);font-size:1.6rem;font-style:italic;}
.ad-b-date{font-family:var(--font-m);font-size:.9rem;letter-spacing:.1em;color:var(--silver);}
.ad-b-email{font-family:var(--font-m);font-size:.85rem;color:rgba(245,242,237,.45);}
.ad-b-status{font-family:var(--font-m);font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;padding:.4rem 1.2rem;text-align:center;}
.ad-b-status.pending{background:rgba(251,191,36,.1);color:#fbbf24;border:1px solid rgba(251,191,36,.3);}
.ad-b-status.confirmed{background:rgba(74,222,128,.1);color:#4ade80;border:1px solid rgba(74,222,128,.3);}
.ad-props{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;}
.ad-prop-row{padding:2rem;background:rgba(245,242,237,.02);border:1px solid rgba(245,242,237,.06);display:flex;flex-direction:column;gap:1.2rem;}
.ad-pr-name{font-family:var(--font-d);font-size:1.8rem;font-style:italic;}
.ad-pr-city{font-family:var(--font-m);font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--silver);}
.ad-pr-price{font-family:var(--font-m);font-size:.95rem;color:var(--gold);}
.ad-pr-status{font-family:var(--font-m);font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;padding:.4rem 1.2rem;display:inline-block;}
.ad-pr-status.available{background:rgba(74,222,128,.1);color:#4ade80;}
.ad-pr-status.rented{background:rgba(245,242,237,.08);color:var(--silver);}
.ad-pr-status.negociation{background:rgba(251,191,36,.1);color:#fbbf24;}

@keyframes live-pulse{0%,100%{opacity:1;}50%{opacity:.4;}}
"""

# ============================================================
# HTML SECTIONS TO INSERT
# ============================================================

# A01 — Before/After slider HTML (insert inside first .psi__img-wrap)
BA_SLIDER_HTML = """<div class="ba-slider" id="ba-slider">\
<div class="ba-slider__label ba-slider__label--before">Before</div>\
<div class="ba-slider__label ba-slider__label--after">After</div>\
<div class="ba-after"><img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=90&auto=format&fit=crop" alt="After renovation"></div>\
<div class="ba-before" id="ba-before"><img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&q=90&auto=format&fit=crop" alt="Before renovation"></div>\
<div class="ba-handle" id="ba-handle"><div class="ba-handle__line"></div><div class="ba-handle__circle"><span class="ba-handle__arrow ba-handle__arrow--left">‹</span><span class="ba-handle__arrow ba-handle__arrow--right">›</span></div></div>\
</div>\
<button class="ba-toggle" id="ba-toggle"><span class="ba-toggle__icon">◧</span><span class="ba-toggle__label">Before / After</span></button>"""

# A02 — Flip cards section (insert after <!-- METRICS --> section)
FLIP_SECTION_HTML = """<!-- FLIP CARDS -->\
<section class="flip-section" id="flip-section">\
<div class="container">\
<div class="s-tag"><span>Quick View</span></div>\
<h2 class="flip-section__title fade-reveal">Hover to <em>Explore</em></h2>\
<div class="flip-grid">\
<div class="flip-card">\
<div class="flip-card__inner">\
<div class="flip-card__front">\
<img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800&q=88&auto=format&fit=crop" alt="Tour Lumière">\
<div class="flip-card__front-overlay"><span class="flip-card__type">Penthouse</span><span class="flip-card__city">Paris 16e</span><span class="flip-card__hint">Hover to discover →</span></div>\
</div>\
<div class="flip-card__back"><div class="flip-card__back-content">\
<div class="flip-card__back-tag">Penthouse · Available</div>\
<h3 class="flip-card__back-name">Tour Lumière</h3>\
<div class="flip-card__back-loc">Paris 16e, France</div>\
<div class="flip-card__back-price">€ 18,500 <span>/mo</span></div>\
<div class="flip-card__back-specs"><span>340 m²</span><span>4 bd</span><span>3 ba</span><span>4.8% yield</span></div>\
<div class="flip-card__back-desc">22nd floor architectural masterpiece. Panoramic Eiffel Tower views.</div>\
<a href="#contact" class="flip-card__back-btn">Request Viewing →</a>\
</div></div>\
</div></div>\
<div class="flip-card">\
<div class="flip-card__inner">\
<div class="flip-card__front">\
<img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&q=88&auto=format&fit=crop" alt="The Meridian">\
<div class="flip-card__front-overlay"><span class="flip-card__type">Apartment</span><span class="flip-card__city">London Mayfair</span><span class="flip-card__hint">Hover to discover →</span></div>\
</div>\
<div class="flip-card__back"><div class="flip-card__back-content">\
<div class="flip-card__back-tag">Apartment · Available</div>\
<h3 class="flip-card__back-name">The Meridian</h3>\
<div class="flip-card__back-loc">London Mayfair, UK</div>\
<div class="flip-card__back-price">€ 22,000 <span>/mo</span></div>\
<div class="flip-card__back-specs"><span>280 m²</span><span>3 bd</span><span>2 ba</span><span>3.2% yield</span></div>\
<div class="flip-card__back-desc">Georgian architecture meets contemporary luxury in the heart of Mayfair.</div>\
<a href="#contact" class="flip-card__back-btn">Request Viewing →</a>\
</div></div>\
</div></div>\
<div class="flip-card">\
<div class="flip-card__inner">\
<div class="flip-card__front">\
<img src="https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800&q=88&auto=format&fit=crop" alt="Villa Aurelia">\
<div class="flip-card__front-overlay"><span class="flip-card__type">Villa</span><span class="flip-card__city">Athens Kifissia</span><span class="flip-card__hint">Hover to discover →</span></div>\
</div>\
<div class="flip-card__back"><div class="flip-card__back-content">\
<div class="flip-card__back-tag">Villa · Available</div>\
<h3 class="flip-card__back-name">Villa Aurelia</h3>\
<div class="flip-card__back-loc">Athens Kifissia, Greece</div>\
<div class="flip-card__back-price">€ 12,500 <span>/mo</span></div>\
<div class="flip-card__back-specs"><span>520 m²</span><span>5 bd</span><span>4 ba</span><span>5.4% yield</span></div>\
<div class="flip-card__back-desc">Mediterranean villa with infinity pool overlooking the Aegean Sea.</div>\
<a href="#contact" class="flip-card__back-btn">Request Viewing →</a>\
</div></div>\
</div></div>\
</div></div></section>"""

# A05 — Yield calculator HTML (insert in first .psi__right)
YIELD_CALC_HTML = """<div class="rent-calc" id="rent-calc-1">\
<div class="rent-calc__header">\
<span class="rent-calc__icon">📊</span>\
<span class="rent-calc__title">Yield Calculator</span>\
<button class="rent-calc__toggle" data-calc="1"><span class="rent-calc__toggle-label">Open</span><span class="rent-calc__toggle-icon">↓</span></button>\
</div>\
<div class="rent-calc__body" id="rcb-1" style="display:none">\
<div class="rc-inputs">\
<div class="rc-field"><label class="rc-label">Purchase Price (€)</label><input type="number" class="rc-input" id="rc-price-1" value="850000"></div>\
<div class="rc-field"><label class="rc-label">Monthly Rent (€)</label><input type="number" class="rc-input" id="rc-rent-1" value="18500"></div>\
<div class="rc-field"><label class="rc-label">Monthly Charges (€)</label><input type="number" class="rc-input" id="rc-charges-1" value="800"></div>\
<div class="rc-field"><label class="rc-label">Notary Fees (%)</label><input type="number" class="rc-input" id="rc-notary-1" value="7.5" step="0.1"></div>\
</div>\
<div class="rc-results" id="rc-results-1">\
<div class="rc-result-item"><span class="rc-result-label">Gross Yield</span><span class="rc-result-value" id="rc-gross-1">—</span></div>\
<div class="rc-result-item"><span class="rc-result-label">Net Yield</span><span class="rc-result-value" id="rc-net-1">—</span></div>\
<div class="rc-result-item"><span class="rc-result-label">Monthly Cash Flow</span><span class="rc-result-value" id="rc-cashflow-1">—</span></div>\
<div class="rc-result-item rc-result-item--highlight"><span class="rc-result-label">ROI at 10 years</span><span class="rc-result-value" id="rc-roi-1">—</span></div>\
</div>\
<div class="rc-chart-wrap"><svg class="rc-chart" id="rc-chart-1" viewBox="0 0 400 120"><line x1="0" y1="119" x2="400" y2="119" stroke="rgba(245,242,237,.1)" stroke-width="1"/><path class="rc-chart-line" id="rc-chart-line-1" d="" fill="none" stroke="var(--gold)" stroke-width="2" style="stroke-dasharray:600;stroke-dashoffset:600"/><path class="rc-chart-area" id="rc-chart-area-1" d="" fill="rgba(184,149,63,.1)"/></svg>\
<div class="rc-chart-labels"><span>Y1</span><span>Y3</span><span>Y5</span><span>Y7</span><span>Y10</span></div></div>\
</div></div>"""

# A08 — Radar chart HTML (insert in first .psi__right)
RADAR_HTML = """<div class="radar-wrap" data-scores="92,78,85,96,88,74">\
<div class="radar-header"><span class="radar-title">Location Score</span><span class="radar-total" data-target="88">0</span><span class="radar-unit">/100</span></div>\
<svg class="radar-svg" viewBox="0 0 280 280" id="radar-1">\
<polygon class="radar-grid" points="140,20 233,80 233,200 140,260 47,200 47,80"/>\
<polygon class="radar-grid" points="140,55 208,100 208,180 140,225 72,180 72,100"/>\
<polygon class="radar-grid" points="140,90 182,120 182,160 140,190 98,160 98,120"/>\
<line class="radar-axis" x1="140" y1="20" x2="140" y2="260"/>\
<line class="radar-axis" x1="233" y1="80" x2="47" y2="200"/>\
<line class="radar-axis" x1="233" y1="200" x2="47" y2="80"/>\
<polygon class="radar-fill" id="radar-fill-1" points="140,140 140,140 140,140 140,140 140,140 140,140"/>\
<text x="140" y="12" class="radar-label" text-anchor="middle">Transport</text>\
<text x="244" y="78" class="radar-label" text-anchor="start">Shops</text>\
<text x="244" y="210" class="radar-label" text-anchor="start">Schools</text>\
<text x="140" y="274" class="radar-label" text-anchor="middle">Safety</text>\
<text x="36" y="210" class="radar-label" text-anchor="end">Yield</text>\
<text x="36" y="78" class="radar-label" text-anchor="end">Prestige</text>\
</svg></div>"""

# A07 — Mortgage section HTML (insert before <!-- CTA -->)
MORTGAGE_HTML = """<!-- MORTGAGE SIMULATOR -->\
<section class="mortgage-sec" id="mortgage">\
<div class="container">\
<div class="s-tag"><span>Financial Tools</span></div>\
<h2 class="mortgage-sec__title fade-reveal">Mortgage <em>Simulator</em></h2>\
<div class="mortgage-grid">\
<div class="mort-inputs">\
<div class="mort-field"><label class="mort-label">Property Price (€)</label><div class="mort-input-wrap"><input type="range" class="mort-range" id="mort-price" min="200000" max="5000000" step="50000" value="850000"><div class="mort-range-display"><span id="mort-price-display">€ 850,000</span></div></div></div>\
<div class="mort-field"><label class="mort-label">Down Payment (%)</label><div class="mort-input-wrap"><input type="range" class="mort-range" id="mort-down" min="10" max="60" step="5" value="20"><div class="mort-range-display"><span id="mort-down-display">20%</span><span id="mort-down-amount" class="mort-sub">€ 170,000</span></div></div></div>\
<div class="mort-field"><label class="mort-label">Interest Rate (%)</label><div class="mort-input-wrap"><input type="range" class="mort-range" id="mort-rate" min="1" max="8" step="0.1" value="3.5"><div class="mort-range-display"><span id="mort-rate-display">3.5%</span></div></div></div>\
<div class="mort-field"><label class="mort-label">Duration (years)</label><div class="mort-input-wrap"><input type="range" class="mort-range" id="mort-dur" min="10" max="30" step="5" value="20"><div class="mort-range-display"><span id="mort-dur-display">20 years</span></div></div></div>\
</div>\
<div class="mort-results">\
<div class="mort-kpi-grid">\
<div class="mort-kpi"><span class="mort-kpi-v" id="mort-monthly">€ —</span><span class="mort-kpi-l">Monthly Payment</span></div>\
<div class="mort-kpi"><span class="mort-kpi-v" id="mort-total">€ —</span><span class="mort-kpi-l">Total Repaid</span></div>\
<div class="mort-kpi mort-kpi--dim"><span class="mort-kpi-v" id="mort-interest">€ —</span><span class="mort-kpi-l">Total Interest</span></div>\
<div class="mort-kpi mort-kpi--accent"><span class="mort-kpi-v" id="mort-capacity">€ —</span><span class="mort-kpi-l">Borrow Capacity</span></div>\
</div>\
<div class="mort-donut-wrap">\
<svg class="mort-donut" viewBox="0 0 200 200" id="mort-donut-svg">\
<circle cx="100" cy="100" r="70" fill="none" stroke="rgba(245,242,237,.08)" stroke-width="20"/>\
<circle id="mort-donut-capital" cx="100" cy="100" r="70" fill="none" stroke="var(--gold)" stroke-width="20" stroke-dasharray="439.8" stroke-dashoffset="0" transform="rotate(-90 100 100)"/>\
<circle id="mort-donut-interest" cx="100" cy="100" r="70" fill="none" stroke="rgba(184,149,63,.3)" stroke-width="20" stroke-dasharray="0 439.8" transform="rotate(-90 100 100)"/>\
</svg>\
<div class="mort-donut-legend">\
<div class="mort-legend-item"><span class="mort-legend-dot" style="background:var(--gold)"></span><span class="mort-legend-label">Capital</span><span class="mort-legend-val" id="mort-leg-cap">—</span></div>\
<div class="mort-legend-item"><span class="mort-legend-dot" style="background:rgba(184,149,63,.4)"></span><span class="mort-legend-label">Interest</span><span class="mort-legend-val" id="mort-leg-int">—</span></div>\
</div></div></div></div></div></section>"""

# A10 — Market data section HTML (insert before <!-- CTA -->)
MARKET_HTML = """<!-- MARKET DATA -->\
<section class="market-sec" id="market">\
<div class="container">\
<div class="s-tag"><span>Market Intelligence</span></div>\
<h2 class="market-sec__title fade-reveal">Real Estate <em>Market Data</em></h2>\
<div class="market-tabs">\
<button class="mtab active" data-zone="paris">Paris</button>\
<button class="mtab" data-zone="london">London</button>\
<button class="mtab" data-zone="athens">Athens</button>\
<button class="mtab" data-zone="monaco">Monaco</button>\
</div>\
<div class="market-grid">\
<div class="market-kpis" id="market-kpis">\
<div class="mkt-kpi"><span class="mkt-kpi-v" id="mkt-price-m2">—</span><span class="mkt-kpi-l">Avg. Price / m²</span></div>\
<div class="mkt-kpi"><span class="mkt-kpi-v" id="mkt-yoy">—</span><span class="mkt-kpi-l">YoY Change</span></div>\
<div class="mkt-kpi"><span class="mkt-kpi-v" id="mkt-days">—</span><span class="mkt-kpi-l">Avg. Days to Rent</span></div>\
<div class="mkt-kpi"><span class="mkt-kpi-v" id="mkt-yield">—</span><span class="mkt-kpi-l">Avg. Gross Yield</span></div>\
</div>\
<div class="market-chart-wrap">\
<div class="market-chart-title">Price per m² — Last 12 months</div>\
<svg class="market-chart-svg" id="market-chart-svg" viewBox="0 0 800 200">\
<line x1="0" y1="199" x2="800" y2="199" stroke="rgba(245,242,237,.08)" stroke-width="1"/>\
<path id="market-chart-line" d="" fill="none" stroke="var(--gold)" stroke-width="2" style="stroke-dasharray:1200;stroke-dashoffset:1200"/>\
<path id="market-chart-area" d="" fill="rgba(184,149,63,.08)"/>\
</svg>\
<div class="market-chart-months"><span>Jan</span><span>Feb</span><span>Mar</span><span>Apr</span><span>May</span><span>Jun</span><span>Jul</span><span>Aug</span><span>Sep</span><span>Oct</span><span>Nov</span><span>Dec</span></div>\
</div></div></div></section>"""

# A06 — Compare bar + modal + A04 cursor preview + A09 vtour overlay + A12 agent dash
# All go before </body>
GLOBAL_HTML_BEFORE_BODY = """<!-- A06 COMPARE BAR -->\
<div class="compare-bar" id="compare-bar">\
<div class="compare-bar__slots" id="compare-slots"></div>\
<div class="compare-bar__actions">\
<span class="compare-bar__count" id="compare-count">0 selected</span>\
<button class="compare-bar__clear" id="compare-clear">Clear</button>\
<button class="compare-bar__open" id="compare-open" disabled>Compare Now →</button>\
</div></div>\
<div class="compare-modal" id="compare-modal">\
<div class="compare-modal__inner">\
<div class="compare-modal__header">\
<h2 class="compare-modal__title">Property <em>Comparison</em></h2>\
<button class="compare-modal__close" id="compare-close">✕</button>\
</div>\
<div class="compare-modal__table" id="compare-table"></div>\
</div></div>\
<!-- A04 CURSOR PREVIEW -->\
<div class="cursor-preview" id="cursor-preview">\
<div class="cursor-preview__img-wrap"><img id="cursor-preview-img" src="" alt=""></div>\
<div class="cursor-preview__info"><span class="cursor-preview__name" id="cursor-preview-name">—</span><span class="cursor-preview__price" id="cursor-preview-price">—</span></div>\
</div>\
<!-- A09 VIRTUAL TOUR OVERLAY -->\
<div class="vtour-overlay" id="vtour-overlay">\
<div class="vtour-bg" id="vtour-bg"><img id="vtour-img" src="" alt=""></div>\
<div class="vtour-overlay-mask" id="vtour-mask"></div>\
<div class="vtour-header"><span class="vtour-name" id="vtour-name">—</span><span class="vtour-counter" id="vtour-counter">1 / 4</span><button class="vtour-close" id="vtour-close">✕</button></div>\
<div class="vtour-nav"><button class="vtour-prev" id="vtour-prev">‹</button><button class="vtour-next" id="vtour-next">›</button></div>\
<div class="vtour-dots" id="vtour-dots"></div>\
<div class="vtour-caption" id="vtour-caption">Living Room</div>\
</div>\
<!-- A12 AGENT DASHBOARD -->\
<div class="agent-dash" id="agent-dash">\
<div class="ad-header">\
<div class="ad-logo"><svg width="18" height="18" viewBox="0 0 32 32"><polygon points="16,2 30,28 2,28" fill="none" stroke="var(--gold)" stroke-width="2"/></svg>NOVUS — Agent Dashboard</div>\
<div class="ad-header-right"><span class="ad-live-dot"></span><span class="ad-live-label">Live Mode</span><button class="ad-close" id="ad-close">✕</button></div>\
</div>\
<div class="ad-body">\
<div class="ad-kpis" id="ad-kpis"></div>\
<div class="ad-section"><div class="ad-section-title">Recent Bookings</div><div class="ad-bookings" id="ad-bookings"></div></div>\
<div class="ad-section"><div class="ad-section-title">Property Status</div><div class="ad-props" id="ad-props"></div></div>\
</div></div>\
<div id="dash-hint" style="position:fixed;bottom:2rem;right:2rem;z-index:50;opacity:0;font-family:DM Mono,monospace;font-size:.7rem;letter-spacing:.15em;color:rgba(184,149,63,.3);pointer-events:none;user-select:none;">Double-click logo for Agent Mode</div>"""

# A06 compare buttons — add to each prop-stacked__item's .psi__right
COMPARE_BTN_1 = """<button class="compare-btn" data-prop-id="prop-1" data-prop-name="Tour Lumière" data-prop-city="Paris 16e" data-prop-price="€ 18,500/mo" data-prop-size="340" data-prop-bed="4" data-prop-bath="3" data-prop-yield="4.8" data-prop-score="94" data-prop-img="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=400">+ Add to Compare</button>"""

COMPARE_BTN_2 = """<button class="compare-btn" data-prop-id="prop-2" data-prop-name="The Meridian" data-prop-city="London Mayfair" data-prop-price="€ 22,000/mo" data-prop-size="280" data-prop-bed="3" data-prop-bath="2" data-prop-yield="3.2" data-prop-score="91" data-prop-img="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=400">+ Add to Compare</button>"""

COMPARE_BTN_3 = """<button class="compare-btn" data-prop-id="prop-3" data-prop-name="Villa Aurelia" data-prop-city="Athens Kifissia" data-prop-price="€ 12,500/mo" data-prop-size="520" data-prop-bed="5" data-prop-bath="4" data-prop-yield="5.4" data-prop-score="87" data-prop-img="https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=400">+ Add to Compare</button>"""

# A09 virtual tour buttons
VTOUR_BTN_1 = """<button class="vtour-btn" data-tour-images="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1600|https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=1600|https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600|https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=1600" data-tour-name="Tour Lumière"><span class="vtour-btn__icon">⬡</span>Virtual Tour</button>"""

# A11 — Booking widget HTML (insert in first .psi__right)
BOOKING_HTML = """<div class="booking-widget" id="booking-1" data-prop="Tour Lumière">\
<div class="bw-header"><span class="bw-title">Book a Viewing</span><span class="bw-subtitle">Select a date & time</span></div>\
<div class="bw-calendar" id="bwc-1">\
<div class="bw-cal-header"><button class="bw-cal-nav" id="bwc-prev-1">‹</button><span class="bw-cal-month" id="bwc-month-1">April 2025</span><button class="bw-cal-nav" id="bwc-next-1">›</button></div>\
<div class="bw-cal-days-labels"><span>Mo</span><span>Tu</span><span>We</span><span>Th</span><span>Fr</span><span>Sa</span><span>Su</span></div>\
<div class="bw-cal-grid" id="bwcg-1"></div>\
</div>\
<div class="bw-slots" id="bw-slots-1"><span class="bw-slots-label">Available Times</span>\
<div class="bw-slots-grid"><button class="bw-slot" data-time="09:00">09:00</button><button class="bw-slot" data-time="10:30">10:30</button><button class="bw-slot" data-time="14:00">14:00</button><button class="bw-slot" data-time="15:30">15:30</button><button class="bw-slot" data-time="17:00">17:00</button></div>\
</div>\
<div class="bw-confirm" id="bw-confirm-1" style="display:none"><div class="bw-confirm-summary" id="bwcs-1">—</div><input class="bw-email" type="email" placeholder="Your email address" id="bw-email-1"><button class="bw-confirm-btn" id="bw-submit-1">Confirm Booking →</button></div>\
<div class="bw-success" id="bw-success-1" style="display:none"><span class="bw-success-icon">✓</span><span class="bw-success-text">Viewing confirmed!</span></div>\
</div>"""


# ============================================================
# ALL JS TO ADD (before the closing </script> or before </body>)
# ============================================================
ADDON_JS = r"""
/* ============================================================
   A01 — BEFORE/AFTER SLIDER LOGIC
============================================================ */
function initBeforeAfter(){
var toggle=document.getElementById('ba-toggle');
var slider=document.getElementById('ba-slider');
var handle=document.getElementById('ba-handle');
var before=document.getElementById('ba-before');
if(!toggle||!slider)return;
var isDragging=false,sliderActive=false;
toggle.addEventListener('click',function(){
sliderActive=!sliderActive;
slider.classList.toggle('active',sliderActive);
toggle.classList.toggle('active',sliderActive);
if(sliderActive){
var tl=gsap.timeline();
tl.from(slider,{opacity:0,duration:.4});
tl.fromTo({pct:100},{pct:50},{duration:1.2,ease:'power3.inOut',onUpdate:function(){var p=this.targets()[0].pct;before.style.clipPath='inset(0 '+(100-p)+'% 0 0)';handle.style.left=p+'%';}});
}});
function onMove(cx){if(!isDragging||!sliderActive)return;var r=slider.getBoundingClientRect();var p=((cx-r.left)/r.width)*100;p=Math.max(2,Math.min(98,p));before.style.clipPath='inset(0 '+(100-p)+'% 0 0)';handle.style.left=p+'%';}
slider.addEventListener('mousedown',function(){isDragging=true;});
window.addEventListener('mouseup',function(){isDragging=false;});
window.addEventListener('mousemove',function(e){onMove(e.clientX);});
slider.addEventListener('touchstart',function(){isDragging=true;},{passive:true});
window.addEventListener('touchend',function(){isDragging=false;});
window.addEventListener('touchmove',function(e){onMove(e.touches[0].clientX);},{passive:true});
}

/* ============================================================
   A02 — 3D FLIP CARDS REVEAL
============================================================ */
gsap.utils.toArray('.flip-card').forEach(function(card,i){
ScrollTrigger.create({trigger:card,start:'top 85%',onEnter:function(){gsap.to(card,{opacity:1,y:0,duration:.9,delay:i*.15,ease:'power3.out'});}});
});
ScrollTrigger.create({trigger:'.flip-section__title',start:'top 82%',onEnter:function(){gsap.to('.flip-section__title',{opacity:1,y:0,duration:.8,ease:'power3.out'});}});

/* ============================================================
   A03 — AMBIENT VIDEO LOGIC
============================================================ */
function initAmbientVideos(){
document.querySelectorAll('.psi__img-wrap,.flip-card__front').forEach(function(wrap){
var vid=wrap.querySelector('.ambient-vid');
if(!vid)return;
var loaded=false;
wrap.addEventListener('mouseenter',function(){
if(!loaded){vid.src=vid.dataset.src;vid.load();loaded=true;}
vid.play().then(function(){vid.classList.add('playing');}).catch(function(){});
});
wrap.addEventListener('mouseleave',function(){
vid.classList.remove('playing');
setTimeout(function(){if(!vid.classList.contains('playing')){vid.pause();vid.currentTime=0;}},700);
});
});
}

/* ============================================================
   A04 — CURSOR PREVIEW IMAGE LOGIC
============================================================ */
function initCursorPreview(){
var preview=document.getElementById('cursor-preview');
var prevImg=document.getElementById('cursor-preview-img');
var prevName=document.getElementById('cursor-preview-name');
var prevPrice=document.getElementById('cursor-preview-price');
if(!preview)return;
var px=0,py=0;
var zones=document.querySelectorAll('.prop-stacked__item[data-preview-img],.flip-card[data-preview-img]');
zones.forEach(function(zone){
zone.addEventListener('mouseenter',function(){
prevImg.src=zone.dataset.previewImg||'';
prevName.textContent=zone.dataset.previewName||'';
prevPrice.textContent=zone.dataset.previewPrice||'';
gsap.to(preview,{opacity:1,scale:1,duration:.4,ease:'power3.out'});
});
zone.addEventListener('mouseleave',function(){
gsap.to(preview,{opacity:0,scale:.92,duration:.35,ease:'power2.in'});
});
});
window.addEventListener('mousemove',function(e){
px+=(e.clientX-px)*.09;py+=(e.clientY-py)*.09;
});
gsap.ticker.add(function(){gsap.set(preview,{x:px,y:py});});
}

/* ============================================================
   A05 — CALCULATEUR RENTABILITÉ LOGIC
============================================================ */
function initYieldCalculators(){
document.querySelectorAll('.rent-calc').forEach(function(calc){
var id=calc.id.replace('rent-calc-','');
var toggleBtn=calc.querySelector('.rent-calc__toggle');
var body=document.getElementById('rcb-'+id);
var inputs=calc.querySelectorAll('.rc-input');
toggleBtn&&toggleBtn.addEventListener('click',function(){
var isOpen=calc.classList.toggle('open');
toggleBtn.querySelector('.rent-calc__toggle-label').textContent=isOpen?'Close':'Open';
if(isOpen){body.style.display='block';gsap.from(body,{opacity:0,y:-12,duration:.4,ease:'power3.out'});computeYield(id);}
else{gsap.to(body,{opacity:0,duration:.25,onComplete:function(){body.style.display='none';body.style.opacity='';}});}
});
inputs.forEach(function(inp){inp.addEventListener('input',function(){computeYield(id);});});
});
}
function computeYield(id){
var price=parseFloat(document.getElementById('rc-price-'+id).value)||0;
var rent=parseFloat(document.getElementById('rc-rent-'+id).value)||0;
var charges=parseFloat(document.getElementById('rc-charges-'+id).value)||0;
var notaryPct=parseFloat(document.getElementById('rc-notary-'+id).value)||7.5;
if(!price||!rent)return;
var totalCost=price*(1+notaryPct/100);
var annualRent=rent*12;var annualCharges=charges*12;
var grossYield=(annualRent/totalCost*100).toFixed(2);
var netYield=((annualRent-annualCharges)/totalCost*100).toFixed(2);
var cashFlow=(rent-charges).toFixed(0);
var roi10=((annualRent-annualCharges)*10/totalCost*100).toFixed(1);
function animateVal(elId,val,suffix){var el=document.getElementById(elId);if(!el)return;gsap.to({v:0},{v:parseFloat(val),duration:.8,ease:'power2.out',onUpdate:function(){el.textContent=parseFloat(this.targets()[0].v).toFixed(suffix==='%'?2:0)+suffix;}});}
animateVal('rc-gross-'+id,grossYield,'%');animateVal('rc-net-'+id,netYield,'%');animateVal('rc-cashflow-'+id,cashFlow,' €');animateVal('rc-roi-'+id,roi10,'%');
drawRoiChart(id,totalCost,annualRent-annualCharges);
}
function drawRoiChart(id,totalCost,annualNet){
var lineEl=document.getElementById('rc-chart-line-'+id);var areaEl=document.getElementById('rc-chart-area-'+id);
if(!lineEl||!areaEl)return;
var W=400,H=110;var years=[0,1,2,3,4,5,6,7,8,9,10];
var vals=years.map(function(y){return Math.min(annualNet*y/totalCost*100,200);});
var maxV=Math.max.apply(null,vals)||1;
var pts=years.map(function(y,i){return{x:(i/10)*W,y:H-(vals[i]/maxV)*H*.85};});
var linePath='M '+pts.map(function(p){return p.x.toFixed(1)+','+p.y.toFixed(1);}).join(' L ');
var areaPath=linePath+' L '+W+','+H+' L 0,'+H+' Z';
lineEl.setAttribute('d',linePath);areaEl.setAttribute('d',areaPath);
var len=lineEl.getTotalLength?lineEl.getTotalLength():600;
lineEl.style.strokeDasharray=len;lineEl.style.strokeDashoffset=len;
gsap.to(lineEl,{strokeDashoffset:0,duration:1,ease:'power3.inOut'});
}

/* ============================================================
   A06 — COMPARATEUR LOGIC
============================================================ */
function initComparator(){
var compareData=[];var MAX=3;
var bar=document.getElementById('compare-bar');
var slots=document.getElementById('compare-slots');
var count=document.getElementById('compare-count');
var openBtn=document.getElementById('compare-open');
var clearBtn=document.getElementById('compare-clear');
var modal=document.getElementById('compare-modal');
var closeBtn=document.getElementById('compare-close');
function updateBar(){
slots.innerHTML='';
compareData.forEach(function(d,i){
var slot=document.createElement('div');slot.className='compare-slot';
slot.innerHTML='<span class="compare-slot__name">'+d.name+'</span><span class="compare-slot__remove" data-idx="'+i+'">✕</span>';
slot.querySelector('.compare-slot__remove').addEventListener('click',function(){remove(i);});
slots.appendChild(slot);
});
count.textContent=compareData.length+' selected';
bar.classList.toggle('visible',compareData.length>0);
openBtn.disabled=compareData.length<2;
}
function remove(idx){
var removed=compareData.splice(idx,1)[0];
var btn=document.querySelector('.compare-btn[data-prop-id="'+removed.id+'"]');
if(btn)btn.classList.remove('selected');updateBar();
}
document.querySelectorAll('.compare-btn').forEach(function(btn){
btn.addEventListener('click',function(){
var id=btn.dataset.propId;
var exists=compareData.findIndex(function(d){return d.id===id;});
if(exists>-1){remove(exists);return;}
if(compareData.length>=MAX){gsap.to(bar,{x:-8,duration:.05,yoyo:true,repeat:5});return;}
compareData.push({id:id,name:btn.dataset.propName,city:btn.dataset.propCity,price:btn.dataset.propPrice,size:btn.dataset.propSize,bed:btn.dataset.propBed,bath:btn.dataset.propBath,yield:btn.dataset.propYield,score:btn.dataset.propScore,img:btn.dataset.propImg});
btn.classList.add('selected');gsap.from(btn,{scale:.96,duration:.3,ease:'back.out(3)'});updateBar();
});
});
clearBtn&&clearBtn.addEventListener('click',function(){compareData.length=0;document.querySelectorAll('.compare-btn').forEach(function(b){b.classList.remove('selected');});updateBar();});
openBtn&&openBtn.addEventListener('click',function(){buildTable();});
closeBtn&&closeBtn.addEventListener('click',function(){modal.classList.remove('open');document.body.style.overflow='';});
function buildTable(){
var table=document.getElementById('compare-table');var cols=compareData.length;
var rows=[{label:'Price',key:'price'},{label:'Surface',key:'size',unit:'m²'},{label:'Bedrooms',key:'bed'},{label:'Bathrooms',key:'bath'},{label:'Gross Yield',key:'yield',unit:'%'},{label:'Location Score',key:'score',unit:'/100'}];
var html='<div class="compare-table-grid" style="grid-template-columns:180px repeat('+cols+',1fr)">';
html+='<div class="ctg-label-cell"></div>';
compareData.forEach(function(d){html+='<div class="ctg-prop-header"><div class="ctg-prop-name">'+d.name+'</div><div class="ctg-prop-city">'+d.city+'</div></div>';});
rows.forEach(function(row){
html+='<div class="ctg-label-cell">'+row.label+'</div>';
var vals=compareData.map(function(d){return parseFloat(d[row.key])||0;});
var max=Math.max.apply(null,vals);
compareData.forEach(function(d){
var v=d[row.key];var num=parseFloat(v)||0;var hl=(num===max&&max>0)?' highlight':'';
html+='<div class="ctg-cell'+hl+'">'+v+'<span class="unit">'+(row.unit||'')+'</span></div>';
});
});
html+='</div>';table.innerHTML=html;
modal.classList.add('open');document.body.style.overflow='hidden';
gsap.to('.ctg-cell',{opacity:1,y:0,duration:.5,stagger:.04,ease:'power3.out',delay:.2});
}
}

/* ============================================================
   A07 — MORTGAGE SIMULATOR LOGIC
============================================================ */
function initMortgageSimulator(){
var ids=['mort-price','mort-down','mort-rate','mort-dur'];
if(!document.getElementById(ids[0]))return;
function fmt(n){return '€ '+Math.round(n).toLocaleString('fr-FR');}
function compute(){
var price=parseFloat(document.getElementById('mort-price').value);
var downPct=parseFloat(document.getElementById('mort-down').value)/100;
var rate=parseFloat(document.getElementById('mort-rate').value)/100/12;
var n=parseFloat(document.getElementById('mort-dur').value)*12;
var downAmt=price*downPct;var loan=price-downAmt;
var monthly=rate>0?loan*rate*Math.pow(1+rate,n)/(Math.pow(1+rate,n)-1):loan/n;
var total=monthly*n;var interest=total-loan;var capacity=monthly/0.33*12;
document.getElementById('mort-price-display').textContent=fmt(price);
document.getElementById('mort-down-display').textContent=Math.round(downPct*100)+'%';
document.getElementById('mort-down-amount').textContent=fmt(downAmt);
document.getElementById('mort-rate-display').textContent=(parseFloat(document.getElementById('mort-rate').value)).toFixed(1)+'%';
document.getElementById('mort-dur-display').textContent=document.getElementById('mort-dur').value+' years';
function setVal(id,v){var el=document.getElementById(id);if(el)el.textContent=fmt(v);}
setVal('mort-monthly',monthly);setVal('mort-total',total);setVal('mort-interest',interest);setVal('mort-capacity',capacity);setVal('mort-leg-cap',loan);setVal('mort-leg-int',interest);
var circumference=2*Math.PI*70;var capPct=loan/total;var capDash=capPct*circumference;var intDash=(1-capPct)*circumference;
gsap.to('#mort-donut-capital',{attr:{strokeDasharray:capDash+' '+circumference},duration:.6,ease:'power2.out'});
gsap.to('#mort-donut-interest',{attr:{strokeDasharray:intDash+' '+circumference,strokeDashoffset:-capDash},duration:.6,ease:'power2.out'});
}
ids.forEach(function(id){document.getElementById(id)&&document.getElementById(id).addEventListener('input',compute);});
compute();
}

/* ============================================================
   A08 — RADAR CHART LOGIC
============================================================ */
function initRadarCharts(){
document.querySelectorAll('.radar-wrap').forEach(function(wrap){
var scores=wrap.dataset.scores.split(',').map(Number);
var fillEl=wrap.querySelector('.radar-fill');
var totalEl=wrap.querySelector('.radar-total');
if(!fillEl)return;
var cx=140,cy=140,maxR=120;
var angles=[270,30,90,150,210,330].map(function(a){return a*Math.PI/180;});
function getPoints(scoresArr){
return angles.map(function(angle,i){var r=(scoresArr[i]/100)*maxR;return(cx+r*Math.cos(angle)).toFixed(1)+','+(cy+r*Math.sin(angle)).toFixed(1);}).join(' ');
}
fillEl.setAttribute('points',Array(6).fill(cx+','+cy).join(' '));
ScrollTrigger.create({trigger:wrap,start:'top 80%',onEnter:function(){
var obj={t:0};
gsap.to(obj,{t:1,duration:1.6,ease:'power3.out',onUpdate:function(){var interp=scores.map(function(s){return s*obj.t;});fillEl.setAttribute('points',getPoints(interp));}});
var avg=Math.round(scores.reduce(function(a,b){return a+b;},0)/scores.length);
if(totalEl){gsap.to({v:0},{v:avg,duration:1.6,ease:'power2.out',snap:{v:1},onUpdate:function(){totalEl.textContent=Math.floor(this.targets()[0].v);}});}
}});
});
}

/* ============================================================
   A09 — VIRTUAL TOUR LOGIC
============================================================ */
function initVirtualTour(){
var overlay=document.getElementById('vtour-overlay');
var imgEl=document.getElementById('vtour-img');
var nameEl=document.getElementById('vtour-name');
var cntEl=document.getElementById('vtour-counter');
var dotsEl=document.getElementById('vtour-dots');
var closeBtn=document.getElementById('vtour-close');
var prevBtn=document.getElementById('vtour-prev');
var nextBtn=document.getElementById('vtour-next');
var caption=document.getElementById('vtour-caption');
if(!overlay)return;
var captions=['Living Room','Master Bedroom','Kitchen','Terrace','Bathroom','View'];
var images=[],current=0;
function setImg(idx){
current=(idx+images.length)%images.length;
gsap.to(imgEl,{opacity:0,scale:1.03,duration:.4,ease:'power2.in',onComplete:function(){
imgEl.src=images[current];caption.textContent=captions[current]||'';
cntEl.textContent=(current+1)+' / '+images.length;
dotsEl.querySelectorAll('.vtour-dot').forEach(function(d,i){d.classList.toggle('active',i===current);});
gsap.fromTo(imgEl,{opacity:0,scale:1.06},{opacity:1,scale:1,duration:.9,ease:'power3.out'});
}});
}
document.querySelectorAll('.vtour-btn').forEach(function(btn){
btn.addEventListener('click',function(){
images=btn.dataset.tourImages.split('|').filter(Boolean);
if(!images.length)return;
dotsEl.innerHTML='';
images.forEach(function(_,i){var d=document.createElement('div');d.className='vtour-dot'+(i===0?' active':'');d.addEventListener('click',function(){setImg(i);});dotsEl.appendChild(d);});
nameEl.textContent=btn.dataset.tourName||'';current=-1;
overlay.classList.add('open');document.body.style.overflow='hidden';setImg(0);
});
});
closeBtn&&closeBtn.addEventListener('click',function(){gsap.to(overlay,{opacity:0,duration:.4,onComplete:function(){overlay.classList.remove('open');overlay.style.opacity='';document.body.style.overflow='';}});});
prevBtn&&prevBtn.addEventListener('click',function(){setImg(current-1);});
nextBtn&&nextBtn.addEventListener('click',function(){setImg(current+1);});
document.addEventListener('keydown',function(e){
if(!overlay.classList.contains('open'))return;
if(e.key==='ArrowRight')setImg(current+1);if(e.key==='ArrowLeft')setImg(current-1);if(e.key==='Escape')closeBtn.click();
});
}

/* ============================================================
   A10 — MARKET DATA LOGIC
============================================================ */
var marketData={
paris:{priceM2:'€ 12,400',yoy:'+4.2%',days:'18 days',yield:'3.8%',prices:[11800,11900,12000,12050,12100,12200,12250,12300,12350,12380,12400,12420]},
london:{priceM2:'£ 15,200',yoy:'+2.8%',days:'22 days',yield:'3.2%',prices:[14600,14700,14800,14850,14900,14950,15000,15050,15100,15150,15200,15220]},
athens:{priceM2:'€ 4,800',yoy:'+8.1%',days:'28 days',yield:'5.4%',prices:[4100,4200,4300,4380,4450,4500,4560,4620,4680,4730,4780,4800]},
monaco:{priceM2:'€ 48,000',yoy:'+6.5%',days:'45 days',yield:'2.1%',prices:[43000,44000,44500,45000,45500,46000,46500,47000,47200,47500,47800,48000]}
};
function updateMarketZone(zone){
var d=marketData[zone];if(!d)return;
document.getElementById('mkt-price-m2').textContent=d.priceM2;
document.getElementById('mkt-yoy').textContent=d.yoy;
document.getElementById('mkt-days').textContent=d.days;
document.getElementById('mkt-yield').textContent=d.yield;
var W=800,H=180;var min=Math.min.apply(null,d.prices);var max=Math.max.apply(null,d.prices);
var pts=d.prices.map(function(v,i){return{x:i/(d.prices.length-1)*W,y:H-((v-min)/(max-min||1))*H*.8-H*.1};});
var linePath='M'+pts.map(function(p){return p.x.toFixed(1)+','+p.y.toFixed(1);}).join('L');
var areaPath=linePath+'L'+W+','+H+'L0,'+H+'Z';
var lineEl=document.getElementById('market-chart-line');var areaEl=document.getElementById('market-chart-area');
lineEl.setAttribute('d',linePath);areaEl.setAttribute('d',areaPath);
var len=lineEl.getTotalLength?lineEl.getTotalLength():1200;
lineEl.style.strokeDasharray=len;lineEl.style.strokeDashoffset=len;
gsap.to(lineEl,{strokeDashoffset:0,duration:1.2,ease:'power3.inOut'});
gsap.from(areaEl,{opacity:0,duration:.6,delay:.4});
}
document.querySelectorAll('.mtab').forEach(function(tab){
tab.addEventListener('click',function(){
document.querySelectorAll('.mtab').forEach(function(t){t.classList.remove('active');});
tab.classList.add('active');updateMarketZone(tab.dataset.zone);
});
});
ScrollTrigger.create({trigger:'.market-sec',start:'top 78%',onEnter:function(){updateMarketZone('paris');}});

/* ============================================================
   A11 — BOOKING WIDGET LOGIC
============================================================ */
function initBookingWidgets(){
document.querySelectorAll('.booking-widget').forEach(function(widget){
var id=widget.id.replace('booking-','');
var selectedDate=null,selectedTime=null;
var currentYear=new Date().getFullYear(),currentMonth=new Date().getMonth();
function renderCalendar(){
var grid=document.getElementById('bwcg-'+id);var label=document.getElementById('bwc-month-'+id);
if(!grid)return;
var months=['January','February','March','April','May','June','July','August','September','October','November','December'];
label.textContent=months[currentMonth]+' '+currentYear;
var firstDay=new Date(currentYear,currentMonth,1).getDay();
var daysInM=new Date(currentYear,currentMonth+1,0).getDate();
var today=new Date();var offset=(firstDay+6)%7;
grid.innerHTML='';
for(var i=0;i<offset;i++){var e=document.createElement('div');e.className='bw-cal-day empty';grid.appendChild(e);}
for(var d=1;d<=daysInM;d++){
var cell=document.createElement('div');cell.className='bw-cal-day';cell.textContent=d;
var thisDate=new Date(currentYear,currentMonth,d);
var isToday=thisDate.toDateString()===today.toDateString();
var isPast=thisDate<today&&!isToday;
var isWeekend=thisDate.getDay()===0||thisDate.getDay()===6;
if(isPast||isWeekend)cell.classList.add('past');
if(isToday)cell.classList.add('today');
if(selectedDate&&thisDate.toDateString()===selectedDate.toDateString())cell.classList.add('selected');
(function(c,td){c.addEventListener('click',function(){
if(c.classList.contains('past'))return;
selectedDate=td;grid.querySelectorAll('.bw-cal-day').forEach(function(x){x.classList.remove('selected');});
c.classList.add('selected');gsap.from(c,{scale:.8,duration:.3,ease:'back.out(3)'});checkConfirm(id);
});})(cell,thisDate);
grid.appendChild(cell);
}
}
document.getElementById('bwc-prev-'+id)&&document.getElementById('bwc-prev-'+id).addEventListener('click',function(){currentMonth--;if(currentMonth<0){currentMonth=11;currentYear--;}renderCalendar();});
document.getElementById('bwc-next-'+id)&&document.getElementById('bwc-next-'+id).addEventListener('click',function(){currentMonth++;if(currentMonth>11){currentMonth=0;currentYear++;}renderCalendar();});
widget.querySelectorAll('.bw-slot').forEach(function(slot){
slot.addEventListener('click',function(){
widget.querySelectorAll('.bw-slot').forEach(function(s){s.classList.remove('active');});
slot.classList.add('active');selectedTime=slot.dataset.time;checkConfirm(id);
});
});
function checkConfirm(id){
var confirmEl=document.getElementById('bw-confirm-'+id);var summaryEl=document.getElementById('bwcs-'+id);
if(!confirmEl||!selectedDate||!selectedTime)return;
var propName=document.getElementById('booking-'+id).dataset.prop||'Property';
var dateStr=selectedDate.toLocaleDateString('en-GB',{day:'numeric',month:'long',year:'numeric'});
summaryEl.textContent=propName+' — '+dateStr+' at '+selectedTime;
confirmEl.style.display='block';gsap.from(confirmEl,{opacity:0,y:12,duration:.4,ease:'power3.out'});
}
document.getElementById('bw-submit-'+id)&&document.getElementById('bw-submit-'+id).addEventListener('click',function(){
var email=document.getElementById('bw-email-'+id).value;
if(!email||email.indexOf('@')<0)return;
var bookings=JSON.parse(localStorage.getItem('novus_bookings')||'[]');
bookings.push({prop:document.getElementById('booking-'+id).dataset.prop,date:selectedDate?selectedDate.toISOString():'',time:selectedTime,email:email,created:new Date().toISOString()});
localStorage.setItem('novus_bookings',JSON.stringify(bookings));
document.getElementById('bw-confirm-'+id).style.display='none';
document.getElementById('bw-success-'+id).style.display='block';
gsap.from('#bw-success-'+id,{opacity:0,scale:.95,duration:.5,ease:'back.out(2)'});
});
renderCalendar();
});
}

/* ============================================================
   A12 — AGENT DASHBOARD LOGIC
============================================================ */
function initAgentDashboard(){
var dash=document.getElementById('agent-dash');
var closeBtn=document.getElementById('ad-close');
var hint=document.getElementById('dash-hint');
if(!dash)return;
var clickCount=0,clickTimer;
var logoEl=document.querySelector('.nav__logo');
logoEl&&logoEl.addEventListener('click',function(e){
e.preventDefault();clickCount++;clearTimeout(clickTimer);
clickTimer=setTimeout(function(){clickCount=0;},500);
if(clickCount>=2){clickCount=0;openDashboard();}
});
logoEl&&logoEl.addEventListener('mouseenter',function(){
gsap.to(hint,{opacity:1,duration:.3});setTimeout(function(){gsap.to(hint,{opacity:0,duration:.3});},3000);
});
closeBtn&&closeBtn.addEventListener('click',function(){
gsap.to(dash,{y:'-100%',duration:.5,ease:'power3.in',onComplete:function(){dash.classList.remove('open');}});
dash.style.transform='';
});
function openDashboard(){
dash.classList.add('open');dash.style.transform='translateY(0)';populateDashboard();
gsap.from('.ad-kpi',{opacity:0,y:20,duration:.5,stagger:.08,ease:'power3.out',delay:.3});
}
function populateDashboard(){
var props=[
{name:'Tour Lumière',city:'Paris 16e',price:'€ 18,500/mo',status:'available'},
{name:'The Meridian',city:'London Mayfair',price:'€ 22,000/mo',status:'rented'},
{name:'Villa Aurelia',city:'Athens Kifissia',price:'€ 12,500/mo',status:'available'},
{name:'Le Grand Cru',city:'Monaco',price:'€ 35,000/mo',status:'negociation'},
{name:'Loft Lumino',city:'Zürich',price:'€ 9,800/mo',status:'rented'}
];
var bookings=JSON.parse(localStorage.getItem('novus_bookings')||'[]');
var available=props.filter(function(p){return p.status==='available';}).length;
var rented=props.filter(function(p){return p.status==='rented';}).length;
var negoc=props.filter(function(p){return p.status==='negociation';}).length;
var kpisEl=document.getElementById('ad-kpis');
kpisEl.innerHTML=[
{v:props.length,l:'Total Properties'},{v:available,l:'Available'},{v:rented,l:'Rented'},{v:negoc,l:'Negotiation'},{v:bookings.length,l:'Bookings'}
].map(function(k){return '<div class="ad-kpi"><span class="ad-kpi-v">'+k.v+'</span><span class="ad-kpi-l">'+k.l+'</span></div>';}).join('');
var bookEl=document.getElementById('ad-bookings');
if(!bookings.length){bookEl.innerHTML='<div style="font-family:var(--font-m);font-size:.9rem;color:rgba(245,242,237,.3);letter-spacing:.1em">No bookings yet.</div>';}
else{bookEl.innerHTML=bookings.slice(-8).reverse().map(function(b){
var d=b.date?new Date(b.date).toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric'}):'—';
return '<div class="ad-booking-row"><span class="ad-b-prop">'+((b.prop)||'—')+'</span><span class="ad-b-date">'+d+' · '+(b.time||'')+'</span><span class="ad-b-email">'+((b.email)||'—')+'</span><span class="ad-b-status pending">Pending</span></div>';
}).join('');}
document.getElementById('ad-props').innerHTML=props.map(function(p){
return '<div class="ad-prop-row"><span class="ad-pr-name">'+p.name+'</span><span class="ad-pr-city">'+p.city+'</span><span class="ad-pr-price">'+p.price+'</span><span class="ad-pr-status '+p.status+'">'+p.status+'</span></div>';
}).join('');
}
}

// ============================================================
// INIT ALL ADD-ONS
// ============================================================
initBeforeAfter();
initAmbientVideos();
initCursorPreview();
initYieldCalculators();
initComparator();
initMortgageSimulator();
initRadarCharts();
initVirtualTour();
initBookingWidgets();
initAgentDashboard();

ScrollTrigger.create({trigger:'.mortgage-sec__title',start:'top 82%',onEnter:function(){gsap.to('.mortgage-sec__title',{opacity:1,y:0,duration:.8,ease:'power3.out'});}});
ScrollTrigger.create({trigger:'.market-sec__title',start:'top 82%',onEnter:function(){gsap.to('.market-sec__title',{opacity:1,y:0,duration:.8,ease:'power3.out'});}});
"""

# ============================================================
# NOW PATCH THE TEMPLATE
# ============================================================

print("Template size before patch:", len(tpl))

# 1. Insert addon CSS before </style>
style_end = tpl.index('</style>')
# Escape CSS for JS string: \ -> \\, ' -> \'
css_escaped = ADDON_CSS.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
tpl = tpl[:style_end] + css_escaped + tpl[style_end:]

print("After CSS injection:", len(tpl))

# 2. Insert flip section after <!-- IMG MARQUEE --> section end (before <!-- ABOUT -->)
# Actually insert after metrics section, before about
about_marker = tpl.index('<!-- ABOUT -->')
flip_escaped = FLIP_SECTION_HTML.replace('\\', '\\\\').replace("'", "\\'")
tpl = tpl[:about_marker] + flip_escaped + '\\n' + tpl[about_marker:]

print("After flip section:", len(tpl))

# 3. Add data-preview-* attributes to prop-stacked__item elements
# Find each prop-stacked__item and add attributes
prop_items = [
    ('Tour Lumière', 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600', '€ 18,500/mo'),
    ('The Meridian', 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=600', '€ 22,000/mo'),
    ('Villa Elysion', 'https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=600', '€ 12,500/mo'),
]

import re

# Find all prop-stacked__item occurrences and add data attributes
pi_count = 0
offset = 0
for match in list(re.finditer(r'class="prop-stacked__item"', tpl)):
    if pi_count >= 3:
        break
    pos = match.start() + offset
    end_pos = match.end() + offset
    name, img, price = prop_items[pi_count]
    attrs = f' data-preview-img="{img}" data-preview-name="{name}" data-preview-price="{price}"'
    # Insert before the closing "
    insert_at = end_pos - 1  # before the last "
    old = tpl[pos:end_pos]
    new = f'class="prop-stacked__item" {attrs.strip()}'
    # We need to be more careful - replace just this occurrence
    # Find the exact position
    replacement = old.replace('class="prop-stacked__item"', f'class="prop-stacked__item"{attrs}')
    tpl = tpl[:pos] + replacement + tpl[end_pos:]
    offset += len(replacement) - len(old)
    pi_count += 1

print(f"Added data-preview to {pi_count} prop items")

# 4. Insert BA slider HTML into first .psi__img-wrap
# Find first psi__img-wrap closing </div> after the img
first_img_wrap = tpl.index('class="psi__img-wrap"')
# Find the closing tag of img-wrap - look for the next </div> after the img inside
# Actually, insert before the first psi__img-wrap's closing </div>
# Let's find the img tag inside it and insert after it
img_after_wrap = tpl.index('</div>', first_img_wrap + 100)  # skip past the img-wrap div content
ba_escaped = BA_SLIDER_HTML.replace('\\', '\\\\').replace("'", "\\'")
tpl = tpl[:img_after_wrap] + ba_escaped + tpl[img_after_wrap:]

print("After BA slider:", len(tpl))

# 5. Insert yield calc, radar, compare btn, vtour btn, booking in first psi__right
# Find first psi__right section - add widgets before its closing
first_psi_right = tpl.index('class="psi__right"')
# Find the SECOND psi__right to know where first one ends
second_psi_right = tpl.index('class="psi__right"', first_psi_right + 50)
# Insert before the prop-stacked__item boundary - find the </div> that closes psi__right
# Look for </section> or next prop-stacked__item
# Actually let's find the next prop-stacked__item after first psi__right
next_prop_item = tpl.index('prop-stacked__item', first_psi_right + 50)
# Go back to find the </div> before it
# Insert the widgets just before the closing </div> of the first psi__right
# Find a unique marker near the end of first property - the yield tag or similar
# Let's find the desc div end - look for a pattern
# Simpler: insert before the second prop-stacked__item's container div
insert_before_second = tpl.rfind('</div>', first_psi_right, next_prop_item)

widgets_html = (YIELD_CALC_HTML + RADAR_HTML + COMPARE_BTN_1 + VTOUR_BTN_1 + BOOKING_HTML).replace('\\', '\\\\').replace("'", "\\'")
tpl = tpl[:insert_before_second] + widgets_html + tpl[insert_before_second:]

print("After first prop widgets:", len(tpl))

# 6. Add compare buttons to 2nd and 3rd properties
# Find 2nd psi__right
second_psi_right = tpl.index('class="psi__right"', tpl.index('class="psi__right"') + 50)
third_psi_right_search = tpl.find('class="psi__right"', second_psi_right + 50)

# For 2nd property
if third_psi_right_search > 0:
    next_boundary = tpl.find('prop-stacked__item', second_psi_right + 50)
    if next_boundary < 0:
        next_boundary = tpl.find('<!-- VIDEO', second_psi_right)
    insert_pt = tpl.rfind('</div>', second_psi_right, next_boundary)
    btn2 = COMPARE_BTN_2.replace('\\', '\\\\').replace("'", "\\'")
    tpl = tpl[:insert_pt] + btn2 + tpl[insert_pt:]

    # For 3rd property
    third_psi_right = tpl.index('class="psi__right"', second_psi_right + 50 + len(btn2))
    video_marker = tpl.index('<!-- VIDEO', third_psi_right)
    insert_pt3 = tpl.rfind('</div>', third_psi_right, video_marker)
    btn3 = COMPARE_BTN_3.replace('\\', '\\\\').replace("'", "\\'")
    tpl = tpl[:insert_pt3] + btn3 + tpl[insert_pt3:]

print("After compare buttons on props 2&3:", len(tpl))

# 7. Insert mortgage + market sections before <!-- CTA -->
cta_marker = tpl.index('<!-- CTA -->')
sections_html = (MORTGAGE_HTML + '\\n' + MARKET_HTML + '\\n').replace('\\', '\\\\').replace("'", "\\'")
# But we already have \\n in the string literal, let's be careful
# The MORTGAGE_HTML and MARKET_HTML don't have real newlines (they use \), so just escape quotes
mort_esc = MORTGAGE_HTML.replace('\\', '\\\\').replace("'", "\\'")
mkt_esc = MARKET_HTML.replace('\\', '\\\\').replace("'", "\\'")
tpl = tpl[:cta_marker] + mort_esc + mkt_esc + tpl[cta_marker:]

print("After mortgage + market sections:", len(tpl))

# 8. Insert global HTML elements before </body>
body_end = tpl.index('</body>')
global_esc = GLOBAL_HTML_BEFORE_BODY.replace('\\', '\\\\').replace("'", "\\'")
tpl = tpl[:body_end] + global_esc + tpl[body_end:]

print("After global HTML:", len(tpl))

# 9. Insert all JS before the LAST \x3c/script> before </body>
# Find the last script close before </body>
body_end = tpl.index('</body>')
last_script_close = tpl.rfind('\\x3c/script>', 0, body_end)
if last_script_close < 0:
    last_script_close = tpl.rfind('\\x3c/script', 0, body_end)

if last_script_close < 0:
    print("WARNING: Could not find script close tag!")
    # Try alternative
    last_script_close = tpl.rfind('<\\/script>', 0, body_end)
    if last_script_close < 0:
        print("ERROR: No script close found at all!")
        import sys; sys.exit(1)

# Escape JS for insertion
js_escaped = ADDON_JS.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
tpl = tpl[:last_script_close] + js_escaped + tpl[last_script_close:]

print("After JS injection:", len(tpl))

# ============================================================
# VERIFY QUOTES
# ============================================================
# Find the return '...' string
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
        problems.append(f'pos {i}: ...{s[max(0,i-20):i+20]}...')
    i += 1

if problems:
    print(f"\nQUOTE PROBLEMS ({len(problems)}):")
    for p in problems[:20]:
        print(p)
    print("ABORTING — fix quotes first!")
    import sys; sys.exit(1)

print(f"\nQuotes OK! Template size: {len(tpl)} chars")

# Write back
content = content[:tpl_start] + tpl + content[tpl_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Template 5 patched with 12 add-ons!")
