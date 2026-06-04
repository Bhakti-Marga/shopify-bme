# Donation Widget Redesign — Spec
Date: 2026-05-12
Reference: bhaktimarga.org/products/donate + Donation Page Brief.html

## Goal

Create a style-and-behavior copy of the donation product page that matches the bhaktimarga.org reference, without touching the existing `product.donation.*` files. The new files can be swapped in and rolled back safely.

## Files to Create

| File | Action |
|------|--------|
| `templates/product.haz-una-donacion.json` | Copy of `product.donation.json`, section type changed to `product__haz-una-donacion` |
| `sections/product__haz-una-donacion.liquid` | New section — same Liquid skeleton, new JS + CSS, schema name "Donation v2" |

**Do not touch:** `product.donation.json`, `product__donation.liquid`

## Liquid Structure (unchanged from existing section)

Keep verbatim:
- `<s-donation>` wrapper with `data-section-id`
- `{% form 'product' %}` with `id`, `novalidate`, `js-product-form`
- `<select class="sr-only" name="id" js-master-select>` — variant loop
- `.subscription-container.sr-only` block — hidden Seal `<select name="selling_plan">`
- `{%- for block in section.blocks -%}{% render block %}{%- endfor -%}` in a hidden `.seal-anchor`
- `<script type="application/json" id="ProductJSON">{{ product | json }}</script>`
- JSON-LD `<script type="application/ld+json">` block

Remove from the right column:
- Pill-style frequency toggle buttons (`donation-freq-btn`)
- 3×2 amount button grid (`donation-amounts-grid`)
- Custom amount input (`donation-custom__input`)
- Impact line (`donation-widget__impact`)

## Right Column Layout

### 1. Product title + description
Unchanged — `{{ product.title }}` and `{{ product.description }}`.

### 2. Frequency selector (custom UI → Seal hidden)
Two stacked radio `<label>` rows inside a bordered container:
- **Row 1:** "Donación única" — `data-freq="once"`
- **Row 2:** "Donación mensual recurrente" — `data-freq="monthly"`

Each row: left dot indicator (18px circle, `border 1.5px #c9c4b4`). Active row: dot filled `#16254c`, row bg `#fbf9f3`.

When monthly is active, show a disclosure line below: `↻ Detalles de la suscripción · {plan}`.

### 3. Variant stepper rows
One row per variant, generated via `{%- for variant in product.variants -%}`.

Row structure: `grid-template-columns: 1fr auto`
- Left: variant title (e.g. "10 €"), `font-weight: 600` when qty > 0
- Right: stepper — `−` button · qty counter · `+` button

Stepper buttons: 30px round, `border: 1.5px solid #c9c4b4`, hover → `border-color: #16254c`, bg `#fbf9f3`. Minus disabled (`opacity .35`) when qty = 0.

Active row (qty > 0): `background: #fbf9f3`.

### 4. Total bar + CTA
Same row, `display: flex; justify-content: space-between`.
- Left: "Importe total:" label + amount in `font-family: monospace`, `font-variant-numeric: tabular-nums`, 22px, bold.
- Right: CTA button — `background: #16254c`, `color: #fff`, `border-radius: 4px`, `padding: 15px 28px`, `text-transform: uppercase`, `letter-spacing: .12em`, `font-weight: 700`.

### 5. Trust line
`Pago seguro · Tarjeta · Apple Pay · Cancela cuando quieras` — centered, 12px, muted.

## Mobile (<768px)

- Single column stack (image above, controls below)
- Total bar + CTA row: `position: sticky; bottom: 0; background: #fff; padding: 12px 16px; border-top: 1px solid #e7e3d8` — pins to viewport bottom

## JavaScript (new IIFE, replaces DonationMain)

Single inline `<script>` at bottom of section. No external dependencies.

### State
```js
{ freq: 'once', plan: 'mensual', qtys: { [variantId]: 0, … } }
```

### Frequency toggle
- Click radio row → update `state.freq`
- If `monthly`: show sub-plan disclosure, check `subCheckbox`, dispatch `change` on it, set `subSelect` value for `state.plan`
- If `once`: hide disclosure, uncheck `subCheckbox`, dispatch `change`

### Stepper
- `+` → increment `qtys[variantId]`, update DOM, recompute total, toggle row active class
- `−` → decrement (min 0), update DOM, recompute total
- `−` disabled when qty = 0

### Total computation
```js
total = variants.reduce((sum, v) => sum + v.price * qtys[v.id], 0)
```
Format: `toLocaleString('es-ES', {minimumFractionDigits:2}) + ' €'`

### Cart submit (form `submit` event)
```js
e.preventDefault();
const items = variants
  .filter(v => qtys[v.id] > 0)
  .map(v => ({
    id: v.id,
    quantity: qtys[v.id],
    ...(state.freq === 'monthly' && sellingPlanId ? { selling_plan: sellingPlanId } : {})
  }));
if (!items.length) return; // nothing selected
POST /cart/add.js { items }
→ dispatch theme cart event (cart:open or equivalent)
```

Variant data sourced from `#ProductJSON` (already in section).

## CSS Tokens

| Token | Value |
|-------|-------|
| ink | `#16254c` |
| line | `#e7e3d8` |
| line-2 | `#ececec` |
| paper | `#fbf9f3` |
| muted | `#6b6f7a` |
| font | Avenir Next, system-ui fallback |
| mono | monospace |

All CSS scoped inside `s-donation[data-section-id="{{ section.id }}"]` to avoid leaking into existing donation section.

## Schema

```json
{ "name": "Donation v2", "blocks": [{ "type": "@app" }] }
```

## Acceptance Criteria

1. Page renders at `/products/[handle-assigned-to-new-template]`
2. Visually matches bhaktimarga.org/products/donate (minus 500€ variant)
3. Frequency toggle wires to Seal — recurring donations use correct `selling_plan`
4. Stepper adds multiple variants to cart in one POST
5. Total updates in real time
6. Mobile: single column, total/CTA sticky at bottom
7. No console errors
8. `product.donation.*` files untouched

## Out of Scope

- Custom/free amount input
- Translations
- Changes to `product.donation.*`
- Any modification to `assets/theme.css`
