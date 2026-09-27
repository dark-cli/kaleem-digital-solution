/**
 * The 6-item top navbar. Every real clinic navbar looks like this — Mayo,
 * Cleveland Clinic, Johns Hopkins all top out around 5–7 items. Individual
 * treatment/service pages are reached via the category landing pages listed
 * in the dropdowns, not by cramming 100+ items into the header.
 *
 * The exhaustive taxonomy still lives in `navigation.ts` — it drives the
 * legacy-URL redirect map, sitemap ordering, and any "all pages" listing.
 * Header display uses this file.
 *
 * Each item and column has both English (`label`) and Arabic (`labelAr`).
 * Header.astro picks the right one based on the current locale, falling
 * back to English when Arabic isn't provided.
 */

export interface HeaderNavItem {
  label: string;
  labelAr?: string;
  href: string;
  columns?: HeaderNavColumn[];   // when set, item renders as mega-menu
}

export interface HeaderNavColumn {
  label: string;
  labelAr?: string;
  href?: string;                 // heading may be a link or plain text
  items: HeaderNavLink[];
}

export interface HeaderNavLink {
  label: string;
  labelAr?: string;
  href: string;
}

export const HEADER_NAV: HeaderNavItem[] = [
  { label: "Home", labelAr: "الرئيسية", href: "/" },

  {
    label: "Treatments",
    labelAr: "العلاجات",
    href: "/treatments/",
    columns: [
      {
        label: "Example Category 1",
        labelAr: "فئة المثال 1",
        href: "/treatments/category-1/",
        items: [
          { label: "Add your first condition",  labelAr: "أضف حالتك الأولى",      href: "/treatments/example-1/" },
          { label: "All in category →",         labelAr: "الكل في الفئة ←",        href: "/treatments/category-1/" },
        ],
      },
      {
        label: "Example Category 2",
        labelAr: "فئة المثال 2",
        href: "/treatments/category-2/",
        items: [
          { label: "Add your second condition", labelAr: "أضف حالتك الثانية",      href: "/treatments/example-2/" },
          { label: "All in category →",         labelAr: "الكل في الفئة ←",        href: "/treatments/category-2/" },
        ],
      },
    ],
  },

  {
    label: "Services",
    labelAr: "الخدمات",
    href: "/services/",
    columns: [
      {
        label: "Service Category 1",
        labelAr: "فئة الخدمة 1",
        items: [
          { label: "Add your first service",    labelAr: "أضف خدمتك الأولى",       href: "/services/example-service-1/" },
          { label: "All services →",            labelAr: "جميع الخدمات ←",          href: "/services/" },
        ],
      },
    ],
  },

  { label: "Doctors", labelAr: "الأطباء", href: "/doctors/" },
  { label: "About",   labelAr: "من نحن",  href: "/about/" },
  { label: "Contact", labelAr: "اتصل بنا", href: "/contact/" },
];

/** Pick the label for the current locale, falling back to English. */
export function navLabel<T extends { label: string; labelAr?: string }>(
  item: T,
  locale: "en" | "ar",
): string {
  if (locale === "ar" && item.labelAr) return item.labelAr;
  return item.label;
}
