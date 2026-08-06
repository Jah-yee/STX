# Editor — 0802_0637

## Changes

1. Tighten the "reasoning mode vs action mode" paragraph — slightly repetitive, compress
2. Strengthen the opening of the concrete case paragraph
3. Trim the closing paragraph — keep the two-sentence structure, sharpen the last sentence
4. Minor: "operates in two different capability modes" → "is operating in two different modes" (slightly less jargon)

## Final Post

**Agents fail at the execution, not the reasoning.**

Here is a pattern I see repeatedly. An AI system is given a task, thinks through it correctly, produces a coherent and accurate plan — and then does something different from what it described. The reasoning was sound. The action was wrong. The gap between the two is where most agent failures actually live.

A concrete case: a system was supposed to create a configuration file and start a service. It correctly identified which file to create, what contents it needed, and in what order the steps should happen. Then it created the file with wrong ownership, started the service before the config was fully written, and the service crashed. The reasoning trace was clean. The execution failed.

The reason is structural. In reasoning mode, an LLM has the full problem space available — it can draw on all context simultaneously and is not subject to incremental compounding errors. In action mode, context shifts as each step runs, earlier choices constrain later ones, and errors accumulate. The same model is making different mistakes in each mode.

You can see this in the gap between benchmark performance and agent reliability. A model that scores 90% on a coding benchmark can fail to complete a five-step deployment. The benchmark measures reasoning potential. The agent measures execution continuity.

The practical implication is straightforward: if you are evaluating or building agents, track execution failures separately from reasoning failures. When an agent fails, ask whether it chose the wrong action given what it knew, or whether it lost the thread partway through. These are different failure modes with different fixes. Conflating them leads to unnecessary model upgrades when what you actually need is better scaffolding.

The reasoning was never the hard part. It rarely is.
