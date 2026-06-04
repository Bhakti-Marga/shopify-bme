# Donation Widget Redesign — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the generic product layout on the donation page with a purpose-built donation widget: frequency toggle (Una vez / Mensual), 4 Seal plan cards, preset amount grid, custom amount via Infinite Options, and a gold CTA button.

**Architecture:** Option A — overlay widget. The native Shopify `{% form 'product' %}` skeleton stays intact. A new `<div class="donation-widget">` replaces the visible UI and drives native inputs programmatically. Seal block hidden in `#SealAnchor`, driven by clicking its radio inputs. IO block re-enabled for custom amount capture.

**Tech Stack:** Shopify Liquid, vanilla JavaScript (ES5-compatible for Shopify), CSS utility classes from theme.css, Seal Subscriptions app block, Infinite Options app block.

**Spec:** `docs/superpowers/specs/2026-05-10-donation-widget-redesign.md`

---

## File Map

| File | Action | What changes |
|---|---|---|
| `sections/product__donation.liquid` | Modify | Rewrite right column (`product__information` div); preserve images, form skeleton, ProductJSON script, LD+JSON script, cart dedup script |
| `templates/product.donation.json` | Modify | Change `"disabled": true` → `"disabled": false` on `infinite_options_app_block_jMJTmD` |

---

## Task 1: Re-enable Infinite Options block

**Files:**
- Modify: `templates/product.donation.json`

- [ ] **Step 1: Open the file and find the IO block**

Read `templates/product.donation.json`. Locate the block with key `infinite_options_app_block_jMJTmD`. It currently reads:
```json
"infinite_options_app_block_jMJTmD": {
  "type": "shopify://apps/infinite-options/blocks/app-block/7e73b6f9-82b0-45f5-9b9b-04f446ba1a9b",
  "disabled": true,
  "settings": {}
},
```

- [ ] **Step 2: Set disabled to false**

Change `"disabled": true` to `"disabled": false`:
```json
"infinite_options_app_block_jMJTmD": {
  "type": "shopify://apps/infinite-options/blocks/app-block/7e73b6f9-82b0-45f5-9b9b-04f446ba1a9b",
  "disabled": false,
  "settings": {}
},
```

- [ ] **Step 3: Verify JSON is valid**

