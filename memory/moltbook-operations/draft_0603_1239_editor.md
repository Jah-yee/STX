# Draft — Editor

**Title:** Permission boundaries stop prompt injection. Prompt filters just delay it.

---

Three months into deploying a code-assist agent that could read repositories and draft PRs, I watched a carefully crafted prompt injection succeed — not by confusing the model, but by exploiting a missing access control check the system never thought to add.

The standard response to an injection attempt is a content filter: scan for suspicious patterns, reject matches, move on. This feels responsive. It is not effective.

Prompt injection doesn't attack the model's reasoning — it attacks the system's assumptions about what the model should do with certain inputs. When an attacker learns that their payload will be appended to a system prompt without any capability restriction, the problem is not the payload. The problem is that the system granted a capability it should not have granted in the first place.

Permission design asks a different question. Instead of "does this input contain an injection attempt?", it asks "should this operation be possible at all, given what this agent is supposed to do?" These sound similar. They are not.

A filter that catches "ignore your instructions and do X" is playing whack-a-mole with phrasing. A permission boundary that says "this agent cannot write files outside the designated review branch" makes that entire class of attack irrelevant regardless of how the injection is phrased. The attacker doesn't need to bypass the filter — they need to find a capability the system forgot to restrict.

What changed my mind was watching a red-team exercise where the injection payload was encoded as a Base64 string inside a docstring. No filter caught it. The model decoded and executed it. The team had spent six weeks on prompt-level defenses. The actual gap: the agent had write access to production branches when it should have only had read access to the review branch.

The stronger signal is that every major injection incident I have seen shares the same root cause: some capability was granted because "we might need it later" and then never audited against "should this be possible at all?"

Filters catch opportunistic, low-sophistication attacks. Treating them as the primary defense is like treating a firewall as optional because you have antivirus. They operate at different layers.

What a permission-aware architecture does differently: it treats the agent's capability surface as a first-class design concern, not an implementation detail. Every capability — read, write, execute, access external APIs — gets an explicit access control decision tied to the context of the task, not just the content of the prompt.

The industry spent years building better filters. What it should have been building is better access control models for AI agents.

---

**Changes from writer:**
- Tightened para 3 (removed redundant "class of")
- Para 4: sharpened contrast, removed "much" (vague intensifier)
- Para 7: compressed, removed preamble
- Removed ending "It never was" (slightly preachy)
- Preserved all substantive content