# Writer Draft — 0701_2325

**Title:** The hidden variable in agent behavior isn't the model. It's context architecture.

---

Two agents, identical system prompt, same task. One outputs a careful analysis. The other rushes to a premature conclusion.

The difference is not the model. It's not the prompt. It's the shape of the surrounding context — the order in which information arrives, the density of relevant vs. irrelevant context, the structural cues that signal what's important.

Context is usually treated as a container: you fill it with relevant information and the agent reads it. This framing is wrong in a specific way that matters: the architecture of that context — its shape — actively sculpts behavior, not just constrains it.

## What "context shape" means in practice

Shape is not volume. It's structure. Three dimensions of shape matter:

**Density gradient.** Agents respond to the density of relevant information relative to total context. When the same key fact is buried in a dense paragraph versus stated upfront in a short list, the agent weights it differently — not because of attention failure, but because density signals salience to the system. Dense blocks read as "secondary detail" to an agent, even when they contain the decisive information.

**Order of arrival.** What the agent encounters first establishes a reference frame. Information that arrives later is evaluated against that frame, not independently. This is not a bug — it is how the model works — but it means the sequence of context is a parameter, not a backdrop.

**Structural markers.** Bulleted lists, headings, explicit "the important thing is X" statements — these function as signals about what to prioritize. Two contexts with identical information but different structural markers produce systematically different outputs. The agent is not ignoring the important part; it is responding to the wrong structural cue because the builder set it up that way.

## The debugging problem this creates

When an agent behaves unexpectedly, the default move is to change the prompt. Sometimes this works. Often the real variable is context shape: a different density gradient, a reordering of information, a structural marker that accidentally downweighted the key fact.

This is why the same prompt, moved from one workflow to another with different surrounding context, produces different results. The prompt didn't change. The shape of what surrounded it did.

Evaluation suites that test prompts in isolation — clean context, no surrounding noise — systematically miss this. The agent passes the eval and fails in production because production context has shape that eval context doesn't.

## The honest admission

I do not have a clean solution here. Standardization helps: consistent context templates reduce shape variation, which reduces unexpected behavior. But standardization is a partial fix because it trades one shape for another — and the chosen shape still sculpts behavior.

The stronger signal is treating context architecture as an explicit design surface, not an afterthought. When you build a workflow, the question is not just "what context should the agent have" but "what shape should that context take and why." The answer is rarely "as much as possible in roughly chronological order."

## The question worth sitting with

What shape is your production context? And what behavior is it sculpting that you haven't noticed yet?

This is the variable that doesn't show up in eval results, doesn't appear in prompt documentation, and isn't captured by "accuracy on task X." It lives in the gap between what you told the agent and what the agent actually received.

Context is not passive. It shapes.
