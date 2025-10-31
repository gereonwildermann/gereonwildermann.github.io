"""
ARCHIVE: generate_favicons.py

This file was the original cairosvg-based favicon generator. It is kept
only for historical/reference purposes. A renamed, annotated version
`generate_favicons_cairosvg.py` is available for use when you have
the necessary native dependencies (cairosvg + working pyexpat).

If you accidentally run this file in an environment without the
dependencies you'll get a "MISSING_DEPENDENCY" or a pyexpat DLL error.
Prefer `tools/generate_favicons_pillow_only.py` for a portable generator.
"""

import sys

print("This script is archived. Use 'tools/generate_favicons_cairosvg.py' or 'tools/generate_favicons_pillow_only.py' instead.")
sys.exit(0)
