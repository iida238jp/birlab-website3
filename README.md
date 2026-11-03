# BIRL — English / 日本語

A static, bilingual website for `iida238jp/birlab-website3`.

## Publish on GitHub Pages

Upload the contents of this folder into the repository root, preserving the `ja` and `assets` folders. Replace the existing `index.html`, `style.css`, `script.js` and `README.md`. In repository Settings → Pages, use **Deploy from a branch → main → / (root)**.

- English: `https://iida238jp.github.io/birlab-website3/`
- Japanese: `https://iida238jp.github.io/birlab-website3/ja/`

Both HTML pages are already generated. No installation, backend or build step is needed. Open `index.html` locally for an initial preview; use a local HTTP server for deployment-like checks. Images are stored locally; videos load from YouTube only after activation (or as embedded players when JavaScript is disabled).

## Editing

`content.json` is the shared source for both languages. Member names, papers, image names and video IDs are shared; prose and captions are translated. `build.py` regenerates both HTML pages using Python 3 and macOS `sips` to read image dimensions. Editing this source is optional: the supplied HTML files work as-is.

Navigation contains exactly five section links. The language switch follows the section currently being viewed. The script also handles the mobile menu, keyboard dismissal and embedded video activation.

## Content decisions

- Member roles follow the current birlab.org directory, checked 3 November 2026. The original groups some posts as Research Associates/Assistants without distinguishing individual ranks; this wording is retained.
- No current member portraits were available on that directory. No portraits or positions were invented.
- The group photograph is explicitly labelled as members and alumni at the December 2023 reunion, rather than a photograph of the current team.
- Community photographs depict past events. No unverified future events or job openings are listed.
- Six published papers are included. Titles and complete author lists were cross-checked against Crossref and/or publisher records. The reservoir paper's published title says “though”; this is intentionally preserved despite “through” appearing on birlab.org.
- Paper figures are omitted where a verified reusable figure could not be retrieved. Research photographs are not passed off as images from the selected papers.
- Photographs remain BIRL archive material. Original source URLs and credits are recorded in SOURCES.md. No new licence is asserted for these assets.

## Verification

See VALIDATION.md for completed checks and remaining browser verification limits.
