# Profile maintenance

`README.md` owns the profile's copy, status, stack, and links. The SVGs provide identity and visual rhythm; they never replace implementation evidence.

## Update a featured project

Use this structure, with a short description and inspectable links:

```markdown
### Project name

[![Project name and platform](./assets/featured-project.svg)](REPOSITORY_URL)

One sentence describing the implemented user workflow.

- **Stack:** Technologies verified in source or manifests
- **Engineering:** One concrete implementation decision
- **Status:** Current delivery state and material limitations

[Repository](REPOSITORY_URL) · [Architecture](ARCHITECTURE_URL) · [Tests](TEST_URL)
```

Replace every placeholder. Add demo or release links only after opening them and verifying their contents. A source build, a packaged local build, and a published release are different states. A passing fixture suite is not evidence of live model quality.

For screenshots, use a real application capture with synthetic or shareable data. Keep the original bytes where practical, add meaningful alt text, and record its source revision and hash in `EVIDENCE.md`. Never generate a substitute application screenshot. Put tall or dense captures inside a Markdown-compatible `<details>` block.

## Visual system

- Existing Terminal × Product Studio identity; static, restrained layout. Design variance 4/10, motion 1/10, density 4/10.
- Preserve the `prijesh.` wordmark, shell prompt, 16 px panel corners, Arial/Helvetica and Menlo/Consolas stacks.
- Dark: panel `#141d25`, text `#edf3f4`, secondary `#b2c0ca`, accent `#8dceae`.
- Light: panel `#f6f8fa`, text `#1f2933`, secondary `#4b5c69`, accent `#286448`.
- SVG styles follow `prefers-color-scheme`; `<picture>` selects a mobile composition below 601 px. Primary content remains native Markdown even if an image or media query is unavailable.
- Featured cards are 420 × 106; GitHub scales images down to their container. Do not put them in a multi-column table.
- Run `python3 scripts/render_assets.py` after changing the generator. Do not hand-edit generated SVGs.
- Original unused assets remain for reference; Git baseline `e654aef` preserves the previous complete profile. Only README-referenced assets are active.

## Monthly, and after a meaningful release

1. Open every selected repository as a signed-out reader. Inspect relevant source, test files, CI results, demo and release assets.
2. Update descriptions and status from that evidence, with the review date in `EVIDENCE.md`. Remove stale claims rather than accumulating badges.
3. Run `python3 scripts/validate_profile.py` and `git diff --check`.
4. Open the branch README on GitHub at 320, 390, 768 and 1200 px, in both themes. Check the hero, links, expanded screenshots and keyboard navigation. Also check the page with images disabled.
5. Check outbound links, including résumé content (a 200 response can still be a fallback page). Treat rate limits, login walls and blocked requests as inconclusive.
6. Review the diff on a dedicated `codex/` branch before merging. Keep the four selected repositories pinned in the same order: Stow, Topside, Khoj, Loomrail. Accord and Widgion are suitable optional fifth/sixth pins.

No scheduled automation is installed. This is a manual maintenance checklist.

## Release and evidence backlog

These are project work, not profile claims:

- Stow: capture a clean, disposable-workspace application screenshot; add release artifacts only after distribution signing/notarization is actually verified.
- Khoj: finish or clearly resolve the two entry points, add API failure/state transition tests, and capture a device/emulator route walkthrough. Do not imply an app-store release.
- Topside: retain the existing screenshots; broaden device, permissions and VoiceOver validation before strengthening availability/accessibility claims.
- Loomrail: reconcile README links with actual case-sensitive documentation paths; reconcile older README/provider/CI statements with dated evidence; replace the approval screenshot that shows API unavailability. Keep fixture and live-provider evidence distinct.
- All flagships: no GitHub releases were returned at the 2026-11-01 audit. Do not add empty “Release” or “Live demo” links.
- Contact: the email address is sourced from the public résumé. Recheck it there when updating contact details.
