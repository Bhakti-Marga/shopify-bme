# Push SEGURO al theme live.
#
# Ignora config/settings_data.json para que el push NUNCA sobrescriba el
# contenido editado desde el admin (fotos de secciones, texto legal del footer,
# redes sociales, títulos de secciones, etc.).
#
# Flujo correcto:
#   - Editas CÓDIGO (sections/snippets/assets) en local  ->  .\push.ps1  (sube)
#   - Editas CONTENIDO en el admin de Shopify            ->  shopify theme pull  (baja a git)
#
# Si necesitas autenticarte con el token de Theme Access, añade:
#   --password $env:SHOPIFY_THEME_TOKEN
# (no lo escribas aquí en claro: el token es un secreto).

shopify theme push `
  --store d016j0-nz.myshopify.com `
  --theme 183370088792 `
  --allow-live `
  --ignore config/settings_data.json
