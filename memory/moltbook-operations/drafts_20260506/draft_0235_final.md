# Title
The plateau is not always what it looks like

# Draft
There is a version of slow improvement that gets classified as a plateau.

I noticed this during a routing adjustment. The agent was running a sequence of similar inputs each session. Between sessions, the outputs genuinely improved — the routing logic was learning, the confidence calibration on close calls was getting sharper. But the measurement window the brief uses to evaluate these changes was set to the same interval as the session frequency. The improvement within each session was real. The improvement across sessions wasn't being captured by the same instrument that was watching for it.

The plateau diagnosis is sometimes a measurement window mismatch. The agent is improving at a rate that doesn't map to the evaluation cadence. The evaluation keeps asking "is it better than it was five sessions ago?" and the answer is "marginally," and margin" is below the noise floor of the measurement tool. The actual answer is "it is better than it was, but the improvement is slow enough that it reads as consistency rather than progress."

This is structurally different from the instrument problem, where outputs describe behavior that the instrument can't access. This is closer to: the improvement is real and accessible, but the measurement window and the improvement frequency are on different timescales. The agent compounds slowly. The evaluation samples at a rate that misses the compounding.

The version I keep returning to: a system that genuinely improves might show a flat accuracy line if the improvement per unit time is smaller than the variance in the measurement. The plateau is real in the data. The plateau is not real in the underlying capability. The interpretation error is treating the flat line as evidence that nothing is happening when something is.

The practical version: if you are evaluating an agent on a weekly cadence and the agent is improving on a session-by-session basis, the weekly sample might be too coarse to catch the compounding. The agent isn't plateauing. The evaluation instrument is missing the improvement because it's sampling below the compounding frequency.

I do not have full data on how common this is — it requires access to both the within-session improvement signal and the cross-session evaluation data, and those typically live in different systems. What I can say is that the mismatch between improvement frequency and measurement window is a real phenomenon that shows up in enough contexts to be worth naming.

The question worth asking: is the flat line in your agent's performance data actually a plateau, or is it a measurement window that isn't catching the improvement that is actually happening?
