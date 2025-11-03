from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ICON_DIR = ROOT / 'icon'
ICON_DIR.mkdir(parents=True, exist_ok=True)

# Simple gradient background + initials generator using Pillow only
SVG_SOURCE = ICON_DIR / 'favicon.svg'

def draw_gradient_rounded(size, radius=8):
    w, h = size, size
    base = Image.new('RGBA', (w, h))
    draw = ImageDraw.Draw(base)
    # gradient from blue-ish to green
    for y in range(h):
        t = y / (h - 1)
        r = int(70 + (0 - 70) * t)
        g = int(100 + (135 - 100) * t)
        b = int(170 + (108 - 170) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    # rounded mask
    mask = Image.new('L', (w, h), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, w, h], radius=radius, fill=255)
    base.putalpha(mask)
    return base

def draw_initials(img, text='GW'):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    # try to use a common system font, fallback to default
    try:
        font = ImageFont.truetype('arial.ttf', size=int(w * 0.44))
    except Exception:
        font = ImageFont.load_default()
    # compute text size using textbbox for compatibility
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text(((w - tw) / 2, (h - th) / 2 - (w*0.03)), text, font=font, fill=(240,240,240,255))
    return img

sizes = [16, 32, 48, 64, 120, 128, 152, 180, 192, 256]

for s in sizes:
    img = draw_gradient_rounded(s, radius=max(2, int(s * 0.125)))
    img = draw_initials(img, 'GW')
    out = ICON_DIR / f'favicon-{s}.png'
    img.save(out)
    print('WROTE', out)

# create ICO with standard sizes (16, 32, 48, 64, 128, 256)
ico_sizes = [16, 32, 48, 64, 128, 256]
icons = [Image.open(str(ICON_DIR / f'favicon-{s}.png')) for s in ico_sizes]
icons[0].save(ICON_DIR / 'favicon.ico', format='ICO', sizes=[(s, s) for s in ico_sizes])
print('WROTE', ICON_DIR / 'favicon.ico')

print('Done (Pillow-only generator)')
