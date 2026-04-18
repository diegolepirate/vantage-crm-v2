# MOODS — VANTAGE
**Four visual moods for the VANTAGE template.**
Each mood overrides the CSS variables defined in `DESIGN_BRIEF.md`. Same structure, different energy. The switcher (delivered later) injects/removes a single `<link>` tag per mood.

Default mood: **SHADOW** (requires no override file — uses the base palette).

---

## MOOD 1 — SHADOW (default)

**Personality:** Dark, powerful, mysterious. The hero moves in the void before he speaks. This is the baseline — every other mood is a deviation from it.
**Audio vibe:** Deep drone + subtle heartbeat.

### CSS variable overrides

```css
/* SHADOW uses the base palette from DESIGN_BRIEF.md — no overrides. */
:root {
  --vt-black:        #0A0A0F;
  --vt-void:         #050508;
  --vt-purple-deep:  #1E0A3C;
  --vt-purple:       #6B21A8;
  --vt-purple-mid:   #7C3AED;
  --vt-purple-light: #A855F7;
  --vt-purple-glow:  rgba(168, 85, 247, .15);
  --vt-purple-dim:   rgba(168, 85, 247, .08);
  --vt-accent:       var(--vt-purple);
  --vt-accent-mid:   var(--vt-purple-mid);
  --vt-accent-light: var(--vt-purple-light);
  --vt-accent-glow:  var(--vt-purple-glow);
  --vt-accent-dim:   var(--vt-purple-dim);
}
```

### Sections that change most dramatically
None — this is the reference.

### Button & CTA
- Primary (`Work with us`): violet fill `#7C3AED`, white text, violet glow on hover.
- Secondary (`See our work →`): transparent, 1px violet border, white text.

### Navbar
- Transparent → `rgba(10, 10, 15, .72)` on scroll + blur(18px).
- Emblem: white stroke on black.
- CTA: violet fill, white text.

---

## MOOD 2 — CRIMSON

**Personality:** Aggressive, urgent, combat-ready. This is the hero mid-fight — adrenaline locked, nothing wasted.
**Audio vibe:** Intense low-frequency pulse.

### CSS variable overrides

```css
/* apex-crimson.css equivalent — vantage-crimson.css */
:root {
  /* Base stays dark */
  --vt-black:        #0A0A0F;
  --vt-void:         #050508;

  /* Violet → Crimson red */
  --vt-purple-deep:  #3C0A0A;             /* was #1E0A3C */
  --vt-purple:       #DC2626;             /* was #6B21A8 — PRIMARY ACCENT */
  --vt-purple-mid:   #EF4444;             /* was #7C3AED */
  --vt-purple-light: #F87171;             /* was #A855F7 */
  --vt-purple-glow:  rgba(220, 38, 38, .15);  /* was violet */
  --vt-purple-dim:   rgba(220, 38, 38, .08);

  /* Alias remap — keeps downstream selectors untouched */
  --vt-accent:       var(--vt-purple);
  --vt-accent-mid:   var(--vt-purple-mid);
  --vt-accent-light: var(--vt-purple-light);
  --vt-accent-glow:  var(--vt-purple-glow);
  --vt-accent-dim:   var(--vt-purple-dim);
}
```

### Sections that change most dramatically
- **`vt-hero`** — the ambient glow behind the hero video goes from mysterious violet haze to coiled red tension.
- **`vt-universe`** — the carousel's glow rings now read as warning lights, not magic.
- **`vt-cta-final`** — the background orb pulses like a heartbeat under pressure.

### Button & CTA
- Primary: crimson fill `#EF4444`, white text, red glow `box-shadow: 0 0 32px rgba(239, 68, 68, .4)`.
- Secondary: transparent, 1px `#DC2626` border, white text.

### Navbar
- Scroll background: `rgba(15, 10, 10, .72)` + blur(18px).
- Emblem: red-tinted white stroke.
- CTA: crimson fill, white text.

---

## MOOD 3 — ARCTIC

**Personality:** Precise, cold, technical. The hero as instrument — surgical, unblinking, unhurried.
**Audio vibe:** Sharp electronic tones.

### CSS variable overrides

