# Figma → Shopify Rollout — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring the live Shopify theme into alignment with the BM España Figma sitemap by sequencing work from highest-impact / lowest-effort to lowest-impact / highest-effort.

**Architecture:** Pure Shopify Liquid theme, no build step. Many target pages already exist as `templates/page.*.json`; the gap is mostly content, missing sections inside existing pages, and a handful of new pages. The main menu is data-driven (Shopify Admin `linklists`), so reordering navigation is an Admin-side task, not code.

**Tech Stack:** Shopify Liquid, Bootstrap 5, theme.css (utility classes), Swiper.js, FullCalendar, Klaviyo, Spanish/English locales (`es.json` primary).

---

## Strategy: How tasks were ordered

Each task was scored on two axes:

| Axis | What it measures |
|------|------------------|
| **Impact** | How visible/valuable to visitors and conversion |
| **Effort** | Hours of work + risk of breaking things |

**Order = (Impact × Visibility) ÷ Effort.** Quick wins first, blockers second, big-content third, speculative work last. Each phase ships independently and is committable.

### Phase summary

| Phase | Theme | Why first | Approx. effort |
|-------|-------|-----------|----------------|
| 0 | **Audit & confirm** what *really* exists vs sitemap | We have ~38 page templates already; without an audit we'd duplicate work | 1-2 h |
| 1 | **Main menu reorder** (Shopify Admin) | Single biggest visual change for ~zero code risk; surfaces existing pages | 30-60 min |
| 2 | **URL slug migrations** (21 listed in `admin-url-changes.md`) | Pre-launch blocker, low effort, high SEO/UX value | 1-2 h |
| 3 | **Polish "Sobre Paramahamsa Vishwananda"** — add 5 missing sections | Page already exists, just adding sections; very high traffic page | 4-6 h |
| 4 | **New page: Rezar por el mundo** (9 sections, all new) | Recurring monthly engagement driver; self-contained | 6-8 h |
| 5 | **Templo individual pages polish** (Lanzarote + Málaga, ✅ confirmed existing) | Templates exist and are teal; verify content + add any missing sections | 2-3 h |
| 6 | **Darshan landing** (`/pages/darshan`) | Blocked on business decisions per `darshan.md`; do when unblocked | 8-12 h |
| 7 | **"Encuentra tu profesor" feature** | Reuses existing map infrastructure | 4-6 h |
| 8 | **Speculative / small pages** — Suscríbete, Contacta Swami Akash, Donación landing, Adopta un deity, etc. | Nice-to-have, can wait | 2-4 h each |

---

## Phase 0 — Audit existing pages vs sitemap

**Why first:** We have `templates/page.aky.json`, `page.omc.json`, `page.bsn.json`, `page.knowledge.json`, `page.rituals.json`, `page.devotional-arts.json`, `page.master.json`, `page.project-mantra.json`, `page.sri-yantra.json`, `page.vedic-chanting.json`, `page.templo-hari-hara.json`, `page.templo-bhava-narasimha.json`, etc. Many "uncertain ⚪" entries in the sitemap probably already exist. Without auditing, we'd build duplicates.

### Task 0.1: Cross-reference templates with sitemap

**Files:**
- Read: every file under `templates/page.*.json` and `templates/page.*.liquid`
- Update: `figma-to-shopify.md` with confirmed status

- [ ] **Step 1: List every `templates/page.*` file with what it appears to be**

For each template, open the JSON and read the `name` field plus the first 2-3 sections to identify what page it represents. Map them to the sitemap entries.

