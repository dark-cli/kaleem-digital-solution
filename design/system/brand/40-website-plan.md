# Website

kaleem.dev is live: a bilingual Astro site, static pages on Cloudflare, built the way we build for clients, so the site itself shows the method. `/` redirects to `/ar/` or `/en/` from the browser language and country.

## Sitemap (as built)

| Page | Path (`/ar/…` and `/en/…`) | Purpose |
| --- | --- | --- |
| Home | `/` | Liberate your data: services, work, from stuck to free, everything stays yours |
| Services | `/services/` | Six services, one method: an index of six tiles, the five steps, one illustrated card per service, hosting sizes, "Whatever we build, you receive" |
| Work | `/work/` | Gallery of case-study tiles + a dashed "Your project next" tile |
| Alimran | `/al-imran/` | Case study 01 |
| Deptmaster | `/deptmaster/` | Case study 02 |
| About | `/about/` | Mission, the name, offices, story, the six values |
| Contact | `/contact/` | Phone, WhatsApp, email, hours, offices |
| Free audit | `/audit/` | The free-audit form |

Header (night sky): logo (mark + "Kaleem" / «كليم» over "Digital Solutions" / «حلول رقمية») · Home · Services · Work · About · Contact · language switch (flat paper button) · "Book a free audit" (lilac, elevated). Below 672px: burger and drawer.
Footer (night sky): contact headline with a mint "Book a free audit" button, call, WhatsApp, email; hours and offices (Basra · Baghdad); logo and the same five links; © and the language switch.

## Home page, block by block

1. **Hero** — `peach` band. `display`: "Liberate your data." / «حرّر بياناتك.» `lead`: "We get your data out of old, locked systems and rebuild it on modern tech that you own." Buttons: mint "Book a free audit" + paper "See our work". Right: the illustration of a locked box setting tangled data free into a folder.
2. **What we do** — six clickable service cards (3 × 2), each in its pastel with a 40px line icon, title and one line. "All services →".
3. **Our work** — `paper-2` band ruled top and bottom: Alimran (text left, window right) then Deptmaster mirrored (dashboard window with the phone hanging over its corner). Each with three `stat` numbers and a pastel "Read the case study" button.
4. **From stuck to free** — left: "Stuck with…" and three problems with peach X badges; right: "…we get you out in five steps" on the numbered track, ending at the butter key "Free". "How we work, in detail →".
5. **Everything stays yours** — one `lilac` band: the five handover items with line icons. "Our values →".

## SEO and technical checklist

- `hreflang` pairs for every page; `lang`/`dir` on `<html>`.
- One `h1` per page; LocalBusiness structured data.
- Favicon: the Open Box mark, readable on light and dark tabs (SVG, ICO, 32 and 192px PNG).
- Target 95+ mobile PageSpeed.

## Still to do

- Real social handles (the footer links are placeholders).
- Photos of the team and of real camera and network installations.
- A self-hosted Newsreader 700 file (headings are currently synthesised bold).
- More projects for the Work gallery, with client permission.
