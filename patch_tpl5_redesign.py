#!/usr/bin/env python3
"""
REDESIGN TOTAL — NOVUS Capital TPL_ECOM_HTML['5']
Replaces color system + adds buttons/patterns/transitions/effects.
"""

filepath = r"C:\vantage-clean\crm-v2-push\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

tpl_start = content.index("TPL_ECOM_HTML['5']")
tpl_end = content.index("TPL_ECOM_HTML['9']")
tpl = content[tpl_start:tpl_end]

print(f"Template size before: {len(tpl)}")

# ============================================================
# STEP 1: Replace :root variables block
# ============================================================
import re

old_root = re.search(r':root\{[^}]+\}', tpl).group()
new_root = (
    ":root{"
    "--void:#080F14;--deep:#0B1720;--mid:#101F2B;--surface:#172838;--lifted:#1E3142;"
    "--border:#263D50;--border-dim:rgba(38,61,80,0.6);"
    "--ivory:#F2EDE4;--cream:#E5DDD0;--sand:#C4BBAC;--muted:#8A9BAA;"
    "--sage:#3D8B7A;--sage-light:#5AA897;--sage-pale:#A8D4CB;"
    "--sage-dim:rgba(61,139,122,0.12);--sage-glow:rgba(61,139,122,0.25);"
    "--terra:#C4714F;--terra-light:#D98E70;--terra-pale:#E8C4B0;"
    "--terra-dim:rgba(196,113,79,0.12);"
    "--plat:#7A9DB0;--plat-light:#9BBCCE;--plat-dim:rgba(122,157,176,0.15);"
    "--champ:#D4B896;--champ-light:#E4CCAE;--champ-dim:rgba(212,184,150,0.1);"
    "--green:#4DB896;--amber:#D4A45A;--rose:#C47070;"
    "--font-d:\\'Cormorant Garamond\\',serif;"
    "--font-b:\\'DM Sans\\',sans-serif;"
    "--font-m:\\'DM Mono\\',monospace;"
    "--ease-out:cubic-bezier(0.16,1,0.3,1);"
    "--ease-io:cubic-bezier(0.76,0,0.24,1);"
    "--ease-expo:cubic-bezier(0.19,1,0.22,1);"
    "--ease-back:cubic-bezier(0.34,1.56,0.64,1);"
    "--shadow-sage:0 0 40px rgba(61,139,122,0.2);"
    "--shadow-terra:0 0 40px rgba(196,113,79,0.15);"
    "--shadow-lift:0 24px 60px rgba(8,15,20,0.5);"
    "--shadow-card:0 8px 32px rgba(8,15,20,0.4);"
    "--grad-sage:linear-gradient(135deg,var(--sage) 0%,var(--sage-light) 100%);"
    "--grad-terra:linear-gradient(135deg,var(--terra) 0%,var(--terra-light) 100%);"
    "}"
)

tpl = tpl.replace(old_root, new_root)
print("Step 1: :root replaced")

# ============================================================
# STEP 2: Replace color variable references
# ============================================================

# Main replacements (order matters - longer first)
color_replacements = [
    ('var(--gold-bright)', 'var(--sage-light)'),
    ('var(--gold-dim)',    'var(--sage-dim)'),
    ('var(--gold)',        'var(--sage)'),
    ('var(--black-warm)',  'var(--mid)'),
    ('var(--black)',       'var(--deep)'),
    ('var(--dark4)',       'var(--lifted)'),
    ('var(--dark3)',       'var(--surface)'),
    ('var(--dark2)',       'var(--mid)'),
    ('var(--white)',       'var(--ivory)'),
    ('var(--silver-light)','var(--sand)'),
    ('var(--silver)',      'var(--muted)'),
    ('var(--cream)',       'var(--cream)'),  # same name, keep
]

for old, new in color_replacements:
    count = tpl.count(old)
    tpl = tpl.replace(old, new)
    if count > 0:
        print(f"  {old} -> {new}: {count} replacements")

# Replace rgba gold references -> rgba sage
# rgba(184,149,63,X) -> rgba(61,139,122,X)
tpl = re.sub(r'rgba\(184,149,63,([^)]+)\)', r'rgba(61,139,122,\1)', tpl)
print(f"  rgba gold -> rgba sage: done")