Example mapping (verify, then mark):
```
page.master.json     → Sobre Paramahamsa Vishwananda (sitemap node 44:1836)
page.aky.json        → Atma Kriya Yoga (sitemap node 44:1589)
page.omc.json        → Om Chanting (sitemap node 44:1606)
page.bsn.json        → Babaji Surya Namaskar (sitemap node 44:1624)
page.knowledge.json  → Conocimiento (sitemap node 44:2127)
page.rituals.json    → Rituales (sitemap node 44:2146)
page.devotional-arts.json → Artes Devocionales (sitemap node 44:2162)
page.project-mantra.json → Project Mantra (sitemap node 44:1641)
page.sri-yantra.json → Sri Yantra (sitemap node 44:1803)
page.vedic-chanting.json → Canto de oraciones (sitemap node 44:1677)
page.templo-hari-hara.json → Templo Lanzarote (sitemap node 66:8801)
page.templo-bhava-narasimha.json → Templo Málaga (sitemap node 66:8818)
page.give.json       → Haz una donación (sitemap node 44:2414)
page.start-now.json  → Suscríbete? (verify)
```

- [ ] **Step 2: Verify each template is published as a live page in Shopify Admin**

In Shopify Admin → Pages, search for each handle. Note which templates are unused (template exists but no page assigned).

- [ ] **Step 3: Update `figma-to-shopify.md` with confirmed statuses**

Replace ⚪ "uncertain" markers with one of:
- ✅ **Exists and published** (template + page both live)
- 🟨 **Template exists, no page assigned** (just create page in Admin)
- 🔴 **Neither template nor page exists** (real new build)

- [ ] **Step 4: Commit the audit**

```bash
git add figma-to-shopify.md
git commit -m "docs: audit figma sitemap against existing page templates"
```

---

## Phase 1 — Main menu reorder (Shopify Admin)

**Why early:** Highest perceived change, zero code risk. The header reads from `linklists[section.settings.header_nav]` — the menu is Admin-configured, not code.

**Confirmed navigation structure (from Figma sitemap Level pills, April 2026 analysis):**

Root domain: `bhaktimarga.es`

Main nav — 6 items left to right:
1. **Conoce al Maestro** → Sobre Paramahamsa Vishwananda + Homepage column
2. **Prácticas Bhakti** → Prácticas Bhakti pages column
3. **Experiencias locales** → Sanghas, Templos, local encounters
4. **Cursos online** → course pages
5. **Donaciones** → donation pages (Haz una donación, Adopta un deity)
6. **Tienda ↗** (external/shop link with sub-items: Todos los productos ↗, Esenciales bhakti ↗, Libros y música ↗)

Note: No dedicated navigation UI design exists in Figma. Nav is built and managed via Shopify Admin linklists. The above names come from the sitemap pill labels.

### Task 1.1: Draft the new menu structure from sitemap

**Files:**
- Reference: `figma-to-shopify.md` (column groupings)
- Create: `docs/menu-structure-proposal.md` (new working doc)

- [ ] **Step 1: Map sitemap columns to top-level menu items**

Use the confirmed 6-item structure above as the basis. Map each item to existing pages/collections in Admin.

Write the proposed structure to `docs/menu-structure-proposal.md` as a tree.

- [ ] **Step 2: User reviews and approves the structure**

Send the doc to the user. Wait for approval before touching the live menu.

- [ ] **Step 3: User implements in Shopify Admin → Navigation → Main menu**

This is a manual Admin step. Provide step-by-step instructions in the proposal doc.

- [ ] **Step 4: Verify on dev theme before pushing live**

```bash
shopify theme dev --store d016j0-nz.myshopify.com
```
Click through every dropdown. Verify links resolve. Check mobile drawer.

- [ ] **Step 5: Commit the proposal doc**

```bash
git add docs/menu-structure-proposal.md
git commit -m "docs: propose new main menu structure aligned with figma sitemap"
```

---

## Phase 2 — URL slug migrations (21 URLs)

**Why now:** Listed as a launch blocker in `admin-url-changes.md` and `CLAUDE.md`. Pure Admin work. Low effort, high SEO value, must happen before Phase 3-7 to avoid relinking later.

### Task 2.1: Execute slug migrations from `admin-url-changes.md`

**Files:**
- Reference: `admin-url-changes.md`
- Modify: any Liquid file that hardcodes the old URLs

- [ ] **Step 1: Read `admin-url-changes.md` and list each URL change in a checklist**

- [ ] **Step 2: For each URL change, search the codebase for hardcoded references**

