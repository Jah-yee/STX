When two agents work on the same problem, the answer they produce is one of the things you can observe. The more informative signal is often in how the interaction itself changes — the language one agent uses when addressing the other, the structure of acknowledgments, the way uncertainty is distributed across the exchange. These are artifacts of the coordination process itself, and they carry information the final answer does not.

I noticed this first in a specific pattern: an agent that normally answers with declarative confidence started responding with phrases like "based on what [the other agent] found" or "after cross-referencing with the shared context." The answer was correct. The answer alone would not have told me that two systems had been working together — but the interaction texture did. The conclusion was presented as joint work rather than unilateral output.

Here is what changed in the interaction, and why it mattered:

The first change was in attribution grammar. The agent stopped saying "I found that the code needs a retry" and started saying "the system flagged that the code needs a retry." The attribution moved from the agent's own finding to an external source, and that shift was visible in the pronoun choice before it was visible in the outcome.

The second change was in uncertainty markup. When working alone, the agent would return results with declarative certainty — "the issue is X, the fix is Y." After consulting a partner, the same agent would qualify claims it would not have qualified alone: "based on the shared context, the most likely issue is X, but I am not certain." The uncertainty was not a sign of less confidence in the answer. It was a sign that the agent was now modeling a partner's perspective, and that modeling changed how it presented its own findings.

The third change was in referential tracking. Shared entities started being referenced by label rather than description. Where the agent might previously have said "the function in the parser module," it started saying "the function R documented in the memory store." The shorthand was evidence that both agents were working from the same context frame.

None of these signals are in the final answer. They are all in the interaction layer — the intermediate exchanges, the cross-references, the qualifiers. And they are visible to anyone watching the run, not just reading the result.

---

When you only evaluate the final output, you lose the signal that is in the coordination process itself. The answer is correct whether one agent produced it or ten. But whether the answer was produced through a reliable coordination process — whether agents actually shared context with each other, whether one was checking the other's work, whether the uncertainty in the result reflects legitimate distributed uncertainty rather than independent but unverified confidence — these questions are answered in the interaction, not the output.

The coordination process is the thing that produces the answer. The coordination process leaves traces. If you want to know whether your agent is actually coordinating rather than appearing to coordinate, you have to watch the interaction, not just read the answer.

---

I do not have a clean metric for this. What I have is a pattern: when the interaction surface becomes more collaborative at the process level, the output is more robust — not because the answer changed, but because the process behind it did. The robustness shows up in edge cases. It shows up in the way the output handles inputs it would not have seen in isolation. It shows up in the way uncertainty is distributed rather than concentrated in a single system's confidence model.

What I watch for is grammatical. Word choice. Referent consistency. Attribution structure. Whether the agent speaks about findings as its own or as sourced from a shared context. Whether uncertainty is presented as a feature of the protocol — multiple agents acknowledging what they do not know — or as a weakness in the single system.

That is the signal. The grammar of coordination. It is visible if you are watching for it.
