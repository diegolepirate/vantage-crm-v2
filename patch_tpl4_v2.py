import re

filepath = r"C:\vantage-clean\crm-v2-push\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find template 4 boundaries
start_marker = "TPL_ECOM_HTML['4'] = function () {"
end_marker = "TPL_ECOM_HTML['9']"

start_idx = content.index(start_marker)
end_idx = content.index(end_marker)

# Find the }; before TPL 9
chunk = content[start_idx:end_idx]
last_close = chunk.rfind('};')
actual_end = start_idx + last_close + 2

# Build the new template - using triple quotes and then escaping
# The template HTML content (will be wrapped in JS string)
tpl_html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vortex Digital — Design Studio</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500;1,600&family=DM+Mono:wght@300;400&display=swap" rel="stylesheet">
<style>
:root {
  --black:#0a0a0a;--white:#f0ede8;--gold:#D4AF37;--gold-light:#e8cc5a;--gray:#888880;
  --dark2:#111110;--dark3:#161614;--font-d:'Cormorant Garamond',serif;--font-m:'DM Mono',monospace;
  --ease-out:cubic-bezier(0.16,1,0.3,1);--ease-io:cubic-bezier(0.76,0,0.24,1);
}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;}
html{font-size:62.5%;scrollbar-width:none;}
html::-webkit-scrollbar{display:none;}
body{cursor:none;overflow-x:hidden;background:var(--black);color:var(--white);font-family:var(--font-m);}

/* NOISE */
.noise{position:fixed;inset:0;z-index:9998;pointer-events:none;opacity:0.032;
background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
background-size:200px 200px;}

/* PAGE TRANSITION */
#pt{position:fixed;inset:0;z-index:8999;background:var(--gold);transform:scaleY(0);transform-origin:bottom;pointer-events:none;}

/* CURSOR */
.cursor{position:fixed;top:0;left:0;z-index:9999;pointer-events:none;mix-blend-mode:difference;}
.cursor__dot{width:8px;height:8px;background:var(--white);border-radius:50%;position:absolute;transform:translate(-50%,-50%);transition:width 0.3s,height 0.3s;}
.cursor__ring{width:44px;height:44px;border:1px solid rgba(240,237,232,0.45);border-radius:50%;position:absolute;transform:translate(-50%,-50%);transition:width 0.3s,height 0.3s,border-radius 0.3s;}
body.c-hover .cursor__dot{width:56px;height:56px;}
body.c-view .cursor__ring{width:80px;height:80px;}
body.c-view .cursor__ring .cr-txt{opacity:1;}
.cr-txt{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-family:var(--font-m);font-size:10px;letter-spacing:0.15em;text-transform:uppercase;opacity:0;transition:opacity 0.3s;color:var(--white);}

/* PRELOADER */
.preloader{position:fixed;inset:0;z-index:9000;background:var(--black);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2.8rem;}
.pre__logo{font-family:var(--font-d);font-size:3rem;letter-spacing:0.45em;text-transform:uppercase;overflow:hidden;}
.pre__logo-inner{display:block;transform:translateY(100%);}
.pre__bar{width:220px;height:1px;background:rgba(240,237,232,0.12);}
.pre__fill{height:100%;width:0;background:var(--gold);}
.pre__num{font-family:var(--font-m);font-size:1.1rem;letter-spacing:0.2em;color:var(--gray);}

