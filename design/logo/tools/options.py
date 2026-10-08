"""Lockup options: E (B and door-based) and C (golden-checked), as SVG strings."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from outline import Face
import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
PHI = (1 + 5 ** .5) / 2
FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
mono, ar = Face(os.path.join(FD, 'mono600.woff')), Face(os.path.join(FD, 'ar600.woff'))
BOX = 'M0 21H55V34H13V97H76V55H89V110H0Z'
STEM = 128 / 1000      # stroke of l/k in IBM Plex Mono 600, per em
ASC = 740 / 1000       # height of k/l (and ك ل in Plex Sans Arabic) per em
def _shape(f, t):
    b = hb.Buffer(); b.add_str(t); b.guess_segment_properties(); hb.shape(f.hbfont, b, {}); return b
def natural(f, t, size): return sum(p.x_advance for p in _shape(f, t).glyph_positions) * size / f.upm
def run(f, t, size, x0, base, width=None):
    b = _shape(f, t); k = size / f.upm; nat = natural(f, t, size); sx = width / nat if width else 1
    pen = SVGPathPen(f.gs, ntos=lambda v: ('%.2f' % v).rstrip('0').rstrip('.')); bp = BoundsPen(f.gs); px = 0
    for i, p in zip(b.glyph_infos, b.glyph_positions):
        g = f.order[i.codepoint]; m = (k * sx, 0, 0, -k, x0 + (px + p.x_offset) * k * sx, base - p.y_offset * k)
        f.gs[g].draw(TransformPen(pen, m)); f.gs[g].draw(TransformPen(bp, m)); px += p.x_advance
    return pen.getCommands(), bp.bounds, sx
def ar_text(size, width):
    best = min(range(4, 60), key=lambda n: abs(natural(ar, 'كلي' + 'ـ' * n + 'م', size) - width))
    return 'كلي' + 'ـ' * best + 'م', best
def mark(ink, block, tf=''):
    t = f' transform="{tf}"' if tf else ''
    return f'<g{t}><path d="{BOX}" fill="{ink}"/><rect x="76" y="0" width="34" height="34" fill="{block}"/></g>'

def lockup_e_fit(gap=13, rule=5, total=288, ink='#1f1f1f', block='#f8d12f'):
    """B: outer box 110 x phi^2; the names fill what is left."""
    xr = 110 + gap; xn = xr + rule + gap; W = total - xn
    s = W / natural(mono, 'kaleem', 1)
    en, _, _ = run(mono, 'kaleem', s, xn, 55)
    t, n = ar_text(s * 0.886, W); arp, _, sx = run(ar, t, s * 0.886, xn, 97, W)
    body = mark(ink, block) + f'<rect x="{xr}" y="21" width="{rule}" height="89" fill="{ink}"/><path d="{en}" fill="{ink}"/><path d="{arp}" fill="{ink}"/>'
    return total, body, dict(size=s, width=W, rule=rule, gap=gap, kashida=n, stretch=sx)

def lockup_e_door(gap=13, ink='#1f1f1f', block='#f8d12f'):
    """Door: tall letters = 34 (the door); rule = the letters' stroke; gaps = the wall."""
    s = 34 / ASC; rule = s * STEM
    xr = 110 + gap; xn = xr + rule + gap
    en, _, _ = run(mono, 'kaleem', s, xn, 55); W = natural(mono, 'kaleem', s)
    t, n = ar_text(s, W); arp, _, sx = run(ar, t, s, xn, 97, W)
    total = xn + W
    body = mark(ink, block) + f'<rect x="{xr:.2f}" y="21" width="{rule:.2f}" height="89" fill="{ink}"/><path d="{en}" fill="{ink}"/><path d="{arp}" fill="{ink}"/>'
    return total, body, dict(size=s, width=W, rule=rule, gap=gap, kashida=n, stretch=sx)

def lockup_c_golden(ink='#1f1f1f', block='#f8d12f'):
    """C checked: H = 200; square : names = 1 : phi; mark = square/phi; one padding
    (the mark's inset) everywhere; guide lines = the wall / phi^4; names centred on their rows."""
    H = 200.0; Wn = H * PHI; inset = (H - H / PHI) / 2; m = H / PHI
    line = 13 / 110 * m / PHI ** 4
    x0 = H; W = Wn - 2 * inset; row = H / 2
    s = W / natural(mono, 'kaleem', 1)
    en0, b0, _ = run(mono, 'kaleem', s, x0 + inset, 0)
    base_en = row / 2 - (b0[1] + b0[3]) / 2
    en, _, _ = run(mono, 'kaleem', s, x0 + inset, base_en)
    sa = s * 0.886; t, n = ar_text(sa, W)
    ar0, b1, _ = run(ar, t, sa, x0 + inset, 0, W)
    base_ar = row + row / 2 - (b1[1] + b1[3]) / 2
    arp, _, sx = run(ar, t, sa, x0 + inset, base_ar, W)
    total = H + Wn; lw = line
    body = (f'<rect x="{lw/2:.3f}" y="{lw/2:.3f}" width="{total-lw:.3f}" height="{H-lw:.3f}" fill="none" stroke="{ink}" stroke-width="{lw:.3f}"/>'
            f'<rect x="{H-lw/2:.3f}" y="0" width="{lw:.3f}" height="{H}" fill="{ink}"/>'
            f'<rect x="{H}" y="{row-lw/2:.3f}" width="{Wn:.3f}" height="{lw:.3f}" fill="{ink}"/>'
            + mark(ink, block, f'translate({inset:.3f} {inset:.3f}) scale({m/110:.5f})')
            + f'<path d="{en}" fill="{ink}"/><path d="{arp}" fill="{ink}"/>')
    return total, H, body, dict(mark=m, inset=inset, line=line, name_width=W, size=s, kashida=n, stretch=sx)

if __name__ == '__main__':
    for f in (lockup_e_fit, lockup_e_door):
        t, _, i = f(); print(f.__name__, round(t, 1), {k: round(v, 3) if isinstance(v, float) else v for k, v in i.items()})
    t, h, _, i = lockup_c_golden(); print('c', round(t, 1), h, {k: round(v, 3) if isinstance(v, float) else v for k, v in i.items()})
