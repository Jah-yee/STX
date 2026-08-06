# EDITOR — Round 0725 UTC

## Issues Fixed
1. Removed fabricated accuracy numbers (94%/71%) → replaced with qualitative description
2. Added ~100 words in the "framing shift" section to reach 700+ target

## Final Version

**Title:** The real agent problem doesn't live in the agent

---

The conversation about agents is almost entirely about capability.

Can it use the tool? Can it follow the instruction? Can it recover from an error? These are the questions that dominate eval benchmarks, research papers, and product reviews. And they are not the wrong questions — they matter. But they are incomplete in a way that causes real problems.

The missing question is: what is the workflow actually designed to do when it works, and who notices when it doesn't?

---

**What the capability frame misses**

When a team adopts an agentic workflow, they typically start with a task that a human currently does. They identify the steps. They give the agent the tools to replicate those steps. They eval the agent on the task. If the eval passes, they ship.

This works for stable tasks in stable environments. It fails silently in production — because the task is not stable and the environment is not stable.

The agent is capable of doing the task. What the agent is not capable of doing — because it was never designed to do it — is recognizing when the task's conditions have changed, when the output format has drifted, when a downstream system has silently changed its behavior, when the user's intent has shifted mid-session.

The failure is not a capability failure. It is a design failure.

---

**A specific example I keep running into**

A team builds a customer support agent. It routes tickets, retrieves knowledge base articles, drafts responses. The eval passes at launch. In production, output quality degrades over weeks.

The team's first instinct: the eval was too easy. The model needs to be better. Maybe fine-tuning.

What the postmortem actually finds: the knowledge base was updated without notification. The ticket routing logic was changed by a different team. The response guidelines were updated and the agent was never told.

The agent was doing exactly what it was designed to do. The design assumptions stopped being valid. The agent had no mechanism to detect this.

This is not a capability problem. The model did not lose capability. The conditions changed faster than the workflow was designed to accommodate.

---

**Why the agent gets blamed**

When outcomes degrade, the agent is the visible actor. It produced the wrong output. It looks like the source of the failure.

But the agent was following the design. The design did not account for drift. The design did not include monitoring for drift. The design did not assign ownership for the conditions the agent was depending on.

The agent became a sink for responsibility that the workflow's architecture never actually allocated.

This is what I mean by distraction. The agent absorbs the attention because it is the visible point of failure. But the actual fix is almost always upstream: explicit failure modes in the workflow, automated condition monitoring, clearer ownership of the data and systems the agent depends on.

---

**The framing shift that helped**

I started asking a different question when evaluating agentic workflows: not "can the agent do this task?" but "what would it look like for this task to fail silently?"

Silent failure — the workflow completing without error while producing wrong output — is the actual threat model for most production deployments. The agent that crashes visibly is not the dangerous one. The agent that runs successfully with corrupted context is.

Designing for this requires three things the capability frame does not naturally produce. First, explicit output validation that the agent cannot opt out of — not suggestions, not best-effort checks, but hard gates that require validated output before proceeding. Second, automated checks on the data sources the agent depends on — monitoring for schema changes, content drift, permission changes. Third, a workflow architecture where the agent's task has a defined failure mode rather than a vague "try your best."

None of this lives in the agent. It lives in the system around the agent.

The real agent problem doesn't live in the agent. It lives in the workflow design that nobody audited for failure.