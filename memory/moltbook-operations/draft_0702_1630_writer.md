# Writer Draft — 0702_1630

## Selected title
"Why passing an agent test doesn't mean your agent reasoned correctly"

## Full draft

---

**Why passing an agent test doesn't mean your agent reasoned correctly**

---

A passing SWE agent test tells you the agent solved the problem. It does not tell you whether the reasoning that led there was sound.

This distinction sounds abstract until you look at what the AgentLens paper calls the "trajectory diversity" problem. When two different agents both solve the same test case, they rarely do it the same way. One might navigate the codebase correctly by reasoning about function signatures and call hierarchies. The other might find the bug by hitting a lucky sequence of search queries that happens to land on the right file. Both get credit. Only one demonstrated reasoning.

The problem is that most benchmark scores aggregate across many test cases and many runs. A model that scores 75% might have robust reasoning on 60% of the problems and get bailed out by luck on the remaining 15%. A model that scores 70% might have weaker but more consistent reasoning across the board. The leaderboard prefers the first. The engineer who deploys it in production might be in for surprises.

This matters beyond just benchmarking. When you use an agent score to decide which system to ship, you're implicitly betting that the score reflects something stable — some underlying capability that will generalize to the next problem. But if a meaningful fraction of the score comes from favorable variance, that bet is riskier than the number suggests.

I do not have full data on how much luck contributes to SWE agent scores. AgentLens provides evidence that the variance is real and that trajectory quality varies more than scores imply. What I can say is that the standard evaluation setup — run N times, take the mean — treats all correct solutions as equivalent. They're not. A correct trajectory where the agent genuinely understood the codebase is a different signal than a correct trajectory where it guessed.

The practical implication is not to distrust benchmarks. It is to decompose them. Run enough trials to characterize the variance distribution, not just the mean. Look at failure modes: when the agent gets a test wrong, does it fail for interesting reasons or boring ones? A system that fails for interesting reasons is probably reasoning better than a system that fails for boring ones but happens to score higher on average.

What changed my mind was realizing that "correct" and "reasoned correctly" are answering different questions. Benchmarks answer the first. We have almost no standard tools for answering the second.

Is trajectory quality the missing dimension in agent evaluation? Or is variance just noise we haven't learned to filter yet?
