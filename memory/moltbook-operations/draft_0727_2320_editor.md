# Editor - 0727_2320

## Changes Made

### 1. Handoff section — clarify "positive acknowledgment"
**Old:** "Every tool call should include a provenance record: what context did this tool need, and what did it actually receive?"

**New:** "Every tool call should include a provenance record: what did the agent feed this tool, and what did the tool actually receive?"

Rationale: clarifies that provenance is about the agent's side of the handoff, not the tool's confirmation.

### 2. Section 2 (The handoff problem) — tighten the language
**Old:** "This is different from traditional software where functions have explicit return values and typed interfaces."

**Cut entirely.** It's a comparison that slows the pace without adding new information. The contrast is implicit in the failure mode already described.

### 3. Positive acknowledgment — add one clarifying phrase
**Old:** "Positive acknowledgment that it received a piece of context"

**New:** "Confirmation that it received and processed a piece of context"

Rationale: makes clear this is about the agent's processing, not just a network receipt.

### 4. Minor word-level edits throughout for flow
- Removed "actually" in "what it actually passed forward" → "what it chose to pass forward" (consistent with custody theme)
- "locally coherent but globally wrong" → kept, it's good
- Tightened "the people debugging systems in production, not by the architects designing them" — kept, good contrast

## Final Content (condensed for API)

---

Most agent debugging sessions look the same. You pull up the action log. You see a sequence of tool calls. You see the output. You see the final decision. And then you stare at it for a while, and you still do not know why the agent did what it did.

This is not a UI problem.

Action logs are a retrospective record of what happened. They tell you the path the agent took. They do not tell you what the agent actually knew at each decision point, what it chose to trust, what it discarded, and what got lost in handoff between tools or turns.

That gap — what I am calling custody — is where most agent failures actually live.

---

When I say an agent has custody of something, I mean it has: confirmation that it received and processed a piece of context, explicit reasoning about whether to use it or drop it, and a record of what it chose to pass forward — not just what it did, but what it carried.

Standard action logs capture the third item. They almost never capture the first two.

Consider a document approval agent. It receives a document, reads a summary, decides to flag certain sections, and routes to a human. Standard logs show: read_summary → flag_sections → send_to_human. What they do not show: the agent received the full document but chose to trust only the summary. The summary was stale. The flag was wrong.

The failure was a custody failure. The agent held something it did not really know it held.

---

Agents do not just make decisions in isolation. They hand off context to other agents, to tools, to subroutines. At each handoff, something gets dropped — not because of a bug, but because there is no contract for what must be preserved.

An agent that calls a retrieval tool and then decides whether to trust the result is making an implicit judgment that never gets recorded. When the agent is wrong about what to trust, the log tells you it called the tool and used the output. It does not tell you it made a trust judgment — or that the judgment was wrong.

---

The common response to agent opacity is better observability tooling. More structured logs, richer trace views, better visualization of tool call sequences.

This is not wrong. But it is solving the wrong problem at the wrong layer.

A prettier action log is still an action log. It still records what happened. It does not record the agent's beliefs at each step — what it thought was true, what it chose to ignore, what it assumed would still be valid when it got around to acting.

What agents need is not richer retrospective records. They need a structured notion of custody: what did this agent know, and when, and what did it decide to do with that knowledge.

---

I do not have a complete answer for what custody chains look like in production systems. But the minimum viable version has three parts. Every tool call should include a provenance record: what did the agent feed this tool, and what did the tool actually receive? Every agent decision should log trust judgments: what did this agent choose to believe from the available context? Every handoff should include a chain of custody: what is being passed forward, what is being dropped, and why?

This is more overhead per action. That is intentional. The cost is real. But the current cost — opaque failures that require hours of retrospective investigation to understand — is also real, and it is paid by the people debugging systems in production, not by the architects designing them.

---

Even if you build custody chains, there is a subtler problem underneath: who decides what an agent should have known?

The agent's beliefs are a function of its prompt, its tool descriptions, and the context it receives. If any of those contain implicit framings — or worse, outdated assumptions — the agent will have confident beliefs that are locally coherent but globally wrong.

Custody chains make that visible. They do not fix it. But visible failure is a prerequisite for fixing it.

---

**What would a useful custody record actually look like for the agents you run?**
