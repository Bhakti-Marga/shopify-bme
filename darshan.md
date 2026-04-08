# Darshan Lanzarote — Event Ticketing Tech Spec

## Event Overview
- **Event:** Darshan in Lanzarote
- **Month:** November (year TBD)
- **Estimated capacity:** ~800 seats
- **Venue:** TBD (indoors/outdoors unclear)

## Ticket Tiers & Pricing

| Tier | Price | Quantity | Notes |
|------|-------|----------|-------|
| VIP (Cortesía) | €0 | Max 5 | Presidente federación + representantes institucionales de la isla. Si no se cubren → se venden a €108 |
| Primeras filas | €108 | Filas 1-3 menos VIPs (si 4 VIPs → 1 más a €108) | Capacidad exacta TBD tras Semana Santa |
| General | €10 | Resto del aforo | |
| Niños (≤17 años) | Gratis | — | Menores de 17 incluidos no pagan |

### Política de edades
- **Adultos (≥18 años):** pagan individualmente
- **Niños (≤17 años, incluidos):** entrada gratuita
- **No existe descuento de familia numerosa**

### Política de accesibilidad
- Minusválidos y acompañantes: **pagan independientemente** la entrada que elijan (sin descuento)
- Por deferencia: Crowd Control los ubicará en **fila 3 o 4, o esquinas delanteras**, independientemente del precio pagado
- Caso especial: hay 1 persona conocida en Darshans anteriores → siempre se coloca en primera fila

### Evento
- Las entradas se venderán como **inscripción a un evento de fiesta** (nombre TBD)
- Concepto: música, actividades, comida y la bendición de Paramahamsa Vishwananda
- Referencia: similar a lo realizado en Rumanía
- **PENDIENTE:** confirmar con el hotel si se permite servir comida

---

## Tech Spec — Confirmed Requirements

### 1. Platform
- **Shopify** (SEED - Production theme)
- Product with 4 variants (one per tier) + inventory tracking per variant

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
1. **Capacidad total:** TBD — @Anushadasi y @Sumanglidasi confirmarán semana después de Semana Santa
2. **Nombre del evento:** TBD — debe enmarcarse como "evento de fiesta" (música, actividades, comida, bendición)
3. **Comida en el hotel:** pendiente confirmar con el hotel
4. **¿Niños gratis necesitan inscripción?** — ¿hace falta ticket gratuito para el conteo de aforo?
5. **Canal de compra:** ¿solo online o también transferencia bancaria / presencial?
6. **Política de cancelación:** ¿hasta cuándo? ¿devolución total, parcial o no?
7. **CSV del año pasado:** ¿qué columnas/datos se recogieron?
8. **API/app de QR:** ¿cuál se usará? (pendiente de confirmar)

---

## Roadmap & Checklist

### Phase 1 — Business Logic (IN PROGRESS)
- [x] Política de edades (adultos ≥18 pagan, niños ≤17 gratis) ✓
- [x] Sin descuento familia numerosa ✓
- [x] Política accesibilidad (pagan igual, ubicación por deferencia) ✓
- [x] Estructura de precios: VIP cortesía / €108 primeras filas / €10 resto ✓
- [x] Concepto de evento definido (fiesta con música, actividades, comida, bendición) ✓
- [ ] Capacidad total — confirmación semana después de Semana Santa (@Anushadasi / @Sumanglidasi)
- [ ] Nombre del evento
- [ ] Confirmar comida con el hotel
- [ ] ¿Niños gratis necesitan ticket/inscripción?
- [ ] Canal de compra (online only vs transferencia)
- [ ] Política de cancelación/reembolso
- [ ] Revisar CSV del año pasado
- [ ] Confirmar API/app de QR

### Phase 2 — Payment Setup (IN PROGRESS)
- [x] PayPal enabled ✓
- [ ] Activate Shopify Payments (treasurer action — legal entity + IBAN + ID)

### Phase 3 — Shopify Build
- [ ] Create Darshan event product with 4 variants (VIP / Premium / Standard / Children)
- [ ] Set inventory limits per variant
- [ ] Configure order confirmation email template in Spanish
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

## Reference
- Previous year: WordPress site, CSV export of attendee data available
