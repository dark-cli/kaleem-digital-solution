"""Outline the Kaleem lockup names to SVG paths, matching the canvas lockups
(SVG <text> with textLength + lengthAdjust=spacingAndGlyphs)."""
import io, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

class Face:
    def __init__(self, path):
        self.tt = TTFont(path); self.tt.flavor = None
        b = io.BytesIO(); self.tt.save(b)
        self.hbfont = hb.Font(hb.Face(hb.Blob(b.getvalue())))
        self.gs = self.tt.getGlyphSet(); self.upm = self.tt['head'].unitsPerEm
        self.order = self.tt.getGlyphOrder()

def text_path(face, text, size, cx, baseline, length):
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(face.hbfont, buf, {})
    k = size / face.upm
    total = sum(p.x_advance for p in buf.glyph_positions) * k
    sx = length / total
    x = cx - length / 2
    pen = SVGPathPen(face.gs, ntos=lambda v: ('%.2f' % v).rstrip('0').rstrip('.'))
    pen_x = 0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        name = face.order[info.codepoint]
        ox = x + (pen_x + pos.x_offset) * k * sx
        oy = baseline - pos.y_offset * k
        face.gs[name].draw(TransformPen(pen, (k * sx, 0, 0, -k, ox, oy)))
        pen_x += pos.x_advance
    return pen.getCommands()
