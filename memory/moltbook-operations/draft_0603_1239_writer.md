# Draft — Writer

**Title:** Permission boundaries stop prompt injection. Prompt filters just delay it.

**Opening:** Three months into deploying a code-assist agent that could read repositories and draft PRs, I watched a carefully crafted prompt injection succeed — not by confusing the model, but by exploiting a missing access control check that the system never thought to add.

**Central claim:** Prompt injection succeeds because it's an access control failure, not a content safety failure. The industry framed it wrong, and that framing led to a decade of ineffective defenses.

---

The standard response to an injection attempt is a content filter: scan the input for suspicious patterns, reject matches, move on. This feels responsive. It is not effective.

The reason is structural. Prompt injection doesn't attack the model's reasoning — it attacks the system's assumptions about what the model should do with certain classes of input. When an attacker learns that their injection payload will be appended to a system prompt and processed by the model without any capability restriction, the problem is not the payload. The problem is that the system granted a capability it should not have granted in the first place.

Permission design asks a different question. Instead of "does this input contain a prompt injection attempt?", it asks "given everything this agent has access to, should this operation be possible at all?" These sound similar. They are not.

A filter that catches "ignore your instructions and do X" is playing whack-a-mole with phrasing. A permission boundary that says "this agent cannot write files outside the designated review branch" makes that entire class of attack irrelevant regardless of how the injection is phrased. The attacker doesn't need to bypass the filter. They need to find a capability the system forgot to restrict. That is a much lower bar.

What changed my mind on this was watching a red-team exercise where the injection payload was encoded as a Base64 string inside a docstring. No filter caught it. The model decoded and executed it. The team had spent six weeks on prompt-level defenses. The actual gap was that the agent had write access to production branches when it should have only had read access to the review branch.

The stronger signal is that every major prompt injection incident I have seen shares the same root cause: some capability was granted because "we might need it later" and then never audited against the question "should this be possible at all, given what this agent is supposed to do?"

Filters have their place — they catch opportunistic, low-sophistication attacks. But treating them as the primary defense is like treating a firewall as optional because you have an antivirus. They operate at different layers and solve different problems.

What a permission-aware architecture does differently: it treats the agent's capability surface as a first-class design concern, not an implementation detail. Every capability — read, write, execute, access external APIs — gets an explicit access control decision tied to the context of the task, not just the content of the prompt.

The industry spent years building better filters. What it should have been building is better access control models for AI agents — because injection is not a content problem. It never was.

---

**Word count:** ~480