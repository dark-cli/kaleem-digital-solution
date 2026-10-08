"""Generate the Kaleem logo master files and the site's logo data.

    pip install fonttools uharfbuzz brotli
    python3 design/logo/tools/masters.py

Writes:
  design/logo/masters/*.svg   the master SVGs (names outlined, no font needed)
  src/data/logo.ts            the shapes the site's KaleemLogo component draws

Then run exports.mjs for the PNG/ICO files and the site's favicon set.

Geometry is the logo standard (design/logo/canvas/): the mark on a 110-unit
grid; lockup E on the same grid (288 x 110), lockup C on a golden grid
(523.6 x 200). Every value is derived below; options.py draws the rejected
alternatives for comparison.
"""
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)

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

from options import PHI, mono, ar, natural, run, ar_text  # noqa: E402  (fonts are in place now)

INK, CHALK, YEL, NIGHT, SKY = '#1f1f1f', '#eceee6', '#f8d12f', '#1d2320', '#c6ddf0'
BOX = 'M0 21H55V34H13V97H76V55H89V110H0Z'


def r(v):
    v = float('%.3f' % v)
    return int(v) if v.is_integer() else v


def name(face, text, size, width):
    """A name outlined at the origin: its ink fills exactly `width` (stretched
    horizontally if needed), ink left edge at x 0, baseline at y 0.
    Returns the path and the ink top and bottom relative to the baseline."""
    adv = natural(face, text, size)
    _, (l, t, rr, b), _ = run(face, text, size, 0, 0)
    sx = width / (rr - l)
    d, (l2, t2, r2, b2), _ = run(face, text, size, -l * sx, 0, adv * sx)
    return d, t2, b2


def names(width):
    """Both names fitted to the same ink width: "kaleem" in IBM Plex Mono 600,
    «كليم» in IBM Plex Sans Arabic 600 at 0.886 of its size, stretched with
    kashidas (then a touch of horizontal scale) to the same width."""
    _, (l, _, rr, _), _ = run(mono, 'kaleem', 1, 0, 0)
    size = width / (rr - l)
    en = name(mono, 'kaleem', size, width)
    text, n = ar_text(size * 0.886, width)
    return dict(size=size, kashida=n, en=en, ar=name(ar, text, size * 0.886, width))


def at(x, y):
    return dict(x=r(x), y=r(y))


# Each lockup has a left-to-right version (English pages: mark on the left,
# "kaleem" above «كليم») and a right-to-left one (Arabic pages: the mirror
# layout, mark on the right, «كليم» above "kaleem"). The mark itself is never
# mirrored.

# Lockup E (everyday): on the mark's own grid. The whole lockup is 110 x phi^2
# (288 x 110); a gap of 13 (the wall), a rule 5 wide (the letter stroke) from 21
# to 110 (the box's height), another 13, then the names fill the 147 left.
# Left-to-right: "kaleem" on line 55, «كليم» on line 97 (the box's inner floor).
# Right-to-left: the rows swap inside the same text block (same top, same bottom).
E_W, E_H, GAP, RULE = 288, 110, 13, 5
E_NAME_W = E_W - 110 - 2 * GAP - RULE
EN = names(E_NAME_W)
(_, en_t, en_b), (_, ar_t, ar_b) = EN['en'], EN['ar']
e_top, e_bottom = 55 + en_t, 97 + ar_b
E = dict(width=E_W, height=E_H,
         ltr=dict(mark=at(0, 0), rule=dict(x=110 + GAP, y=21, width=RULE, height=89),
                  en=at(E_W - E_NAME_W, 55), ar=at(E_W - E_NAME_W, 97)),
         rtl=dict(mark=at(E_W - 110, 0), rule=dict(x=E_NAME_W + GAP, y=21, width=RULE, height=89),
                  ar=at(0, e_top - ar_t), en=at(0, e_bottom - en_b)))

# Lockup C (signature): height 200; square 200 : name area 200 x phi; the mark
# is the square / phi, inset (200 - mark) / 2 = 38.2, and the names keep that
# same padding, each centred in its row. Guide lines = the wall / phi^4.
C_H = 200
C_NW = C_H * PHI
C_W = C_H + C_NW
C_MARK = C_H / PHI
C_PAD = (C_H - C_MARK) / 2
C_LINE = 13 / 110 * C_MARK / PHI ** 4
C_ROW = C_H / 2
CN = names(C_NW - 2 * C_PAD)
(_, cen_t, cen_b), (_, car_t, car_b) = CN['en'], CN['ar']
lw = C_LINE
row1 = lambda t, b: C_ROW / 2 - (t + b) / 2        # noqa: E731  baseline centring a name in the top row
row2 = lambda t, b: C_ROW * 1.5 - (t + b) / 2      # noqa: E731  ... in the bottom row
C = dict(width=r(C_W), height=C_H, line=r(lw), mark_scale=float('%.5f' % (C_MARK / 110)),
         frame=dict(x=r(lw / 2), y=r(lw / 2), width=r(C_W - lw), height=r(C_H - lw)),
         ltr=dict(mark=at(C_PAD, C_PAD),
                  divider=dict(x=r(C_H - lw / 2), y=0, width=r(lw), height=C_H),
                  row=dict(x=C_H, y=r(C_ROW - lw / 2), width=r(C_NW), height=r(lw)),
                  en=at(C_H + C_PAD, row1(cen_t, cen_b)), ar=at(C_H + C_PAD, row2(car_t, car_b))),
         rtl=dict(mark=at(C_NW + C_PAD, C_PAD),
                  divider=dict(x=r(C_NW - lw / 2), y=0, width=r(lw), height=C_H),
                  row=dict(x=0, y=r(C_ROW - lw / 2), width=r(C_NW), height=r(lw)),
                  ar=at(C_PAD, row1(car_t, car_b)), en=at(C_PAD, row2(cen_t, cen_b))))

