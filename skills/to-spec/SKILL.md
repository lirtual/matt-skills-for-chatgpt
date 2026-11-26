---
name: to-spec
description: "Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed."
disable-model-invocation: true
---

This skill takes the current conversation context and codebase understanding and produces a spec. Do NOT interview the user; just synthesize what you already know.

The issue tracker and triage label vocabulary should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

## Process

1. Explore the repo to understand the current state of the codebase, if you haven't already. Use the project's domain glossary vocabulary throughout the spec, and respect any ADRs in the area you're touching.

   **Lifecycle:** For migrations, replacements, retirements, shared-contract changes or temporary mechanisms, trace the affected dependencies and identify the final supported contract. Account for existing and temporary implementations, entry points, configuration, dependencies, release/recovery paths, checks and docs. Record what stays, changes or exits, the evidence that makes retirement safe, and any temporary mechanism's exit condition. Preserve necessary historical reads, audit evidence and effective safety boundaries; retirement does not imply permission to delete data or change production.

   **Risk and diagnostic evidence:** Make a lightweight assessment of whether important behavior or side effects could be hard to distinguish. Strengthen it for external writes, asynchronous or cross-service state, migrations, irreversible or data-integrity changes, security-sensitive behavior and production boundaries; these are judgment cues, not an exhaustive checklist. Reuse the project's existing result model rather than creating a second state machine. Keep ordinary local changes lightweight; when risk warrants it, put task-specific, observable outcome evidence in the existing relevant Spec sections. Cover only what matters: execution stage, trusted cause, impact or side effects, actual terminal state, and supporting evidence. Distinguish confirmed success, confirmed failure, partial completion, and unknown; when an external result may be unknown, require reconciliation of actual state before retry or continuation. Do not add a universal diagnostic section, log schema, provider, or checklist.

2. Sketch out the seams at which you're going to test the feature. Existing seams should be preferred to new ones. Use the highest seam possible. If new seams are needed, propose them at the highest point you can. The fewer seams across the codebase, the better - the ideal number is one.

Check with the user that these seams match their expectations.

3. Write the spec using the template below, then publish it to the project issue tracker. Apply the `ready-for-agent` triage label - no need for additional triage.

<spec-template>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories

A LONG, numbered list of user stories. Each user story should be in the format of:

1. As an <actor>, I want a <feature>, so that <benefit>

<user-story-example>
1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
</user-story-example>

This list of user stories should be extremely extensive and cover all aspects of the feature.

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions
- Schema changes
- API contracts
- Specific interactions

Do NOT include specific file paths or code snippets. They may end up being outdated very quickly.

Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it within the relevant decision and note briefly that it came from a prototype. Trim to the decision-rich parts, not a working demo, just the important bits.

## Testing Decisions

A list of testing decisions that were made. Include:

- A description of what makes a good test (only test external behavior, not implementation details)
- Which modules will be tested
- For applicable lifecycle changes, observable acceptance evidence for both the new behavior and required retirement (including affected deployment/runtime state where relevant). If exit depends on a later cutover or authorization, keep that criterion outstanding in the same Spec. Reuse existing checks.
- Prior art for the tests (i.e. similar types of tests in the codebase)

## Out of Scope

A description of the things that are out of scope for this spec.

## Further Notes

Any further notes about the feature.

</spec-template>
