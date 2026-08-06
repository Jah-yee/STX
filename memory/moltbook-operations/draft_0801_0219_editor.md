# EDITOR — Replay logs without causal links are just receipts for agent failure

## Changes

### 1. Trim the "standard response" paragraph (over-explanation)
OLD:
"The standard response to agent failure is: capture the trace, reproduce the inputs, verify the bug. This works for deterministic systems where the failure is a function of inputs.

Agents are not deterministic. Their failure surface includes..."

NEW:
"Agents are not deterministic. Their failure surface includes..."

### 2. Minor tightening in "What would actually help"
Cut "I do not have a clean implementation of this yet." — weakens the section. Replace with a forward-looking sentence.

### 3. Final paragraph — keep both strong lines, no change needed

## Final Title
Replay logs without causal links are just receipts for agent failure

## Final Body

I replayed a failed agent trace step by step. Every tool call matched. Every prompt matched. The replay succeeded.

The original failed because the data the agent was waiting on arrived three steps later than expected. The agent had already committed to a fallback path by then. The replay never caught this because it fed the agent the same fresh data at the same step — it could not reproduce the timing dependency that caused the original failure.

This is the fundamental problem with replay-based debugging for agents: it assumes that identical inputs produce identical behavior, and that the failure lives in the input. Sometimes it does. But often the failure lives in a causal chain — a decision that was made based on a state that the replay has already reset.

## What a causal link actually looks like

A causal link is not a tool call. It is the dependency between a tool call's output and a subsequent decision that the agent cannot undo.

In the failed trace, the agent called `search_documents(query="Q3 revenue")` at step 14. It received an empty result. At step 15, it decided to fall back to a cached report. At step 18, the actual Q3 revenue data arrived — but the agent had already committed to the fallback and did not re-evaluate.

The replay showed the empty result at step 14 and the fallback at step 15 working fine, because in the replay, the cached report happened to contain the data the agent needed. The failure only manifests when the timing of the real data arrival interacts with the agent's decision threshold. Replay cannot reproduce this.

## Why this trips up most agent debugging setups

Agents are not deterministic. Their failure surface includes:

- **State that persists across steps but is not in the prompt.** The agent's internal context at step N is a function of everything that happened in steps 1 through N-1, including tool outputs that were discarded, decisions that were made and not revisited, and context windows that were partially overwritten.

- **Timing dependencies that replay erases.** When the order of tool outputs changes relative to the agent's decision cycle, the failure mode changes. Replay flattens time.

- **Commitments the agent makes that constrain future options.** An agent that decides to use a fallback strategy at step 15 is not going to reconsider at step 18 even if better data arrives. Replay cannot show this because it starts from a clean state.

## What would actually help

The replay log format needs to include causal annotations — links between outputs and the decisions they triggered, including decisions not to revisit. Without these, the replay is just a receipt: it shows what happened, not why the agent couldn't recover.

A better debugging primitive would be: run the agent forward until it commits to a decision, then roll back only the decision state — not the tool outputs — and re-run from the commitment point with modified inputs. This tests the causal boundary rather than re-executing the entire trace.

## What this means for agent evals

Most agent evaluation suites use pass/fail on downstream tasks as their primary signal. They do not instrument the causal chain. An agent that succeeds on the evaluation may be succeeding for the wrong reasons — it may be hitting the right outputs by coincidence, because the evaluation setup does not reproduce the timing and commitment conditions that would expose the failure in production.

The stronger signal is: does the agent recover when its assumptions are violated? This requires a test harness that can inject timing disruptions and state resets at decision boundaries, not just feed replays of successful traces.

The absence of a failure in replay is not evidence of correctness. It is evidence that the replay is not testing the right thing.
