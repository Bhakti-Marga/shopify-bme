# ES Locale Translations Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 142 missing Spanish translation keys to `locales/es.json` so the entire customer account area, product UI labels, cart labels, and accessibility strings render in Spanish.

**Architecture:** Single-file edit — merge missing keys into the existing `locales/es.json` JSON structure using a Node.js merge script. The script deep-merges translations without touching existing keys.

**Tech Stack:** Node.js (available in repo), Shopify Liquid theme (SEED v1.0.0)

---

### Task 1: Add All Missing Spanish Translations to `locales/es.json`

**Files:**
- Modify: `locales/es.json`

- [ ] **Step 1: Create the merge script**

Create a temporary file `scripts/merge-translations.js` at the repo root:

```js
const fs = require('fs');
const path = require('path');

const esPath = path.join(__dirname, '../locales/es.json');

// Strip block comment header before parsing
const raw = fs.readFileSync(esPath, 'utf8').replace(/^\/\*[\s\S]*?\*\/\s*/, '');
const es = JSON.parse(raw);

// Deep merge helper — only adds keys, never overwrites
function deepMerge(target, source) {
  for (const [k, v] of Object.entries(source)) {
    if (v && typeof v === 'object' && !Array.isArray(v)) {
      target[k] = target[k] || {};
      deepMerge(target[k], v);
    } else if (!(k in target)) {
      target[k] = v;
    }
  }
}

const additions = {
  "general": {
    "password_page": {
      "admin_link_html": "¿Eres el propietario de la tienda? <a href=\"/admin\" class=\"link underlined-link\">Inicia sesión aquí</a>"
    },
    "social": {
      "links": {
        "twitter": "Twitter",
        "facebook": "Facebook",
        "pinterest": "Pinterest",
        "instagram": "Instagram",
        "tumblr": "Tumblr",
        "snapchat": "Snapchat",
        "youtube": "YouTube",
        "vimeo": "Vimeo",
        "tiktok": "TikTok"
      }
    }
  },
  "date_formats": {
    "month_year": "%B %Y"
  },
  "accessibility": {
    "skip_to_text": "Ir al contenido",
    "error": "Error",
    "refresh_page": "Seleccionar una opción provoca una actualización completa de la página."
  },
  "blogs": {
    "article": {
      "blog": "Blog",
      "moderated": "Ten en cuenta que los comentarios deben ser aprobados antes de ser publicados."
    }
  },
  "onboarding": {
    "product_title": "Título de producto de ejemplo",
    "collection_title": "Nombre de tu colección"
  },
  "products": {
    "product": {
      "media": {
        "open_featured_media": "Abrir imagen destacada en la galería",
        "open_media": "Abrir imagen {{ index }} en la galería",
        "play_model": "Reproducir visor 3D",
        "play_video": "Reproducir vídeo"
      },
      "quantity": {
        "input_label": "Cantidad para {{ product }}",
        "increase": "Aumentar cantidad para {{ product }}",
        "decrease": "Reducir cantidad para {{ product }}"
      },
      "pickup_availability": {
        "view_store_info": "Ver información de la tienda",
        "check_other_stores": "Comprobar disponibilidad en otras tiendas",
        "pick_up_available": "Recogida disponible",
        "pick_up_available_at_html": "Recogida disponible en <span class=\"color-foreground\">{{ location_name }}</span>",
        "pick_up_unavailable_at_html": "Recogida no disponible actualmente en <span class=\"color-foreground\">{{ location_name }}</span>",
        "unavailable": "No se pudo cargar la disponibilidad de recogida",
        "refresh": "Actualizar"
      },
      "price": {
        "from_price_html": "Desde {{ price }}",
        "regular_price": "Precio normal",
        "sale_price": "Precio de oferta",
        "unit_price": "Precio unitario"
      },
      "vendor": "Proveedor",
      "video_exit_message": "{{ title }} abre el vídeo en pantalla completa en la misma ventana.",
      "xr_button": "Ver en tu espacio",
      "xr_button_label": "Ver en tu espacio, abre el artículo en ventana de realidad aumentada"
    },
    "modal": {
      "label": "Galería de medios"
    }
  },
  "sections": {
    "cart": {
      "subtotal": "Subtotal",
      "cart_error": "Se ha producido un error al actualizar tu carrito. Por favor, inténtalo de nuevo.",
      "taxes_and_shipping_policy_at_checkout_html": "Impuestos y <a href=\"{{ link }}\">envío</a> calculados al finalizar la compra",
      "taxes_included_but_shipping_at_checkout": "Impuestos incluidos. Envío calculado al finalizar la compra",
      "taxes_included_and_shipping_policy_html": "Impuestos incluidos. <a href=\"{{ link }}\">Envío</a> calculado al finalizar la compra.",
      "taxes_and_shipping_at_checkout": "Impuestos y envío calculados al finalizar la compra"
    },
    "featured_blog": {
      "onboarding_content": "Ofrece a tus clientes un resumen de tu entrada de blog"
    },
    "collection_template": {
      "max_price": "El precio más alto es {{ price }}",
      "product_count": {
        "one": "Mostrando {{ product_count }} de {{ count }} producto",
        "other": "Mostrando {{ product_count }} de {{ count }} productos"
      },
      "reset": "Restablecer",
      "use_fewer_filters_html": "Usa menos filtros o <a class=\"{{ class }}\" href=\"{{ link }}\">borra todos</a>"
    }
  },
  "customer": {
    "account": {
      "title": "Mi cuenta",
      "details": "Datos de la cuenta",
      "view_addresses": "Ver direcciones",
      "return": "Volver a los datos de la cuenta"
    },
    "account_fallback": "Cuenta",
    "activate_account": {
      "title": "Activar cuenta",
      "subtext": "Crea tu contraseña para activar tu cuenta.",
      "password": "Contraseña",
      "password_confirm": "Confirmar contraseña",
      "submit": "Activar cuenta",
      "cancel": "Rechazar invitación"
    },
    "addresses": {
      "title": "Direcciones",
      "default": "Predeterminada",
      "add_new": "Añadir nueva dirección",
      "edit_address": "Editar dirección",
      "first_name": "Nombre",
      "last_name": "Apellidos",
      "company": "Empresa",
      "address1": "Dirección 1",
      "address2": "Dirección 2",
      "city": "Ciudad",
      "country": "País/región",
      "province": "Provincia",
      "zip": "Código postal",
      "phone": "Teléfono",
      "set_default": "Establecer como dirección predeterminada",
      "add": "Añadir dirección",
      "update": "Actualizar dirección",
      "cancel": "Cancelar",
      "edit": "Editar",
      "delete": "Eliminar",
      "delete_confirm": "¿Estás seguro/a de que deseas eliminar esta dirección?"
    },
    "log_in": "Iniciar sesión",
    "log_out": "Cerrar sesión",
    "login_page": {
      "cancel": "Cancelar",
      "create_account": "Crear cuenta",
      "email": "Correo electrónico",
      "forgot_password": "¿Olvidaste tu contraseña?",
      "guest_continue": "Continuar",
      "guest_title": "Continuar como invitado",
      "password": "Contraseña",
      "title": "Iniciar sesión",
      "sign_in": "Iniciar sesión",
      "submit": "Enviar"
    },
    "order": {
      "title": "Pedido {{ name }}",
      "date_html": "Realizado el {{ date }}",
      "cancelled_html": "Pedido cancelado el {{ date }}",
      "cancelled_reason": "Motivo: {{ reason }}",
      "billing_address": "Dirección de facturación",
      "payment_status": "Estado del pago",
      "shipping_address": "Dirección de envío",
      "fulfillment_status": "Estado del pedido",
      "discount": "Descuento",
      "shipping": "Envío",
      "tax": "Impuestos",
      "product": "Producto",
      "sku": "SKU",
      "price": "Precio",
      "quantity": "Cantidad",
      "total": "Total",
      "fulfilled_at_html": "Enviado el {{ date }}",
      "track_shipment": "Rastrear envío",
      "tracking_url": "Enlace de seguimiento",
      "tracking_company": "Transportista",
      "tracking_number": "Número de seguimiento",
      "subtotal": "Subtotal"
    },
    "orders": {
      "title": "Historial de pedidos",
      "order_number": "Pedido",
      "order_number_link": "Número de pedido {{ number }}",
      "date": "Fecha",
      "payment_status": "Estado del pago",
      "fulfillment_status": "Estado del pedido",
      "total": "Total",
      "none": "Todavía no has realizado ningún pedido."
    },
    "recover_password": {
      "title": "Restablecer contraseña",
      "subtext": "Te enviaremos un correo electrónico para restablecer tu contraseña",
      "success": "Te hemos enviado un correo electrónico con un enlace para actualizar tu contraseña."
    },
    "register": {
      "title": "Crear cuenta",
      "first_name": "Nombre",
      "last_name": "Apellidos",
      "email": "Correo electrónico",
      "password": "Contraseña",
      "submit": "Crear"
    },
    "reset_password": {
      "title": "Restablecer contraseña",
      "subtext": "Introduce una nueva contraseña para {{ email }}",
      "password": "Contraseña",
      "password_confirm": "Confirmar contraseña",
      "submit": "Restablecer contraseña"
    }
  },
  "gift_cards": {
    "issued": {
      "remaining_html": "Saldo restante {{ balance }}"
    }
  }
};

deepMerge(es, additions);

// Preserve the original comment header
const header = `/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin language editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */\n`;

fs.writeFileSync(esPath, header + JSON.stringify(es, null, 2) + '\n', 'utf8');
console.log('Done. Keys written to locales/es.json');
```

