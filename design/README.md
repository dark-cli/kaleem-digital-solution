# Kaleem design

Everything the Kaleem brand and website are designed from, kept with the code.

| Folder | What | Edited in |
| --- | --- | --- |
| [`logo/`](logo/) | The logo standard: the mark's construction, lockups, colour, space, sizes, icons and favicon. Open `logo/standard.html`. Master files in `logo/masters/`. | The **Kaleem Logo** design canvas |
| [`system/`](system/) | The design system: brand book (`README.md`), tokens, brand documents (company profile, method and values, services, case studies, website plan) and the component library. | The **Kaleem** design system |
| [`website/`](website/) | The page designs for kaleem.dev (Home, Services, heroes, Deptmaster, phone frame) as canvas boards. | The **Kaleem Website** design canvas |

The canvases are where designs are drawn and reviewed; these folders are their
saved copies. After changing a canvas, copy its files back here (each folder's
README says how) so the repo stays the complete record. `system/` holds the design system's
`project/` files as they are; its fonts are the site's own (`public/fonts/`).

## How it reaches the site

- **Colours, type, spacing:** `system/tokens.json` mirrors `src/styles/global.css`, the site's single source for styles.
- **Logo:** `logo/tools/masters.py` writes `src/data/logo.ts`, which `src/components/KaleemLogo.astro` draws in the header, footer and About page. The favicon set and `public/assets/logo/` come from `logo/masters/`.
- **Fonts:** the site's own files in `public/fonts/` (the design system lists the same files).
