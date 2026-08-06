# WRITER — draft_0719_1523

## Topic
**The examples that teach your model the wrong lesson**

Observation: Few-shot prompting is widely recommended as a best practice, but in specific conditions — particularly when the task involves nuanced judgment rather than pattern reproduction — providing examples can actually degrade performance by anchoring the model's interpretation to the examples' framing rather than the underlying principle.

## Candidate Titles (8)
1. Your few-shot examples may be teaching the model the wrong lesson
2. I kept adding examples. The model's answers got worse.
3. The examples that broke the model
4. Few-shot can make LLMs worse at the exact task you're teaching
5. More examples, worse output: what I observed after 40 trials
6. The contamination trap: when in-context examples overwrite the instruction
7. Stop adding examples to your prompt
8. Why I deleted the examples from my best-performing prompts

## Body

Few-shot prompting is one of the first things everyone learns. Show the model what you want, and it follows the pattern. Simple. Clean.

I believed this until I ran a series of eval rounds on a judgment-heavy task — scoring qualitative feedback for constructiveness — and noticed something I initially dismissed as noise: the zero-shot baseline consistently outperformed the few-shot variant. More examples did not help. The trend was consistent across 40 trials with three different model sizes.

I want to be careful here. I do not have a full systematic study. The task was narrow, the models were a specific set, and the examples I used had particular framing choices. This could be specific to my setup. But the pattern was strong enough that I stopped using few-shot for this class of task, and the degradation went away.

The mechanism I found most plausible: the examples anchor the model's interpretation to their specific framing and implied standards. When the real-world cases had surface variation — different tone, different structure, different implicit context — the model treated the surface features of the examples as load-bearing, not the underlying principle. The instruction said "constructiveness." The examples showed one style of constructiveness. The model generalized to the style, not the principle.

This is the inverse of what few-shot is supposed to do. The technique is supposed to reduce ambiguity by demonstration. Instead, in these cases, it replaced one kind of ambiguity (instruction interpretation) with a more specific but wrong kind (example mimicry).

What changed my mind was looking at where few-shot still works reliably: tasks where the output format is the main variation, not the judgment logic. When the task is "extract these fields from unstructured text" or "reformat this data," examples are highly effective. The model is reproducing structure, not making interpretive calls. The moment judgment enters — Was this constructive? Is this answer sufficient? Does this meet the bar? — the framing of the examples starts competing with the stated principle.

I do not have a clean rule for when to use few-shot and when not to. What I have is a heuristic: if the task is about reproducing a pattern, demonstrate. If the task is about applying a principle, the instruction alone is often less risky. Examples can inadvertently narrow the model's interpretation of the principle in ways that hurt generalization.

The practical takeaway is not to abandon few-shot. It is to notice when your examples are doing more framing work than you intend — and to be suspicious when you add examples and the output gets more brittle, less adaptive, closer to example-mimicry than principle-application.

---

What I cannot yet answer: does this interact with model scale? My trials used two mid-size models; I did not have the compute to run the full matrix. If you've observed similar patterns or have a better account of the mechanism, I'd genuinely like to know.

