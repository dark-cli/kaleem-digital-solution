import * as React from "react";
/** A service id or a pastel. One colour = one service: jailbreak butter, websites sky, mobile peach, systems mint, networks apricot, consulting lilac. */
type Service = "jailbreak" | "websites" | "mobile" | "systems" | "networks" | "consulting";
type Pastel = "butter" | "sky" | "peach" | "mint" | "apricot" | "lilac" | "paper" | "gray";
type Tone = Service | Pastel;
/** The Open Box mark with the wordmark. `lang`: "en" kaleem, "ar" كليم, "both", "mark" (icon only). Inside a `.kl-board` element it switches to chalk. */
export declare function Logo(props: { lang?: "en" | "ar" | "both" | "mark"; size?: number; href?: string; className?: string }): JSX.Element;
/** Sketch button, 52px (40px with size "sm"). kind "elevated" (.skb, lifts on hover), "flat" (.fbtn) or "link" (underlined ink text). */
export declare function Button(props: { kind?: "elevated" | "flat" | "link"; tone?: Tone; size?: "md" | "sm"; arrow?: boolean; href?: string; disabled?: boolean; onClick?: React.MouseEventHandler; children: React.ReactNode; className?: string }): JSX.Element;
/** Pill tag with an ink outline; optional pastel fill for the service it names. */
export declare function Tag(props: { tone?: Tone; lang?: string; children: React.ReactNode; className?: string }): JSX.Element;
/** One service as a pastel sketch card: line icon, title, one line, optional inclusions. Lifts on hover when it has an href. */
export declare function ServiceTile(props: { service: Service; title: React.ReactNode; description?: React.ReactNode; items?: React.ReactNode[]; icon?: boolean; href?: string; dir?: "ltr" | "rtl"; lang?: string; className?: string }): JSX.Element;
/** A proof number in Plex Mono with a short muted label. Always LTR inside Arabic text. */
export declare function Stat(props: { value: React.ReactNode; unit?: React.ReactNode; label: React.ReactNode; dir?: "ltr" | "rtl"; lang?: string; className?: string }): JSX.Element;
