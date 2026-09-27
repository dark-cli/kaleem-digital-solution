# Kaleem Website Component Audit
**Mapping Kaleem Design to Astro Template**

Generated: 2026-09-27

---

## DESIGN SYSTEM TOKENS & INFRASTRUCTURE

### Current Template Status:
- ✅ Design tokens system (CSS custom properties)
- ✅ Bilingual i18n (EN/AR)
- ✅ RTL support (logical properties)
- ✅ Responsive breakpoints
- ❌ Kaleem-specific color palette (would need to port)
- ❌ Kaleem texture system (pure CSS gradients for paper/board)
- ❌ Sketch component styles (uneven borders, pen-line shadow)

### What We Need:
1. **Port Kaleem CSS tokens** to `src/styles/kaleem.css`
   - 8 pastel colors (peach, mint, lilac, butter, sky, apricot, etc.)
   - Board/chalk colors for header/footer
   - Sketch component shadow tricks (border + box-shadow offset)
   - Texture gradients (paper specks, chalkboard dust)

2. **Update global.css** to support Kaleem aesthetic
   - Remove/override generic tokens
   - Import Kaleem color palette
   - Add `.sk`, `.skb`, `.k-tag`, `.k-receipt` component classes

---

## PAGE-LEVEL COMPONENTS

### 1. HEADER / NAVIGATION

**Kaleem Design:**
- Dark chalkboard (`.board` class, 88px desktop / 64px mobile)
- Logo + monospace brand name (left)
- Horizontal nav (5-6 items, desktop)
- Language toggle (AR/EN)
- CTA button (lilac)
- **Mobile collapses to: menu button only** ← NOT IMPLEMENTED IN DRAFT

**Current Template Has:**
- ✅ `src/components/Header.astro` — bilingual header
- ✅ Logo and language toggle
- ✅ Navigation structure
- ✅ Responsive design

**Missing for Kaleem:**
- ❌ Mobile menu button (hamburger)
- ❌ Mobile dropdown/sidebar menu
- ❌ Chalkboard `.board` styling
- ❌ Chalk-colored text and links
- ❌ Kaleem nav item structure
- ❌ Lilac CTA button styling

**WIDGET TO BUILD:**
- **MobileMenuButton** — 44×44 lilac button, opens menu on click
- **MobileMenuSidebar** — Overlay menu for mobile (full-screen or slide-out)
- **NavDropdown** — Desktop hover dropdown (if needed)

---

### 2. FOOTER

**Kaleem Design:**
- Dark chalkboard (`.board` class)
- Logo + promise (left)
- 4-column link grid (Company, Services, Contact, etc.)
- Language/copyright divider bar
- All text in chalk colors

**Current Template Has:**
- ✅ `src/components/Footer.astro` — basic footer structure

**Missing for Kaleem:**
- ❌ Chalkboard styling (`.board` background + texture)
- ❌ Chalk-colored text
- ❌ 4-column grid layout
- ❌ Kaleem brand promise copy
- ❌ Contact section (phone, email, location)

**WIDGET TO BUILD:**
- **KaleemFooter** — Custom footer component (can reuse template footer as base)

---

## SECTION / PAGE BLOCKS

### 3. HERO SECTION (Home Page)

**Kaleem Design:**
- **Peach background** (`.bg-peach`)
- **Split layout:** Text (left) + SVG Illustration (right)
- **Hero heading:** 72px bold
- **Body text:** 22px
- **Two CTAs:** Mint button + Paper button
- **SVG:** Open Box with escaping blocks (hand-drawn style with filter)

**Current Template Has:**
- ✅ Prose block (text + heading)
- ✅ Media block (can hold SVG)
- ✅ Button styling (needs Kaleem `.skb` class)
- ❌ Hero-specific layout (split 50/50 grid)
- ❌ Peach background

**Missing:**
- ❌ Hero layout grid (text | image side-by-side)
- ❌ Pastel background section styling
- ❌ SVG filter support for hand-drawn effect

**WIDGET TO BUILD:**
- **HeroSection** — Custom hero with split text/image, pastel bg, CTAs

---

### 4. PROBLEM CARDS SECTION ("Sound familiar?")