```css
/* vantage-arctic.css */
:root {
  /* Base shifts cool */
  --vt-black:        #050A0F;             /* was #0A0A0F — near-black with blue tint */
  --vt-void:         #020508;
  --vt-purple-deep:  #0A1F3C;             /* was #1E0A3C */

  /* Violet → Ice blue */
  --vt-purple:       #0EA5E9;             /* was #6B21A8 — PRIMARY ACCENT */
  --vt-purple-mid:   #38BDF8;             /* was #7C3AED */
  --vt-purple-light: #7DD3FC;             /* was #A855F7 */
  --vt-purple-glow:  rgba(14, 165, 233, .15);
  --vt-purple-dim:   rgba(14, 165, 233, .08);

  --vt-accent:       var(--vt-purple);
  --vt-accent-mid:   var(--vt-purple-mid);
  --vt-accent-light: var(--vt-purple-light);
  --vt-accent-glow:  var(--vt-purple-glow);
  --vt-accent-dim:   var(--vt-purple-dim);
}
```

### Sections that change most dramatically
- **`vt-powers`** — the three draw-on-scroll SVG icons now read as blueprint diagrams, not superpowers.
- **`vt-services`** — glassmorphism cards shift toward a laboratory-instrument feel.
- **`vt-lore`** — the editorial text reads as technical documentation rather than mythology.

### Button & CTA
- Primary: ice blue fill `#38BDF8`, deep-navy text `#0A1F3C`, cyan glow.
- Secondary: transparent, 1px `#0EA5E9` border, white text.

### Navbar
- Scroll background: `rgba(5, 10, 15, .78)` + blur(18px).
- Emblem: cold-white stroke with subtle cyan inner-glow.
- CTA: ice blue fill, dark-navy text for maximum contrast.

---

## MOOD 4 — GOLD EDITION

**Personality:** Prestigious, victorious, legendary. The hero after the fight — crowned, undisputed, ready to be remembered.
**Audio vibe:** Orchestral swell, epic.

### CSS variable overrides

```css
/* vantage-gold.css */
:root {
  /* Base shifts warm */
  --vt-black:        #0F0A00;             /* was #0A0A0F — warm near-black */
  --vt-void:         #080500;
  --vt-purple-deep:  #3C2400;             /* was #1E0A3C */

  /* Violet → Gold */
  --vt-purple:       #D97706;             /* was #6B21A8 — PRIMARY ACCENT */
  --vt-purple-mid:   #F59E0B;             /* was #7C3AED */
  --vt-purple-light: #FCD34D;             /* was #A855F7 */
  --vt-purple-glow:  rgba(217, 119, 6, .15);
  --vt-purple-dim:   rgba(217, 119, 6, .08);

  --vt-accent:       var(--vt-purple);
  --vt-accent-mid:   var(--vt-purple-mid);
  --vt-accent-light: var(--vt-purple-light);
  --vt-accent-glow:  var(--vt-purple-glow);
  --vt-accent-dim:   var(--vt-purple-dim);
}
```

### Sections that change most dramatically
- **`vt-hero`** — the title "VANTAGE" is no longer a brand, it is a trophy.
- **`vt-gallery`** — photo treatment warms visibly; images read as canonical portraits, not action shots.
- **`vt-cta-final`** — the final orb becomes a sunrise at the edge of the page.

### Button & CTA
- Primary: gold fill `#F59E0B`, black text `#0F0A00`, gold glow.
- Secondary: transparent, 1px `#D97706` border, white text.

### Navbar
- Scroll background: `rgba(15, 10, 0, .74)` + blur(18px).
- Emblem: warm-white stroke with inner gold shimmer.
- CTA: gold fill, black text — the most high-contrast CTA of the four moods.

---

## SHARED ASSUMPTIONS (all moods)

- **Film grain** stays at `.032` opacity — mood-independent.
- **Typography** unchanged across moods — Rajdhani / Inter / Cormorant.
- **Card asymmetric border-radius** (`24px 24px 24px 4px`) unchanged.
- **Easing** (`--vt-ease`) unchanged.
- **Photo filter** (`contrast(1.05) saturate(1.1) brightness(.95)`) unchanged.
- **Accessibility** (focus ring, contrast, touch targets) unchanged — moods never compromise a11y.

---

## DELIVERY NOTES

- SHADOW is the default — lives in the main `<style>` block of `vantage-template.html`.
- The other three moods ship as standalone files:
  - `vantage-crimson.css`
  - `vantage-arctic.css`
  - `vantage-gold.css`
- The mood switcher (added in a later prompt) injects a single `<link>` tag and removes it when switching back to SHADOW.
- All mood files only override variables — they never touch structural CSS.
