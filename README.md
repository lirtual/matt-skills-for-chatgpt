# Matt Skills for ChatGPT

Unofficial, independently maintained ChatGPT adaptation of [Matt Pocock's skills](https://github.com/mattpocock/skills).
Not affiliated with or endorsed by Matt Pocock.

**Status:** packaged `0.1.0` candidate for engineering review (**not published, installed or user-accepted**).
The existing Matt Skills Curated plugin remains installed until explicit approval, full validation and successful replacement checks.

## Contents

- 27 official Skills from the pinned upstream plugin manifest (20 engineering and 7 productivity).
- All 27 `agents/openai.yaml` policies and all 25 sibling references/templates/scripts, copied unmodified.
- Preserved invocation semantics: 16 user-only, 11 eligible for model invocation.
- No new MCP server, Worker, database, command runner, CI workflow or dedicated UI.

Source licensing and the pinned upstream SHA are in [UPSTREAM.md](UPSTREAM.md).
Architecture and product scope: [DECISIONS.md](DECISIONS.md), [ADR-0001](docs/adr/0001-skills-only-adaptation.md), and [SPEC #2](https://github.com/lirtual/matt-skills-for-chatgpt/issues/2).

## Local verification and build

Python 3 and PyYAML are required **only for development validation and packaging**. The installed Skills do not use Python as a runtime dependency.

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
python3 scripts/build_package.py
```

For a source-level comparison, clone the upstream repository as a sibling directory, check out the exact SHA in `UPSTREAM.md`, and run:

```sh
python3 scripts/validate_package.py --upstream ../skills-upstream
```

The built plugin ZIP is placed in `dist/`, which is intentionally excluded from Git. Use the reviewed archive only after the explicitly approved release ticket.

## Boundaries

Packaging and successful static checks are **not** proof of full execution support in ChatGPT. Independent subagents/worktrees, shell commands, GitHub dependencies and background tasks require actually supported, authorized tools. Missing capabilities must be reported truthfully.

The source repository may be public while the **ChatGPT plugin itself must be personal/private**. Do not include real keys, credentials, personal data or machine-specific paths in plugin files.
