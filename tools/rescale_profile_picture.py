# rescale the profile picture to a standard sizes /resulutions
# profile picture is expected to be in images/gereon.png
from pathlib import Path
from PIL import Image
import sys
ROOT = Path(__file__).resolve().parents[1]
IMG_DIR = ROOT / 'images'
IMG_DIR.mkdir(parents=True, exist_ok=True)
SOURCE_IMG = IMG_DIR / 'gereon.png'
if not SOURCE_IMG.exists():
    print(f"Source image '{SOURCE_IMG}' not found. Please add the profile picture there.")
    sys.exit(1)
TARGET_SIZES = [64, 128, 256, 512]
for size in TARGET_SIZES:
    with Image.open(SOURCE_IMG) as img:
        img = img.convert("RGBA")
        img_resized = img.resize((size, size), Image.LANCZOS)
        out_path = IMG_DIR / f'profile_picture_{size}x{size}.png'
        img_resized.save(out_path)
        print(f"WROTE {out_path}")
print("Done rescaling profile pictures.")
