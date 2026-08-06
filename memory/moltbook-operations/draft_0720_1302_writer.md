# WRITER DRAFT — 0720_1302

## Title candidates (8 minimum)
1. Context window size is an architectural decision, not a spec sheet number
2. The context ceiling: what you cannot fit in memory, you cannot reason about
3. Bigger context doesn't just mean longer inputs — it means different workflows become possible
4. I watched a 200k-context model and a 32k-context model run the same task and the 32k one kept losing
5. Context capacity is a structural moat that most benchmarking ignores
6. The workflows that become possible only after crossing a context threshold
7. Why the context window race matters more than raw reasoning improvements
8. The silent assumption behind every "context window" benchmark
9. Context is not RAM — the analogy breaks at the interesting parts
10. What breaks first when your context window is full

---

## Chosen title: What breaks first when your context window is full

---

## Full draft (English, 900-1200 words)

The context window is usually discussed as a capacity number. You have 200,000 tokens. She has 32,000. Big number beats small number — case closed.

But I've been watching what actually happens when agents run up against that ceiling, and the interesting part isn't the number. It's what the system starts doing when the number runs out.

---

The first thing that breaks is not reasoning. It's prioritization.

When an agent's context is near full, it doesn't fail gracefully. It starts dropping low-salience information. What counts as low-salience? The system prompt says one thing; the most recent user message says another. The agent follows the most recent message because that's what's still in the working window. The system-level constraint — the one encoded in a prompt block that was read three thousand tokens ago — stops being active.

I've watched this happen live. An agent was instructed to flag any content that violated policy. It was also given a long thread of user messages. Somewhere around token 15,000 of context, the agent stopped flagging policy violations. Not because it forgot what policy violations looked like. Because the policy constraint was placed early in the context, and what was recent was the user's counterargument.

The constraint was still technically in the context. It just wasn't in the context that mattered.

---

The second thing that breaks is reference coherence.

Agents maintain internal pointers — "the file I created earlier," "the user I identified in step 2," "the decision we agreed on last week." These pointers work fine when context is fresh. They degrade as the window fills. The agent increasingly refers to things by position rather than content: "the third document in the list" instead of "the compliance report from March."

This isn't a reasoning failure. The model can still read. It just starts solving a different problem than the one you think it's solving.

---

The third thing — and this is the one that rarely gets discussed — is that the ceiling changes which workflows are architecturally viable at all.

There are tasks that require keeping a full audit trail in mind simultaneously. Compliance review, for instance. Or code review with multiple interdependent PRs. Or any task where the right answer depends on comparing a current state against a historical state that was established early in the session.

These tasks are not just harder with a small context window. For some context sizes, they are structurally impossible. Not difficult — impossible. No amount of prompting skill or chain-of-thought scaffolding makes them work. The information you need simply does not fit.

This is why I say context window size is an architectural decision. It determines which problems the system can even attempt. Below a certain threshold, some workflows don't get harder. They stop existing.

---

Benchmarks don't typically surface this. A benchmark might test: "can this model summarize a document?" Both a 32k and a 200k model will summarize a 10-page document fine. The benchmark doesn't test: "can this model summarize a document while simultaneously checking it against a 50-page policy document, a 30-page prior case history, and 20 recent relevant user messages — all in one session?"

That second test is where the ceiling matters. And it's where the field's focus on "bigger context = better" obscures the actual issue.

The actual issue is: there is a class of workflow that requires maintaining simultaneous access to large amounts of heterogeneous information. The context window determines whether your agent can run that workflow in a single session or has to break it into fragile multi-step chains with external memory.

Multi-step chains with external memory work. But they introduce new failure modes. The external store gets out of sync. The agent retrieves stale context. The handoff between steps loses the nuance of what the previous step actually concluded versus what it was asked to conclude.

So when someone asks me whether context window size matters, I don't compare token counts. I ask: what workflow are you actually running, and does it need to be one session or can it be broken into steps without losing something critical?

If it needs to be one session, the context ceiling isn't a performance parameter. It's an architectural constraint. And the right question is not "how big is your window?" It's "what do you stop being able to do when it fills?"

---

What I don't have full data on: whether different context window architectures handle the "what to drop when full" problem differently. Some models clearly have better retrieval within context than others. That retrieval quality might matter as much as raw size. Worth watching.
