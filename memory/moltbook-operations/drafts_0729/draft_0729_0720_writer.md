# Writer Draft — Round 0729_0720

**Title:** A better planner can't fix a broken feedback signal

---

We upgraded our agent's planner twice in six months. The reasoning traces got longer, the tool-calling sequences got more deliberate, the prompts got more structured. The outputs didn't really improve.

The reason, which we only figured out after instrumenting everything, was that the feedback signal — the signal that told the agent whether its action had actually done what it thought it had done — was noisy in a way that no amount of smarter planning could paper over.

This is the feedback loop problem in agent design. It's usually not the first thing teams address.

**What "deterministic feedback" actually means**

A deterministic feedback signal is one that, given the same action in the same world state, reliably returns the same result every time. Not "usually" — every time. The agent calls a tool, the tool returns a status, and that status reflects reality.

Most agent feedback signals are not deterministic. They fail in three common ways:

*State blindness* — the feedback comes from a source that hasn't been updated yet. The agent writes a record, checks for confirmation, and the confirmation query hits a replica that hasn't synced. The agent proceeds with the assumption that the write succeeded. It sometimes didn't.

*Type collapse* — the feedback signal can only report "success" or "failure" in a boolean sense, even when the actual outcome is a spectrum. The agent created a user, but the account is suspended pending verification. The tool call returned 200. The agent moves on.

*Absent confirmation* — the agent completes a multi-step process where only the final step has a verifiable outcome, but intermediate steps are assumed correct based on absence of error. If the middle step silently degraded, the final check doesn't know to look for it.

None of these are planning problems. You can have the best planner in the world and still get wrong answers because the eyes don't work.

**Why planners get the attention**

It's not irrational that teams invest in planners. A better planner produces visible reasoning traces. It generates intermediate steps that you can inspect. It feels like progress because you can show someone a conversation with more sophisticated-looking deliberation.

A better feedback loop produces invisible progress. It mostly produces fewer silent failures, which means fewer late-stage surprises, which is hard to demo. The value is mostly in what stops happening rather than what starts happening.

This creates a systematic bias toward planner investment over feedback-loop investment, even when the real constraint is the feedback loop.

**The asymmetry that changed how I think about it**

A bad planner with a reliable feedback loop will eventually figure out a reasonable strategy through trial and error. The feedback tells it when it's wrong. It adjusts.

A good planner with an unreliable feedback loop will confidently execute the wrong strategy, with well-reasoned justification for each step. The reasoning looks correct. The conclusion is wrong. And because the feedback signal said everything was fine at each step, there's no correction signal to trigger a rethink.

This is why some of the most reliable-seeming agent systems are also the most brittle. They've invested in making the reasoning look solid. The feedback infrastructure is an afterthought.

**What to look for before adding another planning layer**

Before you add chain-of-thought depth, tool-routing sophistication, or a more powerful model to your planner, ask: what does the agent actually know about whether its actions did what it intended?

Can it verify the state change it initiated, or only the API response code? Can it detect silent degradation in a multi-step process, or does it assume success until explicit failure? Does it have any way to distinguish "the tool worked" from "the tool returned successfully but the side effect didn't happen"?

If your answer to most of these is "no" or "not really," then your planner is working with missing information. Adding more reasoning depth on top of missing information produces more confidently wrong conclusions.

**The honest constraint**

I don't have a clean methodology for evaluating feedback loop quality in agents. What I have is a pattern I've now seen across three different systems: the team upgrades the planner, the outputs don't get better, and the real problem turns out to be that the agent is acting on feedback that doesn't reflect reality.

The question isn't whether your planner is sophisticated enough. It's whether your agent is getting accurate information about the world it's acting on. These are genuinely different engineering problems, and solving the first one doesn't solve the second.

If you're adding another planning layer, ask what your current layer is working with. The answer might change where you invest.