```bash
grep -rn "old-slug" --include="*.liquid" --include="*.json" --include="*.js"
```

Replace any hardcoded references with the new slug. Pages linked via `linklists` (the menu) auto-update — no code change needed.

- [ ] **Step 3: User changes the slugs in Shopify Admin → Pages**

Admin step. Shopify creates 301 redirects automatically.

- [ ] **Step 4: Verify each old URL 301-redirects to the new URL**

Use `curl -I https://d016j0-nz.myshopify.com/pages/old-slug` and confirm `301` + `Location:` header.

- [ ] **Step 5: Commit any code changes**

```bash
git add -A
git commit -m "fix: update hardcoded URLs to match new slug scheme"
```

---

## Phase 3 — Polish "Sobre Paramahamsa Vishwananda"

**Why now:** Highest-traffic content page. Template (`page.master.json`) and page exist. We're only adding 5 sections. Self-contained, no architecture risk.

**Sitemap node:** `44:1836` — page now has 18 sections total (confirmed April 2026). 5 sections remain orange (not built): Eventos con Él, Festivales, Peregrinajes, Lo que otros dicen, Darshan en Lanzarote 2026.

### Task 3.1: Inspect current `page.master.json` content

**Files:**
- Read: `templates/page.master.json`
- Read: section files referenced by it

- [ ] **Step 1: Open `templates/page.master.json` and list its current sections**

- [ ] **Step 2: Note which sitemap items are already implemented**

The audit in Phase 0.1 already cross-references this. Confirm the 5 orange items are genuinely missing.

### Task 3.2: Add "Eventos con Él" section

**Files:**
- Create or reuse: `sections/Seccion__events-with-him.liquid` (or reuse existing event-list section)
- Modify: `templates/page.master.json` (add the new section to its `order` array)

- [ ] **Step 1: Decide whether to reuse an existing event section or create new**

Check if `sections/Seccion__upcoming-events.liquid` or similar already filters by event type. If yes, reuse with a `tag:guruji` filter or similar.

- [ ] **Step 2: Add the section block to `templates/page.master.json`**

Insert the new section block in the appropriate position (after "Estadísticas", before "YouTube"). Keep the existing sections intact.

- [ ] **Step 3: Push to dev and visually verify**

```bash
shopify theme dev --store d016j0-nz.myshopify.com
```
Open `/pages/sobre-paramahamsa-vishwananda` (or current slug). Confirm section renders.

- [ ] **Step 4: Commit**

```bash
git add sections/Seccion__events-with-him.liquid templates/page.master.json
git commit -m "feat(master): add Eventos con Él section"
```

### Task 3.3: Add "Festivales" section

**Files:**
- Create or reuse: section that lists festival events
- Modify: `templates/page.master.json`

- [ ] **Step 1: Same pattern as Task 3.2 — reuse/create festival list section**

- [ ] **Step 2: Wire it into the template**

- [ ] **Step 3: Visually verify**

- [ ] **Step 4: Commit**

```bash
git commit -m "feat(master): add Festivales section"
```

### Task 3.4: Add "Peregrinajes" section

Same pattern. Pilgrimage list or static content block.

- [ ] **Step 1-4: Build, wire, verify, commit**

```bash
git commit -m "feat(master): add Peregrinajes section"
```

### Task 3.5: Add "Lo que otros dicen" (testimonials) section

**Files:**
- Create: `sections/Seccion__testimonials.liquid` (if not present)
- Modify: `templates/page.master.json`

- [ ] **Step 1: Check if a testimonial component exists**

Search `sections/` for "testimonial" or "review".

- [ ] **Step 2: Build a Swiper-based testimonial carousel**

Match existing Swiper integration patterns in the theme — pass options via `data-options` JSON attribute.

- [ ] **Step 3: Wire into template**

- [ ] **Step 4: Verify and commit**

```bash
git commit -m "feat(master): add testimonials carousel"
```

### Task 3.6: Add "Darshan en Lanzarote 2026" CTA banner

