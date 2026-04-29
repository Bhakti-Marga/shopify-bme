# Figma → Shopify: Plan de trabajo
> Extraído del sitemap de Figma (archivo `6tFHS9TCH3SRBhtaDUQhJ7`, sección `44:1436`)
> Fecha: 2026-04-28
> Última auditoría de templates: 2026-04-28
> Última actualización con análisis Figma: 2026-04-29

---

## Leyenda de colores del sitemap

| Color del icono | Significado | Acción requerida |
|----------------|-------------|-----------------|
| 🟠 Naranja (`#e95500`) icono + texto | Sección/página NO existe todavía | **Construir** |
| 🩵 Teal/cyan icono + texto gris | Sección ya existe en Shopify | Verificar y mantener |
| ⬛ Gris oscuro icono + texto gris | Sección planificada, estado incierto | Revisar/confirmar |
| 🟡 Dorado/ámbar icono | Enlace a producto de la tienda | Configurar enlace |
| 🟣 Morado icono (`#5c5a8c`) | Feature interactiva especial (mapa, directorio) | Feature compleja |

**Color de cabecera de la tarjeta = categoría de la página:**
- 🟦 Azul marino `#002656` = Categoría BM España / Paramahamsa Vishwananda
- 🩵 Teal `#00a3b2` = Categoría Comunidad / Prácticas
- 🟤 Dorado `#927244` = Sub-páginas de práctica específica
- 🟣 Morado `#5c5a8c` = Páginas de features especiales

---

## LEYENDA DE ESTADO (auditoría de templates)

| Estado | Significado |
|--------|-------------|
| ✅ | Template JSON/Liquid existe en `templates/` |
| 🟨 | Template existe pero hay que verificar si la página está asignada en Admin |
| 🔴 | No existe ni template ni página — construir desde cero |
| ⚠️ | Template existe en inglés — requiere revisión/traducción |

---

## RESUMEN EJECUTIVO

| Estado | Páginas |
|--------|---------|
| ✅ Templates confirmados (página o template existe) | ~24 |
| 🟨 Templates existen, verificar asignación en Admin | ~10 |
| 🔴 Páginas genuinamente nuevas por construir | 8 |
| ⚠️ Templates en inglés que requieren revisión | 5 |
| 🔮 Features interactivas nuevas | 2 |

> Actualizado 2026-04-29: templos confirmados ✅, hub "Templos" confirmado ✅, nueva página "Adopta un deity" 🔴 descubierta.

---

## 🔴 PÁGINAS GENUINAMENTE NUEVAS — No existe template

### 1. Rezar por el mundo
**URL sugerida:** `/pages/rezar-por-el-mundo`
**Color:** Teal (categoría comunidad)
**Estado:** 🔴 No existe template

Secciones a crear:
- [ ] Introducción
- [ ] Enviar nombres (formulario para enviar nombres a rezar)
- [ ] Youtube embed
- [ ] Reserva la fecha
- [ ] Sobre Guruji
- [ ] Sobre el mantra
- [ ] Project Mantra (enlace/widget)
- [ ] El poder de la oración
- [ ] El poder de la intención

---

### 2. Suscríbete
**URL sugerida:** `/pages/suscribete`
**Color:** Teal
**Estado:** 🔴 No existe template

Secciones a crear:
- [ ] Formulario de suscripción (Klaviyo embed)

---

### 3. Darshan (página de producto/landing)
**URL sugerida:** `/pages/darshan`
**Color:** Teal (borde `#e0d3c2` — categoría especial)
**Estado:** 🔴 No existe template (bloqueado por decisiones de negocio)

Secciones a crear:
- [ ] Portada/introducción
- [ ] Próximos eventos Darshan (lista de eventos)
- [ ] Sobre Darshan (qué es)
- [ ] Como funciona
- [ ] Beneficios
- [ ] Reseñas

> Nota: Ver `darshan.md` para spec completa de la página de producto Darshan con 4 niveles de tickets.

---

### 4. Darshan Lanzarote 2026
**URL sugerida:** `/pages/darshan-lanzarote-2026`
**Color:** Azul marino
**Estado:** 🔴 No existe template (pendiente de decisiones de negocio)

- [ ] Contenido pendiente de decisiones de negocio

---

### 5. Todos los eventos con Él
**URL sugerida:** `/pages/eventos-con-el` o colección filtrada
**Color:** Azul marino
**Estado:** 🔴 No existe template

- [ ] Página o colección de todos los eventos con Paramahamsa Vishwananda

---

