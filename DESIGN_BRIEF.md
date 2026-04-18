# DESIGN BRIEF — VANTAGE
**Complete design system for the VANTAGE mascot landing page.**
Template: VANTAGE · Agency: Vantage Web Agency · Location: Athens, Greece
Tagline: _"Built different. Coded perfect."_
Language: English — 100% everywhere (content, labels, buttons, errors, meta, comments).

This document is documentation only. Zero code. It is the rulebook the implementation prompts will follow.

---

## 1 · PALETTE

```css
:root {
  /* Darks */
  --vt-black:        #0A0A0F;  /* Main background */
  --vt-void:         #050508;  /* Deepest sections */
  --vt-purple-deep:  #1E0A3C;  /* Section backgrounds */

  /* Purples — primary brand spine */
  --vt-purple:       #6B21A8;  /* Primary accent */
  --vt-purple-mid:   #7C3AED;  /* Hover states */
  --vt-purple-light: #A855F7;  /* Glow effects */
  --vt-purple-glow:  rgba(168, 85, 247, .15);
  --vt-purple-dim:   rgba(168, 85, 247, .08);

  /* Lights */
  --vt-white:        #F8F8FF;  /* Primary text */
  --vt-white-70:     rgba(248, 248, 255, .70);
  --vt-white-40:     rgba(248, 248, 255, .40);
  --vt-white-10:     rgba(248, 248, 255, .10);

  /* Metallic */
  --vt-chrome:       #C0C0D0;  /* Metallic details */
}
```

---

## 2 · TYPOGRAPHY — Golden Ratio Scale (φ ≈ 1.618)

### Scale

| Role | Size | Font |
|------|------|------|
| Display H1 | `clamp(72px, 10vw, 140px)` | **Rajdhani Bold** (or Bebas Neue) |
| H2 | `clamp(44px, 6vw, 86px)` | Rajdhani Bold |
| H3 | `clamp(27px, 3.8vw, 53px)` | Rajdhani SemiBold |
| H4 | `clamp(17px, 2.3vw, 33px)` | Inter 600 |
| Body | `18px` | **Inter 300** (light) |
| Caption | `14px` | Inter 400 |
| Label | `11px` | Inter 600 · `letter-spacing: .18em` · `text-transform: uppercase` |

### Font assignments

- **Title font:** Rajdhani Bold — superhero feel, free Google Font.
- **Body font:** Inter — clean, readable.
- **Quote font:** Cormorant Garamond italic — editorial moments (lore, hero quotes in carousel).

### Typography echo rule (titles with multiple lines)

| Line | Opacity / scale weight |
|------|------------------------|
| Line 1 | **100%** (full weight) |
| Line 2 | **85%** |
| Line 3 | **72%** |

Applied to multi-line H1 and H2 entrances.

---

## 3 · SPACING — Golden Ratio enforcement

### Vertical rhythm

- **Space before an H2 = 1.618 × space after the H2.** Every heading "announces itself."
- **30% of every section must be empty space.** Measure before shipping — this is a review gate.

### Section padding (progressive expansion)

| Section | Top / bottom padding |
|---------|----------------------|
| `vt-hero` | `120px` |
| `vt-origin` | `140px` |
| `vt-universe` | `160px` |
| `vt-powers` | `140px` |
| `vt-services` | **`180px`** (peak) |
| `vt-gallery` | `160px` |
| `vt-lore` | `140px` |
| `vt-cta-final` | `160px` |
| `vt-footer` | `80px` |

Padding grows toward `vt-services`, then gently recedes — visual "breath" mimicking a wave.

---

## 4 · CINEMATIC EASING — one easing for everything

```css
:root {
  --vt-ease: cubic-bezier(0.76, 0, 0.24, 1);
}
```

### Rules

- **Use `--vt-ease` for every editorial element.** Reveals, parallax, text, images.
- **No spring. No bounce.** Bouncing belongs to cartoons, not to Vantage.
- **`elastic.out` is allowed — but only on interactive elements** (buttons, cards, toggles). Never on text or images.

---

## 5 · ANIMATION TIMING RULES

| Rule | Value |
|------|-------|
| **Minimum delay before any animation** | `80ms` (never `0ms`) |
| **Exit duration vs entry** | Exit = Entry × **1.35** |
| **Last element in stagger** | +**15%** duration vs the rest |
| **Typography echo** | Line 1 = 100%, Line 2 = 85%, Line 3 = 72% of initial opacity/weight |

