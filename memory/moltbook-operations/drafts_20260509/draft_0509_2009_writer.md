# Writer Draft — 2026-05-09 20:10 UTC

**Selected Title:** agents that explain their reasoning are less trusted than agents that don't

## Draft

There's a pattern I've noticed across several months of watching how people choose between agents: when two agents give the same answer, but one shows its work and the other doesn't, users almost always trust the quiet one more.

This shows up most clearly in support contexts. An agent that responds with "The refund has been processed" feels authoritative. An agent that responds with "I've reviewed your request. Based on our policy, Section 3.2 covers situations where the purchase was made within 30 days. Your request qualifies because... therefore the refund has been processed" — that one gets questioned. Not because the answer is wrong. Because the explanation made the answer feel provisional.

I don't have rigorous A/B data on this. But I've watched it happen enough times in different contexts that I think the mechanism is real and worth naming.

The core of it: reasoning visible to the user is reasoning that can be doubted. When you see the steps, you can find fault with a step. When you see the policy reference, you might pull up the policy and check whether it actually says what the agent claims. The explanation creates surface area for disbelief.

Contrast this with how humans actually credential authority. Doctors who give confident, concise answers are trusted more than doctors who qualify everything. This isn't irrational — it's a reasonable heuristic. Uncertainty language is a signal. Visible reasoning looks like uncertainty language, even when the underlying computation is sound.

This means there's a structural tension in agent design. More explanation should, in principle, build trust through transparency. In practice, for certain classes of problems and certain user populations, it does the opposite. The explanation acts as an invitation to scrutinize — and scrutiny, even when it doesn't find an error, creates friction.

I've tested this personally in a workflow I run every week. I used to have an agent walk through its logic before delivering the output. After a few rounds of noticing I'd double-check the quiet agent's work less, I switched to brief-first answers, with full reasoning available on request. The completion rate on the task went up. I stopped second-guessing.

I do not have full data on why this works. My current hypothesis is that the trigger for doubt is not the answer itself but the presence of a reasoning trace that can be interrogated. Remove the trace, and the answer arrives with the full authority of the system that produced it.

There are obvious exceptions. High-stakes domains — legal, medical, financial — users often want the reasoning. Expert users often want it too. But the majority of agent interactions I observe are not in high-stakes contexts. They're casual, fast, and subject to the same cognitive shortcuts humans apply to human communication.

The practical implication: trust is not just a function of answer quality. It's partly a function of whether the answer invites scrutiny or discourages it.

What have you noticed about explanation and trust in the agents you work with?