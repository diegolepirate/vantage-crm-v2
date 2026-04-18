import re

filepath = r"C:\vantage-clean\crm-v2-push\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find template 3 boundaries
start_marker = "TPL_ECOM_HTML['3'] = function () {"
end_marker = "TPL_ECOM_HTML['9']"

start_idx = content.index(start_marker)
end_idx = content.index(end_marker)

# Go back to find the }; before TPL 9
chunk_before_9 = content[start_idx:end_idx]
last_close = chunk_before_9.rfind('};')
actual_end = start_idx + last_close + 2  # include };

new_template = r"""TPL_ECOM_HTML['3'] = function () {
  return '<!DOCTYPE html>\
<html lang="en">\
<head>\
<meta charset="UTF-8">\
<meta name="viewport" content="width=device-width, initial-scale=1.0">\
<title>Maison Prestige — Luxury Real Estate</title>\
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700;800;900&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">\
<style>\
*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }\
html { scroll-behavior:smooth; scrollbar-width:none; }\
html::-webkit-scrollbar { display:none; }\
body { background:#0e0e0e; color:#f5f0eb; font-family:Inter,sans-serif; overflow-x:hidden; }\
\
/* ─── PRELOADER ─── */\
.preloader { position:fixed; inset:0; background:#0e0e0e; z-index:10000; display:flex; align-items:center; justify-content:center; }\
.preloader-text { position:absolute; bottom:40px; left:50%; transform:translateX(-50%); font-family:Inter,sans-serif; font-size:11px; letter-spacing:6px; text-transform:uppercase; color:#f5f0eb; opacity:0; animation:preloaderFadeIn 1s ease forwards 0.3s; }\
.preloader-video-wrap { width:80px; height:80px; overflow:hidden; border-radius:4px; animation:preloaderGrow 2s cubic-bezier(.625,.05,0,1) forwards 1.5s; }\
.preloader-video-wrap video { width:100%; height:100%; object-fit:cover; }\
@keyframes preloaderFadeIn { to { opacity:1; } }\
@keyframes preloaderGrow { to { width:100vw; height:100vh; border-radius:0; } }\
\
/* ─── HERO ─── */\
.hero { position:relative; width:100%; height:100vh; overflow:hidden; }\
.hero video { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }\
.hero-overlay { position:absolute; inset:0; background:rgba(14,14,14,0.35); }\
.hero-nav { position:absolute; top:0; left:0; right:0; display:flex; justify-content:space-between; align-items:flex-start; padding:30px 40px; z-index:5; }\
.hero-logo { font-family:Playfair Display,serif; font-size:14px; letter-spacing:4px; text-transform:uppercase; color:#f5f0eb; }\
.hero-logo-icon { font-size:28px; display:block; margin-bottom:4px; text-align:center; }\
.hero-nav-center { display:flex; gap:60px; }\
.hero-nav-col { text-align:center; }\
.hero-nav-col-title { font-size:10px; letter-spacing:4px; text-transform:uppercase; color:rgba(245,240,235,0.5); margin-bottom:12px; }\
.hero-nav-col a { display:block; font-size:13px; color:#f5f0eb; text-decoration:none; margin-bottom:6px; transition:opacity .3s; }\
.hero-nav-col a:hover { opacity:0.6; }\
.hero-cta { font-size:12px; letter-spacing:3px; text-transform:uppercase; color:#f5f0eb; text-decoration:none; border:1px solid rgba(245,240,235,0.3); padding:10px 24px; transition:all .3s; }\
.hero-cta:hover { background:#f5f0eb; color:#0e0e0e; }\
.hero-bottom { position:absolute; bottom:30px; left:0; right:0; display:flex; justify-content:space-between; align-items:center; padding:0 40px; z-index:5; }\
.hero-time { font-size:11px; letter-spacing:3px; color:rgba(245,240,235,0.6); }\
.hero-discover { font-size:11px; letter-spacing:4px; text-transform:uppercase; color:#f5f0eb; cursor:pointer; display:flex; align-items:center; gap:8px; }\
.hero-discover-line { width:30px; height:1px; background:#f5f0eb; }\
\
/* ─── HERO TEXT EDGES ─── */\
.hero-text-left, .hero-text-right { position:absolute; z-index:5; font-family:Playfair Display,serif; font-size:clamp(40px,6vw,90px); font-weight:700; color:#f5f0eb; writing-mode:vertical-lr; }\
.hero-text-left { left:40px; top:50%; transform:translateY(-50%) rotate(180deg); }\
.hero-text-right { right:40px; top:50%; transform:translateY(-50%); }\
\
/* ─── SCROLL TEXT SECTION ─── */\
.scroll-section { position:relative; min-height:100vh; background:#d4d0ca; display:flex; align-items:center; justify-content:center; padding:120px 60px; overflow:hidden; }\
.scroll-text-wrap { text-align:center; max-width:900px; }\
.scroll-text-line { font-family:Playfair Display,serif; font-size:clamp(28px,4vw,52px); font-weight:700; color:#1a1a1a; line-height:1.3; margin-bottom:16px; opacity:0; transform:translateX(80px); transition:all 1.2s cubic-bezier(.22,1,.36,1); }\
.scroll-text-line.visible { opacity:1; transform:translateX(0); }\
.scroll-marker { display:inline-block; width:8px; height:8px; background:#1a1a1a; margin:0 20px; transform:rotate(45deg); vertical-align:middle; }\
\
/* ─── BOTTOM DOCK ─── */\
.bottom-dock { position:fixed; bottom:20px; left:50%; transform:translateX(-50%); background:rgba(14,14,14,0.85); backdrop-filter:blur(12px); border-radius:40px; padding:10px 28px; display:flex; gap:24px; align-items:center; z-index:100; border:1px solid rgba(245,240,235,0.1); }\
.dock-btn { font-size:10px; letter-spacing:3px; text-transform:uppercase; color:#f5f0eb; background:none; border:none; cursor:pointer; opacity:0.7; transition:opacity .3s; }\
.dock-btn:hover { opacity:1; }\
.dock-divider { width:1px; height:14px; background:rgba(245,240,235,0.2); }\
\
/* ─── WORKS GRID ─── */\
.works-section { padding:140px 60px; background:#0e0e0e; }\
.works-title { font-family:Playfair Display,serif; font-size:clamp(36px,5vw,64px); font-weight:700; color:#f5f0eb; text-align:center; margin-bottom:80px; }\
.works-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; }\
.work-item { position:relative; overflow:hidden; aspect-ratio:3/4; cursor:pointer; }\
.work-item img { width:100%; height:100%; object-fit:cover; transition:transform 1.2s cubic-bezier(.22,1,.36,1); }\
.work-item:hover img { transform:scale(1.05); }\
.work-item-label { position:absolute; bottom:20px; left:20px; font-size:12px; letter-spacing:3px; text-transform:uppercase; color:#f5f0eb; opacity:0; transform:translateY(10px); transition:all .5s; }\
.work-item:hover .work-item-label { opacity:1; transform:translateY(0); }\
\
/* ─── CURSOR FOLLOWER ─── */\
.cursor-img { position:fixed; width:120px; height:160px; pointer-events:none; z-index:9999; opacity:0; transition:opacity .3s; overflow:hidden; border-radius:4px; }\
.cursor-img img { width:100%; height:100%; object-fit:cover; }\
\
/* ─── WORKS GRID 2 (VIOLET) ─── */\
.works-section-v { padding:140px 60px; background:#0e0e0e; position:relative; }\
.works-section-v::before { content:""; position:absolute; inset:0; background:rgba(100,60,160,0.12); pointer-events:none; }\
.works-grid-v { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; }\
.work-item-v { position:relative; overflow:hidden; aspect-ratio:3/4; cursor:pointer; }\
.work-item-v img { width:100%; height:100%; object-fit:cover; transition:transform 1.2s cubic-bezier(.22,1,.36,1); filter:saturate(0.7) brightness(0.9); }\
.work-item-v::after { content:""; position:absolute; inset:0; background:rgba(100,60,160,0.25); mix-blend-mode:multiply; transition:opacity .5s; }\
.work-item-v:hover img { transform:scale(1.05); filter:saturate(1) brightness(1); }\
.work-item-v:hover::after { opacity:0; }\
.work-item-v .work-item-label { position:absolute; bottom:20px; left:20px; font-size:12px; letter-spacing:3px; text-transform:uppercase; color:#f5f0eb; opacity:0; transform:translateY(10px); transition:all .5s; z-index:2; }\
.work-item-v:hover .work-item-label { opacity:1; transform:translateY(0); }\
\
/* ─── CONTACT SECTION ─── */\
.contact-section { padding:160px 60px; background:#0e0e0e; text-align:center; }\
.contact-title { font-family:Playfair Display,serif; font-size:clamp(36px,5vw,64px); font-weight:700; color:#f5f0eb; margin-bottom:30px; }\
.contact-sub { font-size:14px; color:rgba(245,240,235,0.5); letter-spacing:2px; margin-bottom:50px; }\
.contact-btn { display:inline-block; font-size:12px; letter-spacing:4px; text-transform:uppercase; color:#f5f0eb; border:1px solid rgba(245,240,235,0.3); padding:16px 40px; text-decoration:none; transition:all .4s; }\
.contact-btn:hover { background:#f5f0eb; color:#0e0e0e; }\
\
/* ─── FOOTER ─── */\
.footer { padding:60px; background:#0e0e0e; border-top:1px solid rgba(245,240,235,0.08); display:flex; justify-content:space-between; align-items:center; }\
.footer-left { font-size:11px; letter-spacing:3px; color:rgba(245,240,235,0.4); text-transform:uppercase; }\
.footer-right { font-size:11px; color:rgba(245,240,235,0.3); }\
\
/* ─── ANIMATIONS ─── */\
@keyframes fadeUp { from { opacity:0; transform:translateY(30px); } to { opacity:1; transform:translateY(0); } }\
.fade-up { opacity:0; transform:translateY(30px); transition:all 1s cubic-bezier(.22,1,.36,1); }\
.fade-up.visible { opacity:1; transform:translateY(0); }\
\
</style>\
</head>\
<body>\
\
<!-- PRELOADER -->\
<div class="preloader" id="preloader">\
  <div class="preloader-video-wrap" id="preloaderVid">\
    <video autoplay muted loop playsinline>\
      <source src="https://videos.pexels.com/video-files/5765284/5765284-uhd_2560_1440_30fps.mp4" type="video/mp4">\
    </video>\
  </div>\
  <div class="preloader-text">Vantage Design</div>\
</div>\
\
<!-- HERO -->\
<div class="hero" id="hero">\
  <video autoplay muted loop playsinline>\
    <source src="https://videos.pexels.com/video-files/5765284/5765284-uhd_2560_1440_30fps.mp4" type="video/mp4">\
  </video>\
  <div class="hero-overlay"></div>\
  \
  <div class="hero-text-left">Prestige</div>\
  <div class="hero-text-right">Maison</div>\
  \
  <nav class="hero-nav">\
    <div class="hero-logo">\
      <span class="hero-logo-icon">\u265E</span>\
      Maison Prestige\
    </div>\
    <div class="hero-nav-center">\
      <div class="hero-nav-col">\
        <div class="hero-nav-col-title">Repertoire</div>\
        <a href="#">Residences</a>\
        <a href="#">Collections</a>\
        <a href="#">Archives</a>\
      </div>\
      <div class="hero-nav-col">\
        <div class="hero-nav-col-title">Narrative</div>\
        <a href="#">Approach</a>\
        <a href="#">Savoir-faire</a>\
        <a href="#">Heritage</a>\
      </div>\
      <div class="hero-nav-col">\
        <div class="hero-nav-col-title">Liaison</div>\
        <a href="#">Contact</a>\
        <a href="#">Press</a>\
        <a href="#">Careers</a>\
      </div>\
    </div>\
    <a href="#" class="hero-cta">Get in touch \u2192</a>\
  </nav>\
  \
  <div class="hero-bottom">\
    <span class="hero-time" id="heroTime">00:00:00 PM</span>\
    <div class="hero-discover"><span class="hero-discover-line"></span> Discover</div>\
  </div>\
</div>\
\
<!-- SCROLL TEXT SECTION -->\
<div class="scroll-section">\
  <div class="scroll-text-wrap">\
    <div class="scroll-text-line" data-scroll-reveal>Where architecture <span class="scroll-marker"></span> meets desire</div>\
    <div class="scroll-text-line" data-scroll-reveal>Curating exceptional residences</div>\
    <div class="scroll-text-line" data-scroll-reveal>for the most <span class="scroll-marker"></span> discerning eye</div>\
  </div>\
</div>\
\
<!-- WORKS GRID -->\
<div class="works-section">\
  <h2 class="works-title fade-up" data-scroll-reveal>Selected Works</h2>\
  <div class="works-grid">\
    <div class="work-item" data-cursor-img="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=400">\
      <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800" alt="Residence">\
      <span class="work-item-label">Villa Serena</span>\
    </div>\
    <div class="work-item" data-cursor-img="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=400">\
      <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800" alt="Residence">\
      <span class="work-item-label">Le Domaine</span>\
    </div>\
    <div class="work-item" data-cursor-img="https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=400">\
      <img src="https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800" alt="Residence">\
      <span class="work-item-label">Horizon House</span>\
    </div>\
  </div>\
</div>\
\
<!-- WORKS GRID VIOLET -->\
<div class="works-section-v">\
  <h2 class="works-title fade-up" data-scroll-reveal style="position:relative;z-index:2;">Private Collection</h2>\
  <div class="works-grid-v">\
    <div class="work-item-v" data-cursor-img="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=400">\
      <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800" alt="Residence">\
      <span class="work-item-label">Amethyst Manor</span>\
    </div>\
    <div class="work-item-v" data-cursor-img="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=400">\
      <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800" alt="Residence">\
      <span class="work-item-label">Maison Violette</span>\
    </div>\
    <div class="work-item-v" data-cursor-img="https://images.unsplash.com/photo-1602343168117-bb8ffe3e2e9f?w=400">\
      <img src="https://images.unsplash.com/photo-1602343168117-bb8ffe3e2e9f?w=800" alt="Residence">\
      <span class="work-item-label">Clair de Lune</span>\
    </div>\
  </div>\
</div>\
\
<!-- CONTACT -->\
<div class="contact-section">\
  <h2 class="contact-title fade-up" data-scroll-reveal>Let\\\'s Create Together</h2>\
  <p class="contact-sub fade-up" data-scroll-reveal>Exceptional properties deserve exceptional presentation</p>\
  <a href="#" class="contact-btn fade-up" data-scroll-reveal>Start a Conversation</a>\
</div>\
\
<!-- FOOTER -->\
<div class="footer">\
  <div class="footer-left">Maison Prestige \u00A9 2026</div>\
  <div class="footer-right">Crafted with precision</div>\
</div>\
\
<!-- CURSOR FOLLOWER -->\
<div class="cursor-img" id="cursorImg"><img id="cursorImgSrc" src="" alt=""></div>\
\
<!-- BOTTOM DOCK -->\
<div class="bottom-dock">\
  <button class="dock-btn">Directory</button>\
  <div class="dock-divider"></div>\
  <button class="dock-btn" id="soundToggle">Sound: Off</button>\
</div>\
\
<\\/script>\
<script>\
(function(){\
  /* ─── PRELOADER ─── */\
  var pre = document.getElementById("preloader");\
  setTimeout(function(){ pre.style.transition = "opacity 0.8s"; pre.style.opacity = "0"; setTimeout(function(){ pre.style.display = "none"; }, 800); }, 3800);\
  \
  /* ─── LIVE TIME ─── */\
  function updateTime(){\
    var d = new Date();\
    var h = d.getHours(); var m = d.getMinutes(); var s = d.getSeconds();\
    var ap = h >= 12 ? "PM" : "AM"; h = h % 12 || 12;\
    document.getElementById("heroTime").textContent = (h<10?"0":"")+h+":"+(m<10?"0":"")+m+":"+(s<10?"0":"")+s+" "+ap;\
  }\
  updateTime(); setInterval(updateTime, 1000);\
  \
  /* ─── SCROLL REVEAL ─── */\
  var obs = new IntersectionObserver(function(entries){\
    entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add("visible"); } });\
  }, { threshold:0.15 });\
  document.querySelectorAll("[data-scroll-reveal], .fade-up").forEach(function(el){ obs.observe(el); });\
  \
  /* ─── CURSOR IMAGE FOLLOWER ─── */\
  var cursorEl = document.getElementById("cursorImg");\
  var cursorSrc = document.getElementById("cursorImgSrc");\
  var cx = 0, cy = 0, tx = 0, ty = 0;\
  document.addEventListener("mousemove", function(e){ tx = e.clientX; ty = e.clientY; });\
  function lerpCursor(){ cx += (tx - cx) * 0.12; cy += (ty - cy) * 0.12; cursorEl.style.left = cx + 20 + "px"; cursorEl.style.top = cy - 80 + "px"; requestAnimationFrame(lerpCursor); }\
  lerpCursor();\
  \
  document.querySelectorAll("[data-cursor-img]").forEach(function(item){\
    item.addEventListener("mouseenter", function(){ cursorSrc.src = this.getAttribute("data-cursor-img"); cursorEl.style.opacity = "1"; });\
    item.addEventListener("mouseleave", function(){ cursorEl.style.opacity = "0"; });\
  });\
  \
  /* ─── DISCOVER SCROLL ─── */\
  document.querySelector(".hero-discover").addEventListener("click", function(){\
    document.querySelector(".scroll-section").scrollIntoView({ behavior:"smooth" });\
  });\
})();\
<\/script>\
</body>\
</html>';
};"""

# Verify no unescaped quotes
# Check the return string portion
ret_idx = new_template.index("return '")
end_idx = new_template.rindex("';")
content_str = new_template[ret_idx+8:end_idx]
i = 0
problems = []
while i < len(content_str):
    if content_str[i] == '\\':
        i += 2
        continue
    if content_str[i] == "'":
        line_start = content_str.rfind('\n', 0, i) + 1
        line_end = content_str.find('\n', i)
        if line_end == -1: line_end = len(content_str)
        context = content_str[max(0,i-20):i+20]
        problems.append(f"Unescaped quote at pos {i}: ...{context}...")
    i += 1

if problems:
    print("QUOTE PROBLEMS FOUND:")
    for p in problems:
        print(p)
    raise SystemExit(1)
else:
    print("No quote problems found!")

# Replace in file
content = content[:start_idx] + new_template + "\n\n" + content[actual_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Template 3 replaced successfully!")
print(f"Old: lines {start_idx} to {actual_end}")
print(f"New template length: {len(new_template)} chars")
