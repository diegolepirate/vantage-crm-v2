# BLUEPRINT — VANTAGE
**Single source of truth. Update after every single prompt. Re-read at start of every prompt without exception.**

Project: VANTAGE — Superhero mascot landing page for Vantage Web Agency
Location: Athens, Greece
Tagline: _"Built different. Coded perfect."_
Language: English — 100% everywhere (content, labels, buttons, errors, meta, comments)
Main file: `vantage-index.html` (kept separate from CRM's `index.html`)

---

## BUTTONS
_Selector | Action | Status_

| Selector | `data-action` | What it does | Status |
|----------|---------------|--------------|--------|
| `.vt-logo` (navbar + footer) | `scroll-top` | Smooth-scroll to page top | html_done |
| `.vt-cta-nav` (navbar) | `scroll-to-contact` | Scroll to `#vt-contact` | html_done |
| `.vt-cta-nav.vt-mobile-cta` | `scroll-to-contact` | Scroll to `#vt-contact` + close menu | html_done |
| `.vt-mobile-close` | `close-mobile-menu` | Close mobile nav overlay | html_done |
| `.vt-btn-primary` (hero: "See our work →") | `scroll-to-gallery` | Scroll to `#vt-gallery` | html_done |
| `.vt-btn-ghost` (hero: "Enter the universe") | `scroll-to-universe` | Scroll to `#vt-universe` | html_done |
| `.vt-btn-service` (Templates card) | `scroll-to-contact` + `data-service=templates` | Scroll to contact, pre-fill service | html_done |
| `.vt-btn-primary` (Custom featured card) | `scroll-to-contact` + `data-service=custom` | Scroll to contact, pre-fill service | html_done |
| `.vt-btn-service` (Maintenance card) | `scroll-to-contact` + `data-service=maintenance` | Scroll to contact, pre-fill service | html_done |
| `.vt-tab[data-tab=newsletter]` | (tab switch) | Show newsletter panel | html_done |
| `.vt-tab[data-tab=collaborate]` | (tab switch) | Show collaborate panel | html_done |
| `.vt-tab[data-tab=sayhello]` | (tab switch) | Show say-hi panel | html_done |
| `.vt-cta-form[data-form=newsletter] button` | (submit) | Subscribe toast + reset | html_done |
| `.vt-cta-tab-panel .vt-btn-primary` (Collaborate) | `scroll-to-contact` | Scroll to contact | html_done |
| `#vt-contact-form button[type=submit]` | (submit) | Send message toast + reset | html_done |
| `.vt-back-to-top` (`#vt-btt`) | `scroll-top` | Smooth scroll to top | html_done |
| `.vt-legal-link[data-action=privacy]` | `privacy` | Toast "Privacy page coming soon" | html_done |
| `.vt-legal-link[data-action=terms]` | `terms` | Toast "Terms page coming soon" | html_done |
| `#vt-cookie-reopen` | `cookie-prefs` | Toast "Cookie prefs coming soon" | html_done |

**Self-check performed:** 0 occurrences of `href="#"`, 0 uniform `border-radius: 8px` on cards, 0 `cursor: none`.

---

## JS MODULES
_Module name | Functions | Status_

| Module | Functions | Status |
|--------|-----------|--------|
| `bootstrap` (inline IIFE) | preloader hide (3s hard cap), navbar scrolled toggle, scroll progress bar, back-to-top visibility, `toast()`, `data-action` router, tab switching, form submit stubs | html_done (bootstrap only — full JS suite arrives in Prompt 2.3) |

---

## SECTIONS
_ID | Purpose | Status (todo / html_done / css_done / js_done / tested)_

**STRUCTURE SIMPLIFIED TO 6 SECTIONS** (previous 11-section structure retired — file rebuilt from scratch keeping all assets)

| ID | Purpose | Status |
|----|---------|--------|
| `vt-hero` | Ghost wordmark + violet circle + hero PNG (mix-blend screen) + tagline + CTAs + avatar marquee | done ✅ |
| `vt-services` | 3 glassmorphism cards — Templates / Custom (featured) / Maintenance | done ✅ |
| `vt-powers` | 3 stat cards — Strength / Speed / Precision with animated counters | done ✅ |
| `vt-gallery` | 4-col hero photo grid (transparent PNGs, no backgrounds) | done ✅ |
| `vt-cta` | Full-screen Join the Universe CTA with hero image backdrop | done ✅ |
| `vt-contact` | Split form + embedded footer | done ✅ |

**Retired in this pass:** `vt-preloader` (no more screen-crack), `vt-origin` scrollytelling (4 acts removed), `vt-universe` carousel (4 cyber cards removed), `vt-lore` timeline (5 chapters removed). Assets kept for future re-use.

---

## KNOWN BUGS
_Description | Priority | Fixed?_

| Description | Priority | Fixed? |
|-------------|----------|--------|
| Hero video: background removed via ffmpeg + rembg frame-by-frame pipeline, re-encoded as VP9 yuva420p WebM with true alpha channel. `vantage-hero.webm` is now the primary source; MP4 kept as fallback. No more mix-blend-mode trick — the alpha channel does the work. | medium | **fixed ✅** |
| Preloader SVG crack animation not yet drawn — placeholder only (container div in DOM, but no fissure paths injected) | medium | no — will arrive with full JS suite in 2.3 |
| Origin scrollytelling: video scrubbing not wired (static placeholder background) | medium | no — will arrive with GSAP ScrollTrigger in 2.3 |
| 3D carousel: cards stacked in center, no rotation yet | medium | no — Three.js/GSAP rotation in 2.3 |
| Powers counters: static text, no scramble-resolve yet | low | no — arrives in 2.3 |
| Lore calligraphic SVG: plain blockquote for now, not SVG stroke-dashoffset draw | low | no — arrives in 2.3 |

---

## DOCUMENTATION ARTIFACTS
_Top-level docs · Status_

| File | Purpose | Status |
|------|---------|--------|
| `BLUEPRINT.md` | Single source of truth (this file) | done |
| `SITEMAP.md` | Site architecture · 11 sections · CTA hierarchy | done |
| `DESIGN_BRIEF.md` | Palette · typography · easing · cards · grain · a11y · perf | done |
| `MOODS.md` | 4 visual moods — SHADOW · CRIMSON · ARCTIC · GOLD | done |
| `CONTENT.md` | 100% English paste-ready copy for every section | done |

---

## ASSETS
_File · Purpose · Status_

| Asset | Purpose | Status |
|-------|---------|--------|
| `vantage-hero.mp4` | Hero video — original (fallback source) | present ✅ |
| `vantage-hero.webm` | Hero video — **transparent bg** (VP9 yuva420p alpha, 1.5 MB, 145 frames @24fps) | ✅ processed via `remove-bg-video.py` (ffmpeg + rembg u2net_human_seg) |
| `remove-bg-video.py` | Video bg-removal pipeline (extract → rembg → re-encode VP9 alpha) | present ✅ |
| `vantage-origin.mp4` · `.webm` | Origin section video — transparent bg alpha | ✅ processed (1.29 MB webm) |
| `vantage-hero-circle.mp4` | Hero circle backdrop video (replaces violet static gradient) | ✅ copied from Downloads (6.6 MB) |
| `super_hero_1.jpg` · `.png` | Full body · transparent-bg | ✅ processed (720×1280 RGBA) |
| `super_hero_4.jpg` · `.png` | Close-up chest/face · transparent-bg | ✅ processed (720×1280 RGBA) |
| `super_hero_5.jpg` · `.png` | Armor detail · transparent-bg | ✅ processed (720×1280 RGBA) |
| `super_hero_6.jpg` · `.png` | Mask close-up · transparent-bg | ✅ processed (720×1280 RGBA) |
| `remove-bg.py` | rembg script — processes all 4 JPGs | present ✅ |

---

## CHANGELOG
_One line per prompt applied_

- Initial blueprint created — VANTAGE agency mascot landing.
- Sitemap created (SITEMAP.md) — 11 sections, CTA hierarchy defined.
- Design brief created (DESIGN_BRIEF.md) — palette, typography, easing, animation timing, film grain, glassmorphism, cyber card structure, 4 carousel variants, contrast narrative, emotional targets, variant map, perf + a11y rules.
- Moods defined (MOODS.md) — 4 moods (SHADOW default, CRIMSON, ARCTIC, GOLD), variable overrides, per-mood sections impacted, button/navbar adaptations.
- Content written (CONTENT.md) — real English copy for all 11 sections, toasts, aria-labels, SEO meta, zero lorem ipsum.
- **Prompt 2.2 — HTML structure built (`vantage-index.html`).** All 13 sections rendered with real English content from CONTENT.md. Baseline CSS covering layout, palette, typography scale, glassmorphism, film grain, preloader, navbar, buttons, cards, forms, toasts, back-to-top, scroll progress, mobile menu, reduced-motion fallback. Minimal JS bootstrap (preloader cap, scroll state, data-action router, tab switcher, form submit stubs, toast helper). All buttons documented with selector + action + status. Self-check: 0 × `href="#"`, 0 × uniform 8px card radius, 0 × `cursor:none`. rembg installed; `remove-bg.py` ready for user's JPG files.
- **Fix pass — full-size content & bg removal.** Copied `super hero 5.jfif` and `super hero 6.jfif` from Downloads as `super_hero_5.jpg` / `super_hero_6.jpg`. Ran rembg on all 4 JPGs → 4 transparent PNGs (720×1280). **Hero video:** `object-fit:contain` (full size, no crop). **Gallery:** removed the MP4 video tile (video now appears ONCE, only in hero). Gallery now shows 4 transparent-bg hero images (super_hero_1/4/5/6) each on a radial-gradient violet halo, `object-fit: contain` so full character always visible. **CTA hero-bg:** `object-fit: contain`, height:100% so full silhouette shows.
- **Video bg removal — done for real.** Wrote `remove-bg-video.py` (ffmpeg via `imageio_ffmpeg` + rembg u2net_human_seg). Pipeline: extract 145 frames @24fps @512px → rembg each frame → re-encode `vantage-hero.webm` (VP9 yuva420p alpha, 1.5 MB). HTML `<video>` now serves `.webm` (primary, true alpha) with `.mp4` fallback. Dropped the `mix-blend-mode: screen` workaround — no longer needed.
- **Hero layered look.** Added 3 background layers to `#vt-hero`: (1) giant `VANTAGE` wordmark at `rgba(255,255,255,.08)` clamp(12–22rem), letter-spacing -.04em, z-index 0; (2) violet radial circle 60vmin at z-index 1 (gradient `#6B21A8` → `#1E0A3C` → transparent) with a 6s breathe scale animation; (3) infinite avatar marquee at the bottom — 8 avatars × 2 (seamless loop), 64px circles with `rgba(168,85,247,.4)` border, `translateX 0 → -50%` over 20s linear, `animation-play-state: paused` on hover. Edge-fade mask on left/right. Z-index order back→front: giant text (0) · circle (1) · hero content (2) · marquee (3). `overflow:hidden` + `isolation:isolate` on the hero so layers clip correctly and `mix-blend` / film grain don't leak.
- **Direction change — simplified premium (Apple × Marvel).** Dropped WebGL, liquid distortion, 3D carousel complexity, and unused CDN loads (GSAP / ScrollTrigger / Flip / MorphSVG removed — only Lenis kept). **Universe carousel** → clean responsive grid of 4 accent-glow cards; each card has subtle CSS scan-lines + per-variant radial glow (violet/red/blue/gold) + accent-coloured hover border + numbered badge (01–04). **Kinetic title** — hero `VANTAGE` line fades+rises on first paint (`translateY 40% → 0`, .9s ease). **Scroll reveals** — IntersectionObserver adds `.is-in-view` to h2/cards/chapters/acts with staggered delays (.08/.16/.24s). **Lenis smooth scroll** activated on load (respects `prefers-reduced-motion`). All existing buttons, toasts, forms, tabs remain wired. Everything works, nothing is placeholder anymore.
- **Prompt 2.3 — CSS completion & polish.** Added the remaining pieces called out in the brief: (1) **Primary button shimmer** — `::before` gradient sweep on hover with `skewX(-18deg)`, 0.8s ease. (2) **Active state** — `scale(.98)` on primary/ghost/service/CTA-nav. (3) **Section divider utility** `.vt-section-divider` — gradient violet line. (4) **Lore timeline connecting line** — horizontal violet gradient across chapters + violet dot at each chapter top. (5) **Performance** — `contain: layout style` on cards, `will-change: transform` on hero-circle/video/marquee, `will-change: width` on preloader fill. (6) **Mobile polish** — `backdrop-filter` disabled on navbar/service-cards below 768px, hero stacks (video above text), services single column, contact stacked. (7) **Tablet** — 2-col grids for services/powers/universe at 769–1023px. (8) **Burger button** — proper 44px touch target, 3-line icon, wired via `data-action="toggle-mobile-menu"` (aria-expanded toggles, body scroll locked while open, auto-close on link click). (9) **Touch targets** — `min-height: 44px` on all button variants. Self-check: 0 × `href="#"`, 0 × `cursor:none`, 1 × 8px radius (burger button — not a card, rule respected). 9 media queries, 86 aria-* attributes, reduced-motion fully guarded.
- **Vantage Resto — cursor-scrub hero video.** (Scope: `vantage-resto-index.html` only.) Video changed from `autoplay loop` to scrubbable: `preload="auto" muted playsinline`, metadata-based ready flag, poster/first frame served instantly. Cursor X across the viewport maps 0→duration. GSAP 3.12.5 loaded from CDN; `gsap.ticker` drives a `.06` lerp between `current` and `target` (set by `mousemove`). `touchmove` path active on pointer-coarse devices. iOS Safari primer (silent play/pause on first click/touch) kicks the element out of its locked state so `currentTime` seeks work. Progress bar `.scrub-progress` (2px, `--vt-purple` glow) tracks scrub in real time. `← Explore →` hint (`.scrub-hint`) follows cursor, appears after 400ms, fades after 3s then self-removes from DOM. `IntersectionObserver` pauses/resumes the ticker when the hero leaves/enters the viewport. `prefers-reduced-motion` guarded. Fallback pure-`requestAnimationFrame` loop kicks in if GSAP fails to load.
- **CRM — Universe template preview fullscreen.** Rewrote `showUniPreviewModal()` in `index.html`. Mac mockup frame (header with dots + label + border + 85vh modal) replaced with full viewport iframe (`100vw × 100vh`, black fallback). Added: (1) single fixed close button ✕ top-right (40px circle, `rgba(0,0,0,.7)` bg, white border `rgba(255,255,255,.2)`, `backdrop-filter: blur(8px)`, hover scale 1.06), (2) Escape key handler (removes listener on close), (3) subtle "PREVIEW MODE — vantagebookweb.netlify.app" badge top-left at opacity .4 (Inter 11px, pill shape, blur bg), (4) `document.body.style.overflow='hidden'` while open. New `closeUniPreview()` helper centralises close logic. Sandbox on iframe allows scripts/same-origin/forms/popups. Body scroll restored on close.
- **MAJOR RESTRUCTURE — 6 sections only.** Rebuilt `vantage-index.html` from scratch. New structure: Hero → Services → Powers → Gallery → CTA → Contact+Footer. Retired preloader / origin scrollytelling / universe carousel / lore timeline. **Tech:** GSAP + ScrollTrigger + Lenis via CDN (all fetched, ticker-synced with ScrollTrigger for Lenis smooth-scroll integration). **Hero:** ghost `VANTAGE` wordmark (`clamp(14rem→32rem)` opacity .06), violet radial circle 60vmin (breathing 6s), hero PNG floating in front with `mix-blend-mode: screen`, tagline "Built different. Coded perfect.", primary "Work with us" + ghost "See our work →", infinite avatar marquee (16 avatars, 24s linear). **Services:** 3 glassmorphism cards, middle card `--featured` (violet border, scale 1.04, larger shadow), prices €800/€4500/€250-per-month. Each button scrolls to `#vt-contact` and pre-fills the `<select>` via `data-service`. **Powers:** 3 cards with animated counters (0→100% / 999→0ms / ∞) via IntersectionObserver + cubic easing. **Gallery:** 4-col grid of transparent PNG heroes (super_hero_1/4/5/6). **CTA:** full-screen hero-image backdrop at .22 opacity, centered "Join the Universe." headline. **Contact:** split form + embedded footer (copyright, legal toast-stubs). **Animations:** GSAP `fromTo` reveals on every `.vt-reveal` element, ScrollTrigger `once: true`, `power2.out` ease, 0.9s duration, data-delay stagger. Fallback IntersectionObserver when GSAP unavailable. **All rules held:** 0 × `href="#"`, 0 × `cursor:none`, 0 × uniform 8px card radius, 100% English, film grain position:fixed opacity:.032, violet #6B21A8 accent everywhere, Rajdhani Bold on all titles, every button wired with a real action + aria-label.
- **TOOL-SPECIFIC ACCENT COLOR SYSTEM.** Each standalone tool now has its own unique accent color, independent of the sector dropdown. The sector color stays only for sector-specific data (category badges, sector dropdown border-left). Tool accent drives: primary buttons, active nav states, segmented control, focus rings, blob backgrounds, progress bars, FAB, notification badges, KPI accents. Implementation: each tool file injects `:root{--tool-accent:#XXX;--tool-accent-soft:rgba(R,G,B,.14)}` + `body{--accent:var(--tool-accent)!important}` before `</style>`. The `!important` on body overrides any JS `setProperty('--accent')` call (JS lacks !important). Dark mode uses brighter variants. Blobs picked up via `.blob,body::before,body::after{background:var(--tool-accent)!important}`. Sector dropdown gets `border-left:3px solid var(--tool-accent)` as visual hint. **Color map:** Revenue Dashboard `#007AFF`→`#409CFF`, CRM Pro/Visual `#34C759`→`#30D158`, Margin Calculator `#FF9500`→`#FF9F0A`, Staff Scheduler `#AF52DE`→`#BF5AF2`, Invoice Generator `#5856D6`→`#6E6CF0`, Inventory Manager `#32ADE6`→`#5AC8FA`, Booking System `#FF2D55`→`#FF375F`. Suite V1 and Suite V2 left sector-driven (they host multiple tools). Zero functionality or data changed; only CSS variables.
- **Suite Unified (5 tools).** Created `vantage-suite-unified.html` — Dashboard + CRM + Calculator + Scheduler + Invoices in one app. Each tool has its own accent color (#007AFF / #34C759 / #FF9500 / #AF52DE / #5856D6) that drives ALL UI chrome (buttons, active states, blob color). Blob background uses `var(--tool-accent)` with `transition: background .8s ease` so switching tools triggers a smooth color morph. Topbar segmented shows all 5 tools always (not sector-filtered like older Suite V2). Sidebar changes per tool with context-aware sub-pages. Global search across clients/products/invoices with type badges + click-to-navigate. Notifications panel with tool routing (click → opens relevant tool + item). Cross-tool: top clients in Dashboard → CRM detail, Invoice client link → CRM. Print CSS for invoice preview. 50 clients, 140 transactions, 9 products, 12 staff × 4 weeks shifts, 50 invoices, 16 tasks. Registered in Book as id:65 Productivity/All-in-One. BLUEPRINT confirms sector dropdown is NOT the driver in this version — tool color IS the driver.

---

# FULL KIT RESTAURANT — `vantage-restaurant-kit.html`

Restaurant: ELIA — Santorini, Greece · Friday dinner service · Manager: Marco

## MODULES
| # | Name | Pages | Status |
|---|------|-------|--------|
| 1 | Overview | Hero KPIs, live feed, rings, top dishes | todo |
| 2 | Floor Map | Tables visual + timers + detail panel | todo |
| 3 | Orders | Tables list + order builder + menu | todo |
| 4 | Bookings | Timeline + list + new modal | todo |
| 5 | Kitchen | Dark bg, ticket cards, timers, checklist | todo |
| 6 | Inventory | 60 items, low-stock alerts, +/- | todo |
| 7 | Staff | 8 cards, clock-in status, tips pool | todo |
| 8 | Revenue | Live CA hero, charts, cash count | todo |
| 9 | Loyalty | Members, tiers, live feed | todo |
| 10 | Invoices | List + create + print | todo |

## LIVE ENGINE
| Event | Interval | Status |
|-------|----------|--------|
| newTransaction (40%) | 35-75s random | todo |
| tableStatusChange (20%) | 35-75s random | todo |
| kitchenUpdate (20%) | 35-75s random | todo |
| stockAlert (5%) | 35-75s random | todo |
| newReservation (10%) | 35-75s random | todo |
| loyaltyEvent (5%) | 35-75s random | todo |
| Timer ticks (1s) | 1000ms | todo |
| Clock tick (1s) | 1000ms | todo |

## KEY BUTTONS
| Selector | action | status |
|----------|--------|--------|
| `#loginBtn` | sign-in-flow | todo |
| `#openServiceBtn` | toggle open/close service | todo |
| `#endServiceBtn` | generate end of night report | todo |
| `#audioToggle` | mute/unmute sounds | todo |
| `#themeToggle` | light/dark | todo |
| module tabs `[data-module]` | switch module | todo |
| floor table cards | open detail panel | todo |
| bay quick-add `+Walk-in` | new reservation modal | todo |
| `+ Reservation` | new reservation modal | todo |
| kitchen ticket DONE | mark ticket complete | todo |
| bottom-nav buttons (mobile) | switch module | todo |

## KEYBOARD SHORTCUTS
1-0 = modules / N = new / / = search / D = theme / Esc = close / ? = help


## STATUS UPDATE (first pass complete)
| Module | Status |
|---|---|
| 1. Overview | done ✅ |
| 2. Floor Map | done ✅ |
| 3. Orders | done ✅ |
| 4. Bookings | done ✅ (list view) |
| 5. Kitchen | done ✅ (dark mode, pulse) |
| 6. Inventory | done ✅ |
| 7. Staff | done ✅ |
| 8. Revenue | done ✅ |
| 9. Loyalty | done ✅ |
| 10. Invoices | done ✅ |
| Login flow | done ✅ |
| Splash | done ✅ |
| Live Engine (6 event types) | done ✅ |
| Toast system | done ✅ |
| Lava blobs (5) | done ✅ |
| Keyboard shortcuts | done ✅ |
| Audio tones | done ✅ |
| End-of-night report | done ✅ |
| Mobile bottom nav | done ✅ |

Registered in Book Universe id:66, Productivity/Hospitality premium.

## BASIC KIT RESTAURANT — `vantage-restaurant-basic.html`
Simpler companion to Full Kit. Taverna Helios · Athens. 4 modules, no live engine, static realistic data. Light design with 3 subtle lava blobs (#FF9500). Registered in Book id:67 classic tier.
| Module | Status |
|---|---|
| 1. Dashboard (Today/Week/Month) | done ✅ |
| 2. Reservations (list + calendar) | done ✅ |
| 3. Staff (cards + tips) | done ✅ |
| 4. Inventory (20 items + alerts) | done ✅ |
| Keyboard shortcuts | done ✅ |
| Mobile bottom nav | done ✅ |

## BASIC KIT AGENCY — vantage-agency-basic.html
- Vantage Web Agency (Athens) — purple #AF52DE accent, 3 lava blobs
- [x] Dashboard: 4 KPIs + revenue chart + today's tasks + deadlines + activity feed
- [x] Projects: filter pills, sort, status cards + kanban task detail view
- [x] Clients: searchable list + VIP flag + slide-in detail panel (projects, invoices)
- [x] Finance: 4 KPIs + charts + invoices table + split-view editor with print preview
- Data: 8 projects, 12 clients, 15 invoices, Greek VAT 24%
- Deployed: https://vantagebookweb.netlify.app/vantage-agency-basic.html
