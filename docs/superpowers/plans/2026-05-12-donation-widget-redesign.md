# Donation Widget Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create `templates/product.haz-una-donacion.json` + `sections/product__haz-una-donacion.liquid` — a stepper-based donation page matching bhaktimarga.org, without touching `product.donation.*`.

**Architecture:** Two new files only. The section keeps the same Liquid/form skeleton as `product__donation.liquid` (same `<s-donation>` wrapper, same hidden Seal wiring, same JSON-LD) but replaces the JS/HTML/CSS in the right column with: stacked-radio frequency rows → stepper rows per variant → total bar + CTA. A new JS IIFE replaces DonationMain.

**Tech Stack:** Shopify Liquid, vanilla JS (IIFE, no framework), scoped CSS custom properties. No build step.

---

## Task 1: Create the JSON template

**Files:**
- Create: `templates/product.haz-una-donacion.json`

- [ ] **Step 1: Write the file**

```json
{
  "sections": {
    "main": {
      "type": "product__haz-una-donacion",
      "blocks": {
        "seal_subscriptions_subscription_widget_DXMRR7": {
          "type": "shopify://apps/seal-subscriptions/blocks/subscription-widget/13b25004-a140-4ab7-b5fe-29918f759699",
          "settings": {
            "product": "{{product}}"
          }
        }
      },
      "block_order": [
        "seal_subscriptions_subscription_widget_DXMRR7"
      ],
      "settings": {}
    }
  },
  "order": ["main"]
}
```

- [ ] **Step 2: Verify JSON is valid**

```bash
node -e "const fs=require('fs');JSON.parse(fs.readFileSync('templates/product.haz-una-donacion.json','utf8'));console.log('OK')"
```

Expected output: `OK`

- [ ] **Step 3: Commit**

```bash
git add templates/product.haz-una-donacion.json
git commit -m "feat: add product.haz-una-donacion.json template"
```

---

## Task 2: Create the section file

**Files:**
- Create: `sections/product__haz-una-donacion.liquid`

This is the main file. It contains Liquid HTML, scoped CSS, a JS IIFE, JSON-LD, and the schema block. Write it in full — do not split across partial files.

**Context you need to know:**
- The left column (image carousel) is copied verbatim from `sections/product__donation.liquid` lines 7–66. Do not modify it.
- The right column (`don2-info`) is new — stacked radio rows + stepper rows + total bar.
- CSS uses `--don2-*` custom properties scoped to `s-donation[data-section-id="{{ section.id }}"]`.
- JS reads variant data from `#ProductJSON` (the inline `{{ product | json }}` tag). No global variables.
- The hidden `.subscription-container` and `.seal-anchor` blocks must be preserved verbatim — Seal reads them.

- [ ] **Step 1: Write the complete section file**

Create `sections/product__haz-una-donacion.liquid` with this exact content:

```liquid
{%- liquid
  assign current_variant = product.selected_or_first_available_variant
  assign product_form_id = 'ProductForm-' | append: section.id | append: product.id
  assign master_select_id = 'MasterSelect-' | append: section.id
-%}

{%- capture carousel_options -%}
  {
    "slidesPerView": "auto",
    "freeMode": true,
    "touchRatio": 1,
    "momentum": true,
    "mousewheel": {"forceToAxis": true},
    "loop": false,
    "spaceBetween": "16",
    "pagination": {"el": ".swiper-pagination","type": "bullets","clickable": true}
  }
{%- endcapture -%}

<s-donation role="section" class="product block container py-md tabletl:py-xl" data-section-id="{{ section.id }}">
  <a class="skip-to-content-link sr-only" href="#ProductInfo-{{ section.id }}">Skip to product information</a>
  <div class="product__layout tabletl:grid tabletl:grid-cols-2 tabletl:gap-md">

    <div class="product__images">
      <s-carousel data-init="belowLaptop" data-options='{{carousel_options}}'>
        <div id="ProductMainImages" class="swiper w-full pb-[50px]" js-carousel>
          <div class="swiper-wrapper tabletl:grid tabletl:grid-cols-2 tabletl:gap-md">
            {% for media in product.media %}
              {% assign slide_classes = 'aspect-[7/9] relative z-1 overflow-hidden' %}
              {% assign index_mod_3 = forloop.index | modulo: 3 %}
              {% if index_mod_3 == 1 %}
                {% assign slide_classes = slide_classes | append: ' tabletl:col-span-2' %}
              {% elsif index_mod_3 == 2 or index_mod_3 == 0 %}
                {% assign slide_classes = slide_classes | append: ' tabletl:col-span-1' %}
              {% endif %}
              {% case media.media_type %}
                {% when 'image' %}
                  <div class="swiper-slide {{ slide_classes }}" js-carousel-slide>
                    {% render 'lazy-image', image: media, picture_classes: 'h-full', img_classes: 'object-cover h-full rounded' %}
                  </div>
                {% when 'video' %}
                  <div class="swiper-slide {{ slide_classes }}" js-carousel-slide>
                    {{ media | video_tag: controls: true, autoplay: false, loop: true, mute: false, class: 'w-full h-full object-cover block' }}
                  </div>
                {% when 'external_video' %}
                  <div class="swiper-slide {{ slide_classes }}" js-carousel-slide>
                    {{ media | external_video_tag }}
                  </div>
              {% endcase %}
            {% endfor %}
          </div>
          <div class="swiper-pagination tabletl:hidden"></div>
        </div>
      </s-carousel>
    </div>

    <div class="don2-info py-lg tabletl:py-xl tabletl:px-xxl tabletl:sticky tabletl:top-[var(--header-height)]" id="ProductInfo-{{ section.id }}">
      {%- form 'product', product, id: product_form_id, class: 'form', novalidate: 'novalidate', js-product-form: true -%}

        <select class="sr-only" id="{{ master_select_id }}" name="id" js-master-select>
          {%- for variant in product.variants -%}
            <option value="{{ variant.id }}"{% if variant == current_variant %} selected{% endif %}{% unless variant.available %} disabled{% endunless %}>
              {{ variant.title }}
            </option>
          {%- endfor -%}
        </select>

        <h1 class="product__title h5 leading-tight mb-lg">{{ product.title }}</h1>

        {% if product.description != blank %}
          <div class="don2-desc rte text-16 mb-lg">{{ product.description }}</div>
        {% endif %}

        <div class="don2-freq mb-sm" role="group" aria-label="Frecuencia de donación">
          <label class="don2-freq__row don2-freq__row--active" data-freq="once">
            <span class="don2-freq__dot"></span>
            <span class="don2-freq__title">Donación única</span>
            <span class="don2-freq__sub">one-time</span>
          </label>
          <label class="don2-freq__row" data-freq="monthly">
            <span class="don2-freq__dot"></span>
            <span class="don2-freq__title">Donación mensual recurrente</span>
            <span class="don2-freq__sub">monthly</span>
          </label>
        </div>

        <div class="don2-plan-detail mb-lg" id="Don2PlanDetail-{{ section.id }}" style="display:none" aria-live="polite">
          <span class="don2-plan-detail__icon">↻</span>
          <span>Detalles de la suscripción · <span class="don2-plan-detail__name">mensual</span></span>
        </div>

        <div class="don2-amounts" id="Don2Amounts-{{ section.id }}">
          {%- for variant in product.variants -%}
            <div class="don2-row"
                 data-variant-id="{{ variant.id }}"
                 data-price="{{ variant.price | divided_by: 100.0 }}"
                 {% unless variant.available %}data-unavailable{% endunless %}>
              <span class="don2-row__label">{{ variant.price | money_without_trailing_zeros }}</span>
              <div class="don2-stepper" role="group" aria-label="Cantidad {{ variant.title }}">
                <button type="button" class="don2-stepper__btn don2-stepper__minus" aria-label="Quitar {{ variant.title }}" disabled>−</button>
                <span class="don2-stepper__qty" aria-live="polite">0</span>
                <button type="button" class="don2-stepper__btn don2-stepper__plus" aria-label="Añadir {{ variant.title }}"{% unless variant.available %} disabled{% endunless %}>+</button>
              </div>
            </div>
          {%- endfor -%}
        </div>

        <div class="don2-totalbar">
          <div class="don2-totalbar__left">
            <span class="don2-totalbar__label">Importe total:</span>
            <span class="don2-totalbar__amt" id="Don2Total-{{ section.id }}">0,00 €</span>
          </div>
          <button class="don2-cta" type="submit" js-add-to-cart>
            <loading-spinner style="--size: 3rem; --bg-opacity: 100%;"></loading-spinner>
            Donar ahora
          </button>
        </div>

        <p class="don2-trust">Pago seguro · Tarjeta · Apple Pay · Cancela cuando quieras</p>

        <div class="subscription-container sr-only" aria-hidden="true">
          <label>
            <input type="checkbox" class="sr-only" js-subscription-checkbox>
            <span></span>
          </label>
          <div>
            <select name="selling_plan" js-subscription-select>
              {%- for group in product.selling_plan_groups -%}
                {%- for plan in group.selling_plans -%}
                  {%- assign plan_freq = plan.name | downcase -%}
                  {%- if plan.name == 'Monthly' -%}{%- assign plan_freq = 'mensual' -%}
                  {%- elsif plan.name == 'Quarterly' -%}{%- assign plan_freq = 'trimestral' -%}
                  {%- elsif plan.name == 'Yearly' or plan.name == 'Annual' -%}{%- assign plan_freq = 'anual' -%}
                  {%- elsif plan.name contains 'Semi' or plan.name contains '6' -%}{%- assign plan_freq = 'semestral' -%}
                  {%- endif -%}
                  <option value="{{ plan.id }}" data-plan="{{ plan_freq }}">{{ plan_freq | capitalize }}</option>
                {%- endfor -%}
              {%- endfor -%}
            </select>
          </div>
        </div>

        <div class="seal-anchor sr-only" id="SealAnchor-{{ section.id }}" aria-hidden="true" style="display:none">
          {%- for block in section.blocks -%}
            {% render block %}
          {%- endfor -%}
        </div>

        <p class="hidden" js-error-message></p>

      {%- endform -%}
    </div>
  </div>

  <script type="application/json" id="ProductJSON">{{ product | json }}</script>
</s-donation>

{%- liquid
  if product.selected_or_first_available_variant.featured_media
    assign seo_media = product.selected_or_first_available_variant.featured_media
  else
    assign seo_media = product.featured_media
  endif
-%}
<script type="application/ld+json">
{
  "@context": "http://schema.org/",
  "@type": "Product",
  "name": {{ product.title | json }},
  "url": {{ shop.url | append: product.url | json }},
  {% if seo_media -%}
  "image": [{{ seo_media | image_url: width: seo_media.preview_image.width | prepend: "https:" | json }}],
  {%- endif %}
  "description": {{ product.description | strip_html | json }},
  {%- if product.selected_or_first_available_variant.sku != blank -%}
  "sku": {{ product.selected_or_first_available_variant.sku | json }},
  {%- endif -%}
  "brand": {"@type": "Brand","name": {{ product.vendor | json }}},
  "offers": [
    {%- for variant in product.variants -%}
    {
      "@type": "Offer",
      {%- if variant.sku != blank -%}"sku": {{ variant.sku | json }},{%- endif -%}
      "availability": "http://schema.org/{% if variant.available %}InStock{% else %}OutOfStock{% endif %}",
      "price": {{ variant.price | divided_by: 100.00 | json }},
      "priceCurrency": {{ cart.currency.iso_code | json }},
      "url": {{ shop.url | append: variant.url | json }}
    }{% unless forloop.last %},{% endunless %}
    {%- endfor -%}
  ]
}
</script>

<style>
s-donation[data-section-id="{{ section.id }}"] {
  --don2-ink: #16254c;
  --don2-line: #e7e3d8;
  --don2-line2: #ececec;
  --don2-paper: #fbf9f3;
  --don2-muted: #6b6f7a;
  --don2-dot-border: #c9c4b4;
}
.don2-freq {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--don2-line);
  border-radius: 10px;
  overflow: hidden;
}
.don2-freq__row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  cursor: pointer;
  background: #fff;
  transition: background .15s;
  font-size: 14px;
}
.don2-freq__row + .don2-freq__row { border-top: 1px solid var(--don2-line); }
.don2-freq__row--active { background: var(--don2-paper); }
.don2-freq__dot {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  border: 1.5px solid var(--don2-dot-border);
  flex: none;
  position: relative;
  transition: border-color .15s;
}
.don2-freq__row--active .don2-freq__dot { border-color: var(--don2-ink); }
.don2-freq__row--active .don2-freq__dot::after {
  content: '';
  position: absolute;
  inset: 3px;
  border-radius: 50%;
  background: var(--don2-ink);
}
.don2-freq__title { font-weight: 600; color: var(--don2-ink); }
.don2-freq__sub { color: var(--don2-muted); font-size: 12px; margin-left: auto; font-family: monospace; }
.don2-plan-detail {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #2b3a5e;
  font-size: 13px;
  margin: 0 2px;
  padding: 2px 0;
}
.don2-plan-detail__icon {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--don2-paper);
  border: 1px solid var(--don2-line);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  color: #7a6533;
  flex: none;
}
.don2-amounts { border-top: 1px solid var(--don2-line2); margin-bottom: 4px; }
.don2-row {
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
  padding: 13px 4px;
  border-bottom: 1px solid var(--don2-line2);
  gap: 14px;
  transition: background .15s;
}
.don2-row--active { background: var(--don2-paper); }
.don2-row__label { font-size: 15px; color: var(--don2-ink); }
.don2-row--active .don2-row__label { font-weight: 600; }
.don2-stepper { display: flex; align-items: center; gap: 14px; font-variant-numeric: tabular-nums; }
.don2-stepper__btn {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  border: 1.5px solid var(--don2-dot-border);
  background: #fff;
  color: var(--don2-ink);
  font-size: 18px;
  line-height: 1;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: border-color .15s, background .15s;
  padding: 0;
}
.don2-stepper__btn:hover:not(:disabled) { border-color: var(--don2-ink); background: var(--don2-paper); }
.don2-stepper__btn:disabled { opacity: .35; cursor: not-allowed; }
.don2-stepper__qty { min-width: 24px; text-align: center; font-weight: 600; font-size: 15px; color: var(--don2-ink); }
.don2-totalbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  padding: 16px 4px;
  border-top: 1px solid var(--don2-line);
  flex-wrap: wrap;
}
.don2-totalbar__label { font-size: 15px; font-weight: 600; color: var(--don2-ink); }
.don2-totalbar__amt {
  font-family: monospace;
  font-size: 22px;
  font-weight: 700;
  color: var(--don2-ink);
  font-variant-numeric: tabular-nums;
  margin-left: 8px;
}
.don2-cta {
  appearance: none;
  border: 0;
  background: var(--don2-ink);
  color: #fff;
  font: inherit;
  font-weight: 700;
  font-size: 13px;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: 15px 28px;
  border-radius: 4px;
  cursor: pointer;
  transition: background .15s;
  position: relative;
}
.don2-cta:hover { background: #1f3168; }
.don2-cta:disabled { opacity: .6; cursor: not-allowed; }
.don2-trust { text-align: center; font-size: 12px; color: var(--don2-muted); margin-top: 12px; margin-bottom: 0; }
.seal-anchor, #infiniteoptions-container { display: none !important; }
@media (max-width: 767px) {
  .don2-totalbar {
    position: sticky;
    bottom: 0;
    background: #fff;
    padding: 12px 16px;
    margin: 0 -16px;
    border-top: 1px solid var(--don2-line);
    z-index: 10;
  }
}
</style>

<script>
(function () {
  'use strict';
  function initDon2(sectionId) {
    var root = document.querySelector('s-donation[data-section-id="' + sectionId + '"]');
    if (!root) return;
    var masterSel   = root.querySelector('[js-master-select]');
    var subCheckbox = root.querySelector('[js-subscription-checkbox]');
    var subSelect   = root.querySelector('[js-subscription-select]');
    var totalEl     = root.querySelector('#Don2Total-' + sectionId);
    var planDetail  = root.querySelector('#Don2PlanDetail-' + sectionId);
    var rows        = root.querySelectorAll('.don2-row');
    var freqLabels  = root.querySelectorAll('.don2-freq__row');
    var state = { freq: 'once', plan: 'mensual', qtys: {} };
    rows.forEach(function (row) { state.qtys[row.dataset.variantId] = 0; });

    freqLabels.forEach(function (label) {
      label.addEventListener('click', function () { setFreq(label.dataset.freq); });
    });

    function setFreq(freq) {
      state.freq = freq;
      freqLabels.forEach(function (l) {
        l.classList.toggle('don2-freq__row--active', l.dataset.freq === freq);
      });
      if (freq === 'monthly') {
        if (planDetail) planDetail.style.display = '';
        var opt = subSelect && subSelect.querySelector('option[data-plan="' + state.plan + '"]');
        if (opt) { subSelect.value = opt.value; subSelect.dispatchEvent(new Event('change', { bubbles: true })); }
        if (subCheckbox) { subCheckbox.checked = true; subCheckbox.dispatchEvent(new Event('change', { bubbles: true })); }
      } else {
        if (planDetail) planDetail.style.display = 'none';
        if (subCheckbox) { subCheckbox.checked = false; subCheckbox.dispatchEvent(new Event('change', { bubbles: true })); }
      }
    }

    rows.forEach(function (row) {
      var vid   = row.dataset.variantId;
      var minus = row.querySelector('.don2-stepper__minus');
      var plus  = row.querySelector('.don2-stepper__plus');
      var qtyEl = row.querySelector('.don2-stepper__qty');
      plus.addEventListener('click', function () {
        state.qtys[vid]++;
        syncRow(row, vid, minus, qtyEl);
        recompute();
      });
      minus.addEventListener('click', function () {
        if (state.qtys[vid] <= 0) return;
        state.qtys[vid]--;
        syncRow(row, vid, minus, qtyEl);
        recompute();
      });
    });

    function syncRow(row, vid, minus, qtyEl) {
      var q = state.qtys[vid];
      qtyEl.textContent = q;
      minus.disabled = q <= 0;
      row.classList.toggle('don2-row--active', q > 0);
      if (q > 0 && masterSel) {
        masterSel.value = vid;
        masterSel.dispatchEvent(new Event('change', { bubbles: true }));
      }
    }

    function recompute() {
      var sum = 0;
      rows.forEach(function (row) {
        var price = parseFloat(row.dataset.price) || 0;
        sum += price * (state.qtys[row.dataset.variantId] || 0);
      });
      if (totalEl) totalEl.textContent = sum.toLocaleString('es-ES', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' €';
    }

    var form = root.querySelector('.form');
    if (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var sellingPlanId = (state.freq === 'monthly' && subSelect) ? (subSelect.value || null) : null;
        var items = [];
        rows.forEach(function (row) {
          var qty = state.qtys[row.dataset.variantId] || 0;
          if (qty <= 0) return;
          var item = { id: parseInt(row.dataset.variantId, 10), quantity: qty };
          if (sellingPlanId) item.selling_plan = parseInt(sellingPlanId, 10);
          items.push(item);
        });
        if (!items.length) return;
        var cta = root.querySelector('.don2-cta');
        if (cta) cta.disabled = true;
        fetch('/cart/add.js', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify({ items: items })
        })
        .then(function (r) {
          if (!r.ok) throw new Error('cart/add ' + r.status);
          return r.json();
        })
        .then(function () {
          document.dispatchEvent(new CustomEvent('cart:open'));
          document.dispatchEvent(new CustomEvent('theme:cart:open'));
          window.dispatchEvent(new CustomEvent('cart:open'));
        })
        .catch(function (err) {
          var errEl = root.querySelector('[js-error-message]');
          if (errEl) { errEl.textContent = 'Error al añadir al carrito. Inténtalo de nuevo.'; errEl.classList.remove('hidden'); }
          console.error('[don2]', err);
        })
        .finally(function () { if (cta) cta.disabled = false; });
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { initDon2('{{ section.id }}'); });
  } else {
    initDon2('{{ section.id }}');
  }
})();
</script>

{% schema %}
{
  "name": "Donation v2",
  "blocks": [{"type": "@app"}]
}
{% endschema %}
```

