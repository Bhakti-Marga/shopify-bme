# Figma → Shopify: Plan de trabajo
> Extraído del sitemap de Figma (archivo `6tFHS9TCH3SRBhtaDUQhJ7`, sección `44:1436`)
> Última auditoría de templates: 2026-04-28
> Última actualización: 2026-04-29

---

## Leyenda — colores del sitemap

| Color del icono | Significado |
|----------------|-------------|
| 🟠 Naranja `#e95500` | Sección/página NO existe todavía — **construir** |
| 🩵 Teal/cyan `#00a3b2` | Sección ya existe en Shopify |
| ⬛ Gris oscuro `#444` | Planificada, estado incierto — revisar |
| 🟡 Dorado `#927244` | Enlace a producto de tienda |
| 🟣 Morado `#5c5a8c` | Feature interactiva especial (mapa, directorio) |

**Color de cabecera = categoría:**
`#002656` azul marino = BM España / PV · `#00a3b2` teal = Comunidad / Prácticas · `#927244` dorado = sub-página de práctica · `#5c5a8c` morado = feature especial

---

## Leyenda — estado de template (auditoría)

| Estado | Significado |
|--------|-------------|
| ✅ | Template JSON/Liquid existe en `templates/` y página publicada |
| 🟨 | Template existe — verificar asignación de página en Admin |
| 🔴 | No existe ni template ni página — construir desde cero |
| ⚠️ | Template existe en inglés — revisar/traducir o eliminar |

---

## Resumen ejecutivo

| Estado | Páginas |
|--------|---------|
| ✅ Confirmadas (template + página) | ~28 |
| 🟨 Template creado, contenido pendiente de negocio | ~3 |
| 🟨 Template existe, verificar asignación en Admin | ~10 |
| 🔴 Nuevas por construir | 5 |
| ⚠️ Templates en inglés (revisar) | 5 |
| 🔮 Features interactivas por completar | 2 |

> 2026-04-29: menú principal ✅, footer ✅, hub Templos ✅, páginas Darshan Lanzarote / Eventos con Él / Adopta un Deity creadas con template placeholder.

---

## 🔴 Páginas nuevas — no existe template

### 1. Rezar por el mundo
**URL:** `/pages/rezar-por-el-mundo` · Teal header
- [ ] Introducción
- [ ] Enviar nombres (formulario Klaviyo)
- [ ] YouTube embed
- [ ] Reserva la fecha
- [ ] Sobre Guruji
- [ ] Sobre el mantra
- [ ] Project Mantra widget
- [ ] El poder de la oración
- [ ] El poder de la intención

### 2. Suscríbete
**URL:** `/pages/suscribete` · Teal header
- [ ] Formulario de suscripción (Klaviyo embed)

### 3. Darshan (landing)
**URL:** `/pages/darshan` · Teal header, borde `#e0d3c2`
**Bloqueado:** decisiones de negocio (ver `darshan.md`)
- [ ] Portada/introducción
- [ ] Próximos eventos Darshan
- [ ] Sobre Darshan
- [ ] Cómo funciona
- [ ] Beneficios
- [ ] Reseñas

### 4. Darshan Lanzarote 2026 🟨 Template creado (2026-04-29)
**URL:** `/pages/darshan-lanzarote-2026` · Azul marino
**Bloqueado:** decisiones de negocio (ver `darshan.md`)
- [x] `templates/page.darshan-lanzarote.json` creado — hero placeholder "Próximamente"
- [x] Página creada en Admin y asignada al template
- [ ] 2 secciones TBD — pendiente de confirmación de negocio

### 5. Todos los eventos con Él 🟨 Template creado (2026-04-29)
**URL:** `/pages/eventos-con-el` · Azul marino
- [x] `templates/page.eventos-con-el.json` creado — hero con título y subtítulo
- [x] Página creada en Admin y asignada al template
- [ ] Añadir sección de listado de eventos (colección filtrada) cuando exista el catálogo

### 6. Encuentra tu profesor (standalone)
**URL:** `/pages/encuentra-tu-profesor` · Morado `#5c5a8c`
- [ ] Feature de mapa/lista con filtro por práctica
- Reutilizar `templates/page.profesores.liquid`

### 7. Cursos online (listado)
**URL:** `/collections/cursos` o `/pages/cursos-online`
- [ ] Página/colección de cursos online disponibles

