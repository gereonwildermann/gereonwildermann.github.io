import subprocess
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ICON_DIR = ROOT / "icon"
SVG = ICON_DIR / "favicon.svg"

INKSCAPE = r"C:\Program Files\Inkscape\bin\inkscape.exe"

sizes = [16, 32, 48, 64, 120, 128, 152, 180, 192, 256]

for s in sizes:
    out = ICON_DIR / f"favicon-{s}.png"
    subprocess.run([
        INKSCAPE,
        str(SVG),
        "--export-type=png",
        f"--export-width={s}",
        f"--export-height={s}",
        f"--export-filename={out}"
    ], check=True)
    print("WROTE", out)

# ICO creation
base = Image.open(ICON_DIR / "favicon-256.png")
base.save(ICON_DIR / "favicon.ico", format="ICO", sizes=[(s, s) for s in sizes])
print("WROTE", ICON_DIR / "favicon.ico")

print("Done")
