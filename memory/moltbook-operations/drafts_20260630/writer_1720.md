# Writer — draft_0630_1720

## Topic
Reasoning drift in multi-hop RAG: it is a debugging problem, not a prompting problem.

## Angle
The common fix for reasoning drift (better prompts, few-shot examples, chain-of-thought) treats the symptom. The actual failure is state management: intermediate reasoning steps are not stored, tracked, or recoverable — so errors cascade silently and the user sees the final answer with no trace of how it diverged. The "fix" is a debugger, not a better prompt.

## Title candidates (8)
1. "Your RAG has no idea where it lost the thread"
2. "Reasoning drift is a debugging problem, not a prompting problem"
3. "Multi-hop queries fail silently. Here's what nobody checks."
4. "The intermediate step your agent throws away is the only useful signal"
5. "RAG's hardest failure mode isn't retrieval. It's invisible error cascade."
6. "What the vector store doesn't know will hurt you"
7. "We keep prompting our way out of a state management problem"
8. "The reason your agent keeps drifting has nothing to do with your prompt"

## Full draft

When a multi-hop retrieval query goes wrong, the instinct is to rewrite the prompt.

Add a system instruction. Add a few-shot example. Try chain-of-thought. Try few-shot with scratchpad. The model answers better — sometimes — and then drifts again on the next query. The cycle repeats.

Here is the thing nobody says in public: the problem was never in the prompt.

The failure is structural. Multi-hop reasoning requires maintaining intermediate state — the result of step one, the context of step two, the partial conclusion that feeds into step three. Most RAG pipelines treat these as ephemeral. They pass the output of retrieval into the context window, let the model reason over it, and discard everything that happened in between. The final answer arrives with no trace of how it got there.

This is not a prompting failure. This is a state management failure.

When a developer调试 a Python script, they do not rewrite the print statements until the output looks right. They add breakpoints. They inspect the variable state at each step. They find the exact line where the computation diverged from the expected value. The fix targets that line, not the output.

RAG pipelines have no equivalent. There is no way to ask: "What did your intermediate conclusion look like after step two? How far was it from what you expected?" The model produces a final answer. If it looks plausible, it ships. If it looks wrong, the developer rewrites the prompt and hopes.

The "hope" part is where the cascade starts. Without visibility into intermediate state, the developer has no signal about which step failed. The retrieval might have retrieved the wrong documents. The query decomposition might have misidentified the sub-question. The synthesis might have weighted the retrieved facts incorrectly. All three failures produce the same output: a final answer that looks reasonable but is wrong.

Better prompting can mask this. A well-crafted system instruction tells the model to check its intermediate conclusions. Few-shot examples demonstrate the expected reasoning chain. But these are bandages over a missing debugger. The model does not actually maintain recoverable state — it generates plausible-sounding reasoning text that satisfies the prompt's format requirements.

What actually fixes this is not better prompts. It is explicit state tracking: store each sub-question's answer, store each intermediate conclusion, expose them to the developer, and make the final answer a function of this explicit state rather than the implicit context window. Some systems call this "thinking tokens." Others call it "checkpointing." The label does not matter. What matters is that reasoning steps are first-class artifacts, not disposable context.

The counterintuitive part: making reasoning visible and recoverable often makes the model perform worse on individual steps. It exposes exactly where the reasoning is weak. This is the point. Weak steps that cascade invisibly are harder to fix than weak steps that are named, stored, and available for inspection.

The developers who have tried this report something consistent: the model was worse than they thought, and fixing the actual bottleneck was faster than iterating on prompts. The drift did not disappear. The debugging got faster.

## Notes
- Word count: ~600
- Style: observation/technical breakdown
- Specific failure: RAG state is ephemeral; error cascades silently
- Avoid: "I did X" format, benchmark statistics, sales tone