/* NAV */
.nav{position:fixed;top:0;width:100%;z-index:100;padding:2.8rem 4.8rem;display:flex;align-items:center;justify-content:space-between;transition:padding 0.5s,background 0.5s;}
.nav.scrolled{padding:2rem 4.8rem;background:rgba(10,10,10,0.88);backdrop-filter:blur(24px);border-bottom:1px solid rgba(255,255,255,0.05);}
.nav__logo{font-family:var(--font-d);font-size:2rem;letter-spacing:0.32em;text-transform:uppercase;display:flex;gap:1.2rem;align-items:center;text-decoration:none;color:var(--white);cursor:none;}
.nav__mark{width:26px;height:26px;border:1px solid var(--gold);transform:rotate(45deg);display:flex;align-items:center;justify-content:center;}
.nav__mark-dot{width:6px;height:6px;background:var(--gold);}
.nav__links{list-style:none;display:flex;gap:3.6rem;}
.nav__links a{font-family:var(--font-m);font-size:1.1rem;letter-spacing:0.15em;text-transform:uppercase;color:rgba(240,237,232,0.55);text-decoration:none;position:relative;cursor:none;}
.nav__links a::after{content:'';position:absolute;bottom:-3px;left:0;width:0;height:1px;background:var(--gold);transition:width 0.4s var(--ease-out);}
.nav__links a:hover::after{width:100%;}
.nav__links a:hover{color:var(--white);}
.nav__btn{font-family:var(--font-m);font-size:1.1rem;background:var(--gold);color:#000;padding:1.1rem 2.8rem;text-decoration:none;text-transform:uppercase;letter-spacing:0.15em;cursor:none;transition:background 0.3s;}
.nav__btn:hover{background:var(--gold-light);}

/* HERO */
.hero{height:100vh;min-height:720px;display:flex;align-items:flex-end;padding:0 4.8rem 9rem;position:relative;overflow:hidden;}
.hero__bg{position:absolute;inset:0;z-index:0;}
.hero__bg img{width:100%;height:100%;object-fit:cover;}
.hero__bg::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,0.25) 0%,rgba(10,10,10,0.08) 35%,rgba(10,10,10,0.65) 75%,rgba(10,10,10,1) 100%);}
.hero__content{position:relative;z-index:2;width:100%;}
.hero__eyebrow{display:inline-flex;gap:1.4rem;align-items:center;margin-bottom:3.2rem;}
.hero__eyebrow::before{content:'';width:36px;height:1px;background:var(--gold);}
.hero__eyebrow span{font-family:var(--font-m);font-size:1.1rem;letter-spacing:0.22em;text-transform:uppercase;color:var(--gold);}
.hero__title{font-family:var(--font-d);font-size:clamp(6rem,10.5vw,15rem);font-weight:300;line-height:0.93;letter-spacing:-0.02em;}
.hero__title em{font-style:italic;color:var(--gold);}
.line{overflow:hidden;display:block;}
.line-i{display:block;transform:translateY(105%);}
.hero__bottom{display:flex;justify-content:space-between;align-items:flex-end;margin-top:4.8rem;}
.hero__desc{font-size:1.5rem;color:rgba(240,237,232,0.55);max-width:300px;line-height:1.6;opacity:0;transform:translateY(20px);}
.hero__actions{opacity:0;transform:translateY(20px);display:flex;gap:2.4rem;align-items:center;}
.hero__scroll{position:absolute;right:4.8rem;bottom:4.8rem;z-index:2;display:flex;flex-direction:column;align-items:center;gap:1.2rem;opacity:0;}
.scroll-line{width:1px;height:72px;background:rgba(240,237,232,0.18);overflow:hidden;position:relative;}
.scroll-line::after{content:'';position:absolute;top:-100%;left:0;width:100%;height:100%;background:var(--gold);animation:sline 2.2s ease-in-out infinite;}
@keyframes sline{0%{top:-100%;}50%{top:0;}100%{top:100%;}}
.hero__scroll span{font-family:var(--font-m);font-size:1rem;letter-spacing:0.2em;text-transform:uppercase;color:rgba(240,237,232,0.45);}

/* MARQUEE */
.marquee{padding:2.2rem 0;overflow:hidden;border-top:1px solid rgba(255,255,255,0.07);border-bottom:1px solid rgba(255,255,255,0.07);background:var(--dark3);}
.marquee__track{display:flex;width:max-content;}
.marquee__run{display:flex;gap:3.6rem;align-items:center;animation:mrun 22s linear infinite;padding-right:3.6rem;}
@keyframes mrun{to{transform:translateX(-100%);}}
.marquee:hover .marquee__run{animation-play-state:paused;}
.marquee__run span{font-family:var(--font-d);font-size:1.5rem;font-style:italic;letter-spacing:0.1em;color:rgba(240,237,232,0.38);white-space:nowrap;}
.marquee__run span::after{content:'\u25C6';color:var(--gold);font-size:0.7rem;font-style:normal;margin-left:3.6rem;}

/* ABOUT */
.about{padding:16rem 4.8rem;}
.container{max-width:1440px;margin:0 auto;}
.about__grid{display:grid;grid-template-columns:1fr 1fr;gap:10rem;align-items:center;}
.about__h{font-family:var(--font-d);font-size:clamp(4.4rem,5.5vw,8rem);font-weight:300;line-height:1.05;margin-bottom:3.2rem;}
.about__h em{font-style:italic;color:var(--gold);}
.rl{overflow:hidden;display:block;}
.ri{display:block;transform:translateY(105%);}
.about__p{font-size:1.5rem;color:rgba(240,237,232,0.55);line-height:1.7;margin-bottom:4.8rem;opacity:0;transform:translateY(20px);}
.stats{display:flex;gap:4.8rem;opacity:0;transform:translateY(20px);}
.stat{display:flex;flex-direction:column;gap:0.6rem;}
.stat__n{font-family:var(--font-d);font-size:4.4rem;font-weight:300;color:var(--gold);}
.stat__l{font-family:var(--font-m);font-size:1rem;letter-spacing:0.15em;text-transform:uppercase;color:var(--gray);}
.about__img{height:640px;overflow:hidden;position:relative;}
.about__img-inner{height:120%;position:relative;top:-10%;}
.about__img-inner img{width:100%;height:100%;object-fit:cover;}

/* S-TAG */
.s-tag{display:inline-flex;align-items:center;gap:1.4rem;margin-bottom:3.2rem;}
.s-tag::before{content:'';width:28px;height:1px;background:var(--gold);}
.s-tag span{font-family:var(--font-m);font-size:1.1rem;letter-spacing:0.22em;text-transform:uppercase;color:var(--gold);}

