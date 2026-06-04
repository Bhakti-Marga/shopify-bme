# Donation Widget Redesign — Spec

**Date:** 2026-05-10  
**Status:** Approved

## Goal

Replace the generic Shopify product layout on the donation page with a purpose-built donation widget that lets users pick frequency (once/monthly), plan (4 Seal plans), and amount (preset grid or custom via Infinite Options).

## Acceptance Criteria

| Scenario | Expected result |
|---|---|
| Select preset amount + Una vez | Adds correct variant to cart, one-time |
| Select preset amount + Mensual | Adds correct variant to cart, Seal subscription (mensual plan) |
| Select preset amount + Trimestral | Adds correct variant, Seal trimestral plan |
| Select preset amount + Semestral | Adds correct variant, Seal semestral plan |
| Select preset amount + Anual | Adds correct variant, Seal anual plan |
| Type custom amount + Una vez | IO captures amount as line item property, one-time |
| Type custom amount while Mensual active | Widget auto-switches to Una vez, IO captures amount |
| Submit with no amount selected | Does not submit (first preset auto-selected on load) |
| Re-submit donation | Cart dedup script removes existing donation first |

## UI Layout

```
[ product images carousel — unchanged ]   [ title                          ]
                                           [ description                    ]
                                           [ ┌─ Una vez ─┐┌─ Mensual ─┐   ]
                                           [ └───────────┘└────────────┘   ]
                                           [ (plan grid — visible if Mensual)]
                                           [ [ Mensual ] [ Trimestral ]     ]
                                           [ [ Semestral] [ Anual     ]     ]
                                           [ ┌──────┐ ┌──────┐ ┌──────┐   ]
                                           [ │  5€  │ │ 10€  │ │ 20€  │   ]
                                           [ └──────┘ └──────┘ └──────┘   ]
                                           [ (more rows as variants exist)  ]
                                           [ ┌─ € ──────────────────────┐  ]
                                           [ │  Otra cantidad            │  ]
                                           [ └──────────────────────────┘  ]
                                           [ Tu donación de X€ ayuda...    ]
                                           [ [      DONAR AHORA       ]    ]
                                           [ Pago seguro · Cancelar...      ]
```

## Architecture

**Approach: Full overlay widget (Option A)**  
New `<div class="donation-widget">` overlays the native Shopify form. The form skeleton (`{% form 'product' %}`) and native inputs (master variant select, quantity) stay in the DOM but are visually hidden. Widget drives them programmatically. Cart dedup script untouched.

**Seal integration:** Seal block rendered inside a `display:none` wrapper (`#SealAnchor`). JS discovers Seal's radio inputs at runtime by matching label text to plan names (mensual/trimestral/semestral/anual), then clicks them programmatically.

**Infinite Options integration:** IO block re-enabled in `product.donation.json`. IO renders `#infiniteoptions-container` hidden below the widget. Custom amount input mirrors into IO's text input via JS. `display:none` applied to IO container via CSS.

**Custom amount + monthly:** When a user types a custom amount while Mensual is active, JS auto-switches frequency to Una vez. Custom amounts are one-time only.

## Design Tokens

- Ink: `#16254c` (bg-blue)
- Gold: `#d6bf90` (btn--gold)
- Gold hover: `#e8dbc0`
- Line: `#e7e3d8`
- Spacing: theme t-shirt sizing (py-sm, py-md, gap-sm, gap-md)
- Border radius: `0.5rem` (rounded-sm) for cards, pill for frequency toggle

## Files Changed

| File | Change |
|---|---|
| `sections/product__donation.liquid` | Rewrite right column; keep images, form skeleton, ProductJSON, LD+JSON, cart dedup script |
| `templates/product.donation.json` | Set `"disabled": false` on `infinite_options_app_block_jMJTmD` |

## Out of Scope

- Changing Seal plan configuration in Seal admin
- Changing Infinite Options field configuration in IO admin
- Sticky mobile CTA (deferred)
- Impact line with dynamic per-variant copy (static message acceptable)
