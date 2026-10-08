The Kaleem logo: the mark (a box open at its top-right corner, with one logo-yellow block stepping out through the door) followed by the lowercase wordmark.

- `lang="both"` (kaleem | كليم), `"en"` or `"ar"` to match the page, `"mark"` for favicons and tight spaces. `size` is the wordmark size in px (default 24).
- The mark is the logo standard's construction on a 110-unit grid: frame 89, walls 13, door and block 34, step out 21. One weight at every size.
- On paper the box is `ink`; inside a `.kl-board` element (the night-sky header and footer) it turns `chalk`. The block is always `logo-block` yellow, with no outline.
- This component is a quick inline logo for previews. For real use take the master files (lockups E and C, icons, favicon) from `design/logo/masters/` in the repo; their spacing is fixed by the standard.
- Clear space: the block's width on every side. Never recolour the block, outline it, rotate the mark or close the gap.
