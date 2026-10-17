# Issue tracker: GitHub

- Repository: https://github.com/lirtual/matt-skills-for-chatgpt
- Specifications and implementation tickets: GitHub Issues.
- Feature and documentation changes: short-lived GitHub branches and PRs targeting `main`.
- Specs should identify their parent design decisions in [DECISIONS.md](../../DECISIONS.md) and link the relevant ADR.
- Desired readiness role: `ready-for-agent`; apply as an Issue label **if the label exists**. Do not silently invent a new repo-wide label scheme.
- Ticket blocking: native GitHub dependencies when an authorized tool supports them; otherwise write explicit `Blocked by: #...` links, as the upstream tracker convention permits.
- No automatic closing or merging of Issues/PRs; close only with implementation evidence or explicit user direction.
- Keep plugin creation, installation and old-plugin uninstallation out of scope until separate user authorization.
