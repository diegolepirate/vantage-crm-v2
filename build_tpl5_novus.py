#!/usr/bin/env python3
"""Build NOVUS Capital Real Estate template for Forma Architects (id 5)."""

filepath = r"C:\vantage-clean\crm-v2-push\index.html"

HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NOVUS \u2014 Capital Real Estate Group</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500;1,600&family=DM+Mono:wght@300;400&family=DM+Sans:wght@300;400&display=swap" rel="stylesheet">
<style>
:root{--void:#060606;--black:#0a0908;--black-warm:#111009;--white:#f5f2ed;--cream:#e9e4db;--gold:#B8953F;--gold-bright:#D4AF5A;--gold-dim:rgba(184,149,63,0.12);--silver:#8C8C8A;--silver-light:#C4C2BE;--dark2:#131210;--dark3:#1C1A17;--dark4:#242118;--font-d:'Cormorant Garamond',serif;--font-b:'DM Sans',sans-serif;--font-m:'DM Mono',monospace;--ease-out:cubic-bezier(0.16,1,0.3,1);--ease-io:cubic-bezier(0.76,0,0.24,1);}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;}
html{font-size:62.5%;scrollbar-width:none;}html::-webkit-scrollbar{display:none;}
body{background:var(--void);color:var(--white);font-family:var(--font-b);font-size:1.6rem;font-weight:300;line-height:1.6;overflow-x:hidden;cursor:none;}
img{display:block;max-width:100%;}a{text-decoration:none;color:inherit;cursor:none;}ul{list-style:none;}

/* NOISE */
.noise{position:fixed;inset:0;z-index:9998;pointer-events:none;opacity:0.025;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");background-size:160px 160px;}

/* STOCK TICKER */
.stock-ticker{position:fixed;top:0;left:0;width:100%;z-index:101;height:3.2rem;background:var(--dark3);border-bottom:1px solid rgba(245,242,237,.06);overflow:hidden;display:flex;align-items:center;}
.stock-ticker__track{display:flex;white-space:nowrap;}
.stock-ticker__run{display:flex;align-items:center;flex-shrink:0;animation:stk-run 40s linear infinite;}
.stk-item{font-family:var(--font-m);font-size:.95rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(245,242,237,.4);padding:0 3.2rem;display:flex;align-items:center;gap:.8rem;}
.stk-price{color:rgba(245,242,237,.7);}.stk-delta{font-size:.85rem;}
.stk-up .stk-delta{color:#4ade80;}.stk-down .stk-delta{color:#f87171;}
.stk-sep{font-family:var(--font-m);font-size:.8rem;color:rgba(245,242,237,.15);padding:0 .4rem;}
@keyframes stk-run{to{transform:translateX(-100%);}}

/* PROGRESS BAR */
#pb-global{position:fixed;top:3.2rem;left:0;z-index:200;height:1px;width:0%;background:linear-gradient(to right,transparent,var(--gold),var(--gold-bright));pointer-events:none;box-shadow:0 0 12px rgba(184,149,63,.5);}

/* PAGE TRANSITION */
.pt{position:fixed;inset:0;z-index:8999;display:grid;grid-template-columns:1fr 1fr;pointer-events:none;}
.pt__left,.pt__right{background:var(--white);transform:scaleY(0);}
.pt__left{transform-origin:bottom;}.pt__right{transform-origin:top;}

/* CURSOR */
.cursor{position:fixed;top:0;left:0;z-index:9999;pointer-events:none;}
.cursor__core{position:absolute;width:5px;height:5px;background:var(--gold);border-radius:50%;transform:translate(-50%,-50%);}
.cursor__orbit{position:absolute;width:36px;height:36px;border:1px solid rgba(184,149,63,.4);border-radius:50%;transform:translate(-50%,-50%);animation:orbit-spin 4s linear infinite;}
.cursor__orbit-dot{position:absolute;top:-3px;left:50%;width:5px;height:5px;background:var(--gold);border-radius:50%;transform:translateX(-50%);}
@keyframes orbit-spin{to{transform:translate(-50%,-50%) rotate(360deg);}}
.cursor__label-wrap{position:absolute;transform:translate(16px,-50%);white-space:nowrap;}
.cursor__label{font-family:var(--font-m);font-size:.85rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);opacity:0;transition:opacity .25s;}
body.c-hover .cursor__orbit{width:56px;height:56px;border-color:rgba(184,149,63,.7);transition:width .3s,height .3s;}
body.c-view .cursor__orbit{width:80px;height:80px;background:rgba(184,149,63,.08);border-color:var(--gold);animation:none;transition:width .3s,height .3s;}
body.c-view .cursor__label{opacity:1;}
body.c-invest .cursor__orbit{width:88px;height:88px;background:var(--gold);border-color:var(--gold);animation:none;}
body.c-invest .cursor__core{background:var(--void);}body.c-invest .cursor__orbit-dot{background:var(--void);}
body.c-invest .cursor__label{opacity:1;color:var(--void);}

/* PRELOADER */
.preloader{position:fixed;inset:0;z-index:9000;background:var(--void);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2rem;}
#pre-canvas{position:absolute;inset:0;width:100%;height:100%;opacity:.15;}
.pre__content{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;gap:2rem;}
.pre__logo-row{display:flex;align-items:center;gap:1.6rem;}
.pre__logo-text-wrap{overflow:hidden;}
.pre__logo-inner{display:block;font-family:var(--font-d);font-size:4rem;font-weight:300;letter-spacing:.6em;text-transform:uppercase;transform:translateY(100%);}
.pre__sub-wrap{overflow:hidden;}
.pre__sub-inner{display:block;font-family:var(--font-m);font-size:1rem;letter-spacing:.28em;text-transform:uppercase;color:rgba(245,242,237,.35);transform:translateY(100%);}
.pre__numbers{display:flex;gap:4rem;opacity:.25;margin:.8rem 0;}
.pre__num-item{font-family:var(--font-m);font-size:1rem;letter-spacing:.12em;color:var(--gold);text-align:center;}
.pre__bar-row{display:flex;align-items:center;gap:1.6rem;}
.pre__ticker-label{font-family:var(--font-m);font-size:.9rem;letter-spacing:.15em;color:var(--gold);opacity:.6;}
.pre__bar{width:200px;height:1px;background:rgba(245,242,237,.1);position:relative;overflow:hidden;}
.pre__fill{position:absolute;top:0;left:0;height:100%;width:0;background:linear-gradient(to right,var(--gold),var(--gold-bright));}
.pre__num{font-family:var(--font-m);font-size:.9rem;letter-spacing:.2em;color:var(--silver);}

/* NAV */
.header{position:fixed;top:3.2rem;left:0;width:100%;z-index:100;transition:top .4s var(--ease-out);}
.header.hide-ticker{top:0;}
.nav{padding:2.6rem 5.6rem;display:flex;align-items:center;justify-content:space-between;transition:padding .5s var(--ease-out),background .5s;}
.nav.scrolled{padding:1.8rem 5.6rem;background:rgba(6,6,6,.92);backdrop-filter:blur(32px);border-bottom:1px solid rgba(245,242,237,.04);}
.nav__logo{display:flex;align-items:center;gap:1.2rem;font-family:var(--font-d);font-size:1.8rem;font-weight:400;letter-spacing:.4em;text-transform:uppercase;}
.nav__logo-sub{font-family:var(--font-m);font-size:.75rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(245,242,237,.3);border-left:1px solid rgba(245,242,237,.15);padding-left:1.2rem;margin-left:.4rem;}
.nav__links{display:flex;gap:4.8rem;}
.nav__links a{font-family:var(--font-m);font-size:1.1rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(245,242,237,.45);display:inline-block;transition:color .3s;position:relative;}
.nav__links a::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:1px;background:var(--gold);transition:width .4s var(--ease-out);}
.nav__links a:hover{color:var(--white);}.nav__links a:hover::after{width:100%;}
.nav__right{display:flex;align-items:center;gap:3.2rem;}
.nav__live{font-family:var(--font-m);font-size:.95rem;letter-spacing:.1em;color:rgba(245,242,237,.4);display:flex;align-items:center;gap:.8rem;}
.nav__live strong{color:var(--gold-bright);font-weight:400;}
.nav__live-dot{width:6px;height:6px;border-radius:50%;background:#4ade80;box-shadow:0 0 8px rgba(74,222,128,.6);animation:live-pulse 2s ease-in-out infinite;}
@keyframes live-pulse{0%,100%{opacity:1}50%{opacity:.3}}
.nav__btn{font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;padding:1.1rem 2.8rem;display:inline-block;border:1px solid var(--gold);color:var(--gold);transition:background .3s,color .3s;}
.nav__btn:hover{background:var(--gold);color:var(--void);}

/* HERO SPLIT */
.hero{display:grid;grid-template-columns:1fr 1fr;height:100vh;min-height:720px;margin-top:calc(3.2rem + 6.6rem);}
.hero__left{background:var(--void);position:relative;display:flex;align-items:center;padding:0 5.6rem;overflow:hidden;}
#hero-particles{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;}
.hero__left-content{position:relative;z-index:1;max-width:600px;}
.hero__eyebrow{display:flex;align-items:center;gap:1.4rem;margin-bottom:3.2rem;}
.hero__eye-line{display:block;width:32px;height:1px;background:var(--gold);}
.hero__eyebrow span:last-child{font-family:var(--font-m);font-size:1rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);}
.hero__title{font-family:var(--font-d);font-size:clamp(6rem,8.5vw,12rem);font-weight:300;line-height:.92;letter-spacing:-.02em;margin-bottom:3.6rem;}
.hero__title em{font-style:italic;color:var(--gold);}
.line{overflow:hidden;display:block;}.line-i{display:block;transform:translateY(108%);}
.hero__desc{font-size:1.5rem;color:rgba(245,242,237,.5);line-height:1.85;max-width:480px;margin-bottom:4rem;opacity:0;transform:translateY(20px);}
.hero__metrics{display:flex;align-items:center;gap:3.2rem;margin-bottom:4.8rem;opacity:0;transform:translateY(20px);}
.h-metric__v{display:block;font-family:var(--font-d);font-size:3.2rem;font-weight:300;color:var(--gold);line-height:1;margin-bottom:.4rem;}
.h-metric__l{font-family:var(--font-m);font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;color:var(--silver);line-height:1.4;}
.h-metric__sep{width:1px;height:48px;background:rgba(245,242,237,.1);}
.hero__actions{display:flex;align-items:center;gap:2.8rem;opacity:0;transform:translateY(20px);}
.hero__right{position:relative;overflow:hidden;}
.hero__right-img{position:absolute;inset:0;}
.hero__right-img img{width:100%;height:100%;object-fit:cover;}
.hero__right-overlay{position:absolute;inset:0;background:linear-gradient(to left,transparent 40%,rgba(6,6,6,.4) 100%);}
.hero__card{position:absolute;bottom:4rem;left:4rem;right:4rem;background:rgba(6,6,6,.82);backdrop-filter:blur(20px);border:1px solid rgba(245,242,237,.08);padding:2.4rem;opacity:0;transform:translateY(16px);}
.hero__card-tag{font-family:var(--font-m);font-size:.85rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);margin-bottom:1rem;}
.hero__card-name{font-family:var(--font-d);font-size:2.4rem;font-weight:300;font-style:italic;margin-bottom:1.6rem;}
.hero__card-detail{display:flex;justify-content:space-between;align-items:center;margin-bottom:2rem;font-family:var(--font-m);font-size:1rem;letter-spacing:.1em;color:var(--silver);}
.hero__card-price{color:var(--gold-bright);}
.hero__card-bar{display:flex;align-items:center;gap:1.2rem;}
.hero__card-occ{font-family:var(--font-m);font-size:.85rem;letter-spacing:.1em;color:var(--silver);}
.hero__card-bar-track{flex:1;height:2px;background:rgba(245,242,237,.1);}
.hero__card-bar-fill{height:100%;width:0%;background:var(--gold);}
.hero__card-occ-val{font-family:var(--font-m);font-size:.85rem;color:var(--gold);}
.hero__scroll{position:absolute;right:2.4rem;top:50%;transform:translateY(-50%);z-index:2;display:flex;flex-direction:column;align-items:center;gap:1.2rem;opacity:0;}
.hero__scroll span{font-family:var(--font-m);font-size:.85rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(245,242,237,.3);writing-mode:vertical-rl;}
.scroll-line{width:1px;height:80px;background:rgba(245,242,237,.15);overflow:hidden;position:relative;}
.scroll-line::after{content:'';position:absolute;top:-100%;left:0;width:100%;height:100%;background:var(--gold);animation:sline 2.4s ease-in-out infinite;}
@keyframes sline{0%{top:-100%}50%{top:0%}100%{top:100%}}

