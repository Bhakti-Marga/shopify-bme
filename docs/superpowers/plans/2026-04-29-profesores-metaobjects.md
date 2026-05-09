# Profesores Directory — Metaobjects Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the hardcoded JS teacher array in `section__profesores-map.liquid` with Shopify Metaobjects so teachers can be added, edited, and hidden from Admin without code changes.

**Architecture:** A `profesor` Metaobject type is defined once in Admin. Each teacher is one entry. The Liquid section loops over `shop.metaobjects.profesor.values` and outputs the JS array dynamically. A URL param (`?practica=slug`) filters the rendered list client-side.

**Tech Stack:** Shopify Liquid, Shopify Metaobjects, Leaflet.js (already loaded), vanilla JS.

---

## Task 1: Create Metaobject definition in Shopify Admin

> This is a manual Admin step — no code. Do this before touching any files.

**Files:** none

- [ ] **Step 1: Open Metaobjects in Admin**

  Go to: Shopify Admin → Content → Metaobjects → click "Add definition"

- [ ] **Step 2: Set type name and key**

  - Display name: `Profesores`
  - API key (auto-generated, verify it reads): `profesor`

- [ ] **Step 3: Add field — name**

  Click "Add field" → Single line text
  - Name: `Name` → key auto-fills `name`
  - Check "Required"
  - Save field

- [ ] **Step 4: Add field — city**

  Click "Add field" → Single line text
  - Name: `City` → key: `city`
  - Check "Required"
  - Save field

- [ ] **Step 5: Add field — lat**

  Click "Add field" → Decimal number
  - Name: `Lat` → key: `lat`
  - Check "Required"
  - Helper text: "Latitud. Obtén en Google Maps: clic derecho → ¿Qué hay aquí?"
  - Save field

- [ ] **Step 6: Add field — lng**

  Click "Add field" → Decimal number
  - Name: `Lng` → key: `lng`
  - Check "Required"
  - Helper text: "Longitud. Segundo número en Google Maps: clic derecho → ¿Qué hay aquí?"
  - Save field

- [ ] **Step 7: Add field — skills**

  Click "Add field" → List of single line text
  - Name: `Skills` → key: `skills`
  - Check "Required"
  - Helper text: "Prácticas que enseña. Ej: Atma Kriya Yoga, Om Chanting, Kirtan"
  - Save field

- [ ] **Step 8: Add field — telegram_url**

  Click "Add field" → URL
  - Name: `Telegram URL` → key: `telegram_url`
  - Leave optional
  - Save field

- [ ] **Step 9: Add field — photo**

  Click "Add field" → File → Images only
  - Name: `Photo` → key: `photo`
  - Leave optional
  - Save field

- [ ] **Step 10: Add field — active**

  Click "Add field" → True/False (Boolean)
  - Name: `Active` → key: `active`
  - Default value: `true`
  - Check "Required"
  - Helper text: "Desactivar para ocultar al profesor sin eliminar el registro"
  - Save field

- [ ] **Step 11: Save the definition**

  Click "Save" on the definition page. Verify the definition now appears in Admin → Content → Metaobjects → Profesores.

---

## Task 2: Enter the existing teacher as first Metaobject entry

> Migrate the one hardcoded teacher before changing any code.

**Files:** none

- [ ] **Step 1: Add entry**

  Admin → Content → Metaobjects → Profesores → "Add entry"

- [ ] **Step 2: Fill in all fields**

  | Field | Value |
  |-------|-------|
  | Name | `Govindaramandnda` |
  | City | `Madrid` |
  | Lat | `40.4168` |
  | Lng | `-3.7038` |
  | Skills | `Atma Kriya Yoga` · `Meditación` · `Kirtan` (add each as separate list item) |
  | Telegram URL | `https://t.me/` (or leave blank if no real link yet) |
  | Photo | Leave blank for now — can upload later from Admin |
  | Active | `true` |

- [ ] **Step 3: Save**

  Click "Save". Verify the entry appears in the Profesores list.

---

## Task 3: Replace hardcoded array with Liquid + add URL filter

**Files:**
- Modify: `sections/section__profesores-map.liquid` (lines 199–208 — the `var profesores = [...]` block)

- [ ] **Step 1: Start dev server to establish baseline**

  ```bash
  shopify theme dev --store d016j0-nz.myshopify.com
  ```

  Open `http://127.0.0.1:9292/pages/profesores`. Verify the map and cards render with the hardcoded teacher. This is the baseline to compare against after the change.