**Kaleem Design:**
- **Section background:** Paper
- **Grid:** 4 columns (3 butter cards + 1 text row)
- **Cards:** `.sk` (sketch style) with `.bg-butter`
- **Typography:** 20px bold in cards, 26px bold in text row
- **Arrow illustration** between card 3 and text

**Current Template Has:**
- ✅ Cards block (for related reading)
- ❌ Problem cards in grid layout

**Missing:**
- ❌ Sketch card component (`.sk` styling)
- ❌ Multi-column problem cards
- ❌ Arrow SVG illustration

**WIDGET TO BUILD:**
- **ProblemCardsSection** — Grid of sketch cards + final text row
- **SketchCard** — Reusable `.sk` component for problem notes

---

### 5. METHOD SECTION (Five Steps)

**Kaleem Design:**
- **Background:** Paper-2 (alternate band) with top/bottom borders
- **Title + intro text** (left-aligned)
- **Grid:** 5 columns, one step per column
- **Each step card:** `.sk` with different pastel (sky, mint, lilac, butter, peach)
- **Mono number:** 01–05 (large, 30px)
- **H3 title** + short description
- **Arrow SVG** (decorative)

**Current Template Has:**
- ✅ Prose block (for title/intro)
- ❌ 5-column grid of method steps

**Missing:**
- ❌ Method step cards (`.sk` style with numbered sequence)
- ❌ Pastel rotation (sky → mint → lilac → butter → peach)
- ❌ Grid layout for desktop (5 cols), collapse mobile
- ❌ Arrow SVG decoration

**WIDGET TO BUILD:**
- **MethodStepsSection** — 5-step grid with auto-colored sketch cards
- **MethodStep** — Single step card with number, title, description

---

### 6. SERVICES GRID (Six Services)

**Kaleem Design:**
- **Section:** Paper background, padding 96px
- **Title + link to details page** (flex, space-between)
- **Grid:** 3 columns × 2 rows (6 service cards)
- **Each card:** `.sk` + service pastel (butter, sky, peach, mint, apricot, lilac)
- **Card anatomy:**
  - 40×40 line icon (`.ico` class)
  - H3 title (26px bold)
  - 1-line description (16px)
  - "Learn more" link (underlined, 15px)
  - Full card is clickable link

**Current Template Has:**
- ✅ Cards block (for related reading)
- ❌ Service card grid structure

**Missing:**
- ❌ Service card styling (`.sk` + service color)
- ❌ Icon + title + description layout
- ❌ 3-column responsive grid
- ❌ Service color palette mapping

**WIDGET TO BUILD:**
- **ServicesGridSection** — 3×2 grid of service cards
- **ServiceCard** — Card with icon, title, description, auto-assigned pastel color

---

### 7. ABOUT / VALUES SECTION

**Kaleem Design:**
- **Background:** Lilac (`.bg-lilac`)
- **Layout:** 2 columns (1280px, gap 64px)
- **Left column:**
  - H2 "You keep the keys"
  - List of 5 checklist items (with check SVG icons)
- **Right column:**
  - H2 "Our values"
  - 2×3 grid of value pairs (dt/dd)
  - Each has title (19px bold) + description (16px)

**Current Template Has:**
- ✅ Prose block (text + heading)
- ❌ 2-column layout for this section
- ❌ Checklist items with icons

**Missing:**
- ❌ 2-column grid layout
- ❌ Lilac background section
- ❌ Checklist SVG icons
- ❌ Definition list (dt/dd) styling
- ❌ Values grid

**WIDGET TO BUILD:**
- **AboutValuesSection** — 2-column lilac section with checklist + values
- **ValuePair** — Single value (title + description)
- **ChecklistItem** — Item with check SVG icon

---

### 8. WORK / CASE STUDY SECTION

**Kaleem Design:**
- **Layout:** 2-column (5fr left, 7fr right)
- **Left column:**
  - Meta text ("Recent work")
  - H2 heading (44px bold)
  - H3 client name (24px bold)
  - Description (18px)
  - **Tag grid:** 2–4 tags (`.k-tag` class, 28px height, service colors)
  - CTA button
- **Right column:**
  - Browser mockup frame (`.sk` card with `.board` title bar + 3 dots)
  - Placeholder image

