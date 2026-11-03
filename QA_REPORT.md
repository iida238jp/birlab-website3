# Inspection report

Inspected 3 November 2026. Source: https://birlab.org/. Delivery: a static ZIP for manual GitHub upload. No repository commits, pull requests, DNS changes or live publication were performed.

## Structure and content

- Five main menu items in the requested order, with separate pages in English and Japanese.
- 34 content pages, including the two homepages and retained research/workshop detail pages, plus six compatibility redirect pages: 40 HTML pages in total.
- News and media are within Events; resources and teaching are within Research; joining information is within Contact.
- The full source bibliography is retained, apart from two clear duplicate records: a repeated flow-cup article and an under-review record whose accepted version was already listed. The exact records appear in `reports/migration-notes.json`.
- Original research, member/alumni and dated photo content is retained. Original footer affiliation links and mismatched resource download targets were corrected. Obsolete wiki edit-question-mark links were removed while their surrounding text was preserved.
- Past events are grouped and ordered by date. Duplicate EI 2024 announcements were consolidated, and two event entries that were joined together in the source were separated.
- Tokyo's exact visiting address was not available on the original contact page, so the page asks visitors to contact the laboratory. No street address or room was invented.

## Visual and functional checks

- All 40 generated HTML pages were checked for local link targets, fragment targets, image references, image alternative text and the five-item navigation structure: **zero internal-link or missing-file errors** in the final package.
- The 12 primary English/Japanese pages were checked in the browser at 1440 and 390 pixels wide. Additional checks covered all 12 at 1280 and 360 pixels. No horizontal overflow or broken loaded images was detected in those checks.
- The mobile menu and equivalent-page language switch were exercised. The shared script produced no browser console errors in the checked views.
- The project-path preview was served at `/birlab-website3/`; links use explicit relative `index.html` paths, also designed to support an extracted local preview. Direct file-URL browser automation was unavailable; the working preview was verified over local HTTP.
- Original and rebuilt desktop screenshots are included. Additional rebuilt phone screenshots and views of the resources section, member-photo archive and narrow-screen menu are included. The screenshots show representative views, not every scroll position of every archival page.
- Source images were measured and local assets checked for valid dimensions. The site uses 110 distinct displayed images, with one additional image linked from its attachment page. An unavailable legacy Geyer illustration was replaced with a descriptive research-page link rather than a fabricated image.
- Photographs use uncropped, proportionate sizing. Original image widths informed the rebuild. The header and page spacing are simplified; the old sidebar and widgets are removed. The result preserves the original visual identity rather than matching every WordPress dimension exactly.

## External-link audit

All **560 unique external URLs** in the final HTML were attempted. The report distinguishes a successful HTTP response from inaccessible or unverifiable destinations:

| Result | URLs |
| --- | ---: |
| Reachable (HTTP 2xx) | 260 |
| Unavailable (HTTP 404 or 410) | 81 |
| Unverified: access restriction / anti-bot response | 127 |
| Unverified: remote server error | 4 |
| Unverified: network failure or timeout | 88 |

44 legacy IEEE links were normalized to document URLs while preserving their article IDs. Incorrect fragments of resource download links were repaired using the source's correct matching targets. The remaining unavailable legacy downloads are labelled on the Research page.

The report does **not** claim that every external link is working. Many archive references, old recruitment pages and former institutional pages are no longer available. Historical links are retained to preserve the source record. HTTP 403/418 and similar responses are not treated as proof that a publisher page is broken. A successful HTTP status also does not guarantee that an external page still contains its original content; the audit is automated reachability checking with focused manual inspection, not a semantic review of all 560 destinations.

`reports/external-links.json` records each URL, source pages, link labels, status, final URL and available page title. `reports/unavailable-links.csv` is a shorter list of the 404/410 results for later editorial work. `reports/link-corrections.json` lists the IEEE URL changes.

## Suggested next editorial updates

1. Confirm the current member lists and Tokyo visiting details.
2. Review the old under-review publication section against the lab's current bibliography.
3. Replace or archive unavailable research-download files and important external links.
4. Add new announcements to Events and promote only a few to the homepage.
5. Translate detailed Japanese research and archive copy incrementally if desired.

These content-review items do not prevent the static prototype from running. The live birlab.org website remains unchanged.
