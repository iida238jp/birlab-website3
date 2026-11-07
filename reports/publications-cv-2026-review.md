# Publication reconciliation — 7 November 2026

Prepared against `5d4f6ed5bde324245e9e35bd5d97bc3f90c64364` on branch `codex/publications-cv-2026`. Publication was subsequently authorised by the user on 7 November 2026. GitHub Pages publishes the root of `main`.

## Scope and source

The supplied **IidaCV-2026.pdf** is the bibliographic authority. Its complete publication sections, on PDF pages 2–28, contain 347 entries: 16 under-review manuscripts, 168 journals, 13 books/chapters, 138 refereed conference papers, 11 other publications and one patent. Every entry is included; none is excluded. The patent is mapped to the existing Others category. Other CV sections, the PDF itself and private material are not included in this repository.

The request mentions Word hyperlink relationships, but the supplied attachment is a flattened PDF, with **zero embedded hyperlink annotations**. DOI URLs were extracted from its visible text, joined across PDF line breaks and checked against the rendered PDF. No DOI or status was inferred from a preprint or external metadata.

`content/en/publications.html` and `content/ja/publications.html` are maintained source fragments. `python3 build.py` regenerates the two publication pages. No framework, dependency, stylesheet, navigation, image or unrelated page is changed. Japanese introductory copy and category headings are preserved; titles and author names remain in their source language.

## Inventory and counts

The comparison inventory was created before publication edits. [The CSV](publications-cv-2026-inventory.csv) maps every CV entry and every retained website-only entry to a unique record anchor. Matching starts with DOI, then checks titles, author lists, venue, year and article/page identifiers. A DOI conflict on the old Costi citation was resolved by title/authors and the two distinct CV records, rather than by DOI alone.

Counts below are per language; the English and Japanese bibliographies are identical.

| Change | Records |
| --- | ---: |
| Added | 33 |
| Existing CV records updated, including bibliographic details, DOI presentation and venue formatting | 307 |
| Existing CV records retained unchanged | 7 |
| Duplicate old entries removed, retaining their final record | 2 |
| Website-only records preserved, including one uncertain chapter candidate | 113 |
| Total before → after | 429 → 460 |
| Records relocated between categories, included in the update count | 16 |

Of the additions, 32 are clear missing records; one is the CV chapter whose relationship to an old manuscript is unconfirmed. Venue-only formatting changes to retained lab records are not counted as bibliographic updates. The two removed duplicates are He’s 2022 accepted entry, superseded by the 2023 final journal entry, and the repeated 2012 Soft Robotics editorial, consolidated into the CV’s Others record. Six under-review manuscripts are updated and relocated, not deleted from the bibliography.

| Category | Before | After |
| --- | ---: | ---: |
| Journal Papers | 163 | 169 |
| Book Chapters | 21 | 15 |
| Reviewed Conference Papers | 125 | 149 |
| Workshop Contributions and Others | 39 | 43 |
| Thesis / Project Reports | 68 | 68 |
| Under review | 13 | 16 |

## Principal corrections

- Nadipineni’s RoboPatients auditory–tactile paper and Xie’s digital-twin routing paper now have their final journal citations.
- Yuan’s hand–object paper uses SMC 2025, pages 4475–4480 and DOI `10.1109/SMC58881.2025.11342908`. Xie’s EV-routing manuscript uses Applied Soft Computing 183:113624 (2025), DOI `10.1016/j.asoc.2025.113624`.
- Trehan’s EIT gripper and Xie’s helix locomotion manuscripts now appear only as accepted IROS 2026 papers, with the CV titles and author order.
- Nazari’s cross-geometry paper is **accepted**, not under review, in the actual attachment. It remains separate from the related ICRA paper. Zhang’s energy-budgets manuscript remains under review, distinct from “Energy as a common currency…”.
- Added the pendulum Physical Reservoir Control paper, “Energy as a common currency…”, Dowdall’s artificial-body-part paper, Obayashi’s human–robot communication paper and all other missing CV entries.
- All 20 IOP proceedings entries are in reviewed conference papers: 12 added, seven moved from books and the Schofield entry corrected. Schofield now uses “Multiple Musical Skills Framework for Robotic Musicianship”, the CV author order and its DOI.
- Replaced outdated publication details throughout the older bibliography, including citation years, author lists, titles, venues and pages. Kept the four accepted CV entries accepted. Dowdall’s DOI retains the explicit **Preprint DOI** label.
- Journal and journal-series names use `<strong><em>…</em></strong>`. Every DOI is a clickable HTTPS DOI anchor without trailing punctuation in its target. Existing useful publisher, PDF and other links are retained; malformed escaped PDF markup on the IAS-7 record is repaired.
- Dated records are grouped newest first by CV citation year, with unique category-prefixed year IDs. Under-review manuscripts remain separate. Records without a stated citation year are grouped under “Year not specified” / “発行年の記載なし”; conference dates and DOI suffixes are not substituted for publication years.

## Items requiring editorial review

