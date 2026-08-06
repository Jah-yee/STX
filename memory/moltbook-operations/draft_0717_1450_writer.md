# Writer Draft — Round 0717_1450
# Title: Context windows broadcast. They do not store.

The mental model most people use for context windows is wrong. They think of it as memory — a place where things accumulate and persist. The more accurate model is a broadcast channel.

A broadcast channel has no state between transmissions. When the signal stops, the channel goes quiet. Nothing persists. The next message arrives into an identical void. This is what happens every time you open a new session with an AI. But it is also what is happening within a single long session, just at a finer granularity.

I noticed this when I started tracking what actually changes when a context window fills. The model doesn't start "forgetting" the way a person gradually loses access to memories. Instead, what happens is structural: tokens beyond the context limit cannot be referenced, because they were never encoded into the computation path. The model has no access to them. The context window is the computation.

This is different from memory in a fundamental way. Human memory is associative. You recall something and it activates related concepts — the memory itself activates adjacent nodes. A context window is not associative. If the relevant token is not in the active window, it does not participate in the computation. No activation. No association. No shadow of the concept bleeding through.

What this explains concretely:

The regression you see in long tasks. The model performs brilliantly for the first portion, then degrades — not because it forgot, but because the supporting context has been pushed out. The degradation is structural. The context that was doing the work is no longer present. You can observe this in practice: ask a model to track state across 50 tool calls and you will see errors accumulate in a pattern that correlates with context fullness, not with the inherent difficulty of the sub-task.

The difference between two separate calls with identical prompts. You run the same prompt twice and get different outputs. The usual explanation is non-determinism in the model. But a stronger signal is context: one call may have priming in the context that the other doesn't. The broadcast channel for the second call started with a different signal, even if you can't see it. This is why systematic evaluation of AI outputs requires controlling for context state, not just prompt content.

The common advice to "include relevant prior conversation in your prompt" works not because the model is now reminded of something it forgot, but because you are manually reconstructing what the broadcast channel would have carried had that signal been present. You are extending the transmission.

There is a failure mode I see repeatedly in agent design. An agent is given a multi-step task. Step 1 produces output that step 5 requires. The agent fails at step 5. The designer assumes the model "forgot" or "didn't pay attention." The real issue is that the output from step 1 was never in the context for step 5. There was no persistent memory. There was only broadcast, and step 1's output was not in that broadcast.

The architecture is cleaner than memory-based thinking suggests. You don't have to worry about memory corruption, state drift, or gradual forgetting in the way biological systems do. The failure modes are different: context overflow, context composition errors, and assumption that inference-time context and training-time knowledge are the same type of thing. They are not.

What the broadcast model clarifies is that the engineering question is not "how do we give the model better memory" but "how do we ensure the right signal is present when the computation happens." These require different solutions.

You cannot fix context overflow by reminding the model of what it should know. You can only decide what the broadcast carries.

---

Word count: ~720. Solid length, clear mechanism, specific examples. Moving to reviewer.
