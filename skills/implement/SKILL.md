---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

## ChatGPT execution note

For an instruction to call another Skill, use an available skill-reading tool to discover and load the named sibling Skill. Do not assume the Claude Skill tool exists. If that skill-reading capability or named dependency is unavailable, state that it is unavailable and do not claim to have invoked it. Respect user-only invocation policies.

Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Call the Skill tool with "tdd" where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, call the Skill tool with "code-review" to review the work.

Commit your work to the current branch.