### 6. Encuentra tu profesor (standalone)
**URL sugerida:** `/pages/encuentra-tu-profesor`
**Color:** Morado `#5c5a8c` — feature interactiva
**Estado:** 🔴 No existe template standalone (la página de profesores existe pero necesita filtros)

- [ ] Feature de mapa o lista de profesores con filtro (similar a mapa de sanghas ya construido)
> Reutilizar la infraestructura del mapa de sanghas/profesores (`templates/page.profesores.liquid`)

---

### 7. Cursos online (página listado)
**URL sugerida:** `/collections/cursos` o `/pages/cursos-online`
**Estado:** 🔴 No existe template de página de listado dedicado

- [ ] Página o colección de todos los cursos online disponibles

---

### 8. Adopta un deity ⭐ NUEVO
**URL sugerida:** `/pages/adopta-un-deity`
**Color:** Azul marino `#002656`
**Estado:** 🔴 No existe template — nueva concept descubierta en análisis Figma abril 2026

Concepto: adopción/patrocinio de deidades como feature de donación/engagement.

- [ ] Validar con stakeholders el modelo (precio, fulfillment, qué ofrece el "adoption")
- [ ] Crear template una vez confirmadas las decisiones de negocio
- [ ] 1 sección TBD (pendiente diseño final)

> Nota: Tarjeta con cabecera azul marino, 1 sección gris "TBD". Bloquear en fase 8 hasta que se defina el modelo.

---

## 🟡 PÁGINAS EXISTENTES CON SECCIONES QUE FALTAN

### Sobre Paramahamsa Vishwananda
**Template:** ✅ `templates/page.master.json` (18 secciones total — confirmado abril 2026)
**URL actual:** (verificar slug — asignar a página correcta en Admin)

Secciones existentes ✅ (13 teal/gray): Portada/intro, Misión, Amor incondicional, Fundador de BM, Cita de Guruji, Es Satguru/Kriya Yogi, Satgurus son especiales, Estadísticas, YouTube Insights from Guruji, Darshan, Síguele en Instagram, Síguele en X, Portada outro misión

**Secciones que FALTAN 🔴 (5 orange en Figma):**
- [ ] Eventos con Él (widget/lista de próximos eventos con Guruji)
- [ ] Festivales (sección con próximos festivales)
- [ ] Peregrinajes (sección con información de peregrinajes)
- [ ] Lo que otros dicen (testimonios/reseñas)
- [ ] Darshan en Lanzarote 2026 (banner/CTA prominente)

---

### Homepage
**URL:** `/`
**Total secciones Figma (confirmado abril 2026):** 12

Secciones existentes ✅ (10 teal):
1. Portada: Conócele / Sobre Él *(antes "Portada")*
2. Darshan
3. Eventos y Festivales
4. Encuentros locales
5. Cursos online
6. Visita un templo
7. Project Mantra
8. Rezar por el Mundo
9. Prácticas diarias Bhakti
10. Suscríbete

**Secciones ⚪ (estado incierto — gris en Figma, diseñadora las conserva sin decidir):**
- [ ] Nuestras creencias (node 62:7324 — confirmar si va o no)
- [ ] Nuestros valores (node 62:7325 — confirmar si va o no)

---

### Prácticas Bhakti
**Template:** ✅ `templates/page.path.json` (15 secciones — el más completo del proyecto)
**URL:** `/pages/practicas-bhakti` (verificar)

Secciones existentes 🩵: Yoga y meditación, Conocimiento, Rituales, Artes devocionales, Subscripción al boletín, Obtén tu curso gratuito de meditación

**Secciones estado incierto ⚪:**
- [ ] Video introducción (icono gris — añadir o confirmar)
- [ ] El camino Bhakti (icono gris)
- [ ] Prácticas diaria: 4 brazos (icono gris)

---

### Templos (hub)
**URL:** `/pages/templos` (verificar)
**Estado:** ✅ confirmada en Figma (abril 2026) — cabecera azul marino `#002656`, 3 secciones todas gray

Secciones existentes ✅: Portada/intro, Templo Lanzarote: Hari Hara, Templo Málaga: Bhava Narasimha

**Tareas:**
- [ ] Verificar que `/pages/templos` está publicada en Admin
- [ ] Verificar que los links a los dos templos individuales funcionan

---

### Calendario de eventos
**Template:** ✅ `templates/page.calendar.liquid`
**URL:** `/calendario` ✅ existe

**Sección ⚪:**
- [ ] Portada/introducción (texto/hero encima del calendario)
- [ ] "Encuentra un profesor" (mapa o lista con filtro) — reutilizar mapa de profesores

