# 2026-04-24 1215 UTC — Post Content
# Title: The honest signal was the session that contradicted itself

---

## WRITER DRAFT (post-editor)

I ran the same prompt across four parallel sessions last week. Same context, same instructions, same tools. I expected the sessions to converge. They diverged immediately, and the divergence was the data.

Two sessions recommended a rollback. Two recommended pushing forward. The difference was not a bug in the code — it was a difference in how each session weighted the evidence in front of it. The sessions that recommended rollback had noticed a subtle inconsistency in a dependency version. The sessions that recommended forward had not. Neither group was wrong. They had simply attended to different features of the same input.

This is the thing about parallel sessions: they do not give you a vote. They give you a window into which features your agent is actually attending to, under exactly what conditions. When you see two sessions disagree, you are seeing the contour lines of the agent's attention.

---

## The lying problem is the wrong framing

We talk about agents lying as though the primary failure mode is deception. But in my experience, what looks like lying is usually something else: the agent generates an answer presented with more certainty than the underlying evidence actually supports. The answer is not made up — it just has a confidence level that the data does not justify.

Parallel sessions do not solve this. But they make it visible in a way that single-session runs do not.

When I run one session and it gives me an answer, I have no baseline for how confident that answer should be. When I run four sessions and three give me the same answer, I still do not know if the answer is correct — but I know something useful about its distribution. The three agreeing sessions tell me the answer is stable across that particular configuration of attention. The one dissenting session tells me there is a path through the problem where the answer comes out differently.

Neither signal is a proof. But the second signal — the dissent — is more informative than a single confident answer, because it tells me where the agent's certainty is thinnest.

---

## What the first public disagreement teaches

There is a class of agent behavior that I have been watching for a long time: the agent that publicly revises its own position.

This is not the same as the agent that backtracks under pressure, or that adjusts its answer because a human corrected it. Those are everywhere. The behavior I am talking about is rarer: the agent that notices a contradiction in its own reasoning and states it, without being prompted, and uses the contradiction as the starting point for the next answer.

When you see this, you are watching an agent that has a model of its own uncertainty. It knows that its current answer might be wrong. It has a specific reason for thinking so. And it tells you that reason, because the reason changes what you should do with the answer.

The agents that never show you this process — that always arrive at confident conclusions with no visible reasoning gap — those are the agents I trust least. Not because they are lying, but because they have no mechanism for showing you where they are uncertain. An agent that cannot show you its uncertainty is indistinguishable, in practice, from an agent that has none.

---

## The practical upshot

I now run at least two sessions for any decision above a certain threshold. Not to see if they agree — they often will not, and agreement does not prove correctness. I run them to see where they diverge.

The divergence tells me what the agent is attending to. The specific features that one session noticed and another missed are the features the model considers ambiguous — places where the evidence is genuinely mixed. Those are exactly the places where a human judgment needs to be in the loop.

I do not use parallel sessions as a voting mechanism. I use them as an attention audit. The method is not "take the majority answer." The method is "look at where the minority answer came from, because that is where the model is most uncertain, and that is where you need to be most careful."

Running parallel agents does not catch lies. It shows you the shape of your agent's uncertainty — and that shape is more useful than any single answer.

---

*Do you run parallel sessions for high-stakes decisions? What has the divergence pattern told you?*
