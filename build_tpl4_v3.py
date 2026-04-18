#!/usr/bin/env python3
"""Build Vortex Digital V3 template with floral spring theme."""

filepath = r"C:\vantage-clean\crm-v2-push\index.html"

# The HTML template — using actual unicode chars, not escape sequences
HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vortex Digital \u2014 Design Studio</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500;1,600&family=DM+Mono:wght@300;400&display=swap" rel="stylesheet">
<style>
:root {
  --black:#0a0a0a;--white:#f0ede8;
  --accent:#e87eb2;--accent-light:#f4a7cf;--accent-dim:rgba(232,126,178,0.12);
  --mint:#5bcfb0;--mint-light:#8ae5cc;
  --sky:#6cb4ee;--sky-light:#9dcdf5;
  --lavender:#b48ede;--lavender-light:#d0b5f0;
  --peach:#f5a87a;
  --gray:#888880;--dark2:#111110;--dark3:#161614;
  --font-d:'Cormorant Garamond',serif;--font-m:'DM Mono',monospace;
  --ease-out:cubic-bezier(0.16,1,0.3,1);--ease-io:cubic-bezier(0.76,0,0.24,1);
}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;}
html{font-size:62.5%;scrollbar-width:none;}
html::-webkit-scrollbar{display:none;}
body{cursor:none;overflow-x:hidden;background:var(--black);color:var(--white);font-family:var(--font-m);}
a{text-decoration:none;color:inherit;cursor:none;}
ul{list-style:none;}

/* NOISE */
.noise{position:fixed;inset:0;z-index:9998;pointer-events:none;opacity:0.032;
background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
background-size:200px 200px;}

/* PROGRESS BAR */
#progress-bar{position:fixed;top:0;left:0;z-index:200;height:2px;width:0%;pointer-events:none;
background:linear-gradient(90deg,var(--mint),var(--sky),var(--accent),var(--lavender));
box-shadow:0 0 12px rgba(232,126,178,0.5);}

/* PAGE TRANSITION */
#pt{position:fixed;inset:0;z-index:8999;pointer-events:none;transform:scaleY(0);transform-origin:bottom;
background:linear-gradient(135deg,var(--accent),var(--lavender),var(--sky));}

/* CURSOR */
.cursor{position:fixed;top:0;left:0;z-index:9999;pointer-events:none;mix-blend-mode:difference;}
.cursor__dot{position:absolute;width:8px;height:8px;background:var(--white);border-radius:50%;transform:translate(-50%,-50%);transition:width .3s var(--ease-out),height .3s var(--ease-out);}
.cursor__ring{position:absolute;width:44px;height:44px;border:1px solid rgba(240,237,232,.45);border-radius:50%;transform:translate(-50%,-50%);transition:width .3s var(--ease-out),height .3s var(--ease-out),border-radius .3s var(--ease-out);display:flex;align-items:center;justify-content:center;}
.cursor__label{font-family:var(--font-m);font-size:.9rem;letter-spacing:.12em;text-transform:uppercase;color:var(--white);opacity:0;transition:opacity .2s;}
body.c-hover .cursor__dot{width:56px;height:56px;}
body.c-view .cursor__ring{width:80px;height:80px;}
body.c-view .cursor__label{opacity:1;}
body.c-drag .cursor__ring{width:88px;height:32px;border-radius:4px;}
body.c-drag .cursor__label{opacity:1;}
body.c-play .cursor__ring{width:80px;height:80px;background:rgba(232,126,178,.15);border-color:var(--accent);}
body.c-play .cursor__label{opacity:1;color:var(--accent);}

/* PRELOADER */
.preloader{position:fixed;inset:0;z-index:9000;background:var(--black);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2.8rem;}
.pre__logo{font-family:var(--font-d);font-size:3rem;font-weight:300;letter-spacing:.45em;text-transform:uppercase;overflow:hidden;}
.pre__logo-inner{display:block;transform:translateY(100%);}
.pre__bar{width:220px;height:1px;background:rgba(240,237,232,.12);position:relative;overflow:hidden;}
.pre__fill{position:absolute;top:0;left:0;height:100%;width:0;
background:linear-gradient(90deg,var(--mint),var(--accent));transition:width .1s linear;}
.pre__num{font-family:var(--font-m);font-size:1.1rem;letter-spacing:.2em;color:var(--gray);}

/* NAV */
.nav{position:fixed;top:0;width:100%;z-index:100;padding:2.8rem 4.8rem;display:flex;align-items:center;justify-content:space-between;transition:padding .5s var(--ease-out),background .5s;}
.nav.scrolled{padding:2rem 4.8rem;background:rgba(10,10,10,.88);backdrop-filter:blur(24px);border-bottom:1px solid rgba(240,237,232,.05);}
.nav__logo{font-family:var(--font-d);font-size:2rem;font-weight:400;letter-spacing:.32em;text-transform:uppercase;display:flex;align-items:center;gap:1.2rem;}
.nav__mark{width:26px;height:26px;border:1px solid var(--accent);transform:rotate(45deg);display:flex;align-items:center;justify-content:center;}
.nav__mark-dot{width:6px;height:6px;background:var(--accent);}
.nav__links{display:flex;gap:4.8rem;}
.nav__links a{font-family:var(--font-m);font-size:1.1rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(240,237,232,.55);transition:color .3s;position:relative;display:inline-block;}
.nav__links a::after{content:'';position:absolute;bottom:-3px;left:0;width:0;height:1px;background:var(--accent);transition:width .4s var(--ease-out);}
.nav__links a:hover{color:var(--white);}
.nav__links a:hover::after{width:100%;}

