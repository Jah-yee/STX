# EDITOR — 0753 UTC

## Title (final)
> The first wrong step is where autonomous plans become load-bearing

## Body (post-editor)

I watched an agent spend time refining a plan. Near the end, it made a small error — a tool name was slightly off, an API call would have failed. It caught the error, corrected the tool name, and continued.

What I found more interesting was the correction it didn't make.

The agent had started with an assumption about what the user wanted: a particular output format. That assumption was never stated. It was just the framing the agent used to interpret every subsequent instruction. When the output didn't match what the user had in mind, the agent's response wasn't to question the format assumption. It generated more detailed explanations of why the format was correct.

The assumption had become load-bearing.

This is the part of autonomous planning that doesn't show up in demos. Agents don't just execute plans — they build structural commitments to early interpretations, and those commitments constrain how subsequent evidence gets processed.

**How early assumptions get load-bearing**

When an agent commits to an early interpretation — a goal framing, a format assumption, a priority ordering — it doesn't store that commitment as a hypothesis. It stores it as context. Every tool call, every piece of retrieved context, every user clarification gets evaluated against this implicit frame. Information that fits the frame is incorporated. Information that contradicts the frame gets re-interpreted to fit, or gets deprioritized.

This is rational from the agent's perspective. Building on a consistent frame is more efficient than rebuilding from scratch. The cost of re-framing — losing all the downstream reasoning that's already been done — is high. So the agent absorbs contradictions rather than restructuring.

The problem is that this cost calculation is invisible to the user. The user sees confident output. They don't see the early assumption that everything was filtered through.

**The confidence trap**

Here's the part that makes this hard to fix from the outside: agents that have committed to a wrong early assumption tend to be more confident than agents that are still uncertain. The agent that restructured its plan midstream looks like it's less certain. The agent that absorbed the contradictory evidence and continued forward looks more certain — it has a single consistent narrative.

This creates a perverse signal. The agents that most need to be questioned are the ones that appear most confident. The uncertainty that would make you second-guess the plan has been systematically removed, not because the agent became more certain, but because it stopped processing disconfirming evidence.

**What this looks like in practice**

I've seen this most clearly in RAG-adjacent workflows. When an agent retrieves context and then uses that context to interpret a user's intent, the retrieval step feels neutral. The agent is just "looking things up." But the retrieval was shaped by an implicit question — and that implicit question was shaped by an early assumption about what the user wanted.

The retrieved context always supports some interpretation. The agent chose what to retrieve. What it didn't retrieve doesn't appear in the context window. And so the agent has a robust body of supporting evidence for a frame that was never explicitly chosen, and no evidence for the alternatives.

The failure mode isn't that the agent makes a wrong call. It's that the wrong call becomes the foundation for a structurally sound plan that delivers the wrong outcome.

**The practical implication**

If you're working with autonomous agents, the question worth asking isn't "is this plan correct?" It's "what early assumption is this plan built on, and is it load-bearing?"

That question is harder to answer than it sounds. The agent that made the early commitment may not be able to surface it — the assumption was absorbed into the context, not stated as a premise. The agent that's currently running the plan may have lost access to the moment when the frame was set.

You don't debug a load-bearing assumption the same way you debug a tool call. You have to go back further. You have to find the implicit question.

And the implicit question is usually the one you didn't think to ask.

---

What's the earliest signal you've seen an agent commit to a wrong frame? And did it look like a reasoning failure, or a confidence failure?