/* PARALLAX BAND */
.pb{height:72vh;overflow:hidden;display:flex;align-items:center;justify-content:center;position:relative;}
.pb__bg{position:absolute;inset:-25%;z-index:0;}
.pb__bg img{width:100%;height:100%;object-fit:cover;}
.pb__mask{position:absolute;inset:0;background:rgba(10,10,10,0.52);z-index:1;}
.pb__content{position:relative;z-index:2;text-align:center;padding:0 4.8rem;}
.pb__q{font-family:var(--font-d);font-size:clamp(3.6rem,6.5vw,9.6rem);font-weight:300;font-style:italic;opacity:0;transform:translateY(40px);}
.pb__q em{color:var(--gold);}

/* VIDEO */
.video-sec{padding:12rem 4.8rem;}
.v-wrap{height:82vh;overflow:hidden;position:relative;clip-path:inset(100% 0 0 0);}
.v-wrap video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
.v-label{position:absolute;bottom:4.8rem;left:4.8rem;z-index:2;opacity:0;}
.v-label span{font-family:var(--font-d);font-size:2rem;font-style:italic;color:rgba(240,237,232,0.65);}

/* WORKS */
.works{padding:16rem 4.8rem;}
.works__hd{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:4.8rem;}
.works__title{font-family:var(--font-d);font-size:clamp(4rem,5vw,7rem);font-weight:300;}
.works__filters{display:flex;gap:1.6rem;margin-bottom:4.8rem;}
.wf{font-family:var(--font-m);font-size:1.1rem;letter-spacing:0.15em;text-transform:uppercase;background:none;border:1px solid rgba(240,237,232,0.12);color:var(--gray);padding:0.8rem 2rem;cursor:none;transition:all 0.3s;}
.wf.active,.wf:hover{border-color:var(--gold);color:var(--gold);}
.works__grid{display:grid;grid-template-columns:repeat(12,1fr);gap:2rem;}
.wi{overflow:hidden;cursor:none;opacity:0;transform:translateY(60px);position:relative;transition:opacity 0.4s;}
.wi:nth-child(1){grid-column:1/8;height:520px;}
.wi:nth-child(2){grid-column:8/13;height:520px;}
.wi:nth-child(3){grid-column:1/5;height:380px;}
.wi:nth-child(4){grid-column:5/9;height:380px;}
.wi:nth-child(5){grid-column:9/13;height:380px;}
.wi img{width:100%;height:100%;object-fit:cover;transition:transform 0.8s var(--ease-out);}
.wi:hover img{transform:scale(1.06);}
.wi__ov{position:absolute;inset:0;background:rgba(10,10,10,0.72);display:flex;flex-direction:column;justify-content:flex-end;padding:3.6rem;opacity:0;transition:opacity 0.4s;}
.wi:hover .wi__ov{opacity:1;}
.wi__cat{font-family:var(--font-m);font-size:1rem;letter-spacing:0.2em;text-transform:uppercase;color:var(--gold);margin-bottom:0.8rem;}
.wi__name{font-family:var(--font-d);font-size:2.8rem;font-weight:300;}

/* CA43 GLASS CARDS in about section */
.glass-cards{display:flex;gap:2rem;margin-top:4.8rem;opacity:0;transform:translateY(20px);}
.gc{width:254px;height:190px;background:transparent;position:relative;box-shadow:0 0 5px rgba(0,0,0,0.44);overflow:hidden;border-radius:10px;}
.gc-inner{cursor:none;width:100%;height:100%;position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0.8rem;
color:var(--white);background:rgba(255,255,255,0.074);border:1px solid rgba(255,255,255,0.222);
backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-radius:10px;transition:all 0.3s;}
.gc-inner .gc-icon{font-size:2.4rem;margin-bottom:0.4rem;}
.gc-inner .gc-title{font-family:var(--font-m);font-size:1.2rem;letter-spacing:0.1em;text-transform:uppercase;}
.gc-inner .gc-desc{font-size:1.1rem;color:var(--gray);text-align:center;padding:0 1.6rem;line-height:1.4;}
.gc::after,.gc::before{width:100px;height:100px;content:'';position:absolute;border-radius:50%;transition:0.5s linear;}
.gc::after{top:-20px;left:-20px;background:rgba(212,175,55,0.4);animation:gcA 5s linear infinite;}
.gc::before{background:rgba(212,175,55,0.3);top:70%;left:70%;animation:gcB 5s linear infinite;animation-delay:3s;}
@keyframes gcA{0%,100%{transform:translate(0,0);}25%{transform:translate(50px,30px);}50%{transform:translate(100px,0);}75%{transform:translate(50px,-30px);}}
@keyframes gcB{0%,100%{transform:translate(0,0);}25%{transform:translate(-30px,-50px);}50%{transform:translate(-60px,0);}75%{transform:translate(-30px,50px);}}
.gc:hover{box-shadow:0 0 10px rgba(212,175,55,0.43);}
.gc:hover::after{left:190px;transform:scale(1.2);}
.gc:hover::before{left:-10px;transform:scale(1.2);}

