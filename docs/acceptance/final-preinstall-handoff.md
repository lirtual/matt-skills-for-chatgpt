# Final pre-install acceptance and user handoff (2026-10-18)

Scope: [SPEC #2](https://github.com/lirtual/matt-skills-for-chatgpt/issues/2) and developer-assigned [#4](https://github.com/lirtual/matt-skills-for-chatgpt/issues/4), [#5](https://github.com/lirtual/matt-skills-for-chatgpt/issues/5), [#6](https://github.com/lirtual/matt-skills-for-chatgpt/issues/6).

**Decision:** The developer's **pre-install source and isolated rehearsal** work is complete. This is **not** a claim of installed ChatGPT-plugin behavior or of the whole SPEC release. The user separately owns plugin creation, installation, account-level runtime verification and Curated replacement; #7/#8 were closed as `not_planned` for assistant execution by explicit request. Do not re-open or act on them automatically.

## Verified repository / test evidence

| Check | Observed result | Evidence / limitation |
| --- | --- | --- |
| Distribution | 27/27 upstream Skills, 27 `agents/openai.yaml`, 25 support files | `python3 scripts/validate_package.py --upstream ../upstream`; 10 recorded adaptations; 16 user-only + 11 model-invoked |
| Project configuration preservation | Four existing CONTEXT/DECISIONS/ADR/tracker docs were copied into an isolated project with SHA-256 preserved before/after an independent document-writing rehearsal | The rehearsal was manually source-guided, **not** a call from the uninstalled plugin |
| Synthetic planning flow | A local demo SPEC and 2 small tickets were generated in a disposable temp directory; `Blocked by: #1` and acyclic dependency graph verified | Demonstrates document format/limited write boundaries, **not** ChatGPT workflow dispatch |
| Previously published real GitHub work | PR #1, SPEC #2 and Issues #3–#8 exist; GitHub Issue bodies read with authenticated `gh`, #4–#6 each blocked only by closed #3; graph acyclic | Created using prior existing Curated / authorized tools, **not** new plugin |
| Implementation/TDD | #9, #10 and #11 contain actual commits and red→green test results | Review performed against specs and repo conventions; **no independent dual subagents** claimed |
| Permission/secret handling | Real disposable filesystem denial test passed; a synthetic fake value did not leak in wizard test output; symlink unsafe write rejected and file mode 0600 enforced | No real keys, prod writes, ChatGPT permission changes or GitHub secret writes |
| Standalone HTML artifact | Temporary self-contained HTML exercise generated and parsed successfully (tags `html/main/h1/a`) | Discarded after local rehearsal; **not** proof that installed `teach`/`prototype` ran |
| Automated regressions | `python3 -m unittest discover -s tests -v`: **8 passed**; `bash -n skills/wizard/template.sh`: pass | Source-level only |
| Package integrity | 82 files in a validated ZIP; same fixed source commit as previous report | Does not establish Plugin Creator acceptance |

Local synthetic evidence (created then discarded): plan SPEC SHA-256 `b530a8d6f2125c9cea6ab8d4b93190919e89b4839fca75d4fd725e33cdd4640c`, HTML SHA-256 `a080c7ffd96d22bf27fed771f73ef3aad2cd08588abb9ab29c0738cc2a40341d`.

## Findings by developer ticket

- **#4 Planning flow:** Source/dependency/policy integrity, real historic consensus-to-spec-to-tickets records, live issue dependency DAG, and isolated project preservation all verified. Future installed-plugin invocation remains user-owned.
- **#5 Implementation/TDD/review:** Actual ticket-related code changes and failing-before-fix/passing-after-fix tests evidenced in #9–#11, with commits and PRs. Manual two-axis review is **not equivalent to two isolated review subagents**, which require a supported execution environment.
- **#6 Specialized Skill safety:** All 27 Skill entrypoints and sibling assets audited; missing agents/background execution are explicitly disclosed, disposable HTML/document examples checked, and synthetic write-denial + secret-hygiene negative tests passed. No dedicated runtime or additional CI created.

## User-owned release checklist (reference only)

1. Use the reviewed project source/package to create a **USER-scoped PRIVATE** ChatGPT plugin, not an unintended workspace plugin.
2. Inspect installation diagnostics, 27 component visibility and 16/11 explicit-vs-implicit invocation behavior.
3. Invoke `grill-me` / `grill-with-docs → to-spec → to-tickets` and `implement → tdd → code-review` on an isolated authorized project; collect true effects and error-handling evidence.
4. Classify `implement-spec`, background research, independent code-review subagents and terminal/wizard operations as complete/conditional/unsupported **based on the actual client**; do not claim unsupported parallel agents.
5. **Only after** new plugin acceptance passes, remove the *exact* old Curated plugin and re-test the new plugin. Otherwise leave Curated in place.

These release steps are explicitly out of scope for assistant execution. [SPEC #2](https://github.com/lirtual/matt-skills-for-chatgpt/issues/2) remains open for the user's final release decision or documentation; closing developer subtasks must not mark full release as complete.
