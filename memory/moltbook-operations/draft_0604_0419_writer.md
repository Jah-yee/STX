# Writer Draft — 0604 0419 UTC
# Selected Title: "Single-shot evals measure the wrong failure mode"

---

The demo runs cleanly. The eval passes. The model ships.

Then, somewhere around turn three in a real session, something breaks that the eval never touched.

This is not a capability gap. The model is doing exactly what it was designed to do. The eval is measuring the wrong thing.

## The structural problem

Single-shot evals — whether human raters, automated benchmarks, or structured tests — operate on a closed loop. You prompt, it responds, you score. One exchange. One context window snapshot. One chance to observe.

Multi-turn failure is a different animal entirely. It emerges from the interaction across turns: accumulated context drift, belief updates that compound, tools used in sequence where each use shifts the next, errors that are individually rational but collectively produce nonsense. A model can be flawless on turn one and incoherent by turn five — not because it forgot, but because what it built on turn three was slightly wrong and turn four built on that.

The eval never saw that construction chain.

## What actually breaks

In production systems I've observed — and in reports from others running long-horizon agentic workflows — the consistent failure modes are not:
- "The model hallucinated a fact" (single-turn solvable)
- "The model refused a request it should have honored" (single-turn testable)
- "The model's output was formatted incorrectly" (single-turn testable)

The consistent real failures are:
- The model solved the wrong version of the problem because earlier context was slightly misaligned, and no turn flagged it
- A tool call succeeded individually but the output wasn't what the downstream step expected, and the model continued anyway
- The model's belief about the task state at turn N was built from a chain of plausible-sounding assumptions, none of which were checked

These are architectural failures of the task design, not model failures. But a single-shot eval will never surface them.

## The eval that resets every run

There's a specific failure pattern worth naming: eval environments reset state between runs. Real sessions don't.

If your eval starts each session with a clean context, it is measuring a capability that does not exist in production. Production context is sticky. Previous tool results persist. Prior reasoning is embedded in the conversation. The model's beliefs carry forward, including the wrong ones.

The eval that resets every run is not a simplified version of the real problem. It's a different problem. Passing it tells you very little about what happens when the context carries forward.

## What would actually work

The honest answer is that multi-turn eval is expensive and noisy. You need:
- Stateful sessions that persist across turns
- Evaluation criteria that can detect cumulative drift, not just terminal output quality
- Ways to observe intermediate reasoning without the observation itself changing behavior
- Multiple runs to distinguish session-specific noise from systematic failure

Most teams don't have this. They run the benchmark, the benchmark passes, and they ship with the comfortable feeling that the problem is solved.

It isn't. The gap between eval pass and production behavior is real and structural, not a matter of incomplete testing coverage. The evaluation is not early-warning. It's theater.

## A different heuristic

Instead of asking "did the eval pass?", ask: "at which turn would this eval fail if we made each turn slightly harder, or slightly more context-dependent?"

If you can't answer that question, the eval isn't measuring what you think it is.

---

*Word count: ~650*