**Files:**
- Create: `sections/Seccion__darshan-banner.liquid` (or reuse a hero/banner section)
- Modify: `templates/page.master.json`

- [ ] **Step 1: Build a prominent CTA banner that links to the Darshan landing page**

Until Phase 6 ships the Darshan page, link to `/pages/darshan-lanzarote-2026` even if it's a placeholder.

- [ ] **Step 2: Wire and verify**

- [ ] **Step 3: Commit**

```bash
git commit -m "feat(master): add Darshan Lanzarote 2026 CTA banner"
```

---

## Phase 4 — New page: Rezar por el mundo

**Why now:** Self-contained, no dependencies, recurring engagement driver (monthly prayer event). All 9 sections are new, but the page is small.

### Task 4.1: Create page template and admin page

**Files:**
- Create: `templates/page.pray-for-the-world.json`
- Admin: Create page "Rezar por el mundo" using this template, slug `/pages/rezar-por-el-mundo`

- [ ] **Step 1: Copy `templates/page.master.json` as a starting structure**

```bash
cp templates/page.master.json templates/page.pray-for-the-world.json
```

Then strip down to skeleton sections.

- [ ] **Step 2: Define the 9 sitemap sections in `order` array**

Sections to wire in (each as its own task below):
1. Introducción
2. Enviar nombres (form)
3. YouTube embed
4. Reserva la fecha
5. Sobre Guruji
6. Sobre el mantra
7. Project Mantra widget
8. El poder de la oración
9. El poder de la intención

- [ ] **Step 3: Commit skeleton**

```bash
git add templates/page.pray-for-the-world.json
git commit -m "feat: scaffold Rezar por el Mundo page template"
```

### Task 4.2: Build "Introducción" section

**Files:**
- Create: `sections/Seccion__pray-intro.liquid`

- [ ] **Step 1: Build hero/intro section with title, subtitle, image**

Match BM-* class conventions from theme.css. Use utility classes (`flex`, `px-md`, `py-xxxl`, etc.).

- [ ] **Step 2: Add to the page template `order` array**

- [ ] **Step 3: Verify and commit**

```bash
git commit -m "feat(pray): add introduction hero section"
```

### Task 4.3-4.10: Build remaining 8 sections

One task per section, same pattern. Each:
- Create `sections/Seccion__pray-<name>.liquid`
- Wire into template
- Verify visually
- Commit

The "Enviar nombres" section needs a Klaviyo form embed (the theme already integrates Klaviyo per `CLAUDE.md`). Reuse that integration.

The "YouTube" and "Project Mantra" sections are likely embeddable widgets — keep static `iframe` or embed code minimal.

---

## Phase 5 — Templo individual pages polish

**Why now:** Both templates exist (`page.templo-hari-hara.json`, `page.templo-bhava-narasimha.json`). **April 2026 Figma analysis confirms both pages are ✅ teal (existing/built) with 6 sections each, all shown as gray (existing).** Effort reduced — mostly verify content and publish.

**Status confirmed:**
- Templo Lanzarote: Hari Hara — ✅ teal, sitemap node `66:8801`, 6 sections all gray
- Templo Málaga: Bhava Narasimha — ✅ teal, sitemap node `66:8818`, 6 sections all gray

**Also confirmed:** A "Templos" hub page exists in Figma (navy `#002656` header, 3 sections: intro + links to both temple sub-pages). Verify `/pages/templos` is published and correctly links to both temple individual pages.

### Task 5.1: Audit Templo Lanzarote: Hari Hara

**Files:**
- Read: `templates/page.templo-hari-hara.json`

- [ ] **Step 1: Open the template, list its current sections**

- [ ] **Step 2: Compare to sitemap node `66:8801`**

Sitemap sections (all teal/gray = existing): Portada/intro, Próximos eventos, Sobre el templo, Horarios, Direcciones, Contacto.

- [ ] **Step 3: Verify page is published in Admin with correct slug**

### Task 5.2: Verify Templo Málaga: Bhava Narasimha