# Replace rgba white/ivory references -> keep but adjust
# rgba(245,242,237,X) stays similar but map to ivory tones
# Actually these are fine as-is for opacity overlays, leave them

# Replace hex gold values
tpl = tpl.replace('#B8953F', '#3D8B7A')
tpl = tpl.replace('#D4AF5A', '#5AA897')
tpl = tpl.replace('#f5f2ed', '#F2EDE4')

# Replace body background
tpl = tpl.replace('background:var(--void)', 'background:var(--deep)')

# Fix specific gold references in addons CSS that use literal values
# rgba(184,149,63 already handled above

# Fix #4ade80 (green) stays
# Fix #fbbf24 (amber) stays

print("Step 2: Color replacements done")

# ============================================================
# STEP 3: Add new CSS (buttons, patterns, transitions, effects)
# ============================================================

NEW_CSS = r"""
/* ============================================================
   BTN-01 — LIQUID BLOB
============================================================ */
.btn-blob{position:relative;display:inline-flex;align-items:center;gap:1.4rem;padding:1.8rem 4rem;overflow:hidden;cursor:none;background:var(--sage);color:var(--ivory);font-family:var(--font-m);font-size:1.1rem;letter-spacing:.15em;text-transform:uppercase;transition:color .3s;clip-path:polygon(0 0,100% 0,100% 100%,0 100%);}
.btn-blob__bg{position:absolute;width:200%;height:200%;background:var(--sage-light);border-radius:50%;transform:translate(-50%,-50%) scale(0);transition:transform .6s var(--ease-expo);pointer-events:none;left:50%;top:50%;z-index:0;}
.btn-blob:hover .btn-blob__bg{transform:translate(-50%,-50%) scale(1.2);}
.btn-blob__text,.btn-blob__arrow{position:relative;z-index:1;transition:letter-spacing .4s var(--ease-out);}
.btn-blob:hover .btn-blob__text{letter-spacing:.22em;}
.btn-blob__arrow{display:inline-block;transition:transform .4s var(--ease-out);}
.btn-blob:hover .btn-blob__arrow{transform:translateX(6px);}
.btn-blob--terra{background:var(--terra);}.btn-blob--terra .btn-blob__bg{background:var(--terra-light);}
.btn-blob--dark{background:var(--surface);border:1px solid var(--border);}.btn-blob--dark .btn-blob__bg{background:var(--sage-dim);}.btn-blob--dark:hover{border-color:var(--sage);}

/* ============================================================
   BTN-02 — CUT CORNER
============================================================ */
.btn-cut{position:relative;display:inline-flex;align-items:center;gap:1.6rem;padding:1.6rem 3.2rem 1.6rem 2.8rem;background:transparent;border:1px solid var(--plat);color:var(--ivory);font-family:var(--font-m);font-size:1.1rem;letter-spacing:.15em;text-transform:uppercase;cursor:none;clip-path:polygon(0 0,calc(100% - 16px) 0,100% 16px,100% 100%,0 100%);transition:background .4s,border-color .4s,clip-path .4s var(--ease-out);overflow:hidden;}
.btn-cut::before{content:\\'\\';position:absolute;top:-1px;right:-1px;width:0;height:0;border-style:solid;border-width:0 18px 18px 0;border-color:transparent var(--plat) transparent transparent;transition:border-color .4s;}
.btn-cut::after{content:\\'\\';position:absolute;inset:0;background:var(--sage-dim);transform:scaleX(0);transform-origin:left;transition:transform .5s var(--ease-out);}
.btn-cut:hover{border-color:var(--sage);clip-path:polygon(0 0,100% 0,100% 0,100% 100%,0 100%);}
.btn-cut:hover::before{border-color:transparent var(--sage) transparent transparent;}
.btn-cut:hover::after{transform:scaleX(1);}
.btn-cut span{position:relative;z-index:1;}
.btn-cut__icon{transition:transform .4s var(--ease-out);}.btn-cut:hover .btn-cut__icon{transform:translate(3px,-3px);}

/* ============================================================
   BTN-03 — GRADIENT BORDER
============================================================ */
.btn-glow{position:relative;display:inline-flex;cursor:none;padding:2px;background:conic-gradient(from var(--angle,0deg),var(--sage) 0%,var(--plat) 25%,var(--terra) 50%,var(--champ) 75%,var(--sage) 100%);animation:glow-rotate 3s linear infinite;}
@keyframes glow-rotate{to{--angle:360deg;}}
.btn-glow__inner{display:flex;align-items:center;gap:1.2rem;padding:1.6rem 3.6rem;background:var(--deep);color:var(--ivory);font-family:var(--font-m);font-size:1.1rem;letter-spacing:.15em;text-transform:uppercase;transition:background .4s;position:relative;z-index:1;white-space:nowrap;}
.btn-glow:hover .btn-glow__inner{background:var(--sage-dim);}

/* ============================================================
   BTN-04 — SPLIT REVEAL
============================================================ */
.btn-split{position:relative;display:inline-flex;align-items:center;overflow:hidden;cursor:none;font-family:var(--font-m);font-size:1.1rem;letter-spacing:.15em;text-transform:uppercase;padding:1.6rem 0;color:var(--ivory);height:5rem;}
.btn-split__default,.btn-split__hover{display:block;transition:transform .5s var(--ease-out),opacity .4s ease;white-space:nowrap;}
.btn-split__hover{position:absolute;top:100%;left:0;color:var(--sage);}
.btn-split:hover .btn-split__default{transform:translateY(-120%);opacity:0;}
.btn-split:hover .btn-split__hover{transform:translateY(-100%);}
.btn-split--lined{border-bottom:1px solid var(--border);padding-bottom:.8rem;transition:border-color .3s;}.btn-split--lined:hover{border-color:var(--sage);}

/* ============================================================
   BTN-05 — CIRCLE EXPAND
============================================================ */
.btn-circle{position:relative;display:inline-flex;align-items:center;justify-content:center;padding:1.8rem 4.4rem;background:transparent;border:1px solid rgba(61,139,122,.5);color:var(--sage);font-family:var(--font-m);font-size:1.1rem;letter-spacing:.18em;text-transform:uppercase;cursor:none;overflow:hidden;transition:color .35s ease,border-color .35s;}
.btn-circle__fill{position:absolute;width:0;height:0;background:var(--sage);border-radius:50%;transform:translate(-50%,-50%);transition:width .65s var(--ease-expo),height .65s var(--ease-expo);left:50%;top:50%;z-index:0;}
.btn-circle:hover{color:var(--deep);border-color:var(--sage);}
.btn-circle:hover .btn-circle__fill{width:400%;height:400%;}
.btn-circle__text{position:relative;z-index:1;transition:letter-spacing .4s var(--ease-out);}.btn-circle:hover .btn-circle__text{letter-spacing:.24em;}
.btn-circle--terra{border-color:rgba(196,113,79,.5);color:var(--terra);}.btn-circle--terra .btn-circle__fill{background:var(--terra);}.btn-circle--terra:hover{color:var(--ivory);border-color:var(--terra);}

/* ============================================================
   BTN-06 — MAGNETIC OUTLINE
============================================================ */
.btn-mag{position:relative;display:inline-flex;align-items:center;justify-content:center;padding:1.4rem 3.2rem;color:var(--ivory);font-family:var(--font-m);font-size:1.1rem;letter-spacing:.15em;text-transform:uppercase;cursor:none;overflow:hidden;}
.btn-mag__border{position:absolute;background:var(--sage);transition:transform .4s var(--ease-out);}
.btn-mag__border--top,.btn-mag__border--bottom{left:0;width:100%;height:1px;transform:scaleX(0);transform-origin:left;}
.btn-mag__border--top{top:0;}.btn-mag__border--bottom{bottom:0;transform-origin:right;}
.btn-mag__border--left,.btn-mag__border--right{top:0;height:100%;width:1px;transform:scaleY(0);transform-origin:bottom;}
.btn-mag__border--left{left:0;}.btn-mag__border--right{right:0;transform-origin:top;}
.btn-mag:hover .btn-mag__border--top{transform:scaleX(1);}.btn-mag:hover .btn-mag__border--right{transform:scaleY(1);}.btn-mag:hover .btn-mag__border--bottom{transform:scaleX(1);}.btn-mag:hover .btn-mag__border--left{transform:scaleY(1);}
.btn-mag__text{position:relative;z-index:1;transition:color .3s;}.btn-mag:hover .btn-mag__text{color:var(--sage);}

/* ============================================================
   BTN-07 — SCRAMBLE TEXT
============================================================ */
.btn-scramble{display:inline-flex;align-items:center;gap:1.2rem;padding:1.4rem 2.8rem;background:rgba(23,40,56,.6);border:1px solid var(--border);color:var(--sand);font-family:var(--font-m);font-size:1rem;letter-spacing:.15em;text-transform:uppercase;cursor:none;transition:border-color .3s,background .3s;backdrop-filter:blur(8px);min-width:200px;}
.btn-scramble:hover{border-color:var(--plat);background:var(--plat-dim);color:var(--ivory);}
.btn-scramble__text{font-variant-numeric:tabular-nums;}

/* ============================================================
   BTN-08 — STAGGER LETTERS
============================================================ */
.btn-letters{display:inline-flex;align-items:center;gap:0;padding:2rem 4.8rem;background:var(--sage);color:var(--deep);font-family:var(--font-m);font-size:1.2rem;letter-spacing:.2em;text-transform:uppercase;cursor:none;overflow:hidden;position:relative;}
.btn-letters__char{display:inline-block;transition:transform .3s var(--ease-back);will-change:transform;}
.btn-letters:hover .btn-letters__char{animation:letter-bounce .5s var(--ease-back) forwards;}
@keyframes letter-bounce{0%{transform:translateY(0);}40%{transform:translateY(-8px);}70%{transform:translateY(3px);}100%{transform:translateY(0);}}

/* ============================================================
   PAT-04 — BLUEPRINT GRID
============================================================ */
.pat-blueprint{background-image:linear-gradient(rgba(122,157,176,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(122,157,176,.06) 1px,transparent 1px),linear-gradient(rgba(122,157,176,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(122,157,176,.03) 1px,transparent 1px);background-size:120px 120px,120px 120px,24px 24px,24px 24px;animation:blueprint-shift 60s linear infinite;}
@keyframes blueprint-shift{to{background-position:120px 120px,120px 120px,24px 24px,24px 24px;}}

/* ============================================================
   PAT-05 — DIAGONAL NOISE
============================================================ */
.pat-diagonal{background-image:repeating-linear-gradient(-45deg,transparent,transparent 4px,rgba(61,139,122,.035) 4px,rgba(61,139,122,.035) 5px);animation:diag-drift 20s linear infinite;}
@keyframes diag-drift{to{background-position:100px 100px;}}

/* ============================================================
   TRANS-01 — DIAGONAL WIPE
============================================================ */
.section-diagonal{clip-path:polygon(0 0,0 0,0 100%,0 100%);}
.section-diagonal.in-view{clip-path:polygon(0 0,100% 0,100% 100%,0 100%);transition:clip-path 1.2s var(--ease-expo);}

/* ============================================================
   TRANS-02 — BLUR DISSOLVE
============================================================ */
.blur-reveal{opacity:0;filter:blur(20px);transform:scale(1.04);transition:opacity .9s var(--ease-out),filter .9s var(--ease-out),transform .9s var(--ease-out);}
.blur-reveal.visible{opacity:1;filter:blur(0);transform:scale(1);}

/* ============================================================
   TRANS-03 — SCALE FROM CORNER
============================================================ */
.scale-corner{transform-origin:bottom left;transform:scale(0.85) rotate(-1deg);opacity:0;transition:transform 1s var(--ease-expo),opacity .8s var(--ease-out);}
.scale-corner.visible{transform:scale(1) rotate(0deg);opacity:1;}

/* ============================================================
   TRANS-04 — LINE DRAW
============================================================ */
.line-draw{display:block;width:0;height:1px;background:var(--sage);transition:width 1.2s var(--ease-expo);}
.line-draw.visible{width:100%;}

/* ============================================================
   TRANS-05 — MORPH CLIP PATH
============================================================ */
.morph-reveal{clip-path:circle(0% at 50% 50%);transition:clip-path 1.4s var(--ease-expo);}
.morph-reveal.visible{clip-path:circle(150% at 50% 50%);}
.morph-reveal--down{clip-path:inset(0 0 100% 0);transition:clip-path 1.2s var(--ease-expo);}
.morph-reveal--down.visible{clip-path:inset(0 0 0% 0);}

/* ============================================================
   TRANS-06 — GLITCH FLASH
============================================================ */
.glitch-reveal{position:relative;opacity:0;}
.glitch-reveal.visible{opacity:1;animation:glitch-in .8s var(--ease-out) forwards;}
@keyframes glitch-in{0%{opacity:0;transform:translateX(-4px);clip-path:inset(0 100% 0 0);}15%{transform:translateX(3px);clip-path:inset(0 60% 0 0);}30%{transform:translateX(-2px);clip-path:inset(0 30% 0 0);}50%{transform:translateX(1px);clip-path:inset(0 10% 0 0);}70%{transform:translateX(-1px);clip-path:inset(0 2% 0 0);}100%{opacity:1;transform:translateX(0);clip-path:inset(0 0% 0 0);}}

/* ============================================================
   EFF-01 — MAGNETIC DIVIDERS
============================================================ */
.mag-divider{position:relative;width:100%;overflow:hidden;}

/* ============================================================
   EFF-02 — AMBIENT LIGHT CURSOR
============================================================ */
.ambient-light{position:fixed;top:0;left:0;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(61,139,122,.06) 0%,transparent 70%);transform:translate(-50%,-50%);pointer-events:none;z-index:1;transition:background .8s ease;will-change:transform;}
.ambient-light--terra{background:radial-gradient(circle,rgba(196,113,79,.05) 0%,transparent 70%);}
.ambient-light--plat{background:radial-gradient(circle,rgba(122,157,176,.05) 0%,transparent 70%);}

/* ============================================================
   EFF-03 — TEXT REVEAL PAR MASQUE
============================================================ */
.title-masked{font-family:var(--font-d);font-weight:300;line-height:1;}
.title-masked em{font-style:italic;color:var(--sage);}
.tm-line{display:block;overflow:hidden;}
.tm-mask{display:block;overflow:hidden;}
.tm-inner{display:block;transform:translateY(108%);transition:transform 1.2s var(--ease-expo);}
.title-masked.visible .tm-line:nth-child(1) .tm-inner{transform:translateY(0);}
.title-masked.visible .tm-line:nth-child(2) .tm-inner{transform:translateY(0);transition-delay:.1s;}
.title-masked.visible .tm-line:nth-child(3) .tm-inner{transform:translateY(0);transition-delay:.2s;}

/* ============================================================
   RESPONSIVE ADD
============================================================ */
@media(max-width:768px){
.flip-grid{grid-template-columns:1fr;}
.flip-card{height:420px;}
.mortgage-grid{grid-template-columns:1fr;gap:4rem;}
.market-grid{grid-template-columns:1fr;gap:3rem;}
.ad-kpis{grid-template-columns:repeat(2,1fr);}
.ad-booking-row{grid-template-columns:1fr 1fr;}
.ad-props{grid-template-columns:1fr;}
.compare-bar{left:1.6rem;right:1.6rem;flex-direction:column;gap:1.2rem;}
.rc-inputs{grid-template-columns:1fr;}
.rc-results{grid-template-columns:repeat(2,1fr);}
}
"""

