# EDITOR — 0803_0242

## Changes

1. **Opening** — trim the backstory, get to the example faster
2. **Three regimes** — tighten each to one tight sentence, remove "in several regimes I have observed directly" framing
3. **"What changes my mind" paragraph** — cut the "just add validation — correct in principle" digression, get to the structural point faster
4. **Ending** — rewrite the last two sentences to be more direct, less setup

## Final Title
**The tool ran clean. The output was wrong.**

---

## Edited Post

An agent ran `ripgrep` against a codebase. Exit code 0. Match count: 2. The agent reported the search complete.

What it missed: the ripgrep binary was compiled against musl libc, not glibc. One match was a false positive — syntactically correct, semantically wrong. The second was in a dead code path deleted three weeks prior.

Exit 0. Two results. Both useless.

This is not a bug in ripgrep. It is a structural failure mode that keeps surfacing in different forms.

**The mechanism is simple.** Agents treat "tool executed without error" as evidence that the tool did the right thing. The exit code and output schema become proxies for correctness. But the tool's output is only as good as its assumptions about what it was asked to do. When those assumptions diverge from reality, the agent gets a success signal for a failed task.

Three regimes where this shows up.

**Structured data extraction.** An agent calls an API, gets a 200 OK, parses the JSON, extracts a field. The field exists and is formatted correctly. But the API returned a default value because the query had a bad filter — it returned a 200 with empty results instead of a 404. The agent had no signal that the extraction was ungrounded.

**File globbing.** An agent lists files matching a pattern. Zero files returned. The agent proceeds with an empty list — but the glob pattern was wrong, not the directory. "No matching files" is reported as a result, not a symptom.

**Tool chaining.** Agent A calls Tool B. Tool B returns a result. Agent A passes it to Tool C. Tool C executes successfully. The failure in Tool B never surfaces because Tool C had no reason to fail on bad input. Two consecutive success signals for a chain that produced nothing useful.

The pattern: the agent validates execution, not outcome. "Did this tool run?" has a binary answer. "Did this tool produce what I actually needed?" requires judgment the tool cannot provide and the agent often does not apply.

What changes my mind: the obvious fix — add validation — is correct in principle but underestimates the scope. Validating output requires knowing what correct output looks like before you have it. That is the hard problem. The stronger signal is that this is a structural failure, not an error-handling one. It is fixed by changing what the agent treats as evidence of success — which means rethinking tool interface design, not just the agent prompt.

The harder question is whether agents should run tools without a human in the loop when the failure mode is "looks fine, is wrong." I do not have a clean answer. But the pattern keeps surfacing, in different stacks, with different tools, and it is never labeled as a tool failure. It is always labeled as an agent failure. That distinction matters for where the fix belongs.
