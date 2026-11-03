# Verification and delivery report

3 November 2026

## Passed

- Inspected the current repository before replacement preparation. The existing homepage was the earlier English-only version.
- Generated English `index.html` and Japanese `ja/index.html` from one shared content source.
- Confirmed identical section order, 15 current member entries, six papers, nine photographs and two video posters in both languages.
- Verified every internal anchor, unique HTML ID, local stylesheet/script/image path, alternate-language destination and image width/height/alt attribute.
- Confirmed five main menu links and minimal remaining links: language switch, home logo, accessibility skip link, six DOI links and one email link per language.
- Confirmed every image file downloaded successfully from its recorded source. Large photographs were resized proportionally and displayed without content cropping.
- Checked JavaScript syntax and exercised both languages using a mocked DOM: repository subpath resolution; section-preserving language switching; mobile menu open/close; Escape focus return; menu closure after navigation; and creation/focus of the correct embedded video player.
- Checked video metadata through YouTube oEmbed and HTTP 200 responses from both youtube-nocookie.com embed endpoints.
- Verified DOI identifiers and publication metadata using Crossref and/or publisher records. Source differences are documented in SOURCES.md.
- Checked CSS brace balance and included desktop, tablet, mobile, reduced-motion, print and keyboard-focus rules.
- Added a no-JavaScript navigation fallback and native embedded video fallback.

## Verification limits

- No browser-control surface was available. Desktop/mobile rendering, actual keyboard traversal in a browser and audiovisual playback have not been visually verified. Mocked-DOM checks are not a substitute for those checks.
- Video playback requires internet access and is subject to YouTube/browser restrictions. A successful embed endpoint response does not prove playback on every device.
- Publisher protections prevented retrieval of some figures; unrelated photographs were not substituted as paper figures.
- The original member directory does not provide current individual portraits or distinguish every research associate/assistant rank. Those details are not invented.

## Publication status

The attempted GitHub write failed with HTTP 403, “Resource not accessible by integration”. No branch or commit was changed by this work. The live website was not updated, and deployment was not verified.

The ZIP contains the complete static website and can be uploaded to the repository root while preserving its history through a normal GitHub commit.