Run:
```bash
node -e "const fs=require('fs');JSON.parse(fs.readFileSync('templates/product.donation.json','utf8'));console.log('OK')"
```
Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add templates/product.donation.json
git commit -m "feat: re-enable Infinite Options block on donation product"
```

---

## Task 2: Rewrite the right column — HTML structure

**Files:**
- Modify: `sections/product__donation.liquid` (lines 68–159, the `product__information` div)

The complete new `sections/product__donation.liquid` file follows. Keep everything outside the `product__information` div unchanged (lines 1–67 images, lines 163+ ProductJSON/LD+JSON/cart-dedup script). Only replace the right column.

- [ ] **Step 1: Locate the right column boundaries**

The right column starts at:
```liquid
<div class="product__information h-[min-content] py-lg tabletl:py-xl tabletl:px-xxl tabletl:sticky tabletl:top-[var(--header-height)]" id="ProductInfo-{{ section.id }}">
```
and ends at the matching `</div><!-- .product__images-container -->` on the line before `</div><!-- .product__layout -->`.

- [ ] **Step 2: Replace the right column with the donation widget**

Replace the entire `product__information` div (and its contents including the `{%- form ... -%}` block) with:

```liquid
    <div class="product__information h-[min-content] py-lg tabletl:py-xl tabletl:px-xxl tabletl:sticky tabletl:top-[var(--header-height)]" id="ProductInfo-{{ section.id }}">
      {%- form 'product', product, id: product_form_id, class: 'form', novalidate: 'novalidate', js-product-form: true -%}

        {%- comment -%} Hidden native variant select — driven by widget JS {%- endcomment -%}
        {% render 'master-variant-select',
          variants: product.variants,
          id: master_select_id,
          current_variant: current_variant,
          display: 'hidden'
        %}
        <input type="hidden" name="quantity" value="1">

        {%- comment -%} Expose variant data + "Otro" variant id for JS {%- endcomment -%}
        {%- assign otro_variant_id = '' -%}
        {%- for variant in product.variants -%}
          {%- assign vtitle = variant.title | downcase -%}
          {%- if vtitle == 'otro' or vtitle contains 'otro' or vtitle contains 'otra' -%}
            {%- assign otro_variant_id = variant.id -%}
          {%- endif -%}
        {%- endfor -%}

        {%- comment -%} Donation widget {%- endcomment -%}
        <div class="donation-widget" 
             id="DonationWidget-{{ section.id }}"
             data-otro-variant="{{ otro_variant_id }}"
             data-section-id="{{ section.id }}">

          <h1 class="product__title h5 leading-tight mb-lg">{{ product.title }}</h1>

          {% if product.description != blank %}
            <div class="donation-widget__description rte text-16 mb-lg tabletl:text-18">{{ product.description }}</div>
          {% endif %}

          {%- comment -%} Frequency toggle {%- endcomment -%}
          <div class="donation-widget__frequency mb-lg" role="group" aria-label="Frecuencia de donación">
            <button type="button" class="donation-freq-btn active" data-freq="once" aria-pressed="true">Una vez</button>
            <button type="button" class="donation-freq-btn" data-freq="monthly" aria-pressed="false">Mensual</button>
          </div>

          {%- comment -%} Plan cards — shown only when Mensual is active {%- endcomment -%}
          <div class="donation-widget__plans mb-lg" id="DonationPlans-{{ section.id }}" aria-hidden="true" style="display:none">
            <div class="donation-plans-grid">
              <button type="button" class="donation-plan-btn" data-plan="mensual">Mensual</button>
              <button type="button" class="donation-plan-btn" data-plan="trimestral">Trimestral</button>
              <button type="button" class="donation-plan-btn" data-plan="semestral">Semestral</button>
              <button type="button" class="donation-plan-btn" data-plan="anual">Anual</button>
            </div>
          </div>

          {%- comment -%} Preset amount grid — all non-Otro variants {%- endcomment -%}
          <div class="donation-widget__amounts mb-lg">
            <div class="donation-amounts-grid">
              {%- for variant in product.variants -%}
                {%- assign vtitle = variant.title | downcase -%}
                {%- unless vtitle == 'otro' or vtitle contains 'otro' or vtitle contains 'otra' -%}
                  <button type="button"
                          class="donation-amount-btn"
                          data-variant-id="{{ variant.id }}"
                          data-price="{{ variant.price | divided_by: 100.0 }}"
                          {% unless variant.available %}disabled{% endunless %}>
                    {{ variant.price | money_without_trailing_zeros }}
                  </button>
                {%- endunless -%}
              {%- endfor -%}
            </div>
          </div>

          {%- comment -%} Custom amount field {%- endcomment -%}
          <div class="donation-widget__custom mb-lg">
            <div class="donation-custom__wrapper">
              <span class="donation-custom__prefix" aria-hidden="true">€</span>
              <input type="number"
                     class="donation-custom__input"
                     id="DonationCustom-{{ section.id }}"
                     placeholder="Otra cantidad"
                     min="1"
                     step="1"
                     aria-label="Otra cantidad en euros">
            </div>
          </div>

          {%- comment -%} Impact line {%- endcomment -%}
          <div class="donation-widget__impact mb-lg" id="DonationImpact-{{ section.id }}" aria-live="polite"></div>

          {%- comment -%} Seal block hidden — driven programmatically by JS {%- endcomment -%}
          <div class="seal-anchor" id="SealAnchor-{{ section.id }}" aria-hidden="true" style="display:none !important">
            {%- for block in section.blocks -%}
              {% render block %}
            {%- endfor -%}
          </div>

          {%- comment -%} IO container is rendered by the IO app block (re-enabled in JSON) — hidden via CSS {%- endcomment -%}

          <button
            class="btn btn--gold py-md w-full uppercase relative"
            type="submit"
            {% unless current_variant.available %} disabled {% endunless %}
            js-add-to-cart>
            <loading-spinner style="--size: 3rem; --bg-opacity: 100%;"></loading-spinner>
            Donar ahora
          </button>
          <p class="hidden" js-error-message></p>

          <p class="donation-widget__trust text-14 text-center mt-sm">Pago seguro · Cancelar en cualquier momento</p>
        </div><!-- .donation-widget -->

      {%- endform -%}
    </div><!-- .product__information -->
