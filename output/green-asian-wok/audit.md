# Green Asian Wok website and review analysis

Reviewed on 10 October 2026, Europe/Dublin. The supplied Maps link resolves to Green Asian Wok at 283 Harold’s Cross Road, Dublin 6W. Its listed official website is [greenasianwok.ie](https://www.greenasianwok.ie/).

The strongest opportunity is to help people choose food earlier and make ordering details easier to trust. The site has a visible Order Now action, a working menu, item prices and allergen information. Its homepage puts a large generic food banner and app advertising ahead of dish discovery. The order journey adds a separate fulfilment page on desktop, then another large banner before the menu. The redesign should keep the working ordering service while improving the customer-facing site.

## What customers say

The [Google listing](https://maps.app.goo.gl/bk5NyCFTQz4Ywi8aA?g_st=ic) showed **4.5 stars from 6 reviews**: five five-star ratings and one two-star rating. Five individual review records were exposed during this run after checking the default, lowest-rated and newest sorts. Four contained written comments; the two-star review had no visible comment. The sixth individual record was not exposed, so its content is unknown. Google labels these reviews as unverified. The small sample does not support a broad claim about delivery reliability or sustained consistency.

| Visible reviewer | Rating | Observed theme | Website implication |
| --- | --- | --- | --- |
| Sean Waters | 5 | Enjoyed the food and singled out sweet-and-sour chicken | Give this dish a clear photo, price and route into the menu |
| Linjie Yang | 5 | Positive about price and food quality | Show prices clearly before customers commit to ordering |
| Camila Yanez | 5 | Enjoyed the food and portions | Use honest serving photography and verified portion descriptions |
| V-Cat | 5 | Positive about flavour, authenticity and affordability | Present a clear local food identity instead of a generic provider template |
| Lisa Marie | 2 | No written explanation visible | Do not invent a complaint; provide a clear support route and investigate directly |

These themes describe the observed comments, not measured prevalence among all customers. The reviews mention food and value, not the website. The relationship between those comments and design recommendations is an inference.

The search also found the business on [Just Eat](https://www.just-eat.ie/restaurants-green-asian-wok-dublin/menu) and [Deliveroo](https://deliveroo.ie/menu/dublin/rathgar/green-asian-wok). Platform menu and delivery terms can differ; they should not silently replace direct-order prices. The concepts use prices verified in the official menu: Sweet & Sour Chicken €11.00, Salt & Chilli Chicken Strips €6.80 and Deep Fried Chicken Gyoza €7.80.

## Captured journey and findings

1. **Desktop homepage, 1280 × 720.** The primary CTA is visually prominent, and the business address appears in the hero. The hero does not explain the cuisine beyond the business name or preview a priced dish. App-store badges compete with the order task. Small white text lies over a busy photo. DOM inspection found the Order Now text and enclosing divs have no button/link role and tabindex −1; the desktop navigation headings are used as controls. This is a concrete semantic and keyboard-access risk. Implement navigation as links, and actions as buttons with visible focus.

![Desktop homepage](/Users/aliassylkhan/Desktop/learningsh/output/green-asian-wok/evidence/01-home-desktop.jpg)

2. **Desktop fulfilment selection.** Order Now reaches a separate delivery/collection page. The collection interval is printed as two adjacent ranges, 00:00–01:00 and 16:00–01:00. This is difficult to interpret across midnight. Offer modes on the same menu surface and show day-specific availability in plain language from one confirmed schedule.

![Delivery and collection selection](/Users/aliassylkhan/Desktop/learningsh/output/green-asian-wok/evidence/02-order-type-desktop.jpg)

3. **Desktop menu entry.** Selecting Collection loads the official menu. Item prices and allergen text are available, but the first viewport is largely a promotional banner, address block and empty basket. Dishes require scrolling. There are sixteen category labels. Bring popular dishes and search into the opening viewport, group categories coherently and make the empty-basket state useful.

![Desktop menu entry](/Users/aliassylkhan/Desktop/learningsh/output/green-asian-wok/evidence/03-menu-desktop.jpg)

4. **Dish options.** Sweet & Sour Chicken opens a side-selection panel. The initial Add to order action is disabled without an explanation that a side is required. Selecting boiled rice correctly changes the displayed total from €11.00 to €11.60. At the captured scrolled state, the top of the panel is obscured by the fixed header. Add an explicit “Choose one side” requirement, retain a visible close action and keep the whole dialog within the available viewport. Use semantic radio controls and restore focus when it closes.

![Dish options](/Users/aliassylkhan/Desktop/learningsh/output/green-asian-wok/evidence/04-dish-options-desktop.jpg)

5. **Mobile homepage, 390 × 844.** The page reflows and the order action is visible. An Ever Dish install banner occupies the top of the page; the business identity and meaningful dish choices receive less space. Make the menu the first useful content, and place optional app promotion later in the journey. Reduce the amount of small italic copy over photography.

![Mobile homepage](/Users/aliassylkhan/Desktop/learningsh/output/green-asian-wok/evidence/07-home-mobile.jpg)

6. **Mobile menu entry, 390 × 844.** A large banner, restaurant card, address, opening intervals, provider promotion and allergy contact block precede the category list. The fixed basket action says Minimum Order €0 for delivery, even though the basket is empty. Use an explicit empty-basket message and a basket count; show delivery eligibility and fees when the mode/address makes them relevant.

![Mobile menu entry](/Users/aliassylkhan/Desktop/learningsh/output/green-asian-wok/evidence/08-menu-mobile.jpg)

## Highest-impact improvements

| Priority | Change | Reason | Acceptance evidence |
| --- | --- | --- | --- |
| P1 | Reconcile contact number and opening schedule | Maps shows 01 265 9610; the website shows 01 491 0221 / 085 199 6556. The correct contact cannot be established from these sources alone | Confirm with the business; use the confirmed record consistently across site, provider and listing |
| P1 | Use native links, buttons and radio inputs | Core controls are not exposed with expected semantics | Complete browsing, mode selection and item configuration using keyboard alone; verify accessible names and focus |
| P1 | Put menu discovery ahead of provider promotion | Customers cannot assess the food or prices on the homepage | A dish photo, name, price and menu action are visible without scrolling at the agreed desktop/mobile breakpoints |
| P2 | Simplify the entry to ordering | A fulfilment page and another banner delay dish discovery | Browse without an address; select mode inline; carry selection into the ordering provider |
| P2 | Fix modal layout and required-option guidance | The dish panel is partly under the header, and the disabled CTA does not explain the requirement | Full panel stays usable at 390 × 844 and 1280 × 720; required side and final price are clear |
| P2 | Add honest, linked social proof | Positive feedback is absent from the homepage | Display the actual rating together with its count and a source link; retain the small sample size |
| P2 | Improve support and content quality | Conflicting numbers, confusing hours and provider-oriented copy weaken confidence | Confirm operational data; proofread copy; use a clear help/contact route |
| P2 | Correct the sitemap target | The footer links to /sitemap/www.mjchinese.ie/sitemap.xml on the Green Asian Wok host | Verify a sitemap for the actual business domain in the production implementation |

No analytics or conversion measurements were available, so the report does not claim a measured conversion uplift. Image contrast is a visible risk; a full contrast audit needs computed colours for every state. A full accessibility audit, payment flow, real order acceptance, delivery eligibility, backend resilience and field validation were outside the inspected journey. No order or feedback was submitted.

## Three visual deliverables

The three concepts are saved as [image 1](/Users/aliassylkhan/Desktop/learningsh/output/green-asian-wok/concepts/01.png), [image 2](/Users/aliassylkhan/Desktop/learningsh/output/green-asian-wok/concepts/02.png) and [image 3](/Users/aliassylkhan/Desktop/learningsh/output/green-asian-wok/concepts/03.png), in the order displayed in chat. They explore different structures and visual systems. Images are concept visuals; depicted food and the storefront/map in the first image are generated illustrations and must be replaced with verified business assets for a production site. The first image has a small generated-text artefact in its supporting copy. The third image groups mixed-category dishes under a selected Starters label; a built menu should call this section Favourites or use a matching category. These are recorded refinements for implementation, not evidence about the current business.

The System Design document specifies a proposed implementation boundary and acceptance checks. It does not claim access to undocumented provider APIs or that a website implementation has been completed. Source-to-implementation Design QA will apply after a concept is selected and rendered as a working site.

## Verification completed

- Desktop homepage → mode selection → collection menu → sweet-and-sour category → dish options were exercised.
- Boiled-rice selection updated the item total by the observed €0.60 surcharge.
- Mobile homepage and menu were captured at 390 × 844; desktop evidence used 1280 × 720.
- Captured website images were saved, opened and visually inspected; loading captures were rejected and replaced.
- Browser console capture returned no error or warning entries for the mobile menu at the time checked. This is not a full performance or resilience test.
- Google default, lowest-rated and newest review views were inspected; limitations above are retained.
- Exactly three independent image-generation calls used the captured site as a reference. Images were inspected for business name, layout, price and rating accuracy.
- The document was cloned from the selected retained reference, rendered and checked. Automated artifact checks are recorded in verification.txt.

The next implementation pass should use the chosen concept, replace illustrative assets, confirm operational data, implement the core menu interactions, then run responsive, keyboard, provider-handoff and source-comparison tests before production release.