**Current Template Has:**
- ✅ Prose block (text)
- ❌ Case study layout
- ❌ Tag styling

**Missing:**
- ❌ 2-column grid (5fr | 7fr)
- ❌ Tag/chip component (`.k-tag` styled)
- ❌ Browser frame mockup (`.sk` with title bar)
- ❌ Image grid display

**WIDGET TO BUILD:**
- **CaseStudySection** — 2-column layout with text + browser frame
- **TagChip** — Service-colored pill badge (`.k-tag` style)
- **BrowserFrame** — Mockup frame with title bar and 3 dots

---

### 9. CONTACT / CTA SECTION

**Kaleem Design:**
- **Background:** Mint (`.bg-mint`)
- **Top border:** 2px ink
- **Layout:** 2-column (text left, SVG right)
- **Left:** H2 heading (52px) + CTA button
- **Right:** Decorative SVG (key illustration)

**Current Template Has:**
- ✅ Prose block (text + heading)
- ❌ CTA section styling

**Missing:**
- ❌ Mint background section
- ❌ 2-column layout
- ❌ Section border styling
- ❌ SVG illustration placement

**WIDGET TO BUILD:**
- **CTASection** — Mint background section with text + decoration

---

## REUSABLE COMPONENTS

### 10. BUTTONS

**Kaleem Design:**
- **`.skb` class** — Sketch button
- **Sizes:** 52px height, 22px padding
- **Styles:**
  - Primary: Mint fill (`.bg-mint`)
  - Secondary: Paper fill (`.bg-paper`)
  - Header CTA: Lilac fill (`.bg-lilac`)
- **Hover:** Translate up-left 1px
- **Font:** Semibold 17px

**Current Template Has:**
- ❌ `.skb` button styling

**Missing:**
- ❌ Button component with `.skb` class
- ❌ Color variants (primary, secondary, header)

**WIDGET TO BUILD:**
- **Button** — Kaleem `.skb` button with color variants

---

### 11. SKETCH CARDS (`.sk`)

**Kaleem Design:**
- **Border:** 2px solid ink
- **Border radius:** Uneven (10px 4px 12px 5px / 5px 12px 4px 10px)
- **Box shadow:** Offset "pen line" effect (4px right + 4px down, paper fill behind)
- **Padding:** 24–48px
- **Pastel fill:** One of 8 colors

**Current Template Has:**
- ❌ `.sk` card styling

**Missing:**
- ❌ Sketch card component
- ❌ Uneven border radius
- ❌ Pen-line shadow effect

**WIDGET TO BUILD:**
- **SketchCard** — Base component for all card-based sections

---

### 12. TAGS / CHIPS (`.k-tag`)

**Kaleem Design:**
- **Height:** 28px (pill-shaped)
- **Padding:** 0 12px
- **Border:** 1.5px ink
- **Border radius:** 999px (fully rounded)
- **Font:** 13px semibold
- **Fill:** Service color (butter, sky, peach, mint, apricot, lilac)

**Current Template Has:**
- ❌ `.k-tag` styling

**Missing:**
- ❌ Tag/chip component
- ❌ Color variants

**WIDGET TO BUILD:**
- **Tag** — Pill-shaped service-colored tag

---

### 13. ILLUSTRATIONS & SVG HANDLING

**Kaleem Design:**
- **Hand-drawn style:** SVG with `feTurbulence` + `feDisplacementMap` filter
- **Illustrations needed:**
  - Open Box (hero, multiple sizes)
  - Decorative arrows
  - Checklist check icon
  - Key icon (contact CTA)
  - Service icons (6 × 40px line icons)
  - Menu icon (mobile)

**Current Template Has:**
- ✅ Media block (can hold SVG)
- ✅ Image component
- ❌ SVG filter support for wobble
- ❌ Icon library

**Missing:**
- ❌ SVG displacement filter setup
- ❌ Icon system (6 service icons + system icons)
- ❌ Illustrated Open Box in multiple contexts

**WIDGET TO BUILD:**
- **IconLibrary** — 6 service icons + system icons (menu, check, etc.)
- **SvgIllustration** — Wrapper for hand-drawn SVGs with wobble filter

---