- [ ] **Step 2: Verify the file exists and has content**

```bash
wc -l sections/product__haz-una-donacion.liquid
```

Expected: at least 200 lines.

- [ ] **Step 3: Verify original files untouched**

```bash
git diff -- sections/product__donation.liquid templates/product.donation.json
```

Expected: no output (no changes to those files).

- [ ] **Step 4: Commit**

```bash
git add sections/product__haz-una-donacion.liquid
git commit -m "feat: add product__haz-una-donacion section — stepper donation widget v2"
```

---

## Task 3: Assign template to product and test on dev store

**Context:** The new template must be assigned to the donation product in Shopify admin for the page to render. The dev store is `d016j0-nz.myshopify.com`.

- [ ] **Step 1: Push both files to the dev store**

```bash
shopify theme push --store d016j0-nz.myshopify.com --theme 183370088792 --allow-live --only templates/product.haz-una-donacion.json sections/product__haz-una-donacion.liquid
```

Expected: `✓ theme pushed` with no errors.

- [ ] **Step 2: Assign the template to the donation product**

In Shopify Admin → Products → "Hacer una donación" (or whatever the handle is) → Theme template → select `haz-una-donacion` → Save.

Alternatively use the dev store preview URL with `?preview_theme_id=183370088792` appended.

- [ ] **Step 3: Open the product page and run the test checklist**

