# Website designs

The boards of the **Kaleem Website** design canvas: the page designs for kaleem.dev.

| Boards | What |
| --- | --- |
| `Main`, `Home-en`, `Home-mobile-ar` | Home page, first (dark) direction: Arabic desktop, English desktop, Arabic mobile |
| `Home-v2-*` | Home page, pastel direction (the one the site uses) |
| `Services-ar`, `Services-en`, `Services-v2-*`, `Services-v3-en` | Services page: dark, pastel, and the visual proposal the site uses |
| `Hero-A-case-file`, `Hero-B-before-after`, `Hero-C-big-type` | Case-study hero concepts (Alimran) |
| `Hero-Work`, `Hero-About` | Work and About page heroes |
| `Deptmaster-desktop`, `Deptmaster-mobile` | Deptmaster case study |
| `Phone-frame` | The phone frame component |
| `Artboard-*` | Scratch boards (notes only) |

`canvas/canvas.json` holds the layout (position and size of every board). The
boards are `.dc.html` files: open them in the canvas to see them rendered.

Screenshots inside the boards are uploads stored in the canvas (`/_blob/…`
links), so they show only there; the same images are in
`public/assets/illustrations/` and `public/assets/deptmaster/`.

These designs predate the new logo standard: their headers still draw the old
mark. The live site uses the new one (`design/logo/`).

To update this copy: read the canvas's `project/*.dc.html` and
`project/canvas.json` and save them into `canvas/`.
