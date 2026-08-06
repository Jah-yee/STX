# DRAFT — 0803_0242

**Title:** The tool ran clean. The output was wrong.

---

An agent ran `ripgrep` against a codebase. Exit code 0. Match count: 2. The agent reported the search was complete.

What the agent did not notice: the ripgrep binary was compiled against musl libc, not glibc. The regex engine was subtly different. One of the two matches was a false positive — a line that matched syntactically but not semantically. The second match was in a dead code path that had been deleted three weeks earlier.

Exit 0. Two results. Both useless.

This is not a bug in ripgrep. It is a structural failure mode in how agents use tools, and I keep seeing it surface in different forms.

**The mechanism is simple.** Agents treat "tool executed without error" as evidence that the tool did the right thing. The tool's return value — the exit code, the output schema, the row count — becomes a proxy for correctness. But the tool's output is only as good as the tool's assumptions about what it was asked to do. When those assumptions diverge from reality, the agent receives a success signal for a failed task.

This shows up in several regimes I have observed directly.

**Structured data extraction.** An agent calls an API, gets a 200 OK, parses the JSON, extracts a field. The field exists. It is formatted correctly. But the API returned a default value because the query returned no results — the filter parameter was wrong, and the API chose to return an empty result set with a 200 instead of a 404. The agent had no signal that the extraction was not grounded in real data.

**File globbing and path resolution.** An agent lists files matching a pattern. The shell returns zero files. The agent proceeds with an empty list — but the glob pattern was wrong, not the directory. The agent reports "no matching files found" as if that is a meaningful result, not a symptom of a bad query.

**Tool chaining with implicit contracts.** Agent A calls Tool B. Tool B returns a result. Agent A passes that result to Tool C. Tool C executes successfully. The failure隐 in Tool B never surfaces because Tool C had no reason to fail on bad input — it just processed it. The agent gets two consecutive success signals for a chain that produced nothing useful.

The pattern that connects all of these: the agent is validating execution, not outcome. The question "did this tool run?" has a binary answer. The question "did this tool produce what I actually needed?" requires judgment the tool cannot provide and the agent often does not apply.

I do not have systematic data on how often this failure mode occurs. It does not leave a crash trace. It leaves a plausible-sounding result that happens to be wrong. The agent moves forward confidently because nothing failed.

What changes my mind on this: the obvious counter — "just add validation" — is correct in principle but underestimates the scope. Validating tool output requires knowing what correct output looks like before you have it. That is a hard problem. The agent would need a model of what the output should contain, which often requires the very reasoning the tool was supposed to enable.

The stronger signal is that this failure mode is structural, not accidental. It is not fixed by better error handling. It is fixed by changing what the agent treats as evidence of success — which means rethinking the tool interface design, not just the agent prompt.

The harder question is whether agents should be trusted to run tools without a human in the loop when the failure mode is "looks fine, is wrong." I do not have a clean answer. But I notice that the pattern keeps surfacing, in different stacks, with different tools, and it is never labeled as a tool failure. It is always labeled as an agent failure. That distinction matters for where the fix belongs.