Same as 5.1 for `templates/page.templo-bhava-narasimha.json`. All 6 sections confirmed teal/gray.

- [ ] **Step 1: Verify page is published in Admin with correct slug**
- [ ] **Step 2: Confirm all sections render correctly**

### Task 5.3: Verify "Templos" hub page

- [ ] **Step 1: Confirm `/pages/templos` is published**
- [ ] **Step 2: Verify it links to both individual temple pages**
- [ ] **Step 3: If not built, create template with 3 sections: intro + links to Lanzarote and Málaga pages**

---

## Phase 6 — Darshan landing page

**Why now (not earlier):** Blocked on business decisions per `darshan.md` (capacity, pricing, refund policy). Schedule this phase only after the association treasurer confirms Shopify Payments + decisions land.

### Task 6.1: Read `darshan.md` and confirm decisions are unblocked

- [ ] **Step 1: Open `darshan.md`**
- [ ] **Step 2: Confirm with treasurer that all blockers are resolved**
- [ ] **Step 3: If still blocked, skip this phase and continue with Phase 7**

### Task 6.2: Build Darshan landing per `darshan.md` spec

The spec covers 4 ticket tiers with QR integration. Use existing `sections/section__ticket-tier.liquid`.

- [ ] **Step 1: Create `templates/page.darshan.json`**
- [ ] **Step 2: Wire 6 sitemap sections (Portada, Próximos eventos, Sobre Darshan, Como funciona, Beneficios, Reseñas)**
- [ ] **Step 3: Integrate ticket tier carousel from existing component**
- [ ] **Step 4: Add QR code generation (per `darshan.md` API selection)**
- [ ] **Step 5: Verify and commit**

---

## Phase 7 — "Encuentra tu profesor" feature

**Why now:** Reuses the existing `page.profesores.liquid` map. Mostly UI polish + filtering.

### Task 7.1: Inspect `page.profesores.liquid`

- [ ] **Step 1: Read the current implementation**
- [ ] **Step 2: Identify what filters are missing for "Find by practice" (AKY, Om Chanting, BSN, etc.)**

### Task 7.2: Add practice filter to teacher map

- [ ] **Step 1: Define filter UI in the Liquid template**
- [ ] **Step 2: Wire filter to existing map JS**
- [ ] **Step 3: Add filter chip per practice, default "All"**
- [ ] **Step 4: Verify on dev**
- [ ] **Step 5: Commit**

```bash
git commit -m "feat(profesores): add practice-based filter"
```

### Task 7.3: Surface "Encuentra tu profesor" links from practice sub-pages

On AKY, Om Chanting, BSN pages: link to the filtered teacher map.

- [ ] **Step 1: Add link section to each practice page template**
- [ ] **Step 2: Pass practice filter as URL param (e.g. `?practica=aky`)**
- [ ] **Step 3: Profesores page reads the param on load and applies filter**

---

## Phase 8 — Speculative / small pages

**Why last:** Nice-to-have, can defer until Phases 1-7 are landed.

### Tasks (each is its own small unit)

- [ ] **Task 8.1: "Suscríbete" dedicated page** — single Klaviyo form. ~1 h.
- [ ] **Task 8.2: "Contacta con Swami Akash"** — contact form variant. Designer shows gold dashed border (unusual) + gray "Formulario" section, suggesting contact form infrastructure is considered existing. ~1 h.
- [ ] **Task 8.3: "Haz una donación" landing** — Figma now has a dedicated card (navy `#002656` header, 1 TBD section). Wraps existing donation product (`page.give.json`) with marketing copy. ~2 h.
- [ ] **Task 8.4: "Adopta un deity"** — NEW concept discovered in April 2026 Figma analysis. Navy `#002656` header, 1 TBD section. Deity adoption/sponsorship as a donation engagement feature. Build once donation/payment infrastructure is confirmed. ~3-4 h.
- [ ] **Task 8.5: "Bhakti Marga España" page** — Figma now shows 3 sections: "Sobre los swamis", "Sobre Swami Akash", "Contacta con él". ~2 h.
- [ ] **Task 8.6: "Todos los eventos con Él"** — collection or page listing all events. ~1-2 h.
- [ ] **Task 8.7: "Darshan Lanzarote 2026"** — when business decisions confirmed. TBD.

