# SITEMAP — VANTAGE
**Template:** VANTAGE — mascot landing page for Vantage Web Agency
**Hero:** Vantage (formerly Marcus, now digital-fused)
**Tagline:** _"Built different. Coded perfect."_
**Location:** Athens, Greece
**Language:** English — 100% everywhere. Zero lorem ipsum. All placeholder text is real English copy.

---

## ORIGIN STORY (canonical)

Marcus was an ordinary web developer obsessed with perfection. One night, working on an impossible project, a surge of pure digital energy fused with his biology. He became **Vantage** — the embodiment of what a website can be when someone refuses mediocrity.

- **His strength** = code solidity
- **His speed** = performance
- **His power** = visual impact

The hero represents the agency's quality standard. Every section must make the visitor feel they are dealing with something completely different from any other web agency.

---

## GLOBAL CTA HIERARCHY

| Level | Label | Destination | Appears in |
|-------|-------|-------------|------------|
| **Primary** | `Work with us` | `#contact` (final CTA form) | Navbar, Final CTA |
| **Secondary** | `See our work →` | `#gallery` (photo gallery) | Hero |
| **Tertiary** | `Join the Universe` | `#newsletter` (within Final CTA) | Final CTA |

---

## SECTION MAP (order of appearance)

### 1 — PRELOADER
- **ID:** `vt-preloader`
- **Purpose:** Transform the page load into the hero's entrance.
- **Effect:** Screen-crack reveal. SVG fissures animate outward from a single impact point. The site reveals itself behind the cracks as they open.
- **Emotional target:** _Shock. Awe. "Whatever this is, it's not a normal website."_
- **Duration:** 3 seconds hard cap (force-hide safety timeout — lesson from Apex/Pixel Forge).
- **Interactive elements:** None (non-skippable, but safety-capped).
- **CTA:** None.
- **Wow moment:** The first crack sound + the hero silhouette glimpsed through the fissure a split-second before the site appears.

---

