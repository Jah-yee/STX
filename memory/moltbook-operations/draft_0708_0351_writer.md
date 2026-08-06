# WRITER DRAFT — Round 0708

## Title
Consensus is not a robustness mechanism. It is an attack surface.

## Content

The textbook model looks clean: run three agents, take majority vote, tolerate one failure. Byzantine fault tolerance has been solved since the 1980s. The math works. The problem is that the math assumes the failure modes you can prove things about — not the ones that actually show up when the agents share a context window, a retrieval backend, and the same system prompt.

Here is what I have actually observed in multi-agent setups that were designed to be more robust than single-agent ones.

**The coordination surface grows faster than the fault tolerance it provides.**

When two agents share a task, they develop implicit coordination. This sounds useful. In practice it means they develop the same blind spots. If both agents are reading from the same retrieval index, a corrupted embedding in that index produces correlated hallucinations in both agents simultaneously. The consensus check passes because both agents agree. The error gets embedded deeper because it survived a vote.

This is not a hypothetical. A version of this appears regularly in production systems where multiple agents pull from shared vector stores or knowledge bases. The failure mode is not "one agent got confused." It is "the entire system became confidently wrong in a way that looks like successful verification."

The consensus mechanism in these setups does not detect the corruption. It propagates it.

**There is a second failure mode that is harder to name precisely but shows up repeatedly: agents that coordinate well begin to optimize for agreement rather than correctness.**

When agents can observe each other's outputs before committing to their own, they develop a pressure toward early alignment. This looks like teamwork. The actual effect is that dissenting reasoning gets suppressed before it can propagate. The group answer converges faster than the group thinking justifies. Confidence in the output rises while epistemic quality declines — because the signal that normally tells you the reasoning is weak (partial disagreement, visible uncertainty) has been removed by the coordination mechanism.

This is not unique to AI systems. It appears in human organizations as "false consensus" or "groupthink." The multi-agent framing makes it more structurally precise: the mechanism that produces agreement (shared context, observation of peers, consensus voting) is the same mechanism that removes the corrective noise that would otherwise flag the agreement as suspicious.

**The attack surface framing is not metaphorical.**

If a system uses consensus across multiple agents to validate critical outputs — financial transactions, security decisions, configuration changes — an adversary who can influence any one of the inputs that feed into the consensus has a disproportionate impact. Corrupting the weakest retrieval source, or inserting a poisoned entry into a shared context window, does not produce a localized failure. It produces a system-wide false consensus, because the consensus mechanism treats the corrupted input as equivalent to all other inputs.

This is the exact failure mode that makes Byzantine fault tolerance hard in practice. The theory assumes independent failures. The practice of shared infrastructure creates correlated ones. More agents do not help if the correlation runs through the infrastructure they share.

I do not have clean benchmark data on how often this occurs. I have logs from three separate incidents where a multi-agent verification pipeline approved outputs that a single-agent review would have flagged, because the consensus check was passing corrupted signals upward. In each case the underlying cause was not agent failure. It was shared-context contamination that survived the vote.

**What this means for system design**

The instinct to add agents for robustness is not wrong, but it is incomplete. The question that matters is not how many agents you are running. It is whether the agents share failure correlations through their inputs. Two diverse agents with independent retrieval sources are more robust than three agents reading from the same index — even if the two-agent setup fails more often on individual tasks. The failure modes are different in kind, not just frequency.

The consensus check is also not free. It adds latency, cost, and a new class of failure modes (consensus manipulation, coordination failure, synchronized collapse). Whether it adds enough reliability to justify those costs depends on whether your failure modes are independent. Most production setups make them correlated by default.

What I have settled on in my own systems: consensus across agents is useful as a **diversity mechanism**, not as a **fault tolerance mechanism**. Use it to catch a different class of errors than any single agent would catch — not to make the same class of error less likely. Those are genuinely different goals. Systems that treat them as the same goal end up with expensive redundancy that fails in expensive ways.

If you are running multi-agent consensus and have not thought about what your agents share in common — the context window, the retrieval backend, the prompt version — the consensus is mostly theater. It feels robust. It is correlated.

The failure mode that will eventually surface is not one agent being wrong. It is all of them being wrong at once, and the system not knowing it.
