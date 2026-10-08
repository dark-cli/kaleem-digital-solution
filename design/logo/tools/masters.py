"""Generate the Kaleem logo master files and the site's logo data.

    pip install fonttools uharfbuzz brotli
    python3 design/logo/tools/masters.py

Writes:
  design/logo/masters/*.svg   the master SVGs (names outlined, no font needed)
  src/data/logo.ts            the shapes the site's KaleemLogo component draws

The PNG exports (favicon.ico, favicon-*.png, apple-touch-icon.png, the
masters/*.png) are rasterised from these SVGs; see design/logo/README.md.

Geometry is the logo standard (design/logo/canvas/): the mark on a 110-unit
grid, lockups 524 x 200 with the names at the positions measured from the
canvas lockups, fitted to equal widths.
"""
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
from outline import Face, text_path  # noqa: E402

# IBM Plex Mono 600 (Latin) and IBM Plex Sans Arabic 600 (Arabic), from Google Fonts.
FONTS = {
    'mono600.woff': 'https://fonts.gstatic.com/s/ibmplexmono/v20/-F6qfjptAgt5VM-kVkqdyU8n3vAOwlBFhA.woff',
    'ar600.woff': 'https://fonts.gstatic.com/s/ibmplexsansarabic/v15/Qw3NZRtWPQCuHme67tEYUIx3Kh0PHR9N6YPi-OCRXMJ5Kw.woff',
}
FONT_DIR = os.path.join(HERE, 'fonts')
os.makedirs(FONT_DIR, exist_ok=True)
for name, url in FONTS.items():
    path = os.path.join(FONT_DIR, name)
    if not os.path.exists(path):
        urllib.request.urlretrieve(url, path)

INK, CHALK, YEL, SKY = '#1f1f1f', '#eceee6', '#f8d12f', '#1d2320'
BOX = 'M0 21H55V34H13V97H76V55H89V110H0Z'
AR = 'كلي' + 'ـ' * 22 + 'م'  # 22 kashidas: the Arabic name as wide as "kaleem"

mono = Face(os.path.join(FONT_DIR, 'mono600.woff'))
ar = Face(os.path.join(FONT_DIR, 'ar600.woff'))
NAMES = {
    'E_EN': text_path(mono, 'kaleem', 71.1, 382, 76.45, 255.95),
    'E_AR': text_path(ar, AR, 63, 382, 163.6, 255.91),
    'C_EN': text_path(mono, 'kaleem', 76.6, 363, 79.2, 275.75),
    'C_AR': text_path(ar, AR, 67.9, 363, 164.05, 275.78),
}


def mark(ink, block, tf=''):
    t = f' transform="{tf}"' if tf else ''
    return f'<g{t}><path d="{BOX}" fill="{ink}"/><rect x="76" y="0" width="34" height="34" fill="{block}"/></g>'