---

## ✅ PÁGINAS EXISTENTES — Solo verificar

Estas páginas están en el sitemap con todas las secciones en teal (existen):

| Página | Template | URL actual | Estado |
|--------|----------|-----------|--------|
| Calendario de eventos | `page.calendar.liquid` | `/calendario` | ✅ Funcional |
| Sanghas | `page.sangha-map.liquid` | `/pages/sanghas` | ✅ Con mapa |
| Profesores | `page.profesores.liquid` | `/pages/profesores` | ✅ Con mapa |
| Templo Lanzarote: Hari Hara | `page.templo-hari-hara.json` | `/pages/templo-lanzarote` | ✅ Confirmado teal en Figma (6 secciones) — verificar slug en Admin |
| Templo Málaga: Bhava Narasimha | `page.templo-bhava-narasimha.json` | `/pages/templo-malaga` | ✅ Confirmado teal en Figma (6 secciones) — verificar slug en Admin |
| Bhakti Marga España | `page.mission.json` | `/pages/bhakti-marga-espana` | 🟨 Verificar |
| El camino Bhakti | `page.path.json` | `/pages/practicas-bhakti` | 🟨 Verificar slug |
| Haz una donación | `page.give.json` | `/pages/donacion` | 🟨 Verificar |
| Puja | `page.request-a-puja.json` | `/pages/puja` | 🟨 Verificar |

---

## 📄 SUB-PÁGINAS DE PRÁCTICA — Auditoría de templates

Resultado de la auditoría: la mayoría YA tienen template. Verificar asignación en Admin y estado del contenido:

| Página | Template | Estado | Notas |
|--------|----------|--------|-------|
| Atma Kriya Yoga | `page.aky.json` | 🟨 Template existe | 8 secciones, verificar contenido |
| Om Chanting | `page.omc.json` | 🟨 Template existe | Encabezados en inglés — revisar |
| Babaji Surya Namaskar | `page.bsn.json` | 🟨 Template existe | 6 secciones |
| Project Mantra | `page.project-mantra.json` | 🟨 Template existe | 6 secciones |
| Puja | `page.request-a-puja.json` | 🟨 Template existe | 8 secciones |
| Canto de oraciones | `page.vedic-chanting.json` | 🟨 Template existe | 7 secciones |
| Kirtan: Canto devocional *(antes "Kirtan")* | — | 🔴 No encontrado | Crear o integrar en Artes Devocionales |
| Pintura de arte devocional *(antes "Pintura devocional")* | — | 🔴 No encontrado | Crear o integrar en Artes Devocionales |
| Yoga y Meditación | `page.y-m.json` | 🟨 Template existe | 9 secciones |
| Conocimiento | `page.knowledge.json` | 🟨 Template existe | 9 secciones |
| Rituales | `page.rituals.json` | 🟨 Template existe | 8 secciones |
| Artes Devocionales | `page.devotional-arts.json` | 🟨 Template existe | 5 secciones |
| Sri Yantra | `page.sri-yantra.json` | 🟨 Template existe | 7 secciones |
| Templo Lanzarote: Hari Hara | `page.templo-hari-hara.json` | ✅ Confirmado teal en Figma | 6 secciones (ver tabla páginas existentes) |
| Templo Málaga: Bhava Narasimha | `page.templo-bhava-narasimha.json` | ✅ Confirmado teal en Figma | 6 secciones (ver tabla páginas existentes) |

---

## ⚠️ TEMPLATES EN INGLÉS — Revisar/actualizar o eliminar

Estos templates existen pero están en inglés y pueden estar desactualizados:

| Template | Contenido | Acción |
|----------|-----------|--------|
| `page.all-programs.json` | "Bhakti Marga Programs" | Revisar si tiene equivalente en español o eliminar |
| `page.ashram.json` | "Shree Peetha Nilaya" | Revisar si aplica a BM España |
| `page.start-now.json` | "Start your Journey to Love" | Probable candidato a eliminar |
| `page.sunday-program.json` | "Bhakti Sundays" | Probable candidato a eliminar |
| `page.temple.json` | Generic English temple page | Usar templates de templo específicos en su lugar |

---

## 🛒 ENLACES A TIENDA — Secciones que linkan a productos

Identificadas en el sitemap con iconos dorados `#927244`:

| Sección | Producto en tienda |
|---------|--------------------|
| Bhagavad Gita: Lo esencial | Necesita producto en Shopify |
| Bhagavad Gita | Necesita producto en Shopify |
| Shreemad Bhagavatam | Necesita producto en Shopify |
| Otras publicaciones | Colección de libros |
| Libro de oraciones | Necesita producto en Shopify |

