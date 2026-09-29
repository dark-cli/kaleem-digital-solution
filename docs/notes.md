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

Reports (linked from the page):

- Old: https://pagespeed.web.dev/analysis/https-alimranmed-com/r6lyy9qjqs?form_factor=mobile
- New: https://pagespeed.web.dev/analysis/https-alimran-clinic/5mz18s71ut?form_factor=mobile

Saved reports expire after a while. Re-run both and update the links and
numbers if they stop opening.

## Sky tuner

`src/components/StarfieldControls.astro` shows a ✦ tuning panel only under
`npm run dev`. It is not in the built site. Copy the values you settle on
into `P` in that file.
