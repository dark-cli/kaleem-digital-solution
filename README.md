# Medical Clinic Website Template

A production-grade, bilingual (English + Arabic) medical clinic website template built with **Astro 5**, featuring a powerful block-based content system, integrated CMS, and image optimization pipeline.

This template is designed to be forked and customized for any medical clinic or healthcare practice. All clinic-specific content has been removed; only the framework and block widget system remain.

---

## Quick start

```bash
# Clone and set up
git clone <your-repo-url>
cd your-clinic-website
npm install

# Local development
npm run dev     # Preview at http://localhost:4321

# Build for production
npm run build
```

### Using the CMS

1. Run `npm run dev`
2. Visit [http://localhost:4321/admin/](http://localhost:4321/admin/) in **Chrome, Edge, or Brave**
   - (Firefox and Safari not supported — they don't have File System Access API)
3. Click "Work with Local Repository" and select your project folder
4. The CMS reads/writes markdown files in `src/content/` and mirrors your `src/content.config.ts` schema

### After cloning: Update your clinic's info

1. **`src/consts.ts`** — Update clinic name, contact info, social links, branding
2. **`src/data/header-nav.ts`** — Update navigation structure for your services/conditions
3. **`src/pages/[locale]/index.astro`** — Update homepage hero, services, and clinic info
4. **`public/images/`** — Replace with your clinic's photos and assets
5. **`src/styles/global.css`** — Update design tokens (colors) to match your branding
6. **`src/content/pages/about/`** — Update mission, vision, values
7. Add your **treatments**, **services**, **doctors**, and **blog posts** using the markdown structure

Everything else — deploys, CMS features, content authoring guidelines, the 14 block widget types, the image optimization pipeline — is documented in **[`docs/`](docs/)**.

---

## Documentation map

| File | Purpose |
|---|---|
| [`docs/setup.md`](docs/setup.md) | Local development setup + prerequisites |
| [`docs/deployment.md`](docs/deployment.md) | Cloudflare Pages workflow, build logs, rollback |
| [`docs/project-structure.md`](docs/project-structure.md) | Where every file type lives and why |
| [`docs/content-authoring.md`](docs/content-authoring.md) | How to write articles: frontmatter, voice, bilingual policy |
| [`docs/sections.md`](docs/sections.md) | All block/widget types with syntax + examples |
| [`docs/cms.md`](docs/cms.md) | Using the Sveltia admin — features and limitations |
| [`docs/image-optimization.md`](docs/image-optimization.md) | How the WebP variant pipeline works |
| [`docs/scripts.md`](docs/scripts.md) | Utility scripts: link checks, font updates, redirects |
| [`docs/tokens.md`](docs/tokens.md) | Design-system tokens (colours, type, spacing) |
| [`docs/ai/SKILL.md`](docs/ai/SKILL.md) | Brief for AI collaborators — how to work on this project |

---

## Stack

- **[Astro 5](https://astro.build/)** — static site generator, TypeScript
- **[Sveltia CMS](https://sveltiacms.app/)** — browser-based Git CMS
- **[Cloudflare Workers/Pages](https://developers.cloudflare.com/pages/)** — hosting + edge
- **[Sharp](https://sharp.pixelplumbing.com/)** — build-time image optimization
- **Self-hosted fonts** — Newsreader, IBM Plex, Amiri, IBM Plex Sans Arabic

## License

Copyright © 2026 Ali Mussa Imran. All rights reserved. See `LICENSE`.
