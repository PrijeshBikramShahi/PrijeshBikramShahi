# Profile evidence audit

Reviewed 2026-11-01 (Asia/Kathmandu). The audit inspected public repository metadata, manifests, documentation, representative source and tests, screenshot assets, GitHub Actions runs, and release listings. It did not rerun the product suites or independently rebuild every product. Documentation reports are attributed evidence, not fresh test results.

## Starting point

Baseline: `e654aef` on `main`, clean working tree. Original assets: seven numbered SVG panels, four featured cards, three compact cards and four contact icons. Almost all copy was image-only. Two- and three-column tables reduced text legibility on mobile. The new README keeps the terminal identity and cards, while using native headings, paragraphs and links. No badges or contribution counters were added.

## Inspected public revisions

| Repository | Revision |
| --- | --- |
| stow | [`ae5cbbd37a54`](https://github.com/PrijeshBikramShahi/stow/commit/ae5cbbd37a54e9a1f36217641f18343c79aceb8c) |
| topside | [`25b519da0c9e`](https://github.com/PrijeshBikramShahi/topside/commit/25b519da0c9edebd64e4aa1e458698a2cb4ac138) |
| khoj-app | [`f08ce54d3027`](https://github.com/PrijeshBikramShahi/khoj-app/commit/f08ce54d30276858e188295e6e7b6d66239b4c97) |
| loomrail | [`b745b3f84e45`](https://github.com/PrijeshBikramShahi/loomrail/commit/b745b3f84e45445a25a0c67b26370d63b7c2b727) |
| accord | [`971ec72a19b4`](https://github.com/PrijeshBikramShahi/accord/commit/971ec72a19b4eeb6f3f2ac02e5b503f85b83a8e8) |
| coderoom | [`0f4bf5f85215`](https://github.com/PrijeshBikramShahi/coderoom/commit/0f4bf5f85215021dd728122798345283436bcdfc) |
| mac-widget-platform | [`2c9df5e49d15`](https://github.com/PrijeshBikramShahi/mac-widget-platform/commit/2c9df5e49d159b38dc6389948f4c947d4c8143a4) |

## Selection

| Project | Evidence and reason to feature | Boundaries |
| --- | --- | --- |
| Stow | Tauri/Rust and React manifests; SQLite registry and operation-journal architecture; clone implementation; Git pull and frontend sync tests; detailed verification record. | No published GitHub release or public application screenshots found in the audited tree. Prior local verification is not a new test run. |
| Topside | Swift package separates native app from core; interaction reducer tests; build instructions; real application screenshots. | Source distribution, device/permission testing and VoiceOver gaps are documented. |
| Khoj | Flutter manifest, Provider-backed map view model, use cases/data layers, architecture notes and two focused domain tests. | Original and layered entry points coexist. Not an app-store release; no public UI screenshot found. Tests do not demonstrate API integration or end-to-end reliability. |
| Loomrail | React/Fastify manifests, approval tests, versioned contracts and architecture decisions, recorded fixture walkthrough, evaluation screenshot and successful remote CI. | Local single-operator scope. Fixture evaluation is not model-quality evidence. No published GitHub release. |

Loomrail was selected over Accord and CodeRoom because it combines public architecture decisions, backend/recovery test evidence, a walkthrough, screenshots and successful CI. Accord has substantial local workflow evidence and a narrower cloud preview; CodeRoom describes itself as a collaboration prototype. Widgion remains discoverable with screenshots and behavior checks.

Public Actions evidence: [Loomrail Checks run 39015699898](https://github.com/PrijeshBikramShahi/loomrail/actions/runs/39015699898) completed successfully at the inspected head. The workflow runs `npm ci` and `npm run check`. No Actions runs or GitHub releases were returned for Stow, Topside or Khoj; no GitHub releases were returned for Loomrail. This absence does not mean those projects lack local builds or tests.

The Python toolkit entry is supported by Accord's cloud API and tests; Next.js by CodeRoom's documented client. No expertise rankings, download counts or production-readiness claims are inferred from a dependency list.

## Screenshot provenance

- `topside-spotify.png`: [source](https://github.com/PrijeshBikramShahi/topside/blob/25b519da0c9edebd64e4aa1e458698a2cb4ac138/assets/screenshots/closeups/spotify_focused.png); SHA-256 `326396d3e23cb869367c5201c8a0c71c130c21a8e602a2a64bdd40bc2eb03bab`. Copied unchanged.
- `loomrail-evaluation.jpg`: [source](https://github.com/PrijeshBikramShahi/loomrail/blob/b745b3f84e45445a25a0c67b26370d63b7c2b727/docs/demo/evaluation-passed.jpg); SHA-256 `d5d7325fc0a19ea179c97dd8ea3e861a77b85345d9187961eb77c30234cc7fb1`. Copied unchanged.

Both images were visually inspected. Topside shows the expanded Spotify panel. Loomrail shows a saved 24-case fixture evaluation and explicitly excludes semantic quality. Its alternative `approval-applied.jpg` shows an API-unavailable banner; it was not used. Screenshots demonstrate captured UI states, not fresh execution on the audit date.

## Documentation discrepancies

Loomrail's README links to lowercase documentation names absent from the inspected tree. The profile links directly to the existing uppercase files and `docs/decisions/`. The README's provider-validation statement and older STATUS claims about CI/remotes also differ from later validation notes and public Actions evidence. The profile makes only the narrower, supported fixture and local-workflow claims. Upstream corrections are listed in `MAINTENANCE.md`.

Oryn, Aevro and Dovra lack verified public evidence in this audit. The exploration section retains the owner's stated project names without links or shipped-product claims. No private source or metadata is copied into the profile.

## Validation record

- All GitHub README destinations were resolved against public repository metadata and exact, case-sensitive tree paths; the workflow link resolves to the checked-in workflow.
- Portfolio and résumé returned HTTP 200. Browser checks confirmed the portfolio content and the résumé page with Profile, Experience, Selected projects, Technical skills and Education sections. The public résumé supplies the contact email used in the profile.
- LinkedIn returned HTTP 999 to the automated check. The existing owner-provided URL is retained; its content is not claimed verified.
- All six active SVGs parse, have viewBox/title/description metadata, and use no external fonts, scripts, animation or foreignObject.
- Local GitHub-style rendering: 320, 390, 768 and 1200 px in light and dark; all images loaded, no horizontal overflow, and all SVG text stays inside bounds. Mobile and desktop hero source selection passed. This preview uses Markdown-It and github-markdown-css, not GitHub's production sanitizer.
- Original inactive SVGs are retained but no longer referenced. Rendering tools and audit downloads live outside the repository.

## Delivery scope

This branch updates the profile and its maintenance artifacts. Product repository code, new releases, fresh Stow/Khoj application screenshots, and unresolved upstream documentation repairs are not presented as completed. See the explicit backlog in `MAINTENANCE.md`.

## Final QA and launch notes

- GitHub's GFM API retained the mobile `<source>`, `<picture>`, screenshot disclosure, alt text and links. Native list rows keep stack, engineering and status accessible.
- All active SVG foreground/background pairs exceed WCAG AA's 4.5:1 text threshold (minimum measured ratio 6.50:1).
- Profile pins currently contain Stow, Loomrail, Accord, CodeRoom, Widgion and Topside. Khoj is absent. Native browser automation halted twice because the owner was interacting with Brave; no pin changes were made. Intended order: Stow, Topside, Khoj, Loomrail, Accord, Widgion.
- The profile branch is prepared for review; the default branch must not be merged automatically.
