# Design: Profesores Directory — Shopify Metaobjects

**Date:** 2026-04-29
**Status:** Approved
**File affected:** `sections/section__profesores-map.liquid`

---

## Problem

Teacher data is hardcoded in a JavaScript array inside `section__profesores-map.liquid`. Adding or editing a teacher requires a code change. There is currently one entry (Govindaramandnda, Madrid).

---

## Solution

Migrate to **Shopify Metaobjects**. Each teacher becomes one Admin entry. The Liquid outputs the JS array dynamically from metaobject values. No code change is needed to add, edit, hide, or remove a teacher.

---

## Data Model

**Metaobject type key:** `profesor`
**Display name:** Profesores

| Field key | Type | Required | Notes |
|-----------|------|----------|-------|
| `name` | Single line text | Yes | Full display name |
| `city` | Single line text | Yes | e.g. "Madrid" |
| `lat` | Decimal number | Yes | Latitude — get from Google Maps right-click → "¿Qué hay aquí?" |
| `lng` | Decimal number | Yes | Longitude — same method |
| `skills` | List of single line text | Yes | Readable names: "Atma Kriya Yoga", "Om Chanting", etc. |
| `telegram_url` | URL | No | Full Telegram link |
| `photo` | File (image) | No | Headshot — rendered at 200×200px |
| `active` | True/False | Yes | False = hidden from map and cards without deleting |

Adding new fields later (bio, WhatsApp, region, languages) requires only adding a new field in Admin → no code changes.

---

## Admin Workflow

1. Shopify Admin → Content → Metaobjects → Profesores → "Add entry"
2. Fill fields → Save
3. Map and cards update on next page load — no deploy needed

**To hide a teacher without deleting:** set `active` to false.

**Migration:** The one existing hardcoded teacher (Govindaramandnda, Madrid, lat 40.4168 / lng -3.7038, skills: Atma Kriya Yoga / Meditación / Kirtan) must be re-entered manually as the first Metaobject entry before the hardcoded array is removed from the Liquid.

---

## Liquid Changes (`section__profesores-map.liquid`)

Replace the hardcoded `var profesores = [...]` block with:

```liquid
var profesores = [
  {%- for p in shop.metaobjects.profesor.values -%}
    {%- if p.active.value == true -%}
    {
      name:     {{ p.name.value | json }},
      city:     {{ p.city.value | json }},
      lat:      {{ p.lat.value }},
      lng:      {{ p.lng.value }},
      skills:   {{ p.skills.value | json }},
      telegram: {{ p.telegram_url.value | default: "" | json }},
      photo:    "{{ p.photo.value | image_url: width: 200 }}"
    }{%- unless forloop.last -%},{%- endunless -%}
    {%- endif -%}
  {%- endfor -%}
];
```

Everything else in the section (Leaflet map init, marker rendering, popup HTML, card rendering) is unchanged — it already reads from the `profesores` array.

---

## URL Skill Filter

Practice pages can link to `/pages/profesores?practica=atma-kriya-yoga` to arrive pre-filtered.

Add this JS block immediately after the `profesores` array definition, before any rendering:

```js
var params = new URLSearchParams(window.location.search);
var filtro = params.get('practica');

if (filtro) {
  profesores = profesores.filter(function(p) {
    return p.skills.some(function(s) {
      return s.toLowerCase().replace(/\s+/g, '-') === filtro;
    });
  });
}
```

**Slug mapping (automatic):** Admin stores readable names ("Atma Kriya Yoga"). JS converts to slug on the fly for comparison. Admin never enters slugs.

| Admin value | URL param |
|-------------|-----------|
| Atma Kriya Yoga | `atma-kriya-yoga` |
| Om Chanting | `om-chanting` |
| Babaji Surya Namaskar | `babaji-surya-namaskar` |
| Meditación | `meditacion` |
| Kirtan | `kirtan` |

---

## Out of Scope

- Sangha map migration (same pattern, separate task)
- Self-service teacher registration form
- Teacher profile pages (detail page per teacher)
