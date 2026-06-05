# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Shopify Liquid theme** for Bhakti Marga España — a Spanish spiritual community association (non-profit, CIF G76198209). The store sells events, courses, donations, and products, and also provides a sangha (local chapters) directory with map, a community blog, and an event calendar.

Store: `d016j0-nz.myshopify.com` | Theme: SEED v1.0.0 | Theme ID: `183370088792`

## Development Commands

```bash
# Start local dev server (mirrors dev.ps1)
shopify theme dev --store d016j0-nz.myshopify.com

# Push to live theme (SAFE — ignores config/settings_data.json so admin-edited
# content like section photos, footer legal text, and social links is never wiped)
.\push.ps1

# Pull admin/editor changes down into the repo (run before committing settings)
shopify theme pull --store d016j0-nz.myshopify.com --theme 183370088792

# Raw push (AVOID — overwrites admin content with whatever is in local files)
# shopify theme push --store d016j0-nz.myshopify.com --theme 183370088792 --allow-live

# Validate JSON locale files
node -e "const fs=require('fs');JSON.parse(fs.readFileSync('locales/es.json','utf8'));console.log('OK')"

# Build translation comparison Excel
python build_translation_excel.py
```

## Architecture

**No build step** — pure Shopify Liquid theme. No `package.json` or npm.

### Key directories

- `sections/` (64 files) — page-level components assigned via template JSON files
- `snippets/` — reusable partials (cards, icons, drawers, filters)
- `templates/` — JSON files that wire sections to routes; custom Liquid templates for sangha map and calendar
- `locales/` — `en.default.json` is source of truth; `es.json` is the Spanish translation
- `assets/` — Bootstrap 5, theme.css/js, Swiper.js, FullCalendar libs

### Naming conventions

- Theme sections: `section__*.liquid` (e.g., `section__ticket-tier.liquid`)
- BM-custom sections: `Seccion__*.liquid` (Spanish prefix for store-specific components)
- Custom CSS classes: `BM-*` prefix

### Styling

Utility-first approach (Tailwind-like utilities from theme.css): `flex`, `px-md`, `mt-0`, `py-xxxl`, `tabletl:px-xl`. Color tokens: `bg-blue`, `text-white`, `text-gray-light`. Spacing variants use t-shirt sizing (`xs`, `sm`, `md`, `lg`, `xl`, `xxl`, `xxxl`).

### Multilingual

Spanish (`es.json`) and English (`en.default.json`). Spanish is the primary language. Both files must stay in sync — add keys to `en.default.json` first, then `es.json`.

### JavaScript integrations

- **Swiper.js** — carousels (ticket tiers, event sliders); options passed via `data-options` attribute as JSON
- **FullCalendar** — loaded only on `/calendario` route (conditional asset tag in `layout/theme.liquid`)
- **Klaviyo** — email capture (embed in `layout/theme.liquid`)
- **Fastbots** — chatbot widget (embed in `layout/theme.liquid`)

## Important Reference Files

- `needs.md` — current implementation status, launch blockers, and phased roadmap (the canonical source of what's done and what's pending)
- `darshan.md` — technical spec for the Darshan event ticketing feature (4 ticket tiers, QR integration, capacity planning)
- `admin-url-changes.md` — checklist of 21 URL slug migrations needed before launch (pages, products, blog, collections)
- `legal.md` — Spanish legal compliance requirements (RGPD, cookie banner, consent checkboxes, image rights)

## Current Project State (as of April 2026)

### Launch blockers (Phase 1)
- SEED theme upgrade — waiting on external SEED team
- Shopify Payments activation — action required by association treasurer
- Darshan event product — blocked on business decisions (capacity, pricing, refund policy)
- Legal pages (Aviso Legal, Cookies Policy) not published
- Cookie consent banner not implemented
- 21 URL slugs need migration to Spanish (see `admin-url-changes.md`)

### Darshan event (Phase 3)
Four ticket tiers (VIP, Premium, Standard, Children) displayed via `sections/section__ticket-tier.liquid`. QR code integration is pending API selection. See `darshan.md` for full spec.