/* METRICS */
.metrics{padding:0;background:var(--dark3);}
.metrics__grid{display:grid;grid-template-columns:repeat(4,1fr);}
.metric-block{position:relative;padding:7.2rem 4rem;border-right:1px solid rgba(245,242,237,.06);overflow:hidden;opacity:0;transform:translateY(40px);}
.metric-block:last-child{border-right:none;}
.metric-block__bg{position:absolute;inset:0;background:radial-gradient(circle at 0% 100%,rgba(184,149,63,.06) 0%,transparent 60%);opacity:0;transition:opacity .5s;}
.metric-block:hover .metric-block__bg{opacity:1;}
.metric-block__val{display:block;font-family:var(--font-d);font-size:clamp(4.8rem,6vw,8rem);font-weight:300;color:var(--gold);line-height:1;margin-bottom:1.6rem;}
.metric-block__label{display:block;font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;color:var(--silver);}

/* IMG MARQUEE */
.img-marquee{padding:8rem 0;overflow:hidden;background:var(--black);}
.img-marquee__track{display:flex;white-space:nowrap;}
.img-marquee__run{display:flex;gap:2.4rem;flex-shrink:0;animation:imq-run 30s linear infinite;padding-right:2.4rem;}
.img-marquee:hover .img-marquee__run{animation-play-state:paused;}
.imq-item{position:relative;width:380px;height:260px;overflow:hidden;flex-shrink:0;}
.imq-item img{width:100%;height:100%;object-fit:cover;transition:transform .8s var(--ease-out);filter:saturate(.7) brightness(.85);}
.imq-item:hover img{transform:scale(1.06);filter:saturate(1) brightness(1);}
.imq-item span{position:absolute;bottom:1.6rem;left:1.6rem;font-family:var(--font-m);font-size:.9rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(245,242,237,.7);opacity:0;transform:translateY(8px);transition:opacity .3s,transform .3s;}
.imq-item:hover span{opacity:1;transform:translateY(0);}
@keyframes imq-run{to{transform:translateX(-100%);}}

/* ABOUT */
.about{display:grid;grid-template-columns:1fr 1fr;min-height:90vh;background:var(--black);overflow:hidden;}
.about__img-col{position:relative;overflow:hidden;}
.about__img-wrap{position:absolute;inset:-5% 0;}
#about-img{width:100%;height:110%;object-fit:cover;}
.about__img-data{position:absolute;bottom:4rem;right:4rem;display:flex;flex-direction:column;gap:2rem;}
.about__img-stat{background:rgba(6,6,6,.75);backdrop-filter:blur(16px);border:1px solid rgba(245,242,237,.08);padding:2rem 2.8rem;}
.about__img-stat-v{display:block;font-family:var(--font-d);font-size:3.2rem;font-weight:300;color:var(--gold);line-height:1;}
.about__img-stat-l{display:block;font-family:var(--font-m);font-size:.85rem;letter-spacing:.15em;text-transform:uppercase;color:var(--silver);margin-top:.4rem;}
.about__content{padding:10rem 7.2rem;display:flex;flex-direction:column;justify-content:center;position:relative;background:var(--black);}
.deco-num{position:absolute;top:-4rem;right:-2rem;font-family:var(--font-d);font-size:32vw;font-weight:300;line-height:1;color:transparent;-webkit-text-stroke:1px rgba(245,242,237,.03);pointer-events:none;z-index:0;user-select:none;}
.s-tag{display:inline-flex;align-items:center;gap:1.4rem;margin-bottom:3.2rem;}
.s-tag::before{content:'';width:28px;height:1px;background:var(--gold);}
.s-tag span{font-family:var(--font-m);font-size:1.1rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);}
.about__h{font-family:var(--font-d);font-size:clamp(4.4rem,5.2vw,7.6rem);font-weight:300;line-height:1;letter-spacing:-.02em;margin-bottom:3.6rem;}
.about__h em{font-style:italic;color:var(--gold);}
.rl{overflow:hidden;display:block;}.ri{display:block;transform:translateY(108%);}
.about__p{font-size:1.5rem;color:rgba(245,242,237,.5);line-height:1.9;margin-bottom:3.6rem;max-width:500px;opacity:0;transform:translateY(24px);}
.about__tags{display:flex;flex-wrap:wrap;gap:1.2rem;margin-bottom:4rem;opacity:0;}
.a-tag{font-family:var(--font-m);font-size:.9rem;letter-spacing:.14em;text-transform:uppercase;border:1px solid rgba(184,149,63,.3);color:rgba(184,149,63,.7);padding:.6rem 1.6rem;}

