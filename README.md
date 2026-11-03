# BIRL minimal prototype

Two static homepages: `index.html` (English) and `ja/index.html` (Japanese). No dependencies, images, external requests or production changes.

## Preview

Double-click `index.html`, or run `python3 -m http.server 8765 --bind 127.0.0.1` in this folder and visit http://127.0.0.1:8765/. Use the EN / 日本語 switch to change language.

## Edit

All wording is in **content.json**, organised under `en` and `ja`.

- Opening: `lab`, `affiliations`, `statement`.
- Sections: `sections.research`, `sections.people`, `sections.publications`, `sections.community`, `sections.join` — edit each `heading` and `text` in both languages.
- Footer uses `lab`.

After editing, run **python3 build.py** once to regenerate both homepages. Python uses only its standard library. The generated pages need no build process to view or host.

`layout.html` is the shared page template; `style.css` controls both languages. `script.js` preserves the section when switching languages. Navigation remains fully visible on mobile and wraps onto additional lines where necessary.

This is a local prototype. Nothing was committed to the repository or deployed, because commits on the live Pages branch could publish it. The existing repository's static HTML/CSS and optional Python-generation approach is retained in simplified form.

Validation: both language pages, five section anchors, all local file paths and language paths checked; JavaScript syntax and section preservation checked with a mocked DOM. Responsive rules checked at the source level; browser rendering could not be verified because a browser test runtime is unavailable.
