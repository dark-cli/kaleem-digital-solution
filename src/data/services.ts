/**
 * The six Kaleem services: one colour and one icon each, used everywhere
 * a service appears (homepage cards, Services hero tiles, Services cards)
 * so a service always looks the same. Ids match the #anchors on the
 * Services page.
 */

export type ServiceId = "jailbreak" | "websites" | "mobile" | "systems" | "networks" | "consulting";

/** Background class per service (see the .bg-* colour utilities in global.css). */
export const SERVICE_BG: Record<ServiceId, string> = {
  jailbreak:  "bg-butter",
  websites:   "bg-sky",
  mobile:     "bg-peach",
  systems:    "bg-mint",
  networks:   "bg-apricot",
  consulting: "bg-lilac",
};

/** 32×32 line icons (inner SVG markup, styled by .ico). */
export const SERVICE_ICON: Record<ServiceId, string> = {
  jailbreak:  `<path d="M18 6H6V26H26V14"></path><rect x="20" y="3" width="9" height="9" fill="#faf6ee"></rect>`,
  websites:   `<rect x="4" y="6" width="24" height="20" rx="2"></rect><path d="M4 11h24"></path><path d="M8 8.5h1M11 8.5h1"></path>`,
  mobile:     `<rect x="10" y="3" width="12" height="26" rx="3"></rect><path d="M14 25h4"></path>`,
  systems:    `<ellipse cx="16" cy="8" rx="10" ry="4"></ellipse><path d="M6 8v16c0 2.2 4.5 4 10 4s10-1.8 10-4V8"></path><path d="M6 16c0 2.2 4.5 4 10 4s10-1.8 10-4"></path>`,
  networks:   `<path d="M4 9l18-4l2 9l-18 4z"></path><path d="M14 16v8H6"></path><circle cx="20" cy="10" r="1.5"></circle>`,
  consulting: `<path d="M5 6h22v14H14l-6 5v-5H5z"></path><path d="M10 11h12M10 15h8"></path>`,
};