```

- [ ] **Step 3: Verify the file still has the image carousel, ProductJSON, LD+JSON, and cart dedup script**

Read the file and confirm:
- Lines before `product__information`: image carousel div still present
- After the closing `</div><!-- .product__layout -->` and `</s-product>`: `<script type="application/json" id="ProductJSON">` present (once, not twice)
- LD+JSON `<script type="application/ld+json">` present
- Cart dedup `<script>(function() { ... })();</script>` present at bottom

If the duplicate `<script id="ProductJSON">` (original bug at lines 163–165) is present, remove the second copy now.

- [ ] **Step 4: Commit**

```bash
git add sections/product__donation.liquid
git commit -m "feat: donation widget — HTML structure"
```

---

## Task 3: Add CSS styles for the donation widget

**Files:**
- Modify: `sections/product__donation.liquid` — add `<style>` block inside `<s-product>` before the closing `</s-product>` tag (or inline in the section, before the `{% schema %}` block)

- [ ] **Step 1: Add the style block**

Insert this `<style>` block into `sections/product__donation.liquid`, after `</s-product>` and before `{%- liquid ... -%}` (the SEO media assignment block):

```liquid
<style>
/* donation-widget */
.donation-widget__frequency {
  display: flex;
  gap: 0;
  border: 1px solid #e7e3d8;
  border-radius: 62.4375rem;
  overflow: hidden;
  width: fit-content;
}
.donation-freq-btn {
  padding: 0.625rem 1.5rem;
  background: transparent;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
  color: inherit;
  transition: background-color 0.15s ease-out, color 0.15s ease-out;
  line-height: 1.5;
}
.donation-freq-btn.active {
  background-color: #d6bf90;
  color: #16254c;
  font-weight: 600;
}
.donation-freq-btn:hover:not(.active) {
  background-color: #e8dbc0;
}
.donation-plans-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
}
.donation-plan-btn {
  padding: 0.75rem 1rem;
  border: 1px solid #e7e3d8;
  border-radius: 0.5rem;
  background: transparent;
  cursor: pointer;
  font-size: 0.875rem;
  font-weight: 500;
  text-align: center;
  transition: all 0.15s ease-out;
}
.donation-plan-btn.active {
  background-color: #d6bf90;
  border-color: #d6bf90;
  color: #16254c;
  font-weight: 600;
}
.donation-plan-btn:hover:not(.active) {
  border-color: #d6bf90;
}
.donation-amounts-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
}
.donation-amount-btn {
  padding: 0.75rem 0.5rem;
  border: 1px solid #e7e3d8;
  border-radius: 0.5rem;
  background: transparent;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  text-align: center;
  transition: all 0.15s ease-out;
}
.donation-amount-btn.active {
  background-color: #d6bf90;
  border-color: #d6bf90;
  color: #16254c;
}
.donation-amount-btn:hover:not(.active):not([disabled]) {
  border-color: #d6bf90;
}
.donation-amount-btn[disabled] {
  opacity: 0.4;
  cursor: not-allowed;
}
.donation-custom__wrapper {
  display: flex;
  align-items: center;
  border: 1px solid #e7e3d8;
  border-radius: 0.5rem;
  padding: 0 1rem;
  transition: border-color 0.15s ease-out;
}
.donation-custom__wrapper:focus-within {
  border-color: #d6bf90;
  outline: 2px solid #d6bf9040;
}
.donation-custom__prefix {
  font-weight: 600;
  color: #16254c;
  padding-right: 0.5rem;
  font-size: 1rem;
  user-select: none;
}
.donation-custom__input {
  flex: 1;
  border: none;
  padding: 0.75rem 0;
  font-size: 1rem;
  background: transparent;
  outline: none;
  width: 100%;
  -moz-appearance: textfield;
}
.donation-custom__input::-webkit-inner-spin-button,
.donation-custom__input::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
.donation-widget__impact {
  font-size: 0.875rem;
  color: #16254c;
  min-height: 1.5rem;
  font-style: italic;
}
.donation-widget__trust {
  color: #6b7280;
  font-size: 0.8125rem;
}
/* Hide Seal and IO native UI */
.seal-anchor,
#infiniteoptions-container {
  display: none !important;
}
</style>
```

- [ ] **Step 2: Verify visually on dev server (if running)**

Run the Shopify dev server:
```bash
shopify theme dev --store d016j0-nz.myshopify.com
```
Navigate to the donation product page. Confirm:
- Frequency toggle appears as a pill segmented control
- Amount grid is 3 columns
- Custom field has € prefix
- No Seal widget visible
- No IO container visible

- [ ] **Step 3: Commit**

```bash
git add sections/product__donation.liquid
git commit -m "feat: donation widget — CSS styles"
```

---

## Task 4: Add widget JavaScript

**Files:**
- Modify: `sections/product__donation.liquid` — add a `<script>` block after the cart dedup script and before the `{% schema %}` block

- [ ] **Step 1: Add the widget script**

Insert this script block after the cart dedup `</script>` and before `{% schema %}`:

```liquid
<script>
(function() {
  'use strict';

  function initDonationWidget(sectionId) {
    var sectionEl = document.querySelector('s-product[data-section-id="' + sectionId + '"]');
    if (!sectionEl) return;

    var widgetEl    = sectionEl.querySelector('#DonationWidget-' + sectionId);
    var masterSel   = sectionEl.querySelector('#MasterSelect-' + sectionId);
    var sealAnchor  = sectionEl.querySelector('#SealAnchor-' + sectionId);
    var plansPanel  = sectionEl.querySelector('#DonationPlans-' + sectionId);
    var impactEl    = sectionEl.querySelector('#DonationImpact-' + sectionId);
    var customInput = sectionEl.querySelector('#DonationCustom-' + sectionId);
    var otroVariantId = widgetEl ? widgetEl.dataset.otroVariant : null;
    var ioInput     = null;

    if (!widgetEl || !masterSel) return;

    var state = { freq: 'once', plan: 'mensual', custom: false };

    /* ── Frequency toggle ── */
    sectionEl.querySelectorAll('[data-freq]').forEach(function(btn) {
      btn.addEventListener('click', function() {
        setFreq(btn.dataset.freq);
      });
    });

    function setFreq(freq) {
      state.freq = freq;
      sectionEl.querySelectorAll('[data-freq]').forEach(function(b) {
        var on = b.dataset.freq === freq;
        b.classList.toggle('active', on);
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
      if (freq === 'monthly') {
        plansPanel.style.display = '';
        plansPanel.setAttribute('aria-hidden', 'false');
        selectPlan(state.plan || 'mensual');
      } else {
        plansPanel.style.display = 'none';
        plansPanel.setAttribute('aria-hidden', 'true');
        clickSealOneTime();
      }
    }

    /* ── Plan cards ── */
    sectionEl.querySelectorAll('[data-plan]').forEach(function(btn) {
      btn.addEventListener('click', function() {
        selectPlan(btn.dataset.plan);
      });
    });

    function selectPlan(planName) {
      state.plan = planName;
      sectionEl.querySelectorAll('[data-plan]').forEach(function(b) {
        b.classList.toggle('active', b.dataset.plan === planName);
      });
      clickSealPlan(planName);
    }

    function clickSealPlan(planName) {
      if (!sealAnchor) return;
      /* Seal renders radio inputs; find the one whose label contains the plan name */
      var radios = sealAnchor.querySelectorAll('input[type="radio"]');
      var matched = false;
      radios.forEach(function(radio) {
        if (matched) return;
        var labelEl = sealAnchor.querySelector('label[for="' + radio.id + '"]')
                    || radio.closest('label')
                    || radio.parentElement;
        var text = (labelEl ? labelEl.textContent : '').toLowerCase().trim();
        if (text.indexOf(planName.toLowerCase()) !== -1) {
          radio.click();
          matched = true;
        }
      });
    }

    function clickSealOneTime() {
      /* Click Seal's "compra única" or first non-subscription option */
      if (!sealAnchor) return;
      var radios = sealAnchor.querySelectorAll('input[type="radio"]');
      var oneTimeTerms = ['vez', 'once', 'única', 'unica', 'one-time', 'one time'];
      var matched = false;
      radios.forEach(function(radio) {
        if (matched) return;
        var labelEl = sealAnchor.querySelector('label[for="' + radio.id + '"]')
                    || radio.closest('label')
                    || radio.parentElement;
        var text = (labelEl ? labelEl.textContent : '').toLowerCase();
        oneTimeTerms.forEach(function(term) {
          if (!matched && text.indexOf(term) !== -1) {
            radio.click();
            matched = true;
          }
        });
      });
    }

    /* ── Amount buttons ── */
    sectionEl.querySelectorAll('[data-variant-id]').forEach(function(btn) {
      btn.addEventListener('click', function() {
        if (btn.disabled) return;
        state.custom = false;
        clearCustomField();
        setActiveAmountBtn(btn);
        setVariant(btn.dataset.variantId);
        showImpact(parseFloat(btn.dataset.price));
      });
    });

    function setActiveAmountBtn(activeBtn) {
      sectionEl.querySelectorAll('[data-variant-id]').forEach(function(b) {
        b.classList.toggle('active', b === activeBtn);
      });
    }

    function setVariant(variantId) {
      if (!masterSel) return;
      masterSel.value = variantId;
      masterSel.dispatchEvent(new Event('change', { bubbles: true }));
    }

    /* ── Custom amount ── */
    if (customInput) {
      customInput.addEventListener('input', handleCustomInput);
    }

    function handleCustomInput() {
      var val = (customInput.value || '').trim();
      if (!val || parseFloat(val) <= 0) {
        state.custom = false;
        clearIO();
        return;
      }
      state.custom = true;
      /* Deselect preset buttons */
      sectionEl.querySelectorAll('[data-variant-id]').forEach(function(b) {
        b.classList.remove('active');
      });
      /* Auto-switch to Una vez if monthly is active */
      if (state.freq === 'monthly') {
        setFreq('once');
      }
      /* Route to IO */
      syncIO(val);
      /* Select "Otro" variant so the form submits a valid variant ID */
      if (otroVariantId) {
        setVariant(otroVariantId);
      } else {
        /* Fallback: use first available variant */
        var firstOption = masterSel.options[0];
        if (firstOption) setVariant(firstOption.value);
      }
      showImpact(parseFloat(val));
    }

    function syncIO(val) {
      resolveIO();
      if (ioInput) {
        ioInput.value = val;
        ioInput.dispatchEvent(new Event('input', { bubbles: true }));
        ioInput.dispatchEvent(new Event('change', { bubbles: true }));
      }
    }

    function clearIO() {
      resolveIO();
      if (ioInput) ioInput.value = '';
    }

    function resolveIO() {
      if (ioInput) return;
      var container = document.querySelector('#infiniteoptions-container');
      if (container) {
        ioInput = container.querySelector('input[type="text"], input[type="number"], textarea');
      }
    }

    function clearCustomField() {
      if (customInput) customInput.value = '';
      clearIO();
    }

    /* ── Impact line ── */
    function showImpact(amount) {
      if (!impactEl) return;
      if (!amount || isNaN(amount) || amount <= 0) {
        impactEl.textContent = '';
        return;
      }
      impactEl.textContent = 'Tu donación de ' + Math.round(amount) + '€ ayuda a mantener el templo abierto.';
    }

    /* ── Auto-select first preset on load ── */
    var firstBtn = sectionEl.querySelector('[data-variant-id]');
    if (firstBtn && !firstBtn.disabled) {
      firstBtn.classList.add('active');
      setVariant(firstBtn.dataset.variantId);
      showImpact(parseFloat(firstBtn.dataset.price));
    }
  }

  /* Init after DOM ready */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      initDonationWidget('{{ section.id }}');
    });
  } else {
    initDonationWidget('{{ section.id }}');
  }
})();
</script>
```

- [ ] **Step 2: Manual smoke test — open dev server and test each interaction**

With `shopify theme dev` running, navigate to the donation product page and test:

| Action | Expected |
|---|---|
| Page loads | First preset amount button is highlighted gold |
| Click a different amount | That button turns gold, others clear |
| Click Mensual | Plan panel slides into view; first preset amount stays selected |
| Click Trimestral card | Trimestral card turns gold |
| Click back to Una vez | Plan panel hides |
| Type 25 in custom field | All preset buttons clear; frequency switches to Una vez if was on Mensual; impact line shows "25€" |
| Clear custom field | Impact line clears |
| Click Donar ahora | Spinner shows, cart is updated (verify in cart drawer) |

- [ ] **Step 3: Verify Seal radio is being clicked (browser console check)**

In browser console while on the donation page:
```javascript
document.querySelector('#SealAnchor-' + document.querySelector('[data-section-id]').dataset.sectionId + ' input[type="radio"]')
```
Expected: returns a radio input element (confirms Seal rendered its widget inside the anchor).

If Seal has not rendered radios (returns null), Seal may render async. This is acceptable — the `clickSealPlan` function searches at click time, not at init.

- [ ] **Step 4: Commit**

```bash
git add sections/product__donation.liquid
git commit -m "feat: donation widget — JavaScript interaction logic"
```

---

## Task 5: Fix pre-existing duplicate ProductJSON bug

**Files:**
- Modify: `sections/product__donation.liquid`

The original file had a duplicate `<script type="application/json" id="ProductJSON">` block (lines 163–165). Duplicate IDs cause `document.getElementById('ProductJSON')` to return unpredictably. Remove the second copy.

- [ ] **Step 1: Find and remove the duplicate**

Search `sections/product__donation.liquid` for `id="ProductJSON"`. There should be exactly one instance. If two exist, remove the second one (the duplicate that appears after the first).

- [ ] **Step 2: Confirm single instance**

```bash
grep -c 'id="ProductJSON"' sections/product__donation.liquid
```
Expected: `1`

- [ ] **Step 3: Commit**

```bash
git add sections/product__donation.liquid
git commit -m "fix: remove duplicate ProductJSON script tag in donation section"
```

---

## Task 6: Full acceptance test

**No code changes in this task — testing only.**

- [ ] **Step 1: Start dev server**

```bash
shopify theme dev --store d016j0-nz.myshopify.com
```

- [ ] **Step 2: Test preset + Una vez**

1. Load donation page
2. Click any preset amount (e.g., 10€)
3. Confirm Mensual plan panel is hidden
4. Click "Donar ahora"
5. Open cart: item should be 10€ with no subscription tag

- [ ] **Step 3: Test preset + Mensual**

1. Click "Mensual" toggle — plan panel appears
2. Click "Trimestral" plan card
3. Click "Donar ahora"
4. Open cart: item should show a Seal subscription badge/label for Trimestral

- [ ] **Step 4: Test custom + Una vez**

1. Type "37" in the Otra cantidad field
2. Confirm preset buttons deselect, frequency stays/switches to Una vez
3. Confirm impact line says "Tu donación de 37€ ayuda..."
4. Click "Donar ahora"
5. Open cart: item should have the custom amount as a line item property (check via cart API: `fetch('/cart.js').then(r=>r.json()).then(c=>console.log(JSON.stringify(c.items[0].properties,null,2)))`)

- [ ] **Step 5: Test custom auto-switches from Mensual**

1. Click "Mensual"
2. Select "Anual" plan
3. Type "50" in custom field
4. Confirm frequency switches back to "Una vez", plan panel hides

- [ ] **Step 6: Test cart dedup (re-donate)**

1. Add a donation to cart
2. Without emptying cart, return to donation page
3. Select a different amount
4. Click "Donar ahora"
5. Check cart: should have only ONE donation item at the new amount (old one removed)

- [ ] **Step 7: Commit (if any fix was needed)**

If any test revealed a bug, fix it and commit:
```bash
git add sections/product__donation.liquid
git commit -m "fix: donation widget — [describe what was fixed]"
```

---

## Task 7: Push to live theme (requires explicit approval)

**Do NOT run this task without user confirmation.**

- [ ] **Step 1: Get approval**

Ask the user: "All acceptance tests pass. Ready to push to the live theme?"

- [ ] **Step 2: Push**

Only after explicit approval:
```bash
shopify theme push --store d016j0-nz.myshopify.com --theme 183370088792 --allow-live
```

Expected: all changed files upload, no errors.

- [ ] **Step 3: Verify on live**

Open the live donation page in a browser and confirm the widget appears correctly.

---

## Self-Review

**Spec coverage check:**
- [x] Frequency toggle (Una vez / Mensual) — Task 2 HTML + Task 4 JS `setFreq()`
- [x] 4 plan cards (mensual/trimestral/semestral/anual) — Task 2 HTML + Task 4 JS `selectPlan()`
- [x] Preset amount grid (3-col, all non-Otro variants) — Task 2 HTML + Task 4 JS amount buttons
- [x] Custom amount field with € prefix — Task 2 HTML + Task 4 JS `handleCustomInput()`
- [x] Custom + monthly → auto-switch to Una vez — Task 4 JS `handleCustomInput()` `setFreq('once')` call
- [x] Seal hidden, driven programmatically — Task 2 `.seal-anchor` + Task 3 CSS + Task 4 `clickSealPlan()`
- [x] IO block re-enabled — Task 1
- [x] IO container hidden — Task 3 CSS `#infiniteoptions-container { display:none !important }`
- [x] IO input driven by custom field — Task 4 `syncIO()`
- [x] Cart dedup script preserved — not touched (explicitly kept)
- [x] Duplicate ProductJSON bug fixed — Task 5
- [x] Impact line — Task 2 HTML + Task 4 `showImpact()`
- [x] Trust line — Task 2 HTML
- [x] CTA button uses btn--gold — Task 2 HTML
- [x] Auto-select first preset on load — Task 4 JS init block
- [x] Acceptance criteria test matrix — Task 6

**No placeholders found.** All code blocks are complete. All file paths are exact. Type/method names consistent across tasks.