### 8. Adopta un deity ⭐ NUEVO (descubierto abril 2026) 🟨 Template creado (2026-04-29)
**URL:** `/pages/adopta-un-deity` · Azul marino
- [x] `templates/page.adopta-un-deity.json` creado — hero placeholder "Próximamente"
- [x] Página creada en Admin y asignada al template
- [ ] Validar modelo con stakeholders (precio, fulfillment, qué ofrece la "adopción")
- [ ] Construir secciones definitivas una vez confirmadas las decisiones de negocio

---

## 🟡 Páginas existentes con secciones que faltan

### Sobre Paramahamsa Vishwananda
**Template:** ✅ `templates/page.master.json` · 18 secciones (13 existentes + 5 naranjas)

Secciones existentes ✅: Portada, Misión, Amor incondicional, Fundador de BM, Cita de Guruji, Es Satguru/Kriya Yogi, Satgurus son especiales, Estadísticas, YouTube Insights from Guruji, Darshan, Síguele en Instagram, Síguele en X, Portada outro misión

**Secciones que faltan 🔴:**
- [ ] Eventos con Él
- [ ] Festivales
- [ ] Peregrinajes
- [ ] Lo que otros dicen (testimonios/reseñas)
- [ ] Darshan en Lanzarote 2026 (banner/CTA)

---

### Homepage `/`
**Total:** 12 secciones (confirmado abril 2026)

| # | Sección | Estado |
|---|---------|--------|
| 1 | Portada: Conócele / Sobre Él | ✅ teal |
| 2 | Darshan | ✅ teal |
| 3 | Eventos y Festivales | ✅ teal |
| 4 | Encuentros locales | ✅ teal |
| 5 | Cursos online | ✅ teal |
| 6 | Visita un templo | ✅ teal |
| 7 | Project Mantra | ✅ teal |
| 8 | Rezar por el Mundo | ✅ teal |
| 9 | Prácticas diarias Bhakti | ✅ teal |
| 10 | Nuestras creencias | ⚪ gris — diseñadora las conserva sin decidir (node 62:7324) |
| 11 | Nuestros valores | ⚪ gris — diseñadora las conserva sin decidir (node 62:7325) |
| 12 | Suscríbete | ✅ teal |

---

### Prácticas Bhakti
**Template:** ✅ `templates/page.path.json` (15 secciones)

Secciones inciertas ⚪: Video introducción · El camino Bhakti · Prácticas diarias: 4 brazos

---

### Templos (hub) ✅ COMPLETADO (2026-04-29)
**Template:** `templates/page.templos.json` — hero + icon grid (Hari Hara + Bhava Narasimha), 3 secciones
- [x] `templates/page.templos.json` creado y página publicada en Admin
- [x] Links a los dos templos individuales funcionan

---

### Calendario de eventos
**Template:** ✅ `templates/page.calendar.liquid`
- [ ] Portada/introducción encima del calendario (⚪)

---

## ✅ Páginas confirmadas — solo verificar

| Página | Template | Estado |
|--------|----------|--------|
| Sanghas | `page.sangha-map.liquid` | ✅ Con mapa |
| Profesores | `page.profesores.liquid` | ✅ Con mapa |
| Templo Lanzarote: Hari Hara | `page.templo-hari-hara.json` | ✅ Confirmado teal (abril 2026) |
| Templo Málaga: Bhava Narasimha | `page.templo-bhava-narasimha.json` | ✅ Confirmado teal (abril 2026) |
| Bhakti Marga España | `page.mission.json` | 🟨 Verificar slug |
| El camino Bhakti | `page.path.json` | 🟨 Verificar slug |
| Haz una donación | `page.give.json` | 🟨 Verificar |
| Puja | `page.request-a-puja.json` | 🟨 Verificar |
| Contacta con Swami Akash | — | 🟨 Formulario gray (infraestructura existe) |

---

## 📄 Sub-páginas de práctica — auditoría de templates

| Página | Template | Estado |
|--------|----------|--------|
| Atma Kriya Yoga | `page.aky.json` | 🟨 8 secciones |
| Om Chanting | `page.omc.json` | 🟨 Encabezados en inglés |
| Babaji Surya Namaskar | `page.bsn.json` | 🟨 6 secciones |
| Project Mantra | `page.project-mantra.json` | 🟨 6 secciones |
| Puja | `page.request-a-puja.json` | 🟨 8 secciones |
| Canto de oraciones | `page.vedic-chanting.json` | 🟨 7 secciones |
| Kirtan: Canto devocional | — | 🔴 No encontrado standalone |
| Pintura de arte devocional | — | 🔴 No encontrado standalone |
| Yoga y Meditación | `page.y-m.json` | 🟨 9 secciones |
| Conocimiento | `page.knowledge.json` | 🟨 9 secciones + links tienda |
| Rituales | `page.rituals.json` | 🟨 8 secciones |
| Artes Devocionales | `page.devotional-arts.json` | 🟨 5 secciones |
| Sri Yantra | `page.sri-yantra.json` | 🟨 7 secciones |
| Templo Lanzarote: Hari Hara | `page.templo-hari-hara.json` | ✅ 6 secciones |
| Templo Málaga: Bhava Narasimha | `page.templo-bhava-narasimha.json` | ✅ 6 secciones |

