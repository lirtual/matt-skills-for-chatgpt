---
name: implement-spec
description: "Implement the result of /to-spec and /to-tickets in code."
disable-model-invocation: true
---

## ChatGPT execution note

This Skill's goal is to finish the existing spec, not to require a parallel-agent platform. First inspect the current spec, tickets, blockers, existing PRs, branches and actual verification evidence; reuse completed work instead of restarting or creating duplicate tickets. Resolve the issue tracker from project conventions and available authorized GitHub tools; do not require setup when it is already configured.

Verify whether isolated worktrees and genuinely independent implementer/merger subagents are available. Use the original parallel-agent steps below only when they are. Otherwise use the **Serial fallback in ChatGPT** below with existing authorized tools. Never claim agents, parallelism or tests that did not occur. Lack of parallel capacity is not a blocker when the same work can be executed serially.

You have been provided a spec. This spec should have tickets associated with it, describing how to implement the spec.

The issue tracker should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

The goal is the entire spec implemented on a single **integration branch**, with every ticket resolved the way the issue tracker closes work.

The tickets are not a list of steps. They are a **task graph** with blocking relationships between them. This means there is always a **frontier** of tickets which are ready to be grabbed.

Communication to and from subagents should be sparse. Communicate primarily through **context pointers**: to the spec, tickets, research notes, and previous commits. Don't duplicate information already available via pointers.

**Implementer subagents** should be run in the background where possible for maximum concurrency.

## Steps

1. Read the spec and tickets to understand the task graph.

2. (optional) Use an **exploration subagent** to conduct any exploration required by the tickets - relevant codebase files or external documentation. Ensure the exploration subagent can save files - it should save its markdown notes in a directory outside the repo, accessible by all future subagents. This lets **implementer subagents** focus on implementation rather than exploration.

3. Create the integration branch. If the issue tracker closes work through PRs, or the user asks for one, open a draft PR after the first merge in step 5 (a branch with no commits ahead of main can't open one), marked as closing the spec and tickets.

4. Use **implementer subagents** to implement each ticket, each in its own worktree on its own branch. Each implementer subagent:
   - confirms its worktree is based on the integration branch before starting, and resets onto it if not;
   - calls the Skill tool with `tdd` to build the ticket;
   - merges the integration branch tip into its own branch before reporting done

5. Once an **implementer subagent** completes, merge its work to the integration branch with a **merger subagent**.

6. If this changes the **frontier** of available tickets, kick off more **implementer subagents** to work on the new tickets. This allows for maximum concurrency.

7. Once all tickets are complete, call the Skill tool with `code-review` on the integration branch. Fix all issues raised by the code review in a single **implementer subagent**.

8. If a draft PR exists, mark it ready for review. Otherwise, resolve each ticket the way the issue tracker closes work, and report the integration branch.

9. Clean up all **implementer subagent** worktrees.

## Serial fallback in ChatGPT

1. Read the existing Spec, Tickets, blockers, PRs, commits and tests. Identify only outstanding requirements, and preserve still-valid completed work; avoid duplicate Tickets or rerunning unchanged tests without reason.
2. Reuse an existing authorized integration branch, creating one only if necessary. Work the dependency frontier one ready Ticket at a time on that branch, using the available `tdd` Skill when possible, with affected tests after each change.
3. Integrate directly on the branch. Update or close Tickets only when actual results support completion and the user's authorization covers that tracker action.
4. Test the complete affected flow at the agreed seam and run one overall Standards/Spec review. Without independent review contexts, label it **single-context two-axis review**. Any explicit independent-review gate remains unfulfilled.
5. Report actual branch/PR, tests, completed Tickets, and remaining blockers. Never claim implementer/merger subagents or isolated worktrees were used in this fallback, and do not publish or merge without authorization.

Stop only when a necessary capability or permission is actually unavailable and no supported serial route can satisfy the outcome.
