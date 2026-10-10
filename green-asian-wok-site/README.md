# Green Asian Wok — design 2

A responsive implementation of the selected “Wok After Dark” concept using **plain HTML, CSS and JavaScript**. No React, JSX, TypeScript or browser runtime dependencies.

## The three source files

- `index.html` — semantic page content, navigation, featured dishes and native dialogs.
- `src/style.css` — self-hosted fonts, design tokens, responsive layouts, focus/hover states and reduced motion.
- `src/script.js` — menu search/category filters, dish details, side selection, live EUR totals, dialog focus return and ordering handoff.

All images, fonts and icons are local in `assets/`. You can open `index.html` directly in a modern browser. You can also serve the directory with any static web server.

For development:

```sh
npm ci
npm run dev -- --host 127.0.0.1 --port 4173 --strictPort
```

The running preview is `http://127.0.0.1:4173/`. Vite is only the development server. Production is the original static HTML/CSS/JS, copied without a frontend framework or transpilation.

## Verify and build

```sh
npm test
npm run test:sites
```

`npm test` first builds the static output and then runs 11 Node tests. They cover integer-cent EUR formatting, required-side pricing, search/category intersections, invalid selection handling, escaped content, verified records, missing assets and hosting behavior. Browser checks cover real interactive states and responsive layouts; see `design-qa.md` and `evidence/`.

`npm run build` writes the standalone website into `dist/client/`, plus the existing Sites-compatible Worker and hosting metadata. Deploy `dist/client/` to an ordinary static host. No deployment has been performed. `npm run format` formats the source.

## Behavior and factual limits

- Header Menu, See the menu and View menu open a searchable favourites menu. Mains/Starters filters intersect with the search. Empty results offer a working reset.
- Featured dishes open details and allergen information. Sweet & Sour Chicken requires one side before continuation. Boiled Rice/Chips add €0.60; Fried Rice adds €1.00; Fried Noodles adds €2.00. Prices use integer cents.
- Order online opens the restaurant’s existing delivery/collection selector. Continue to order and the full-menu link open the official ordering menu. The local selections are **not transferred**; the UI explains that the customer selects and pays on the provider page. No payment, order submission or fake confirmation is implemented.
- Find us shows the verified address and directions. Read the reviews opens the user-supplied Google Maps listing.
- Native dialogs support Escape, keep keyboard focus inside the active task, and restore focus to the trigger. The long mobile dish view keeps its close/back controls visible. Search/results are labelled; price updates use a live region. Reduced-motion settings are respected.
- Three verified favourites are shown; this is not an invented full restaurant menu. The full menu is available through the official provider.
- Business address, prices and allergens came from the 10 October 2026 audit. The homepage preserves the supplied mock’s 4.5/6 Google-review snapshot. Contact numbers and collection hours conflicted between sources, so neither is guessed here. Update the snapshot and menu facts before a public launch.
- No customer details, analytics, cookies, authentication, API keys or persistent storage are used.

## Assets and evidence

Reference: `../output/green-asian-wok/concepts/02.png` (1159 × 1358).

Food photographs and the supplied-concept wordmark were individually prepared with Image Gen, then converted to WebP. Food images are illustrative, not verified photographs of the restaurant’s actual dishes. Original renders are retained in `evidence/source-assets/`. Fonts are self-hosted Anton and Roboto from [Google Fonts](https://github.com/google/fonts); OFL licenses are included. Icons are from [Tabler Icons](https://github.com/tabler/tabler-icons), with its MIT license. The Google G is the public Google brand mark, used only to identify the review platform.

The dark forest background, lime actions, condensed editorial headlines and photography follow the chosen concept. Supporting dialogs extend the same design. Source selection, measurements, comparisons and acceptable differences are documented in `DESIGN.md` and `design-qa.md`.
