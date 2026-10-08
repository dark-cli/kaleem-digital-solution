# Case studies

Case studies are proof of the method, not the business itself. The Work page is a gallery of equal-size tiles (screenshot in a WindowWidget, story, Tags) ending with a dashed "Your project next" tile that links to the audit form. The home page's Our work band shows the current cases in alternating rows: text and three `stat` numbers on one side, the screenshot window on the other. Once there are five or more projects, the Work page gains a hero for the best one.

## Template for every case study

1. **Before** — one paragraph: what was locked, lost or scattered.
2. **The method, step by step** — Audit, Extract & clean, Rebuild, Hand over the keys, Support. One or two lines each.
3. **What the client now controls** — a checklist.
4. **Results** — up to four real, dated numbers (Stat components).
5. **Services involved** — Tags.

Only publish with the client's written permission, and never show personal or confidential data.

## Case study 01 · Alimran Medical Center (Basra, 2026) — `/al-imran/`

**Services:** The Jailbreak · Websites · Networks & security · Consulting
**Permission:** granted in the client agreement (clause 2.6): name, logo, screenshots and public performance figures, with no patient data, confidential information or credentials.

**Before.** An old, slow WordPress site the owner could no longer log into, with more than 600 articles split across two separate sites (Arabic and English), many pages in one language only. The Google Business profile and social pages were out of the clinic's control.

**The method in practice**
- **Audit** — mapped both old sites, the domain, Google Business, Instagram and Facebook.
- **Extract & clean** — pulled every article and media file out of the old site and cleaned them.
- **Rebuild on open standards** — content converted to Markdown; one bilingual site built with Astro as static pages on Cloudflare, with a live-preview content editor; SEO errors fixed; staff and guest networks separated, with a guest Wi-Fi portal.
- **Hand over the keys** — code repository, Cloudflare account and domain transferred to the clinic, with documentation; old domain, Google Business and social pages recovered.
- **Support** — free fix and advice periods; a media campaign starting next.

**Results (September 2026):** 600 articles moved · Arabic + English in one site · mobile PageSpeed 74 → 97 (LCP 4.9 s → 2.1 s; Accessibility, Best Practices and SEO all 100) · pages open in under a second instead of 3 to 10.
The headline is the speed people feel; PageSpeed is the supporting proof. Never claim "10×" or uptime numbers.

**AR.** موقع ووردبريس قديم وبطيء فقد المالك صلاحية الدخول إليه، وأكثر من 600 مقالة موزّعة على موقعين. طبّقنا طريقتنا خطوة بخطوة: استخرجنا المحتوى ونظّفناه، وحوّلناه إلى صيغة مفتوحة، وبنينا موقعًا واحدًا ثنائي اللغة لا يكلّف استضافة، ثم سلّمنا العيادة كل المفاتيح.

## Case study 02 · Deptmaster — debt-collection platform, utility company (2026) — `/deptmaster/`

**Services:** Management systems · Mobile apps · Consulting
**Tagline:** A debt-collection platform where no one — not even the administrators — can quietly change the numbers. — منصة لتحصيل الديون لا يستطيع فيها أحد — ولا حتى المسؤولون — تغيير الأرقام بصمت.

**Before.** Dozens of field collectors, shared wallets, verbal approvals. Balances were overwritten in place, so when something looked off nobody could answer: who changed that, when, and from what?

**The method in practice**
- **Audit** — in week one, of the existing system. They asked for logs everywhere; we told them: make the data structure the log.
- **Extract & clean** — a migration script copied everything out of the old database and reshaped it.
- **Build** — event sourcing: every action is a permanent event and balances are computed from them. One shared Rust core runs on the server (Axum, Postgres) and in the Flutter mobile app (SQLite, works offline). Fine-grained permissions per wallet, team, contact group and action.
- **Hand over** — one binary on the client's own server, full source code; no cloud, no subscription, no vendor. The code is public on GitHub (github.com/dark-cli/deptmaster) under PolyForm Noncommercial 1.0.0.
- **Support** — both systems ran side by side for almost a week; nobody needed to fall back, and the old system was retired.

**Results:** 230 automated tests (206 full scenarios) · 3 months from first contact to production · field app works with no signal · no major bugs reported since go-live.