1. **Unconfirmed chapter identity:** the website’s Scimeca/Iida (2020) “Developmental soft robotics”, *Handbook of Developmental Robotics* (in press), may be an earlier version of the CV’s (2022) “Soft Robotics: A Developmental Approach”, *Cognitive Robotics*. Both title and book differ and there is no shared DOI. Both records are retained pending confirmation; shared authors, editors and topic alone are not treated as proof of duplication.
2. **Missing citation years:** `journals-1`, `journals-49`, `conferences-30`, `conferences-67`, `conferences-100`, `conferences-109`, `conferences-110`, `conferences-119`, `others-1` and `others-8` have no explicit citation year. Their bibliographic text is preserved in the undated groups. The 1999 date in `others-8` describes the original MIT Press book, not an established translation date. The patent’s explicit 26.08.2013 date supplies its 2013 grouping.
3. **Literal source discrepancies:** the CV repeats “Leong, F.” in the He 2023 author list and gives pages 9–16 for the 2006 Robotics Society of Japan article, where the old website gave 783–790. The CV values are retained. Other source spellings, including “passivity-baseed”, are not silently rewritten. Mechanical duplicate punctuation and missing word spacing are cleaned without altering bibliographic meaning.
4. **Website-only encoding:** existing malformed names/encoding in old student reports are preserved where the CV supplies no correction. They are not evidence for removing those records.

## Duplicate review

There are no repeated DOI targets in either page. Title and similarity checks were reviewed as well as DOI matches. Distinct publication forms remain separate, including the 2002 IAS-7 / 2003 journal visual-odometer papers, the 2006 conference / 2009 journal bipedal-jogging papers and the 2006 conference / 2009 journal compliant-biped papers. The identical “Iterative product engineering” conference/workshop titles refer to different named events and remain separate. The two “Dynamic locomotion of a biologically inspired quadruped robot” workshop records likewise identify different events. Distinct book chapters in the same edited volume and student reports sharing department wording are retained. The uncertain developmental-robotics chapter pair is identified above.

## Validation

- **57 structural/content checks passed:** HTML5 parsing; unique IDs; all 347 CV mappings; all supplied DOI targets and citation tokens; category order; year heading order and ID accuracy; under-review status transitions; all 68 retained theses; exact English/Japanese bibliographic equality; internal links and fragments; unchanged header/navigation/footer; and the four-page change scope.
- The build succeeds using the existing Python standard-library generator. `git diff --check` passes. No incoming source links to the replaced numeric year IDs were found.
- Desktop previews at 1440 px and mobile previews at 390 px in both languages, plus English at 360 px, show 460 records, loaded local fonts/logo, working mobile menus and no horizontal overflow. Long DOI anchors wrap within the viewport. Screenshots of journals, proceedings, long citations and under-review lists were visually inspected. Shared style and responsive rules are unchanged.
- **601 unique external URLs tested.** See [the link audit](publications-cv-2026-links.csv). There are 379 reachable links, 144 blocked responses (HTTP 403), 54 DNS/TLS/timeout errors, five remote server errors and **19 confirmed legacy 404s**, verified with GET after HEAD. These categories are reported separately. All 316 DOI URLs either reach a publisher (255) or are blocked by it (61); no DOI returns a confirmed 404/410. Publisher blocking is not represented as a broken DOI. Legacy links are retained as requested; unknown replacements are not invented.

HTML5 validation and browser automation used temporary local tools outside the repository. The website gains no runtime or build dependency. Machine-readable results are in [the validation report](publications-cv-2026-validation.json).

## Changed files and preview

Website files:

- `content/en/publications.html`
- `content/ja/publications.html`
- `publications/index.html`
- `ja/publications/index.html`

Review evidence:

- `reports/publications-cv-2026-inventory.csv`
- `reports/publications-cv-2026-links.csv`
- `reports/publications-cv-2026-review.md`
- `reports/publications-cv-2026-validation.json`

Local preview: `http://127.0.0.1:8807/publications/index.html` and `http://127.0.0.1:8807/ja/publications/index.html`. The generated HTML can also be opened directly without a server. To restart the preview, run `python3 -m http.server 8807 --bind 127.0.0.1` from the checkout. The user’s subsequent request authorises merging the verified publication updates and publishing through the existing GitHub Pages configuration.

## Publication follow-up

All 16 under-review manuscripts from the unchanged supplied CV are present, with exact CV author order and titles. All 314 CV DOI identifiers have direct HTTPS DOI links in both languages. Two additional DOI identifiers were already present in the old publisher URLs and have now been made explicit DOI links as well, for **316 DOI anchors per language**:

- Iida/Hara (1999), “Behavior learning of a face robot based on the characteristics of human instruction”: `10.1163/156855399X00577`.
- Nurzaman et al. (2014), “Soft Robotics on the Move…”: `10.1089/soro.2014.0012`.

Their titles, authors, journal, volume, issue and pages were verified against Crossref registration records. The original publisher links and bibliographic records are preserved. Neither identifier was inferred for a paper lacking DOI evidence. Both DOI resolvers reach their publishers, whose automated-access responses are HTTP 403; they are classified as blocked, not broken.