# Insert CSS before </style>
style_end = tpl.index('</style>')
css_escaped = NEW_CSS.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
tpl = tpl[:style_end] + css_escaped + tpl[style_end:]
print(f"Step 3: CSS injected. Size: {len(tpl)}")

# ============================================================
# STEP 4: Add HTML elements for patterns + effects
# ============================================================

# Add ambient light + mag dividers before </body>
EXTRA_HTML = (
    '<!-- AMBIENT LIGHT -->'
    '<div class="ambient-light" id="ambient-light"></div>'
    '<!-- MAG DIVIDER 1 -->'
    '<div class="mag-divider" id="divider-1">'
    '<svg viewBox="0 0 1440 60" preserveAspectRatio="none" style="width:100%;height:6rem;display:block">'
    '<path id="div-path-1" d="M0,30 Q360,30 720,30 Q1080,30 1440,30" fill="none" stroke="var(--sage)" stroke-width="1" opacity=".3"/>'
    '</svg></div>'
)

body_end = tpl.index('</body>')
html_esc = EXTRA_HTML.replace('\\', '\\\\').replace("'", "\\'")
tpl = tpl[:body_end] + html_esc + tpl[body_end:]
print(f"Step 4: HTML elements added. Size: {len(tpl)}")

# ============================================================
# STEP 5: Add all new JS
# ============================================================

