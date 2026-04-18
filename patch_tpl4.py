filepath = r"C:\vantage-clean\crm-v2-push\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

marker = "TPL_ECOM_HTML['9']"
idx = content.index(marker)

new_tpl = r"""TPL_ECOM_HTML['4'] = function () {
  return '<!DOCTYPE html>\
<html lang="en">\
<head>\
<meta charset="UTF-8">\
<meta name="viewport" content="width=device-width, initial-scale=1.0">\
<title>Vortex Digital — Design Studio</title>\
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"/>\
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">\
<style>\
*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }\
html { scrollbar-width:none; }\
html::-webkit-scrollbar { display:none; }\
body { margin:0; background:#000; font-family:Inter,sans-serif; color:#fff; overflow-x:hidden; }\
\
.swiper { width:100%; height:100vh; }\
.swiper-slide { position:relative; display:flex; align-items:center; justify-content:center; }\
.swiper-slide img { position:absolute; width:100%; height:100%; object-fit:cover; z-index:-1; }\
.overlay { background:rgba(0,0,0,0.4); padding:20px 40px; border-radius:10px; font-size:40px; font-weight:bold; }\
</style>\
</head>\
<body>\
\
<div class="swiper main-slider">\
  <div class="swiper-wrapper">\
    <div class="swiper-slide">\
      <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=1920" alt="Project 1">\
      <div class="overlay">Project 1</div>\
    </div>\
    <div class="swiper-slide">\
      <img src="https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=1920" alt="Project 2">\
      <div class="overlay">Project 2</div>\
    </div>\
    <div class="swiper-slide">\
      <img src="https://images.unsplash.com/photo-1563089145-599997674d42?w=1920" alt="Project 3">\
      <div class="overlay">Project 3</div>\
    </div>\
  </div>\
</div>\
\
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"><\/script>\
<script>\
var mainSlider = new Swiper(".main-slider", {\
  slidesPerView: 1,\
  centeredSlides: true,\
  spaceBetween: 0,\
  effect: "fade",\
  fadeEffect: { crossFade: true },\
  speed: 800,\
  autoplay: { delay: 3000, disableOnInteraction: false },\
  allowTouchMove: false,\
  simulateTouch: false,\
  touchRatio: 0,\
  loop: true\
});\
<\/script>\
</body>\
</html>';
};

"""

# Verify quotes
ret_idx = new_tpl.index("return '")
end_idx = new_tpl.rindex("';")
s = new_tpl[ret_idx+8:end_idx]
i = 0; problems = []
bs = chr(92)
sq = chr(39)
while i < len(s):
    if s[i] == bs: i += 2; continue
    if s[i] == sq: problems.append(f'pos {i}: ...{s[max(0,i-20):i+20]}...')
    i += 1

if problems:
    print("QUOTE PROBLEMS:")
    for p in problems: print(p)
    raise SystemExit(1)

print("Quotes OK!")
content = content[:idx] + new_tpl + content[idx:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Template 4 inserted!")
