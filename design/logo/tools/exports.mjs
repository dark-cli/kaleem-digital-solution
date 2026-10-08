// Rasterise the logo masters and install the website's logo files.
//
//   python3 design/logo/tools/masters.py     (first: writes masters/*.svg)
//   node design/logo/tools/exports.mjs
//
// Needs Playwright with Chromium (`npm i -D playwright && npx playwright install chromium`,
// or set PLAYWRIGHT_MODULE to an installed copy). Writes:
//   design/logo/masters/*.png            PNG exports of the masters
//   public/favicon.svg, favicon.ico (16, 32, 48), favicon-32.png,
//   favicon-192.png, apple-touch-icon.png (180)   the sky tile
//   public/assets/logo/*.svg             copies of the SVG masters, for linking
//   public/assets/og-default(-ar).png    the social share images (1200 x 630)
import { copyFileSync, mkdirSync, mkdtempSync, readdirSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const REPO = resolve(HERE, '../../..');
const MASTERS = join(HERE, '../masters');
const PUBLIC = join(REPO, 'public');
const { chromium } = await import(process.env.PLAYWRIGHT_MODULE
  ? pathToFileURL(join(process.env.PLAYWRIGHT_MODULE, 'index.mjs')).href : 'playwright');

const TMP = mkdtempSync(join(tmpdir(), 'kaleem-logo-'));
const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 1 });

async function shot(html, out, w, h, transparent = true) {
  const file = join(TMP, 'page.html');
  writeFileSync(file, html);
  await page.setViewportSize({ width: w, height: h });
  await page.goto(pathToFileURL(file).href);
  await page.waitForLoadState('networkidle');
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(150);
  return page.screenshot({ path: out, omitBackground: transparent, clip: { x: 0, y: 0, width: w, height: h } });
}

const png = (svg, out, w, h = w) => shot(
  `<html><body style="margin:0;background:transparent"><img src="${pathToFileURL(join(MASTERS, svg)).href}" style="display:block;width:${w}px;height:${h}px"></body></html>`,
  out, w, h);

// Master PNGs. The lockups are 2.618 : 1, so 1048 x 400.
for (const [svg, out, w, h] of [
  ['kaleem-app-icon-sky.svg', 'kaleem-app-icon-sky-512.png', 512],
  ['kaleem-app-icon-sky.svg', 'kaleem-app-icon-sky-192.png', 192],
  ['kaleem-app-icon.svg', 'kaleem-app-icon-512.png', 512],
  ['kaleem-app-icon.svg', 'kaleem-app-icon-192.png', 192],
  ['kaleem-avatar.svg', 'kaleem-avatar-400.png', 400],
  ['kaleem-avatar-sky.svg', 'kaleem-avatar-sky-400.png', 400],
  ['kaleem-lockup-e.svg', 'kaleem-lockup-e-1048.png', 1048, 400],
  ['kaleem-lockup-e-chalk.svg', 'kaleem-lockup-e-chalk-1048.png', 1048, 400],
  ['kaleem-lockup-c.svg', 'kaleem-lockup-c-1048.png', 1048, 400],
  ['kaleem-lockup-c-chalk.svg', 'kaleem-lockup-c-chalk-1048.png', 1048, 400],
  ['kaleem-lockup-e-ar.svg', 'kaleem-lockup-e-ar-1048.png', 1048, 400],
  ['kaleem-lockup-e-ar-chalk.svg', 'kaleem-lockup-e-ar-chalk-1048.png', 1048, 400],
  ['kaleem-lockup-c-ar.svg', 'kaleem-lockup-c-ar-1048.png', 1048, 400],
  ['kaleem-lockup-c-ar-chalk.svg', 'kaleem-lockup-c-ar-chalk-1048.png', 1048, 400],
]) await png(svg, join(MASTERS, out), w, h ?? w);

