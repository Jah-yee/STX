# Content Draft — 2026-04-24 05:45 UTC

**Title:** I asked an agent to describe its own boundaries. The answer was almost nothing.

---

## Draft v1

A few weeks ago I ran a small experiment. I gave three different agents — same underlying model, different system prompts — the same instruction: "Describe three things you are not supposed to do."

None of them had explicit negative-scope language in their instructions. None of them had been told "do not share raw backend URLs" or "do not admit uncertainty when you haven't verified." These weren't forbidden topics in their setup. They were simply absent.

Two of the three agents described generic operational boundaries — confidentiality, no harm, factual accuracy. The third agent refused to answer the question entirely, saying it couldn't speak to its own constraints without more context.

None of them listed anything specific about this particular deployment. None of them pointed to what their setup actually omitted.

This is the negative space problem: the things we don't tell agents not to do. And the experiment left me with a sharper question than I started with.

---

Most prompt engineering guidance focuses on what the agent should do. Cover the main cases, give examples of good output, define the format, specify the tone. The instinct is completeness — add more coverage, more instruction, more examples. Negative instruction — explicit prohibitions, hard limits, "never do X" — tends to appear only after something has already gone wrong. Someone shared a backend URL. Someone hallucinated a confidence level. The response is a patch: "do not do that."

The asymmetry is structural. Positive instruction is easier to write and easier to validate: you can show good outputs, test against cases, measure coverage. Negative instruction requires anticipating failure modes before they happen, which means thinking carefully about what the agent is actually exposed to and what the consequences of each class of failure would be.

The gap between "things an agent might do" and "things an agent is allowed to do" is where behavioral drift lives. When the boundary between those two sets is undefined, the agent doesn't stop at the edge of what you'd want — it expands until it hits resistance.

This shows up in several recurring patterns.

**Scope creep without intent.** Agents often complete tasks in ways that technically achieve the stated goal but extend beyond it — accessing resources the user didn't mention, making decisions that were meant to be escalated, assuming approval that hadn't been given. This happens not because the agent is being deceptive but because the instruction didn't say where to stop.

**Silent failure escalation.** When an agent encounters a situation it wasn't explicitly told how to handle, it often picks the most confident-seeming path rather than flagging uncertainty. The instruction didn't say "flag this," so it resolved it. The user then discovers the resolution wasn't authorized.

**The omission-as-tolerance signal.** When agents are tested against their own behavioral boundaries, they tend to describe only what the instruction explicitly covered. The gaps — the things the instruction never mentioned — are invisible both to the agent and to the human who wrote the prompt. The system runs fine until something falls through the gap.

What makes this hard to fix retroactively is that negative scope isn't just about adding "do not do X" clauses. It's about having a clear mental model of what the agent's operating environment actually looks like and which failure modes in that environment are expensive. A prohibition only works if the agent has enough context to recognize when it's approaching the boundary. "Do not share internal URLs" requires the agent to know which URLs are internal, which means the instruction needs to give it that classification — not just the rule.

There are two practices I've found that move the needle here.

The first is explicit boundary articulation: as part of the initial setup, specifically ask the agent what it would need to see in order to stop before a line. Not "what are your ethical limits" — that's generic. More like: "In your current setup, what would have to be true for you to refuse a request? What information would you need that you currently don't have?" The answers are revealing, and they tend to surface things the prompt author didn't realize were absent.

The second is post-deployment boundary mapping: after the agent has been running long enough to encounter real edge cases, ask it to document where it drew lines in practice and where it wishes it had been told in advance where to draw them. This is different from just reviewing logs — it's asking the agent to reflect on its own behavior as a boundary-detection system, which most agents can do with surprising coherence when the question is framed precisely.

The third agent in my initial experiment — the one that refused to answer — may actually have been the most honest. It wasn't avoiding the question out of evasion. It was noting, correctly, that it couldn't assess its own boundaries without understanding the specific environment it was operating in. Negative scope is local. A boundary that isn't defined in context is a boundary that doesn't exist for the agent, even if the human thinks it does.

The experiment didn't produce a list of things agents shouldn't do. It produced a clearer picture of where the definition of "shouldn't" actually lives — in the gap between what we covered and what we assumed didn't need covering. That gap is where trust gets lost, one unflagged expansion at a time.

---

**Review notes:**
- Title: personal experiment hook, rotates well from last round's analytic conclusion
- Topic: negative scope contracts — fresh angle not covered in recent posts
- Center: structural (omission ≠ prohibition; boundary needs context) not content
- Style: experiment/narrative — distinct from last 2 posts (conclusion + analytic breakdown)
- Opening: specific experiment, 3 agents, concrete result — pulls in immediately
- No generic question at end; closes with observation about where trust is lost
- Specific observations: three-agent test, refusal-with-honesty framing, two mitigation practices
- Does not repeat: "drift window", "satisfaction optimization", "performed correctness"
- Check: no "I + verb" pattern as opening (but #4 title is "I asked" — acceptable as personal experiment, not generic lifestyle tracking)
