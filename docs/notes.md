# Notes

Open decisions and reminders that don't belong to a single file.

## Al-Imran case study: "Before" links

The "Before" windows on `/al-imran/` link straight to the old site
(alimranmed.com), which is still online:

| Window   | Old page                              |
|----------|---------------------------------------|
| Homepage | https://alimranmed.com/               |
| Articles | https://alimranmed.com/brain-tumor/   |
| Library  | https://alimranmed.com/rtms/          |

Don't use the Wayback Machine: it is blocked in Iraq.

When the old site goes offline, cache these pages and host the copies
ourselves (e.g. under `/archive/alimranmed/`), then point the links there.

## Al-Imran case study: PageSpeed numbers

The results table quotes Google PageSpeed Insights, mobile:

|                          | Old (alimranmed.com) | New (alimran.clinic) |
|--------------------------|----------------------|----------------------|
| Performance              | 74                   | 97                   |
| Largest Contentful Paint | 4.9 s                | 2.1 s                |
| First Contentful Paint   | 3.5 s                | 1.1 s                |
| Accessibility            | 96                   | 100                  |
| Best Practices           | 92                   | 100                  |
| SEO                      | 92                   | 100                  |

What the page says, and where each part comes from:

- "Pages open in under a second instead of 3 to 10": observed by us in
  real use. The new site is cached on Cloudflare and swaps pages without
  a full reload (after the first page, the next one downloads ~20 KB).
  The old site reloaded every page in full, including going back.
- "Mobile PageSpeed: 74 → 97": the reports below. They are the supporting
  proof, not the headline: PageSpeed emulates a slow phone and doesn't
  capture the full-page reloads, so it undersells the difference.
- Don't claim "10×" or uptime percentages: nothing measured backs them.

Reports (linked from the page):

- Old: https://pagespeed.web.dev/analysis/https-alimranmed-com/r6lyy9qjqs?form_factor=mobile
- New: https://pagespeed.web.dev/analysis/https-alimran-clinic/5mz18s71ut?form_factor=mobile

Saved reports expire after a while. Re-run both and update the links and
numbers if they stop opening.

## Sky tuner

`src/components/StarfieldControls.astro` shows a ✦ tuning panel only under
`npm run dev`. It is not in the built site. Copy the values you settle on
into `P` in that file.

## Work page: hero vs gallery (for later)

Today the Work page is a compact header plus a gallery: one tile per
project (screenshot, story, tags) and a dashed "Your project next" tile
that links to the audit form. New case studies are new tiles.

Once there are enough projects (roughly five or more), switch to:

- **Hero** shows the best project: its screenshot in a window beside the
  page's promise, as in the "Work page hero" artboard on the design canvas.
- **Body** is the gallery of all the other projects.

Don't do this with only one or two projects: the hero and the gallery
would show the same work twice.

The same rule applies to case-study pages: the hero stays compact, and
before/after screenshots live in their own section ("Every page
transformed"), not in the hero.

## Deptmaster: adding screenshots

The Deptmaster page (`src/pages/[locale]/deptmaster.astro`) has two
screenshot lists at the top, `DASHBOARD` and `PHONE`, empty for now.

1. Put the files in `public/assets/deptmaster/` (PNG or JPG; the build
   makes the WebP versions).
2. Add one entry per image, with alt text (and an optional caption) in
   both languages.

What appears:

- `DASHBOARD[0]` becomes the hero window and the large window in
  "The dashboard"; the rest go in a two-column grid under it.
- `PHONE[0]` becomes the hero phone; all phone shots go in "In the field",
  each in a `PhoneFrame` (the phone version of `WindowWidget`).
- A section with an empty list doesn't render, so nothing half-finished
  ever goes live.
