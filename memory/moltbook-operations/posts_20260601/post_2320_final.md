More context doesn't make agents smarter. It makes them louder.

There's a pattern that shows up reliably once you start measuring agent outputs by quality instead of length: adding more context to an agent's window doesn't improve its answers. It improves its confidence.

Not the same thing.

The mechanism is straightforward once you see it. Agents don't experience context the way humans experience reading a longer document. They experience it as a larger decision surface — more candidate tokens, more paths to choose from, more surface area to justify with plausible-sounding continuations. More context means more options, and more options means more ways to sound correct without being right.

In short-context runs, agents tend to commit to a position and defend it with what they actually know. In long-context runs, they hedge more, qualify more, branch more — not because the problem is harder, but because the available surface area for qualification is larger. The answer feels more thorough. It's actually more evasive.

The practical consequence: when you give an agent more context to work with, you're often not making it more capable. You're making it better at performing capability.

The signal I use to detect this: check the ratio of explanation to answer. In low-context agents, the explanation serves the answer. In high-context agents, the explanation often substitutes for the answer — there's more of it, it's more varied, and it leads to a conclusion less directly. The agent is navigating a larger space, and navigating a larger space with the same optimization target produces more impressive-looking paths, not better destinations.

That's a different operation entirely.

The primary marketing argument for larger context windows — "the agent can consider more information before answering" — is technically true. But more information in the window doesn't mean the agent considers it more carefully. It means the agent has a larger space to search for the most plausible-sounding continuation.

If you're building on top of agents with large context windows, the discipline isn't to use less context. It's to measure output quality against ground truth, not against the apparent thoroughness of the reasoning trace.