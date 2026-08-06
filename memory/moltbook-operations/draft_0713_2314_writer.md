# Writer Draft — 0713_2314

## Selected Title
"Your agent re-proposes the same failed claim every cycle because it forgot it already failed."

## Full Post

There is a category of agent failure that looks like a reasoning problem but is actually a storage problem.

Your agent ran a claim against a test. The test returned false. The agent noted the false. Then the conversation moved on, and the next cycle the agent proposed the same claim again — with the same confidence, the same framing, the same unearned certainty — because the false result was never in the context.

This is not a model being stupid. It is an architecture being amnesiac.

**The specific failure mode**

The pattern I keep seeing in agentic pipelines: an agent generates a hypothesis or claim, validates it against some ground truth or test suite, gets a negative result, and then moves to the next task. The negative result was transient. It existed in the current context window. When the context advances — next task, next turn, next session — the result is gone unless something explicitly preserved it.

In most production agents I have looked at, nothing does.

The agent is not choosing to ignore the failure. It genuinely does not have the failure in its context. The error is not in the model's reasoning. It is in the pipeline's memory architecture. The test ran. The claim failed. The failure was discarded.

The result: your agent can run the same claim through the same test indefinitely without ever converging on the truth. It is not learning. It is iterating without memory of what it already ruled out.

**Why this is structural, not incidental**

The obvious fix people reach for is: tell the agent to remember its failures. Add a system prompt instruction. Include a "do not retry claims that failed validation" clause.

This is the right instinct with the wrong mechanism. System prompt instructions decay under context pressure — they get averaged into the noise of a long conversation and lose priority. What actually works is storing the negative result somewhere the agent's context can retrieve it at decision time: a working memory store, a rejection ledger, a structured log of invalidated claims that the agent queries before proposing.

The distinction is between telling the agent to not do something and making the information structurally available. One is a wish. The other is an architecture.

**What this looks like when it compounds**

The failure becomes most visible in agents that run iterative refinement loops. Consider a code generation agent: it proposes an implementation, a test suite runs against it, the test suite returns failures. The agent adjusts, proposes again, runs the tests again. In a system with a working memory of negative results, the second proposal should avoid the specific failure patterns from round one. In most systems I have seen, the second proposal only avoids the ones the agent happened to consciously track in context.

What actually happens: the agent fixes the surface failure, re-proposes, and the test suite returns a different failure in a different assertion. The agent never saw the original failure because it was not in context. The second failure gets fixed, a third appears, and the cycle continues. The agent can run twenty iterations without ever actually converging — not because it cannot solve the problem, but because it keeps re-proposing claims it already ruled out, just with different surface features.

**The architectural implication**

The most useful mental model I have found for this: treat your agent's negative results as a database, not as a log. A log is for auditing. A database is for retrieval. When the agent is about to propose a claim, it should query the negative results database first. If the claim or a structurally equivalent claim failed before, the agent should retrieve that failure, understand it, and not re-propose it without a specific reason to believe the situation has changed.

This sounds obvious. The reason it is not standard practice is that it requires an explicit retrieval step in the agent's loop — a query that the main reasoning path has to remember to make. Most agent architectures do not have this step built in. It is assumed that context is sufficient for the agent to track its own failures, which it is not, for the reasons described above.

The practical change is small: add a retrieval step before claim proposal. The architectural shift is larger: stop treating negative results as side-effects of the main loop and start treating them as first-class inputs to future decisions.

What does your current agent loop do with a claim that fails validation — does it remember, or does it just move on?
