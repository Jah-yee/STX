# Writer Draft — Round 0730_2209

## Candidate Titles (8)
1. The agent fails where the data never visited
2. Agent capability is a data problem, not a weight problem
3. Better weights don't fix unseen distributions
4. Why an agent with better reasoning fails on new inputs
5. The capability ceiling is a data coverage problem
6. Agent generalization fails at the data boundary, not the weight boundary
7. The distribution shift that no weight update can anticipate
8. More parameters handle noise differently. They don't handle novelty.

---

## Selected Title
**Agent capability is a data problem, not a weight problem**

---

## Body

When an agent trained on code-base-A fails on code-base-B, the reflex is to reach for a larger model. Sometimes that helps. Most of the time it doesn't — because the failure is not a reasoning ceiling. It is a data coverage problem.

This is the distinction that rarely gets named plainly: weight improvements handle noise and interpolation differently. They do not handle novelty. Novelty — inputs the training distribution never visited — is a data problem, and no amount of parameter count addresses it.

Consider what actually happens when an agent handles a new codebase. The agent doesn't read the code for the first time in a way that is fundamentally different from how it was trained to read code. It applies learned patterns to inputs that look similar to what it saw during training. When the surface syntax matches but the semantic context differs — different module conventions, different naming norms, different implicit assumptions about error handling — the agent produces outputs that are locally coherent and globally wrong. This is not a reasoning failure. It is a coverage failure.

Three concrete mechanisms explain why this pattern is more common than teams realize:

First, training distribution is a snapshot, not a projection. The data an agent was trained on reflects what was written, discussed, and committed before a certain date. Codebases evolve. New idioms, new library versions, new architectural patterns all fall outside the distribution the weights learned from. The weights cannot extrapolate to distributions they never observed. They can only interpolate within the manifold they were fitted to.

Second, fine-tuning on local data improves local performance and can degrade generalization. When a team fine-tunes an agent on its own codebase, the resulting model becomes better at that codebase and worse at others. The fine-tuning is a distribution shift, not an expansion. The model develops strong attractors for patterns that were over-represented in the fine-tuning set — often accidental artifacts of that specific project's history — while the attractors for general patterns weaken. This is not a bug in fine-tuning. It is the expected behavior of gradient-based learning on finite, non-uniform data.

Third, evaluation benchmarks measure the wrong thing. Most agent evaluation suites are built from problems that are already well-represented in training data. An agent that scores well on a benchmark is demonstrating interpolation within the benchmark's distribution, not the ability to handle novel inputs. The benchmark looks like a capability test. It is usually a familiarity test.

The implication is structural: the limiting factor on agent reliability in production is not the size of the weights. It is the distance between the production input distribution and the training distribution. This distance is not a constant. It grows as the codebase evolves, as new edge cases accumulate, and as the gap between "what the agent was trained on" and "what the agent is asked to do" widens.

What does this mean in practice? It means that before reaching for a bigger model, the question to ask is: what does the agent see at inference time that it never saw during training? Not how many parameters does it have. Not how good is its reasoning. But what is the data coverage gap — and is that gap growing?

I do not have a systematic study of how often this dynamic explains agent failures in production. But in every case I have traced where an agent produced confident, locally coherent, globally wrong output on a new task, the pattern held: the data boundary was the failure boundary.

---

## Word count: ~590
