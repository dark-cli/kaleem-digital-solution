Kaleem (كليم) is an Iraqi digital solutions company with offices in Basra and Baghdad. We **liberate data**: we get it out of old, locked systems, clean it, and rebuild it on modern technology the client owns. Around that we build websites, apps and business systems, and install networks and security. The brand looks like **a teacher's notebook on a clean desk, under a night sky**: cream paper, soft pastels, a dark pen outline drawn by hand but kept tidy, and a starry board framing the top and bottom of every page. The promise: **your data, your systems, your freedom.** — **حرّر بياناتك.**

## Vision and idea

- **Vision:** Iraqi organisations truly own their digital infrastructure: free from single-vendor lock-in, from trapped data, and from the fear of upgrading. By freeing data and investing in open infrastructure, Kaleem helps Iraq build real digital independence. — أن تملك المؤسسات العراقية أنظمتها الرقمية ملكية حقيقية، ونساعد العراق على بناء استقلالية رقمية حقيقية.
- **The idea:** years of valuable data sit trapped in aging systems that their owners can't reach, build on or leave. We open the box. Every project goes **from stuck to free** in five steps and ends with every key in the client's name.
- **Hero line:** "Liberate your data." / «حرّر بياناتك.» Sub: "We get your data out of old, locked systems and rebuild it on modern tech that you own."
- **Closing line:** "Everything stays yours." / «كل شيء يبقى لك.»
- **The name:** كليم is "the one you speak with": the person you talk to, and who talks back. We speak the language of old, tangled systems and explain them plainly.
- **Why a notebook:** a teacher's notebook is where things get explained step by step. Hand-drawn outlines say "made by people who explain", while exact alignment and spacing say "engineered".
- **Why a night sky:** the header and footer are an open sky, the opposite of a locked box. It frames the page without competing with the content.

## Content fundamentals

- **Bilingual, always.** Every page exists in Arabic (`/ar/`, RTL) and English (`/en/`). The language switch sits in the header. Never mix the two languages inside one sentence.
- **Arabic register:** Modern Standard Arabic, plain and warm; no dialect on the site.
- **Voice:** "we" for Kaleem, "you" for the client. Short sentences, active verbs: liberate, extract, rebuild, hand over. Explain a technical term the first time, in plain words.
- **Casing:** sentence case for headings, buttons and eyebrows ("See our work", "Our work").
- **Numbers over adjectives**, and only measured ones: "Mobile PageSpeed 74 → 97", "230 automated tests", "3 months to go live". Never "10×" or uptime figures nobody measured.
- **No emoji, no exclamation marks, no stock clichés** (handshakes, hooded hackers, padlocks).
- **Honesty lines we keep:** we never promise a search ranking; we say who owns what after handover; we say when something costs extra.
- Real copy to model:
  - Problems: "An old system you can't leave" · "Data you can't reach" · "A slow, broken website". AR: «نظام قديم لا تستطيع مغادرته» · «بيانات لا تصل إليها» · «موقع بطيء ومعطّل».
  - CTA: "Book a free audit" / «احجز تقييماً مجانياً»; secondary "See our work" / «شاهد أعمالنا».
  - Services lede: "Six services. One method." / «ست خدمات. وطريقة واحدة.»

## Colour

- **One theme: Paper.** Every page is `paper` with its pencil-speck texture. The site has no dark mode; the night sky is a frame, not a theme.
- **One pastel per block.** A section is either paper or one pastel fill (`peach` hero, `paper-2` work band, `lilac` keep band). Never two pastels as section backgrounds next to each other.
- **One colour = one service**, everywhere it appears (card, tag, button, illustration): `butter` The Jailbreak · `sky` Websites & web apps · `peach` Mobile apps · `mint` Management & store systems · `apricot` Networks & security · `lilac` Consulting & training.
- Text is always `ink` (or `ink-muted` for leads, eyebrows and labels) on paper and on every pastel. Pastels are fills, never text colours.
- Buttons take the pastel of what they lead to; the hero's primary is `mint`, the header CTA `lilac`, a neutral second action `paper`.
- `board` (with the starfield) is for the header, footer, window chrome bars and phone rails only. On it, text is `chalk` / `chalk-muted` / `chalk-dim`, focus is `sky`.
- Links in running text on paper are `link`; on pastel bands, a link is `ink` 600, underlined with a 6px offset, followed by an arrow that flips in RTL ("All services →").

## Typography

