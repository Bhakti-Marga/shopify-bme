# Darshan Popup — Design Spec

**Date:** 2026-05-07  
**Status:** Approved  

---

## Summary

A fixed-overlay promotional popup for the homepage that announces the Darshan en Lanzarote event. Fully editable via the Shopify theme admin. Renders only within a configured date window; dismissed state persisted in localStorage/sessionStorage.

---

## Implementation

**Single file:** `sections/section__darshan-popup.liquid`  
Added once to `templates/index.json`.

No blocks, no snippet separation — the popup has a fixed layout and is single-use. One file is easier to maintain.

---

## Schema Settings

### Group: Visibilidad

| ID | Type | Default | Notes |
|---|---|---|---|
| `enabled` | checkbox | `true` | Master on/off toggle |
| `start_date` | text | blank | ISO date `2026-01-01`; blank = no start constraint |
| `end_date` | text | blank | ISO date `2026-12-31`; blank = no end constraint |
| `delay_ms` | number | `1500` | Milliseconds before popup opens on first load |
| `dismiss_duration` | select | `permanent` | Options: `session`, `1day`, `7days`, `30days`, `permanent` |

### Group: Media

| ID | Type | Default | Notes |
|---|---|---|---|
| `media_type` | select | `video` | Options: `video`, `image` |
| `video_url` | text | — | CDN or external video URL |
| `image` | image_picker | — | Used as video poster and for image mode |
| `badge_text` | text | `En vivo · Lanzarote` | Pill badge overlaid on media |

### Group: Contenido

| ID | Type | Default | Notes |
|---|---|---|---|
| `eyebrow` | text | `Evento especial · 2026` | Small uppercase label above title |
| `title` | text | `Darshan en Lanzarote` | Main heading |
| `description` | textarea | — | Body paragraph |
| `date_label` | text | `Sábado 21 de noviembre de 2026` | Date row text |
| `location_label` | text | `Lanzarote, Islas Canarias` | Location row text |
| `cta_text` | text | `Reserva tu plaza` | CTA button label |
| `cta_url` | url | `/pages/darshan-lanzarote` | CTA destination |
| `dismiss_text` | text | `No, gracias` | Dismiss link text |

---

## Scheduling Logic (Liquid — server-side)

Evaluated at render time using `date: '%s'` Unix timestamps. If outside the active window, **nothing is rendered** — no DOM, no JS.

```
enabled = true
AND (start_date blank OR now >= start_date)
AND (end_date blank OR now <= end_date)
```

Both dates blank → always render (no scheduling constraint).

---

## Dismiss Logic (JavaScript)

- localStorage key: `bm-popup-{{ section.id }}`  
- On dismiss: write key with expiry timestamp  
- On page load: check key; if expired or missing → open after `delay_ms`  
- `dismiss_duration = session` → use `sessionStorage` instead  
- `dismiss_duration = permanent` → write key with no expiry (never re-show)  
- Close triggers: overlay click, ✕ button, dismiss link, `Escape` key  
- CTA click closes the popup but does NOT set dismissed (user may return to book)

---

## HTML Structure

```
.bm-pop-overlay        (fixed overlay, backdrop blur)
.bm-pop                (fixed modal, CSS grid 2-col desktop / 1-col mobile)
  button.bm-pop__close (absolute top-right)
  .bm-pop__media       (left panel — video or image)
    .bm-pop__badge     (pulsing pill badge)
  .bm-pop__body        (right panel)
    .bm-pop__eyebrow
    h2.bm-pop__title
    p.bm-pop__sub
    .bm-pop__meta      (date + location rows with inline SVG icons)
    a.bm-pop__cta      (pill button)
    button.bm-pop__dismiss
```

Layout: `grid-template-columns: 1.05fr 1fr` on desktop, single column on mobile (≤760px). Media panel collapses to `aspect-ratio: 4/3` on mobile.

---

## Animations

- Overlay: `opacity 0→1` (`0.35s ease`)  
- Modal: `opacity 0→1` + `scale(0.96)→scale(1)` + `translateY(-48%→-50%)` (`0.4–0.45s cubic-bezier(.2,.8,.2,1)`)  
- Badge dot: `@keyframes bm-pulse` gold glow ring  
- Close button: `rotate(90deg)` on hover  
- CTA arrow: `translateX(3px)` on hover  

---

## Accessibility

- `role="dialog"`, `aria-modal="true"`, `aria-labelledby="bmPopTitle-{{ section.id }}"`  
- `body { overflow: hidden }` while open  
- `Escape` key closes  
- Close button has `aria-label="Cerrar"`

---

## Colors (CSS custom properties)

```css
--bm-navy: #16254c
--bm-navy-deep: #0e1a37
--bm-cream: #f6f1e8
--bm-gold: #c9a25b
--bm-muted: #5a6273
```

Scoped to `.bm-pop` wrapper to avoid conflicts with theme globals.

---

## Files Changed

| File | Action |
|---|---|
| `sections/section__darshan-popup.liquid` | Create |
| `templates/index.json` | Add section entry |