/* SERVICES */
.services{padding:16rem 4.8rem;}
.svc__list{margin-top:4.8rem;}
.svc-item{display:grid;grid-template-columns:96px 1fr auto;align-items:center;padding:3.6rem 0;border-top:1px solid rgba(255,255,255,0.07);opacity:0;transform:translateY(28px);transition:border-color 0.3s;}
.svc-item:hover{border-color:rgba(212,175,55,0.25);}
.svc-item__n{font-family:var(--font-m);font-size:1.2rem;color:var(--gray);letter-spacing:0.1em;}
.svc-item__t{font-family:var(--font-d);font-size:clamp(2.4rem,3.2vw,4.4rem);font-weight:300;font-style:italic;transition:color 0.3s;cursor:none;}
.svc-item:hover .svc-item__t{color:var(--gold);}
.svc-item__a{font-size:2.2rem;color:var(--gray);transition:transform 0.35s,color 0.35s;cursor:none;}
.svc-item:hover .svc-item__a{transform:translateX(8px) rotate(-45deg);color:var(--gold);}

/* CTA */
.cta{padding:16rem 4.8rem;text-align:center;background:var(--dark3);position:relative;}
.cta::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 70% 60% at 50% 110%,rgba(212,175,55,0.07) 0%,transparent 70%);pointer-events:none;}
.cta__sub{font-family:var(--font-m);font-size:1.3rem;letter-spacing:0.22em;text-transform:uppercase;color:var(--gold);margin-bottom:3.2rem;opacity:0;}
.cta__title{font-family:var(--font-d);font-size:clamp(5.6rem,10vw,14.4rem);font-weight:300;line-height:0.93;margin-bottom:4.8rem;}
.cta__title em{font-style:italic;color:var(--gold);}
.cta__btns{opacity:0;display:flex;gap:2.4rem;justify-content:center;align-items:center;flex-wrap:wrap;}

