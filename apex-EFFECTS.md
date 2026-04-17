# Apex Consulting — Visual Effects Reference
### Complete catalogue of all signature effects

---

## How to Read This Document

Each effect is described with:
- **Section** — where it lives
- **Effect** — what it does
- **Trigger** — what activates it
- **Tech** — implementation
- **Modify** — how to adjust

---

## Effects by Section

### HERO
**Radar Scan Line**
- Effect: A golden translucent line sweeps left to right
- Trigger: Automatic, every 8 seconds
- Tech: GSAP `from left:'-100%' to left:'160%'`
- Modify: Change interval in `signatureHero()`, line 1
  `setTimeout(runScan, 3200)` → delay
  `duration: 2.4` → speed of sweep

**Ambient Orb**
- Effect: 800px soft golden glow follows cursor with 1.2s lag
- Trigger: Mouse movement on hero section
- Tech: GSAP `to(orb, { left, top, duration:1.2 })`
- Modify: `opacity:.06` → intensity; `duration:1.2` → lag

**Editorial Title Entrance**
- Effect: Title lines rise from behind overflow mask
- Trigger: Preloader completes
- Tech: GSAP `y:'115%'→'0%'` with `overflow:hidden` wrapper
- Modify: `duration:1.3` → speed; `stagger:.12` → delay between lines

---

### METRICS
**Bloomberg Glitch**
- Effect: Numbers flicker with random chars before showing real value
- Trigger: Section enters viewport
- Tech: `setInterval` replacing text with `0123456789₁₂₃€£%`
- Modify: `6` iterations → how many glitch frames
  `60ms` interval → glitch speed

---

### PROPERTIES
**Magazine Reveal**
- Effect: Cards enter via clip-path `inset(0 0 100% 0)`
- Trigger: ScrollTrigger `top 90%`
- Tech: GSAP clip-path animation with `clearProps`
- Modify: `delay: (i % 3) * .14` → stagger between columns

**Property Depth**
- Effect: Image parallax inside card + mouse reaction
- Trigger: Scroll + mousemove
- Tech: `height:115%` + `top:-7.5%` + GSAP set y
- Modify: `* 40` → parallax intensity; `* 10/8` → mouse sensitivity

---

### SERVICES
**SVG Icon Draw**
- Effect: Each icon path traces itself on scroll
- Trigger: Card enters `top 82%`
- Tech: `getTotalLength()` + `strokeDashoffset` animation
- Modify: `duration:.9` → draw speed; `stagger:.12` → path delay

**Spotlight**
- Effect: Gold radial gradient follows cursor inside card
- Trigger: Mousemove on `.ax-service-card`
- Tech: CSS `--sx --sy` custom properties + `radial-gradient`
- Modify: `.07` opacity → spotlight intensity

---

### MARKET DATA
**Bloomberg Terminal**
- Effect: Values glitch with random chars, then resolve
- Trigger: Section enters `top 78%`
- Tech: `setInterval` character replacement × 6
- Modify: `220` delay between items; `60ms` glitch speed

**SVG Curve Draw**
- Effect: Market trend line traces from left to right
- Trigger: Chart enters `top 75%`
- Tech: `stroke-dashoffset: 1200 → 0` over 2.2s
- Modify: `1200` → match your SVG path length

---

### TEAM
**B&W to Colour**
- Effect: Photos desaturate → full colour on hover
- Trigger: Mouseenter on `.ax-equipe__membre`
- Tech: GSAP `filter: grayscale(.8) → grayscale(0)`
- Modify: `duration:.6` → transition speed

**Citation Reveal**
- Effect: Quote slides up from bottom while photo colours
- Trigger: Same hover as above
- Tech: GSAP `from { y:24, opacity:0 }`
- Modify: `y:24` → entrance distance

---

### TESTIMONIALS
**Quote Mark Float**
- Effect: Giant quote mark enters with blur dissolve
- Trigger: Section enters `top 80%`
- Tech: GSAP `from { y:40, opacity:0, filter:'blur(4px)' }`
- Modify: `y:40` → entrance distance; `blur(4px)` → softness

---

### FAQ
**Gold Background Shift**
- Effect: Section background warms to pale gold gradient
- Trigger: Any FAQ item opens
- Tech: CSS `.ax-faq.has-open` class + MutationObserver
- Modify: `rgba(201,169,110,.04)` → gold intensity

**Left Gold Line**
- Effect: 2px gold border appears on left of open item
- Trigger: Click on trigger
- Tech: GSAP `borderLeft: '2px solid var(--ax-gold)'`
- Modify: `2px` → line thickness

---

### NEWS
**Title Clip Reveal**
- Effect: Article title revealed left-to-right like a curtain
- Trigger: Title enters `top 85%`
- Tech: GSAP `clipPath: 'inset(0% 100% 0% 0%)' → inset(0%)`
- Modify: `duration:.7` → speed; `i * 120` → stagger

---

### CTA FINAL
**Canvas Particles**
- Effect: 22 ascending golden particles (fireflies)
- Trigger: Section enters viewport (IntersectionObserver)
- Tech: Canvas `requestAnimationFrame` with particle physics
- Modify: `22` → particle count; `.06` → opacity

---

### CONTACT
**Visual Connector**
- Effect: Thin gold vertical line appears between columns
- Trigger: Any form field receives focus
- Tech: CSS `height: 0 → 60%` transition on `.is-connected`
- Modify: `60%` → connector height; `opacity: .3` → visibility

---

### FOOTER
**Email Letter-by-Letter**
- Effect: Email address appears character by character
- Trigger: Email enters viewport
- Tech: Each character wrapped in `<span>` with CSS delay
  `transition-delay: ${i * 0.04}s`
- Modify: `0.04` → delay per character

---

## Global Effects

**Scroll Progress Bar**
- 1px gold bar at top, advances with scroll
- Modify `height` in CSS for thickness

**CountUp Numbers**
- All `data-counter` elements animate from 0
- Modify `duration:2.4` for speed

**Ripple on Buttons**
- Click creates expanding circle from cursor position
- `rgba(255,255,255,.14)` → ripple opacity

**Magnetic CTA**
- Navbar CTA + final CTA follow cursor ±15%
- `* .15` multiplier → magnetic strength

**Konami Code Easter Egg**
- ↑↑↓↓←→←→BA → "Apex Mode Unlocked" overlay
- Fully branded with agency tagline