---

## 6 · FILM GRAIN (global overlay)

- **Position:** `fixed` · full viewport · `z-index: 9999` · `pointer-events: none`
- **Source:** SVG `<feTurbulence baseFrequency=".65" />` — animated noise
- **Opacity:** `.032` — always on, every section, every frame
- **Animation:** 8-frame loop, `steps(2)` (stuttering, not smooth — that's the point)
- **Performance:** `animation-play-state: paused` when `document.hidden === true`
- **Accessibility:** `aria-hidden="true"`

---

## 7 · GLASSMORPHISM STANDARD (service cards)

```css
.vt-glass-card {
  background: rgba(255, 255, 255, .04);
  backdrop-filter: blur(12px) saturate(1.4);
  border: 1px solid rgba(255, 255, 255, .10);
  border-radius: 24px 24px 24px 4px;  /* asymmetric — luxury rule */
}
```

**Asymmetric border-radius is a hard rule across the template.** Uniform 8px = generic. Asymmetric = bespoke.

---

## 8 · CARD SYSTEM (generic)

| Property | Rule |
|----------|------|
| **Shape** | Asymmetric border-radius — never uniform 8px |
| **Texture** | Noise grain at `.035` opacity on card background |
| **Shadow** | Dynamic — moves opposite to the tilt direction (real physical light) |
| **Idle animation** | Floating breathe — `translateY 0 → -4px`, 4s loop, staggered per card |
| **Hover** | 3D tilt ±5° with dynamic shadow |
| **Containment** | `contain: layout style` + `aspect-ratio` defined |

---

## 9 · CYBER CARD (3D carousel section `vt-universe`)

### Required structure (exact, from CRM reference)

```
.vt-canvas
  └── 25× .tr  (25 transform-tr divs forming the grid base)
.vt-cyber-lines (4 corners — top-left, top-right, bottom-left, bottom-right)
.vt-scan-line (vertical sweep)
.vt-glow-1
.vt-glow-2
.vt-glow-3
.vt-particles (6 floating dots)
.vt-card-glare (hover effect)
```

### The 4 color variants

| Variant | Background | `glow-1` | `scan-line` |
|---------|------------|---------|-------------|
| **ORIGIN** · violet | `#0D0A1F` | `rgba(168, 85, 247, .4)` | `rgba(232, 121, 249, .6)` |
| **CONFLICT** · red | `#1F0A0A` | `rgba(239, 68, 68, .4)` | `rgba(252, 165, 165, .6)` |
| **POWER** · blue | `#0A0F1F` | `rgba(59, 130, 246, .4)` | `rgba(147, 197, 253, .6)` |
| **VICTORY** · gold | `#1A1400` | `rgba(245, 158, 11, .4)` | `rgba(253, 224, 71, .6)` |

---

## 10 · PHOTO TREATMENT — all hero images

```css
.vt-hero-img {
  filter: contrast(1.05) saturate(1.1) brightness(.95);
}
```

- **Consistency:** same filter on every image, same temperature.
- **Background:** the hero always floats — remove background via PNG alpha or CSS `isolation`. **Never** frame him in a card.

---

## 11 · CONTRAST NARRATIVE — section sequence

Each section's atmosphere is pre-mapped. Adjacent sections **must differ on at least 2 of these axes:** luminosity / density / movement / temperature / scale.

| Section | Atmosphere |
|---------|-----------|
| `vt-preloader` | **black + impact** |
| `vt-navbar` | **transparent** |
| `vt-hero` | **black + video (light emanates from video)** |
| `vt-origin` | **black → deep purple shift** |
| `vt-universe` | **deep purple (darkest point of the page)** |
| `vt-powers` | **black → purple → black (color shift on scroll)** |
| `vt-services` | **deep purple (glassmorphism cards)** |
| `vt-gallery` | **near-black (images breathe)** |
| `vt-lore` | **black textured (linen + vignette)** |
| `vt-cta-final` | **void black (most intense)** |
| `vt-footer` | **`#050508` (resolution)** |

---

## 12 · EMOTIONAL TARGETS per section

| Section | Target emotion |
|---------|----------------|
| `vt-preloader` | _"I have never seen anything like this"_ |
| `vt-hero` | _"This agency operates at a different level"_ |
| `vt-origin` | _"I want to know more — I cannot stop scrolling"_ |
| `vt-universe` | _"This universe is real and I want to enter it"_ |
| `vt-powers` | _"These people are truly capable"_ |
| `vt-services` | _"I can afford this and it will be worth it"_ |
| `vt-gallery` | _"This hero is alive — he is real to me"_ |
| `vt-lore` | _"There is depth here — this is not a template"_ |
| `vt-cta-final` | _"I need to contact them right now"_ |
| `vt-footer` | _"I know exactly who these people are"_ |

---

## 13 · VISUAL REFERENCES

| Dimension | Reference |
|-----------|-----------|
| **Typography energy** | Marvel Studios title cards |
| **Animation timing** | Apple product pages (precise, no waste) |
| **Card atmosphere** | Cyberpunk 2077 UI meets luxury editorial |
| **Overall feeling** | _What if a superhero studio built a web agency?_ |

---

## 14 · VARIANT_MAP for this template

| Dimension | Value |
|-----------|-------|
| `card_shape` | `asymmetric_rounded` (24px 24px 24px 4px) |
| `card_hover` | `tilt_dynamic_shadow` |
| `card_idle` | `floating_breathe` |
| `text_reveal` | `vertical_mask` (lines rise from overflow) |
| `preloader` | `screen_crack_custom` |
| `counter_style` | `scramble_resolve` |
| `interaction_perso` | `dark` (fast ×0.8, snap, magnetic 20px) |
| `cursor_trail` | `sector_words` (Built / Coded / Perfect / Vantage) |
| `ambient_bg` | `breathing_orb` |
| `section_transition` | `clip_wipe` |
| `button_border` | `from_center` |
| `button_arrow` | `points_to_cursor` |

---

## 15 · PERFORMANCE RULES

- **All images:** `loading="lazy"` **except** the hero video poster.
- **Hero video:** `loading="eager"` · `preload="auto"`.
- **`will-change`:** add **before** animation starts, remove in `onComplete`. Never leave it permanently.
- **WebGL / heavy effects:** disabled if `isLowEnd` or `isMobile` (detect via `navigator.deviceMemory <= 4` or `navigator.hardwareConcurrency <= 4` or `matchMedia('(max-width: 768px)')`).
- **Film grain:** pause if `document.hidden`.
- **LCP target:** < 2.5s (hero video poster preloaded, fonts preloaded with `rel="preload"`).
- **CLS target:** < 0.1 (every image has `aspect-ratio` or explicit width/height).
- **INP target:** < 200ms (no blocking JS on interaction).

---

## 16 · ACCESSIBILITY

- **All animations** respect `prefers-reduced-motion: reduce` — fall back to opacity-only fades.
- **Focus visible** on every interactive element — `outline: 2px solid var(--vt-purple-light); outline-offset: 3px;`.
- **Film grain div:** `aria-hidden="true"`.
- **Hero video:** `aria-hidden="true"` (decorative, not informational).
- **All buttons** have accessible English names via text content or `aria-label`.
- **Contrast:** 4.5:1 minimum for body text, 3:1 for large text (WCAG AA).
- **Touch targets:** 44 × 44px minimum on mobile.
- **Keyboard:** full navigability, skip-link to main content, focus trap on modals.

---

## 17 · DESIGN INVARIANTS (quick reference — must hold everywhere)

1. Asymmetric border-radius on all cards.
2. One easing curve: `--vt-ease`.
3. Minimum 80ms delay on every animation.
4. Film grain: always on, opacity .032, paused on hidden tab.
5. 30% empty space per section.
6. Adjacent sections differ on ≥2 axes.
7. Hero image filter: `contrast(1.05) saturate(1.1) brightness(.95)`.
8. All text in English, always.
9. Preloader: 3s hard cap (force-hide safety).
10. `prefers-reduced-motion`: respected, no exceptions.

---

## 18 · NOT IN SCOPE of this brief

- **Implementation details** (specific GSAP timelines, HTML structure) — those arrive in later prompts.
- **Content wording** (final copy) — lives in `SITEMAP.md`.
- **Template placement in the CRM** — handled by inject scripts at the end.

---

*End of design brief. Zero code. All rules documented.*
