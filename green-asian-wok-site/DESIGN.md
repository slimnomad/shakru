# Design authority

The selected second image is the visual authority: `../output/green-asian-wok/concepts/02.png`, 1159 × 1358. The user pinned this design; no new direction selection is needed.

Mode: Persuade. The first viewport must make the takeaway identity, location and ordering action obvious. Supporting menu interactions let the customer understand a dish before continuing to the real provider.

## Composition

- Approximately 694px full-width photographic hero at reference size. 5vw horizontal gutters; brush-script brand at upper left, Menu/Find us/Order online at right.
- Tall two-line condensed display headline on the left; warm noodle/chicken photography on the right. Lime primary action and an underlined secondary action.
- 84px service strip with delivery/collection and the street address, separated by thin rules.
- Editorial three-column favourites composition: heading on the left, two food photos with names/prices. The long feature heading intentionally reaches into the next visual column.
- Google-review trust line below a thin rule.

## Tokens and assets

Forest/charcoal `#101913`; warm white `#f8f8ef`; lime `#d1ef72`; secondary text `#c1cbbd`; separator `#48503b`. Anton provides the closest bold display cap height, narrowed horizontally to reproduce the reference. Roboto provides the UI text. Both are real local font files. Headline type is a deliberate exception to generic display-size guidelines because it is pinned by the selected mock.

Raster assets: one full-bleed hero, two individual dish photographs and the transparent wordmark. No CSS/div art or handcrafted illustration substitutes. Upstream Tabler SVGs provide UI icons; standard icon outlines may differ slightly from generated artwork.

## Responsive and interaction states

Below 700px, the header uses a second nav row; the hero text/actions sit above the food photo; service information stacks; dishes become a single-column list. At ≤375px the wordmark shrinks to protect the order action. The same hierarchy and palette remain.

Native dialogs hold menu search, category selection, empty results, details and required-side pricing. Focus rings use lime; disabled ordering remains legible and explains the required selection. Long mobile details retain sticky close/back controls. Motion is confined to a short dialog reveal and restrained hover feedback; reduced motion disables both.

## Accepted differences

Generated food pieces and wordmark brush details differ slightly from the source. The supplied mock has no font metadata, so typeface/width matching is visual. Supporting dialogs and responsive mobile compositions were absent from the mock and are designed to extend it. No unsupported promotional claims, open status or contact number is added.