---

## Footer status (April 2026)

**No footer design exists in Figma.** The Figma file contains only the sitemap diagram — no wireframes, no component library, no UI designs for header or footer.

**Footer is ✅ built and functional:**
- `sections/footer.liquid` exists and works
- 12-column grid: 6-col nav area (`footer_nav` linklist) + 5-col contact/social area
- Contact block: `contact_title` + `contact_body` settings (admin-configurable)
- Social media: Instagram, X, YouTube, Facebook, Flickr (in `snippets/social-media-links.liquid`)
- Subfooter bar: language switcher + `subfooter_nav` linklist + copyright
- All nav links admin-configurable via Shopify linklists (no hardcoded links)

**Remaining Admin-only tasks (no code changes needed):**
- Legal pages (Aviso Legal, Política de Cookies, Política de Privacidad) NOT yet published — publish and add their links to `subfooter_nav` menu in Admin
- No BM logo in footer (content gap)
- No CIF G76198209 / non-profit info in footer (content gap)
- Newsletter handled via Klaviyo global embed in `theme.liquid` + dedicated Suscríbete page (not in footer by design)

---

## Homepage sections (April 2026 confirmed state)

**12 sections total** (up from previous count):

| # | Section name | Status |
|---|---|---|
| 1 | Portada: Conócele / Sobre Él | ✅ teal |
| 2 | Darshan | ✅ teal |
| 3 | Eventos y Festivales | ✅ teal |
| 4 | Encuentros locales | ✅ teal |
| 5 | Cursos online | ✅ teal |
| 6 | Visita un templo | ✅ teal |
| 7 | Project Mantra | ✅ teal |
| 8 | Rezar por el Mundo | ✅ teal |
| 9 | Prácticas diarias Bhakti | ✅ teal |
| 10 | Nuestras creencias | ⚪ gray/uncertain (node 62:7324, kept by designer — no decision to remove) |
| 11 | Nuestros valores | ⚪ gray/uncertain (node 62:7325, kept by designer — no decision to remove) |
| 12 | Suscríbete | ✅ teal |

Note: Section 1 was previously labeled "Portada" — full name confirmed as "Portada: Conócele / Sobre Él".

---

## Self-review notes

**Spec coverage:** Every page from `figma-to-shopify.md` is mapped to a phase. The 14 sub-practice pages from the "uncertain ⚪" table are all handled by Phase 0 audit (most exist already).

**Changes since initial plan (April 2026 Figma analysis):**
- Temples both confirmed ✅ teal — Phase 5 effort reduced
- "Templos" hub page confirmed existing
- "Adopta un deity" is a new page concept discovered (added to Phase 8)
- "Haz una donación" now has its own dedicated card in Figma (was only a note before)
- Sobre Paramahamsa Vishwananda has 18 sections (up from ~13 previously estimated)
- Footer confirmed built — only Admin configuration tasks remain
- Navigation 6-item structure confirmed from sitemap pills
- Kirtan renamed to "Kirtan: Canto devocional"
- Pintura devocional renamed to "Pintura de arte devocional"
- Empty placeholder frame 57:5518 found in Figma (x=9360, y=3631) — designer artifact, no action needed

**Risk areas:**
- Phase 1 menu reorder requires user/admin action — flagged.
- Phase 6 has external blockers — flagged.
- "Bhakti Marga España" page — Figma now shows 3 sections, enough to build. No longer fully speculative.
- "Adopta un deity" — novel concept, needs stakeholder validation on pricing/fulfillment model before building.

**Dependencies between phases:**
- Phase 2 (slug migration) should land before Phase 3 to avoid re-linking.
- Phase 7 depends on Phase 0 audit (need to confirm `page.profesores.liquid` existing structure).
- Phase 6 depends on `darshan.md` being unblocked.
