# needs.md — BhaktiMarga España Shopify Store

> Status audit: 2026-04-18
> Theme: SEED v1.0.0 — d016j0-nz.myshopify.com
> Entity: Asociación Bhakti Marga España — CIF G76198209
> Based on: darshan.md · legal.md · admin-url-changes.md · snippets and translation.md · theme audit

---

## Phase 1 — Launch Blockers
*Nothing can go live until these are resolved.*

### 1.1 External — Message to SEED Team

> Jai Gurudev, the help we would like:
>
> - Upgrade our store to the latest version of the SEED theme
> - Set up the Darshan event page for Lanzarote — this logic is already done in SPN (with data privacy checkboxes, registration flow, etc.), we need it applied here
> - Help configuring the Darshan registration form
> - The donation form is already done in SPN — we need the same here

### 1.2 Payments
| # | Item | Owner | Status |
|---|------|-------|--------|
| 5 | Verify Shopify Payments is active on the live store | Treasurer | darshan.md says not activated — live store may differ. Needs manual check in Shopify Admin → Settings → Payments |
| 6 | If not active: provide legal entity name, Spanish IBAN, and ID to Shopify | Treasurer | Blocked on #5 |

### 1.3 Legal (required before any paid ticket sale — Spanish law)
| # | Item | Location |
|---|------|---------|
| 7 | Cookie consent banner — blocks Klaviyo and Fastbots until user accepts | `layout/theme.liquid` lines 80 and 127 |
| 8 | "I accept Terms of Service" checkbox in cart before checkout | `sections/cart__main.liquid` — currently absent |
| 9 | Aviso Legal page published and linked in subfooter | Shopify Admin → Pages + Navigation → seed-subfooter |
| 10 | Cookie Policy page created and linked in subfooter | Shopify Admin → Pages + Navigation → seed-subfooter |
| 11 | Privacy Policy updated: third-party processors (Klaviyo, Fastbots, Formful) + event data | Shopify Admin → Settings → Policies |
| 12 | Terms of Service covering: ticket sales, refund/cancellation policy, image rights | Shopify Admin → Settings → Policies |
| 13 | Cancellation/refund policy displayed on each event product page | `sections/product__main.liquid`, `sections/main-product-event-formulario.liquid` |
| 14 | Formful form: add data processing notice (RGPD Art. 13) + image consent checkbox | Formful app dashboard |

---

## Phase 2 — Pre-Launch
*Complete before removing the store password.*

### 2.1 URL Slug Changes (0 of ~21 done)
All changes must be made in Shopify Admin with redirect enabled. Full instructions in `admin-url-changes.md`.

**Pages (12):**
give → dona · all-programs → todos-los-programas · bhakti-sundays → domingos-bhakti · calendar → calendario · communities → comunidades · contact → contacto · help-center → ayuda · om-chanting → canto-om · project-mantra → proyecto-mantra · request-a-course → solicitar-curso · start-now → empieza-ahora · vedic-chanting → canto-vedico

**Products (1):** make-a-donation → hacer-una-donacion

**Blog (1):** events → eventos

**Articles (7):**
guruji-birthday → cumpleanos-guruji · main-event-template → plantilla-evento · meditation-essentials → esenciales-meditacion · online-darshan → darshan-online · temple-anniversary → aniversario-templo · yogic-philosophy → filosofia-yoguica · 4-days-to-soul-awakening-with-paramahamsa-vishwananda → 4-dias-despertar-del-alma-con-paramahamsa-vishwananda

**Collections (1):** events → eventos

### 2.2 Translation Gaps in `locales/es.json`
If the SEED upgrade (Phase 1, #1) does not resolve these, they must be added manually.
Current state: 125 ES keys vs 266 EN keys — 142 missing.

| Namespace | Keys missing | Visible impact |
|-----------|-------------|----------------|
| `customer.*` | ~60 | Entire account area in English: login, register, account dashboard, order history, addresses |
| `products.product.*` | ~15 | Media labels, quantity +/− buttons, price display, vendor label |
| `sections.cart.*` | 5 | Cart subtotal label, taxes and shipping text |
| `accessibility.*` | 3 | Skip-to-content, error message, refresh page |
| `blogs.article.*` | 2 | Blog section labels |
| `date_formats.*` | 1 | Month/year format |

### 2.3 Payment Confirmation Flow
| # | Item | Notes |
|---|------|-------|
| 15 | Order confirmation email template verified in Spanish | Shopify Admin → Settings → Notifications — check and update if in English |
| 16 | Full checkout test: select tier → add to cart → checkout → pay → receive confirmation email | No theme code change required — Shopify native flow |

---

## Phase 3 — Darshan Event Operations
*Specific to the November Lanzarote event. Can run in parallel with Phase 2 once business decisions are resolved.*

### 3.1 Pending Business Decisions (blocking the Phase 3 build)
| # | Decision needed | Owner |
|---|----------------|-------|
| D1 | Total venue capacity | @Anushadasi / @Sumanglidasi — post-Easter confirmation |
| D2 | Official event name (must frame as "fiesta": music, activities, food, blessing) | Event team |
| D3 | Hotel food service: confirmed or not? | Event team |
| D4 | Do children (free) need a ticket issued for headcount purposes? | Event team |
| D5 | Purchase channel: online only, or also bank transfer / in-person sales? | Event team |
| D6 | Cancellation/refund policy: deadline, full/partial/none? | Legal + event team |
| D7 | Which QR app/API will be used? | Tech team |

### 3.2 QR Integration (blocked on D7)
| # | Item |
|---|------|
| 17 | Connect Shopify orders to QR API via webhook or Shopify Admin API |
| 18 | Test QR code generation and email delivery to buyer (one QR per order) |
| 19 | Test QR scan validation at venue entrance using the chosen scanner app |

---

## Phase 4 — Post-Launch / Improvements
*Not blocking go-live. Address after the first event.*

| # | Item | Notes |
|---|------|-------|
| 20 | Image/recording rights consent checkbox | Separate optional checkbox on Formful form — required by Ley Orgánica 1/1982; cannot be bundled with ticket purchase consent |
| 21 | VAT breakdown on event prices | Confirm applicable VAT rate with legal for spiritual/educational activities; currently `{{ current_variant.price | money }}` shows no VAT info |
| 22 | Minor/guardian consent flow | Only needed if under-14 attendees are confirmed |
| 23 | Data Processing Agreements signed with Shopify, Klaviyo, and Formful | RGPD Art. 28 — admin task, no code changes |
| 24 | Remove store password | Final go-live step — only after all Phase 1 and Phase 2 items are complete |

---

## Dependency Map

```
SEED upgrade (#1) ──────────────────────→ Translation gaps (2.2) likely resolved
SEED event product (#2) ───────────────→ Darshan form (#3) → QR integration (#17-19)
Payments verified (#5) ─────────────────→ Paid ticket sales enabled
Legal items (#7-14) ────────────────────→ Store password removal (#24)
URL slugs (2.1) ────────────────────────→ No broken links at go-live
Business decisions (D1-D7) ────────────→ Phase 3 build unblocked
```

---

*Generated: 2026-04-18*
