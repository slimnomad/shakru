# Design QA

final result: passed

Source visual truth: `/Users/aliassylkhan/Desktop/learningsh/output/green-asian-wok/concepts/02.png`.
Implementation: `http://127.0.0.1:4173/`.
Source pixels: 1159 × 1358. Final implementation screenshot: `evidence/desktop-final.jpg`, 1159 × 1358 pixels. Desktop CSS viewport: 1159 × 1358, DPR 1; no density resampling. Final capture is at scrollY 0 with closed dialogs and no focused control. The document is 1359px tall. The first desktop capture was scrolled 21px, so its vertical offsets were excluded from precise findings.
State: closed dialogs, home page, dark theme. Mobile supplemental viewport: 390 × 844, DPR 1.

## Comparison history — pass 1

Full view: `evidence/comparison-pass1.jpg`, combines the source and browser capture in one image. Mobile: `evidence/mobile-pass1.jpg`; interactive options: `evidence/mobile-dish.jpg`.

- [P1] Headline is too wide. The first line extends farther into the food than the source. Fix: condense Anton horizontally to .86 while keeping its matching cap height and line rhythm.
- [P2] Featured grid expands the first track to the heading’s min-content width, pushing dishes to the right. Fix: use `minmax(0, …fr)` tracks, enlarge the feature heading cap height and condense its width to retain the source’s editorial overlap.
- [P2] Footer and featured section make the page taller than the source. Fix: set the hero to its measured 59.9vw, reduce feature bottom padding by 8px and set the footer to 139px with a 30px top inset.
- [P2] On mobile, photography lies behind the secondary menu action. Fix: start the photograph beneath the actions, at 430px.

## Comparison history — pass 2

Full view: `evidence/comparison-final.jpg`. Focused paired regions: `evidence/hero-detail.jpg`, `evidence/feature-detail.jpg`, `evidence/header-detail.jpg`.

The four pass-1 corrections are visible: the headline width now fits the same left-hand area, the first dish starts at the measured grid column, the footer aligns near the source’s divider, and the mobile secondary action has a dark, quiet background. Desktop page height is 1359px versus the 1358px source, with no horizontal overflow.

Supplemental 320px browser geometry found a 6px overlap between the wordmark and order button. [P2] Fixed by sizing the wordmark to the available width at ≤375px. Long mobile dish dialogs also benefit from a persistent close/back row; [P2] corrected with a sticky dialog header. These are responsive/interaction states absent from the source mock.

The initial tablet full-page capture had inconsistent clipping despite DOM geometry reporting no overflow. Replaced it with a fresh viewport capture after reload. Before/after capture geometry confirms scrollY 0, a wordmark at y22.33 and an order button at y20.

## Final confirmation

No actionable P0/P1/P2 findings remain. `evidence/comparison-final.jpg` was refreshed from the final desktop screenshot and reopened alongside paired header, hero and featured-dish regions. The major regions, type hierarchy, headline wrapping, grid, buttons, prices, address and review strip preserve the selected concept. Overall page-height drift is 1px.

- `evidence/mobile-320-final.jpg`: 320 × 780 pixels/CSS viewport, DPR 1. No document overflow; wordmark ends at x178 and Order starts at x202.03, leaving a 24.03px gap.
- `evidence/mobile-final.jpg`: 390px-wide full-page capture from a 390 × 844 CSS viewport, DPR 1. Text/actions remain readable above the photograph; service rows and dishes stack; footer links wrap deliberately.
- `evidence/tablet-final.jpg`: 768 × 1024 pixels/CSS viewport, DPR 1. No horizontal overflow; all actions remain available. The longer chicken-strip label wraps naturally onto two lines.
- `evidence/mobile-dish-final.jpg`: 390 × 844. Persistent close/back row visible while the form is scrolled; Fried Noodles selected and live total is €13.00.

Density normalization was unnecessary: all comparison and supplemental screenshots are DPR 1. Combined images add only a labelled gutter; source and implementation pixels are not stretched.

## Required fidelity surfaces

- Fonts: self-hosted Anton for tall condensed display lettering, Roboto variable for UI. Reference typography is visual, with no font metadata. Anton’s matching cap height and corrected width preserve the reference hierarchy; feature type has the corrected size/width/line rhythm. Body copy, labels and prices remain legible and use appropriate regular/bold weights. Fonts report loaded; no fallback or truncation observed. Small differences in generated letter shapes are accepted P3 variation. Roboto is chosen to match the supplied image, so the detector’s generic overused-font warning is intentionally accepted.
- Spacing: 5vw margins, measured 694px hero and 84px service strip match the reference scale. Corrected grid tracks restore dish alignment; footer divider and page height match within 1px. No unintended overlap remains at tested sizes; editorial heading overlap is intentional and follows the source.
- Colors: forest/charcoal `#101913`, warm white `#f8f8ef`, lime `#d1ef72`. Main copy remains white/lime against a dark background. Dark CTA text is used on lime.
- Image quality: four individually prepared image assets (hero, both featured dishes, wordmark), WebP delivery, no CSS art. Photo subjects, dark plates, warm light and peppers/scallions match. Generated compositions are expected to differ in individual food pieces. Icons use upstream Tabler SVGs; Google uses its supplied public raster mark.
- Copy: all headline/navigation/featured prices/address/review-count copy preserved. Dialog copy adds verified menu facts and honest provider handoff. No unsupported hours, contact number, delivery ETA, awards, or fake reviews.

## Interaction evidence

Tested in browser: Menu opens; SWEET search produces one result; dish details show allergens; required side disables continuation; Boiled Rice selects and changes the live total to €11.60; Back to menu retains the query; category/search intersection has a visible empty state; Reset restores all 3 dishes; Escape closes the dialog and restores focus to Menu; Find us opens the address/directions and Close returns focus to Find us; Fried Noodles changes the total to €13.00; Continue to order reaches the real official menu at `https://www.greenasianwok.ie/shopDetail?rId=3238`. No purchase or order was placed.

All 11 automated tests pass, including all four existing hosting checks. JavaScript syntax check passes. Browser console check after final local reload returned no warnings or errors. All images report complete with nonzero natural dimensions. Native focus containment, labels, alt text, lime focus indicators and reduced-motion CSS were checked. No authentication, persistence or customer-data entry is part of this frontend.

## Implementation checklist

- All source assets placed and optimized locally.
- All P0/P1/P2 fixes confirmed by browser-rendered evidence.
- Desktop/full-view and focused comparisons completed.
- 320px/390px/768px layouts and primary interactions verified.
- Console, images, syntax, automated tests and real provider handoff checked.
- Local browser preview remains open; viewport override reset.

## Follow-up polish

P3 only: source lettering has no exact font metadata; generated brush details/food pieces and upstream Tabler icon outlines differ slightly. Those accepted visual variations do not alter composition or use. No blocking test gaps remain within the requested frontend scope. Real provider payment/fulfilment remains outside this implementation and was not submitted during testing.
