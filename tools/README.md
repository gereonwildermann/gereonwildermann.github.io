Favicon generation tools
=======================

This folder contains small scripts to generate raster favicon fallbacks from
the source vector `icon/favicon.svg`.

Files
- `generate_favicons_pillow_only.py` (recommended):
  - Pure Pillow implementation that draws a gradient rounded square and the
    initials "GW". Works reliably without native XML dependencies.
  - Usage: `python tools/generate_favicons_pillow_only.py`

- `generate_favicons_cairosvg.py` (optional):
  - Uses `cairosvg` to rasterize the SVG -> PNG more faithfully (better SVG
    feature support). Requires cairosvg and a working Python installation
    (pyexpat native extension). On some Windows/Conda installs `pyexpat`
    may fail to import (DLL error). If that happens, use the Pillow-only
    generator or fix your Python environment.
  - Usage: `python tools/generate_favicons_cairosvg.py`

- `generate_favicons.py` (archived):
  - Kept as an archive and intentionally exits early. See the renamed
    `generate_favicons_cairosvg.py` for the working cairosvg script.

Recommendations
- For local, predictable generation use the Pillow-only script.
- If you need exact SVG rasterization (fonts, filters), try
  `generate_favicons_cairosvg.py` inside a fresh conda environment.