### 2 — NAVBAR
- **ID:** `vt-navbar`
- **Purpose:** Persistent top anchor, always available to convert.
- **Layout:** Fixed, full-width. Translucent dark background with `backdrop-filter: blur(18px)`. 1px violet-tinted bottom border.
- **Logo:** `VANTAGE` wordmark + geometric emblem (same mark from the hero's chest armor).
- **Links:** `Origin · Universe · Powers · Services · Lore · Contact` — minimal white text, 11px tracking-wide uppercase.
- **CTA button:** **`Work with us`** — violet glow, pulse on hover.
- **Emotional target:** _Confidence. "This agency means business."_
- **Wow moment:** On scroll, the emblem subtly rotates 90° and the CTA glow intensifies.

---

### 3 — HERO SECTION
- **ID:** `vt-hero`
- **Purpose:** Claim the visitor's attention in the first 3 seconds.
- **Layout:** Two-column split.
  - **LEFT (55%):** Huge cinematic title **"VANTAGE"** in display serif italic (clamp 80–200px). Tagline **"Built different. Coded perfect."** in bold condensed sans. 1-sentence subtitle: _"A web agency from Athens, engineering landing pages that refuse to be forgettable."_. Secondary CTA: **`See our work →`**.
  - **RIGHT (45%):** The hero video (wood-carving loop) floating with transparent background — no frame, no border. Slightly taller than the text block. Occasionally Vantage looks directly at the viewer (every 12–15s).
- **Background:** Deep black `#0A0A0F` with subtle violet film grain (animated noise, 8% opacity).
- **Emotional target:** _"This is not WordPress. This is not Wix. This is something else entirely."_
- **CTA:** `See our work →` → scrolls to `#vt-gallery`.
- **Wow moment:** Vantage's first eye-contact glance — the visitor realises the mascot is actually watching them back.

---

### 4 — SCROLLYTELLING · HIS ORIGIN
- **ID:** `vt-origin`
- **Purpose:** Turn the visitor into a reader. Make them invest 20 seconds of emotional attention.
- **Layout:** Full-viewport sticky container. Video scrubs frame-by-frame as the user scrolls. Text reveals in parallel on the right column in 4 acts.
- **The 4 acts:**
  1. **`Act I — The Developer`** — "Marcus worked nights. Every pixel mattered. Every millisecond counted."
  2. **`Act II — The Accident`** — "One impossible deadline. One surge of pure digital energy. One moment of fusion."
  3. **`Act III — The Awakening`** — "He didn't just know code anymore. He was code."
  4. **`Act IV — Vantage`** — "A name. A standard. A promise: built different, coded perfect."
- **Video placeholder:** 15s MP4 loop (supplied later). For now: `data-video-src="placeholder"` attribute + black canvas.
- **Background:** Transitions `#0A0A0F` → `#1A0B2E` (deep violet) as you scroll through the 4 acts.
- **Emotional target:** _Investment. Identification. "I want to know what happens next."_
- **CTA:** None — pure story beat.
- **Wow moment:** Act III — the instant "he was code" appears, the background glitches for 200ms and shifts to violet.

---

### 5 — CAROUSEL 3D · THE UNIVERSE
- **ID:** `vt-universe`
- **Purpose:** Reinforce the world-building. Show range.
- **Layout:** 3D carousel, `perspective: 1200px`. Cards rotate on the Y-axis in a circle of 4 (minimum). Auto-rotate every 5s. Drag-to-rotate on desktop, swipe on mobile.
- **Card style:** Cyber aesthetic — scan-line overlay, soft radial glow, floating particles behind the card.
- **Card content (each):** Hero photo (transparent background) + a quote from his universe, attributed to him.
- **The 4 cards:**
  1. **`Origin`** — violet (`#7C3AED`) — _"Perfection isn't a feature. It's the baseline."_
  2. **`Conflict`** — red (`#DC2626`) — _"Every shortcut is a future bug. I don't take shortcuts."_
  3. **`Power`** — electric blue (`#00D4FF`) — _"Speed isn't optional. It's oxygen."_
  4. **`Victory`** — gold (`#D4A855`) — _"We don't ship average. Ever."_
- **Emotional target:** _Mystery. "There's a whole world here."_
- **CTA:** Drag hint — "Drag to explore."
- **Wow moment:** The scan-line aligning across all 4 cards for a frame when they're in rest position.

---

### 6 — POWERS & CAPABILITIES
- **ID:** `vt-powers`
- **Purpose:** Translate the mythology into concrete agency value.
- **Layout:** 3-column grid. Each column = one power. Sticky header "His Powers. Our Standards." Background color shifts section-wide as you scroll through the 3.
- **The 3 powers:**
  1. **`Strength`** — _Code solidity._ Icon: shield-code hybrid, animated SVG draw-on-scroll. Counter: **100% precision** (counts from 0 → 100%).
  2. **`Speed`** — _Performance._ Icon: lightning through a browser window, draw-on-scroll. Counter: **0ms reaction** (pulses at 0).
  3. **`Precision`** — _Visual impact._ Icon: crosshair locking on target, draw-on-scroll. Counter: **∞ endurance** (infinity symbol, slowly rotating).
- **Background shift:** `#0A0A0F` → `#1A0B2E` → `#2E0B1A` across the 3 powers as you scroll.
- **Emotional target:** _Respect. "These people are operators, not artists."_
- **CTA:** `See our work →` (repeats the hero CTA — consistency).
- **Wow moment:** All 3 SVGs complete their draw simultaneously when the section hits center-viewport.

---

### 7 — AGENCY SERVICES
- **ID:** `vt-services`
- **Purpose:** The business pitch. The actual offer.
- **Layout:** 3 glassmorphism cards, side by side on desktop, stacked on mobile. Frosted glass, violet gradient borders, subtle hover lift.
- **The 3 services:**
  1. **`Premium Templates`** — From **€800**. Production-ready landing pages. Delivered in 48h. One client per template per city.
  2. **`Custom Sites`** — From **€4,500**. Fully bespoke. 3-week delivery. Unlimited revisions during the sprint.
  3. **`Maintenance & Care`** — From **€250/month**. We watch your site so you don't have to. SLA response under 4h.
- **Each card contains:** Service name · Price · 3 bullet features · CTA `Start →`
- **Emotional target:** _Clarity. "I understand exactly what I can buy."_
- **CTA:** `Start →` on each card → scrolls to `#vt-contact` with the service pre-selected.
- **Wow moment:** On hover, the card lifts 12px AND the violet gradient border animates a 360° sweep.

---

### 8 — PHOTO GALLERY
- **ID:** `vt-gallery`
- **Purpose:** Visual proof. The hero is a character, not a stock asset.
- **Layout:** Masonry grid, 4 columns desktop / 2 tablet / 1 mobile. Hero images with transparent backgrounds float in the grid — no card frames.
- **Content:** 10–12 hero photos in varied poses. One tile is **2× larger** and contains an autoplay-muted video loop.
- **Hover effect:** Liquid distortion (WebGL shader or CSS `filter: url(#liquid)`), radial ripple from cursor.
- **Emotional target:** _Delight. "I want to spend time here."_
- **CTA:** None — free exploration is the point.
- **Wow moment:** The liquid ripple propagating to adjacent tiles for a beat when cursor moves fast.

---

### 9 — THE LORE
- **ID:** `vt-lore`
- **Purpose:** Depth. Editorial gravity. The brand that takes itself seriously enough to build a mythology.
- **Layout:** Two parts.
  - **Top:** Editorial text block — a paragraph of long-form copy about the hero's world, written in present-tense mythological voice.
  - **Bottom:** Horizontal scroll timeline — chapters of his story. Each chapter = one card with a year, a title, and a 2-line synopsis. Scrub horizontally by scroll or drag.
- **The timeline (5 chapters):**
  1. **`2019 — Before`** — Marcus ships his first site. A local bakery in Athens. It loads in 3.2 seconds. He is ashamed.
  2. **`2022 — The Surge`** — The accident. The fusion.
  3. **`2023 — First Signal`** — The first client to call him after the change doesn't understand why their conversion rate tripled.
  4. **`2025 — The Standard`** — Vantage becomes a byword in the Athenian web scene for "the ones who don't ship junk".
  5. **`Now`** — You're reading this. Which means we're working with you next.
- **Background:** Dark textured — linen noise + violet vignette.
- **Typography:** Key quotes rendered in SVG calligraphic stroke that draws in on scroll.
- **Emotional target:** _Immersion. "I'm inside a story, not a brochure."_
- **CTA:** None.
- **Wow moment:** The SVG calligraphy for the final line `Now, you're reading this` writing itself stroke-by-stroke as you hit it.

---

### 10 — JOIN THE UNIVERSE · FINAL CTA
- **ID:** `vt-cta-final`
- **Purpose:** Close. Capture. Convert.
- **Layout:** Full-viewport black section. Hero present LARGE in the background, 40% opacity, behind the content. Foreground: headline + form.
- **Headline:** _"Join the Universe."_
- **Subheadline:** _"Three ways in. Pick yours."_
- **3 pathways presented as tabs:**
  1. `Newsletter` — _"Monthly. No spam. Real insights from the build."_ → email input + **`Subscribe`**
  2. `Collaborate` — _"You have a project. We have a standard. Let's talk."_ → 3-field contact form + **`Work with us`**
  3. `Just say hi` — _"Sometimes that's enough."_ → single message box + **`Send`**
- **Background glow:** Violet orb behind the hero, slow pulse (4s cycle).
- **Emotional target:** _Invitation. "This isn't a sales page. It's a door."_
- **CTA (primary):** `Work with us` on the `Collaborate` tab → form submit → success toast + scroll lock overlay "We'll be in touch within 24h."
- **Wow moment:** Switching tabs morphs the submit button from `Subscribe` → `Work with us` → `Send` with a letter-by-letter character swap animation.

---

### 11 — FOOTER
- **ID:** `vt-footer`
- **Purpose:** Close the frame. Brand integrity.
- **Layout:** Minimal, single-row on desktop, stacked on mobile. 40px vertical padding.
- **Content:**
  - **Left:** VANTAGE logo + emblem
  - **Centre:** Links — `Origin · Services · Lore · Contact · Privacy`
  - **Right:** Address — **`Athens, Greece · hello@vantage-agency.com`**
- **Legal line:** `© 2026 Vantage Web Agency — All rights reserved.`
- **Emotional target:** _Confidence. "Real address. Real agency. Not a dropshipper."_
- **Wow moment:** Hovering the emblem triggers a 400ms violet pulse that crosses the entire footer row.

---

## NAVIGATION ANCHORS (quick reference)

| Anchor | Target section |
|--------|----------------|
| `#origin` | `vt-origin` |
| `#universe` | `vt-universe` |
| `#powers` | `vt-powers` |
| `#services` | `vt-services` |
| `#gallery` | `vt-gallery` |
| `#lore` | `vt-lore` |
| `#contact` | `vt-cta-final` |
| `#newsletter` | Newsletter tab inside `vt-cta-final` |

---

## DESIGN INVARIANTS (to hold across all sections)

- **Palette:** `#0A0A0F` (black base) · `#1A0B2E` (deep violet) · `#7C3AED` (violet accent) · `#00D4FF` (electric blue highlight) · `#D4A855` (gold accent) · `#F5F5F7` (off-white text)
- **Fonts:** Display serif italic (titles) · Bold condensed sans (subheads) · Inter (body) — all Google Fonts, subset to Latin.
- **Violet grain overlay:** 8% opacity, animated noise, present globally over the black base.
- **Preloader safety:** 3s hard cap via `setTimeout` force-hide.
- **`localStorage`:** always wrapped in try/catch (iframe-sandbox safety).
- **WCAG AA:** 4.5:1 contrast minimum, keyboard nav, `prefers-reduced-motion` respected.
- **LCP target:** < 2.5s — hero video poster preloaded, fonts preloaded.

---

## CONTENT INVENTORY — zero lorem ipsum confirmed

Every placeholder above is real, shippable English copy. No section contains filler text. Body paragraphs, quotes, counters, testimonials, and CTAs are all written out in full.