/* BUTTONS */
.btn{display:inline-flex;align-items:center;gap:1.2rem;font-family:var(--font-m);font-size:1.1rem;letter-spacing:0.15em;text-transform:uppercase;cursor:none;transition:all 0.35s var(--ease-out);text-decoration:none;color:var(--white);}
.btn-arrow{display:inline-block;transition:transform 0.35s var(--ease-out);}
.btn:hover .btn-arrow{transform:translateX(5px);}
.btn--fill{color:#000;background:var(--gold);padding:1.7rem 3.6rem;}
.btn--fill:hover{background:var(--gold-light);transform:translateY(-2px);box-shadow:0 16px 40px rgba(212,175,55,0.2);}
.btn--line{color:var(--white);border-bottom:1px solid rgba(240,237,232,0.3);padding-bottom:0.4rem;}
.btn--line:hover{color:var(--gold);border-color:var(--gold);}
.btn--xl{padding:2.2rem 6rem;font-size:1.2rem;}

/* P8 NEON FLICKER BUTTON */
.vb-neon-flick{padding:1.4rem 3.2rem;font-size:1.1rem;font-family:var(--font-m);font-weight:600;background:transparent;color:#0ff;border:2px solid #0ff;border-radius:8px;cursor:none;letter-spacing:0.15em;text-transform:uppercase;text-shadow:0 0 10px #0ff,0 0 20px #0ff;box-shadow:0 0 5px #0ff,0 0 20px #0ff,0 0 40px #0ff;animation:vb-neonFlicker 0.1s infinite alternate;text-decoration:none;display:inline-flex;align-items:center;gap:1rem;}
@keyframes vb-neonFlicker{0%{opacity:1;box-shadow:0 0 5px #0ff,0 0 20px #0ff,0 0 40px #0ff;}25%{opacity:0.8;box-shadow:0 0 2px #0ff,0 0 8px #0ff;}50%{opacity:1;box-shadow:0 0 5px #0ff,0 0 25px #0ff,0 0 50px #0ff;}75%{opacity:0.6;box-shadow:0 0 1px #0ff;}100%{opacity:1;box-shadow:0 0 5px #0ff,0 0 20px #0ff,0 0 40px #0ff;}}

/* FOOTER */
.footer{padding:6.4rem 4.8rem;background:var(--black);border-top:1px solid rgba(255,255,255,0.05);}
.footer__in{display:flex;align-items:center;justify-content:space-between;}
.footer__logo{font-family:var(--font-d);font-size:2rem;font-weight:300;letter-spacing:0.32em;text-transform:uppercase;color:var(--white);}
.footer__links{list-style:none;display:flex;gap:2.4rem;}
.footer__links a{font-family:var(--font-m);font-size:1rem;letter-spacing:0.15em;text-transform:uppercase;color:var(--gray);text-decoration:none;cursor:none;transition:color 0.3s;}
.footer__links a:hover{color:var(--gold);}
.footer__copy{font-family:var(--font-m);font-size:1rem;color:rgba(136,136,128,0.45);}

/* RESPONSIVE */
@media(max-width:1024px){
.about__grid{grid-template-columns:1fr;gap:7.2rem;}
.about__img{height:440px;}
.wi:nth-child(1),.wi:nth-child(2){grid-column:1/13;}
.wi:nth-child(3),.wi:nth-child(4),.wi:nth-child(5){grid-column:span 4;}
.glass-cards{flex-wrap:wrap;justify-content:center;}
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
.cursor{display:none;}
body{cursor:auto;}
.glass-cards{flex-direction:column;align-items:center;}
}
</style>
</head>
<body>

<!-- NOISE -->
<div class="noise"></div>

<!-- PAGE TRANSITION -->
<div id="pt"></div>

<!-- CURSOR -->
<div class="cursor">
  <div class="cursor__dot"></div>
  <div class="cursor__ring"><span class="cr-txt">VIEW</span></div>
</div>

<!-- PRELOADER -->
<div class="preloader" id="preloader">
  <div class="pre__logo"><span class="pre__logo-inner">Vortex</span></div>
  <div class="pre__bar"><div class="pre__fill" id="pre-fill"></div></div>
  <div class="pre__num" id="pre-num">0%</div>
</div>

<!-- NAV -->
<nav class="nav" id="nav">
  <a href="#" class="nav__logo">
    <div class="nav__mark"><div class="nav__mark-dot"></div></div>
    Vortex
  </a>
  <ul class="nav__links">
    <li><a href="#about">Studio</a></li>
    <li><a href="#works">Works</a></li>
    <li><a href="#services">Services</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
  <a href="#contact" class="vb-neon-flick">Start Project</a>
</nav>

<!-- HERO -->
<section class="hero" id="hero">
  <div class="hero__bg">
    <img id="hero-img" src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=2200&q=90&auto=format&fit=crop" loading="eager">
  </div>
  <div class="hero__content">
    <div class="hero__eyebrow"><span>Digital Studio \u2014 2025</span></div>
    <h1 class="hero__title" id="hero-h">
      <span class="line"><span class="line-i">We Craft</span></span>
      <span class="line"><span class="line-i"><em>Digital</em></span></span>
      <span class="line"><span class="line-i">Excellence.</span></span>
    </h1>
    <div class="hero__bottom">
      <p class="hero__desc" id="hero-desc">Award-winning digital studio specializing in brand identity, immersive web experiences, and motion design for visionary brands.</p>
      <div class="hero__actions" id="hero-act">
        <a href="#works" class="btn btn--fill">View Work <span class="btn-arrow">\u2192</span></a>
        <a href="#about" class="btn btn--line">Our Story <span class="btn-arrow">\u2192</span></a>
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
      <span>Digital Direction</span><span>UI/UX Design</span><span>Web Development</span><span>Motion Design</span><span>Brand Identity</span><span>Creative Strategy</span><span>3D Experiences</span>
    </div>
    <div class="marquee__run" aria-hidden="true">
      <span>Digital Direction</span><span>UI/UX Design</span><span>Web Development</span><span>Motion Design</span><span>Brand Identity</span><span>Creative Strategy</span><span>3D Experiences</span>
    </div>
  </div>
</div>

<!-- ABOUT -->
<section class="about" id="about">
  <div class="container">
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
        <!-- CA43 GLASS CARDS -->
        <div class="glass-cards" id="glass-cards">
          <div class="gc"><div class="gc-inner"><span class="gc-icon">\u2726</span><span class="gc-title">Processing</span><span class="gc-desc">High-end design functions that bring creative beauty to form</span></div></div>
          <div class="gc"><div class="gc-inner"><span class="gc-icon">\u25A8</span><span class="gc-title">Growth Archive</span><span class="gc-desc">Set-up templates and choices for different project varieties</span></div></div>
        </div>
      </div>
      <div class="about__img" id="about-img">
        <div class="about__img-inner" id="about-img-i">
          <img src="https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=1400&q=90&auto=format&fit=crop">
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PARALLAX FULLBLEED -->
<div class="pb" id="pb">
  <div class="pb__bg" id="pb-bg"><img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=2200&q=90&auto=format&fit=crop"></div>
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

<!-- WORKS -->
<section class="works" id="works">
  <div class="container">
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
      <div class="wi" data-cat="brand"><img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1400&q=85&auto=format&fit=crop"><div class="wi__ov"><span class="wi__cat">Brand Identity</span><span class="wi__name">Lumi\u00E8re Studio</span></div></div>
      <div class="wi" data-cat="web"><img src="https://images.unsplash.com/photo-1547658719-da2b51169166?w=1000&q=85&auto=format&fit=crop"><div class="wi__ov"><span class="wi__cat">Web Design</span><span class="wi__name">Nexus Platform</span></div></div>
      <div class="wi" data-cat="digital"><img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=900&q=85&auto=format&fit=crop"><div class="wi__ov"><span class="wi__cat">Digital Art</span><span class="wi__name">Prism Collection</span></div></div>
      <div class="wi" data-cat="brand"><img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=900&q=85&auto=format&fit=crop"><div class="wi__ov"><span class="wi__cat">Brand Strategy</span><span class="wi__name">Vertex Analytics</span></div></div>
      <div class="wi" data-cat="web"><img src="https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=900&q=85&auto=format&fit=crop"><div class="wi__ov"><span class="wi__cat">Web Development</span><span class="wi__name">Aurora Dashboard</span></div></div>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="services" id="services">
  <div class="container">
    <div class="s-tag"><span>What We Do</span></div>
    <div class="svc__list">
      <div class="svc-item"><span class="svc-item__n">01</span><span class="svc-item__t">Brand Identity &amp; Strategy</span><span class="svc-item__a">\u2192</span></div>
      <div class="svc-item"><span class="svc-item__n">02</span><span class="svc-item__t">UI/UX Design &amp; Prototyping</span><span class="svc-item__a">\u2192</span></div>
      <div class="svc-item"><span class="svc-item__n">03</span><span class="svc-item__t">Web Development &amp; Engineering</span><span class="svc-item__a">\u2192</span></div>
      <div class="svc-item"><span class="svc-item__n">04</span><span class="svc-item__t">Motion Design &amp; Animation</span><span class="svc-item__a">\u2192</span></div>
      <div class="svc-item"><span class="svc-item__n">05</span><span class="svc-item__t">3D &amp; Immersive Experiences</span><span class="svc-item__a">\u2192</span></div>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="cta" id="contact">
  <div class="container">
    <p class="cta__sub" id="cta-sub">Ready to start?</p>
    <h2 class="cta__title" id="cta-h">
      <span class="line"><span class="line-i">Let\u2019s Build</span></span>
      <span class="line"><span class="line-i">Something <em>Iconic.</em></span></span>
    </h2>
    <div class="cta__btns" id="cta-btns">
      <a href="mailto:hello@vortex.studio" class="btn btn--fill btn--xl">Start a Project <span class="btn-arrow">\u2192</span></a>
      <a href="#works" class="btn btn--line">View Our Work</a>
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

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"><\/script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"><\/script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.14/dist/lenis.min.js"><\/script>
<script>
(function(){
  gsap.registerPlugin(ScrollTrigger);

  /* LENIS */
  var lenis = new Lenis({ duration: 1.2, easing: function(t){ return Math.min(1, 1.001 - Math.pow(2, -10 * t)); } });
  lenis.on("scroll", ScrollTrigger.update);
  gsap.ticker.add(function(time){ lenis.raf(time * 1000); });
  gsap.ticker.lagSmoothing(0);

  /* CURSOR */
  var dot = document.querySelector(".cursor__dot");
  var ring = document.querySelector(".cursor__ring");
  var rx = 0, ry = 0, mx = 0, my = 0;
  document.addEventListener("mousemove", function(e){
    mx = e.clientX; my = e.clientY;
    gsap.to(dot, { x: mx, y: my, duration: 0.08 });
  });
  gsap.ticker.add(function(){
    rx += (mx - rx) * 0.11;
    ry += (my - ry) * 0.11;
    gsap.set(ring, { x: rx, y: ry });
  });
  document.querySelectorAll("a,button,.btn,.vb-neon-flick").forEach(function(el){
    el.addEventListener("mouseenter", function(){ document.body.classList.add("c-hover"); });
    el.addEventListener("mouseleave", function(){ document.body.classList.remove("c-hover"); });
  });

  /* PRELOADER */
  var preFill = document.getElementById("pre-fill");
  var preNum = document.getElementById("pre-num");
  var preloader = document.getElementById("preloader");
  var prog = 0;
  gsap.to(".pre__logo-inner", { y: "0%", duration: 0.8, ease: "power3.out" });
  var tick = setInterval(function(){
    prog += Math.random() * 14;
    if(prog > 100) prog = 100;
    preFill.style.width = prog + "%";
    preNum.textContent = Math.floor(prog) + "%";
    if(prog >= 100){ clearInterval(tick); setTimeout(closePreloader, 300); }
  }, 70);

  function closePreloader(){
    gsap.to(preloader, {
      opacity: 0, duration: 0.8, ease: "power2.inOut",
      onComplete: function(){ preloader.style.display = "none"; initHero(); }
    });
  }

  /* SCRAMBLE */
  function scrambleText(el, duration){
    duration = duration || 1200;
    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*";
    var final2 = el.textContent;
    var total = final2.length;
    var start = performance.now();
    el.style.fontVariantNumeric = "tabular-nums";
    function tk(now){
      var elapsed = now - start;
      var progress = Math.min(elapsed / duration, 1);
      var revealed = Math.floor(progress * total);
      var result = "";
      for(var i = 0; i < total; i++){
        if(final2[i] === " "){ result += " "; continue; }
        if(i < revealed) result += final2[i];
        else result += chars[Math.floor(Math.random() * chars.length)];
      }
      el.textContent = result;
      if(progress < 1) requestAnimationFrame(tk);
      else el.textContent = final2;
    }
    requestAnimationFrame(tk);
  }

  /* HERO INIT */
  function initHero(){
    var tl = gsap.timeline();
    tl.from("#hero-img", { scale: 1.12, duration: 2.2, ease: "power2.out" }, 0);
    tl.to(".hero__title .line-i", { y: "0%", duration: 1.25, stagger: 0.12, ease: "power4.out" }, 0.18);
    tl.from(".hero__eyebrow", { opacity: 0, x: -16, duration: 0.7 }, 0.5);
    tl.to(["#hero-desc","#hero-act"], { opacity: 1, y: 0, duration: 0.85, stagger: 0.18 }, 0.9);
    tl.to("#hero-scroll", { opacity: 1, duration: 0.6 }, 1.3);
    tl.from("#nav", { y: -20, opacity: 0, duration: 0.9, ease: "power4.out" }, 0.2);
    tl.add(function(){
      scrambleText(document.querySelector(".hero__title .line-i:last-child"), 1200);
      initScroll();
    }, 1.5);
  }

  /* KINETIC TYPOGRAPHY */
  var heroEl = document.getElementById("hero");
  if(heroEl){
    heroEl.addEventListener("mousemove", function(e){
      gsap.to("#hero-h", {
        rotationY: (e.clientX / window.innerWidth - 0.5) * 6,
        rotationX: -(e.clientY / window.innerHeight - 0.5) * 4,
        transformPerspective: 800, duration: 0.8, ease: "power2.out"
      });
    });
    heroEl.addEventListener("mouseleave", function(){
      gsap.to("#hero-h", { rotationY: 0, rotationX: 0, duration: 1 });
    });
  }

  /* ALL SCROLL TRIGGERS */
  function initScroll(){
    /* NAV SCROLL */
    ScrollTrigger.create({
      start: "top -100",
      onUpdate: function(self){
        if(self.direction === 1) document.getElementById("nav").classList.add("scrolled");
        if(self.scroll() < 100) document.getElementById("nav").classList.remove("scrolled");
      }
    });

    /* MARQUEE DIRECTION */
    lenis.on("scroll", function(e){
      document.querySelectorAll(".marquee__run").forEach(function(el){
        el.style.animationDirection = e.direction === -1 ? "reverse" : "normal";
      });
    });

    /* ABOUT TITLE */
    ScrollTrigger.create({
      trigger: "#about-h", start: "top 82%",
      onEnter: function(){ gsap.to(".ri", { y: "0%", duration: 1.25, stagger: 0.1, ease: "power4.out" }); }
    });
    ScrollTrigger.create({
      trigger: "#about-p", start: "top 82%",
      onEnter: function(){
        gsap.to("#about-p", { opacity: 1, y: 0, duration: 0.85 });
        gsap.to("#about-stats", { opacity: 1, y: 0, duration: 0.85, delay: 0.2 });
        gsap.to("#glass-cards", { opacity: 1, y: 0, duration: 0.85, delay: 0.4 });
        /* COUNTERS */
        document.querySelectorAll(".stat__n").forEach(function(el){
          var target = parseInt(el.dataset.target);
          var suffix = el.dataset.suffix || "";
          gsap.to({ val: 0 }, {
            val: target, duration: 2, ease: "power2.out", snap: { val: 1 },
            onUpdate: function(){ el.textContent = Math.floor(this.targets()[0].val) + suffix; }
          });
        });
      }
    });

    /* ABOUT IMAGE PARALLAX */
    ScrollTrigger.create({
      trigger: "#about-img", start: "top bottom", end: "bottom top",
      onUpdate: function(self){ gsap.set("#about-img-i", { y: self.progress * -90 }); }
    });

    /* PARALLAX BAND */
    ScrollTrigger.create({
      trigger: "#pb", start: "top bottom", end: "bottom top",
      onUpdate: function(self){ gsap.set("#pb-bg", { y: self.progress * 140 - 70 }); }
    });
    ScrollTrigger.create({
      trigger: "#pb-q", start: "top 78%",
      onEnter: function(){ gsap.to("#pb-q", { opacity: 1, y: 0, duration: 1.2, ease: "power3.out" }); }
    });

    /* VIDEO REVEAL */
    ScrollTrigger.create({
      trigger: "#vid", start: "top 72%",
      onEnter: function(){
        gsap.to("#v-wrap", { clipPath: "inset(0% 0 0 0)", duration: 1.5, ease: "power4.inOut" });
        gsap.to("#v-label", { opacity: 1, duration: 0.8, delay: 1.2 });
      }
    });

    /* WORKS REVEAL */
    gsap.utils.toArray(".wi").forEach(function(el, i){
      ScrollTrigger.create({
        trigger: el, start: "top 88%",
        onEnter: function(){
          gsap.to(el, { opacity: 1, y: 0, duration: 0.95, delay: (i % 3) * 0.1, ease: "power3.out" });
        }
      });
    });

    /* SERVICES REVEAL */
    gsap.utils.toArray(".svc-item").forEach(function(el, i){
      ScrollTrigger.create({
        trigger: el, start: "top 88%",
        onEnter: function(){
          gsap.to(el, { opacity: 1, y: 0, duration: 0.65, delay: i * 0.07, ease: "power3.out" });
        }
      });
    });

    /* CTA REVEAL */
    ScrollTrigger.create({
      trigger: "#cta-sub", start: "top 82%",
      onEnter: function(){
        gsap.to("#cta-sub", { opacity: 1, duration: 0.6 });
        gsap.to(".cta__title .line-i", { y: "0%", duration: 1.25, stagger: 0.12, ease: "power4.out", delay: 0.1 });
        gsap.to("#cta-btns", { opacity: 1, duration: 0.85, delay: 0.55 });
        setTimeout(function(){
          var iconic = document.querySelector(".cta__title em");
          if(iconic) scrambleText(iconic, 1200);
        }, 400);
      }
    });
  }

  /* WORKS FOCUS EFFECT */
  document.querySelectorAll(".wi").forEach(function(item){
    item.addEventListener("mouseenter", function(){
      document.body.classList.add("c-view");
      document.querySelectorAll(".wi").forEach(function(other){
        if(other !== item) gsap.to(other, { opacity: 0.35, duration: 0.4 });
      });
    });
    item.addEventListener("mouseleave", function(){
      document.body.classList.remove("c-view");
      document.querySelectorAll(".wi").forEach(function(other){
        gsap.to(other, { opacity: 1, duration: 0.4 });
      });
    });
  });

  /* WORKS FILTERS */
  document.querySelectorAll(".wf").forEach(function(btn){
    btn.addEventListener("click", function(){
      var filter = btn.dataset.filter;
      var items = document.querySelectorAll(".wi");
      var before = [];
      items.forEach(function(el){ before.push(el.getBoundingClientRect()); });
      items.forEach(function(el){
        el.style.display = (filter === "all" || el.dataset.cat === filter) ? "" : "none";
      });
      items.forEach(function(el, i){
        if(el.style.display === "none") return;
        var after = el.getBoundingClientRect();
        var dx = before[i].left - after.left;
        var dy = before[i].top - after.top;
        gsap.from(el, { x: dx, y: dy, duration: 0.6, ease: "power3.out" });
      });
      document.querySelectorAll(".wf").forEach(function(b){ b.classList.remove("active"); });
      btn.classList.add("active");
    });
  });

  /* MAGNETIC BUTTONS */
  document.querySelectorAll(".btn--fill").forEach(function(btn){
    btn.addEventListener("mousemove", function(e){
      var rect = btn.getBoundingClientRect();
      var ox = e.clientX - rect.left - rect.width / 2;
      var oy = e.clientY - rect.top - rect.height / 2;
      gsap.to(btn, { x: ox * 0.28, y: oy * 0.28, duration: 0.4, ease: "power2.out" });
    });
    btn.addEventListener("mouseleave", function(){
      gsap.to(btn, { x: 0, y: 0, duration: 0.7, ease: "elastic.out(1,0.5)" });
    });
  });

  /* PAGE TRANSITIONS */
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener("click", function(e){
      e.preventDefault();
      var target = document.querySelector(this.getAttribute("href"));
      if(!target) return;
      var pt = document.getElementById("pt");
      gsap.timeline()
        .to(pt, { scaleY: 1, duration: 0.5, ease: "power3.inOut", transformOrigin: "bottom" })
        .add(function(){ lenis.scrollTo(target, { duration: 0, immediate: true }); })
        .to(pt, { scaleY: 0, duration: 0.6, ease: "power3.inOut", transformOrigin: "top", delay: 0.05 });
    });
  });
})();
<\/script>
</body>
</html>'''

# Now convert to JS string: escape single quotes, backslashes, newlines
# First escape existing backslashes
js_str = tpl_html.replace('\\', '\\\\')
# Escape single quotes
js_str = js_str.replace("'", "\\'")
# Escape newlines
js_str = js_str.replace('\n', '\\n')

new_template = f"TPL_ECOM_HTML['4'] = function () {{\n  return '{js_str}';\n}};\n\n"

# Verify: parse the JS string to check for issues
# Count that quotes are balanced
in_escape = False
problems = []
ret_start = new_template.index("return '") + 8
ret_end = new_template.rindex("';")
s = new_template[ret_start:ret_end]
i = 0
while i < len(s):
    if s[i] == '\\':
        i += 2
        continue
    if s[i] == "'":
        ctx = s[max(0,i-30):i+30]
        problems.append(f"Unescaped quote at pos {i}: ...{ctx}...")
    i += 1

if problems:
    print("QUOTE PROBLEMS:")
    for p in problems[:10]:
        print(p)
    raise SystemExit(1)

print(f"Quote check OK! Template length: {len(new_template)} chars")

# Replace in file
content = content[:start_idx] + new_template + content[actual_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Template 4 replaced successfully!")
