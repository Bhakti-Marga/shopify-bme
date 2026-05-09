# Darshan Popup — Implementation Plan

**Spec:** `docs/superpowers/specs/2026-05-07-darshan-popup-design.md`  
**Date:** 2026-05-07

---

## Tasks

### Task 1: Create `sections/section__darshan-popup.liquid`

Full Liquid section with:
- Server-side scheduling gate (Liquid date comparison)
- HTML structure matching the spec
- CSS scoped to `.bm-pop` prefix (no external dependencies)
- JS dismiss logic with configurable duration
- Schema with all settings groups: Visibilidad, Media, Contenido

### Task 2: Add section to `templates/index.json`

Insert a new entry in `sections` and append its key to `order`. Section is disabled by default (merchant enables it in admin).

### Task 3: Start dev server and verify

Run `shopify theme dev --store d016j0-nz.myshopify.com` and confirm the homepage loads without errors.
