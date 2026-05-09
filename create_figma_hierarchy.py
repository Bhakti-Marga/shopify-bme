from PIL import Image, ImageDraw, ImageFont
import os

W, H = 900, 620
BG = "#F7F5F2"
img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Fonts — fallback to default if system font not found
def load_font(size, bold=False):
    candidates_bold = [
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/calibrib.ttf",
        "C:/Windows/Fonts/seguisb.ttf",
    ]
    candidates = [
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
    ]
    pool = candidates_bold if bold else candidates
    for path in pool:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

font_title   = load_font(28, bold=True)
font_section = load_font(18, bold=True)
font_label   = load_font(16)
font_sub     = load_font(13)
font_tiny    = load_font(11)

# ── Title ─────────────────────────────────────────────────────────────────────
draw.text((W//2, 30), "Figma Sitemap Color Hierarchy", font=font_title,
          fill="#1A1A1A", anchor="mm")
draw.text((W//2, 58), "BM España — Design file reference", font=font_sub,
          fill="#888888", anchor="mm")

DIVIDER_Y = 75
draw.line([(40, DIVIDER_Y), (W-40, DIVIDER_Y)], fill="#DDDDDD", width=1)

# ── Swatch helper ─────────────────────────────────────────────────────────────
SWATCH_W, SWATCH_H = 36, 36
RADIUS = 6

def rounded_rect(draw, xy, fill, radius=RADIUS):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill)

def row(draw, x, y, color, label, sublabel=""):
    rounded_rect(draw, [x, y, x+SWATCH_W, y+SWATCH_H], fill=color)
    draw.text((x + SWATCH_W + 14, y + 4), label, font=font_label, fill="#1A1A1A")
    if sublabel:
        draw.text((x + SWATCH_W + 14, y + 22), sublabel, font=font_tiny, fill="#777777")

# ── LEFT COLUMN: Header colors (page hierarchy) ───────────────────────────────
COL_L = 55
Y = 100

draw.text((COL_L, Y), "Page Card Header Color", font=font_section, fill="#333333")
draw.text((COL_L, Y+24), "→ indicates hierarchy level", font=font_sub, fill="#999999")
Y += 62

entries_left = [
    ("#002656", "Primary pages",           "e.g. Homepage, Sobre PV, Prácticas Bhakti"),
    ("#00a3b2", "Secondary pages",          "e.g. Rezar por el mundo, Darshan, Calendario"),
    ("#927244", "Tertiary pages",           "e.g. Atma Kriya Yoga, Om Chanting, BSN"),
    ("#5c5a8c", "Special interactive features", "e.g. Sanghas map, Profesores map"),
]

for color, label, sub in entries_left:
    row(draw, COL_L, Y, color, label, sub)
    Y += 52

# ── RIGHT COLUMN: Icon colors (section status) ────────────────────────────────
COL_R = 470
Y = 100

draw.text((COL_R, Y), "Section Icon Color", font=font_section, fill="#333333")
draw.text((COL_R, Y+24), "→ indicates implementation status", font=font_sub, fill="#999999")
Y += 62

entries_right = [
    ("#00a3b2", "Already exists in Shopify",   "Section is built and live"),
    ("#e95500", "Needs to be built",            "Not yet implemented"),
    ("#444444", "Planned / uncertain",          "Exists in design, needs review"),
    ("#927244", "Link to store product",        "Points to a Shopify product/collection"),
    ("#5c5a8c", "Special interactive feature",  "Map, directory, calendar widget"),
]

for color, label, sub in entries_right:
    row(draw, COL_R, Y, color, label, sub)
    Y += 52

# ── Vertical divider ──────────────────────────────────────────────────────────
MID_X = W // 2
draw.line([(MID_X, 85), (MID_X, H - 55)], fill="#E0E0E0", width=1)

# ── Footer ────────────────────────────────────────────────────────────────────
draw.line([(40, H-45), (W-40, H-45)], fill="#DDDDDD", width=1)
draw.text((W//2, H-25), "Source: Figma file 6tFHS9TCH3SRBhtaDUQhJ7  ·  Audited 2026-05-06",
          font=font_tiny, fill="#AAAAAA", anchor="mm")

# Save
out = "docs/figma-sitemap-color-hierarchy.jpg"
os.makedirs("docs", exist_ok=True)
img.save(out, "JPEG", quality=92)
print(f"Saved: {out}  ({W}x{H})")