/* O5 DEPTH MULTI BUTTON */
.vb-dp-multi{padding:1.1rem 2.8rem;font-family:var(--font-m);font-size:1.1rem;font-weight:700;color:#fff;cursor:none;letter-spacing:.15em;text-transform:uppercase;
background:linear-gradient(180deg,#e87eb2,#c74b8a);border:none;border-radius:12px;
box-shadow:0 2px 0 #a83d72,0 4px 0 #933466,0 6px 0 #7e2b5a,0 8px 0 #69224e,0 10px 25px rgba(0,0,0,.35);
transition:all .1s;text-decoration:none;display:inline-flex;align-items:center;gap:1rem;}
.vb-dp-multi:active{transform:translateY(10px);box-shadow:0 0 0 #a83d72,0 0 0 #933466,0 0 0 #7e2b5a,0 0 0 #69224e;}

/* A9 SKEUOMORPHIC BUTTON */
.vb-boom-skeu{width:auto;min-width:140px;padding:1rem 2rem;border-radius:3rem;cursor:none;font-family:var(--font-m);font-weight:700;border:none;transition:.2s;font-size:1.1rem;letter-spacing:.12em;text-transform:uppercase;text-decoration:none;display:inline-flex;align-items:center;gap:.8rem;}
.vb-boom-skeu-bl{background:linear-gradient(90deg,#5bcfb0 0%,#2a9d8f 100%);
box-shadow:inset -2px 0 18px #2a9d8f,inset -14px 0 6px #5bcfb0,inset 4px 0 6px #1a7a6e;color:#d0f5eb;}
.vb-boom-skeu-bl:hover{background:linear-gradient(90deg,#8ae5cc 0%,#5bcfb0 100%);color:#fff;}
.vb-boom-skeu-bl:active{box-shadow:inset 2px 0 18px #2a9d8f,inset 14px 0 6px #5bcfb0;}

/* HERO */
.hero{height:100vh;min-height:720px;display:flex;align-items:flex-end;padding:0 4.8rem 9rem;position:relative;overflow:hidden;}
.hero__bg{position:absolute;inset:0;z-index:0;}
.hero__bg video{width:100%;height:100%;object-fit:cover;}
.hero__bg::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,0.2) 0%,rgba(10,10,10,0.05) 35%,rgba(10,10,10,0.6) 75%,rgba(10,10,10,1) 100%);}
#mesh-canvas{position:absolute;inset:0;z-index:0;width:100%;height:100%;pointer-events:none;}
#particle-canvas{position:absolute;inset:0;z-index:1;width:100%;height:100%;pointer-events:none;}
.hero__content{position:relative;z-index:2;width:100%;}
.hero__eyebrow{display:inline-flex;gap:1.4rem;align-items:center;margin-bottom:3.2rem;}
.hero__eyebrow::before{content:'';width:36px;height:1px;background:var(--accent);}
.hero__eyebrow span{font-family:var(--font-m);font-size:1.1rem;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);}
.hero__title{font-family:var(--font-d);font-size:clamp(6rem,10.5vw,15rem);font-weight:300;line-height:0.93;letter-spacing:-0.02em;}
.hero__title em{font-style:italic;color:var(--accent);}
.line{overflow:hidden;display:block;}
.line-i{display:block;transform:translateY(105%);}
.hero__bottom{display:flex;justify-content:space-between;align-items:flex-end;margin-top:4.8rem;}
.hero__desc{font-size:1.5rem;color:rgba(240,237,232,.55);max-width:340px;line-height:1.6;opacity:0;transform:translateY(20px);}
.hero__actions{opacity:0;transform:translateY(20px);display:flex;gap:2.4rem;align-items:center;}
.hero__scroll{position:absolute;right:4.8rem;bottom:4.8rem;z-index:2;display:flex;flex-direction:column;align-items:center;gap:1.2rem;opacity:0;}
.scroll-line{width:1px;height:72px;background:rgba(240,237,232,.18);overflow:hidden;position:relative;}
.scroll-line::after{content:'';position:absolute;top:-100%;left:0;width:100%;height:100%;background:var(--accent);animation:sline 2.2s ease-in-out infinite;}
@keyframes sline{0%{top:-100%;}50%{top:0;}100%{top:100%;}}
.hero__scroll span{font-family:var(--font-m);font-size:1rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(240,237,232,.45);}

/* MARQUEE */
.marquee{padding:2.2rem 0;overflow:hidden;border-top:1px solid rgba(240,237,232,.07);border-bottom:1px solid rgba(240,237,232,.07);background:var(--dark3);}
.marquee__track{display:flex;white-space:nowrap;}
.marquee__run{display:flex;flex-shrink:0;animation:mrun 22s linear infinite;}
.marquee:hover .marquee__run{animation-play-state:paused;}
.marquee__item{font-family:var(--font-d);font-size:1.5rem;font-style:italic;letter-spacing:.1em;color:rgba(240,237,232,.38);padding:0 4.8rem;display:flex;align-items:center;gap:4.8rem;}
.marquee__item::after{content:'\u2666';font-size:.7rem;font-style:normal;
background:linear-gradient(135deg,var(--mint),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
@keyframes mrun{to{transform:translateX(-100%);}}

/* ABOUT */
.about{padding:16rem 4.8rem;}
.container{max-width:1440px;margin:0 auto;position:relative;}
.about__grid{display:grid;grid-template-columns:1fr 1fr;gap:10rem;align-items:center;}
.about__h{font-family:var(--font-d);font-size:clamp(4.4rem,5.5vw,8rem);font-weight:300;line-height:1.05;margin-bottom:3.2rem;}
.about__h em{font-style:italic;color:var(--mint);}
.rl{overflow:hidden;display:block;}
.ri{display:block;transform:translateY(105%);}
.about__p{font-size:1.5rem;color:rgba(240,237,232,.55);line-height:1.7;margin-bottom:4.8rem;opacity:0;transform:translateY(20px);}
.stats{display:flex;gap:4.8rem;opacity:0;transform:translateY(20px);}
.stat{display:flex;flex-direction:column;gap:.6rem;}
.stat__n{font-family:var(--font-d);font-size:4.4rem;font-weight:300;
background:linear-gradient(135deg,var(--mint),var(--sky));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.stat__l{font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gray);}
.about__img{height:640px;overflow:hidden;position:relative;border-radius:4px;}
.about__img-inner{height:120%;position:relative;top:-10%;}
.about__img-inner img{width:100%;height:100%;object-fit:cover;}
.deco-num{position:absolute;top:-4rem;left:-2rem;font-family:var(--font-d);font-size:40vw;font-weight:300;line-height:1;color:transparent;
-webkit-text-stroke:1px rgba(240,237,232,0.04);pointer-events:none;z-index:0;user-select:none;}

/* S-TAG */
.s-tag{display:inline-flex;align-items:center;gap:1.4rem;margin-bottom:3.2rem;}
.s-tag::before{content:'';width:28px;height:1px;background:var(--accent);}
.s-tag span{font-family:var(--font-m);font-size:1.1rem;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);}

/* PARALLAX BAND */
.pb{height:72vh;overflow:hidden;display:flex;align-items:center;justify-content:center;position:relative;}
.pb__bg{position:absolute;inset:-25%;z-index:0;}
.pb__bg img{width:100%;height:100%;object-fit:cover;}
.pb__mask{position:absolute;inset:0;background:rgba(10,10,10,0.52);z-index:1;}
.pb__content{position:relative;z-index:2;text-align:center;padding:0 4.8rem;}
.pb__q{font-family:var(--font-d);font-size:clamp(3.6rem,6.5vw,9.6rem);font-weight:300;font-style:italic;opacity:0;transform:translateY(40px);}
.pb__q em{color:var(--accent);}

/* VIDEO */
.video-sec{padding:12rem 4.8rem;}
.v-wrap{height:82vh;overflow:hidden;position:relative;clip-path:inset(100% 0 0 0);border-radius:8px;}
.v-wrap video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
.v-label{position:absolute;bottom:4.8rem;left:4.8rem;z-index:2;opacity:0;}
.v-label span{font-family:var(--font-d);font-size:2rem;font-style:italic;color:rgba(240,237,232,.65);}

/* HORIZONTAL SCROLL */
.hscroll-wrap{background:var(--black);padding:0;}
.hscroll-pin{overflow:hidden;}
.hscroll{display:flex;align-items:center;gap:4rem;padding:0 4.8rem;width:max-content;will-change:transform;}
.hscroll__title{min-width:420px;padding-right:6rem;}
.hscroll__title h2{font-family:var(--font-d);font-size:clamp(4rem,5vw,7rem);font-weight:300;line-height:1.05;letter-spacing:-.02em;}
.hscroll__title em{font-style:italic;color:var(--lavender);}
.hcard{position:relative;min-width:480px;height:640px;overflow:hidden;flex-shrink:0;border-radius:8px;}
.hcard__img{width:100%;height:100%;}
.hcard__img img{width:100%;height:100%;object-fit:cover;transition:transform .8s var(--ease-out);}
.hcard:hover .hcard__img img{transform:scale(1.05);}
.hcard__info{position:absolute;bottom:0;left:0;right:0;padding:2.4rem 3.2rem;
background:linear-gradient(to top,rgba(10,10,10,.9) 0%,transparent 100%);display:flex;flex-direction:column;gap:.8rem;}
.hcard__num{font-family:var(--font-m);font-size:1rem;letter-spacing:.2em;color:var(--accent);}
.hcard__name{font-family:var(--font-d);font-size:2.8rem;font-weight:300;font-style:italic;}
.hcard__cat{font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gray);}

/* WORKS */
.works{padding:16rem 4.8rem;}
.works__hd{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:4.8rem;}
.works__title{font-family:var(--font-d);font-size:clamp(4rem,5vw,7rem);font-weight:300;}
.works__filters{display:flex;gap:1.6rem;margin-bottom:4.8rem;}
.wf{font-family:var(--font-m);font-size:1.1rem;letter-spacing:.15em;text-transform:uppercase;background:none;border:1px solid rgba(240,237,232,.12);color:var(--gray);padding:.8rem 2rem;cursor:none;transition:all .3s;}
.wf.active,.wf:hover{border-color:var(--accent);color:var(--accent);}
.works__grid{display:grid;grid-template-columns:repeat(12,1fr);gap:2rem;}
.wi{overflow:hidden;cursor:none;opacity:0;transform:translateY(60px);position:relative;transition:opacity .4s;border-radius:6px;}
.wi:nth-child(1){grid-column:1/8;height:520px;}
.wi:nth-child(2){grid-column:8/13;height:520px;}
.wi:nth-child(3){grid-column:1/5;height:380px;}
.wi:nth-child(4){grid-column:5/9;height:380px;}
.wi:nth-child(5){grid-column:9/13;height:380px;}
.wi img{width:100%;height:100%;object-fit:cover;transition:transform .8s var(--ease-out);}
.wi:hover img{transform:scale(1.06);}
.wi__ov{position:absolute;inset:0;background:rgba(10,10,10,.72);display:flex;flex-direction:column;justify-content:flex-end;padding:3.6rem;opacity:0;transition:opacity .4s;}
.wi:hover .wi__ov{opacity:1;}
.wi__cat{font-family:var(--font-m);font-size:1rem;letter-spacing:.2em;text-transform:uppercase;color:var(--mint);margin-bottom:.8rem;}
.wi__name{font-family:var(--font-d);font-size:2.8rem;font-weight:300;}

/* SERVICES */
.services{padding:16rem 4.8rem;}
.svc__list{margin-top:4.8rem;}
.svc-item{display:grid;grid-template-columns:96px 1fr auto;align-items:center;padding:3.6rem 0;border-top:1px solid rgba(255,255,255,.07);opacity:0;transform:translateY(28px);transition:border-color .3s;cursor:none;}
.svc-item:hover{border-color:rgba(232,126,178,.25);}
.svc-item__n{font-family:var(--font-m);font-size:1.2rem;color:var(--gray);letter-spacing:.1em;}
.svc-item__t{font-family:var(--font-d);font-size:clamp(2.4rem,3.2vw,4.4rem);font-weight:300;font-style:italic;transition:color .3s;}
.svc-item:hover .svc-item__t{color:var(--accent);}
.svc-item__a{font-size:2.2rem;color:var(--gray);transition:transform .35s,color .35s;}
.svc-item:hover .svc-item__a{transform:translateX(8px) rotate(-45deg);color:var(--accent);}

/* SVC IMAGE TRAIL */
#svc-trail{position:fixed;top:0;left:0;z-index:50;pointer-events:none;width:320px;height:220px;overflow:hidden;opacity:0;transform:translate(-50%,-50%);border-radius:8px;}
#svc-trail img{width:100%;height:100%;object-fit:cover;}

/* CTA */
.cta{padding:16rem 4.8rem;text-align:center;background:var(--dark3);position:relative;}
.cta::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 70% 60% at 50% 110%,rgba(232,126,178,0.07) 0%,transparent 70%);pointer-events:none;}
.cta__sub{font-family:var(--font-m);font-size:1.3rem;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);margin-bottom:3.2rem;opacity:0;}
.cta__title{font-family:var(--font-d);font-size:clamp(5.6rem,10vw,14.4rem);font-weight:300;line-height:.93;margin-bottom:2rem;}
.cta__title em{font-style:italic;color:var(--lavender);}
.cta__svg-deco{width:100%;height:6rem;display:block;margin-bottom:5.6rem;overflow:visible;}
.cta__btns{opacity:0;display:flex;gap:2.4rem;justify-content:center;align-items:center;flex-wrap:wrap;}

