# BIRL website

A ready-to-upload static rebuild of [birlab.org](https://birlab.org/), inspected on 3 November 2026. The aim is a small, dependable starting point that can be edited incrementally. The original lab identity, research photographs, bibliography and archives are retained within a simpler navigation structure.

## Preview and launch

Unzip the package, then open `index.html`. Navigation, styles, photographs and fonts work without an internet connection. Links to papers, videos and other external websites still require internet access.

The ZIP contains the website files at its root. Upload the **extracted contents**, keeping their folders intact, to [iida238jp/birlab-website3](https://github.com/iida238jp/birlab-website3) or another repository. The repository root must contain `index.html`, `style.css`, `script.js` and `assets/`.

GitHub Pages can serve these files directly. In **Settings → Pages → Build and deployment**, select **Deploy from a branch**, choose the branch containing this website and the **/ (root)** folder, then save. No build command is needed. The relative links work on both a project URL such as `/birlab-website3/` and a domain root.

This delivery does not publish or modify the live website. No custom-domain file (`CNAME`) is included. If the repository already has one, review it before committing; retain it only if that domain is intended for this deployment.

### Upload through GitHub's website

GitHub limits browser uploads to 100 files at a time. Use these batches:

1. At the repository root, choose **Add file → Upload files**. Upload the root files and the page folders, including `ja/`, but leave `assets/`, `content/` and `reports/` for later. Commit this batch.
2. At the repository root, upload `content/` and `reports/` together in another batch. These are the editable source fragments and inspection evidence; the public pages work without the reports.
3. Use **Add file → Create new file**, enter `assets/images/.gitkeep` as the filename, and commit the empty file. This creates the asset folders.
4. Navigate into `assets/`, choose **Upload files**, and drag in the `fonts/` folder from the extracted package. Commit.
5. Navigate into `assets/images/`. Upload the image files from the corresponding extracted folder in two batches, for example the first 60 files and then the remainder. Commit each batch. Do not rename the files.

Alternatively, GitHub Desktop can commit the complete extracted folder in one operation. Existing unrelated repository files are not automatically removed by an upload. An old homepage must be replaced by this package's `index.html`.

## Exact navigation

| English | Japanese | Page contents |
| --- | --- | --- |
| Home | ホーム | Entrance page for the selected language |
| Research | 研究 | Overview, research projects, previous projects, research videos, simulation and data resources, teaching, related organisations |
| Members | メンバー | Tokyo and Cambridge teams, alumni, dated lab-photo archive |
| Publications | 論文 | Full bibliography, retained publication categories and a separate historical under-review section |
| Events | イベント | Recent announcements, talks and conference links, dated past events, news archive and media coverage |
| Contact | お問い合わせ | Tokyo and Cambridge contacts, visiting information and joining enquiries |

Home / ホーム, the BIRL logo and the lab title return to the entrance page for the selected language. There is no extra News, Resources or Media item in the primary menu. The EN/日本語 switch keeps the same page. The desktop and mobile menus contain the same six items.

The homepage contains a short introduction, three original research images and current news and upcoming-event highlights. Detail pages remain reachable from the main pages. Old `/news/`, `/resources/` and `/media-about-birl-research/` routes have static redirect pages. These are HTML refresh redirects, not server-level HTTP 301 redirects.

## Make small updates

The site has no CMS, database or JavaScript framework.

- Page text lives in `content/en/` and `content/ja/`. Edit the corresponding fragments in both languages when appropriate.
- Run `python3 build.py` from this folder after editing the fragments or `site.json`. Python 3's standard library is sufficient. This regenerates the HTML pages; upload the changed files.
- `site.json` defines the page names, paths, menu and old-route mappings.
- `style.css` controls the shared appearance. `script.js` contains only a small mobile-menu enhancement.
- Research photographs live in `assets/images/`. Keep their aspect ratios. Add a descriptive `alt` attribute and intrinsic `width` and `height` to new images.
- Current-member portraits live in `assets/images/members/` and use square CSS crops. Verified image sources and credits are recorded in `reports/member-portrait-sources.json`. Add personal websites only when the member's identity is confirmed; university and research profiles have separate labels.
- `@ROOT@` inside a content fragment is replaced by the build script with the correct relative path. Use, for example, `@ROOT@research/index.html` rather than `/research/`, so project-hosted Pages links keep working.

For a very quick change, a generated `index.html` can also be edited directly in GitHub's editor. Make the same edit in its matching source fragment before the next rebuild, otherwise it will be overwritten. There is intentionally no automatic rebuild workflow or dependency installation.

To add one member, paper or announcement, update the matching content fragment, rebuild and commit. You do not need to redesign the homepage or add another menu item.

## Content and asset notes

Japanese navigation, primary headings and introductory/contact copy are included. Detailed research descriptions, names, publication titles and historical event material remain in their original language where indicated. This is not a complete translation of every archive entry.

The public website is the content source. Current membership, project status and old publication statuses require the lab's editorial review. Historical dates and claims were not silently updated. Past recruitment notices are kept within dated archives.

All website images and fonts needed for rendering are stored locally. Image variants were sized for web use without cropping. Full-resolution originals are not necessarily included. Research-download ZIPs, publisher pages and video services remain external.

The original BIRL logo, white/grey layout, rust headings, blue links, Poppins headings and Arimo body text are retained. It is a simplified rebuild, not a pixel-identical WordPress clone. The fonts' SIL Open Font License notices are in `assets/fonts/`. Photograph and publication rights remain with the original owners and credited contributors.

See `QA_REPORT.md` for checks and known limitations. `reports/` contains the complete link audit, image inventory, source measurements, migration notes and comparison screenshots.

## GitHub documentation

- [Adding files through the browser](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
- [Configuring the GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
