# Legal Compliance Analysis — BhaktiMarga España Shopify Store

> **Purpose:** Pre-meeting analysis to support legal review before selling event tickets online.  
> **Store:** d016j0-nz.myshopify.com — SEED theme (v1.0.0)  
> **Entity:** Asociación Bhakti Marga España — CIF G76198209  
> **Address:** Calle Pablo Picasso, 11 — 29719 Benamocarra (Málaga)  
> **Applicable law:** Spain / European Union

---

## 1. Where Legal Text Lives in This Theme

### 1.1 Footer Navigation (subfooter)
**File:** `sections/footer.liquid` + `config/settings_data.json`

The footer has two navigation zones powered by Shopify linklists:
- **`seed-footer`** — main footer columns (content pages, programs, etc.)
- **`seed-subfooter`** — bottom bar. **This is where legal links must go** (Privacy Policy, Terms of Service, Cookie Policy, Legal Notice, etc.)

To view or edit these links:
> Shopify Admin → Online Store → Navigation → find "seed-subfooter" → edit links

The footer also hardcodes the association identity in `config/settings_data.json`:
```
Asociación BHAKTI MARGA ESPAÑA — CIF G76198209
Calle Pablo Picasso, 11 — 29719 Benamocarra (Málaga)
Email: spain@bhaktimarga.es
Copyright line: "Todos los derechos reservados" (hardcoded in footer.liquid:59)
```

### 1.2 Shopify Policy Pages (outside theme code)
Shopify stores actual legal texts as **store policies**, managed at:
> **Shopify Admin → Settings → Policies**

These generate automatic pages at standard URLs:
- `/policies/privacy-policy`
- `/policies/terms-of-service`
- `/policies/refund-policy`
- `/policies/shipping-policy`

These pages exist only in Shopify admin — **not** in local theme files. The footer links to them via the subfooter navigation.

### 1.3 Cart (`sections/cart__main.liquid`, `snippets/cart.liquid`)
The only legally relevant text present is:
> *"Impuestos y envío calculados al finalizar la compra"*  
> (Taxes and shipping calculated at checkout)

**What is absent:** no legal acceptance checkbox, no link to Terms of Service before the user proceeds to checkout.

### 1.4 Event Product Pages
Three event templates exist in the theme:

| Template file | Section used | Notes |
|---|---|---|
| `templates/product.event.json` | `sections/product__main.liquid` | Standard product layout with event metafields |
| `templates/product.evento.formulario.json` | `sections/main-product-event-formulario.liquid` | Event with Formful app registration form embedded |
| `templates/product.evento-una-localizacion.json` | (product main) | Single-location event variant |

Neither template contains a consent checkbox, cancellation notice, or link to terms in the code. Any consent inside the Formful registration form depends entirely on how that form is configured in the Formful app dashboard.

### 1.5 Global Layout (`layout/theme.liquid`)
- **No cookie consent banner** anywhere in the code
- **No GDPR/RGPD scripts** or consent management platform
- **Klaviyo** (email marketing tracker) is loaded unconditionally on every page — line 80:
  ```html
  <script async src="https://static.klaviyo.com/onsite/js/SQJQY5/klaviyo.js?company_id=SQJQY5"></script>
  ```
- **Fastbots.ai** (AI chatbot) is loaded unconditionally on every page — line 127:
  ```html
  <script defer src="https://app.fastbots.ai/embed.js" data-bot-id="cmmnygabi00hfp824bm11g3g0"></script>
  ```
Both tools process user data without any prior consent mechanism in place.

---

## 2. Compliance Gaps Found

| # | Gap | Where in code | Legal risk |
|---|-----|---------------|-----------|
| 1 | No cookie consent banner | `layout/theme.liquid` | LSSI-CE Art. 22.2 + RGPD — AEPD fines up to €20M |
| 2 | Klaviyo loads before consent | `layout/theme.liquid:80` | RGPD Art. 5 & 7 — tracking without consent |
| 3 | Fastbots chatbot loads before consent | `layout/theme.liquid:127` | RGPD — third-party data processor without consent |
| 4 | No "I accept Terms" checkbox before checkout | `sections/cart__main.liquid` | RDL 1/2007 Art. 97 — consumer must confirm terms |
| 5 | No cancellation/refund policy on event pages | `sections/product__main.liquid`, `main-product-event-formulario.liquid` | Ley 34/2002 Art. 27 — must inform before purchase |
| 6 | No data consent on event registration form | Formful app (not in code) | RGPD Art. 7 — consent must be explicit and granular |
| 7 | No age restriction notice or minor consent | All event templates | LOPDGDD Art. 7 — age verification for data processing |
| 8 | No image/recording rights notice | No file | Ley Orgánica 1/1982 — requires explicit consent |
| 9 | No Aviso Legal page verifiable from code | Footer nav (not verifiable locally) | LSSI-CE Art. 10 — mandatory legal notice page |
| 10 | No VAT/tax breakdown on event price | `sections/product__main.liquid:74` | RDL 1/2007 — price must show whether VAT is included |

---

## 3. Data Flows Identified (Third-Party Tools)

| Tool | Where loaded | Data collected | Consent mechanism |
|------|-------------|----------------|-------------------|
| **Klaviyo** | Every page (theme.liquid:80) | Browsing behavior, email, purchases | None |
| **Fastbots.ai** | Every page (theme.liquid:127) | Chat messages, session data | None |
| **Formful** | Event registration pages only | Name, email, and any custom fields | Configurable inside app |
| **Shopify Payments** | Checkout (Shopify-managed) | Payment + billing data | Shopify's own consent |
| **Shopify** (platform) | Entire store | All user and transaction data | Shopify DPA with merchant |