/* PROPERTIES STACKED */
.props-stack{background:var(--black);}
.prop-stacked__item{display:grid;grid-template-columns:1.1fr 1fr;min-height:100vh;padding:8rem 5.6rem;align-items:center;gap:8rem;border-top:1px solid rgba(245,242,237,.05);opacity:0;}
.psi__img-wrap{position:relative;height:640px;overflow:hidden;}
.psi__img{width:100%;height:100%;object-fit:cover;transition:transform .9s var(--ease-out);}
.prop-stacked__item:hover .psi__img{transform:scale(1.04);}
.psi__img-tags{position:absolute;top:2.4rem;left:2.4rem;display:flex;gap:1rem;}
.psi__type-tag{font-family:var(--font-m);font-size:.85rem;letter-spacing:.15em;text-transform:uppercase;background:var(--gold);color:var(--void);padding:.5rem 1.4rem;}
.psi__avail-tag{font-family:var(--font-m);font-size:.85rem;letter-spacing:.15em;text-transform:uppercase;padding:.5rem 1.4rem;}
.psi__avail-tag.available{background:rgba(74,222,128,.15);color:#4ade80;border:1px solid rgba(74,222,128,.3);}
.psi__avail-tag.rented{background:rgba(245,242,237,.08);color:var(--silver);border:1px solid rgba(245,242,237,.1);}
.psi__right{padding-left:2rem;}
.psi__num{font-family:var(--font-m);font-size:1rem;letter-spacing:.2em;color:var(--gold);margin-bottom:2.4rem;opacity:0;}
.psi__name{font-family:var(--font-d);font-size:clamp(4.8rem,6vw,8rem);font-weight:300;line-height:.95;letter-spacing:-.02em;margin-bottom:2rem;}
.psi__name em{font-style:italic;color:var(--gold);}
.psi__name .rl{overflow:hidden;display:block;}.psi__name .ri{display:block;transform:translateY(108%);}
.psi__loc{font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;color:var(--silver);margin-bottom:3.2rem;opacity:0;}
.psi__price-row{display:flex;align-items:baseline;gap:4rem;margin-bottom:3.2rem;padding-bottom:3.2rem;border-bottom:1px solid rgba(245,242,237,.07);opacity:0;}
.psi__price{font-family:var(--font-d);font-size:4rem;font-weight:300;color:var(--gold);}
.psi__price span{font-size:1.8rem;color:var(--silver);}
.psi__yield{font-family:var(--font-m);font-size:1.1rem;letter-spacing:.1em;color:#4ade80;}
.psi__yield span{color:var(--silver);font-size:.85rem;display:block;margin-top:.2rem;}
.psi__specs{display:flex;gap:3.2rem;margin-bottom:2.8rem;opacity:0;}
.psi__spec{display:flex;flex-direction:column;gap:.3rem;}
.psi__spec span:first-child{font-family:var(--font-d);font-size:3.2rem;font-weight:300;line-height:1;}
.psi__spec span:last-child{font-family:var(--font-m);font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;color:var(--silver);}
.psi__desc{font-size:1.4rem;color:rgba(245,242,237,.45);line-height:1.85;margin-bottom:2.8rem;opacity:0;}

/* BTN */
.btn{display:inline-flex;align-items:center;gap:1.2rem;font-family:var(--font-m);font-size:1.1rem;letter-spacing:.15em;text-transform:uppercase;cursor:none;transition:all .35s var(--ease-out);color:var(--white);}
.btn-arrow{display:inline-block;transition:transform .35s var(--ease-out);}
.btn:hover .btn-arrow{transform:translateX(5px);}
.btn--fill{color:var(--void);background:var(--gold);padding:1.7rem 3.6rem;}
.btn--fill:hover{background:var(--gold-bright);transform:translateY(-2px);box-shadow:0 16px 40px rgba(184,149,63,.2);}
.btn--ghost{color:var(--silver);border-bottom:1px solid rgba(245,242,237,.2);padding-bottom:.4rem;transition:color .3s,border-color .3s;}
.btn--ghost:hover{color:var(--gold);border-color:var(--gold);}
.btn--xl{padding:2.2rem 6rem;font-size:1.2rem;}

/* VIDEO */
.video-sec{background:var(--void);padding:0;}
.vid-wrap{position:relative;height:90vh;overflow:hidden;clip-path:inset(100% 0 0 0);}
.vid-wrap video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
.vid-overlay{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(6,6,6,.3) 0%,rgba(6,6,6,.15) 40%,rgba(6,6,6,.6) 100%);}
.vid-content{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;z-index:2;}
.vid-quote{font-family:var(--font-d);font-size:clamp(3.2rem,6vw,9rem);font-weight:300;font-style:italic;text-align:center;line-height:1.1;opacity:0;transform:translateY(40px);}
.vid-quote em{color:var(--gold);}

/* PERF */
.perf{padding:13rem 5.6rem;background:var(--dark2);overflow:hidden;position:relative;}
.container{max-width:1440px;margin:0 auto;position:relative;}
.perf__header{display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:7.2rem;}
.perf__title{font-family:var(--font-d);font-size:clamp(4rem,5vw,7.2rem);font-weight:300;line-height:1;letter-spacing:-.02em;}
.perf__title em{font-style:italic;color:var(--gold);}
.perf__title .rl{overflow:hidden;display:block;}.perf__title .ri{display:block;transform:translateY(108%);}
.perf__summary{display:flex;gap:4.8rem;}
.perf__kpi-v{display:block;font-family:var(--font-d);font-size:4.8rem;font-weight:300;color:var(--gold);line-height:1;}
.perf__kpi-l{font-family:var(--font-m);font-size:.9rem;letter-spacing:.15em;text-transform:uppercase;color:var(--silver);margin-top:.6rem;display:block;}
#perf-svg{width:100%;height:auto;display:block;}

/* CTA */
.cta{padding:18rem 5.6rem;background:var(--void);position:relative;overflow:hidden;text-align:center;}
.cta::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 60% 50% at 50% 100%,rgba(184,149,63,.06) 0%,transparent 70%);pointer-events:none;}
.cta__sub{font-family:var(--font-m);font-size:1.1rem;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);margin-bottom:4rem;opacity:0;}
.cta__title{font-family:var(--font-d);font-size:clamp(5.6rem,11vw,15.5rem);font-weight:300;line-height:.9;letter-spacing:-.025em;margin-bottom:4rem;}
.cta__title .line{overflow:hidden;display:block;}.cta__title .line-i{display:block;transform:translateY(108%);}
.cta__title em{font-style:italic;color:var(--gold);}
.cta__desc{font-size:1.5rem;color:rgba(245,242,237,.4);max-width:560px;margin:0 auto 5.6rem;line-height:1.8;opacity:0;}
.cta__actions{display:flex;align-items:center;justify-content:center;gap:3.2rem;opacity:0;margin-bottom:6rem;}
.cta__disclaimer{font-family:var(--font-m);font-size:.85rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(245,242,237,.2);opacity:0;}

/* FOOTER */
.footer{background:var(--void);border-top:1px solid rgba(245,242,237,.05);padding:8rem 5.6rem 4rem;}
.footer__main{display:grid;grid-template-columns:1.5fr repeat(4,1fr);gap:6rem;margin-bottom:6rem;padding-bottom:6rem;border-bottom:1px solid rgba(245,242,237,.05);}
.footer__logo{display:flex;align-items:center;gap:1.2rem;font-family:var(--font-d);font-size:2rem;font-weight:400;letter-spacing:.4em;text-transform:uppercase;margin-bottom:1.6rem;}
.footer__desc{font-family:var(--font-m);font-size:.9rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(245,242,237,.3);line-height:1.8;margin-bottom:2.4rem;}
.footer__stock{display:flex;align-items:center;gap:1.2rem;font-family:var(--font-m);font-size:.95rem;letter-spacing:.1em;}
.footer__stock-ticker{color:var(--silver);}.footer__stock-price{color:var(--gold);}.footer__stock-delta{color:#4ade80;font-size:.85rem;}
.fcol-title{font-family:var(--font-m);font-size:.9rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);display:block;margin-bottom:2.4rem;}
.footer__col ul{display:flex;flex-direction:column;gap:1.2rem;}
.footer__col a{font-family:var(--font-b);font-size:1.3rem;font-weight:300;color:rgba(245,242,237,.35);transition:color .3s;}
.footer__col a:hover{color:var(--white);}
.footer__legal{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:2rem;margin-bottom:2.4rem;}
.footer__legal span{font-family:var(--font-m);font-size:.8rem;letter-spacing:.08em;color:rgba(245,242,237,.2);}
.footer__legal-links{display:flex;gap:2.4rem;}
.footer__legal-links a{font-family:var(--font-m);font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(245,242,237,.25);transition:color .3s;}
.footer__legal-links a:hover{color:var(--silver);}
.footer__disclaimer{font-family:var(--font-m);font-size:.8rem;letter-spacing:.06em;color:rgba(245,242,237,.15);line-height:1.7;max-width:900px;padding-top:2.4rem;border-top:1px solid rgba(245,242,237,.04);}

