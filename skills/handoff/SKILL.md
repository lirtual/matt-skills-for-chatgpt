---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

## ChatGPT execution note

Use an OS temporary directory only when the next agent really has access to the same filesystem. Otherwise deliver a copyable handoff in the chat or persist it at an explicitly authorized project/artifact location the next session can read. Do not assume ChatGPT sessions share local files. Refer to existing Issues, Specs and commits rather than duplicating them.

Write a handoff document summarising the current conversation so a fresh agent can continue the work. When the next agent can access the same OS filesystem, save to its temporary directory (`$TMPDIR`, else `/tmp`; `%TEMP%` on Windows), not the current workspace. Otherwise use the accessible ChatGPT handoff route above.

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