---

## 🗺 Navegación confirmada (sitemap Level pills, abril 2026)

Root: `bhaktimarga.es`

| # | Ítem de menú | Agrupa |
|---|---|---|
| 1 | Conoce al Maestro | Homepage, Sobre Paramahamsa Vishwananda |
| 2 | Prácticas Bhakti | Prácticas Bhakti + sub-páginas |
| 3 | Experiencias locales | Sanghas, Templos, encuentros |
| 4 | Cursos online | Páginas de cursos |
| 5 | Donaciones | Haz una donación, Adopta un deity |
| 6 | Tienda ↗ | Todos los productos ↗ · Esenciales bhakti ↗ · Libros y música ↗ |

> El menú se gestiona vía Shopify Admin (linklists) — no está hardcoded en Liquid. No existe diseño de header en Figma (solo estos pills de sitemap).

---

## 🦶 Footer ✅ COMPLETADO (2026-04-29) — diseño final (Figma: `Zv83zUiKu6Vjz8Ba3NP5Wi`, node `1:2`)

**Diseño definitivo confirmado por la diseñadora.** `sections/footer.liquid` reescrito desde cero — coincide con el diseño Figma.

### Especificación final Figma

**Fondo:** `#16254c` · **Padding:** 91px arriba, 90px abajo, 66px laterales

**ZONA SUPERIOR — 6 columnas flex, gap 44px, ancho completo:**

| Columna | Encabezado | Sub-items |
|---------|-----------|-----------|
| 1 | El Maestro | Paramahamsa Vishwananda · Darshan Lanzarote 2026 · Todos los eventos con Él |
| 2 | Experiencias | Calendario de eventos · Cursos online · Prácticas Bhakti · Templos · Sanghas · Profesores |
| 3 | Donaciones | Apoya con una donación · Adopta un Deity |
| 4 | Tienda | Todos los productos · Libros y música · Esenciales bhakti |
| 5 | Aprende con Bhakti+ | *(sin sub-items — solo encabezado)* |
| 6 | Bhakti Marga | Contáctanos · Bhakti Marga Internacional · Shree Peetha Nilaya Ashram |

**ZONA INFERIOR — flex-col, gap 20px:**
- Fila 1: links legales (gap 40px) + iconos sociales (derecha): Política de privacidad y cookies · Aviso Legal · Términos del Servicio · © año Todos los derechos reservados
- Fila 2: `Asociación BHAKTI MARGA ESPAÑA, CIF G76198209. Calle Pablo Picasso, 11, 29719 Benamocarra, Málaga. Email: spain@bhaktimarga.es.`

**Iconos sociales:** Instagram, Facebook, YouTube — alineados a la derecha en la fila 1 inferior
**Tipografía encabezados:** 14px bold white · Sub-items: 14px white 50% opacidad · Zona inferior: 12px white 50% opacidad

### Cambios respecto al footer actual

| Elemento | Antes | Después |
|----------|-------|---------|
| Encabezados de columna | Ocultos (`class="hidden"`) | Visibles, bold |
| Columnas de nav | 6 genéricas sin títulos | 6 con títulos específicos (ver tabla) |
| Bloque de contacto (`contact_title`/`contact_body`) | ✅ presente | 🔴 Eliminar |
| Selector de idioma | ✅ presente | 🔴 Eliminar (no está en Figma) |
| Dirección legal / CIF | ❌ ausente | ✅ Añadir como setting |
| Iconos sociales | Columna derecha | Fila inferior derecha |
| Fondo | `bg-blue` | `#16254c` |
| Copyright | Dentro de `subfooter_nav` | Fila inferior, año dinámico |

### Cambios de código (`sections/footer.liquid`) ✅ todos completados
- [x] Mostrar encabezados de columna (quitar `class="hidden"`)
- [x] Reorganizar layout: columnas arriba, zona legal abajo
- [x] Eliminar bloque contacto (quitar settings `contact_title`, `contact_body`)
- [x] Eliminar selector de idioma
- [x] Añadir setting `legal_address` (textarea) con texto de dirección
- [x] Mover social icons a la fila inferior derecha (justify-content: space-between)
- [x] Actualizar fondo a `#16254c`
- [x] Mantener `footer_nav` y `subfooter_nav` linklists (admin-configurable)
- [ ] Publicar páginas legales y añadir a `subfooter_nav` en Admin — pendiente (ver `legal.md`)

