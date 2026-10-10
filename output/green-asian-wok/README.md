# Green Asian Wok redesign research

This package contains a screenshot-based website audit, review analysis, three independent redesign images and a System Design document cloned from the selected template. Research date: 10 October 2026, Europe/Dublin.

- `audit.md`: findings, screenshot evidence, review sample and limitations.
- `concepts/01.png`, `02.png`, `03.png`: the images in their chat display order.
- `green-asian-wok-system-design.docx`: the requested System Design template document.
- `menu-contract.schema.json`: proposed display contract, not a provider API.
- `verification.txt`: checks completed on this delivery package.

Website interactions were checked in the Codex in-app browser. No real order or feedback was submitted. The verified price examples are Sweet & Sour Chicken €11.00, Salt & Chilli Chicken Strips €6.80 and Deep Fried Chicken Gyoza €7.80. A boiled-rice selection increased the first dish by €0.60.

The concept imagery is generated. Real food photography, storefronts, maps, approved brand assets and operational details must be confirmed before production. Google showed six ratings, but only five individual records were exposed in the inspected views. The website and Google disagree on the phone number.

The site has not been implemented in this package. After a concept is selected, the intended delivery is a responsive working menu, supported provider handoff, keyboard and mobile checks, and Design QA against the selected image. The acceptance checks are detailed in the Word document. The three images have been delivered as the requested visual exploration.

The local artifact verification suite is `tests/verify_deliverables.py`. It uses the retained reference and evidence contract in this task’s `tmp/green-asian-wok/` directory, and a temporary JSON Schema validator installed there. Run with the bundled Python runtime advertised in the workspace dependencies. Six checks pass; see `verification.txt`.
