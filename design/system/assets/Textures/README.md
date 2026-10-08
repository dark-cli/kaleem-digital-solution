# Textures (legacy)

These three files belong to the earlier Chalkboard direction and are **not used on kaleem.dev**. Keep them for reference only.

The live textures are pure CSS, defined in the site's `global.css`:

- `.paper` — `paper` (#faf6ee) with 14 layers of tiny `ink` specks (radial gradients at 18–32% opacity) on prime-number tile sizes (127px … 263px) so no repeat shows. The page background.
- `.dust` — the same specks without the colour, laid over any pastel (`class="bg-mint dust"`).
- `.board` — `board` (#1d2320) with chalk, butter, sky and pink specks. On the live site the header and footer are transparent over a WebGL starfield (`data-sky`) instead: one continuous night sky across every element that opts in.