---

## 🛒 Links a tienda (iconos dorados en sitemap)

| Sección | Producto en Shopify |
|---------|---------------------|
| Bhagavad Gita: Lo esencial | Necesita producto |
| Bhagavad Gita | Necesita producto |
| Shreemad Bhagavatam | Necesita producto |
| Otras publicaciones | Colección de libros |
| Libro de oraciones | Necesita producto |

---

## ⚠️ Templates en inglés — revisar o eliminar

| Template | Contenido | Acción |
|----------|-----------|--------|
| `page.all-programs.json` | "Bhakti Marga Programs" | Revisar o eliminar |
| `page.ashram.json` | "Shree Peetha Nilaya" | Revisar si aplica |
| `page.start-now.json` | "Start your Journey to Love" | Probable eliminar |
| `page.sunday-program.json` | "Bhakti Sundays" | Probable eliminar |
| `page.temple.json` | Generic English temple | Sustituir por templates específicos |

---

## 📋 Plan de implementación

**Estrategia:** orden = (Impacto × Visibilidad) ÷ Esfuerzo. Victorias rápidas primero, bloqueantes segundo, contenido nuevo tercero, especulativo al final.

**Tech Stack:** Shopify Liquid, Bootstrap 5, theme.css (utilidades), Swiper.js, FullCalendar, Klaviyo. Sin build step.

### Resumen de fases

| Fase | Qué | Por qué primero | Esfuerzo |
|------|-----|-----------------|----------|
| 0 | Auditoría templates vs sitemap | ✅ COMPLETADA | — |
| 1 | Reordenar menú principal (Admin) | Cambio visual máximo, riesgo cero de código | 30-60 min |
| 2 | Migración 21 URLs (`admin-url-changes.md`) | Bloqueante pre-lanzamiento, SEO | 1-2 h |
| 3 | Añadir 5 secciones naranjas a "Sobre PV" | Página de mayor tráfico, template ya existe | 4-6 h |
| 4 | Nueva página: Rezar por el mundo | Driver de engagement mensual, autocontenida | 6-8 h |
| 5 | Verificar páginas de templos | Templates ✅ — solo verificar contenido y slugs | 2-3 h |
| 6 | Darshan landing | Bloqueado — arrancar cuando se desbloquee `darshan.md` | 8-12 h |
| 7 | Feature "Encuentra tu profesor" | Reutiliza mapa existente, filtra por práctica | 4-6 h |
| 8 | Páginas pequeñas / especulativas | Nice-to-have, puede esperar | 1-4 h c/u |

---

### Fase 0 — Auditoría ✅ COMPLETADA

Cruzados todos los `templates/page.*` con el sitemap. Resultado: ~22 templates ya existen. Pendiente:
- [ ] Verificar en Admin qué templates tienen página publicada asignada correctamente

---

### Fase 1 — Menú principal ✅ COMPLETADO (2026-04-29)

**Sin código.** El header lee de `linklists[section.settings.header_nav]`.

- [x] Crear/reordenar el menú en Admin → Navigation → Main menu con los 6 ítems confirmados
- [x] Verificar en dev
- [x] Dropdowns y drawer móvil operativos

---

### Fase 2 — URL slugs (21 URLs)

Ver `admin-url-changes.md` para la lista completa.

- [ ] Para cada URL: buscar referencias hardcoded en `*.liquid` y `*.json`
- [ ] Usuario cambia slugs en Admin → Pages (Shopify crea 301s automáticamente)
- [ ] Verificar cada 301: `curl -I https://d016j0-nz.myshopify.com/pages/old-slug`
- [ ] Commit cualquier cambio de código

---

### Fase 3 — Sobre Paramahamsa Vishwananda (5 secciones naranjas)

**Template:** `templates/page.master.json` ya existe. Solo añadir secciones.

- [ ] **Eventos con Él** — comprobar si `sections/Seccion__upcoming-events.liquid` se puede reutilizar con filtro `tag:guruji`
- [ ] **Festivales** — lista de eventos tipo festival
- [ ] **Peregrinajes** — bloque estático o lista de eventos tipo peregrinaje
- [ ] **Lo que otros dicen** — carrusel Swiper de testimonios (buscar primero si ya existe)
- [ ] **Darshan en Lanzarote 2026** — banner CTA que apunta a `/pages/darshan-lanzarote-2026`
- [ ] Para cada sección: añadir a `order` array en `page.master.json`, verificar en dev, commit individual

