# 🎨 Porsche Digest V6 - Design System

## 🎯 Design Principles

```
Premium • Performance • Accessibility • Porsche Heritage
```

### Core Philosophy

1. **Minimalist Premium** - Clean, high-contrast, no clutter
2. **Porsche Heritage** - Gold accents, racing inspiration, quality
3. **Performance First** - 90+ Lighthouse score, fast loading
4. **Accessible by Default** - WCAG 2.1 AA compliant

---

## 🎨 Color Tokens

### Primary Palette

```css
:root {
  /* Porsche Brand Colors */
  --porsche-gold: #d4af37;
  --porsche-black: #0a0a0a;
  --porsche-white: #f5f5f5;
  
  /* Dark Theme */
  --bg-primary: #0a0a0a;
  --bg-secondary: #111111;
  --bg-card: #161616;
  
  /* Text Colors */
  --text-primary: #f5f5f5;
  --text-secondary: #a0a0a0;
  --text-muted: #666666;
  
  /* Accents */
  --accent-green: #27ae60;
  --accent-blue: #3b82f6;
  --accent-red: #c41e3a;
}
```

### Component Colors

| Component | Background | Text | Border |
|---|---|---|---|
| Cards | var(--bg-card) | var(--text-primary) | var(--border) |
| Buttons | var(--gold) | var(--bg-primary) | var(--gold) |
| Badges | var(--accent-green) | white | var(--accent-green) |
| Links | var(--accent-blue) | var(--accent-blue) | none |

---

## 🔤 Typography

### Font Stack

```
Primary: Inter, system-ui, sans-serif (Body text)
Display: Playfair Display, Georgia, serif (Titles)
Grotesk: Space Grotesk, sans-serif (Nav, UI)
```

### Type Scale

| Element | Font | Weight | Size | Line-Height |
|---|---|---|---|---|
| Display | Playfair | 700 | clamp(2.5rem, 8vw, 5rem) | 1.1 |
| H1 | Playfair | 700 | 2.5rem | 1.1 |
| H2 | Space Grotesk | 700 | 1.8rem | 1.3 |
| H3 | Space Grotesk | 600 | 1.3rem | 1.4 |
| Body | Inter | 400 | 1rem | 1.6 |
| Small | Inter | 400 | 0.875rem | 1.4 |

---

## 📐 Layout Grid

### Breakpoints

```css
/* Mobile First */
430px  → 1 column (mobile)
768px  → 2-3 columns (tablet)
1024px → 3-5 columns (desktop)
1200px+ → 5 cards visible (wide)
```

### Card Dimensions

| Card Type | Desktop Width | Mobile Width |
|---|---|---|
| News Carousel | 280px | 158px |
| Market Card | 300px auto | 100% |
| Parts Card | 200px | 100% |
| Video Card | 280x160 | 100% |

---

## 📐 Spacing System

```css
:root {
  --space-0: 0px;
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
}
```

---

## 🔘 Component Library

### Buttons

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  font-family: var(--font-grotesk);
  font-weight: 600;
  font-size: 0.875rem;
  border-radius: 999px;
  transition: all 0.3s ease;
  cursor: pointer;
}

.btn-primary {
  background: var(--gold);
  color: var(--bg-primary);
  border: 1px solid var(--gold);
}

.btn-primary:hover {
  background: transparent;
  box-shadow: 0 0 15px var(--gold);
}
```

### Cards

```css
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: var(--space-6);
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-gold);
}
```

### Carousel

```css
.carousel {
  display: flex;
  gap: var(--space-6);
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}

.carousel-item {
  scroll-snap-align: start;
  min-width: 280px;
  flex: 0 0 auto;
}
```

---

## 🔧 Animation Principles

```
Duration: 300ms (standard), 500ms (page transitions)
Easing: cubic-bezier(0.4, 0, 0.2, 1)
Effects:
  - Subtle hover transforms
  - Slide-in for modals
  - Fade for transitions
  - No excessive animations
```

---

## 📱 Responsive Patterns

### Mobile

- Single column layout
- Hamburger menu
- Touch targets 44px+
- Font sizes increased for readability

### Tablet

- 2-3 column grids
- Navigation stays visible
- Images optimized for portrait

### Desktop

- Wide layouts (5+ columns)
- Full feature set
- Hover states active
- Precise click targets

---

## ✓ Accessibility Checklist

- [✅] Semantic HTML (`<header>`, `<nav>`, `<main>`, `<section>`)
- [✅] Skip navigation link
- [✅] Proper heading hierarchy (H1 → H2 → H3)
- [✅] Color contrast 4.5:1+ (13.5:1 on main text)
- [✅] Keyboard navigable
- [✅] Focus states visible
- [✅] Alt text on all images
- [✅] ARIA labels on interactive elements
- [✅] No keyboard traps
- [✅] Form labels (where applicable)

---

## 🎯 Design Tokens Summary

```json
{
  "colors": {
    "primary": "#d4af37",
    "background": "#0a0a0a",
    "text": "#f5f5f5",
    "accent": {
      "green": "#27ae60",
      "blue": "#3b82f6",
      "red": "#c41e3a"
    }
  },
  "typography": {
    "fontFamily": "Inter, Playfair Display, Space Grotesk",
    "sizes": {
      "h1": "clamp(2.5rem, 8vw, 5rem)",
      "h2": "1.8rem",
      "body": "1rem"
    }
  },
  "spacing": {
    "xs": "4px",
    "sm": "8px",
    "md": "16px",
    "lg": "24px",
    "xl": "32px"
  }
}
```