/* RESPONSIVE */
@media(max-width:1024px){.hero{grid-template-columns:1fr;height:auto;}.hero__left{min-height:80vh;}.hero__right{height:60vh;}.about{grid-template-columns:1fr;}.about__img-col{height:50vh;position:relative;}.about__img-wrap{position:relative;inset:auto;height:100%;}.about__content{padding:6rem 4rem;}.prop-stacked__item{grid-template-columns:1fr;gap:4rem;}.psi__img-wrap{height:400px;}.metrics__grid{grid-template-columns:repeat(2,1fr);}.footer__main{grid-template-columns:1fr 1fr;gap:4rem;}}
@media(max-width:768px){html{font-size:54%;}.nav{padding:2.2rem 2.4rem;}.nav__links,.nav__live{display:none;}.hero{margin-top:6rem;}.hero__left{padding:0 2.4rem;min-height:60vh;}.metrics__grid{grid-template-columns:1fr;}.prop-stacked__item{padding:4rem 2.4rem;min-height:auto;}.psi__img-wrap{height:300px;}.footer__main{grid-template-columns:1fr;}.footer__legal{flex-direction:column;text-align:center;}.cursor{display:none;}body{cursor:auto;}#hero-particles{display:none;}.perf{padding:8rem 2.4rem;}.cta{padding:10rem 2.4rem;}}
</style>
</head>
<body>

<div class="noise"></div>
<div id="pb-global"></div>
<div class="pt" id="pt"><div class="pt__left"></div><div class="pt__right"></div></div>
<div class="cursor" id="cursor"><div class="cursor__core"></div><div class="cursor__orbit"><div class="cursor__orbit-dot"></div></div><div class="cursor__label-wrap"><span class="cursor__label" id="cursor-label"></span></div></div>

<!-- SVG DISTORT -->
<svg style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true"><defs><filter id="distort" x="-20%" y="-20%" width="140%" height="140%"><feTurbulence id="svg-turbulence" type="fractalNoise" baseFrequency="0 0" numOctaves="2" result="noise"/><feDisplacementMap id="svg-displacement" in="SourceGraphic" in2="noise" scale="0" xChannelSelector="R" yChannelSelector="G"/></filter></defs></svg>

<!-- STOCK TICKER -->
<div class="stock-ticker" id="stock-ticker"><div class="stock-ticker__track">
<div class="stock-ticker__run"><span class="stk-item stk-up">NVS:PAR <span class="stk-price" id="stk-nvs">\u20AC 48.72</span> <span class="stk-delta">\u25B2 +1.24%</span></span><span class="stk-sep">|</span><span class="stk-item stk-down">CAC 40 <span class="stk-price">7,842.10</span> <span class="stk-delta">\u25BC -0.31%</span></span><span class="stk-sep">|</span><span class="stk-item stk-up">EUR/USD <span class="stk-price">1.0934</span> <span class="stk-delta">\u25B2 +0.08%</span></span><span class="stk-sep">|</span><span class="stk-item">AUM <span class="stk-price">\u20AC 4.2B</span></span><span class="stk-sep">|</span><span class="stk-item stk-up">REIT INDEX <span class="stk-price">412.88</span> <span class="stk-delta">\u25B2 +0.55%</span></span><span class="stk-sep">|</span><span class="stk-item">LAST UPDATE <span class="stk-price" id="stk-time">\u2014</span></span></div>
<div class="stock-ticker__run" aria-hidden="true"><span class="stk-item stk-up">NVS:PAR <span class="stk-price">\u20AC 48.72</span> <span class="stk-delta">\u25B2 +1.24%</span></span><span class="stk-sep">|</span><span class="stk-item stk-down">CAC 40 <span class="stk-price">7,842.10</span> <span class="stk-delta">\u25BC -0.31%</span></span><span class="stk-sep">|</span><span class="stk-item stk-up">EUR/USD <span class="stk-price">1.0934</span> <span class="stk-delta">\u25B2 +0.08%</span></span><span class="stk-sep">|</span><span class="stk-item">AUM <span class="stk-price">\u20AC 4.2B</span></span><span class="stk-sep">|</span><span class="stk-item stk-up">REIT INDEX <span class="stk-price">412.88</span> <span class="stk-delta">\u25B2 +0.55%</span></span><span class="stk-sep">|</span><span class="stk-item">LAST UPDATE <span class="stk-price">\u2014</span></span></div>
</div></div>

<!-- PRELOADER -->
<div class="preloader" id="preloader"><canvas id="pre-canvas"></canvas><div class="pre__content"><div class="pre__logo-row"><div class="pre__logo-mark"><svg width="32" height="32" viewBox="0 0 32 32"><polygon points="16,2 30,28 2,28" fill="none" stroke="var(--gold)" stroke-width="1"/><polygon points="16,10 24,26 8,26" fill="var(--gold)" opacity=".15"/></svg></div><div class="pre__logo-text-wrap"><span class="pre__logo-inner">NOVUS</span></div></div><div class="pre__sub-wrap"><span class="pre__sub-inner">Capital Real Estate Group</span></div><div class="pre__numbers" id="pre-numbers"></div><div class="pre__bar-row"><span class="pre__ticker-label">NVS:PAR</span><div class="pre__bar"><div class="pre__fill" id="pre-fill"></div></div><span class="pre__num" id="pre-num">0%</span></div></div></div>

<!-- NAV -->
<header class="header" id="header"><nav class="nav" id="nav"><a href="#" class="nav__logo"><svg width="24" height="24" viewBox="0 0 32 32"><polygon points="16,2 30,28 2,28" fill="none" stroke="var(--gold)" stroke-width="1.5"/><polygon points="16,10 24,26 8,26" fill="var(--gold)" opacity=".2"/></svg><span>NOVUS</span><span class="nav__logo-sub">Capital Real Estate</span></a><ul class="nav__links"><li><a href="#about" class="mag-link">Group</a></li><li><a href="#properties" class="mag-link">Portfolio</a></li><li><a href="#performance" class="mag-link">Investors</a></li><li><a href="#contact" class="mag-link">Contact</a></li></ul><div class="nav__right"><span class="nav__live"><span class="nav__live-dot"></span>NVS:PAR <strong>\u20AC 48.72</strong></span><a href="#contact" class="nav__btn mag-btn">Invest Now</a></div></nav></header>

<!-- HERO -->
<section class="hero" id="hero"><div class="hero__left"><canvas id="hero-particles"></canvas><div class="hero__left-content"><div class="hero__eyebrow"><span class="hero__eye-line"></span><span>Listed \u00B7 Euronext Paris \u00B7 NVS:PAR</span></div><h1 class="hero__title" id="hero-h"><span class="line"><span class="line-i" id="ht-1">Capital.</span></span><span class="line"><span class="line-i" id="ht-2"><em>Architecture.</em></span></span><span class="line"><span class="line-i" id="ht-3">Legacy.</span></span></h1><p class="hero__desc" id="hero-desc">A publicly listed real estate group managing \u20AC4.2 billion in prime assets across Europe\u2019s most sought-after locations.</p><div class="hero__metrics" id="hero-metrics"><div class="h-metric"><span class="h-metric__v">\u20AC4.2B</span><span class="h-metric__l">Assets Under<br>Management</span></div><div class="h-metric__sep"></div><div class="h-metric"><span class="h-metric__v">12,400</span><span class="h-metric__l">Properties<br>Managed</span></div><div class="h-metric__sep"></div><div class="h-metric"><span class="h-metric__v">27</span><span class="h-metric__l">Years of<br>Excellence</span></div></div><div class="hero__actions" id="hero-act"><a href="#properties" class="btn btn--fill mag-btn">Explore Portfolio</a><a href="#performance" class="btn btn--ghost">Investor Relations \u2192</a></div></div></div><div class="hero__right" id="hero-right"><div class="hero__right-img"><img id="hero-img" src="https://images.unsplash.com/photo-1486325212027-8081e485255e?w=1600&q=92&auto=format&fit=crop" alt="NOVUS flagship"></div><div class="hero__right-overlay"></div><div class="hero__card" id="hero-card"><div class="hero__card-tag">Featured Property</div><div class="hero__card-name">Tour Lumi\u00E8re, Paris 16e</div><div class="hero__card-detail"><span>Penthouse \u00B7 340m\u00B2</span><span class="hero__card-price">\u20AC 18,500 / mo</span></div><div class="hero__card-bar"><span class="hero__card-occ">Occupancy</span><div class="hero__card-bar-track"><div class="hero__card-bar-fill" id="h-card-fill"></div></div><span class="hero__card-occ-val">98.4%</span></div></div><div class="hero__scroll" id="hero-scroll"><div class="scroll-line"></div><span>Scroll</span></div></div></section>

<!-- METRICS -->
<section class="metrics" id="metrics"><div class="metrics__grid"><div class="metric-block" data-target="4.2" data-suffix="B\u20AC"><div class="metric-block__bg"></div><span class="metric-block__val">0</span><span class="metric-block__label">Assets Under Management</span></div><div class="metric-block" data-target="12400" data-suffix="+"><div class="metric-block__bg"></div><span class="metric-block__val">0</span><span class="metric-block__label">Properties Managed</span></div><div class="metric-block" data-target="98.4" data-suffix="%"><div class="metric-block__bg"></div><span class="metric-block__val">0</span><span class="metric-block__label">Average Occupancy</span></div><div class="metric-block" data-target="27" data-suffix=""><div class="metric-block__bg"></div><span class="metric-block__val">0</span><span class="metric-block__label">Years of Leadership</span></div></div></section>

<!-- IMG MARQUEE -->
<div class="img-marquee" id="img-marquee"><div class="img-marquee__track"><div class="img-marquee__run"><div class="imq-item"><img src="https://images.unsplash.com/photo-1574362848149-11496d93a7c7?w=760&q=88&auto=format&fit=crop" alt=""><span>Paris 16e</span></div><div class="imq-item"><img src="https://images.unsplash.com/photo-1560184897-ae75f418493e?w=760&q=88&auto=format&fit=crop" alt=""><span>London Mayfair</span></div><div class="imq-item"><img src="https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=760&q=88&auto=format&fit=crop" alt=""><span>Monaco</span></div><div class="imq-item"><img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=760&q=88&auto=format&fit=crop" alt=""><span>Athens Kifissia</span></div><div class="imq-item"><img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=760&q=88&auto=format&fit=crop" alt=""><span>C\u00F4te d\u2019Azur</span></div><div class="imq-item"><img src="https://images.unsplash.com/photo-1486325212027-8081e485255e?w=760&q=88&auto=format&fit=crop" alt=""><span>Zurich</span></div></div><div class="img-marquee__run" aria-hidden="true"><div class="imq-item"><img src="https://images.unsplash.com/photo-1574362848149-11496d93a7c7?w=760&q=88&auto=format&fit=crop" alt=""><span>Paris 16e</span></div><div class="imq-item"><img src="https://images.unsplash.com/photo-1560184897-ae75f418493e?w=760&q=88&auto=format&fit=crop" alt=""><span>London Mayfair</span></div><div class="imq-item"><img src="https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=760&q=88&auto=format&fit=crop" alt=""><span>Monaco</span></div><div class="imq-item"><img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=760&q=88&auto=format&fit=crop" alt=""><span>Athens Kifissia</span></div><div class="imq-item"><img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=760&q=88&auto=format&fit=crop" alt=""><span>C\u00F4te d\u2019Azur</span></div><div class="imq-item"><img src="https://images.unsplash.com/photo-1486325212027-8081e485255e?w=760&q=88&auto=format&fit=crop" alt=""><span>Zurich</span></div></div></div></div>

<!-- ABOUT -->
<section class="about" id="about"><div class="about__img-col"><div class="about__img-wrap" id="about-img-wrap"><img id="about-img" src="https://images.unsplash.com/photo-1497366216548-37526070297c?w=1400&q=90&auto=format&fit=crop" alt="NOVUS HQ"><div class="about__img-data"><div class="about__img-stat"><span data-target="4.2" data-suffix="B\u20AC" class="about__img-stat-v">0</span><span class="about__img-stat-l">AUM</span></div><div class="about__img-stat"><span data-target="27" data-suffix="yrs" class="about__img-stat-v">0</span><span class="about__img-stat-l">Experience</span></div></div></div></div><div class="about__content"><div class="deco-num" id="deco-about">01</div><div class="s-tag"><span>About the Group</span></div><h2 class="about__h" id="about-h"><span class="rl"><span class="ri">Building</span></span><span class="rl"><span class="ri">Wealth Through</span></span><span class="rl"><span class="ri"><em>Real Assets.</em></span></span></h2><p class="about__p" id="about-p">Founded in 1998, NOVUS Capital Real Estate Group has grown from a boutique advisory firm to one of Europe\u2019s leading publicly listed real estate groups. We combine institutional-grade investment discipline with a curated approach to property selection.</p><div class="about__tags" id="about-tags"><span class="a-tag">Euronext Listed</span><span class="a-tag">ESG Committed</span><span class="a-tag">SIIC Certified</span><span class="a-tag">INREV Member</span></div><a href="#performance" class="btn btn--fill mag-btn">View Investor Relations</a></div></section>

<!-- PROPERTIES STACKED -->
<section class="props-stack" id="properties"><div class="s-tag" style="padding:8rem 5.6rem 0;"><span>Property Portfolio</span></div>
<div class="prop-stacked__item"><div class="psi__left"><div class="psi__img-wrap"><img class="psi__img" src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=90&auto=format&fit=crop" alt="Tour Lumi\u00E8re"><div class="psi__img-tags"><span class="psi__type-tag">Penthouse</span><span class="psi__avail-tag available">Available</span></div></div></div><div class="psi__right"><div class="psi__num">01 / 03</div><h3 class="psi__name"><span class="rl"><span class="ri">Tour</span></span><span class="rl"><span class="ri"><em>Lumi\u00E8re</em></span></span></h3><div class="psi__loc">Paris 16e, France</div><div class="psi__price-row"><div class="psi__price">\u20AC 18,500 <span>/mo</span></div><div class="psi__yield">4.8% <span>gross yield</span></div></div><div class="psi__specs"><div class="psi__spec"><span>340</span><span>m\u00B2</span></div><div class="psi__spec"><span>4</span><span>Bedrooms</span></div><div class="psi__spec"><span>3</span><span>Bathrooms</span></div><div class="psi__spec"><span>2</span><span>Parking</span></div></div><p class="psi__desc">An architectural masterpiece on the 22nd floor, offering panoramic views of the Eiffel Tower and La D\u00E9fense skyline.</p><a href="#contact" class="btn btn--fill mag-btn">Request a Viewing</a></div></div>
<div class="prop-stacked__item"><div class="psi__left"><div class="psi__img-wrap"><img class="psi__img" src="https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=1200&q=90&auto=format&fit=crop" alt="The Meridian"><div class="psi__img-tags"><span class="psi__type-tag">Villa</span><span class="psi__avail-tag available">Available</span></div></div></div><div class="psi__right"><div class="psi__num">02 / 03</div><h3 class="psi__name"><span class="rl"><span class="ri">The</span></span><span class="rl"><span class="ri"><em>Meridian</em></span></span></h3><div class="psi__loc">London, Mayfair</div><div class="psi__price-row"><div class="psi__price">\u00A3 32,000 <span>/mo</span></div><div class="psi__yield">3.9% <span>gross yield</span></div></div><div class="psi__specs"><div class="psi__spec"><span>520</span><span>m\u00B2</span></div><div class="psi__spec"><span>6</span><span>Bedrooms</span></div><div class="psi__spec"><span>5</span><span>Bathrooms</span></div><div class="psi__spec"><span>3</span><span>Parking</span></div></div><p class="psi__desc">A Georgian townhouse meticulously restored to its original grandeur, steps from Hyde Park and Grosvenor Square.</p><a href="#contact" class="btn btn--fill mag-btn">Request a Viewing</a></div></div>
<div class="prop-stacked__item"><div class="psi__left"><div class="psi__img-wrap"><img class="psi__img" src="https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1200&q=90&auto=format&fit=crop" alt="Villa Elysion"><div class="psi__img-tags"><span class="psi__type-tag">Villa</span><span class="psi__avail-tag rented">Rented</span></div></div></div><div class="psi__right"><div class="psi__num">03 / 03</div><h3 class="psi__name"><span class="rl"><span class="ri">Villa</span></span><span class="rl"><span class="ri"><em>Elysion</em></span></span></h3><div class="psi__loc">Athens, Kifissia</div><div class="psi__price-row"><div class="psi__price">\u20AC 8,200 <span>/mo</span></div><div class="psi__yield">5.6% <span>gross yield</span></div></div><div class="psi__specs"><div class="psi__spec"><span>640</span><span>m\u00B2</span></div><div class="psi__spec"><span>5</span><span>Bedrooms</span></div><div class="psi__spec"><span>4</span><span>Bathrooms</span></div><div class="psi__spec"><span>2</span><span>Pool</span></div></div><p class="psi__desc">A modernist villa with infinity pool overlooking the Saronic Gulf, designed by award-winning Greek architects.</p><a href="#contact" class="btn btn--fill mag-btn">Request a Viewing</a></div></div>
</section>

<!-- VIDEO -->
<div class="video-sec" id="video-sec"><div class="vid-wrap" id="vid-wrap"><video autoplay muted loop playsinline preload="auto"><source src="https://videos.pexels.com/video-files/3129671/3129671-uhd_2560_1440_30fps.mp4" type="video/mp4"></video><div class="vid-overlay"></div><div class="vid-content"><p class="vid-quote" id="vid-quote">\u201CWe don\u2019t just manage<br>properties. We build <em>legacies.</em>\u201D</p></div></div></div>

<!-- PERFORMANCE -->
<section class="perf" id="performance"><div class="container"><div class="deco-num" id="deco-perf">03</div><div class="perf__header"><div><div class="s-tag"><span>Financial Performance</span></div><h2 class="perf__title"><span class="rl"><span class="ri">Consistent</span></span><span class="rl"><span class="ri"><em>Outperformance.</em></span></span></h2></div><div class="perf__summary"><div class="perf__kpi"><span class="perf__kpi-v" data-target="14.3" data-suffix="%">0%</span><span class="perf__kpi-l">10-Year IRR</span></div><div class="perf__kpi"><span class="perf__kpi-v" data-target="6.8" data-suffix="%">0%</span><span class="perf__kpi-l">Dividend Yield</span></div></div></div><div class="perf__chart" id="perf-chart"><svg id="perf-svg" viewBox="0 0 1200 320" preserveAspectRatio="none"><defs><linearGradient id="chart-grad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="var(--gold)" stop-opacity=".2"/><stop offset="100%" stop-color="var(--gold)" stop-opacity="0"/></linearGradient><clipPath id="chart-clip"><rect id="chart-clip-rect" x="0" y="0" width="0" height="320"/></clipPath></defs><path id="chart-area" d="M0,280 L100,240 L200,220 L300,200 L400,185 L500,165 L600,150 L700,130 L800,110 L900,90 L1000,75 L1100,55 L1200,40 L1200,320 L0,320 Z" fill="url(#chart-grad)" clip-path="url(#chart-clip)"/><path id="chart-line" d="M0,280 L100,240 L200,220 L300,200 L400,185 L500,165 L600,150 L700,130 L800,110 L900,90 L1000,75 L1100,55 L1200,40" fill="none" stroke="var(--gold)" stroke-width="2" style="stroke-dasharray:2000;stroke-dashoffset:2000"/><line x1="0" y1="319" x2="1200" y2="319" stroke="rgba(245,242,237,.1)" stroke-width="1"/><text x="0" y="310" font-size="12" fill="rgba(245,242,237,.3)" font-family="DM Mono">2015</text><text x="420" y="310" font-size="12" fill="rgba(245,242,237,.3)" font-family="DM Mono">2018</text><text x="840" y="310" font-size="12" fill="rgba(245,242,237,.3)" font-family="DM Mono">2021</text><text x="1120" y="310" font-size="12" fill="rgba(245,242,237,.3)" font-family="DM Mono">2025</text></svg></div></div></section>

<!-- CTA -->
<section class="cta" id="contact"><div class="container"><p class="cta__sub" id="cta-sub">Begin Your Investment Journey</p><h2 class="cta__title" id="cta-h"><span class="line"><span class="line-i">Your Next</span></span><span class="line"><span class="line-i">Property <em id="cta-scr">Awaits.</em></span></span></h2><p class="cta__desc" id="cta-desc">Whether you\u2019re a private tenant, institutional investor, or family office, our team delivers unmatched access to Europe\u2019s finest real estate.</p><div class="cta__actions" id="cta-act"><a href="mailto:invest@novus-capital.fr" class="btn btn--fill btn--xl mag-btn">Schedule a Call <span class="btn-arrow">\u2192</span></a><a href="#performance" class="btn btn--ghost">Investor Deck \u2192</a></div><div class="cta__disclaimer" id="cta-disc">Listed on Euronext Paris \u00B7 NVS:PAR \u00B7 SIIC \u00B7 Regulated by AMF</div></div></section>

<!-- FOOTER -->
<footer class="footer"><div class="footer__main"><div class="footer__brand"><div class="footer__logo"><svg width="20" height="20" viewBox="0 0 32 32"><polygon points="16,2 30,28 2,28" fill="none" stroke="var(--gold)" stroke-width="1.5"/><polygon points="16,10 24,26 8,26" fill="var(--gold)" opacity=".2"/></svg><span>NOVUS</span></div><p class="footer__desc">Capital Real Estate Group<br>Listed \u00B7 Euronext Paris</p><div class="footer__stock"><span class="footer__stock-ticker">NVS:PAR</span><span class="footer__stock-price">\u20AC 48.72</span><span class="footer__stock-delta">\u25B2 +1.24%</span></div></div><div class="footer__col"><span class="fcol-title">Portfolio</span><ul><li><a href="#">Residential</a></li><li><a href="#">Commercial</a></li><li><a href="#">Luxury Rental</a></li><li><a href="#">Off-Market</a></li></ul></div><div class="footer__col"><span class="fcol-title">Investors</span><ul><li><a href="#">Annual Reports</a></li><li><a href="#">Press Releases</a></li><li><a href="#">Dividend Policy</a></li><li><a href="#">ESG Report</a></li></ul></div><div class="footer__col"><span class="fcol-title">Locations</span><ul><li><a href="#">Paris</a></li><li><a href="#">London</a></li><li><a href="#">Athens</a></li><li><a href="#">Monaco</a></li></ul></div><div class="footer__col"><span class="fcol-title">Contact</span><ul><li><a href="#">+33 1 00 00 00 00</a></li><li><a href="#">invest@novus-capital.fr</a></li><li><a href="#">14 Avenue George V, Paris</a></li></ul></div></div><div class="footer__legal"><span>\u00A9 2025 NOVUS Capital Real Estate Group S.A. \u00B7 NVS:PAR \u00B7 SIIC \u00B7 RCS Paris 123 456 789</span><div class="footer__legal-links"><a href="#">Prospectus</a><a href="#">Legal</a><a href="#">Privacy</a><a href="#">AMF Disclosure</a></div></div><div class="footer__disclaimer">Past performance is not a reliable indicator of future results. Investment in real estate involves risk. This website is for informational purposes only. Regulated by AMF.</div></footer>

SCRIPTTAG src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js">SCRIPTCLOSE
SCRIPTTAG src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js">SCRIPTCLOSE
SCRIPTTAG src="https://cdn.jsdelivr.net/npm/lenis@1.1.14/dist/lenis.min.js">SCRIPTCLOSE
SCRIPTTAG>
(function(){
gsap.registerPlugin(ScrollTrigger);
var lenis=new Lenis({duration:1.5,easing:function(t){return Math.min(1,1.001-Math.pow(2,-10*t));},smoothWheel:true});
lenis.on("scroll",ScrollTrigger.update);
gsap.ticker.add(function(time){lenis.raf(time*1000);});
gsap.ticker.lagSmoothing(0);

/* Progress bar */
lenis.on("scroll",function(e){var pb=document.getElementById("pb-global");if(pb&&e.limit)pb.style.width=(e.scroll/e.limit*100)+"%";});

/* Marquee direction */
lenis.on("scroll",function(e){document.querySelectorAll(".img-marquee__run").forEach(function(el){el.style.animationDirection=e.direction===-1?"reverse":"normal";});});

/* Stock time */
function updateStockTime(){var d=new Date();var h=String(d.getHours()).padStart(2,"0");var m=String(d.getMinutes()).padStart(2,"0");var s=String(d.getSeconds()).padStart(2,"0");var el=document.getElementById("stk-time");if(el)el.textContent=h+":"+m+":"+s+" CET";}
setInterval(updateStockTime,1000);updateStockTime();
/* Price fluctuation */
var basePrice=48.72;
setInterval(function(){basePrice+=(Math.random()-0.5)*0.08;basePrice=Math.max(48.5,Math.min(49.0,basePrice));var el=document.getElementById("stk-nvs");if(el)el.textContent="\\u20AC "+basePrice.toFixed(2);},3000);

/* Cursor */
var core=document.querySelector(".cursor__core");
var orbit=document.querySelector(".cursor__orbit");
var cMx=0,cMy=0,cOx=0,cOy=0;
document.addEventListener("mousemove",function(e){cMx=e.clientX;cMy=e.clientY;gsap.to(core,{x:cMx,y:cMy,duration:0.06});});
gsap.ticker.add(function(){cOx+=(cMx-cOx)*0.1;cOy+=(cMy-cOy)*0.1;gsap.set(orbit,{x:cOx,y:cOy});var lw=document.querySelector(".cursor__label-wrap");if(lw)gsap.set(lw,{x:cOx+18,y:cOy});});
document.querySelectorAll("a,button,.nav__btn").forEach(function(el){el.addEventListener("mouseenter",function(){document.body.classList.add("c-hover");});el.addEventListener("mouseleave",function(){document.body.classList.remove("c-hover");});});
document.querySelectorAll(".prop-stacked__item,.imq-item").forEach(function(el){el.addEventListener("mouseenter",function(){document.body.classList.add("c-view");});el.addEventListener("mouseleave",function(){document.body.classList.remove("c-view");});});
document.querySelectorAll(".btn--fill").forEach(function(el){el.addEventListener("mouseenter",function(){document.body.classList.add("c-invest");document.body.classList.remove("c-hover");});el.addEventListener("mouseleave",function(){document.body.classList.remove("c-invest");});});

/* Preloader */
var preCanvas=document.getElementById("pre-canvas");
if(preCanvas){var pCtx=preCanvas.getContext("2d");preCanvas.width=window.innerWidth;preCanvas.height=window.innerHeight;pCtx.strokeStyle="rgba(184,149,63,1)";pCtx.lineWidth=1;pCtx.beginPath();var py=preCanvas.height*.5;pCtx.moveTo(0,py);for(var px=0;px<preCanvas.width;px+=4){py+=(Math.random()-.48)*8;py=Math.max(preCanvas.height*.2,Math.min(preCanvas.height*.8,py));pCtx.lineTo(px,py);}pCtx.stroke();}
gsap.to(".pre__logo-inner",{y:"0%",duration:.9,ease:"power3.out",delay:.2});
gsap.to(".pre__sub-inner",{y:"0%",duration:.7,ease:"power3.out",delay:.5});
var preNums=document.getElementById("pre-numbers");
var pnData=[["\\u20AC 4.2B","AUM"],["12,400+","Properties"],["\\u20AC 48.72","NVS:PAR"],["98.4%","Occupation"],["27 ans","Expertise"]];
pnData.forEach(function(d){var div=document.createElement("div");div.className="pre__num-item";div.innerHTML="<div style=\\"font-size:1.6rem;color:var(--gold);font-family:var(--font-d)\\">"+d[0]+"</div><div style=\\"font-size:.8rem;letter-spacing:.15em;opacity:.5;margin-top:.3rem\\">"+d[1]+"</div>";preNums.appendChild(div);});
gsap.from(".pre__num-item",{opacity:0,y:12,duration:.5,stagger:.1,delay:.8});
var prog=0;var tick=setInterval(function(){prog+=Math.random()*11;if(prog>100){prog=100;clearInterval(tick);setTimeout(closePreloader,400);}document.getElementById("pre-fill").style.width=prog+"%";document.getElementById("pre-num").textContent=Math.floor(prog)+"%";},60);

function closePreloader(){gsap.to("#preloader",{opacity:0,duration:.9,ease:"power2.inOut",onComplete:function(){document.getElementById("preloader").style.display="none";initHero();}});}

/* Scramble */
function scrambleText(el,dur){dur=dur||1200;var chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*";var final2=el.textContent.trim();var total=final2.length;var start=performance.now();function tk(now){var p=Math.min((now-start)/dur,1);var rev=Math.floor(p*total);var r="";for(var i=0;i<total;i++){if(final2[i]===" "){r+=" ";continue;}r+=i<rev?final2[i]:chars[Math.floor(Math.random()*chars.length)];}el.textContent=r;if(p<1)requestAnimationFrame(tk);else el.textContent=final2;}requestAnimationFrame(tk);}

/* Hero particles WebGL */
function initHeroParticles(){var canvas=document.getElementById("hero-particles");if(!canvas)return;var gl=canvas.getContext("webgl");if(!gl)return;function resize(){var rect=canvas.parentElement.getBoundingClientRect();canvas.width=rect.width;canvas.height=rect.height;gl.viewport(0,0,canvas.width,canvas.height);}resize();window.addEventListener("resize",resize);var VERT="attribute vec2 a_pos;attribute float a_size;attribute float a_alpha;uniform vec2 u_mouse;uniform float u_time;varying float v_alpha;void main(){vec2 pos=a_pos;vec2 diff=pos-u_mouse;float dist=length(diff);float force=max(0.0,1.0-dist/0.3)*0.07;pos+=normalize(diff+vec2(0.0001))*force;pos.x+=sin(u_time*0.4+a_pos.y*9.0)*0.005;pos.y+=cos(u_time*0.35+a_pos.x*9.0)*0.005;gl_Position=vec4(pos,0.0,1.0);gl_PointSize=a_size;v_alpha=a_alpha;}";var FRAG="precision mediump float;uniform vec3 u_color;varying float v_alpha;void main(){vec2 c=gl_PointCoord-0.5;float d=length(c);if(d>0.5)discard;gl_FragColor=vec4(u_color,(1.0-d*2.0)*v_alpha);}";function compile(type,src){var s=gl.createShader(type);gl.shaderSource(s,src);gl.compileShader(s);return s;}var prg=gl.createProgram();gl.attachShader(prg,compile(gl.VERTEX_SHADER,VERT));gl.attachShader(prg,compile(gl.FRAGMENT_SHADER,FRAG));gl.linkProgram(prg);gl.useProgram(prg);var N=160,pos=new Float32Array(N*2),sz=new Float32Array(N),alp=new Float32Array(N);for(var i=0;i<N;i++){pos[i*2]=Math.random()*2-1;pos[i*2+1]=Math.random()*2-1;sz[i]=Math.random()*2.5+.5;alp[i]=Math.random()*.4+.08;}function mkBuf(d){var b=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,b);gl.bufferData(gl.ARRAY_BUFFER,d,gl.DYNAMIC_DRAW);return b;}var bPos=mkBuf(pos),bSz=mkBuf(sz),bAlp=mkBuf(alp);var aPos=gl.getAttribLocation(prg,"a_pos"),aSz=gl.getAttribLocation(prg,"a_size"),aAlp=gl.getAttribLocation(prg,"a_alpha");var uMse=gl.getUniformLocation(prg,"u_mouse"),uTim=gl.getUniformLocation(prg,"u_time"),uCol=gl.getUniformLocation(prg,"u_color");gl.enable(gl.BLEND);gl.blendFunc(gl.SRC_ALPHA,gl.ONE_MINUS_SRC_ALPHA);var mx2=-2,my2=-2;window.addEventListener("mousemove",function(e){var r=canvas.getBoundingClientRect();mx2=((e.clientX-r.left)/r.width)*2-1;my2=-(((e.clientY-r.top)/r.height)*2-1);});function render(t){gl.clearColor(0,0,0,0);gl.clear(gl.COLOR_BUFFER_BIT);gl.uniform2f(uMse,mx2,my2);gl.uniform1f(uTim,t*.001);gl.uniform3f(uCol,184/255,149/255,63/255);gl.bindBuffer(gl.ARRAY_BUFFER,bPos);gl.enableVertexAttribArray(aPos);gl.vertexAttribPointer(aPos,2,gl.FLOAT,false,0,0);gl.bindBuffer(gl.ARRAY_BUFFER,bSz);gl.enableVertexAttribArray(aSz);gl.vertexAttribPointer(aSz,1,gl.FLOAT,false,0,0);gl.bindBuffer(gl.ARRAY_BUFFER,bAlp);gl.enableVertexAttribArray(aAlp);gl.vertexAttribPointer(aAlp,1,gl.FLOAT,false,0,0);gl.drawArrays(gl.POINTS,0,N);requestAnimationFrame(render);}requestAnimationFrame(render);}

/* Hero entrance */
function initHero(){initHeroParticles();var tl=gsap.timeline({defaults:{ease:"power4.out"}});tl.from("#hero-img",{scale:1.08,duration:2.4,ease:"power2.out"},0);tl.to(".hero__title .line-i",{y:"0%",duration:1.3,stagger:.1},.2);tl.from(".hero__eyebrow",{opacity:0,x:-20,duration:.8},.4);tl.to("#hero-desc",{opacity:1,y:0,duration:.8},.9);tl.to("#hero-metrics",{opacity:1,y:0,duration:.8,delay:.1},.9);tl.to("#hero-act",{opacity:1,y:0,duration:.8,delay:.2},.9);tl.to("#hero-card",{opacity:1,y:0,duration:.7},1.2);tl.to("#hero-scroll",{opacity:1,duration:.5},1.4);tl.to("#h-card-fill",{width:"98.4%",duration:1.2,ease:"power3.out"},1.3);tl.add(function(){scrambleText(document.getElementById("ht-3"),1000);initScroll();},1.5);}

/* Kinetic typo */
var heroSec=document.getElementById("hero");
if(heroSec){heroSec.addEventListener("mousemove",function(e){gsap.to("#hero-h",{rotationY:(e.clientX/window.innerWidth-0.5)*7,rotationX:-(e.clientY/window.innerHeight-0.5)*4,transformPerspective:900,duration:0.9,ease:"power2.out"});});heroSec.addEventListener("mouseleave",function(){gsap.to("#hero-h",{rotationY:0,rotationX:0,duration:1.2,ease:"power3.out"});});}

/* All ScrollTriggers */
function initScroll(){
ScrollTrigger.create({start:"top -40",onUpdate:function(s){document.getElementById("header").classList.toggle("hide-ticker",s.progress>0);document.getElementById("nav").classList.toggle("scrolled",s.progress>0);}});

/* Metrics */
ScrollTrigger.create({trigger:".metrics",start:"top 80%",onEnter:function(){gsap.to(".metric-block",{opacity:1,y:0,duration:.8,stagger:.1,ease:"power3.out"});document.querySelectorAll(".metric-block").forEach(function(el){var t=parseFloat(el.dataset.target);var s=el.dataset.suffix;var v=el.querySelector(".metric-block__val");var isF=String(t).indexOf(".")!==-1;gsap.to({val:0},{val:t,duration:2.5,ease:"power2.out",delay:.3,onUpdate:function(){var n=this.targets()[0].val;v.textContent=(isF?n.toFixed(1):Math.floor(n).toLocaleString())+s;}});});}});

/* About */
ScrollTrigger.create({trigger:"#about-h",start:"top 82%",onEnter:function(){gsap.to(".about__h .ri",{y:"0%",duration:1.25,stagger:.1,ease:"power4.out"});}});
ScrollTrigger.create({trigger:"#about-p",start:"top 82%",onEnter:function(){gsap.to("#about-p",{opacity:1,y:0,duration:.85});gsap.to("#about-tags",{opacity:1,duration:.85,delay:.2});}});
ScrollTrigger.create({trigger:".about__img-col",start:"top bottom",end:"bottom top",onUpdate:function(s){gsap.set("#about-img",{y:s.progress*-80});}});
ScrollTrigger.create({trigger:".about__img-data",start:"top 80%",onEnter:function(){document.querySelectorAll(".about__img-stat-v").forEach(function(el){var t=parseFloat(el.dataset.target),s=el.dataset.suffix;var isF=String(t).indexOf(".")!==-1;gsap.to({v:0},{v:t,duration:2,ease:"power2.out",onUpdate:function(){el.textContent=(isF?this.targets()[0].v.toFixed(1):Math.floor(this.targets()[0].v))+s;}});});}});

/* Properties */
document.querySelectorAll(".prop-stacked__item").forEach(function(item){ScrollTrigger.create({trigger:item,start:"top 80%",onEnter:function(){gsap.to(item,{opacity:1,duration:.6,ease:"power3.out"});gsap.to(item.querySelectorAll(".ri"),{y:"0%",duration:1.2,stagger:.07,ease:"power4.out"});gsap.to(item.querySelectorAll(".psi__num,.psi__loc,.psi__price-row,.psi__specs,.psi__desc"),{opacity:1,y:0,duration:.7,stagger:.07,ease:"power3.out",delay:.3});}});});

/* Video */
ScrollTrigger.create({trigger:"#video-sec",start:"top 68%",onEnter:function(){gsap.to("#vid-wrap",{clipPath:"inset(0% 0 0 0)",duration:1.6,ease:"power4.inOut"});gsap.to("#vid-quote",{opacity:1,y:0,duration:1.2,ease:"power3.out",delay:.8});}});

/* Perf chart */
ScrollTrigger.create({trigger:"#perf-chart",start:"top 75%",onEnter:function(){gsap.to("#chart-line",{strokeDashoffset:0,duration:2,ease:"power3.inOut"});gsap.to("#chart-clip-rect",{attr:{width:1200},duration:2,ease:"power3.inOut"});gsap.to(".perf__title .ri",{y:"0%",duration:1.2,stagger:.1,ease:"power4.out"});document.querySelectorAll(".perf__kpi-v").forEach(function(el){var t=parseFloat(el.dataset.target),s=el.dataset.suffix;gsap.to({v:0},{v:t,duration:2.2,ease:"power2.out",onUpdate:function(){el.textContent=this.targets()[0].v.toFixed(1)+s;}});});}});

/* CTA */
ScrollTrigger.create({trigger:"#cta-h",start:"top 76%",onEnter:function(){gsap.to("#cta-sub",{opacity:1,duration:.6});gsap.to("#cta-h .line-i",{y:"0%",duration:1.3,stagger:.12,ease:"power4.out",delay:.1});gsap.to(["#cta-desc","#cta-act","#cta-disc"],{opacity:1,duration:.8,stagger:.15,delay:.5});setTimeout(function(){var s=document.getElementById("cta-scr");if(s)scrambleText(s,900);},700);}});

ScrollTrigger.refresh();
}

/* Magnetic */
document.querySelectorAll(".mag-link,.mag-btn").forEach(function(el){el.addEventListener("mousemove",function(e){var r=el.getBoundingClientRect();gsap.to(el,{x:(e.clientX-r.left-r.width/2)*.3,y:(e.clientY-r.top-r.height/2)*.3,duration:.4,ease:"power2.out"});});el.addEventListener("mouseleave",function(){gsap.to(el,{x:0,y:0,duration:.7,ease:"elastic.out(1,.5)"});});});

/* Page transitions */
document.querySelectorAll("a[href^=\\"#\\"]").forEach(function(a){a.addEventListener("click",function(e){e.preventDefault();var target=document.querySelector(this.getAttribute("href"));if(!target)return;var tl=gsap.timeline();tl.to(".pt__left",{scaleY:1,duration:.55,ease:"power4.inOut"},0);tl.to(".pt__right",{scaleY:1,duration:.55,ease:"power4.inOut",delay:.06},0);tl.add(function(){lenis.scrollTo(target,{offset:-80,duration:0,immediate:true});});tl.to(".pt__left",{scaleY:0,duration:.55,ease:"power4.inOut",transformOrigin:"top",delay:.1});tl.to(".pt__right",{scaleY:0,duration:.55,ease:"power4.inOut",transformOrigin:"bottom",delay:.16});});});

/* Click ripple */
document.addEventListener("click",function(e){var r=document.createElement("div");r.style.cssText="position:fixed;left:"+e.clientX+"px;top:"+e.clientY+"px;width:6px;height:6px;border:1px solid var(--gold);border-radius:50%;transform:translate(-50%,-50%) scale(0);pointer-events:none;z-index:9997;";document.body.appendChild(r);gsap.to(r,{scale:9,opacity:0,duration:1,ease:"power2.out",onComplete:function(){r.remove();}});});

})();
SCRIPTCLOSE
</body>
</html>'''

# Replace script placeholders
HTML = HTML.replace('SCRIPTTAG src=', 'XSCRIPTOPEN src=')
HTML = HTML.replace('SCRIPTTAG>', 'XSCRIPTOPEN>')
HTML = HTML.replace('>SCRIPTCLOSE', '>XSCRIPTCLOSE')
HTML = HTML.replace('SCRIPTCLOSE', 'XSCRIPTCLOSE')

# Build JS string
js_str = HTML.replace('\\', '\\\\')  # escape backslashes
js_str = js_str.replace("'", "\\'")  # escape single quotes
js_str = js_str.replace('\n', '\\n') # escape newlines

# Replace script placeholders with \x3c versions
js_str = js_str.replace('XSCRIPTOPEN', '\\x3cscript')
js_str = js_str.replace('XSCRIPTCLOSE', '\\x3c/script>')

new_template = "TPL_ECOM_HTML['5'] = function () {\n  return '" + js_str + "';\n};\n\n"

# Verify quotes
ret_start = new_template.index("return '") + 8
ret_end = new_template.rindex("';")
s = new_template[ret_start:ret_end]
i = 0
problems = []
bs = chr(92)
sq = chr(39)
while i < len(s):
    if s[i] == bs:
        i += 2
        continue
    if s[i] == sq:
        ctx = s[max(0,i-30):i+30]
        problems.append(f"Unescaped quote at pos {i}: ...{ctx}...")
    i += 1

if problems:
    print("QUOTE PROBLEMS:")
    for p in problems[:10]:
        print(p)
    raise SystemExit(1)

print(f"Quote check OK! Template size: {len(new_template)} chars")

# Insert before TPL 9
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

marker = "TPL_ECOM_HTML['9']"
idx = content.index(marker)
content = content[:idx] + new_template + content[idx:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Template 5 NOVUS inserted successfully!")

# Verify no <script in the template (should all be \x3cscript)
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
start = content.index("TPL_ECOM_HTML['5']")
end = content.index("TPL_ECOM_HTML['9']")
tpl = content[start:end]
import re
bad_scripts = [m for m in re.finditer('<script', tpl)]
if bad_scripts:
    print(f"WARNING: {len(bad_scripts)} unescaped <script tags found!")
else:
    print("All script tags properly escaped!")