/* BUTTONS */
.btn{display:inline-flex;align-items:center;gap:1.2rem;font-family:var(--font-m);font-size:1.1rem;letter-spacing:.15em;text-transform:uppercase;cursor:none;transition:all .35s var(--ease-out);text-decoration:none;color:var(--white);}
.btn-arrow{display:inline-block;transition:transform .35s var(--ease-out);}
.btn:hover .btn-arrow{transform:translateX(5px);}
.btn--line{color:var(--white);border-bottom:1px solid rgba(240,237,232,.3);padding-bottom:.4rem;}
.btn--line:hover{color:var(--accent);border-color:var(--accent);}

/* FOOTER */
.footer{padding:6.4rem 4.8rem;background:var(--black);border-top:1px solid rgba(255,255,255,.05);}
.footer__in{display:flex;align-items:center;justify-content:space-between;}
.footer__logo{font-family:var(--font-d);font-size:2rem;font-weight:300;letter-spacing:.32em;text-transform:uppercase;color:var(--white);}
.footer__links{display:flex;gap:2.4rem;}
.footer__links a{font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gray);cursor:none;transition:color .3s;}
.footer__links a:hover{color:var(--accent);}
.footer__copy{font-family:var(--font-m);font-size:1rem;color:rgba(136,136,128,.45);}

/* SVG DISTORTION FILTER */
.distort-svg{position:absolute;width:0;height:0;overflow:hidden;}

/* REDUCED MOTION */
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms !important;animation-iteration-count:1 !important;transition-duration:.01ms !important;}
.line-i,.ri{transform:none !important;}.pb__q{opacity:1 !important;transform:none !important;}}

/* RESPONSIVE */
@media(max-width:1024px){
.about__grid{grid-template-columns:1fr;gap:7.2rem;}
.about__img{height:440px;}
.wi:nth-child(1),.wi:nth-child(2){grid-column:1/13;}
.wi:nth-child(3),.wi:nth-child(4),.wi:nth-child(5){grid-column:span 4;}
.hcard{min-width:380px;height:520px;}
}
@media(max-width:768px){
html{font-size:54%;}
.nav{padding:2.2rem 2.4rem;}
.nav__links{display:none;}
.hero{padding:0 2.4rem 6.4rem;}
.about,.works,.services,.cta,.video-sec{padding:8rem 2.4rem;}
.works__grid{grid-template-columns:1fr;gap:1.6rem;}
.wi{grid-column:1/-1 !important;height:280px !important;}
.footer__in{flex-direction:column;gap:3.2rem;text-align:center;}
.svc-item{grid-template-columns:60px 1fr;}
.svc-item__a{display:none;}
.cursor,.noise{display:none;}
body{cursor:auto;}
#mesh-canvas,#particle-canvas{display:none;}
.hscroll-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;}
.hcard{min-width:300px;height:400px;}
.deco-num{display:none;}
#svc-trail{display:none;}
}
</style>
</head>
<body>

