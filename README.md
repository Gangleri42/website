# seedhammer.studio

Landing page for SeedHammer EDITION (Gangleri42/seedhammer) and SeedHammer
Studio (Gangleri42/studio). Static: one HTML file, one stylesheet, one small
script. Concept in CONCEPT.md.

- `tools/gen_glyphs.py` typesets the hero in the machine engraving font from
  the Studio checkout's drift-guarded glyphs.js and injects it into
  index.html. `--check` fails if the committed SVG drifted.
- `tools/lint_copy.py` enforces the copy house rules (no em-dashes, no
  banned adjectives).
- `tools/check.sh` runs every gate: glyph drift, copy lint, asset
  references, 300 KB transfer budget.

Images under assets/img are the firmware's own renders, copied from the
firmware repo's docs/images (regenerated there by cmd/docs in CI).
Fonts: Switzer (Fontshare, ITF Free Font License) and IBM Plex Mono (OFL).