---

## 🔮 FEATURES INTERACTIVAS ESPECIALES

### Encuentra tu profesor (mapa/directorio)
- **Template actual:** `templates/page.profesores.liquid` ✅ ya existe
- Añadir filtros por práctica (AKY, Om Chanting, BSN, etc.)
- Aparece como enlace en las páginas de: AKY, Om Chanting, Babaji Surya Namaskar

### Encuentra tu Sangha (mapa/lista)
- **Template:** `templates/page.sangha-map.liquid` ✅ ya existe y funciona

---

## 📋 ORDEN DE PRIORIDAD SUGERIDO

### Fase 0 — Auditoría (completada ✅)
- [x] Cruzar templates existentes con sitemap de Figma
- [ ] Verificar en Shopify Admin qué páginas tienen template asignado correctamente

### Fase 1 — Lanzamiento (bloqueantes)
1. **Menú principal** — reordenar/actualizar en Shopify Admin (cero riesgo de código)
2. **21 URL slugs** — migrar a español (ver `admin-url-changes.md`)
3. **Verificar asignaciones** — confirmar que los ~10 templates 🟨 están asignados a páginas correctas en Admin

### Fase 2 — Completar páginas existentes
4. **Sobre Paramahamsa Vishwananda** — añadir 5 secciones naranjas faltantes
5. **Templates en inglés** — revisar y actualizar o eliminar los 5 templates ⚠️
6. **Páginas de templos** individuales — verificar slugs y contenido de Lanzarote y Málaga

### Fase 3 — Páginas nuevas prioritarias
7. **Rezar por el mundo** — página nueva completa (9 secciones)
8. **Suscríbete** — página nueva simple (formulario Klaviyo)
9. **Darshan** — cuando se desbloqueen las decisiones de negocio

### Fase 4 — Features y crecimiento
10. Sub-páginas de prácticas (verificar contenido de los 🟨 existentes)
11. **Encuentra tu profesor** — añadir filtros por práctica al template existente
12. **Conocimiento** — configurar links a productos de libros
13. **Darshan Lanzarote 2026** — cuando se confirmen detalles

---

## 🧭 NAVEGACIÓN — Estructura confirmada (análisis Figma abril 2026)

**Estructura de 6 items** extraída de los pills de nivel en el sitemap de Figma:

| # | Ítem principal | Contenido |
|---|---|---|
| 1 | Conoce al Maestro | Sobre Paramahamsa Vishwananda + columna Homepage |
| 2 | Prácticas Bhakti | Páginas de prácticas Bhakti |
| 3 | Experiencias locales | Sanghas, Templos, encuentros locales |
| 4 | Cursos online | Páginas de cursos online |
| 5 | Donaciones | Haz una donación, Adopta un deity |
| 6 | Tienda ↗ | Todos los productos ↗, Esenciales bhakti ↗, Libros y música ↗ |

> Nota: No existe diseño de UI de navegación en Figma. La nav se gestiona en Shopify Admin → Navigation → linklists. Los nombres anteriores son de los pills del sitemap.

---

## 🦶 FOOTER — Estado (análisis Figma abril 2026)

**No existe diseño de footer en Figma.** El archivo Figma contiene únicamente el diagrama del sitemap.

**Footer ✅ construido y funcional:**
- `sections/footer.liquid` — cuadrícula 12 columnas: 6 col nav (`footer_nav` linklist) + 5 col contacto/social
- Bloque de contacto: `contact_title` + `contact_body` (configurables en Admin)
- Redes sociales: Instagram, X, YouTube, Facebook, Flickr (`snippets/social-media-links.liquid`)
- Subfooter: selector de idioma + `subfooter_nav` linklist + copyright
- Todos los links son configurables en Admin (sin hardcode)

**Tareas pendientes (solo Admin — sin cambios de código):**
- [ ] Publicar páginas legales (Aviso Legal, Política de Cookies, Política de Privacidad)
- [ ] Añadir sus links al menú `subfooter_nav` en Admin una vez publicadas
- [ ] Añadir logo BM al footer (gap de contenido)
- [ ] Añadir CIF G76198209 / info asociación (gap de contenido)

---

## 🔗 Archivos relacionados

- `needs.md` — estado actual y bloqueantes de lanzamiento
- `darshan.md` — spec técnica del producto Darshan
- `admin-url-changes.md` — 21 URLs que migrar antes del lanzamiento
- `legal.md` — requisitos legales (RGPD, cookies, consentimiento)