<!-- NOISE -->
<div class="noise"></div>

<!-- PROGRESS BAR -->
<div id="progress-bar"></div>

<!-- PAGE TRANSITION -->
<div id="pt"></div>

<!-- CURSOR -->
<div class="cursor" id="cursor">
  <div class="cursor__dot"></div>
  <div class="cursor__ring"><span class="cursor__label"></span></div>
</div>

<!-- PRELOADER -->
<div class="preloader" id="preloader">
  <div class="pre__logo"><span class="pre__logo-inner">Vortex</span></div>
  <div class="pre__bar"><div class="pre__fill" id="pre-fill"></div></div>
  <div class="pre__num" id="pre-num">0%</div>
</div>

<!-- SVG DISTORTION -->
<svg class="distort-svg" aria-hidden="true">
  <defs>
    <filter id="distort" x="-20%" y="-20%" width="140%" height="140%">
      <feTurbulence id="turbulence" type="fractalNoise" baseFrequency="0 0" numOctaves="2" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" id="displacement" scale="0" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </defs>
</svg>

<!-- NAV -->
<nav class="nav" id="nav">
  <a href="#" class="nav__logo">
    <div class="nav__mark"><div class="nav__mark-dot"></div></div>
    Vortex
  </a>
  <ul class="nav__links">
    <li><a href="#about" class="mag-link">Studio</a></li>
    <li><a href="#works" class="mag-link">Works</a></li>
    <li><a href="#services" class="mag-link">Services</a></li>
    <li><a href="#contact" class="mag-link">Contact</a></li>
  </ul>
  <a href="#contact" class="vb-dp-multi mag-btn">Start Project</a>
</nav>

<!-- HERO -->
<section class="hero" id="hero">
  <canvas id="mesh-canvas"></canvas>
  <canvas id="particle-canvas"></canvas>
  <div class="hero__bg">
    <video autoplay muted loop playsinline preload="auto">
      <source src="assets/vortex-hero.mp4" type="video/mp4">
    </video>
  </div>
  <div class="hero__content">
    <div class="hero__eyebrow"><span>Creative Studio \u2014 2025</span></div>
    <h1 class="hero__title" id="hero-h">
      <span class="line"><span class="line-i" id="ht-1">We Craft</span></span>
      <span class="line"><span class="line-i" id="ht-2"><em>Digital</em></span></span>
      <span class="line"><span class="line-i" id="ht-3">Excellence.</span></span>
    </h1>
    <div class="hero__bottom">
      <p class="hero__desc" id="hero-desc">Award-winning digital experiences that push the boundaries of design, technology, and creative expression.</p>
      <div class="hero__actions" id="hero-act">
        <a href="#works" class="vb-dp-multi mag-btn">View Work \u2192</a>
        <a href="#about" class="vb-boom-skeu vb-boom-skeu-bl">Our Story \u2192</a>
      </div>
    </div>
  </div>
  <div class="hero__scroll" id="hero-scroll">
    <div class="scroll-line"></div>
    <span>Scroll</span>
  </div>
</section>

<!-- MARQUEE -->
<div class="marquee">
  <div class="marquee__track">
    <div class="marquee__run">
      <span class="marquee__item">Digital Direction</span><span class="marquee__item">UI/UX Design</span><span class="marquee__item">Web Development</span><span class="marquee__item">Motion Design</span><span class="marquee__item">Brand Identity</span><span class="marquee__item">Creative Strategy</span><span class="marquee__item">3D Experiences</span>
    </div>
    <div class="marquee__run" aria-hidden="true">
      <span class="marquee__item">Digital Direction</span><span class="marquee__item">UI/UX Design</span><span class="marquee__item">Web Development</span><span class="marquee__item">Motion Design</span><span class="marquee__item">Brand Identity</span><span class="marquee__item">Creative Strategy</span><span class="marquee__item">3D Experiences</span>
    </div>
  </div>
</div>

<!-- ABOUT -->
<section class="about" id="about">
  <div class="container">
    <div class="deco-num" id="deco-about">01</div>
    <div class="about__grid">
      <div class="about__content">
        <div class="s-tag"><span>About the Studio</span></div>
        <h2 class="about__h" id="about-h">
          <span class="rl"><span class="ri">Where Vision</span></span>
          <span class="rl"><span class="ri">Meets <em>Craft.</em></span></span>
        </h2>
        <p class="about__p" id="about-p">We are a collective of designers, developers, and dreamers crafting digital experiences that push boundaries. Every pixel, every interaction, every moment is designed with intention and precision.</p>
        <div class="stats" id="about-stats">
          <div class="stat"><span class="stat__n" data-target="120" data-suffix="+">0</span><span class="stat__l">Projects</span></div>
          <div class="stat"><span class="stat__n" data-target="8" data-suffix="">0</span><span class="stat__l">Awwwards</span></div>
          <div class="stat"><span class="stat__n" data-target="12" data-suffix="">0</span><span class="stat__l">Countries</span></div>
        </div>
      </div>
      <div class="about__img" id="about-img">
        <div class="about__img-inner" id="about-img-i">
          <img src="https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=1400&q=90&auto=format&fit=crop" alt="Studio">
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PARALLAX FULLBLEED -->
<div class="pb" id="pb">
  <div class="pb__bg" id="pb-bg"><img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=2200&q=90&auto=format&fit=crop" alt="Parallax"></div>
  <div class="pb__mask"></div>
  <div class="pb__content">
    <p class="pb__q" id="pb-q">\u201CWe don\u2019t make websites.<br>We craft <em>experiences.</em>\u201D</p>
  </div>
</div>

<!-- VIDEO -->
<div class="video-sec" id="vid">
  <div class="v-wrap" id="v-wrap">
    <video autoplay muted loop playsinline preload="auto">
      <source src="https://videos.pexels.com/video-files/3129671/3129671-uhd_2560_1440_30fps.mp4" type="video/mp4">
    </video>
    <div class="v-label" id="v-label"><span>Showreel \u2014 2025</span></div>
  </div>
</div>

<!-- HORIZONTAL SCROLL -->
<section class="hscroll-wrap" id="hscroll-wrap">
  <div class="hscroll-pin" id="hscroll-pin">
    <div class="hscroll" id="hscroll">
      <div class="hscroll__title">
        <div class="s-tag"><span>Featured Projects</span></div>
        <h2>Selected<br><em>Work</em></h2>
      </div>
      <div class="hcard"><div class="hcard__img"><img src="https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=960&q=85&auto=format&fit=crop" alt="Project"></div><div class="hcard__info"><span class="hcard__num">01</span><span class="hcard__name">Bloom Studio</span><span class="hcard__cat">Brand Identity</span></div></div>
      <div class="hcard"><div class="hcard__img"><img src="https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=960&q=85&auto=format&fit=crop" alt="Project"></div><div class="hcard__info"><span class="hcard__num">02</span><span class="hcard__name">Petal Works</span><span class="hcard__cat">Web Design</span></div></div>
      <div class="hcard"><div class="hcard__img"><img src="https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=960&q=85&auto=format&fit=crop" alt="Project"></div><div class="hcard__info"><span class="hcard__num">03</span><span class="hcard__name">Garden Digital</span><span class="hcard__cat">Development</span></div></div>
      <div class="hcard"><div class="hcard__img"><img src="https://images.unsplash.com/photo-1561070791-2526d30994b5?w=960&q=85&auto=format&fit=crop" alt="Project"></div><div class="hcard__info"><span class="hcard__num">04</span><span class="hcard__name">Flora Platform</span><span class="hcard__cat">Digital Product</span></div></div>
    </div>
  </div>