---

### Fase 4 — Nueva página: Rezar por el mundo

- [ ] Crear `templates/page.pray-for-the-world.json`
- [ ] Crear 9 secciones (ver lista en "Páginas nuevas" arriba)
- [ ] La sección "Enviar nombres" reutiliza el embed de Klaviyo
- [ ] Crear página en Admin, slug `/pages/rezar-por-el-mundo`
- [ ] Verificar en dev, commit

---

### Fase 5 — Templos ✅ COMPLETADO (2026-04-29)

Ambas páginas ✅ confirmadas teal en Figma.

- [x] `/pages/templo-lanzarote` publicada
- [x] `/pages/templo-malaga` publicada
- [x] `/pages/templos` (hub) publicada y links a templos individuales funcionando

---

### Fase 6 — Darshan landing 🔒 Bloqueada

Esperar a que se resuelvan las decisiones en `darshan.md` (capacidad, precios, política de reembolso, activación de Shopify Payments).

Cuando se desbloquee:
- [ ] Crear `templates/page.darshan.json`
- [ ] 6 secciones: Portada, Próximos eventos, Sobre Darshan, Cómo funciona, Beneficios, Reseñas
- [ ] Integrar `sections/section__ticket-tier.liquid` (4 tiers ya implementados)
- [ ] QR code — seleccionar API (ver `darshan.md`)

---

### Fase 7 — Migrar directorios a Metaobjects ✅ Profesores completado (2026-04-29) | Sanghas pendiente

**Por qué:** Los mapas de profesores y sanghas tienen los datos hardcodeados en JavaScript dentro del Liquid — añadir un nuevo profesor o sangha requiere tocar código. La solución es Shopify Metaobjects: el equipo puede gestionar el directorio entero desde Admin → Contenido → Metaobjects, sin código.

**Archivos afectados:**
- `sections/section__profesores-map.liquid` — datos hardcodeados en `var profesores = [...]`
- `sections/section__sangha-map.liquid` (o equivalente) — misma situación

**Tareas:**
- [x] Crear definición de Metaobject `profesor` en Admin (8 campos: name, city, lat, lng, skills, telegram_url, photo, active)
- [x] Actualizar `section__profesores-map.liquid`: array hardcodeado reemplazado por loop Liquid + filtro URL `?practica=slug`
- [x] Migrar datos de profesores existentes a Admin → Metaobjects
- [ ] Crear definición de Metaobject `sangha` en Admin (pendiente)
- [ ] Actualizar el mapa de sanghas con el mismo patrón (pendiente)
- [ ] Migrar datos de sanghas a Admin → Metaobjects (pendiente)

> Una vez hecho, cualquier miembro del equipo puede añadir/editar/borrar profesores y sanghas desde Admin sin tocar código.

---

### Fase 8 — "Encuentra tu profesor" (filtros por práctica)

- [ ] Leer `templates/page.profesores.liquid` — identificar qué filtros faltan
- [ ] Añadir chips de filtro por práctica (AKY, Om Chanting, BSN…)
- [ ] Leer filtro de URL param (`?practica=aky`) al cargar la página
- [ ] En páginas de práctica (AKY, Om Chanting, BSN): añadir link con param al mapa de profesores
- [ ] Verificar en dev, commit

---

### Fase 8 — Páginas pequeñas / especulativas

| Tarea | Descripción | Esfuerzo |
|-------|-------------|----------|
| 8.1 Suscríbete | Single Klaviyo form embed | ~1 h |
| 8.2 Contacta con Swami Akash | Formulario de contacto (infraestructura existe) | ~1 h |
| 8.3 Haz una donación | Landing que envuelve `page.give.json` con copy de marketing | ~2 h |
| 8.4 Adopta un deity | ⭐ Nuevo — validar modelo stakeholders primero | ~3-4 h |
| 8.5 Bhakti Marga España | 3 secciones: "Sobre los swamis", "Sobre Swami Akash", "Contacta con él" | ~2 h |
| 8.6 Todos los eventos con Él | Colección o página listado | ~1-2 h |
| 8.7 Darshan Lanzarote 2026 | TBD — cuando se confirmen detalles | TBD |

---

## 🔗 Archivos relacionados

- `needs.md` — estado actual y bloqueantes de lanzamiento
- `darshan.md` — spec técnica del producto Darshan
- `admin-url-changes.md` — 21 URLs que migrar antes del lanzamiento
- `legal.md` — requisitos legales (RGPD, cookies, consentimiento)
