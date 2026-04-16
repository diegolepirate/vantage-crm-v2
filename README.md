# PIXEL FORGE — Template Premium
## Motion Design & Brand Animation Studio
## Vantage Web Agency — Livrable Client

---

## CONTENU DU LIVRABLE

```
pixel-forge/
│
├── index.html              ← Site complet (tout-en-un)
├── pixel-forge-dark.css    ← Mood Dark Forge
├── pixel-forge-minimal.css ← Mood Minimal Craft
├── pixel-forge-cyber.css   ← Mood Cyber Organic
└── README.md               ← Ce document
```

---

## MISE EN LIGNE RAPIDE

### Netlify (recommandé — 2 minutes)

1. Aller sur [netlify.com](https://netlify.com)
2. Drag & drop du dossier `pixel-forge/`
3. Le site est en ligne immédiatement
4. Optionnel : connecter un domaine personnalisé

### Vercel

```bash
npx vercel deploy --prod
```

### FTP classique

Uploader tous les fichiers à la racine du serveur.
Aucun fichier serveur requis — tout est statique.

---

## PERSONNALISER LE SITE (15 minutes)

### Étape 1 — Changer les textes

Dans `index.html`, rechercher et remplacer :

| Remplacer | Par |
|-----------|-----|
| `Pixel Forge` | Nom de votre studio |
| `Motion. Identity. Alive.` | Votre tagline |
| `hello@pixelforge.studio` | Votre email |
| `Paris · Remote Worldwide` | Vos villes |
| `140+` | Votre nombre de projets |
| `98%` | Votre satisfaction clients |
| `4 Years Studio` | Votre ancienneté |
| `Lumio App`, `Arc Browser`, etc. | Vos vrais projets |

### Étape 2 — Changer les couleurs (8 variables)

Dans `index.html`, dans le bloc `<style>`, modifier :

```css
:root {
  --pf-rose:   #FF3CAC;  /* Votre couleur 1 */
  --pf-violet: #7B2FBE;  /* Votre couleur 2 */
  --pf-orange: #FF6B35;  /* Votre couleur 3 */
  --pf-white:  #FFFFFF;  /* Blanc ou crème */
  --pf-ink:    #0A0A0F;  /* Noir ou très sombre */
  --pf-font-display: 'Plus Jakarta Sans', sans-serif;
  --pf-font-body:    'Inter', sans-serif;
  --pf-r-xl: 20px;       /* 4px angulaire, 32px très rond */
}
```

### Étape 3 — Changer les images

Remplacer les URLs Unsplash par vos vraies images :

```html
https://images.unsplash.com/photo-XXXXXXX
→ ./images/mon-image.jpg
```

**Format recommandé :**
- Hero principal : 1200x800px, WebP, < 150 Ko
- Work grid items : 800x600px, WebP, < 80 Ko
- Showreel thumbnail : 1400x788px, WebP, < 200 Ko

### Étape 4 — Activer le formulaire

```javascript
/* Option A — Netlify Forms (gratuit) */
// Ajouter data-netlify="true" sur le <form>

/* Option B — Formspree */
fetch('https://formspree.io/f/VOTRE_ID', {
  method: 'POST',
  body:   new FormData(form),
  headers: { Accept: 'application/json' }
});

/* Option C — EmailJS */
emailjs.send('SERVICE_ID', 'TEMPLATE_ID', { ... });
```

---

## CHANGER DE MOOD VISUEL

Ajouter dans `<head>` après le CSS principal :

```html
<link rel="stylesheet" href="pixel-forge-dark.css">
<link rel="stylesheet" href="pixel-forge-minimal.css">
<link rel="stylesheet" href="pixel-forge-cyber.css">
```

Pour revenir au défaut, retirer la ligne.

---

## EFFETS SIGNATURE

### Hero
- Trail de particules qui suit la souris
- 3 blocs bento arrivant de directions différentes
- Perspective 3D sur la grille
- Canvas mesh 3 blobs animés

### Trust Bar
- Gradient individuel par client au hover
- Inversion de direction au scroll up

### Showreel
- Flash obturateur au clic play
- Parallax thumbnail avec la souris
- Ring pulsant autour du bouton play

### Services
- Numéro "02" géant en fond
- Gradient titre adapté par card au hover
- Tilt 3D selon la souris
- Spotlight suit la souris dans chaque card

### Work Grid
- Couleur dominante par projet au hover
- Grain de film cinématique
- Ligne gradient rose→orange en bas
- Filtrage GSAP animé

### Process
- Icônes SVG qui se tracent à l'activation
- Rotation lente continue
- Ligne timeline scrub au scroll

### Pricing
- Canvas orbital autour d'Ignite
- Spring agressif au reveal
- Halo respirant continu

### Testimonials
- Quote marks géantes au hover
- Flood par colonne au reveal
- Carousel mobile scroll-snap

### FAQ
- Typewriter sur les réponses
- Fond rose à l'ouverture

### CTA Finale
- 24 particules ascendantes
- Titre lignes masquées
- Mesh intensity au scroll

### Contact
- Colonne info colorée au focus champ

### Footer
- Email révélé lettre par lettre
- Border gradient animée

---

## EASTER EGG

Taper **↑ ↑ ↓ ↓ ← → ← → B A** pour le **FORGE MODE**.

---

## PERFORMANCES

Scores Lighthouse attendus :
- Performance :    90+
- Accessibilité :  95+
- Best Practices : 95+
- SEO :            100

Optimisations intégrées :
- Hero image préchargée (LCP < 2.5s)
- Scripts en `defer`
- Lazy loading images hors fold
- `aspect-ratio` sur tous conteneurs (CLS = 0)
- Canvas et blobs désactivés sur mobile
- `backdrop-filter` désactivé sur mobile
- `gsap.ticker.lagSmoothing(0)`
- Animations pausées onglet caché
- Cleanup ScrollTriggers au déchargement

---

## ACCESSIBILITÉ — WCAG 2.1 AA

- Navigation clavier (Tab + Arrow keys)
- Focus visible universel
- Skip link "Skip to main content"
- ARIA labels complets
- Contraste minimum 4.5:1
- `prefers-reduced-motion` respecté
- `forced-colors` supporté
- Focus trap modales
- Live regions dynamiques

---

## SEO

- Meta title + description optimisées
- Open Graph + Twitter Card
- Schema.org JSON-LD (Organization + FAQPage + Offers + Reviews)
- Heading hierarchy H1→H2→H3
- Alt text descriptif
- Canonical URL
- `rel="noopener noreferrer"` externes

---

## STACK TECHNIQUE

```
HTML5 sémantique     → index.html (tout-en-un)
CSS3                 → Variables, Grid, Flexbox, Animations
JavaScript           → Vanilla ES5+, modules IIFE
GSAP 3.12.5         → ScrollTrigger, Flip
Lenis 1.1.14        → Smooth scroll
Google Fonts         → Plus Jakarta Sans + Inter
Canvas API           → Mesh hero + particules pricing
IntersectionObserver → Lazy loading
ResizeObserver       → FAQ heights
PerformanceObserver  → Core Web Vitals (dev)
```

**Aucune dépendance npm. Aucun build step. Zéro config.**

---

## COMPATIBILITÉ NAVIGATEURS

| Navigateur | Support |
|------------|---------|
| Chrome 90+ | Complet |
| Firefox 88+ | Complet |
| Safari 14+ | Complet |
| Edge 90+ | Complet |
| iOS Safari 14+ | Optimisé |
| Android Chrome | Optimisé |
| IE 11 | Non supporté |

---

## TARIFICATION SUGGÉRÉE

| Offre | Prix | Inclus |
|-------|------|--------|
| Template seul | €500 | index.html + 3 moods |
| Template + couleurs | €750 | + 1h customisation |
| Template + personnalisation complète | €1,200 | + textes + images + formulaire |
| Template + maintenance | €1,200 + €250/an | + hébergement + mises à jour |

---

## CHECKLIST AVANT LIVRAISON

**CONTENU :**
- [ ] Tous les textes remplacés
- [ ] Email, téléphone, adresse à jour
- [ ] Vraies images
- [ ] Vraies stats
- [ ] Vrais témoignages

**TECHNIQUE :**
- [ ] Formulaire connecté
- [ ] Meta title + description
- [ ] Open Graph image (1200x630px)
- [ ] Favicon personnalisé
- [ ] Analytics (GA4 ou Plausible)
- [ ] Domaine configuré
- [ ] HTTPS activé
- [ ] Lighthouse > 90

**QUALITÉ :**
- [ ] Test Chrome / Firefox / Safari
- [ ] Test mobile iOS + Android
- [ ] Navigation clavier
- [ ] Formulaire testé
- [ ] Liens vérifiés
- [ ] Console sans erreurs
- [ ] Easter egg testé

---

## JOURNAL DES PROMPTS (17/17)

```
Phase 1 — Planification
  1.1  Sitemap global
  1.2  Design Brief complet
  1.3  Variantes 3 moods

Phase 2 — Construction
  2.1  HTML sémantique
  2.2  CSS Design System
  2.3  Architecture modulaire JS

Phase 3 — Animations
  3.1  GSAP + Lenis + Preloader + Reveals
  3.2  Logique fonctionnelle
  3.3  Effets visuels avancés
  3.4  Micro-interactions & Polish
  3.5  Effets signature par section

Phase 4 — Optimisation
  4.1  Performance & Core Web Vitals
  4.2  Accessibilité & SEO
  4.3  Bug hunting & Corrections
  4.4  Polish final

Phase 5 — Variations & Livrable
  5.1  3 variations moods CSS
  5.2  Documentation complète
```

---

## SUPPORT

Template créé par **Vantage Web Agency**

*Template version : 1.0*
*Vantage Web Agency — Premium Templates*
