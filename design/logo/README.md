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
| `standard.html` | The standard as one static page: the mark, lockups, colour, space and size, never, in use, the construction study and the A–E lockup study. Generated, do not edit. |
| `canvas/` | The source: the boards of the **Kaleem Logo** design canvas (`.dc.html` files and `canvas.json`). Edit the standard there. |
| `masters/` | The master files. SVG with the names outlined (no font needed), plus PNG exports. |
| `tools/` | The scripts that make `masters/`, `standard.html` and the site's logo data. |

## Master files

| File | Use |
| --- | --- |
| `kaleem-mark.svg`, `kaleem-mark-chalk.svg` | The mark alone, on light / on the night sky |
| `kaleem-mark-one-colour-ink.svg`, `-chalk.svg` | Single-ink print: stamps, engraving |
| `kaleem-lockup-e.svg`, `kaleem-lockup-e-chalk.svg` | Everyday lockup: site header and footer, cards, social, invoices. Min. 40px / 11 mm tall |
| `kaleem-lockup-e-one-colour-ink.svg` | Everyday lockup in one ink |
| `kaleem-lockup-c.svg`, `kaleem-lockup-c-chalk.svg` | Signature lockup with guide lines: About page, proposals, signage. Min. 96px / 25 mm tall |
| `kaleem-app-icon.svg` (+ `-512.png`, `-192.png`) | App icon: night-sky tile, mark at 65%, centred on grid point (50, 60) |
| `kaleem-app-icon-white.svg` | App icon on white |
| `kaleem-icon-square.svg` | Unrounded tile, for platforms that round corners themselves |
| `kaleem-avatar.svg` (+ `-400.png`) | Social avatar, for round crops |
| `favicon.svg` | Browser favicon: the bare mark, chalk on dark tabs |
| `kaleem-lockup-e-1048.png`, `kaleem-lockup-c-1048.png` | 2× PNGs of the lockups for documents and slides |

Colours: logo yellow `#f8d12f` (the block only), ink `#1f1f1f` (on light),
chalk `#eceee6` (on the night sky `#1d2320`). Clear space on every side: the
side of the yellow block.

## On the website

- `src/components/KaleemLogo.astro` draws the mark and both lockups from
  `src/data/logo.ts`, which `tools/masters.py` generates. Header and footer use
  lockup E in chalk; the About page uses lockup C.
- `public/favicon.svg`, `favicon.ico` (16, 32, 48), `favicon-32.png`,
  `favicon-192.png` and `apple-touch-icon.png` (180) come from the masters.
- `public/assets/logo/` holds copies of the SVG masters for linking.
- `public/assets/og-default.png` is the social share image (1200 × 630).

## Changing the logo

1. Edit the boards on the Kaleem Logo canvas and save their files into `canvas/`.
2. Rebuild the static page: `python3 design/logo/tools/build_static.py design/logo/canvas design/logo/standard.html`
3. If the geometry changed, update `tools/masters.py` and run it
   (`pip install fonttools uharfbuzz brotli`, then `python3 design/logo/tools/masters.py`).
   It downloads the two fonts into `tools/fonts/` (ignored by git), outlines the
   names, and rewrites `masters/*.svg` and `src/data/logo.ts`.
4. Re-export the PNGs from the SVGs at the sizes above and copy the favicon set
   into `public/`.

The lockup names sit where the canvas lockups place them (IBM Plex Mono 600 and
IBM Plex Sans Arabic 600, «كليم» stretched with 22 kashidas to the width of
"kaleem"); the numbers in `masters.py` were measured from the canvas.