## FUNCTIONAL COMPONENTS (NOT IN DRAFT)

### 14. MOBILE MENU (Missing from handoff)

**Needed for Kaleem:**
- **Mobile breakpoint:** <672px (currently only has 390px reference)
- **Menu button:** 44×44 lilac button with menu icon
- **Menu state:** Hidden → overlay when open
- **Menu items:** Same nav structure as desktop, stacked vertically
- **Behavior:** Click menu button → toggle visibility, close on link click
- **RTL:** Menu slides from right (RTL) or left (LTR)

**Current Template Has:**
- ✅ Responsive breakpoints
- ✅ Header component
- ❌ Mobile menu functionality

**Missing:**
- ❌ Menu button toggle
- ❌ Sidebar/dropdown overlay
- ❌ Mobile menu state management
- ❌ Keyboard nav (ESC to close, focus trap)

**WIDGET TO BUILD:**
- **MobileMenuButton** — Hamburger button (44×44, lilac)
- **MobileMenuOverlay** — Full-screen or slide-in menu (RTL-aware)
- **MobileMenuLogic** — JavaScript for toggle/close/focus management

---

### 15. DROPDOWN MENU (Desktop, if multi-level nav)

**Kaleem Design:**
- Services page → potentially sub-navigation
- No dropdown shown in current draft, but mentioned in design-system

**Current Template Has:**
- ✅ Header with nav links

**Missing:**
- ❌ Dropdown / multi-level nav
- ❌ Hover states
- ❌ Accessibility (arrow keys, focus management)

**WIDGET TO BUILD:**
- **NavDropdown** — If needed for Services or other sections

---

### 16. FORM / CONTACT (NOT IN DRAFT)

**Kaleem handoff says:** "Contact (free-audit form)" — designed pages not yet included

**Needed:**
- Form inputs (text, email, textarea)
- Form styling (ink outlines, focus states)
- Submit button
- Possibly multi-step form for audit questionnaire

**Current Template Has:**
- ✅ Form infrastructure (Astro form handling)
- ❌ Kaleem-styled form components

**Missing:**
- ❌ Styled form inputs/textarea with sketch aesthetic
- ❌ Form layout and spacing
- ❌ Validation styling

**WIDGET TO BUILD:**
- **FormInput** — Sketch-styled text input
- **FormTextarea** — Sketch-styled textarea
- **ContactForm** — Full contact form page

---

### 17. SERVICE DETAIL PAGE (NOT IN DRAFT)

**Kaleem handoff says:** Need to build from components, not included in draft

**Anatomy (from design-system):**
- **Service detail panel:** `.sk` card
- **Layout:** 5fr / 7fr grid (icon+title+promise | what-we-do+receipt)
- **Icon:** 40×40 line icon
- **Title:** Service name
- **Promise:** One-line value prop
- **Who it's for:** Target audience
- **What we do:** Bulleted list
- **Receipt box:** `.k-receipt` (dashed border, tan fill)

**Current Template Has:**
- ✅ Prose block
- ❌ Service detail layout

**Missing:**
- ❌ Service detail page structure
- ❌ 2-column panel layout
- ❌ Receipt box styling

**WIDGET TO BUILD:**
- **ServiceDetailPage** — Page template for individual service
- **ServiceDetailPanel** — 2-column service description

---

### 18. CASE STUDY PAGE (NOT IN DRAFT)

**Kaleem handoff says:** Case study template + Al Imran Clinic example

**Needed:**
- Case study cover section
- Problem → solution narrative
- Timeline or results section
- Related case studies (cards)
- CTA to contact

**Current Template Has:**
- ✅ Content blocks (prose, images, etc.)
- ❌ Case study layout/structure

**Missing:**
- ❌ Case study page template
- ❌ Case study specific sections

**WIDGET TO BUILD:**
- **CaseStudyPage** — Page template
- **CaseStudyHero** — Hero section for case study

---

### 19. SERVICES HUB PAGE

**Kaleem handoff:** "Services, English, desktop" — services.html

**Anatomy:**
- Similar to home, but Services-focused
- Service detail sections (not in draft, mentioned in design-system)
- Each service: `.sk` panel with icon + title + promise + what-we-do list + receipt

