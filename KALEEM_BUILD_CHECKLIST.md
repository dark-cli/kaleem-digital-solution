# Kaleem Website Build Checklist
**What to Build for Kaleem.dev**

---

## 🔴 CRITICAL FIRST (Foundation)

- [ ] **Port Kaleem CSS System** → `src/styles/kaleem.css`
  - Color tokens (8 pastels + board/chalk)
  - Texture gradients (paper specks, chalkboard dust)
  - `.sk` sketch card (border + offset shadow)
  - `.skb` button (sketch style)
  - `.k-tag` pill tag
  - `.k-receipt` dashed box
  - Responsive breakpoints (1440 / 1056 / 672 / mobile)

- [ ] **Restyle Template Header** → `src/components/Header.astro`
  - Chalkboard (`.board`) background
  - Chalk-colored text and links
  - Update nav item colors
  - Update CTA button to lilac (`.skb`)
  - Keep bilingual + RTL support

- [ ] **Restyle Template Footer** → `src/components/Footer.astro`
  - Chalkboard (`.board`) background
  - Chalk-colored text
  - Reorganize to 4-column grid (Company, Services, Contact, etc.)
  - Add border divider before copyright row
  - Keep bilingual support

- [ ] **Build SketchCard Component** → `src/components/SketchCard.astro`
  - Props: `children`, `background` (color name), `padding`
  - Render with `.sk` class + background color
  - Reusable for problem cards, method steps, service cards, etc.

- [ ] **Build Button Component** → `src/components/Button.astro`
  - Props: `label`, `href` (or `onclick`), `variant` (primary/secondary/header)
  - Render as `<a>` or `<button>` with `.skb` class
  - Colors: mint (primary), paper (secondary), lilac (header)

---

## 🟡 HIGH PRIORITY (Home Page Sections)

- [ ] **Build HeroSection** → `src/components/HeroSection.astro`
  - Props: title, description, ctas, illustration (SVG)
  - Layout: 2-column (text | image)
  - Background: peach (`.bg-peach`)
  - Text: 72px bold title + 22px body + 2 buttons

- [ ] **Build ProblemCardsSection** → `src/components/sections/ProblemCardsSection.astro`
  - Grid: 4 columns (3 cards + 1 text row)
  - Cards: SketchCard with `.bg-butter`
  - Card content: 20px bold text
  - Final row: 26px bold text + arrow SVG

- [ ] **Build MethodStepsSection** → `src/components/sections/MethodStepsSection.astro`
  - Grid: 5 columns (one per step)
  - Background: `.bg-paper-2` with top/bottom borders
  - Each step: SketchCard with rotating color (sky → mint → lilac → butter → peach)
  - Content: large mono number (01–05) + title + description
  - Decoration: arrow SVG between title and grid

- [ ] **Build ServicesGridSection** → `src/components/sections/ServicesGridSection.astro`
  - Grid: 3 columns × 2 rows
  - Cards: SketchCard with service color (mapped 1:1 to pastel)
  - Card anatomy: icon (40×40) + title (26px) + description (16px) + "Learn more" link
  - Full card is clickable link to service detail page
  - Props: services array (name, description, href, icon, color)

- [ ] **Build AboutValuesSection** → `src/components/sections/AboutValuesSection.astro`
  - Layout: 2-column (gap 64px)
  - Background: `.bg-lilac` with top/bottom borders
  - Left: H2 + 5 checklist items (each with check SVG)
  - Right: H2 + 2×3 grid of value pairs (dt/dd format)
  - Props: checks[], values[]

- [ ] **Build CaseStudySection** → `src/components/sections/CaseStudySection.astro`
  - Layout: 2-column (5fr text | 7fr image)
  - Text: meta label + H2 + client H3 + description + tags + CTA button
  - Image: browser frame mockup (`.sk` with `.board` title bar + 3 dots)
  - Props: metaLabel, heading, clientName, description, tags[], cta, imageSrc

- [ ] **Build CTASection** → `src/components/sections/CTASection.astro`
  - Background: `.bg-mint` with top border
  - Layout: 2-column (text left | SVG right)
  - Text: H2 (52px) + Button
  - SVG: key illustration (decorative)
  - Props: heading, buttonLabel, buttonHref, illustration

---

## 🟠 MOBILE NAVIGATION (User Request)

- [ ] **Build MobileMenuButton** → `src/components/MobileMenuButton.astro`
  - 44×44 lilac button (`.skb` class)
  - Menu icon SVG (3 horizontal lines)
  - Visible only on mobile (<672px)
  - onClick: toggle `aria-expanded` and menu visibility

- [ ] **Build MobileMenuOverlay** → `src/components/MobileMenuOverlay.astro`
  - Full-screen overlay (position fixed, top 0, left 0)
  - Background: semi-transparent dark
  - Menu slides in from left (LTR) or right (RTL)
  - Items: Same nav structure as desktop, stacked vertically
  - Close: On item click, on ESC key, on close button
  - Keyboard: Focus trap inside menu, ESC closes