- [ ] **Step 2: Replace the hardcoded profesores array**

  In `sections/section__profesores-map.liquid`, find and replace this block (lines ~199–208):

  ```js
  var profesores = [
    {
      name: 'Govindaramandnda',
      city: 'Madrid',
      lat: 40.4168,
      lng: -3.7038,
      skills: ['Atma Kriya Yoga', 'Meditación', 'Kirtan'],
      telegram: 'https://t.me/'
    }
  ];
  ```

  Replace with:

  ```liquid
  var profesores = [
    {%- assign is_first = true -%}
    {%- for p in shop.metaobjects.profesor.values -%}
      {%- if p.active.value == true -%}
        {%- unless is_first -%},{%- endunless -%}
        {
          name:     {{ p.name.value | json }},
          city:     {{ p.city.value | json }},
          lat:      {{ p.lat.value }},
          lng:      {{ p.lng.value }},
          skills:   {{ p.skills.value | json }},
          telegram: {{ p.telegram_url.value | default: "" | json }},
          photo:    "{{ p.photo.value | image_url: width: 200 }}"
        }
        {%- assign is_first = false -%}
      {%- endif -%}
    {%- endfor -%}
  ];
  ```

  > The `is_first` flag puts commas *before* each entry after the first. This correctly handles inactive entries being skipped — no trailing comma bug.

- [ ] **Step 3: Add URL filter immediately after the array**

  After the closing `];` of the profesores array and before the `profesores.forEach` map rendering, add:

  ```js
  function skillToSlug(str) {
    return str.toLowerCase()
      .replace(/[áàä]/g, 'a').replace(/[éèë]/g, 'e')
      .replace(/[íìï]/g, 'i').replace(/[óòö]/g, 'o')
      .replace(/[úùüû]/g, 'u').replace(/ñ/g, 'n')
      .replace(/\s+/g, '-');
  }

  var params = new URLSearchParams(window.location.search);
  var filtro = params.get('practica');
  if (filtro) {
    profesores = profesores.filter(function(p) {
      return p.skills.some(function(s) {
        return skillToSlug(s) === filtro;
      });
    });
  }
  ```

  > `normalize('NFD')` + stripping combining marks removes accents before slugifying, so "Meditación" → "meditacion" and matches `?practica=meditacion` correctly.

- [ ] **Step 4: Update card avatar to show photo when available**

  Find the card rendering block (in the `profesores.forEach` near the bottom). Find this line:

  ```js
  + '<div class="pmap__card-avatar">🙏</div>'
  ```

  Replace with:

  ```js
  + '<div class="pmap__card-avatar">' + (p.photo ? '<img src="' + p.photo + '" alt="' + p.name + '">' : '🙏') + '</div>'
  ```

- [ ] **Step 5: Verify — map and cards render from Metaobject**

  With the dev server still running, hard-refresh `http://127.0.0.1:9292/pages/profesores`.

  Check:
  - Map pin appears in Madrid ✓
  - Clicking the pin shows the popup with name, city, skills ✓
  - Teacher card appears below the map ✓
  - Card shows 🙏 (no photo uploaded yet — expected) ✓

- [ ] **Step 6: Verify — URL filter works**

  Open `http://127.0.0.1:9292/pages/profesores?practica=atma-kriya-yoga`

  Expected: the Madrid teacher appears (has "Atma Kriya Yoga" in skills) ✓

  Open `http://127.0.0.1:9292/pages/profesores?practica=om-chanting`

  Expected: empty map, no cards (teacher doesn't have Om Chanting) ✓

- [ ] **Step 7: Verify — active toggle works**

  In Admin → Content → Metaobjects → Profesores → edit entry → set `Active` to `false` → Save.

  Hard-refresh the dev preview. Expected: no pin, no card.

  Set `Active` back to `true` → Save. Refresh. Expected: pin and card return ✓

- [ ] **Step 8: Commit**

  ```bash
  git add sections/section__profesores-map.liquid
  git commit -m "feat: migrate profesores directory to Shopify Metaobjects"
  ```

---

## Task 4: Update figma-to-shopify.md

**Files:**
- Modify: `figma-to-shopify.md`

- [ ] **Step 1: Mark Fase 7 as complete**

  In `figma-to-shopify.md`, find the Fase 7 section and update it:

  Change heading from:
  ```
  ### Fase 7 — Migrar directorios a Metaobjects (profesores + sanghas)
  ```
  To:
  ```
  ### Fase 7 — Migrar directorios a Metaobjects ✅ Profesores completado (2026-04-29) | Sanghas pendiente
  ```

  Mark profesores tasks as done:
  ```markdown
  - [x] Crear definición de Metaobject `profesor` en Admin
  - [x] Actualizar `section__profesores-map.liquid`: reemplazar array hardcodeado por loop Liquid
  - [x] Añadir filtro URL `?practica=slug`
  - [x] Migrar datos del profesor existente a Admin
  - [ ] Crear definición de Metaobject `sangha` en Admin (pendiente)
  - [ ] Actualizar el mapa de sanghas con el mismo patrón (pendiente)
  - [ ] Migrar los datos existentes de sanghas a Admin (pendiente)
  ```

- [ ] **Step 2: Commit**

  ```bash
  git add figma-to-shopify.md
  git commit -m "docs: mark profesores metaobjects migration as complete"
  ```

---

## Notes

- **Pushing to live:** Do NOT push to the live theme without asking the user first. The dev server is sufficient to verify all tasks.
- **Sangha migration:** Out of scope for this plan — same pattern applies when ready.
- **Photo upload:** Admins can upload photos at any time from Admin → Content → Metaobjects → Profesores → edit entry → Photo field.