- [ ] **Step 2: Run the merge script**

```bash
mkdir -p scripts
# move script into place then run
node scripts/merge-translations.js
```

Expected output: `Done. Keys written to locales/es.json`

- [ ] **Step 3: Validate the JSON is parseable**

```bash
node -e "
  const raw = require('fs').readFileSync('locales/es.json','utf8').replace(/^\/\*[\s\S]*?\*\//,'');
  JSON.parse(raw);
  console.log('Valid JSON');
"
```

Expected output: `Valid JSON`

- [ ] **Step 4: Verify key count increased**

```bash
node -e "
  const es = JSON.parse(require('fs').readFileSync('locales/es.json','utf8').replace(/^\/\*[\s\S]*?\*\//,''));
  const en = JSON.parse(require('fs').readFileSync('locales/en.default.json','utf8').replace(/^\/\*[\s\S]*?\*\//,''));
  function keys(o,p=''){return Object.entries(o).flatMap(([k,v])=>typeof v==='object'?keys(v,p?p+'.'+k:k):[p?p+'.'+k:k]);}
  const missing = keys(en).filter(k => !new Set(keys(es)).has(k));
  console.log('Missing keys remaining:', missing.length);
  if (missing.length > 0) missing.forEach(k => console.log(' -', k));
"
```

Expected output: `Missing keys remaining: 0`

- [ ] **Step 5: Delete the temporary script**

```bash
rm scripts/merge-translations.js
rmdir scripts 2>/dev/null || true
```

- [ ] **Step 6: Commit**

```bash
git add locales/es.json
git commit -m "feat: add 142 missing Spanish translation keys (customer area, cart, products, accessibility)"
```

---

### Verification Checklist (manual — after deploy to Shopify)

After running `shopify theme push`, spot-check these pages on the live store:

| Page | What to check |
|------|--------------|
| `/account/login` | "Iniciar sesión", "Correo electrónico", "Contraseña", "¿Olvidaste tu contraseña?" |
| `/account/register` | "Crear cuenta", "Nombre", "Apellidos" |
| `/account` | "Mi cuenta", "Historial de pedidos", "Ver direcciones", "Cerrar sesión" |
| `/account/addresses` | "Añadir nueva dirección", "Código postal", "País/región" |
| `/account/orders/[id]` | "Dirección de facturación", "Estado del pago", "Subtotal", "Total" |
| `/cart` | "Subtotal", "Impuestos y envío calculados al finalizar la compra" |
| Any product page | Quantity +/− button aria-labels (inspect element) |

---

*Plan saved: 2026-04-18*
