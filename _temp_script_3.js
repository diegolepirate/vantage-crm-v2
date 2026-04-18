(function(){

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
setInterval(function(){basePrice+=(Math.random()-0.5)*0.08;basePrice=Math.max(48.5,Math.min(49.0,basePrice));var el=document.getElementById("stk-nvs");if(el)el.textContent="\u20AC "+basePrice.toFixed(2);},3000);

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
if(preCanvas){var pCtx=preCanvas.getContext("2d");preCanvas.width=window.innerWidth;preCanvas.height=window.innerHeight;pCtx.strokeStyle="rgba(79,110,247,1)";pCtx.lineWidth=1;pCtx.beginPath();var py=preCanvas.height*.5;pCtx.moveTo(0,py);for(var px=0;px<preCanvas.width;px+=4){py+=(Math.random()-.48)*8;py=Math.max(preCanvas.height*.2,Math.min(preCanvas.height*.8,py));pCtx.lineTo(px,py);}pCtx.stroke();}
gsap.to(".pre__logo-inner",{y:"0%",duration:.9,ease:"power3.out",delay:.2});
gsap.to(".pre__sub-inner",{y:"0%",duration:.7,ease:"power3.out",delay:.5});
var preNums=document.getElementById("pre-numbers");
var pnData=[["\u20AC 4.2B","AUM"],["12,400+","Properties"],["\u20AC 48.72","NVS:PAR"],["98.4%","Occupation"],["27 ans","Expertise"]];
pnData.forEach(function(d){var div=document.createElement("div");div.className="pre__num-item";div.innerHTML="<div style=\"font-size:1.6rem;color:var(--sage);font-family:var(--font-d)\">"+d[0]+"</div><div style=\"font-size:.8rem;letter-spacing:.15em;opacity:.5;margin-top:.3rem\">"+d[1]+"</div>";preNums.appendChild(div);});
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
document.querySelectorAll("a[href^=\"#\"]").forEach(function(a){a.addEventListener("click",function(e){e.preventDefault();var target=document.querySelector(this.getAttribute("href"));if(!target)return;var tl=gsap.timeline();tl.to(".pt__left",{scaleY:1,duration:.55,ease:"power4.inOut"},0);tl.to(".pt__right",{scaleY:1,duration:.55,ease:"power4.inOut",delay:.06},0);tl.add(function(){lenis.scrollTo(target,{offset:-80,duration:0,immediate:true});});tl.to(".pt__left",{scaleY:0,duration:.55,ease:"power4.inOut",transformOrigin:"top",delay:.1});tl.to(".pt__right",{scaleY:0,duration:.55,ease:"power4.inOut",transformOrigin:"bottom",delay:.16});});});

/* Click ripple */
document.addEventListener("click",function(e){var r=document.createElement("div");r.style.cssText="position:fixed;left:"+e.clientX+"px;top:"+e.clientY+"px;width:6px;height:6px;border:1px solid var(--sage);border-radius:50%;transform:translate(-50%,-50%) scale(0);pointer-events:none;z-index:9997;";document.body.appendChild(r);gsap.to(r,{scale:9,opacity:0,duration:1,ease:"power2.out",onComplete:function(){r.remove();}});});

})();

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
var opts=Object.assign({spacing:32,radius:1.2,color:'rgba(79,110,247,1)',wave:true},options||{});
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
  tl.to(clone, { y:-20, boxShadow:'0 40px 80px rgba(7,6,15,.6)', duration:.3, ease:'power2.out' });
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
  toast.style.cssText = 'position:fixed;bottom:4rem;left:50%;transform:translateX(-50%);background:var(--sage);color:var(--deep);font-family:var(--font-m);font-size:.9rem;letter-spacing:.14em;text-transform:uppercase;padding:1.2rem 2.8rem;z-index:9999;pointer-events:none;box-shadow:0 8px 32px rgba(79,110,247,.3);';
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
  spotlight.style.cssText = 'position:fixed;width:800px;height:800px;border-radius:50%;background:radial-gradient(circle,rgba(79,110,247,.04) 0%,transparent 70%);pointer-events:none;z-index:0;transform:translate(-50%,-50%);will-change:transform;';
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


})()