---

## 4. Event-Specific Architecture

The event purchase flow works as follows:

1. User lands on event page (product template)
2. Event info shown via metafields: `event.date_time`, `event.teacher`, `event.location`, `event.type`
3. Ticket tiers optionally shown via `sections/section__ticket-tier.liquid` (separate section)
4. Purchase goes through standard Shopify cart → Shopify checkout
5. For events with registration form: Formful app block renders inside the event sidebar (`main-product-event-formulario.liquid:172-178`)
6. Payment is processed by Shopify — the store does NOT handle payment card data directly

The **Formful app** is key: it sits between the event page and purchase, collecting attendee data. Its legal configuration (consent checkboxes, data processing notices) is entirely managed in the Formful dashboard, not in any theme file.

---

## 5. Questions for Legal

### 5.1 Data Protection (RGPD / LOPDGDD)

1. **Who is the Data Controller?** Is it Asociación Bhakti Marga España (CIF G76198209) alone, or is there joint controllership with Bhakti Marga International (Germany/India)? This determines who signs the privacy policy and who is liable.

2. **What is the legal basis for processing attendee data?** Options: performance of a contract (ticket purchase), legitimate interest, or explicit consent. The answer determines what text must appear in the registration form and privacy policy.

3. **What data is collected in the Formful registration form and for how long is it retained?** RGPD Art. 13 requires informing users at the point of collection about: purpose, retention period, their rights, and the identity of the controller.

4. **Is attendee data shared with any third parties?** e.g. Klaviyo, Fastbots, Shopify, event teachers. If data is transferred internationally (to BM International in Germany/India), what legal mechanism is used (Standard Contractual Clauses, adequacy decision)?

5. **Does the association have a Record of Processing Activities (RoPA)?** Mandatory under RGPD Art. 30 for organizations processing personal data.

6. **Has a Data Processing Agreement (DPA) been signed with Shopify, Klaviyo, and Formful?** All three act as data processors. DPAs are required under RGPD Art. 28.

### 5.2 Cookie Consent

7. **Klaviyo and Fastbots load on every page before any user consent.** Legal needs to confirm: are these classified as strictly necessary (exempt from consent), or do they require prior opt-in? If opt-in is required, a consent management platform (cookie banner) must be implemented before the store goes public.

8. **Is there an approved Cookie Policy?** If not, one must be created before launch — especially before any paid event goes live.

### 5.3 Event Ticket Sales / Consumer Rights

9. **What is the cancellation and refund policy for events?** Spanish consumer law (RDL 1/2007) and Ley 34/2002 require that this information be clearly displayed **before** the user confirms a purchase. If the event falls under the "leisure activities at a specific date" exemption, the 14-day withdrawal right may not apply — but this must be stated explicitly and legal must confirm whether the exemption applies here.

10. **What happens if the event is cancelled or postponed by the organisation?** A clause covering full refund, credit, or access to an online alternative must be drafted and displayed on the event page and in the Terms of Service.

11. **Are tickets nominal (tied to a specific person)?** If so, the Terms must state whether transfers to another attendee are allowed or not.

12. **Does the displayed price include VAT?** Spanish law requires the final price shown to consumers to include all taxes. The code currently shows `{{ current_variant.price | money }}` with no VAT breakdown or inclusion note. Legal must confirm the applicable VAT rate for spiritual retreat/educational activities.

### 5.4 Event Activities & Participant Safety

13. **Is there an age restriction for the event?** LOPDGDD Art. 7 sets 14 as the minimum age for processing personal data with own consent in Spain. If minors may attend, parental/guardian authorization is required — this must be in the registration form.

14. **Does the event include physical activities** (Atma Kriya Yoga, Babaji Surya Namaskar, meditation, etc.)? If so, does legal require a health declaration or liability waiver from attendees? This would need to be added to the Formful form.

15. **Will the event be photographed or recorded?** Attendees must give explicit, separately obtained consent for use of their image (Ley Orgánica 1/1982). This consent cannot be bundled with the ticket purchase consent — it must be a separate, optional checkbox.

### 5.5 Legal Notice (Aviso Legal — LSSI-CE)

16. **Is the Aviso Legal page published and accessible from all pages?** LSSI-CE Art. 10 requires the following to be permanently and easily accessible: legal name, registered address, CIF/NIF, registration details (Registro de Asociaciones), and a contact email. The footer currently shows address and CIF — but there must also be a full Aviso Legal page reachable via the subfooter navigation.

17. **What is the association's registration number in the Registro Nacional de Asociaciones or regional equivalent?** This must appear in the Aviso Legal.

---

## 6. Recommended Pre-Launch Actions

Before selling any event ticket online, the following should be in place:

- [ ] Cookie consent banner implemented (blocks Klaviyo + Fastbots until user accepts)
- [ ] Cookie Policy page created and linked in footer
- [ ] Privacy Policy updated to reflect all third-party processors and event data collection
- [ ] Terms of Service page covering: ticket sales, refund/cancellation policy, image rights, physical activity disclaimer
- [ ] Aviso Legal page published with all LSSI-CE Art. 10 required fields
- [ ] "I accept the Terms of Service" checkbox added to cart before checkout
- [ ] Cancellation/refund policy displayed on each event product page
- [ ] Formful form updated with: data processing notice (Art. 13), separate image consent checkbox, age verification field
- [ ] DPAs signed with Shopify, Klaviyo, and Formful
- [ ] VAT inclusion confirmed and displayed on all product prices
- [ ] Minor/guardian consent process defined if under-14s may attend