- **Newsreader** (serif, `serif`) for display and headings, weight 700; Arabic swaps to **Amiri** 700 (`serif-ar`).
- **IBM Plex Sans** (`sans`) for body; **IBM Plex Sans Arabic** (`arabic`) on Arabic pages.
- **IBM Plex Mono** (`mono`) for proof numbers, step numbers, meta labels and the wordmark. On Arabic pages mono labels swap to Plex Sans Arabic, no caps, no tracking.
- Hero `display`; sections `heading-1`; bands `heading-2`; hero paragraph `lead`; cards `card-title` + `body-sm`; text `body`; numbers `stat`.
- Arabic runs taller: line-height 1.9–1.95 for body, 1.22 for headings, never letter-spacing.
- **Font files** (`fonts/`, copied from the site's `public/fonts/`): Newsreader 400, IBM Plex Sans 400, IBM Plex Mono 400 and 500 (basic Latin subsets), IBM Plex Sans Arabic 400/500/600 and Amiri 400/700 (Arabic subsets). The site also has latin-ext subsets, left out here because the system can't scope a file to a character range.
- **Missing weights:** the site has no Newsreader 700 file (its 700 headings are synthesised by the browser), and no Plex Sans 600/700 or Plex Mono 600 file (its `fonts.css` points those weights at the 400 file; the page also loads them from Google Fonts). The components here fill the same gaps from Google Fonts. Add the real files to match this spec exactly.

## Layout

- Container max `page-max` (1280px) with `gutter-desktop` sides (80px), `gutter-mobile` (16px) below 672px.
- Breakpoints: 1056px (hero stacks, cards 2 across) and 672px (one column, vertical step track).
- Spacing only from `space-1`…`space-11`. Sections: `space-10` (88px) top and bottom; 56px on mobile.
- Section rules are 2px `ink` lines, like a pen ruling the page.
- RTL: mirror everything with logical properties. Numbers, code and the Latin wordmark stay LTR (`<bdi>`).

## The sketch

- **Sketch card (`.sk`):** 2px `ink` border, `sketch-radius` (uneven corners), `shadow-sketch` (a second pen line 4px down-right), `space-7` padding, `space-4` child rhythm.
- **Lift:** clickable cards and elevated buttons rise up-left 4px on hover/focus and the offset grows (`shadow-sketch-lift`, `shadow-button-lift`); they press back 1px on click. 140ms, `cubic-bezier(0.2, 0.9, 0.3, 1.2)`. Off under `prefers-reduced-motion`.
- **Two buttons:** elevated `.skb` for primary actions, flat `.fbtn` for secondary and toolbar actions. Both 52px tall, 17px/600, any pastel fill.
- **Window widget:** a sketch card with a 40px night-sky chrome bar (peach and butter dots) framing a screenshot. Every product screenshot sits in one; phone screenshots go in a `PhoneFrame`.
- **Five-step track:** numbered 50px circles on a 3px `ink` line (Audit → Extract & clean → Build → Hand over → Support), ending in a `butter` key labelled "Free".
- **Texture:** the pencil-speck `paper` texture and the `dust` overlay are pure CSS (prime-sized radial-gradient tiles); no image files.

## Logo

The full standard lives in the repo, in `design/logo/` (open `standard.html`); the master files are in `design/logo/masters/`.

- **The idea:** someone walking out of a box. The frame is the box, the open corner is the door, the yellow block is you, mid-step.
- **The mark** is built on one rule, each part is the one before it divided by φ; on a 110-unit grid: frame 89, wall run 55, door and block 34, step out 21, wall thickness 13. Symmetric across the diagonal through the door; the whole mark is a 110 × 110 square; one weight from a 16px favicon to a sign.
- **Colours:** `logo-block` yellow (#f8d12f) for the block only; box and name in `ink` on light grounds, `chalk` on the night sky. One-colour versions use ink or chalk for everything.
- **Lockups** (both 2.618 : 1): E, the everyday lockup (mark | kaleem / كليم), 288 × 110 on the mark's grid: gaps of 13 (the wall) either side of a 5-wide rule (the letter stroke) from 21 to 110, names filling the 147 left. Site header and footer in chalk, cards, invoices, social; min. 40px / 11 mm tall. C, the signature lockup on a golden grid: square 200, names 200φ, mark 123.6 (square ÷ φ), one padding of 38.2, guide lines 2.13 (wall ÷ φ⁴). About page, proposals, signage, stickers and badges; min. 96px / 25 mm. Each has an Arabic version for Arabic pages: the mirror layout, mark on the right and «كليم» on top (the mark itself never flips).
- **Icons:** the app icon is the mark on a rounded tile (tile 170, mark 110, centred on grid point (50, 60)); the favicon is that tile in `sky` (#c6ddf0) with the ink mark, so it shows on light and dark browser tabs.
- **Clear space:** the block's width on every side. **Minimum:** the mark 16px / 5 mm.
- **Never:** recolour or outline the block, stretch or rotate the mark, close the gap, set the name in another face or case, or use the old mark (small pale block).

## Iconography

- 32×32 line icons drawn inline: 2px `ink` stroke, round caps and joins, no fill (`.ico`). One per service (open box, browser, phone, database, camera, speech bubble) and one per handover item (key, code, globe, document, team).
- Directional arrows flip in RTL. No emoji, no filled or 3D icons, no icon fonts.

## Imagery

- Real work only: screenshots of client systems in a WindowWidget or PhoneFrame, before/after pairs, real installations.
- Spot illustrations are hand-drawn in the same 2px ink line with pastel fills (the hero's locked box setting tangled data free into a folder).
- Never show personal, patient or client data in screenshots.

## Accessibility

- `ink` on paper and every pastel is 10.8:1 or more; `ink-muted` 5.8:1 or more; `chalk` on board 13.7:1.
- `link` blue passes only on `paper` (4.9:1): on pastels use underlined `ink`.
- Focus: 2px solid `focus` outline, 2px offset; `sky` on the board.
- Set `lang` and `dir` on `<html>`, and on any inline span in the other language.
