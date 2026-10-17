# Pre-install source compatibility audit

> Date: 2026-10-18. Related: #4, #5, #6 and draft code PR.
>
> **This is NOT installed ChatGPT plugin acceptance.** The proposed plugin has not been created, saved to a user's account, connected, or invoked as an installed plugin. Runtime-only gates remain under #7, which requires separate explicit user approval.

## Evidence actually observed

| Test / artifact | What happened | Evidence scope |
| --- | --- | --- |
| Upstream content and invocation policies | 27 SKILL.md, 27 openai.yaml, 25 support files; 16 explicit / 11 implicit | Static source comparison at pinned SHA |
| ZIP packaging | Deterministic 82-file archive; original upstream source intact in #3 | Package integrity, **not installation** |
| ChatGPT Skills tool access | Current conversation loaded *Curated* installed Skills with an existing skill-reading connector | Current session's tool availability only |
| GitHub Issues / PRs | SPEC #2, tracer tickets #3–#8 and #9 PR were actually created; #9 was merged | Existing GitHub connector works; new plugin **not involved** |
| Real code/test execution | #3 introduced packaging validator through observed red→green automated tests; Remote Control ran Python/ Git in an authorized isolated development directory | Existing tool and current session, **not new plugin** |
| Adapter instructions | Nine source Skills now explain ChatGPT loading/permission requirements or absence of true parallel/background execution | Readable source instructions, runtime behavioral validation **pending** |

## Behavioral scenarios deferred until installation (#7)

- Does an explicit invocation of the new plugin's `grill-me` actually resolve `grilling`? The source notes require it, but the uninstalled candidate has no observable invocation.
- Do `grill-with-docs`, `to-spec`, `to-tickets`, `triage` preserve settled decisions, repo configuration, and real tracker relationships in an isolated authorized project?
- Does `implement → tdd → code-review` execute real project tests and honestly report a missing independent agent?
- Are all special Skills accurately marked complete / conditional / unsupported in the actual client?
- Does missing Shell or denied file write result in a clear refusal instead of fabricated success? **No live permission was changed or revoked to simulate a denial.**
- Does a wizard avoid secret disclosure on the real execution boundary? **No real credentials were used.**
- Are the new plugin's 27 components discoverable and its personal/private scope correctly set?

## Current blockers and release decision

No pre-install evidence above is proof of plugin runtime behavior. Preserve Curated and leave #4–#6 open until their remaining acceptance criteria are met or their runtime-specific checks are explicitly reassigned and demonstrated in #7. The creation and cutover gates in #7 and #8 remain authorization-protected. Do not introduce a new backend, scheduler, or CI.
