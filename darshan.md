# Darshan Lanzarote — Event Ticketing Tech Spec

## Event Overview
- **Event:** Darshan in Lanzarote
- **Date:** Sábado, 21 de noviembre de 2026
- **Estimated capacity:** ~800 seats
- **Venue:** Hotel Beatriz Costa & Spa, Costa Teguise, Lanzarote

## Ticket Tiers & Pricing

| Tier | Nombre en tienda | Price | Notas |
|------|-----------------|-------|-------|
| ~~VIP (Cortesía)~~ | ~~eliminado~~ | ~~€0~~ | ~~Eliminado del diseño final~~ |
| Primeras Filas | Primeras Filas | €108 | Filas 1-3 · inventario limitado (~20 plazas) |
| General | Entrada General | €10 | Resto del aforo |
| Menores de 18 | Menores de 18 | Gratis | Entrada gratuita, acompañante adulto obligatorio |

### Política de edades
- **Adultos (≥18 años):** pagan individualmente
- **Menores de 18 (incluidos):** entrada gratuita
- **No existe descuento de familia numerosa**

### Política de accesibilidad
- Minusválidos y acompañantes: **pagan independientemente** la entrada que elijan (sin descuento)
- Por deferencia: Crowd Control los ubicará en **fila 3 o 4, o esquinas delanteras**, independientemente del precio pagado
- Caso especial: hay 1 persona conocida en Darshans anteriores → siempre se coloca en primera fila

### Política de cancelación
- **Más de 14 días antes:** reembolso del 100%
- **7-13 días antes:** reembolso del 50%
- **Menos de 7 días:** sin reembolso

### Evento
- Las entradas se venderán como **inscripción a un evento de fiesta** (nombre TBD)
- Concepto: música, actividades, comida y la bendición de Paramahamsa Vishwananda
- Referencia: similar a lo realizado en Rumanía
- **PENDIENTE:** confirmar con el hotel si se permite servir comida

---

## Tech Spec — Confirmed Requirements

### 1. Platform
- **Shopify** (SEED - Production theme)
- Product with 3 variants (one per tier) + inventory tracking per variant

### 2. Purchase Flow
- Buyer selects tier + quantity → checkout → pays → Shopify sends order confirmation email (native)
- No seat selection, no seat map, no named per-attendee registration

### 3. Email Confirmation
- **Shopify native order confirmation email** sent immediately after purchase
- Contains: order number, tier, quantity, amount paid
- Language: Spanish
- No custom dev needed — Shopify handles this automatically

### 4. QR Code Delivery
- QR codes are **NOT generated at checkout**
- A few days before the event, an **external API** generates and sends QR codes to buyers
- One QR per order (not per seat) — TBD if one QR covers multiple tickets
- Delivery channel: email (via the external API)
- **Shopify role:** expose order data (order ID, email, tier, quantity) to the external API via Shopify Admin API or webhook

### 5. QR Code Validation at Entry
- **External QR scanner app** used at venue entrance
- Volunteers scan QR on their phone/device
- Validation happens in the external app (not Shopify)
- Shopify is not involved at the door

### 6. Payment Methods
- **Shopify Payments** — main method (NOT yet activated, needs setup by treasurer)
- **PayPal** — secondary method ✓ ENABLED
- Bhakti Marga España has a registered legal entity in Spain ✓
- Treasurer must provide for Shopify Payments: legal entity name, Spanish IBAN, ID verification

---

## Open Business Logic Questions (pending)
1. **Capacidad total:** TBD — @Anushadasi y @Sumanglidasi confirmarán
2. **Nombre del evento:** TBD — debe enmarcarse como "evento de fiesta" (música, actividades, comida, bendición)
3. **Comida en el hotel:** pendiente confirmar con el hotel
4. **¿Menores gratis necesitan inscripción?** — ¿hace falta ticket gratuito para el conteo de aforo?
5. **Canal de compra:** ¿solo online o también transferencia bancaria / presencial?
6. **CSV del año pasado:** ¿qué columnas/datos se recogieron?
7. **API/app de QR:** ¿cuál se usará? (pendiente de confirmar)

---

## Roadmap & Checklist

### Phase 1 — Business Logic ✅
- [x] Política de edades (adultos ≥18 pagan, menores gratis) ✓
- [x] Sin descuento familia numerosa ✓
- [x] Política accesibilidad (pagan igual, ubicación por deferencia) ✓
- [x] Estructura de precios: €108 primeras filas / €10 general / gratis menores ✓ — VIP eliminado
- [x] Concepto de evento definido (fiesta con música, actividades, comida, bendición) ✓
- [x] Política de cancelación definida (14d 100% / 7-13d 50% / <7d sin reembolso) ✓
- [ ] Capacidad total — confirmación pendiente (@Anushadasi / @Sumanglidasi)
- [ ] Nombre del evento
- [ ] Confirmar comida con el hotel
- [ ] ¿Menores gratis necesitan ticket/inscripción?
- [ ] Canal de compra (online only vs transferencia)
- [ ] Revisar CSV del año pasado
- [ ] Confirmar API/app de QR

### Phase 2 — Payment Setup (IN PROGRESS)
- [x] PayPal enabled ✓
- [ ] Activate Shopify Payments (treasurer action — legal entity + IBAN + ID)

### Phase 3 — Shopify Build (IN PROGRESS)
- [~] Producto Darshan existe en tienda (`/products/darshan`) con 3 variantes — falta `templates/product.darshan.json` en el repo
- [ ] Set inventory limits per variant (Primeras Filas: ~20 plazas)
- [x] Email de confirmación de pedido en español — Shopify nativo, funciona automáticamente ✓
- [ ] Asignar template `darshan` al producto en admin
- [ ] Test checkout end-to-end (purchase + confirmation email)

### Phase 4 — QR Integration
- [ ] Confirm QR API/app (pending details)
- [ ] Connect Shopify orders to QR API (via Shopify Admin API or webhook)
- [ ] Test QR generation and email delivery to buyer
- [ ] Test QR scan validation at entry with scanner app

### Phase 5 — Go Live
- [ ] Full end-to-end test (buy → email → QR → scan)
- [ ] Remove store password protection
- [ ] Monitor first sales

---

## Bugs conocidos — Formulario de producto (`/products/darshan`)

| # | Problema | Capa | Causa raíz | Dónde se arregla | Esfuerzo |
|---|---|---|---|---|---|
| 1 | Obliga a marcar TODOS los checkboxes | App: Infinite Options | Los campos están marcados como `required` en el admin de IO | Admin Infinite Options → producto Darshan → desmarcar "Required" en campos opcionales | Bajo — solo config |
| 2 | Menores de 18 no deberían marcar el checkbox de edad | App: Infinite Options | IO no detecta la variante seleccionada; muestra los mismos campos a todos | **Opción A:** IO Conditional Logic (feature de pago). **Opción B:** JS en `product__main.liquid` | A = Bajo · B = Medio |
| 3 | El carrito no carga tras añadir producto | Tema Shopify (probable) | Bug 1 bloquea el submit → el handler `s-product` en `theme.js` nunca dispara | Resolver bug 1 primero. Si persiste: revisar consola del navegador para el error JS exacto | Desconocido |

---

## Reference
- Previous year: WordPress site, CSV export of attendee data available
- Blog article del evento: `/blogs/events-1/darshan-blessing-lanzarote`
- Sección venue: `sections/section__venue-map.liquid`
- Template artículo: `templates/article.darshan.json`
