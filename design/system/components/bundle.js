/* @ds-bundle: {"format":4,"namespace":"Kaleem","components":[{"name":"Logo"},{"name":"Button"},{"name":"Tag"},{"name":"ServiceTile"},{"name":"Stat"}]} */
(function () {
  var R = window.React, h = R.createElement;
  function cx() { return Array.prototype.filter.call(arguments, Boolean).join(" "); }
  // A service id or a pastel name → the pastel. One colour = one service.
  var TONE = { jailbreak: "butter", websites: "sky", mobile: "peach", systems: "mint", networks: "apricot", consulting: "lilac",
    butter: "butter", sky: "sky", peach: "peach", mint: "mint", apricot: "apricot", lilac: "lilac", paper: "paper", gray: "gray" };
  function tone(t, d) { return "kl-" + (TONE[t] || d); }
  // 32×32 line icons, one per service (as on kaleem.dev).
  var ICON = {
    jailbreak: [["path", { d: "M18 6H6V26H26V14" }], ["rect", { x: 20, y: 3, width: 9, height: 9 }]],
    websites: [["rect", { x: 4, y: 6, width: 24, height: 20, rx: 2 }], ["path", { d: "M4 11h24M8 8.5h1M11 8.5h1" }]],
    mobile: [["rect", { x: 10, y: 3, width: 12, height: 26, rx: 3 }], ["path", { d: "M14 25h4" }]],
    systems: [["ellipse", { cx: 16, cy: 8, rx: 10, ry: 4 }], ["path", { d: "M6 8v16c0 2.2 4.5 4 10 4s10-1.8 10-4V8M6 16c0 2.2 4.5 4 10 4s10-1.8 10-4" }]],
    networks: [["path", { d: "M4 9l18-4l2 9l-18 4zM14 16v8H6" }], ["circle", { cx: 20, cy: 10, r: 1.5 }]],
    consulting: [["path", { d: "M5 6h22v14H14l-6 5v-5H5zM10 11h12M10 15h8" }]]
  };
  function Icon(p) {
    var parts = ICON[p.service]; if (!parts) return null;
    return h("svg", { className: "kl-ico", viewBox: "0 0 32 32", "aria-hidden": "true" },
      parts.map(function (e, i) { return h(e[0], Object.assign({ key: i }, e[1])); }));
  }
  function Mark() {
    // The logo standard's mark on its 110-unit grid (see design/logo/ in the repo).
    return h("svg", { viewBox: "0 0 110 110", "aria-hidden": "true" },
      h("path", { className: "kl-box", d: "M0 21H55V34H13V97H76V55H89V110H0Z" }),
      h("rect", { className: "kl-block", x: 76, y: 0, width: 34, height: 34 }));
  }
  function Logo(p) {
    p = p || {};
    var lang = p.lang || "en", size = p.size || 24;
    var kids = [h(Mark, { key: "m" })];
    if (lang !== "ar") kids.push(h("span", { key: "w", className: "kl-logo-word" }, "kaleem"));
    if (lang === "both") kids.push(h("span", { key: "s", className: "kl-logo-sep" }));
    if (lang !== "en") kids.push(h("span", { key: "a", className: "kl-logo-ar", lang: "ar" }, "كليم"));
    if (lang === "mark") kids = [h(Mark, { key: "m" })];
    return h(p.href ? "a" : "span", { className: cx("kl-logo", p.className), href: p.href, style: { fontSize: size + "px" }, "aria-label": "Kaleem — كليم" }, kids);
  }
  function Button(p) {
    var kind = p.kind || "elevated", arrow = !!p.arrow;
    var rest = {}; for (var k in p) if (["kind", "tone", "size", "arrow", "children", "className"].indexOf(k) < 0) rest[k] = p[k];
    rest.className = cx("kl-btn", "kl-btn-" + kind, kind !== "link" && tone(p.tone, "paper"), p.size === "sm" && "kl-btn-sm", p.className);
    return h(p.href ? "a" : "button", rest, h("span", null, p.children), arrow ? h("span", { className: "kl-arrow", "aria-hidden": "true" }, "→") : null);
  }
  function Tag(p) {
    return h("span", { className: cx("kl-tag", p.tone && tone(p.tone, "paper"), p.className), lang: p.lang }, p.children);
  }
  function ServiceTile(p) {
    return h(p.href ? "a" : "article", { className: cx("kl-tile", tone(p.service, "paper"), p.className), href: p.href, dir: p.dir, lang: p.lang },
      p.icon === false ? null : h(Icon, { service: p.service }),
      h("h3", { className: "kl-tile-title" }, p.title),
      p.description ? h("p", { className: "kl-tile-desc" }, p.description) : null,
      p.items && p.items.length ? h("ul", { className: "kl-tile-list" }, p.items.map(function (t, i) { return h("li", { key: i }, t); })) : null);
  }
  function Stat(p) {
    return h("div", { className: cx("kl-stat", p.className), dir: p.dir, lang: p.lang },
      h("bdi", { className: "kl-stat-value" }, p.value, p.unit ? h("small", null, p.unit) : null),
      h("span", { className: "kl-stat-label" }, p.label));
  }
  window.Kaleem = Object.assign(window.Kaleem || {}, { Logo: Logo, Button: Button, Tag: Tag, ServiceTile: ServiceTile, Stat: Stat });
})();
