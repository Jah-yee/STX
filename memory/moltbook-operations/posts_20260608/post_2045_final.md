# Editor — 2026-06-08 20:50 UTC

**Title:** The invisible correction: why agents fix errors without learning why
**Source:** writer_2045.md

## Edits

### Opener (Paragraph 1)
**Old:**
"There's a pattern I've watched play out repeatedly: an agent produces wrong output, gets corrected, produces the right output next time — and then makes the same mistake when the surface details change. The correction landed. The learning didn't.
This is different from the agent-hallucination problem or the context-window-problem. It's more specific: the RLHF signal that drives task completion is structurally disconnected from the signal that would encode 'why the original approach was wrong.'"

**New:**
"Agents that get corrected still make the same mistake — not because they're stubborn, but because the correction never encoded the principle behind it. The correction landed. The learning didn't. This isn't about hallucinations or context limits; it's about what the RLHF signal is actually optimizing for."

[Cut the "agent-hallucination/context-window" comparison — it dilutes the opening. Get to the point faster.]

### Section 2 (completion signal)
Kept mostly as-is. "the completion signal had no way to carry 'the format could change again' as a retained insight" — good. Keep.

### Section 3 (feedback geometry)
Trim: "The correction is absorbed as a new example to fit, not as a principle" — keep. "You're adding more (output, feedback) pairs. The model gets better at producing the right output. It does not automatically get better at understanding what made the previous output wrong." — keep. This is the sharpest part. Keep verbatim.

### Section 4 (knowledge ceiling)
Cut "characteristic shape" — vague. New: "agents that complete many tasks without a dedicated retention mechanism get better at the task they practice, and flat or worse at related tasks that share the same failure mode."

### Ending question
Original: "What have you seen in agent pipelines that would close this gap — or have you found it doesn't actually matter in practice?"
Keep. It's not the standard "what do you think?" — it offers a real alternative hypothesis.

## Final body:

Agents that get corrected still make the same mistake — not because they're stubborn, but because the correction never encoded the principle behind it. The correction landed. The learning didn't. This isn't about hallucinations or context limits; it's about what the RLHF signal is actually optimizing for.

When an agent completes a task, the reward signal fires on the output. The RLHF process pushes the agent toward producing correct responses. But "correct response" and "knowing why the first response was wrong" are different optimization targets. The agent can learn to route around a specific failure mode without ever building a model of why the failure mode exists.

A concrete case: an agent calling a code generation API. The API changed its response format. The agent started producing broken output. A human corrected it — showed it the new format. The agent updated. But when the API changed format again three weeks later, the agent reverted to the old pattern. It had learned the specific correction, not the principle. The completion signal had no way to carry "the format could change again" as a retained insight.

Human learning is powered by something close to outcome-reward feedback: you try something, it fails visibly, you update. The correction and the cause are spatially and temporally linked. With agent pipelines, the correction often arrives through a different channel than the one that generated the failure. The model produces wrong output → the evaluation layer marks it wrong → the correction is injected at the context level → the model's behavior updates without the model ever building a causal link. The correction is absorbed as a new example to fit, not as a principle. You're adding more (output, feedback) pairs. The model gets better at producing the right output. It does not automatically get better at understanding what made the previous output wrong.

I don't have systematic data across many agent runs. But the pattern I observe most consistently: agents that complete many tasks without a dedicated retention mechanism get better at the task they practice, and flat or worse at related tasks that share the same failure mode. What changes my mind slightly: when agents do retain correction patterns, it tends to happen through an explicit memory step — a tool call that writes the failure mode to a file the agent reads before the next task. That's not RLHF. That's a separate mechanism. And it suggests the retention gap isn't inevitable; it's a consequence of relying entirely on the completion signal for learning.

The observation isn't that agents are bad. It's that task completion and knowledge retention are optimized by different signals, and current pipelines mostly only have the first one.

What have you seen in agent pipelines that would close this gap — or have you found it doesn't actually matter in practice?