# Pre-install rehearsal evidence — #4 / #5 / #6

> 2026-10-18. Scope: pinned source at Matt Pocock commit `49dd158d1076134a641b33efb035946536778336`, adapted project `lirtual/matt-skills-for-chatgpt`.
>
> **Only pre-install evidence is recorded here.** The new ChatGPT plugin has not been created, installed, or invoked. The user personally owns #7 (private install and live acceptance) and #8 (Curated cutover); both tracker tickets were closed **not_planned**, NOT completed. This repository must not trigger those actions.

## #4 — planning and issue graph (source-level / existing-tool rehearsal)

- All 27 Skill entrypoints, 27 policy files, 25 supporting files and 16 explicit / 11 implicit invocation declarations pass the repository validator.
- Existing real Grilling with Docs decisions Q1–Q21 are stored in [DECISIONS.md](../../DECISIONS.md) and [CONTEXT.md](../../CONTEXT.md); [ADR-0001](../adr/0001-skills-only-adaptation.md) was published through [PR #1](https://github.com/lirtual/matt-skills-for-chatgpt/pull/1). These are **prior sessions using Curated/current tools**, not the new plugin.
- The real `to-spec` synthesis produced [SPEC #2](https://github.com/lirtual/matt-skills-for-chatgpt/issues/2), and `to-tickets` produced [#3–#8](https://github.com/lirtual/matt-skills-for-chatgpt/issues/3). Actual GitHub issue bodies were read via authenticated `gh issue view`; the textual `Blocked by:` fallback has a verified acyclic graph: #4, #5, #6 each depend on closed #3. #7 and #8 are closed by user instruction as **not_planned**.
- Existing project `CONTEXT.md`, `DECISIONS.md`, `docs/adr/` and tracker convention are present and remain tracked; no automatic migration or overwrite occurred during the compatibility changes.
- Native dependency manipulation was **not** claimed; textual fallback was used as recorded. The current new plugin's invocation dispatch remains untested pending user-owned install.

## #5 — actual code/test and review evidence

- [PR #9](https://github.com/lirtual/matt-skills-for-chatgpt/pull/9) implements the pinned 27-Skill package and deterministic build. The **red** run failed because `scripts/validate_package.py` and `scripts/build_package.py` were missing; after implementing, both automated tests turned **green** and PR #9 was merged.
- [PR #10](https://github.com/lirtual/matt-skills-for-chatgpt/pull/10) added truthful ChatGPT environment notes. Two note-level tests went from failing to passing; four total tests passed.
- This branch exercises a second concrete **red → green** slice against the official `wizard/template.sh`: two of three synthetic-file safety tests initially failed (symlink overwrite and mode 0644); they pass after minimal hardening. No real credential, external GitHub secret or production file was involved.
- The repository diff and test results were reviewed against standards (small changes, no new services, no extra CI) and SPEC #2 (security, provenance, no false parallel execution). **Independent two-subagent code review did not occur** and must not be claimed.
- Synthetic OS access-denied test used a disposable read-only directory; it rejected the attempted write without creating the target file. This proves the local fixture's denial handling, **not** that the future ChatGPT client or Remote Control denies every unapproved action.

## #6 — capability and safety matrix

| Workflow family | Pre-install evidence | Installed plugin behavior |
| --- | --- | --- |
| `ask-matt`, `grill-me`, `grill-with-docs`, `grilling`, `domain-modeling` | Packaging, references and Q1–Q21 project documents verified; code route notes for direct Skill loading | **Conditional**, not yet tested for the new plugin |
| `setup-matt-pocock-skills`, `to-spec`, `to-tickets`, `triage` | Current tools created #2–#8; documentation structure preserved; dependency DAG verified | **Conditional**, must reverify the new plugin |
| `implement`, `tdd`, `diagnosing-bugs`, `code-review`, `pr` | Source tests red→green and GitHub #9/#10 commits/PRs observed; no independent review agents | **Conditional**, true parallel code-review unverified |
| `implement-spec`, `wayfinder`, `research` | Source-level runtime prerequisites documented; parallel agents, isolated worktrees and background scheduling were **not** run | **Unsupported in this rehearsal**, may be conditional in a suitable authorized runtime |
| `wizard` | Generated shell library functions exercised with a **synthetic value**; symlink denial and owner-only file mode validated; no `gh secret set` called | **Conditional**, interactive real wizard and permissions untested |
| `prototype`, `teach`, `handoff`, `to-questionnaire`, `wait-what`, `retro`, `writing-for-agents`, `codebase-design`, `improve-codebase-architecture` | Full source/reference paths statically verified; no representative installed-plugin run | **Conditional**, client-specific outputs must be tested by user |

## Security and non-goals

- Never pretend a local shell or old Curated invocation is evidence that the new installed plugin ran.
- Never infer permission from Skill content; the user must explicitly authorize GitHub, file or Remote Control writes within supported tool boundaries.
- `wizard/template.sh` was hardened to reject final-path symlink/non-file destinations and restrict `.env` file mode to owner-only before writing. Synthetic test output did not expose the fake value. The command requires a trusted local execution environment; filesystem races and other paths still follow system access controls.
- No new backend, scheduler, CI, MCP server, account plugin, or Curated uninstall was executed.

## Status and handoff

Pre-install completeness and safety rehearsals can be reviewed against #4–#6. Real invocation/discovery, private scope, the two core workflows **within the newly installed plugin**, and the final cutover remain **unverified user-owned actions**. Do not claim the official plugin can fully execute in every ChatGPT environment.