Navigate to the product URL. Open browser DevTools → Console tab. Run through:

**Visual checks:**
- [ ] Page renders without Liquid errors (no `Liquid error:` text on page)
- [ ] Left column shows product image(s)
- [ ] Right column: product title and description visible
- [ ] Two stacked radio rows for frequency — "Donación única" (active by default) and "Donación mensual recurrente"
- [ ] Active row has `#fbf9f3` background and filled blue dot
- [ ] 5 stepper rows visible (1€, 5€, 10€, 50€, 100€)
- [ ] Each row: label left, `−` `0` `+` right
- [ ] `−` button starts disabled (opacity 0.35)
- [ ] "Importe total: 0,00 €" visible below rows
- [ ] "DONAR AHORA" CTA button visible, `#16254c` background
- [ ] No console errors

**Interaction checks:**
- [ ] Click `+` on 10€ row → qty shows `1`, row bg turns `#fbf9f3`, total shows `10,00 €`, `−` enabled
- [ ] Click `+` on 10€ again → qty shows `2`, total shows `20,00 €`
- [ ] Click `+` on 50€ → total shows `70,00 €`
- [ ] Click `−` on 10€ → qty `1`, total `60,00 €`
- [ ] Click `−` until 0 → `−` disabled again, row bg resets to white
- [ ] Click "Donación mensual recurrente" → row activates (dot fills), plan detail line appears
- [ ] Click "Donación única" → plan detail hidden, dot resets
- [ ] Click "DONAR AHORA" with nothing selected → nothing happens (no cart request)
- [ ] Click `+` on any row, then "DONAR AHORA" → `POST /cart/add.js` fires (check Network tab), cart drawer opens

**Mobile check (resize to < 768px):**
- [ ] Single column layout (image above, controls below)
- [ ] Total bar + CTA row sticks to viewport bottom

- [ ] **Step 4: Commit test evidence**

If all checks pass:

```bash
git commit --allow-empty -m "test: product__haz-una-donacion — all acceptance criteria verified on dev store"
```

---

## Self-Review

**Spec coverage check:**
- ✅ JSON template created with correct section type and Seal block
- ✅ Section HTML: title, description, frequency radios, stepper rows, total bar, CTA, trust line
- ✅ CSS: frequency dot styles, stepper button styles, active row, total bar, mobile sticky
- ✅ JS: frequency toggle → Seal wiring, stepper +/−, total recompute, cart submit with selling_plan
- ✅ Liquid: master select, subscription-container, seal-anchor, blocks loop, JSON-LD all present
- ✅ `product.donation.*` not touched (Task 2 Step 3 verifies)
- ✅ Mobile sticky total bar in CSS

**Placeholder scan:** None found — all code is complete.

**Type consistency:** `state.qtys[row.dataset.variantId]` used consistently. `syncRow()` called in both `+` and `−` handlers. `don2-freq__row--active` class toggled in both `setFreq()` and initial HTML.