**Current Template Has:**
- ✅ Page structure

**Missing:**
- ❌ Services hub page layout
- ❌ Service detail panels

**WIDGET TO BUILD:**
- **ServicesHubPage** — Services listing page
- **ServiceDetailSection** — Full service detail with 2-col layout

---

## SUMMARY TABLE

| Component | Kaleem Needs | Template Has | Status | Priority |
|-----------|-------------|------------|--------|----------|
| **Header** | Chalkboard nav | Basic header | ⚠️ Restyle | High |
| **Footer** | Chalkboard footer | Basic footer | ⚠️ Restyle | High |
| **Mobile Menu Button** | Hamburger button | ❌ None | 🔴 Build | High |
| **Mobile Menu Sidebar** | Overlay/slide menu | ❌ None | 🔴 Build | High |
| **Hero Section** | Split text+image, pastel bg | Generic layout | ⚠️ Create | High |
| **Problem Cards** | Grid + sketch cards | None | 🔴 Build | High |
| **Method Steps** | 5-col grid, colored cards | None | 🔴 Build | High |
| **Services Grid** | 3×2 service cards | Cards block | ⚠️ Adapt | High |
| **About/Values** | 2-col lilac section | Prose | ⚠️ Create | Medium |
| **Case Study Section** | 2-col + browser frame | None | 🔴 Build | High |
| **Contact CTA** | Mint band + decoration | None | 🔴 Build | High |
| **Sketch Card (`.sk`)** | Base card component | None | 🔴 Build | Critical |
| **Button (`.skb`)** | Sketch button | Generic buttons | ⚠️ Restyle | Critical |
| **Tag/Chip (`.k-tag`)** | Service-colored pills | None | 🔴 Build | Medium |
| **Icons** | 6 service + system icons | None | 🔴 Create | High |
| **SVG Filters** | Hand-drawn wobble | None | 🔴 Setup | Medium |
| **Form Inputs** | Sketch-styled forms | Generic | ❌ Build | Medium |
| **Service Detail Page** | Individual service pages | None | 🔴 Build | Medium |
| **Case Study Page** | Case study template | None | 🔴 Build | Medium |
| **Services Hub** | Services listing page | None | 🔴 Build | High |
| **Kaleem CSS** | Tokens + components | Generic | 🔴 Port | Critical |

---

## PRIORITY BUILD ORDER

### Phase 1: Foundation (Critical)
1. ✅ Port Kaleem CSS (tokens, textures, `.sk`, `.skb`, `.k-tag`)
2. ✅ Create SketchCard component
3. ✅ Create Button component (`.skb`)
4. ✅ Update Header (chalkboard styling, nav links)
5. ✅ Update Footer (chalkboard styling, layout)

### Phase 2: Home Page
6. ✅ HeroSection (split layout, pastel bg)
7. ✅ ProblemCardsSection (4-col grid)
8. ✅ MethodStepsSection (5-col colored steps)
9. ✅ ServicesGridSection (3×2 cards)
10. ✅ AboutValuesSection (2-col lilac)
11. ✅ CaseStudySection (2-col + browser frame)
12. ✅ CTASection (mint band)

### Phase 3: Mobile & Navigation
13. ✅ MobileMenuButton
14. ✅ MobileMenuOverlay
15. ✅ NavDropdown (if needed)
16. ✅ Responsive refinements for all sections

### Phase 4: Sub-pages
17. ✅ ServiceDetailPage + ServiceDetailPanel
18. ✅ CaseStudyPage
19. ✅ ServicesHubPage
20. ✅ ContactForm + form inputs

### Phase 5: Polish
21. ✅ Icons (6 service + system)
22. ✅ SVG filters
23. ✅ Accessibility audit
24. ✅ Cross-browser testing

---

## NOTES

- **Kaleem uses inline styles heavily in handoff** — convert to Astro components/CSS classes
- **Mobile reference only at 390px** — need to design for 672px tablet & 1056px desktop breakpoints
- **No JavaScript in handoff** — need to build menu toggle, form handling, potentially animations
- **RTL thoroughly addressed** — use logical properties (`margin-inline`, `padding-inline`, etc.)
- **Pastel color system is central** — every component needs color variant support