NEW_JS = r"""
/* ============================================================
   BTN-01 — LIQUID BLOB MOUSE FOLLOW
============================================================ */
document.querySelectorAll('.btn-blob').forEach(function(btn){
var bg=btn.querySelector('.btn-blob__bg');
if(!bg)return;
btn.addEventListener('mousemove',function(e){
var r=btn.getBoundingClientRect();
var x=((e.clientX-r.left)/r.width)*100;
var y=((e.clientY-r.top)/r.height)*100;
gsap.to(bg,{left:x+'%',top:y+'%',duration:.4,ease:'power2.out'});
});
btn.addEventListener('mouseleave',function(){gsap.to(bg,{left:'50%',top:'50%',duration:.6,ease:'power3.out'});});
});

/* ============================================================
   BTN-05 — CIRCLE EXPAND FROM HOVER POINT
============================================================ */
document.querySelectorAll('.btn-circle').forEach(function(btn){
var fill=btn.querySelector('.btn-circle__fill');
if(!fill)return;
btn.addEventListener('mouseenter',function(e){
var r=btn.getBoundingClientRect();
gsap.set(fill,{left:e.clientX-r.left,top:e.clientY-r.top});
});
});

/* ============================================================
   BTN-06 — MAGNETIC EFFECT
============================================================ */
document.querySelectorAll('.btn-mag').forEach(function(btn){
btn.addEventListener('mousemove',function(e){
var r=btn.getBoundingClientRect();
var dx=(e.clientX-r.left-r.width/2)*.3;
var dy=(e.clientY-r.top-r.height/2)*.3;
gsap.to(btn,{x:dx,y:dy,duration:.4,ease:'power2.out'});
});
btn.addEventListener('mouseleave',function(){gsap.to(btn,{x:0,y:0,duration:.7,ease:'elastic.out(1,.5)'});});
});

/* ============================================================
   BTN-07 — SCRAMBLE TEXT
============================================================ */
var SCHARS='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
function scrambleTo(el,targetText,duration){
duration=duration||800;
var start=performance.now();
function tick(now){
var p=Math.min((now-start)/duration,1);
var revealed=Math.floor(p*targetText.length);
var result='';
for(var i=0;i<targetText.length;i++){
if(i<revealed)result+=targetText[i];
else result+=SCHARS[Math.floor(Math.random()*SCHARS.length)];
}
el.textContent=result;
if(p<1)requestAnimationFrame(tick);
else el.textContent=targetText;
}
requestAnimationFrame(tick);
}
document.querySelectorAll('.btn-scramble').forEach(function(btn){
var textEl=btn.querySelector('.btn-scramble__text');
var dflt=btn.dataset.textDefault;var hov=btn.dataset.textHover;
if(!textEl||!dflt||!hov)return;
btn.addEventListener('mouseenter',function(){scrambleTo(textEl,hov,700);});
btn.addEventListener('mouseleave',function(){scrambleTo(textEl,dflt,600);});
});

/* ============================================================
   BTN-08 — STAGGER LETTERS INIT
============================================================ */
function initLetterButtons(){
document.querySelectorAll('.btn-letters').forEach(function(btn){
var text=btn.dataset.text||btn.textContent.trim();
btn.innerHTML='';
text.split('').forEach(function(ch,i){
var span=document.createElement('span');
span.className='btn-letters__char';
span.textContent=ch===' '?'\u00A0':ch;
span.style.animationDelay=(i*0.04)+'s';
btn.appendChild(span);
});
});
}
initLetterButtons();

/* ============================================================
   PAT-01 — DOT GRID CANVAS
============================================================ */
function initDotGrid(canvasId,options){
var canvas=document.getElementById(canvasId);
if(!canvas)return;
var ctx=canvas.getContext('2d');
var opts=Object.assign({spacing:32,radius:1.2,color:'rgba(61,139,122,1)',wave:true},options||{});
var W,H,dots=[];
var mouseX=-1000,mouseY=-1000;
function resize(){var r=canvas.parentElement.getBoundingClientRect();W=canvas.width=r.width;H=canvas.height=r.height;
var cols=Math.ceil(W/opts.spacing)+1;var rows=Math.ceil(H/opts.spacing)+1;dots=[];
for(var rr=0;rr<rows;rr++)for(var c=0;c<cols;c++)dots.push({ox:c*opts.spacing,oy:rr*opts.spacing,x:c*opts.spacing,y:rr*opts.spacing,scale:1});}
resize();window.addEventListener('resize',resize);
canvas.parentElement.addEventListener('mousemove',function(e){var r=canvas.getBoundingClientRect();mouseX=e.clientX-r.left;mouseY=e.clientY-r.top;});
canvas.parentElement.addEventListener('mouseleave',function(){mouseX=-1000;mouseY=-1000;});
function draw(t){ctx.clearRect(0,0,W,H);
dots.forEach(function(dot){
var dx=dot.ox-mouseX;var dy=dot.oy-mouseY;var dist=Math.sqrt(dx*dx+dy*dy);var rep=Math.max(0,1-dist/120);
if(opts.wave){dot.x=dot.ox+Math.sin(t*.0008+dot.oy*.05)*3;dot.y=dot.oy+Math.cos(t*.0006+dot.ox*.05)*3;}
dot.x+=dx*rep*.06;dot.y+=dy*rep*.06;dot.scale=1+rep*2;
ctx.beginPath();ctx.arc(dot.x,dot.y,opts.radius*dot.scale,0,Math.PI*2);ctx.fillStyle=opts.color;ctx.fill();
});requestAnimationFrame(draw);}
requestAnimationFrame(draw);
}

/* ============================================================
   EFF-01 — MAGNETIC DIVIDERS
============================================================ */
function initMagDividers(){
document.querySelectorAll('.mag-divider').forEach(function(div){
var path=div.querySelector('path');if(!path)return;
div.addEventListener('mousemove',function(e){
var r=div.getBoundingClientRect();var x=e.clientX-r.left;var y=e.clientY-r.top-r.height/2;
var cp=Math.min(x,r.width-x);
gsap.to(path,{attr:{d:'M0,30 Q'+(x-cp)+','+(30+y*.4)+' '+x+','+(30+y)+' Q'+(x+cp)+','+(30+y*.4)+' 1440,30'},duration:.4,ease:'power2.out'});
});
div.addEventListener('mouseleave',function(){
gsap.to(path,{attr:{d:'M0,30 Q360,30 720,30 Q1080,30 1440,30'},duration:.8,ease:'elastic.out(1,.4)'});
});
});
}
initMagDividers();

/* ============================================================
   EFF-02 — AMBIENT LIGHT CURSOR
============================================================ */
function initAmbientLight(){
var light=document.getElementById('ambient-light');
if(!light)return;
var lx=0,ly=0;
window.addEventListener('mousemove',function(e){lx+=(e.clientX-lx)*.06;ly+=(e.clientY-ly)*.06;gsap.set(light,{x:lx,y:ly});});
}
initAmbientLight();

/* ============================================================
   EFF-03 — TEXT REVEAL MASKED
============================================================ */
document.querySelectorAll('.title-masked').forEach(function(title){
ScrollTrigger.create({trigger:title,start:'top 82%',onEnter:function(){title.classList.add('visible');}});
});

/* ============================================================
   EFF-06 — SECTION COLOR WASH
============================================================ */
var sectionColors=[
{s:'#hero',bg:'#080F14'},{s:'#metrics',bg:'#0B1820'},
{s:'#about',bg:'#091218'},{s:'#properties',bg:'#0E1D28'},
{s:'#performance',bg:'#091520'},{s:'#contact',bg:'#060D12'}
];
sectionColors.forEach(function(sc){
var section=document.querySelector(sc.s);if(!section)return;
ScrollTrigger.create({trigger:section,start:'top 60%',
onEnter:function(){gsap.to(document.body,{backgroundColor:sc.bg,duration:1.2});},
onEnterBack:function(){gsap.to(document.body,{backgroundColor:sc.bg,duration:1.2});}
});
});

/* ============================================================
   EFF-07 — IMAGE TILT 3D
============================================================ */
function initImageTilt(){
document.querySelectorAll('.psi__img-wrap,.flip-card__front').forEach(function(wrap){
wrap.style.transformStyle='preserve-3d';wrap.style.perspective='800px';wrap.style.willChange='transform';
wrap.addEventListener('mousemove',function(e){
var r=wrap.getBoundingClientRect();var x=(e.clientX-r.left)/r.width-.5;var y=(e.clientY-r.top)/r.height-.5;
gsap.to(wrap,{rotationY:x*10,rotationX:-y*8,transformPerspective:800,duration:.4,ease:'power2.out'});
});
wrap.addEventListener('mouseleave',function(){gsap.to(wrap,{rotationY:0,rotationX:0,duration:.8,ease:'elastic.out(1,.6)'});});
});
}
initImageTilt();

/* ============================================================
   EFF-08 — SCROLL VELOCITY SKEW
============================================================ */
function initScrollSkew(){
var currentSkew=0;var lastScroll=0;
gsap.ticker.add(function(){
var scroll=window.scrollY;var velocity=scroll-lastScroll;lastScroll=scroll;
currentSkew+=(velocity*8/window.innerHeight-currentSkew)*.08;
document.querySelectorAll('.props-stack,.about,.flip-section,.mortgage-sec,.market-sec').forEach(function(s){
gsap.set(s,{skewY:Math.max(-2,Math.min(2,currentSkew))});
});
});
}
initScrollSkew();

/* ============================================================
   EFF-10 — CURSOR TRAIL
============================================================ */
function initCursorTrail(){
var particles=[];
document.addEventListener('mousemove',function(e){
var p=document.createElement('div');
p.style.cssText='position:fixed;left:'+e.clientX+'px;top:'+e.clientY+'px;width:4px;height:4px;background:var(--sage);border-radius:50%;pointer-events:none;z-index:9990;transform:translate(-50%,-50%);';
document.body.appendChild(p);particles.push(p);
gsap.to(p,{scale:0,opacity:0,x:(Math.random()-.5)*30,y:(Math.random()-.5)*30,duration:.8,ease:'power2.out',onComplete:function(){p.remove();var idx=particles.indexOf(p);if(idx>-1)particles.splice(idx,1);}});
while(particles.length>36){var old=particles.shift();if(old)old.remove();}
});
}
initCursorTrail();

/* ============================================================
   TRANS REVEALS — blur, scale, glitch, line, diagonal
============================================================ */
document.querySelectorAll('.blur-reveal,.scale-corner,.glitch-reveal,.section-diagonal').forEach(function(el){
ScrollTrigger.create({trigger:el,start:'top 82%',onEnter:function(){el.classList.add('visible');el.classList.add('in-view');}});
});
document.querySelectorAll('.line-draw').forEach(function(line){
ScrollTrigger.create({trigger:line,start:'top 88%',onEnter:function(){line.classList.add('visible');}});
});
"""

# Insert JS before the last script close tag before </body>
body_end = tpl.index('</body>')
last_script_close = tpl.rfind('\\x3c/script>', 0, body_end)
if last_script_close < 0:
    last_script_close = tpl.rfind('<\\/script>', 0, body_end)

if last_script_close < 0:
    print("ERROR: No script close found!")
    import sys; sys.exit(1)

js_escaped = NEW_JS.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
tpl = tpl[:last_script_close] + js_escaped + tpl[last_script_close:]
print(f"Step 5: JS injected. Size: {len(tpl)}")

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

print(f"\nQuotes OK! Final template size: {len(tpl)} chars")

# Write back
content = content[:tpl_start] + tpl + content[tpl_end:]
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("REDESIGN PATCH APPLIED!")
