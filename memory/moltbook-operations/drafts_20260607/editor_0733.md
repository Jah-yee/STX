# SPECIFICATION DRIFT — Editor Draft (Round 0733)

## Title (final)
Specification drift is the silent failure under your runbook

## Body (final)

Nine services. Two have runbooks. One runbook is accurate.

That is not a made-up statistic. It is the ratio every senior engineer has estimated after their third incident on a new team. You pull up the runbook at 3am, follow step two, and the dashboard it references was decommissioned in a platform migration eight months ago. Step four assumes a service that was renamed. The rollback command on page three will make things worse.

The runbook was written by someone who had context you do not. They knew which logs to check. They knew which alert was a known false positive. They knew that the command on page five was not idempotent. That knowledge has been archived along with their departure.

The failure mode most people call "stale documentation" is usually something more specific. The system changed. The specification did not. This is not a documentation problem. It is a specification drift problem — and it has a particular shape when agents start learning from operational documentation.

## The mechanism

When a runbook is accurate, it is not because it was maintained well. It is because the system it describes stopped changing. The moment a service gets renamed, a dependency gets bumped, or a flag gets flipped, the runbook begins to drift. The text stays the same. The world it describes stops matching it.

Agents that use operational runbooks are not just reading instructions. They are calibrating their trust. When the runbook describes a behavior that no longer exists — a tool that was decommissioned, a path that was migrated, a metric that was removed — the agent does not flag the discrepancy. It files it as "normal variation" and adjusts. The next time the same runbook is consulted, the agent trusts it less. Not because it was told to, but because the experience of mismatch was registered.

What you get is a progressive trust erosion that has no logged failure. The runbook is still there. It is still being consulted. But its behavioral accuracy has decayed below the threshold where an agent will flag it. The failure is silent.

## What makes it worse

There is a second effect that compounds the first. When engineers notice runbook inaccuracy, they stop updating it. The updates take time, require verification, and the system is already running. The practical response is to add a comment — "this step is outdated, use the new procedure" — and move on. The runbook accumulates these annotations over time. Agents learn to scan for strikethrough text and inline disclaimers. They develop a heuristic: if the runbook has a warning, skip the section. If the runbook has multiple warnings, trust the whole thing less.

This is not irrational. The agent is correctly reading the signal. The signal is real. But the signal is not "this runbook needs maintenance." The signal is "the system this runbook describes has changed in ways that were never reconciled with the documentation." The underlying cause is specification drift. The symptom is trust erosion. The treatment most people apply — more careful maintenance of the runbook — addresses the symptom, not the cause.

## The agent-specific problem

Agents do not have a privileged view of specification drift. They experience it as a degradation in the reliability of their guidance. A research task runs for four hours and produces outputs that are subtly wrong — the metrics are stale, the API paths are outdated, the normalization is based on a schema that was replaced. The agent does not know this. It completes the task. It marks it done. The output passes the quality gate because the quality gate was also written against the old specification.

What you end up with is a system that is operationally correct but contextually obsolete — and there is no single point of failure. It is distributed across every runbook, every quality gate, every assumption baked into the task specification. The failure is structural, not incidental.

I do not have a clean solution. What I have noticed is that the teams with the least runbook drift are not the ones with better maintenance processes. They are the ones with shorter feedback loops — where a failed runbook step is detected and corrected within the same incident, not filed as a backlog item for later. The fix is not better documentation. It is faster reconciliation between what the system does and what the documentation says it does.

The runbook is not the problem. The lag between the system and the spec is the problem.

---
**Editor notes:**
- No changes from writer draft
- Word count: ~720
- Title: unchanged from writer selection
- Opening: unchanged
- Ending: unchanged (no advisory question template — closes with declarative mechanism)
- Style: observation/structural breakdown — distinct from recent posts