</section>

<!-- WORKS GRID -->
<section class="works" id="works">
  <div class="container">
    <div class="deco-num" id="deco-works">02</div>
    <div class="works__hd">
      <div>
        <div class="s-tag"><span>Selected Work</span></div>
        <h2 class="works__title" id="works-h">Our Projects</h2>
      </div>
      <a href="#" class="btn btn--line">View All <span class="btn-arrow">\u2192</span></a>
    </div>
    <div class="works__filters" id="works-filters">
      <button class="wf active" data-filter="all">All</button>
      <button class="wf" data-filter="brand">Brand</button>
      <button class="wf" data-filter="web">Web</button>
      <button class="wf" data-filter="digital">Digital</button>
    </div>
    <div class="works__grid" id="works-grid">
      <div class="wi" data-cat="brand"><img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1400&q=85&auto=format&fit=crop" alt="Work"><div class="wi__ov"><span class="wi__cat">Brand Identity</span><span class="wi__name">Fleur Studio</span></div></div>
      <div class="wi" data-cat="web"><img src="https://images.unsplash.com/photo-1547658719-da2b51169166?w=1000&q=85&auto=format&fit=crop" alt="Work"><div class="wi__ov"><span class="wi__cat">Web Design</span><span class="wi__name">Nexus Platform</span></div></div>
      <div class="wi" data-cat="digital"><img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=900&q=85&auto=format&fit=crop" alt="Work"><div class="wi__ov"><span class="wi__cat">Digital Art</span><span class="wi__name">Prism Collection</span></div></div>
      <div class="wi" data-cat="brand"><img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=900&q=85&auto=format&fit=crop" alt="Work"><div class="wi__ov"><span class="wi__cat">Brand Strategy</span><span class="wi__name">Vertex Analytics</span></div></div>
      <div class="wi" data-cat="web"><img src="https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=900&q=85&auto=format&fit=crop" alt="Work"><div class="wi__ov"><span class="wi__cat">Web Development</span><span class="wi__name">Aurora Dashboard</span></div></div>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="services" id="services">
  <div class="container">
    <div class="deco-num" id="deco-services">03</div>
    <div class="s-tag"><span>What We Do</span></div>
    <div class="svc__list">
      <div class="svc-item" data-img="https://images.unsplash.com/photo-1634942537034-2531766767d1?w=640&q=80&auto=format&fit=crop"><span class="svc-item__n">01</span><span class="svc-item__t">Brand Identity &amp; Strategy</span><span class="svc-item__a">\u2192</span></div>
      <div class="svc-item" data-img="https://images.unsplash.com/photo-1586717791821-3f44a563fa4c?w=640&q=80&auto=format&fit=crop"><span class="svc-item__n">02</span><span class="svc-item__t">UI/UX Design &amp; Prototyping</span><span class="svc-item__a">\u2192</span></div>
      <div class="svc-item" data-img="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=640&q=80&auto=format&fit=crop"><span class="svc-item__n">03</span><span class="svc-item__t">Web Development &amp; Engineering</span><span class="svc-item__a">\u2192</span></div>
      <div class="svc-item" data-img="https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?w=640&q=80&auto=format&fit=crop"><span class="svc-item__n">04</span><span class="svc-item__t">Motion Design &amp; Animation</span><span class="svc-item__a">\u2192</span></div>
      <div class="svc-item" data-img="https://images.unsplash.com/photo-1561070791-2526d30994b5?w=640&q=80&auto=format&fit=crop"><span class="svc-item__n">05</span><span class="svc-item__t">3D &amp; Immersive Experiences</span><span class="svc-item__a">\u2192</span></div>
    </div>
  </div>
</section>

<!-- SVC IMAGE TRAIL -->
<div id="svc-trail"><img id="svc-trail-img" src="" alt=""></div>

<!-- CTA -->
<section class="cta" id="contact">
  <div class="container">
    <p class="cta__sub" id="cta-sub">Ready to start?</p>
    <h2 class="cta__title" id="cta-h">
      <span class="line"><span class="line-i">Let\u2019s Build</span></span>
      <span class="line"><span class="line-i">Something <em id="cta-scramble">Iconic.</em></span></span>
    </h2>
    <svg class="cta__svg-deco" viewBox="0 0 1200 120" preserveAspectRatio="none">
      <path id="cta-line-path" d="M 0 60 Q 300 20 600 60 Q 900 100 1200 60" fill="none" stroke="url(#cta-grad)" stroke-width="1" opacity="0.6" style="stroke-dasharray:1400;stroke-dashoffset:1400;"/>
      <defs><linearGradient id="cta-grad" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#5bcfb0"/><stop offset="50%" stop-color="#e87eb2"/><stop offset="100%" stop-color="#b48ede"/></linearGradient></defs>
    </svg>
    <div class="cta__btns" id="cta-btns">
      <a href="mailto:hello@vortex.studio" class="vb-dp-multi mag-btn">Start a Project \u2192</a>
      <a href="#works" class="vb-boom-skeu vb-boom-skeu-bl">View Our Work</a>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer class="footer">
  <div class="footer__in">
    <span class="footer__logo">Vortex</span>
    <ul class="footer__links">
      <li><a href="#">Privacy</a></li>
      <li><a href="#">Instagram</a></li>
      <li><a href="#">LinkedIn</a></li>
      <li><a href="#">Dribbble</a></li>
    </ul>
    <span class="footer__copy">\u00A9 2025 Vortex Digital. All rights reserved.</span>
  </div>
</footer>

