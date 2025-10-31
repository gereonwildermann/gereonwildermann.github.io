"""
generate_favicons_cairosvg.py

High-fidelity SVG rasterizer for favicons.

This script uses cairosvg + Pillow to rasterize the SVG `icon/favicon.svg`
into multiple PNG sizes and an ICO containing multiple sizes.

Prerequisites:
- Python with a working stdlib (pyexpat) and native dependencies.
- cairosvg
- Pillow

On some Windows/Conda installations pyexpat may fail to import (DLL errors).
If you get a "DLL load failed while importing pyexpat" error, prefer the
Pillow-only generator `generate_favicons_pillow_only.py` instead or fix your
Python/Conda installation (repair or create a fresh conda env).

Usage:
    python generate_favicons_cairosvg.py

This file is provided as an optional, higher-fidelity generator. If you do
not need exact SVG rendering, use the Pillow-only script instead.
"""

import sys
from pathlib import Path

try:
    import cairosvg
    from PIL import Image
except Exception as e:
    print('MISSING_DEPENDENCY', e)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
ICON_DIR = ROOT / 'icon'
SVG = ICON_DIR / 'favicon.svg'

if not SVG.exists():
    print('SVG_MISSING', SVG)
    sys.exit(3)

sizes = [16, 32, 48, 64, 128, 256]

print('Generating PNGs...')
for s in sizes:
    out = ICON_DIR / f'favicon-{s}.png'
    cairosvg.svg2png(url=str(SVG), write_to=str(out), output_width=s, output_height=s)
    print('WROTE', out)

# also create a 192-target for Android sized icon
if (ICON_DIR / 'favicon-192.png').exists():
    print('favicon-192 already exists')
else:
    cairosvg.svg2png(url=str(SVG), write_to=str(ICON_DIR / 'favicon-192.png'), output_width=192, output_height=192)
    print('WROTE', ICON_DIR / 'favicon-192.png')

print('Creating ICO...')
base = Image.open(str(ICON_DIR / 'favicon-256.png'))
base.save(str(ICON_DIR / 'favicon.ico'), format='ICO', sizes=[(s, s) for s in sizes])
print('WROTE', ICON_DIR / 'favicon.ico')

print('Done')
