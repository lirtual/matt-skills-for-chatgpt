# Upstream provenance and update policy

- Source: https://github.com/mattpocock/skills
- Pinned upstream commit: `49dd158d1076134a641b33efb035946536778336`
- Upstream manifest version: `1.3.1` (`.claude-plugin/plugin.json`)
- Source license: MIT; copied in [LICENSE](LICENSE).
- Publication: **unofficial ChatGPT adaptation**, not endorsed by Matt Pocock.
- Initial target: 27 official skills (20 Engineering, 7 Productivity), corresponding invocation metadata and required adjacent assets.
- Status: **candidate package prepared; not yet installed or released as a ChatGPT plugin**.

## Update process (manual)

1. Fetch `mattpocock/skills` to a local Git remote called `upstream`. This remote is a local Git configuration, not a feature of GitHub's server-side repository settings.
2. Compare the pinned commit with a proposed new upstream commit or released version, inspecting the official plugin manifest and `skills/engineering` + `skills/productivity`.
3. Review added/removed skills, policy changes, support files, license/credits and any changed runtime dependencies. Preserve original behavior where possible and document intentional ChatGPT differences.
4. Import reviewed changes into a short-lived branch, run static and affected behavior checks, and open a PR.
5. Only after review and acceptance, update this file's pinned SHA, update the plugin version, and explicitly publish a new plugin release.

**Do not** merge the original upstream repository into this adapted repository wholesale, automatically sync `main`, auto-create releases, or present upstream version `1.3.1` as the new plugin's version.

## Attribution

Copyright (c) 2026 Matt Pocock, licensed under MIT. Preserve any upstream third-party credit documents such as `pr/CREDITS.md` in corresponding Skill directories when packaging.

## Initial candidate adaptations

At version `0.1.0`, all 27 upstream Skill directories and their companion files are copied byte-for-byte. The only adaptation is the portable root `plugin.json` and the standalone repo/package layout. Some execution features are conditional on the current authorized ChatGPT tool environment and will be validated in later Issues.
