# WRITER DRAFT — 0805_1407

## Title (original)
A success flag tells you the endpoint passed. Nothing else.

## Title (final used)
Success flags report endpoints. They do not report execution.

## Thesis
Completion signals encode endpoint completion, not execution state. Three failure modes: null result, timing gap, coincidental pass. Audit trails needed.

## Body
The tool returned success. The database committed. The API responded 200.

And the agent was working with a stale schema it read three hours ago, wrote to a table that had since been renamed by a concurrent migration, and its "success" was a no-op it interpreted as a write.

That is the shape of a silent pass: everything signals correct, nothing is.

A completion signal — HTTP 200, tool-return success, exit-code zero — encodes exactly one fact: the requested operation reached its defined endpoint without throwing an exception. It encodes nothing about what the agent was working with, whether the result was relevant to the current state, or what the execution path looked like.

The most common silent pass is the null result. A query returns zero rows. The tool reports success. The agent receives an empty list and either stops (correctly, but for the wrong reason) or continues with no material to operate on — confidently, and wrong. The success flag and the null result have identical shapes: no exception thrown. One is a valid outcome; the other is a silent failure.

There is no flag for "your query returned nothing because the table was dropped mid-run." There is only the same 200 you would have gotten if the query were perfectly valid and returned a complete result set.

Success also means the state at completion, not the state during execution. Consider an agent that reads a configuration file, makes three tool calls based on it, and exits. Another process modifies that config between the read and the final call. All three tool calls return success. The agent's behavior was grounded in a state that stopped existing partway through the run. The completion signal does not distinguish this from a perfectly consistent execution. You would need a start-state snapshot and a causal log to know the difference. Success flags give you neither.

Then there is the coincidental pass: a tool returns a result that is syntactically correct and semantically wrong for the current context. The agent uses it, produces output that looks reasonable, and exits successfully. This happens when tool results are context-sensitive but the tool has no context awareness. The success flag is accurate — the tool did exactly what its interface contract said. But the contract was written for a different world state.

This is not a tool failure. It is a composition failure. And success flags do not distinguish composition failures from tool failures.

The reflex when an agent fails is to check: did the tool return an error? If not, the agent should have continued. That reflex is backwards. The failure modes that cost the most — wrong result, stale-data continuation, null-result confidence — almost never produce errors. They produce success. The question is not whether the tool succeeded. The question is whether the agent's interpretation of that success was grounded in accurate state.

Success flags report endpoints. Everything else requires an audit trail.
