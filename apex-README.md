# Apex Consulting — Premium Real Estate Template
### Vantage Web Agency · Production Deliverable

---

## 📦 Package Contents

```
apex-consulting/
│
├── index.html              ← Complete site (all-in-one)
├── index-demo.html         ← Demo version with switcher
│
├── apex-onyx.css           ← Onyx Dark mood
├── apex-cote.css           ← Côte Naturelle mood
├── apex-urban.css          ← Urban Slate mood
│
├── manifest.json           ← PWA manifest
├── sw.js                   ← Service worker (offline)
├── offline.html            ← Offline fallback page
│
├── sitemap.xml             ← Search engine sitemap
├── robots.txt              ← Crawler instructions
│
├── README.md               ← This document
├── PITCH.md                ← Sales guide (agency use)
├── EFFECTS.md              ← Visual effects reference
└── CHANGELOG.md            ← Version history
```

---

## 🚀 Quick Start (2 minutes)

### Netlify (recommended)
1. Go to [netlify.com](https://netlify.com) — free account
2. Drag & drop the `apex-consulting/` folder
3. Your site is live immediately
4. Add a custom domain in site settings

### Vercel
```bash
npx vercel deploy --prod
```

### FTP / cPanel
Upload all files to your server root directory.
No server configuration required — everything is static.

---

## 🎨 Customise in 15 Minutes

### Step 1 — Texts

In `index.html`, search and replace:

| Find | Replace with |
|------|--------------|
| `Apex Consulting` | Your agency name |
| `Where Ambition Meets Address.` | Your tagline |
| `contact@apex-consulting.fr` | Your email |
| `+33 1 42 67 XX XX` | Your phone |
| `12 Avenue de la Grande Armée` | Your address |
| `75116 Paris` | Your city & postcode |
| `247+` | Your transactions count |
| `98%` | Your satisfaction rate |
| `15 years` | Your years of experience |
| `Thomas Leroux` | Your agent names |
| `Alexandre Beaumont` | (demo name) |

### Step 2 — Colours (8 variables)

In `index.html`, in the `<style>` block, modify:

```css
:root {
  --ax-gold:        #C9A96E;   /* Primary accent colour */
  --ax-gold-dark:   #A8853A;   /* Hover state */
  --ax-ivory:       #FAFAF8;   /* Main background */
  --ax-black:       #0A0A0A;   /* Dark sections */
  --ax-ink:         #1A1A1A;   /* Text colour */
  --ax-font-display:'Cormorant Garamond', serif;  /* Title font */
  --ax-font-body:   'Inter', sans-serif;           /* Body font */
  --ax-r-lg:        8px;       /* Card border radius */
}
```

### Step 3 — Images

Replace Unsplash URLs with your own images:

```html
<!-- Search for: images.unsplash.com -->
<!-- Replace with: -->
./images/your-property.jpg
<!-- or -->
https://your-cdn.com/image.jpg
```

**Recommended dimensions:**
- Hero: 1920×1080px, WebP, < 200KB
- Property cards: 800×600px, WebP, < 80KB
- Team photos: 400×500px, WebP, < 50KB

### Step 4 — Forms

The contact form simulates submission by default.
To make it functional, replace the simulation in the JS:

**Option A — Netlify Forms (free)**
```html
<!-- Add to both <form> elements: -->
<form ... data-netlify="true" name="contact">
```

**Option B — Formspree**
```javascript
/* Replace the simulated fetch with: */
const response = await fetch('https://formspree.io/f/YOUR_ID', {
  method: 'POST',
  body: new FormData(form),
  headers: { 'Accept': 'application/json' }
});
```

**Option C — EmailJS**
```javascript
await emailjs.send('SERVICE_ID', 'TEMPLATE_ID', {
  firstName: data.get('prenom'),
  email:     data.get('email'),
  message:   data.get('message'),
});
```

### Step 5 — Analytics

Replace the GA4 ID in the cookie banner section:
```javascript
const GA_ID = 'G-XXXXXXXXXX'; // Replace with your ID
```

---

## 🌙 Visual Styles

Four visual styles are available. Activate by adding a CSS file
link in `<head>` after the main stylesheet:

```html
<!-- Onyx Dark — deep blacks, warm gold -->
<link rel="stylesheet" href="apex-onyx.css">

<!-- Côte Naturelle — sand, sage green -->
<link rel="stylesheet" href="apex-cote.css">

<!-- Urban Slate — grey, steel blue -->
<link rel="stylesheet" href="apex-urban.css">
```

Remove the link to return to the default **Prestige Ivory** style.

**Demo switcher:** The interactive switcher is enabled by adding
`data-demo="true"` to the `<body>` tag. Remove for production.

---

## ♿ Accessibility

WCAG 2.1 AA compliant:
- Full keyboard navigation
- Screen reader compatible (VoiceOver, NVDA tested)
- Focus visible on all interactive elements
- 4.5:1 minimum contrast ratio
- Touch targets minimum 44×44px on mobile
- `prefers-reduced-motion` respected
- Windows High Contrast mode supported

---

## ⚡ Performance Targets

| Metric | Target | Technique |
|--------|--------|-----------|
| LCP    | < 2.5s | Hero preload + eager loading |
| CLS    | < 0.1  | aspect-ratio on all images |
| INP    | < 200ms | RAF throttle + debounce |
| FCP    | < 1.8s | Font preload + swap |

Expected Lighthouse scores:
- Performance:    90+
- Accessibility:  95+
- Best Practices: 95+
- SEO:            100

---

## 📱 PWA — Install as App

The site installs as a native-like app on mobile:
- `manifest.json` configured
- Service worker with offline support
- Install banner appears after 45s engagement
- 3 home screen shortcuts (Valuation, Properties, Contact)

---

## 🌍 Browser Support

| Browser | Support |
|---------|---------|
| Chrome 90+ | ✅ Full |
| Firefox 88+ | ✅ Full |
| Safari 14+ | ✅ Full |
| Edge 90+ | ✅ Full |
| iOS Safari 14+ | ✅ Optimised |
| Android Chrome | ✅ Optimised |
| IE 11 | ❌ Not supported |

---

## ✅ Pre-Launch Checklist

**Content**
- [ ] All texts replaced with real content
- [ ] All agent names, photos updated
- [ ] Real property listings added
- [ ] Actual statistics (transactions, satisfaction rate)
- [ ] Real testimonials added

**Technical**
- [ ] Forms connected (Netlify / Formspree / EmailJS)
- [ ] GA4 / Plausible ID configured
- [ ] Meta title + description personalised
- [ ] OG image uploaded (1200×630px)
- [ ] Favicon set (SVG + PNG)
- [ ] Custom domain connected
- [ ] HTTPS enabled
- [ ] `data-demo="true"` removed from `<body>`
- [ ] Demo robots tag updated to `index, follow`
- [ ] SW.js deployed at root level
- [ ] Lighthouse score verified > 90

**Quality**
- [ ] Tested on Chrome, Firefox, Safari, Edge
- [ ] Tested on iPhone + Android
- [ ] Keyboard navigation tested
- [ ] Form submission tested (real send)
- [ ] All links verified
- [ ] Console error-free
- [ ] `window.runQA()` grade A
- [ ] Cookie banner categories configured

---

## 🛠 Tech Stack

```
HTML5 · CSS3 · Vanilla ES6+
GSAP 3.12.5 + ScrollTrigger + Flip
Lenis 1.1.14 (smooth scroll)
Google Fonts (Cormorant Garamond + Inter)
Canvas API (hero particles)
IntersectionObserver · ResizeObserver
PerformanceObserver (CWV)
Service Worker + IndexedDB
Web App Manifest (PWA)

Zero dependencies · Zero npm · Zero build step
One HTML file · Deployable by drag & drop
```

---

*Built with precision by Vantage Web Agency*
*Template version 1.0.0 · October 2025*
