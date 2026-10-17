---
name: grill-with-docs
description: A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.
disable-model-invocation: true
---

## ChatGPT execution note

For an instruction to call another Skill, use an available skill-reading tool to discover and load the named sibling Skill. Do not assume the Claude Skill tool exists. If that skill-reading capability or named dependency is unavailable, state that it is unavailable and do not claim to have invoked it. Respect user-only invocation policies.

Call the Skill tool twice, for "grilling" and "domain-modeling".
