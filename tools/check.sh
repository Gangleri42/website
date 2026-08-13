#!/bin/sh
# All verification gates. Run from the repo root: tools/check.sh
set -e
cd "$(dirname "$0")/.."

python3 tools/gen_glyphs.py --check
python3 tools/lint_copy.py

# every local asset referenced by the page must exist
python3 - <<'EOF'
import re, sys
from pathlib import Path
html = Path("index.html").read_text()
missing = [ref for ref in re.findall(r'(?:src|href)="(?!https?:|#|mailto:)([^"]+)"', html)
           if not Path(ref).exists()]
css = Path("style.css").read_text()
missing += [ref for ref in re.findall(r'url\(([^)]+)\)', css)
            if not Path(ref.strip("'\"")).exists()]
if missing:
    sys.exit("missing local assets: " + ", ".join(missing))
print(f"local asset references resolve")
EOF

# transfer budget: everything a first paint can pull, before the optional emulator boot
python3 - <<'EOF'
import sys
from pathlib import Path
budget = 300_000
total = sum(p.stat().st_size for p in
            [Path("index.html"), Path("style.css"), Path("main.js"),
             *Path("assets").rglob("*") ] if p.is_file())
print(f"page weight {total:,} B of {budget:,} B budget")
if total > budget:
    sys.exit("over budget")
EOF

echo "all checks pass"
