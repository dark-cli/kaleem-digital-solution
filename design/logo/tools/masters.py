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
    return float('%.3f' % v)


# Lockup E (everyday): on the mark's own grid. The whole lockup is 110 x phi^2
# (288 x 110); a gap of 13 (the wall), a rule 5 wide (the letter stroke) from 21
# to 110 (the box's height), another 13, then the names fill the 147 left.
# "kaleem" sits on line 55, the Arabic name on line 97 (the box's inner floor).
E_W, E_H, GAP, RULE = 288, 110, 13, 5
E_RULE_X = 110 + GAP
E_NAME_X = E_RULE_X + RULE + GAP
E_NAME_W = E_W - E_NAME_X
e_size = E_NAME_W / natural(mono, 'kaleem', 1)
e_en = run(mono, 'kaleem', e_size, E_NAME_X, 55)[0]
e_ar_text, e_kashida = ar_text(e_size * 0.886, E_NAME_W)
e_ar = run(ar, e_ar_text, e_size * 0.886, E_NAME_X, 97, E_NAME_W)[0]
E = dict(width=E_W, height=E_H, rule=dict(x=E_RULE_X, y=21, width=RULE, height=89))

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
c_names_w = C_NW - 2 * C_PAD
c_size = c_names_w / natural(mono, 'kaleem', 1)
_, b0, _ = run(mono, 'kaleem', c_size, 0, 0)
c_en = run(mono, 'kaleem', c_size, C_H + C_PAD, C_ROW / 2 - (b0[1] + b0[3]) / 2)[0]
c_ar_text, c_kashida = ar_text(c_size * 0.886, c_names_w)
_, b1, _ = run(ar, c_ar_text, c_size * 0.886, 0, 0, c_names_w)
c_ar = run(ar, c_ar_text, c_size * 0.886, C_H + C_PAD, C_ROW * 1.5 - (b1[1] + b1[3]) / 2, c_names_w)[0]
lw = C_LINE
C = dict(width=r(C_W), height=C_H, line=r(lw),
         frame=dict(x=r(lw / 2), y=r(lw / 2), width=r(C_W - lw), height=r(C_H - lw)),
         divider=dict(x=r(C_H - lw / 2), y=0, width=r(lw), height=C_H),
         row=dict(x=C_H, y=r(C_ROW - lw / 2), width=r(C_NW), height=r(lw)),
         mark=dict(x=r(C_PAD), y=r(C_PAD), scale=float('%.5f' % (C_MARK / 110))))

NAMES = {'E_EN': e_en, 'E_AR': e_ar, 'C_EN': c_en, 'C_AR': c_ar}


def mark(ink, block, tf=''):
    t = f' transform="{tf}"' if tf else ''
    return f'<g{t}><path d="{BOX}" fill="{ink}"/><rect x="76" y="0" width="34" height="34" fill="{block}"/></g>'


def svg(vb, body, label='Kaleem — كليم'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">{body}</svg>\n'


def rect(d, ink, extra=''):
    return f'<rect x="{d["x"]}" y="{d["y"]}" width="{d["width"]}" height="{d["height"]}" fill="{ink}"{extra}/>'


def lockup_e_body(ink, block):
    return (mark(ink, block) + rect(E['rule'], ink)
            + f'<path d="{NAMES["E_EN"]}" fill="{ink}"/><path d="{NAMES["E_AR"]}" fill="{ink}"/>')


def lockup_c_body(ink, block):
    f, m = C['frame'], C['mark']
    return (f'<rect x="{f["x"]}" y="{f["y"]}" width="{f["width"]}" height="{f["height"]}" fill="none" stroke="{ink}" stroke-width="{C["line"]}"/>'
            + rect(C['divider'], ink) + rect(C['row'], ink)
            + mark(ink, block, f'translate({m["x"]} {m["y"]}) scale({m["scale"]})')
            + f'<path d="{NAMES["C_EN"]}" fill="{ink}"/><path d="{NAMES["C_AR"]}" fill="{ink}"/>')


def lockup_e(ink, block):
    return svg(f'0 0 {E_W} {E_H}', lockup_e_body(ink, block))


def lockup_c(ink, block):
    return svg(f'0 0 {C["width"]} {C_H:g}', lockup_c_body(ink, block))


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
      ' * IBM Plex Mono 600 and IBM Plex Sans Arabic 600, fitted to equal widths.',
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
      '/** Lockup E: the mark at 1:1, then the rule, then the names. */',
      f'export const E_LOCKUP = {ts_obj(E)} as const;',
      '/** Lockup C: frame, divider and row line (all one weight), the mark placed at `mark`. */',
      f'export const C_LOCKUP = {ts_obj(C)} as const;',
      '']
for key, d in NAMES.items():
    ts.append(f'export const {key} =\n  "{d}";')
with open(os.path.join(REPO, 'src', 'data', 'logo.ts'), 'w') as f:
    f.write('\n'.join(ts) + '\n')

print(f'{len(MASTERS)} masters, src/data/logo.ts')
print(f'E: names {E_NAME_W} wide, size {e_size:.2f}, {e_kashida} kashidas; '
      f'C: mark {C_MARK:.2f}, padding {C_PAD:.2f}, line {C_LINE:.3f}, size {c_size:.2f}, {c_kashida} kashidas')

# The canvas components Logo-E and Logo-C draw the same shapes; their colours
# stay holes ({{ink}}, {{block}}) for the canvas's props. Scale 1 = 200 tall.
import re  # noqa: E402
canvas = os.path.join(REPO, 'design', 'logo', 'canvas')
for name, vb, w, body in (('Logo-E.dc.html', f'0 0 {E_W} {E_H}', 200 * E_W / E_H, lockup_e_body('{{ink}}', '{{block}}')),
                          ('Logo-C.dc.html', f'0 0 {C["width"]} {C_H}', C['width'], lockup_c_body('{{ink}}', '{{block}}'))):
    p = os.path.join(canvas, name)
    with open(p) as f:
        s = f.read()
    s = re.sub(r'<svg width="\{\{w\}\}".*?\n</svg>\n',
               lambda _: f'<svg width="{{{{w}}}}" height="{{{{h}}}}" viewBox="{vb}" role="img" aria-label="Kaleem — كليم" style="display: block">\n{body}\n</svg>\n',
               s, flags=re.S)
    s = re.sub(r'return \{ w: [\d.]+ \* s,', f'return {{ w: {w:.3f} * s,', s)
    with open(p, 'w') as f:
        f.write(s)
print('canvas/Logo-E.dc.html, canvas/Logo-C.dc.html')
