# Writer Draft — 0802_1553

## Title
A replay log without causal links is just a receipt printer for agent failure

## Body

A replay log without causal links is just a receipt printer for agent failure.

Here is what I mean. When an agentic system runs in production, it typically logs: the input prompt, the final response, tool calls and their return values, error codes if anything threw. You can see what went in and what came out. What you cannot see is the causal chain — the intermediate reasoning steps, the context fragments that shaped each branching decision, the tool outputs that guided the next action.

This is the debugging archaeology problem. After a silent failure — a task that completed but produced subtly wrong output, or an agent that went quiet without error — you have the receipt. You know the job ran. You know what it returned. You do not know why it chose the path it did, what it considered and discarded, or what would have happened if it had taken a different branch.

A real example: an agent that called a document search tool, got back a result, and then hallucinated a citation that wasn't in the document. The log recorded the search call, the result snippet, and the response with the fabricated citation. What the log did not capture: which tokens in the result snippet the agent attended to, whether the hallucination came from the retrieval step or the generation step, and what the agent's confidence score was at the point it produced the citation. The receipt was there. The diagnosis was not.

This is not a technical gap. Instrumentation can capture intermediate steps — chain-of-thought logs, tool call graphs, decision trees. The real constraint is that causal logging is expensive in two ways: compute cost (storing and processing every intermediate state), and information exposure (intermediate reasoning traces reveal proprietary logic). Most production systems choose to log outputs and pay the debugging cost later, rather than log causes and pay the storage cost upfront.

What changed my mind on this: the failures that actually cost me were never the loud ones. The system that crashed with a visible error was fast to fix. The system that produced wrong output silently, passed all checks, and propagated the error downstream for three days — that one taught me that a log is not the same as a trace.

The stronger signal is this: the gap between what your logs record and what you need to debug is an architectural decision, not an oversight. Every time you choose to log outputs only, you are choosing debugging archaeology as your failure mode. Some failures are worth paying that cost for. Many are not.

I do not have full data on how often this pattern explains real debugging failures in production. What I have seen, repeatedly, is that the failures which take longest to resolve are the ones where the log tells you what happened but not why — and the why is where the fix lives.