<SCRIPTTAG src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></SCRIPTCLOSE>
<SCRIPTTAG src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></SCRIPTCLOSE>
<SCRIPTTAG src="https://cdn.jsdelivr.net/npm/lenis@1.1.14/dist/lenis.min.js"></SCRIPTCLOSE>
<SCRIPTTAG>
(function(){
  gsap.registerPlugin(ScrollTrigger);

  /* LENIS */
  var lenis = new Lenis({ duration:1.5, easing:function(t){return Math.min(1,1.001-Math.pow(2,-10*t));}, smoothWheel:true });
  lenis.on("scroll", ScrollTrigger.update);
  gsap.ticker.add(function(time){ lenis.raf(time*1000); });
  gsap.ticker.lagSmoothing(0);

  /* PROGRESS BAR */
  lenis.on("scroll", function(e){
    var pbar = document.getElementById("progress-bar");
    if(pbar && e.limit) pbar.style.width = (e.scroll/e.limit*100)+"%";
  });

  /* SCROLL COLOR SHIFT */
  lenis.on("scroll", function(e){
    if(!e.limit) return;
    var p = e.scroll/e.limit;
    var r = Math.round(10 + p*5);
    var g = Math.round(10 + p*3);
    var b = Math.round(10 + p*2);
    document.body.style.background = "rgb("+r+","+g+","+b+")";
  });

  /* MARQUEE DIRECTION */
  lenis.on("scroll", function(e){
    document.querySelectorAll(".marquee__run").forEach(function(el){
      el.style.animationDirection = e.direction === -1 ? "reverse" : "normal";
    });
  });

  /* CURSOR */
  var dot = document.querySelector(".cursor__dot");
  var ring = document.querySelector(".cursor__ring");
  var rx=0,ry=0,mx=0,my=0;
  document.addEventListener("mousemove",function(e){
    mx=e.clientX; my=e.clientY;
    gsap.to(dot,{x:mx,y:my,duration:0.08});
  });
  gsap.ticker.add(function(){
    rx+=(mx-rx)*0.11; ry+=(my-ry)*0.11;
    gsap.set(ring,{x:rx,y:ry});
  });
  document.querySelectorAll("a,button,.vb-dp-multi,.vb-boom-skeu").forEach(function(el){
    el.addEventListener("mouseenter",function(){document.body.classList.add("c-hover");});
    el.addEventListener("mouseleave",function(){document.body.classList.remove("c-hover");});
  });
  document.querySelectorAll(".wi").forEach(function(el){
    el.addEventListener("mouseenter",function(){document.body.classList.add("c-view");});
    el.addEventListener("mouseleave",function(){document.body.classList.remove("c-view");});
  });
  var hscrollEl = document.querySelector(".hscroll");
  if(hscrollEl){
    hscrollEl.addEventListener("mouseenter",function(){document.body.classList.add("c-drag");});
    hscrollEl.addEventListener("mouseleave",function(){document.body.classList.remove("c-drag");});
  }
  var vWrap = document.querySelector(".v-wrap");
  if(vWrap){
    vWrap.addEventListener("mouseenter",function(){document.body.classList.add("c-play");});
    vWrap.addEventListener("mouseleave",function(){document.body.classList.remove("c-play");});
  }

  /* MESH CANVAS */
  function initMeshCanvas(){
    var canvas=document.getElementById("mesh-canvas");
    if(!canvas) return;
    var ctx=canvas.getContext("2d");
    function resize(){canvas.width=window.innerWidth;canvas.height=window.innerHeight;}
    resize(); window.addEventListener("resize",resize);
    var orbs=[
      {x:.2,y:.3,r:.45,color:"rgba(232,126,178,0.06)",vx:.0003,vy:.0002},
      {x:.7,y:.6,r:.55,color:"rgba(91,207,176,0.05)",vx:-.0002,vy:.0003},
      {x:.5,y:.1,r:.4,color:"rgba(108,180,238,0.04)",vx:.0004,vy:-.0002},
      {x:.1,y:.8,r:.5,color:"rgba(180,142,222,0.04)",vx:.0002,vy:-.0004}
    ];
    function draw(t){
      ctx.clearRect(0,0,canvas.width,canvas.height);
      orbs.forEach(function(o){
        o.x+=Math.sin(t*o.vx*1000)*0.0008;
        o.y+=Math.cos(t*o.vy*1000)*0.0008;
        var gx=o.x*canvas.width,gy=o.y*canvas.height;
        var gr=o.r*Math.max(canvas.width,canvas.height);
        var g=ctx.createRadialGradient(gx,gy,0,gx,gy,gr);
        g.addColorStop(0,o.color);g.addColorStop(1,"transparent");
        ctx.fillStyle=g;ctx.beginPath();ctx.arc(gx,gy,gr,0,Math.PI*2);ctx.fill();
      });
      requestAnimationFrame(draw);
    }
    requestAnimationFrame(draw);
  }
  initMeshCanvas();

  /* PARTICLE WEBGL */
  function initParticleWebGL(){
    var canvas=document.getElementById("particle-canvas");
    if(!canvas) return;
    var gl=canvas.getContext("webgl");
    if(!gl) return;
    function resize(){canvas.width=window.innerWidth;canvas.height=window.innerHeight;gl.viewport(0,0,canvas.width,canvas.height);}
    resize(); window.addEventListener("resize",resize);
    var VERT="attribute vec2 a_pos;attribute float a_size;attribute float a_alpha;uniform vec2 u_mouse;uniform float u_time;varying float v_alpha;void main(){vec2 pos=a_pos;vec2 diff=pos-u_mouse;float dist=length(diff);float force=max(0.0,1.0-dist/0.25)*0.08;pos+=normalize(diff+vec2(0.0001))*force;pos.x+=sin(u_time*0.4+a_pos.y*8.0)*0.004;pos.y+=cos(u_time*0.3+a_pos.x*8.0)*0.004;gl_Position=vec4(pos,0.0,1.0);gl_PointSize=a_size;v_alpha=a_alpha;}";
    var FRAG="precision mediump float;uniform vec3 u_color;varying float v_alpha;void main(){vec2 c=gl_PointCoord-0.5;float d=length(c);if(d>0.5)discard;float alpha=(1.0-d*2.0)*v_alpha;gl_FragColor=vec4(u_color,alpha);}";
    function compile(type,src){var s=gl.createShader(type);gl.shaderSource(s,src);gl.compileShader(s);return s;}
    var prog=gl.createProgram();
    gl.attachShader(prog,compile(gl.VERTEX_SHADER,VERT));
    gl.attachShader(prog,compile(gl.FRAGMENT_SHADER,FRAG));
    gl.linkProgram(prog);gl.useProgram(prog);
    var N=180,pos2=new Float32Array(N*2),sizes=new Float32Array(N),alpha=new Float32Array(N);
    for(var i=0;i<N;i++){pos2[i*2]=Math.random()*2-1;pos2[i*2+1]=Math.random()*2-1;sizes[i]=Math.random()*2.5+.5;alpha[i]=Math.random()*.5+.1;}
    function mkBuf(data){var b=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,b);gl.bufferData(gl.ARRAY_BUFFER,data,gl.DYNAMIC_DRAW);return b;}
    var bPos=mkBuf(pos2),bSz=mkBuf(sizes),bAlp=mkBuf(alpha);
    var aPos=gl.getAttribLocation(prog,"a_pos"),aSz=gl.getAttribLocation(prog,"a_size"),aAlp=gl.getAttribLocation(prog,"a_alpha");
    var uMouse=gl.getUniformLocation(prog,"u_mouse"),uTime=gl.getUniformLocation(prog,"u_time"),uColor=gl.getUniformLocation(prog,"u_color");
    gl.enable(gl.BLEND);gl.blendFunc(gl.SRC_ALPHA,gl.ONE_MINUS_SRC_ALPHA);
    var mx2=-99,my2=-99;
    window.addEventListener("mousemove",function(e){mx2=(e.clientX/window.innerWidth)*2-1;my2=-((e.clientY/window.innerHeight)*2-1);});
    function render(t){
      gl.clearColor(0,0,0,0);gl.clear(gl.COLOR_BUFFER_BIT);
      gl.uniform2f(uMouse,mx2,my2);gl.uniform1f(uTime,t*0.001);
      gl.uniform3f(uColor,232/255,126/255,178/255);
      gl.bindBuffer(gl.ARRAY_BUFFER,bPos);gl.bufferData(gl.ARRAY_BUFFER,pos2,gl.DYNAMIC_DRAW);
      gl.enableVertexAttribArray(aPos);gl.vertexAttribPointer(aPos,2,gl.FLOAT,false,0,0);
      gl.bindBuffer(gl.ARRAY_BUFFER,bSz);gl.enableVertexAttribArray(aSz);gl.vertexAttribPointer(aSz,1,gl.FLOAT,false,0,0);
      gl.bindBuffer(gl.ARRAY_BUFFER,bAlp);gl.enableVertexAttribArray(aAlp);gl.vertexAttribPointer(aAlp,1,gl.FLOAT,false,0,0);
      gl.drawArrays(gl.POINTS,0,N);requestAnimationFrame(render);
    }
    requestAnimationFrame(render);
  }
  initParticleWebGL();

  /* PRELOADER */
  gsap.to(".pre__logo-inner",{y:"0%",duration:.8,ease:"power3.out",delay:.1});
  var prog2=0;
  var tick=setInterval(function(){
    prog2+=Math.random()*14;
    if(prog2>100){prog2=100;clearInterval(tick);setTimeout(closePreloader,300);}
    document.getElementById("pre-fill").style.width=prog2+"%";
    document.getElementById("pre-num").textContent=Math.floor(prog2)+"%";
  },70);

  function closePreloader(){
    gsap.to("#preloader",{opacity:0,duration:.8,ease:"power2.inOut",
      onComplete:function(){document.getElementById("preloader").style.display="none";initHero();}
    });
  }

  /* SCRAMBLE TEXT */
  function scrambleText(el,duration){
    duration=duration||1200;
    var chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*";
    var final2=el.textContent.trim();
    var total=final2.length;
    var start=performance.now();
    el.style.fontVariantNumeric="tabular-nums";
    function tk(now){
      var elapsed=now-start;
      var progress=Math.min(elapsed/duration,1);
      var revealed=Math.floor(progress*total);
      var result="";
      for(var i=0;i<total;i++){
        if(final2[i]===" "){result+=" ";continue;}
        if(i<revealed) result+=final2[i];
        else result+=chars[Math.floor(Math.random()*chars.length)];
      }
      el.textContent=result;
      if(progress<1) requestAnimationFrame(tk);
      else el.textContent=final2;
    }
    requestAnimationFrame(tk);
  }

  /* HERO INIT */
  function initHero(){
    var tl=gsap.timeline({defaults:{ease:"power4.out"}});
    tl.from("#nav",{y:-20,opacity:0,duration:.9},0);
    tl.to(".hero__title .line-i",{y:"0%",duration:1.25,stagger:.12},.18);
    tl.from(".hero__eyebrow",{opacity:0,x:-16,duration:.7},.5);
    tl.to(["#hero-desc","#hero-act"],{opacity:1,y:0,duration:.85,stagger:.18},.9);
    tl.to("#hero-scroll",{opacity:1,duration:.6},1.3);
    tl.add(function(){
      scrambleText(document.getElementById("ht-3"),1000);
      initScroll();
    },1.6);
  }

  /* KINETIC TYPOGRAPHY */
  var heroSection=document.getElementById("hero");
  if(heroSection){
    heroSection.addEventListener("mousemove",function(e){
      gsap.to("#hero-h",{
        rotationY:(e.clientX/window.innerWidth-0.5)*7,
        rotationX:-(e.clientY/window.innerHeight-0.5)*4,
        transformPerspective:900,duration:0.9,ease:"power2.out"
      });
    });
    heroSection.addEventListener("mouseleave",function(){
      gsap.to("#hero-h",{rotationY:0,rotationX:0,duration:1.2,ease:"power3.out"});
    });
  }

  /* ALL SCROLL TRIGGERS */
  function initScroll(){
    /* NAV */
    ScrollTrigger.create({start:"top -100",onUpdate:function(self){
      if(self.direction===1) document.getElementById("nav").classList.add("scrolled");
      if(self.scroll()<100) document.getElementById("nav").classList.remove("scrolled");
    }});

    /* ABOUT */
    ScrollTrigger.create({trigger:"#about-h",start:"top 82%",onEnter:function(){
      gsap.to(".ri",{y:"0%",duration:1.25,stagger:.1,ease:"power4.out"});
    }});
    ScrollTrigger.create({trigger:"#about-p",start:"top 82%",onEnter:function(){
      gsap.to("#about-p",{opacity:1,y:0,duration:.85});
      gsap.to("#about-stats",{opacity:1,y:0,duration:.85,delay:.2});
      document.querySelectorAll(".stat__n").forEach(function(el){
        var target=parseFloat(el.dataset.target);
        var suffix=el.dataset.suffix||"";
        gsap.to({val:0},{val:target,duration:2.2,ease:"power2.out",snap:{val:1},
          onUpdate:function(){el.textContent=Math.floor(this.targets()[0].val)+suffix;}
        });
      });
    }});
    ScrollTrigger.create({trigger:"#about-img",start:"top bottom",end:"bottom top",
      onUpdate:function(self){gsap.set("#about-img-i",{y:self.progress*-90});}
    });
    ScrollTrigger.create({trigger:"#about",start:"top bottom",end:"bottom top",
      onUpdate:function(self){gsap.set("#deco-about",{y:self.progress*-120});}
    });

    /* PARALLAX BAND */
    ScrollTrigger.create({trigger:"#pb",start:"top bottom",end:"bottom top",
      onUpdate:function(self){
        gsap.set("#pb-bg",{y:self.progress*140-70});
        var w=300+self.progress*300;
        document.getElementById("pb-q").style.fontVariationSettings="'wght' "+w;
      }
    });
    ScrollTrigger.create({trigger:"#pb-q",start:"top 78%",
      onEnter:function(){gsap.to("#pb-q",{opacity:1,y:0,duration:1.2,ease:"power3.out"});}
    });

    /* VIDEO */
    ScrollTrigger.create({trigger:"#vid",start:"top 72%",onEnter:function(){
      gsap.to("#v-wrap",{clipPath:"inset(0% 0 0 0)",duration:1.5,ease:"power4.inOut"});
      gsap.to("#v-label",{opacity:1,duration:.8,delay:1.2});
    }});

    /* HORIZONTAL SCROLL */
    var hscroll=document.getElementById("hscroll");
    if(hscroll){
      gsap.to("#hscroll",{
        x:function(){return -(hscroll.scrollWidth-window.innerWidth+96);},
        ease:"none",
        scrollTrigger:{trigger:"#hscroll-pin",start:"top top",
          end:function(){return "+="+(hscroll.scrollWidth-window.innerWidth+96);},
          pin:true,scrub:1.2,anticipatePin:1}
      });
    }

    /* WORKS */
    gsap.utils.toArray(".wi").forEach(function(el,i){
      ScrollTrigger.create({trigger:el,start:"top 88%",onEnter:function(){
        gsap.to(el,{opacity:1,y:0,duration:.95,delay:(i%3)*0.1,ease:"power3.out"});
      }});
    });

    /* DECO NUMS */
    ScrollTrigger.create({trigger:"#works",start:"top bottom",end:"bottom top",
      onUpdate:function(self){gsap.set("#deco-works",{y:self.progress*-120});}
    });
    ScrollTrigger.create({trigger:"#services",start:"top bottom",end:"bottom top",
      onUpdate:function(self){gsap.set("#deco-services",{y:self.progress*-120});}
    });

    /* SERVICES */
    gsap.utils.toArray(".svc-item").forEach(function(el,i){
      ScrollTrigger.create({trigger:el,start:"top 88%",onEnter:function(){
        gsap.to(el,{opacity:1,y:0,duration:.65,delay:i*0.07,ease:"power3.out"});
      }});
    });

    /* CTA */
    ScrollTrigger.create({trigger:"#contact",start:"top 75%",onEnter:function(){
      gsap.to("#cta-sub",{opacity:1,duration:.6});
      gsap.to("#cta-h .line-i",{y:"0%",duration:1.25,stagger:.12,ease:"power4.out",delay:.1});
      gsap.to("#cta-line-path",{strokeDashoffset:0,duration:1.8,ease:"power3.inOut",delay:.4});
      gsap.to("#cta-btns",{opacity:1,duration:.85,delay:.55});
      setTimeout(function(){var s=document.getElementById("cta-scramble");if(s)scrambleText(s,900);},600);
    }});

    ScrollTrigger.refresh();
  }

  /* WORKS FOCUS + DISTORTION */
  var turbulence=document.getElementById("turbulence");
  var displacement=document.getElementById("displacement");
  document.querySelectorAll(".wi").forEach(function(item){
    item.addEventListener("mouseenter",function(){
      document.querySelectorAll(".wi").forEach(function(other){
        if(other!==item) gsap.to(other,{opacity:0.3,duration:.4});
      });
      var img=item.querySelector("img");
      if(img && turbulence && displacement){
        img.style.filter="url(#distort)";
        gsap.fromTo(turbulence,{attr:{baseFrequency:"0 0"}},{attr:{baseFrequency:"0.04 0.01"},duration:.4,ease:"power2.out",yoyo:true,repeat:1});
        gsap.fromTo(displacement,{attr:{scale:0}},{attr:{scale:25},duration:.4,ease:"power2.out",yoyo:true,repeat:1,onComplete:function(){img.style.filter="";}});
      }
    });
    item.addEventListener("mouseleave",function(){
      document.querySelectorAll(".wi").forEach(function(other){gsap.to(other,{opacity:1,duration:.4});});
    });
  });

  /* WORKS FILTERS */
  document.querySelectorAll(".wf").forEach(function(btn){
    btn.addEventListener("click",function(){
      var filter=btn.dataset.filter;
      var items=document.querySelectorAll(".wi");
      var before=[];items.forEach(function(el){before.push(el.getBoundingClientRect());});
      items.forEach(function(el){el.style.display=(filter==="all"||el.dataset.cat===filter)?"":"none";});
      items.forEach(function(el,i){
        if(el.style.display==="none") return;
        var after=el.getBoundingClientRect();
        gsap.from(el,{x:before[i].left-after.left,y:before[i].top-after.top,duration:.6,ease:"power3.out"});
      });
      document.querySelectorAll(".wf").forEach(function(b){b.classList.remove("active");});
      btn.classList.add("active");
    });
  });

  /* SERVICES IMAGE TRAIL */
  var trail=document.getElementById("svc-trail");
  var trailImg=document.getElementById("svc-trail-img");
  var trailX=0,trailY=0;
  document.querySelectorAll(".svc-item").forEach(function(item){
    item.addEventListener("mouseenter",function(){
      trailImg.src=item.dataset.img;
      gsap.to(trail,{opacity:1,duration:.4,ease:"power3.out"});
      gsap.fromTo(trail,{scale:.85,rotation:-3},{scale:1,rotation:0,duration:.5,ease:"power3.out"});
    });
    item.addEventListener("mouseleave",function(){gsap.to(trail,{opacity:0,duration:.3,scale:.9});});
  });
  window.addEventListener("mousemove",function(e){
    trailX+=(e.clientX-trailX)*0.09;trailY+=(e.clientY-trailY)*0.09;
    gsap.set(trail,{x:trailX,y:trailY});
  });

  /* MAGNETIC */
  document.querySelectorAll(".mag-link,.mag-btn").forEach(function(el){
    el.addEventListener("mousemove",function(e){
      var r=el.getBoundingClientRect();
      var x=e.clientX-r.left-r.width/2;
      var y=e.clientY-r.top-r.height/2;
      gsap.to(el,{x:x*.35,y:y*.35,duration:.4,ease:"power2.out"});
    });
    el.addEventListener("mouseleave",function(){
      gsap.to(el,{x:0,y:0,duration:.7,ease:"elastic.out(1,.5)"});
    });
  });

  /* PAGE TRANSITIONS */
  document.querySelectorAll("a[href^=\\"#\\"]").forEach(function(a){
    a.addEventListener("click",function(e){
      e.preventDefault();
      var target=document.querySelector(this.getAttribute("href"));
      if(!target) return;
      var pt=document.getElementById("pt");
      gsap.timeline()
        .to(pt,{scaleY:1,duration:.5,ease:"power3.inOut",transformOrigin:"bottom"})
        .add(function(){lenis.scrollTo(target,{duration:0,immediate:true});})
        .to(pt,{scaleY:0,duration:.6,ease:"power3.inOut",transformOrigin:"top",delay:.05});
    });
  });

  /* CLICK RIPPLE */
  document.addEventListener("click",function(e){
    var ripple=document.createElement("div");
    ripple.style.cssText="position:fixed;left:"+e.clientX+"px;top:"+e.clientY+"px;width:8px;height:8px;border:1px solid var(--accent);border-radius:50%;transform:translate(-50%,-50%) scale(0);pointer-events:none;z-index:9997;";
    document.body.appendChild(ripple);
    gsap.to(ripple,{scale:6,opacity:0,duration:.8,ease:"power2.out",onComplete:function(){ripple.remove();}});
  });

})();
</SCRIPTCLOSE>
</body>
</html>'''

# Replace SCRIPTTAG/SCRIPTCLOSE with \x3cscript and \x3c/script>
HTML = HTML.replace('SCRIPTTAG', 'XSCRIPTOPEN')
HTML = HTML.replace('</SCRIPTCLOSE>', 'XSCRIPTCLOSE')
HTML = HTML.replace('SCRIPTCLOSE>', 'XSCRIPTCLOSE')

# Now build the JS string
# Escape backslashes first
js_str = HTML.replace('\\', '\\\\')
# Escape single quotes
js_str = js_str.replace("'", "\\'")
# Escape newlines
js_str = js_str.replace('\n', '\\n')

# Now replace the script tag placeholders with \x3c versions
js_str = js_str.replace('XSCRIPTOPEN', '\\x3cscript')
js_str = js_str.replace('XSCRIPTCLOSE', '\\x3c/script>')

new_template = "TPL_ECOM_HTML['4'] = function () {\n  return '" + js_str + "';\n};\n\n"

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

# Now replace in index.html
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "TPL_ECOM_HTML['4']"
end_marker = "TPL_ECOM_HTML['9']"
start_idx = content.index(start_marker)
end_idx = content.index(end_marker)
chunk = content[start_idx:end_idx]
last_close = chunk.rfind('};')
actual_end = start_idx + last_close + 2

content = content[:start_idx] + new_template + content[actual_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Template 4 V3 replaced successfully!")
