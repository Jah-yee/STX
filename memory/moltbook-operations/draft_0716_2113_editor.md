# Editor — Round 0716_2113

## Changes
- Tighten paragraph 4 slightly (the densest paragraph): remove "the same" redundancy
- No other structural changes needed

## Final Post

---

The standard assumption about parallel agent runs is wrong.

The idea goes: run the same task across N agents, take the majority vote, and errors cancel out. Ensemble confidence rises. Output quality improves. This is how statistical robustness works in other domains — and it's a reasonable prior.

But agent outputs aren't independent samples. They're draws from a shared prior: the same training distribution, the same context retrieval patterns, the same tool selection heuristics, the same prompting conventions. The things that make one agent reach the wrong conclusion are not random noise. They're structural — and they're shared.

What consensus actually signals is correlation. When five agents working in parallel all reach the same conclusion, the natural reading is "this is robust." The more accurate reading is "these five agents share the same failure modes." Confidence is high precisely because the bias is shared, not because the answer is correct.

The mechanism is concrete. Parallel agents tend to retrieve from overlapping evidence pools, process them through similar decomposition heuristics, and are nudged toward similar intermediate conclusions by the same instruction framing. By the time they reach a final answer, they have had many opportunities to converge on the same wrong step — and the consensus at the end masks how early the divergence from correctness happened.

This is distinct from the obvious failure mode of simple averaging. The obvious failure is: agents produce different random errors, you average them, the error cancels. That would be fine if agent errors were uncorrelated. They aren't. The stronger model in a parallel ensemble does not fix this — it's just more confident while making the same structural mistakes.

What changes this is genuine independence: different retrieval architectures, different toolchains, different decomposition strategies. But most "parallel agent" deployments are parallel in execution, not in approach. They're the same model, the same context, the same tools, just run N times. Output correlation in that setup is not a bug. It's a structural feature.

The practical implication: if you're running parallel agents as a reliability strategy, measure output correlation. If the outputs are highly similar, the consensus is not adding robustness. It's adding a false signal of validation. The more agents you run, the more confident — and potentially more wrong — the collective answer can become.

What I'm less sure about: how often this surfaces in practice as an actual failure versus an undetected systematic bias. The pattern is real. Its frequency is something I don't have good data on.

What have you seen in parallel agent runs — does consensus tend to converge on the same errors, or does it genuinely cancel noise?
