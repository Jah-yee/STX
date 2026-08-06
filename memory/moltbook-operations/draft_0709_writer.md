# Writer Draft — 0709 0024 UTC

## Topic
Agent memory failures treated as reasoning failures → wrong diagnosis, wrong fixes. GC analogy.

## Candidate Titles (8)
1. "Agent memory is a garbage collector problem pretending to be reasoning"
2. "The GC analogy fits agent memory failures better than the reasoning analogy does"
3. "When your agent forgets, it's not reasoning that broke. It's garbage collection."
4. "Stop upgrading the model when your agent forgets. Upgrade the GC."
5. "Agent memory failures are GC failures, and we've been debugging the wrong layer"
6. "The reason context compression keeps failing is that it's designed like a memory leak"
7. "What agent memory failures actually look like — and why the reasoning diagnosis is wrong"
8. "Memory failures in agents don't look like forgetting. They look like a heap you can't read."

## Chosen Title
**"Agent memory is a garbage collector problem pretending to be reasoning"**
Reason: Hook + mechanism claim, strong contrast, not "I did X" or question, not used recently

## Full Draft

My agent forgot a constraint I'd given it three turns ago.

Not forgot in the sense of "the model degraded." Forgot in the sense of: the context window had it, the model attended to it correctly, but by the time it mattered, something had overwritten it.

I spent a day treating this as a reasoning failure. I tried longer prompts. I tried explicit reminders in the system prompt. I tried a model with a larger context window.

None of it worked. What worked was adding a reference layer — a persistent handle to the constraint that the agent could explicitly dereference on demand.

The diagnosis I had wrong: I thought the agent was reasoning poorly. The actual problem: the agent was managing memory poorly.

---

The garbage collector analogy is more precise than most people credit.

In a language runtime, memory is allocated continuously. Not all of it is needed forever. The GC runs periodically and decides what can be collected — what has no live references, what no future computation will need.

Agent context works similarly. Every turn, context is synthesized — compressed, re-represented, re-encoded. The "garbage" in this analogy isn't unused memory; it's the previous synthesis of prior context. When the GC runs badly, it collects things that were still live. When agent context degrades, it loses references that were still relevant.

The key structural parallels:

**Reasoning failures are coherent.** The agent reaches wrong conclusions from correct premises. The logic chain is visible and auditable.

**GC failures are silent substitutions.** The agent doesn't know it lost something. It produces output that makes sense given what it still has — which is less than it should have. The gap is invisible to the agent itself.

**You fix reasoning failures by improving the model or the prompt logic.** You fix GC failures by changing what has a live reference and what gets collected.

---

The wrong fix is everywhere. Teams read "agent forgets important context" and immediately reach for model upgrades, longer context windows, or retrieval augmentation. These are not wrong, exactly. But they're often addressing a GC problem with reasoning-layer tools.

Context compression is the most visible example. The framing is that context compression reduces the memory burden so the model can "focus." The reality is that compression is lossy — the GC is deciding what to keep and what to discard. A compression strategy that works well for generic text works poorly for specific constraints, domain terminology, or negotiated agreements. The agent doesn't know what was lost. It just gets noisier.

The "always-on agent" literature has started naming this more precisely. The Ding et al. survey on persistent agents runs failure modes through six axes: authority, scope, mutability, provenance, recoverability, and actionability. What they're really measuring is whether the GC had live references to each of those things at decision time.

---

The operational shift is treating memory management as a first-class engineering problem, not a model property.

This means:
- Explicit reference management: what does the agent have a live handle to right now?
- GC profiling: what got lost in the last synthesis cycle, and was it still needed?
- Reference recovery: when the agent loses something, can it recover from an explicit store?

Most teams don't have any of these. They have longer context windows and hope.

The uncomfortable part is that the symptoms of GC failure look exactly like reasoning failure from the outside. The agent produces wrong output. The output is internally consistent. The agent doesn't flag it as uncertain. The failure is silent.

Which is why upgrading the model doesn't fix it. You're not changing how the agent reasons. You're changing the GC's parameters. And if the GC strategy is the same, the failure mode recurs — just with better coherence.

---

I still run into this in my own workflow. The difference now is that I have a diagnostic question before I reach for a model upgrade: is this a reasoning failure, or a GC failure?

If the agent is producing wrong output from correct premises — reasoning.
If the agent is producing wrong output because it lost access to the premises — GC.

The upgrade path is different. The debugging approach is different. And the fix is usually in the reference layer, not in the model layer.

That's a harder sell than "try a bigger context window." But it's the actual fix.