- [ ] **Integrate Mobile Menu into Header** → Update `src/components/Header.astro`
  - Conditionally render MobileMenuButton on small screens
  - Conditionally render MobileMenuOverlay based on state
  - State management: Use Astro client components or vanilla JS

- [ ] **Test Responsive Breakpoints**
  - Desktop (≥1056px): Horizontal nav
  - Tablet (672–1055px): Single-column content, horizontal nav (or menu button)
  - Mobile (<672px): Menu button + mobile menu overlay

---

## 🟢 SUB-PAGES

- [ ] **Build ServiceDetailPage** → `src/pages/[locale]/services/[...slug].astro`
  - Hero: Service name + color band
  - Main content: Service detail panels (2-column layout)
  - Each panel: `.sk` card with icon + title + promise + who-it's-for + what-we-do list + `.k-receipt` box

- [ ] **Build CaseStudyPage** → `src/pages/[locale]/work/[slug].astro`
  - Hero section
  - Problem/solution narrative (prose + images)
  - Timeline or results section
  - Related case studies (cards)
  - CTA to contact

- [ ] **Build ServicesHubPage** → `src/pages/[locale]/services/index.astro`
  - Services directory
  - All service detail sections stacked
  - Link to individual service pages

- [ ] **Build ContactPage** → `src/pages/[locale]/contact/index.astro`
  - Contact form (free audit questionnaire)
  - Form inputs: text, email, textarea (all Kaleem-styled)
  - Submit button
  - Contact info section

---

## 🔵 COMPONENTS & UTILITIES

- [ ] **Build IconLibrary** → `src/components/icons/`
  - Service icons (6 × 40px line icons): Jailbreak, Web, Mobile, Systems, Networks, Consulting
  - System icons: menu (32px), check (20px), close (24px)
  - Render as SVG (inline, inherit color via `.ico` class)

- [ ] **Build SvgIllustration Component** → `src/components/SvgIllustration.astro`
  - Wrapper for hand-drawn SVGs with wobble filter
  - Props: name (hero, arrow, key, etc.), size, ariaHidden
  - Apply `feTurbulence` + `feDisplacementMap` filter for hand-drawn effect

- [ ] **Build FormInput Component** → `src/components/FormInput.astro`
  - Props: name, label, type (text/email/etc.), required, placeholder
  - Styled with ink border (2px), padding, focus state (blue outline)
  - Use design tokens for colors

- [ ] **Build FormTextarea Component** → `src/components/FormTextarea.astro`
  - Props: name, label, required, placeholder, rows
  - Same styling as FormInput

- [ ] **Create Tag/Chip Component** → `src/components/Tag.astro`
  - Props: label, color (pastel name or hex)
  - Render with `.k-tag` class + background color
  - Pill-shaped (28px height, rounded)

---

## 📱 RESPONSIVE REFINEMENTS

- [ ] Test all sections at 3 breakpoints:
  - Desktop (1440px)
  - Tablet (800px)
  - Mobile (390px)

- [ ] Verify RTL layouts:
  - Flex direction flips
  - Logical properties work (margin-inline-start, etc.)
  - Menu slides from right on RTL

- [ ] Image optimization:
  - Browser frames, service icons, illustrations
  - Use template's Sharp pipeline

---

## 🎨 STYLING & POLISH

- [ ] Verify all colors match Kaleem palette
- [ ] Test focus rings on all interactive elements
- [ ] Ensure 44px+ touch targets on mobile
- [ ] Test reduced-motion media query (@prefers-reduced-motion: reduce)
- [ ] Verify contrast ratios (10.9:1 for ink on pastels, 13.7:1 for chalk on board)
- [ ] Cross-browser testing (Chrome, Firefox, Safari, Edge)

---

## 📝 DOCUMENTATION

- [ ] Update template README for Kaleem fork
- [ ] Document color tokens in `docs/tokens.md`
- [ ] Document new Kaleem-specific components in `docs/sections.md`
- [ ] Add Kaleem design principles to project

---

## QUICK STATS

| Phase | Estimated Components | Est. Time | Priority |
|-------|---------------------|-----------|----------|
| Foundation | 4–5 | 2–3 days | Critical |
| Home Page Sections | 7 | 3–4 days | High |
| Mobile Navigation | 3 | 1–2 days | High |
| Sub-pages | 3–4 | 2–3 days | Medium |
| Components/Utilities | 7–8 | 2–3 days | Medium |
| Testing & Polish | — | 1–2 days | High |
| **TOTAL** | **~28 components** | **~2–3 weeks** | — |

---

## NOTES

- Start with **Foundation phase** to establish colors, tokens, and base components
- **ProblemCardsSection** and **MethodStepsSection** are conceptually similar — build once, reuse pattern
- **Mobile menu** is **not shown in handoff** — design from scratch using accessibility best practices
- Form inputs and sub-pages can be built **in parallel** while sections are being finalized
- Use **Astro client components** sparingly (only for interactive elements like menu toggle)