NAMES = {'E_EN': EN['en'][0], 'E_AR': EN['ar'][0], 'C_EN': CN['en'][0], 'C_AR': CN['ar'][0]}


def mark(ink, block, tf=''):
    t = f' transform="{tf}"' if tf else ''
    return f'<g{t}><path d="{BOX}" fill="{ink}"/><rect x="76" y="0" width="34" height="34" fill="{block}"/></g>'


def svg(vb, body, label='Kaleem — كليم'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">{body}</svg>\n'


def rect(d, ink, extra=''):
    return f'<rect x="{d["x"]}" y="{d["y"]}" width="{d["width"]}" height="{d["height"]}" fill="{ink}"{extra}/>'


def placed(d, pos, ink):
    return f'<path transform="translate({pos["x"]} {pos["y"]})" d="{d}" fill="{ink}"/>'


def lockup_e_body(ink, block, dir='ltr'):
    L = E[dir]
    return (mark(ink, block, f'translate({L["mark"]["x"]} 0)' if L['mark']['x'] else '') + rect(L['rule'], ink)
            + placed(NAMES['E_EN'], L['en'], ink) + placed(NAMES['E_AR'], L['ar'], ink))


def lockup_c_body(ink, block, dir='ltr'):
    f, L = C['frame'], C[dir]
    return (f'<rect x="{f["x"]}" y="{f["y"]}" width="{f["width"]}" height="{f["height"]}" fill="none" stroke="{ink}" stroke-width="{C["line"]}"/>'
            + rect(L['divider'], ink) + rect(L['row'], ink)
            + mark(ink, block, f'translate({L["mark"]["x"]} {L["mark"]["y"]}) scale({C["mark_scale"]})')
            + placed(NAMES['C_EN'], L['en'], ink) + placed(NAMES['C_AR'], L['ar'], ink))


def lockup_e(ink, block, dir='ltr'):
    return svg(f'0 0 {E_W} {E_H}', lockup_e_body(ink, block, dir))


def lockup_c(ink, block, dir='ltr'):
    return svg(f'0 0 {C["width"]} {C_H:g}', lockup_c_body(ink, block, dir))


# Icons: a 170 tile around the 110 mark, centred on the grid point (50, 60),
# corner radius 38. The favicon is the tile in sky, the website's pastel: it
# reads on light and dark browser tabs alike.
TILE = '-35 -25 170 170'


def tile(ground, ink, rx=38, label='Kaleem'):
    rr = f' rx="{rx}"' if rx else ''
    return svg(TILE, f'<rect x="-35" y="-25" width="170" height="170"{rr} fill="{ground}"/>' + mark(ink, YEL), label)


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
    'kaleem-lockup-c-one-colour-ink.svg': lockup_c(INK, INK),
    # Arabic versions (right to left): for Arabic pages and Arabic documents.
    'kaleem-lockup-e-ar.svg': lockup_e(INK, YEL, 'rtl'),
    'kaleem-lockup-e-ar-chalk.svg': lockup_e(CHALK, YEL, 'rtl'),
    'kaleem-lockup-e-ar-one-colour-ink.svg': lockup_e(INK, INK, 'rtl'),
    'kaleem-lockup-c-ar.svg': lockup_c(INK, YEL, 'rtl'),
    'kaleem-lockup-c-ar-chalk.svg': lockup_c(CHALK, YEL, 'rtl'),
    'kaleem-lockup-c-ar-one-colour-ink.svg': lockup_c(INK, INK, 'rtl'),
    'kaleem-app-icon-sky.svg': tile(SKY, INK),
    'kaleem-app-icon.svg': tile(NIGHT, CHALK),
    'kaleem-app-icon-white.svg': tile('#ffffff', INK),
    # Square, no rounding: for platforms that round or crop the corners
    # themselves (apple-touch-icon, the 192px icon Google Search shows).
    'kaleem-icon-square-sky.svg': tile(SKY, INK, rx=0),
    'kaleem-icon-square.svg': tile(NIGHT, CHALK, rx=0),
    'kaleem-avatar.svg': svg('-60 -50 220 220', f'<rect x="-60" y="-50" width="220" height="220" fill="{NIGHT}"/>' + mark(CHALK, YEL), 'Kaleem'),
    'kaleem-avatar-sky.svg': svg('-60 -50 220 220', f'<rect x="-60" y="-50" width="220" height="220" fill="{SKY}"/>' + mark(INK, YEL), 'Kaleem'),
    # Browser favicon: the sky tile.
    'favicon.svg': tile(SKY, INK),
}

