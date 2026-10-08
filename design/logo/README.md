# Kaleem logo

The logo standard and everything made from it. Open **`standard.html`** in a
browser to read the full standard.

The logo is someone walking out of a box: the frame is the box, the open
corner is the door, the yellow block is you, mid-step. Every dimension comes
from one rule, each part is the one before it divided by φ, so on a 110-unit
grid they are Fibonacci numbers:

| Part | Grid | Of the frame |
| --- | --- | --- |
| Frame (the box) | 89 | 1 |
| Wall run on each open edge | 55 | 0.618 |
| Door, and the block | 34 | 0.382 |
| Step out, and the gaps | 21 | 0.236 |
| Wall thickness | 13 | 0.146 |

The mark is symmetric across the diagonal through the door, the whole mark is
a 110 × 110 square, and one weight works from a 16px favicon to a sign.

## What is here

| Path | What |
| --- | --- |
| `standard.html` | The standard as one static page: the mark, lockups, colour, space and size, never, in use, the construction study and the open options. Generated, do not edit. |
| `canvas/` | The source: the boards of the **Kaleem Logo** design canvas (`.dc.html` files and `canvas.json`). Edit the standard there. |
| `masters/` | The master files. SVG with the names outlined (no font needed), plus PNG exports. |
| `archive/` | Earlier studies kept for reference: the A–E lockup study. |
| `tools/` | The scripts that make `masters/`, `standard.html` and the site's logo data. |

## The lockups

Both lockups are 2.618 : 1 (φ²), and every value comes from the mark or from φ.
The **Options** board (last in `standard.html`) keeps the alternatives that were
weighed; E2, C2 and the sky favicon were chosen in October 2026.

| | Lockup E · everyday | Lockup C · signature |
| --- | --- | --- |
| Size | 288 × 110, on the mark's grid | 523.6 × 200 (200 + 200φ) |
| Mark | 110, full height | 123.6 = the square ÷ φ, inset 38.2 |
| Divider | rule 5 wide (the letter stroke), from 21 to 110 (the box) | guide lines 2.13 = the wall ÷ φ⁴ |
| Spacing | 13 either side of the rule (the wall) | one padding, 38.2, around mark and names |
| Names | fill the 147 left; "kaleem" on line 55, «كليم» on line 97 | 247.2 wide, each centred in its row |

Both names are fitted by their ink (the visible letters), so they fill the
name area exactly.

**Arabic versions.** Each lockup has an Arabic version for Arabic pages and
Arabic documents: the mirror layout, with the mark on the right and «كليم» on
top. In E the two names swap rows inside the same text block, and the box
stays one door (34) from the rule: in English the open side faces the rule
(block 13 away, wall 34), in Arabic the solid wall does, so the Arabic E is
309 × 110. In C the square moves to the right; the mark sits the same way in
its cell and the names keep the 38.2 padding. The mark itself is never mirrored. On the site,
`KaleemLogo` picks the version from the page's language.

## Favicon

The app-icon tile in **sky** `#c6ddf0`, the website's pastel, with the ink mark:
it stands out on light and dark browser tabs, and blue sets the yellow block off
best. Rounded tile for tabs (`favicon.svg`, `.ico`, `-32.png`); square tile where
the platform rounds or crops the corners itself (`favicon-192.png`,
`apple-touch-icon.png`).

`tools/options.py` still draws the rejected options, for comparison.

## Master files

| File | Use |
| --- | --- |
| `kaleem-mark.svg`, `kaleem-mark-chalk.svg` | The mark alone, on light / on the night sky |
| `kaleem-mark-one-colour-ink.svg`, `-chalk.svg` | Single-ink print: stamps, engraving |
| `kaleem-lockup-e.svg`, `kaleem-lockup-e-chalk.svg` | Everyday lockup: site header and footer, cards, social, invoices. Min. 40px / 11 mm tall |
| `kaleem-lockup-e-one-colour-ink.svg` | Everyday lockup in one ink |
| `kaleem-lockup-c.svg`, `-chalk.svg`, `-one-colour-ink.svg` | Signature lockup with guide lines: About page, proposals, signage, stickers. Min. 96px / 25 mm tall |
| `kaleem-lockup-e-ar*.svg`, `kaleem-lockup-c-ar*.svg` | The Arabic versions of both lockups (same three colourings): mark on the right, «كليم» on top |
| `kaleem-app-icon-sky.svg` (+ `-512.png`, `-192.png`) | App icon in sky, the favicon's tile: mark at 65%, centred on grid point (50, 60) |
| `kaleem-app-icon.svg` (+ `-512.png`, `-192.png`), `kaleem-app-icon-white.svg` | App icon on the night sky, or on white |
| `kaleem-icon-square-sky.svg`, `kaleem-icon-square.svg` | Unrounded tiles, for platforms that round corners themselves |
| `kaleem-avatar.svg`, `kaleem-avatar-sky.svg` (+ `-400.png`) | Social avatar, for round crops |
| `favicon.svg` | Browser favicon: the sky tile |
| `kaleem-lockup-*-1048.png`, `kaleem-lockup-e-ar*-1124.png` | 400px-tall PNGs of the lockups, English and Arabic, for documents and slides |

Colours: logo yellow `#f8d12f` (the block only), ink `#1f1f1f` (on light),
chalk `#eceee6` (on the night sky `#1d2320`). Clear space on every side: the
side of the yellow block.

## On the website

- `src/components/KaleemLogo.astro` draws the mark and both lockups from
  `src/data/logo.ts`, which `tools/masters.py` generates. Header and footer use
  lockup E in chalk; the About page uses lockup C. English pages get the
  English version, Arabic pages the Arabic one (or pass `lang`).
- `public/favicon.svg`, `favicon.ico` (16, 32, 48), `favicon-32.png`,
  `favicon-192.png` and `apple-touch-icon.png` (180): the sky tile, from the masters.
- `public/assets/logo/` holds copies of the SVG masters for linking.
- `public/assets/og-default.png` and `og-default-ar.png` are the social share images (1200 × 630), English and Arabic.

## Changing the logo

1. Edit the boards on the Kaleem Logo canvas and save their files into `canvas/`.
2. If the geometry changed, update `tools/masters.py` and run it
   (`pip install fonttools uharfbuzz brotli`, then `python3 design/logo/tools/masters.py`).
   It downloads the two fonts into `tools/fonts/` (ignored by git), outlines the
   names, and rewrites `masters/*.svg`, `src/data/logo.ts` and the canvas
   components `canvas/Logo-E`, `Logo-C`, `Logo-E-ar` and `Logo-C-ar`.
3. Run `node design/logo/tools/exports.mjs` (needs Playwright with Chromium). It
   renders the PNGs and `favicon.ico`, and copies the favicon set,
   `public/assets/logo/` and the share images into `public/`.
4. Rebuild the static page: `python3 design/logo/tools/build_static.py design/logo/canvas design/logo/standard.html`
5. Copy the changed canvas components back to the Kaleem Logo canvas.

The names are IBM Plex Mono 600 and IBM Plex Sans Arabic 600, outlined, with
«كليم» stretched with 21 kashidas to the width of "kaleem", both fitted by ink.