// Favicon set: the rounded sky tile for tabs, the square one where the
// platform rounds or crops the corners itself.
copyFileSync(join(MASTERS, 'favicon.svg'), join(PUBLIC, 'favicon.svg'));
await png('kaleem-app-icon-sky.svg', join(PUBLIC, 'favicon-32.png'), 32);
await png('kaleem-icon-square-sky.svg', join(PUBLIC, 'favicon-192.png'), 192);
await png('kaleem-icon-square-sky.svg', join(PUBLIC, 'apple-touch-icon.png'), 180);
const icoSizes = [16, 32, 48];
const icoImages = [];
for (const s of icoSizes) icoImages.push(await png('kaleem-app-icon-sky.svg', join(TMP, `ico-${s}.png`), s));
writeFileSync(join(PUBLIC, 'favicon.ico'), ico(icoSizes, icoImages));

// The SVG masters, for linking from the site.
const logoDir = join(PUBLIC, 'assets/logo');
mkdirSync(logoDir, { recursive: true });
for (const f of readdirSync(MASTERS)) {
  if (f.endsWith('.svg') && f !== 'favicon.svg') copyFileSync(join(MASTERS, f), join(logoDir, f));
}

// Social share images: lockup E in chalk on the night sky, one per language,
// set in the site's own font files.
const font = (f) => pathToFileURL(join(PUBLIC, 'fonts', f)).href;
const ogFonts = `@font-face{font-family:Newsreader;font-weight:100 900;src:url(${font('newsreader-latin-400.woff2')})}
@font-face{font-family:Amiri;font-weight:700;src:url(${font('amiri-arabic-700.woff2')})}
@font-face{font-family:'IBM Plex Mono';font-weight:500;src:url(${font('ibm-plex-mono-latin-500.woff2')})}`;
for (const [lang, lockupFile, headline, out] of [
  ['en', 'kaleem-lockup-e-chalk.svg', 'We free your data, modernize your systems, and hand you the keys.', 'og-default.png'],
  ['ar', 'kaleem-lockup-e-ar-chalk.svg', 'نحرّر بياناتك، ونحدّث أنظمتك، ونسلّمك المفاتيح.', 'og-default-ar.png'],
]) {
  const ar = lang === 'ar';
  await shot(`<!doctype html><html lang="${lang}" dir="${ar ? 'rtl' : 'ltr'}"><head><meta charset="utf-8"><style>${ogFonts}
body{margin:0}.og{width:1200px;height:630px;box-sizing:border-box;padding:96px 96px 0;background:#1d2320;color:#eceee6;display:flex;flex-direction:column;align-items:flex-start;gap:44px}
h1{margin:0;font-family:${ar ? 'Amiri,serif' : 'Newsreader,Georgia,serif'};font-weight:700;font-size:${ar ? 66 : 62}px;line-height:${ar ? 1.5 : 1.12};letter-spacing:${ar ? 0 : '-0.5px'};max-width:980px}
.url{font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:28px;color:#c6ddf0;direction:ltr}</style></head><body>
<div class="og"><img src="${pathToFileURL(join(MASTERS, lockupFile)).href}" width="314" height="120" alt="">
<h1>${headline}</h1><div class="url">kaleem.dev</div></div></body></html>`,
    join(PUBLIC, 'assets', out), 1200, 630, false);
}

await browser.close();
console.log('masters/*.png, public favicon set, public/assets/logo, og-default.png, og-default-ar.png');

// An ICO file whose images are PNGs (supported by every current browser).
function ico(sizes, images) {
  const head = Buffer.alloc(6 + 16 * images.length);
  head.writeUInt16LE(0, 0); head.writeUInt16LE(1, 2); head.writeUInt16LE(images.length, 4);
  let offset = head.length;
  images.forEach((img, i) => {
    const e = 6 + 16 * i, s = sizes[i];
    head.writeUInt8(s >= 256 ? 0 : s, e); head.writeUInt8(s >= 256 ? 0 : s, e + 1);
    head.writeUInt16LE(1, e + 4); head.writeUInt16LE(32, e + 6);
    head.writeUInt32LE(img.length, e + 8); head.writeUInt32LE(offset, e + 12);
    offset += img.length;
  });
  return Buffer.concat([head, ...images]);
}