def svg(vb, body, label='Kaleem — كليم'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">{body}</svg>\n'


def lockup_e(ink, block):
    return svg('0 0 524 200', mark(ink, block, 'scale(1.81818)')
               + f'<rect x="217" y="8" width="9" height="184" fill="{ink}"/>'
               + f'<path d="{NAMES["E_EN"]}" fill="{ink}"/><path d="{NAMES["E_AR"]}" fill="{ink}"/>')


def lockup_c(ink, block):
    return svg('0 0 524 200', f'<rect x="1" y="1" width="522" height="198" fill="none" stroke="{ink}" stroke-width="2"/>'
               + f'<rect x="202" y="2" width="2" height="196" fill="{ink}"/><rect x="204" y="99" width="318" height="2" fill="{ink}"/>'
               + mark(ink, block, 'translate(40 38) scale(1.12727)')
               + f'<path d="{NAMES["C_EN"]}" fill="{ink}"/><path d="{NAMES["C_AR"]}" fill="{ink}"/>')


# Icons: a 170 tile around the 110 mark, centred on the grid point (50, 60).
TILE = '-35 -25 170 170'
MASTERS = {
    'kaleem-mark.svg': svg('0 0 110 110', mark(INK, YEL), 'Kaleem'),
    'kaleem-mark-chalk.svg': svg('0 0 110 110', mark(CHALK, YEL), 'Kaleem'),
    'kaleem-mark-one-colour-ink.svg': svg('0 0 110 110', mark(INK, INK), 'Kaleem'),
    'kaleem-mark-one-colour-chalk.svg': svg('0 0 110 110', mark(CHALK, CHALK), 'Kaleem'),
    'kaleem-lockup-e.svg': lockup_e(INK, YEL),
    'kaleem-lockup-e-chalk.svg': lockup_e(CHALK, YEL),
    'kaleem-lockup-e-one-colour-ink.svg': lockup_e(INK, INK),
    'kaleem-lockup-c.svg': lockup_c(INK, YEL),
    'kaleem-lockup-c-chalk.svg': lockup_c(CHALK, YEL),
    'kaleem-app-icon.svg': svg(TILE, f'<rect x="-35" y="-25" width="170" height="170" rx="38" fill="{SKY}"/>' + mark(CHALK, YEL), 'Kaleem'),
    'kaleem-app-icon-white.svg': svg(TILE, f'<rect x="-35" y="-25" width="170" height="170" rx="38" fill="#ffffff"/>' + mark(INK, YEL), 'Kaleem'),
    # Square, no rounding: for platforms that round the corners themselves
    # (apple-touch-icon, the 192px icon Google Search shows).
    'kaleem-icon-square.svg': svg(TILE, f'<rect x="-35" y="-25" width="170" height="170" fill="{SKY}"/>' + mark(CHALK, YEL), 'Kaleem'),
    'kaleem-avatar.svg': svg('-60 -50 220 220', f'<rect x="-60" y="-50" width="220" height="220" fill="{SKY}"/>' + mark(CHALK, YEL), 'Kaleem'),
    # Browser favicon: the bare mark; the box turns chalk on dark tabs.
    'favicon.svg': ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 110 110"><style>path{fill:#1f1f1f}'
                    '@media (prefers-color-scheme:dark){path{fill:#eceee6}}</style>'
                    f'<path d="{BOX}"/><rect x="76" y="0" width="34" height="34" fill="#f8d12f"/></svg>\n'),
}

out_dir = os.path.join(REPO, 'design', 'logo', 'masters')
for name, text in MASTERS.items():
    with open(os.path.join(out_dir, name), 'w') as f:
        f.write(text)

ts = ['/**',
      ' * Kaleem logo geometry: the single source for every logo on the site.',
      ' * Generated by design/logo/tools/masters.py from the logo standard',
      ' * (design/logo/). Do not edit by hand; change the standard and regenerate.',
      ' *',
      ' * The mark sits on a 110-unit grid (frame 89, door and block 34, step 21,',
      ' * wall 13). Lockups are 524 x 200; the names are outlined IBM Plex Mono 600',
      ' * and IBM Plex Sans Arabic 600, fitted to equal widths.',
      ' */',
      '',
      f'export const LOGO_INK = "{INK}";',
      f'export const LOGO_CHALK = "{CHALK}";',
      f'export const LOGO_YELLOW = "{YEL}";',
      '',
      '/** The box, as one filled shape (110 x 110 grid). */',
      f'export const MARK_BOX = "{BOX}";',
      '/** The block: x, y, size on the same grid. */',
      'export const MARK_BLOCK = { x: 76, y: 0, size: 34 } as const;',
      '']
for key, d in NAMES.items():
    ts.append(f'export const {key} =\n  "{d}";')
with open(os.path.join(REPO, 'src', 'data', 'logo.ts'), 'w') as f:
    f.write('\n'.join(ts) + '\n')

print(f'{len(MASTERS)} masters, src/data/logo.ts')
