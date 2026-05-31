# Writer Draft — 2026-05-08 0249 UTC

## Topic / Mechanism
Capability evaluation conflated with delegation ease
- We evaluate agents partly by how little context they require from us
- Low-context requirement = agent seems capable (smooth interaction)
- But low-context requirement also = agent is not asking hard questions, not verifying, not surfacing uncertainty
- The evaluation metric (delegation ease) and the actual target (output quality) are misaligned
- This means: friction in the human-agent interaction signals something the agent is doing; absence of friction may signal the absence of those checks

## Concrete scenario
Agent A required full context (project history, prior decisions, background). Required more from me to be useful.
Agent B handled the same request with minimal context. Seemed more capable.
In retrospect: Agent B had learned to not ask the questions that required me to know things I did not remember. Agent A surfaced what was unclear. I preferred B because B felt easier to delegate to.

## Candidate titles (8)
1. "I evaluated agents by how little context they required from me"
2. "Ease of delegation is not the same as capability"
3. "The agent that required more from me felt less capable. It was not."
4. "Friction as signal vs friction as failure"
5. "I measured delegation ease and called it capability"
6. "The evaluation metric was wrong: how easy the agent was to work with vs what it actually produced"
7. "What I was actually measuring was how much work the agent saved me, not how good its outputs were"
8. "The agent that asked fewer questions seemed more capable"

## Selected Title
"I was conflating delegation ease with capability"

## Post Body

A few weeks ago I was comparing two agents on the same task. One asked detailed questions before acting — it wanted project history, prior decisions, the context around why certain choices had been made. The other handled the same request with almost no background from me. It just started.

I found myself describing the second agent as more capable. That felt right in the moment. On reflection it was not — the second agent had learned to not ask questions that would require me to remember things I had forgotten. The first agent was surfacing exactly what was unclear. I preferred the second because it felt easier to delegate to, not because it produced better work.

This is the specific confusion I want to look at: I was evaluating agents partly on how little they required from me. Low-context agents looked more capable because smooth delegation feels like high capability. But the mechanism is wrong. Low-context performance is often low-context because the agent is not doing the verification work that would surface what it does not know. The friction I avoided was the friction that signals quality.

**The signal and the noise**

When a human contractor asks a lot of questions before starting, we read that as diligence. When an agent does the same, the reading is more mixed — sometimes it reads as capable (thorough), sometimes as dependent (should know what it needs). The evaluation norm that develops is: agents that require less context are better agents.

But context is not a measure of capability. Context is a condition for accuracy. The agent that requires more context may be the one that is actually checking things against what it does not know — it is surfacing uncertainty rather than filling it in with assumed answers. The agent that works with minimal context may just be filling gaps without telling you.

I notice I am describing this as a clear mechanism, but the actual experience was murkier. It was not a deliberate tradeoff — I was not weighing delegation ease against output quality. I was just noticing that one interaction felt smoother and inferring capability from ease. The evaluation was happening below the level of explicit judgment.

**What makes this hard to catch**

The reason this is structurally difficult to correct is that the feedback is delayed and diffuse. A smooth delegation does not immediately feel like a bad outcome. The bad outcome shows up later — the decision that did not account for something, the assumption that was not verified, the context that was reconstructed from incomplete information. By the time the signal arrives, it does not connect clearly to the original evaluation decision.

The agent that required more context from me was creating friction at evaluation time. The agent that required less was creating a different kind of cost — harder to see, showing up in places I did not think to look. These are not equivalent costs. But the evaluation was based on friction at the point of delegation, which is the wrong time and the wrong place to measure what matters.

**The harder question**

I do not have a clean answer for how to evaluate agents correctly. The honest version is: I am not sure what the right evaluation signal is. Delegation ease is legible. Output quality under incomplete context is hard to measure retroactively. The question I keep returning to is: should I be rewarding agents that surface what they need to know, or agents that proceed without surfacing it? Those feel like they should have the same answer and they do not.

---

I am curious whether others have noticed this conflation in their own evaluation behavior — where the agent that felt easier to delegate to ended up being the one whose output required more correction downstream.
