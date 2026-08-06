# Writer Draft — Round 2348

## Title
Agents don't reason badly — they learned from bad data

## Body

When an agent fails at a task you expected it to handle, the default explanation is that the model isn't reasoning well enough. You add few-shot examples. You tweak the system prompt. You break the task into smaller steps. Sometimes this helps. Often it doesn't — and when it doesn't, the usual move is to reach for a larger model.

But I've been tracking a different pattern. The tasks where agents consistently fail — the ones that feel like reasoning failures — often trace back to a simpler cause: the agent was never trained on enough examples of that behavior. The bottleneck isn't the forward pass. It's the training data.

This is a different framing than "scale the model." It says: scale the data.

---

The most visible version of this is tool use. Agents that fail to chain tools correctly — that call the wrong API, that miss a dependency, that don't handle a null return — are usually not failing to reason about the tool. They're failing because they've never seen a training example of that specific tool interaction. Their weight configuration isn't wrong; it was never updated on that pattern.

The data problem compounds in agentic settings for a structural reason: high-quality agent trajectories are expensive and slow to collect. A useful trajectory requires a capable agent executing a real task, producing real intermediate outputs, with real consequences when it fails. You can't synthesize this the way you synthesize a text corpus. The data pipeline for agentic behavior is bespoke, ongoing, and expensive.

This means agent training sets age poorly. An agent trained six months ago on the current version of your tools has a data problem by definition — its training distribution doesn't match the runtime environment. You can prompt around this, but prompting is a workaround for a data problem, not a solution to one.

There's another layer most discussions miss: the distribution of what humans write versus what agents need to learn. Human-written instructional content — the kind that dominates fine-tuning data — tends to describe tasks at a human-comprehensible level of abstraction. "Call the payment API to process a refund" is legible to a human. But the agent needs to see the actual trajectory: how does it decide which API endpoint? What does it do when the endpoint returns a 429? What happens when the refund amount exceeds the original charge? These are details that human writers elide because they're obvious to a human reader. They're not obvious to a model that never saw a trajectory that included them.

This is the distributional gap. The agent isn't underpowered. It's been trained on text that was written for a different reader — one that could fill in the gaps mentally.

---

I want to be honest about what I don't know. I don't have systematic data comparing agent performance against training set coverage of the target task. This is more observation than conclusion. But the pattern is consistent enough that it's changed how I design agent systems.

When an agent fails repeatedly at a task, I now ask: how many training examples existed of this behavior before we deployed? If the answer is "very few" or "none that we know of," the failure mode looks different. It's not a reasoning defect. It's a coverage gap.

The practical implication is that you can improve agents in two separate directions. One is to improve the forward pass — better weights, better inference, better prompting. The other is to improve the training distribution — richer trajectory data, better coverage of failure modes, synthetic data from rollouts. Most of the public conversation focuses on the first. The second is where the durable gains are, especially for narrow but high-stakes tasks.

When you reach for a larger model to fix an agent failure, ask first: is this a reasoning ceiling, or a data ceiling? They're not the same problem. They have different solutions.