out_dir = os.path.join(REPO, 'design', 'logo', 'masters')
for name, text in MASTERS.items():
    with open(os.path.join(out_dir, name), 'w') as f:
        f.write(text)

def ts_obj(d):
    return '{ ' + ', '.join(f'{k}: {ts_obj(v) if isinstance(v, dict) else v}' for k, v in d.items()) + ' }'


ts = ['/**',
      ' * Kaleem logo geometry: the single source for every logo on the site.',
      ' * Generated by design/logo/tools/masters.py from the logo standard',
      ' * (design/logo/). Do not edit by hand; change the standard and regenerate.',
      ' *',
      ' * The mark sits on a 110-unit grid (frame 89, door and block 34, step 21,',
      ' * wall 13). Lockup E is 288 x 110 on that same grid; lockup C is',
      ' * 523.6 x 200 on a golden grid. Both are 2.618 : 1. The names are outlined',
      ' * IBM Plex Mono 600 and IBM Plex Sans Arabic 600, fitted to equal ink',
      ' * widths and drawn at the origin (ink left edge x 0, baseline y 0); each',
      ' * layout places them with `en` and `ar`.',
      ' *',
      ' * `ltr` is the English layout (mark left, "kaleem" on top); `rtl` the',
      ' * Arabic one (mark right, «كليم» on top). The mark is never mirrored.',
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
      '',
      '/** Lockup E: the mark at 1:1, the rule, the names. */',
      f'export const E_LOCKUP = {ts_obj(E)} as const;',
      '/** Lockup C: frame, divider and row line (all one weight); the mark at `mark`, scaled by `mark_scale`. */',
      f'export const C_LOCKUP = {ts_obj(C)} as const;',
      '']
for key, d in NAMES.items():
    ts.append(f'export const {key} =\n  "{d}";')
with open(os.path.join(REPO, 'src', 'data', 'logo.ts'), 'w') as f:
    f.write('\n'.join(ts) + '\n')

print(f'{len(MASTERS)} masters, src/data/logo.ts')
print(f'E: names {E_NAME_W} wide, size {EN["size"]:.2f}, {EN["kashida"]} kashidas; '
      f'C: mark {C_MARK:.2f}, padding {C_PAD:.2f}, line {C_LINE:.3f}, size {CN["size"]:.2f}, {CN["kashida"]} kashidas')

# The canvas components Logo-E, Logo-C and their Arabic versions draw the same
# shapes; their colours stay holes ({{ink}}, {{block}}) for the canvas's props.
# Scale 1 = 200 tall. The Arabic components start as copies of the English ones.
import re  # noqa: E402
import shutil  # noqa: E402
canvas = os.path.join(REPO, 'design', 'logo', 'canvas')
for name, src, title, vb, w, body in (
        ('Logo-E.dc.html', None, None, f'0 0 {E_W} {E_H}', 200 * E_W / E_H, lockup_e_body('{{ink}}', '{{block}}')),
        ('Logo-C.dc.html', None, None, f'0 0 {C["width"]} {C_H}', C['width'], lockup_c_body('{{ink}}', '{{block}}')),
        ('Logo-E-ar.dc.html', 'Logo-E.dc.html', 'Kaleem logo · everyday lockup (E), Arabic', f'0 0 {E_W} {E_H}', 200 * E_W / E_H, lockup_e_body('{{ink}}', '{{block}}', 'rtl')),
        ('Logo-C-ar.dc.html', 'Logo-C.dc.html', 'Kaleem logo · signature lockup (C), Arabic', f'0 0 {C["width"]} {C_H}', C['width'], lockup_c_body('{{ink}}', '{{block}}', 'rtl'))):
    p = os.path.join(canvas, name)
    if src and not os.path.exists(p):
        shutil.copy(os.path.join(canvas, src), p)
    with open(p) as f:
        s = f.read()
    if title:
        s = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', s)
    s = re.sub(r'<svg width="\{\{w\}\}".*?\n</svg>\n',
               lambda _: f'<svg width="{{{{w}}}}" height="{{{{h}}}}" viewBox="{vb}" role="img" aria-label="Kaleem — كليم" style="display: block">\n{body}\n</svg>\n',
               s, flags=re.S)
    s = re.sub(r'return \{ w: [\d.]+ \* s,', f'return {{ w: {w:.3f} * s,', s)
    with open(p, 'w') as f:
        f.write(s)
print('canvas/Logo-E, Logo-C, Logo-E-ar, Logo-C-ar')
