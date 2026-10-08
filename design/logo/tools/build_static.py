"""Build design/logo/standard.html: every board of the logo canvas as one
static page (no canvas runtime). Child components (<dc-import>) are inlined
with their props filled in, the way the canvas renders them."""
import json, os, re, sys
SRC, OUT = sys.argv[1], sys.argv[2]
FONTS = ('https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,700'
         '&family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;600'
         '&family=IBM+Plex+Sans+Arabic:wght@600&display=swap')
def body(path):
    t = open(os.path.join(SRC, path)).read()
    return re.search(r'</helmet>(.*?)</x-dc>', t, re.S).group(1)
def comp(name, a):
    s = float(a.get('scale', 1)); size = int(a.get('size', 200))
    v = {'w': f'{524*s:g}', 'h': f'{200*s:g}', 'px': f'{size}px',
         'ink': a.get('ink', '#1f1f1f'), 'block': a.get('block', '#f8d12f')}
    return re.sub(r'\{\{\s*(\w+)\s*\}\}', lambda m: v[m.group(1)], body(name + '.dc.html'))
def inline(html):
    def rep(m):
        a = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        return comp(a['name'], a)
    return re.sub(r'<dc-import([^>]*)></dc-import>', rep, html)
idx = json.load(open(os.path.join(SRC, 'canvas.json')))
show = [b for b in idx['order'] if b.startswith(('Main', 'Std-', 'Construction', 'Logo-lockup'))]
parts = []
for b in show:
    parts.append(f'<section class="board"><h2 class="cap">{idx["boards"][b].get("title", b)}</h2>{inline(body(b))}</section>')
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=1520">
<title>Kaleem logo standard</title>
<link rel="stylesheet" href="{FONTS.replace('&', '&amp;')}">
<style>
body {{ margin: 0; background: #e6e2d8; font-family: 'IBM Plex Sans', system-ui, sans-serif; }}
main {{ display: flex; flex-direction: column; align-items: center; gap: 56px; padding: 56px 40px; }}
.board {{ width: 1440px; }}
.cap {{ margin: 0 0 12px; font: 600 13px/1 'IBM Plex Mono', monospace; letter-spacing: .08em; color: #4a4a4a; }}
.board > div {{ box-shadow: 0 0 0 1px #c9c3b4; }}
</style>
</head>
<body>
<!-- Generated from design/logo/canvas/ by design/logo/tools/build_static.py. Edit the canvas, not this file. -->
<main>
{chr(10).join(parts)}
</main>
</body>
</html>
'''
open(OUT, 'w').write(page)
print(len(show), 'boards ->', OUT)
