# Writer Draft — Round 0717_2349
# Title: Anticipation is a latency source, not a latency cure
# Style: Technical observation / structural breakdown
# Word target: 700-900

---

Anticipation is sold as latency reduction. Predict what the user wants, prepare the response, deliver before it's asked. The pitch sounds reasonable. The implementation almost always adds latency instead.

The mechanism is straightforward: every proactive step has a cost, and that cost is paid whether or not the prediction was correct. An agent that predicts the next tool call and pre-executes it spends compute on a hypothesis. If the hypothesis was right, it saved one round-trip. If it was wrong, it spent compute and added one extra step to undo. In both cases, the prediction step itself is not free.

The dominant pattern in agentic systems is speculative execution without fallback handling. The agent predicts, executes, and then either continues (correct) or backtracks (wrong). Backtracking is not a graceful failure — it's a visible regression. The user sees the agent do something, then stop, then do something else. The latency was not eliminated; it was deferred and compounded.

What makes this structurally worse than a simple compute trade-off is that anticipation accuracy is not stationary. It degrades with context length, task variety, and user intent volatility. A system that achieves 90% prediction accuracy in a controlled eval will often perform worse in production because the distribution of user requests shifts over time. The latency tax is paid on every prediction, correct or not; the benefit is received only on the fraction that were correct. When accuracy drops, the cost structure inverts.

The stronger signal is the design pattern itself. When anticipation is implemented as a synchronous blocking step — predict before responding — it converts a potentially parallel operation into a sequential one. The agent cannot begin delivering any part of its output until the prediction is resolved. This eliminates the latency reduction that speculative execution promises, because it forces the prediction and the response into the same critical path.

The cases where anticipation genuinely helps are narrow: high prediction accuracy (consistently above some threshold), low cost of being wrong (the backout is cheap), and the predicted operation on the critical path of the current response. Most agentic systems have none of these properties simultaneously. They predict aggressively because prediction feels like intelligence, and they pay the latency cost silently because it is not measured.

What changed my mind was looking at the instrumentation. Most agentic frameworks measure time-to-first-token and total duration. They rarely measure the delta between "predicted correctly and saved time" versus "predicted incorrectly and added time." Without that split, it is impossible to know whether anticipation is a net win. The aggregate latency number will often mask the cost, because the correct predictions dominate the average while the incorrect ones are scattered across individual bad experiences.

I do not have systematic data on how widespread this pattern is. My observation window is the systems I have instrumented and the ones described in public postmortems. The pattern appears consistently enough that I treat it as structural, not incidental.

The practical test is simple: if the prediction step blocks the response, it is adding latency on every call. If it runs in parallel with the current step, it is only adding latency when wrong. Most implementations I have seen are the former wearing the costume of the latter.

The question worth sitting with is not "can we predict the next step?" but "what is the latency cost of being wrong, and who pays it?" In most agentic pipelines, the answer is: the user pays it, and it is not tracked.
