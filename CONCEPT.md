# seedhammer.studio · Landing page concept

Doc SHS-CONCEPT-01 · Rev 1 · 2026-08-13 · Direction: **TRIPLE ZERO**
Rendered version: https://claude.ai/code/artifact/2d02ac3a-6b6b-45d4-a0dd-12c7e3f7e700 (includes the live hero mock)

Quality bar: a page an agency would quote 21K for. Subject: the SeedHammer EDITION
firmware fork (Gangleri42/seedhammer) and SeedHammer Studio (Gangleri42/studio).
Not an official SeedHammer project; the machine is built and sold at seedhammer.com.

## The idea

The page reports, it doesn't advertise. The fork's best marketing is its bench
data: circle distortion driven from 2.89% to 0.000%, a 973-character descriptor
engraved and read back with zero errors, the machine's real firmware (about 8.7 MB of WebAssembly) running in the visitor's browser. So the page borrows the
one genre this audience already trusts, the instrument datasheet, produced at
full agency polish. Every claim carries a number; every number carries a repo path.

Chosen from three independently developed directions scored by three judges
(optics / conversion / craft): the bench report won optics 9 and craft 9; the
atelier direction won conversion 9 and its conversion mechanics were grafted on
(category kicker, CTA microline, proof rail under the hero, Open Studio three
times). From the dark "sovereign terminal" direction: serpentine draw order with
its source cite and strokes cooling brass to ink.

## Signature element

The hero headline **ENGRAVE ANYTHING.** typeset in the machine's actual
engraving font, generated from `glyphs.js` (the firmware's own font tables,
single-stroke SVG paths, monospace advance 4000, baseline 5000). It engraves
itself once on load, ~2.5 s, in serpentine row order (engrave/engrave.go:1912),
strokes cooling from brass to ink. Reduced motion gets the finished plate.
Plate drawn at true firmware geometry: 85 × 85 mm, margin 3 mm, no corner holes
(the firmware defines none).

## Design language

- **Color.** Paper `#FAF9F6` / ink `#17191B` / hairline `#DFDACE`; dark theme
  graphite `#131518` / steel `#C9CCCE`. One accent: brass `#A87710` (dark:
  `#D9A441`), pulled from the Studio icon's gold. Brass marks measured values,
  the live stroke, and the primary CTA. Nothing else.
- **Type, three voices.** Machine engraving font as inline SVG for display
  moments only. A self-hosted grotesk for prose (Switzer or General Sans;
  not Inter). A mono for every number (IBM Plex Mono or Commit Mono), tabular
  figures, measured values set slightly larger than the text around them.
- **Motifs.** Hairline rules, dimension lines with mm callouts, numbered figure
  captions with source paths, firmware-rendered screenshots framed as
  instrument screens, crosshair registration mark as section divider.
- **Motion.** The hero engrave is the single orchestrated animation. Everything
  else: max 200 ms scroll reveals, nothing loops.

## Page blueprint

0. **Masthead** — hammer mark (icon.svg), SEEDHAMMER EDITION, anchors
   (Studio / Firmware / Provenance), disclaimer as hairline strip.
1. **Hero** — kicker "A FIRMWARE FORK FOR THE SEEDHAMMER II", self-engraving
   headline, subhead, `[ OPEN STUDIO ]` + microline "The real firmware,
   compiled to WebAssembly. Runs in your browser. Zero hardware.",
   ghost link Firmware releases.
2. **Proof rail** — five brass numbers: 0.000% distortion · 973 chars, zero
   errors · 95/95 glyphs · ~1,500-char QR capacity · 253 of 256 bits yours.
3. **Studio showpiece** — "Boot the machine": click-to-load emulator embed
   (the ~8.7 MB wasm loads on demand behind a poster frame). Demo copy:
   press 1 for BACON, 1 then 3 for one wallet from both ends. Second CTA.
4. **Engrave anything** — vitrine of four plates (drawing, rich text, seed
   grid, npub) from firmware-rendered images; curves payload, six text sizes,
   small 85 × 55 plate and its printable jaw (3MF + STEP).
5. **Your hand draws the seed** — 253/3 bit split as a dimension-line diagram.
6. **Multisig in steel** — on-device M-of-N with first-address cross-check;
   the split: any signing quorum of steel rebuilds the wallet in Sparrow.
7. **Sign your own firmware** — sh2key ceremony; exactly three commands can
   burn fuses, each named, each behind readback + typed consent; 24-word steel
   backup restores to a byte-identical PEM. Ownership framing, never
   security-superiority.
8. **Built like an instrument** — deterministic nix builds, audits published
   in-repo with open findings and fixplan, docs doctor gating 41 byte-identical
   firmware-rendered screenshots.
9. **Ordering information** — machine from seedhammer.com · firmware free,
   public domain · Studio free, offline · jaw files in-repo.
10. **Footer** — third CTA, repo + edge links, "This page does not track its
    visitors." Optional wink: "This page has no framework, no tracker, and no
    invoice."

## Facts the page must honor

- Disclaimer above the fold; buyers routed to seedhammer.com; SeedHammer named
  only as the machine this software runs on. Courtesy note upstream pre-launch.
- Unsigned firmware said plainly: flashing means fusing your own boot key;
  official firmware stays bootable beside yours.
- The in-browser hardware-wallet emulator experiment is local-only, removed
  from the public Studio on 2026-07-21. The site never names it or its vendor;
  the copy linter enforces this.
- No corner holes on plate drawings; the firmware defines none.
- No rotting numbers (commit counts). Rev field carries the firmware sync tag.
- "Does not track its visitors" must be literally true.

## Build plan

- One hand-written static page in this repo: HTML + modern CSS + minimal
  vanilla JS (click-to-boot embed, scroll reveals). No framework. Fonts
  self-hosted woff2. Glyph SVG and screenshots generated from the firmware
  checkout at build time, pinned to the same sync tag Studio uses.
- Domain: apex serves the landing. Studio should follow onto the domain
  (/studio/ or app.); the NFC bridge allow-list and firmware install.sh both
  name the GitHub Pages origin today and need the new origin added. Until
  then, CTAs point at gangleri42.github.io/studio/.
- CI gates: copy linter (banned words, em-dash, claim-needs-number),
  Lighthouse 100s, transfer well under 300 KB before the optional emulator
  boot, both themes + reduced motion screenshot-tested, link check including
  deep links into repo docs.

## Next steps

1. Approve or adjust this direction.
2. Build pass 1: design system, hero with the real glyph pipeline, sections 0-2.
3. Build pass 2: Studio showpiece with click-to-boot embed, remaining sections.
4. CI + deploy to seedhammer.studio.
5. Decide Studio's move under the domain; courtesy note to upstream.
