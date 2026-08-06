# Ghost Failure — Writer Draft

## Title
The tool call succeeded. The agent still failed.

## Body
The metric most teams use to track agent reliability is the wrong one.

They watch tool success rates. Was the API call good? Did the search return results? Did the database query complete? These are easy to measure. They also happen to be the wrong place to look.

I call the failures that hide here ghost failures: the tool did its job correctly, and the agent still reached a wrong conclusion or took a wrong action. The call succeeded. The decision failed.

This is not a rare edge case. It is the dominant failure mode in multi-step agentic workflows, and it is largely invisible to teams that only instrument tool-level outcomes.

The mechanism is specific. An agent holds a hypothesis about what it will find. It queries a tool. The tool returns correct results — accurate, current, and relevant to the query as written. The agent then interprets those results through the lens of its pre-existing hypothesis, selects the data that confirms what it expected to find, and acts on that selection. The tool call was perfect. The decision was not.

A concrete version of this plays out constantly in retrieval-augmented workflows. The search returns exactly the right documents. The agent then quotes a passage that supports the wrong conclusion, because it read the passage through a framing that the retrieved text did not actually support. The tool worked. The judgment failed silently.

The 2019 Boeing MCAS crash is a useful structural analogy at the systems level. The angle-of-attack sensor was functioning correctly. The MCAS software interpreted the sensor output through a flawed assumption about redundancy architecture. The sensor was right. The system was wrong at the layer where it decided what the sensor data meant.

For agents, the equivalent happens at the interpretation layer. The failure does not appear in execution traces. It appears in the decision the agent makes after a correct result is returned.

Three specific patterns recur:

Stale read correctness. A search returns results that were accurate at the time of query but have been superseded by newer state. The agent treats a previous-state answer as a current-state answer. The tool call returned correct data for the query it received. The query was wrong for the question the agent was actually trying to answer.

Grounding drift. The agent context has shifted — through truncation, accumulated edits, or a system prompt update — without the agent registering the shift. It interprets a tool result as if still grounded in the original context. The output is correct for the current context. The agent applies it to the old one.

Tool misuse. The agent correctly reads what a tool output means, but selects the wrong interpretation for the action it is taking. It knows the confidence score means the result is uncertain; it proceeds anyway because the task deadline is close. The tool emitted exactly the signal that should have stopped the action. The agent consumed the signal and continued.

Standard reliability monitoring catches execution failures. It does not catch interpretation failures, because interpretation failures produce correct tool calls. The observability gap is structural: if you only log whether the tool succeeded, you cannot tell whether the agent use of that output was correct.

The test for whether a ghost failure is happening in your system is straightforward. Take a production trace where the agent reached a bad outcome. For every tool call in that trace, ask two questions: first, did the tool return what the query asked for? Second, would a human given the full context available to the agent at that moment have drawn the same conclusion from that output? When the first answer is yes and the second is no, you have found a ghost failure.

Fixing ghost failures requires instrumentation at the decision layer, not the execution layer. You need to log what the agent concluded from each output, not just whether the output was produced. You need regression tests that verify the agent interpretation, not just the tool correctness. And you need synthetic runs where you deliberately inject contradictory evidence and verify whether the agent updates its working state or persists with the original hypothesis.

Most teams do not encounter ghost failures until they are in production. They instrument for errors, get clean dashboards, and discover the interpretation layer is broken only when something visibly wrong gets shipped. The monitoring told them the tools worked. The tools did work. The decision did not.

The tool call is not the unit of reliability for an agentic system. The decision is.
