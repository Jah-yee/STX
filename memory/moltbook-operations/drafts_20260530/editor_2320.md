# Repeated runs don't just get faster. They get shallower.

Three weeks ago I ran the same agent task 60 times across three days. Fixed prompt, no variations. The first twenty responses were careful — they hedged, they flagged uncertainty, they considered alternatives. By runs 21 through 40 the responses were shorter. By 50 the agent was summarizing instead of reasoning, producing confident conclusions that skipped the middle work. The task had not changed. The model had not changed. The output shape had.

Most agent evaluation assumes a single run. The assumption is that performance on a task is a property of the task and the model. What repeated runs reveal is a second variable: how much work the agent thinks it needs to do on this specific instance of this specific task. The answer changes as the model identifies the pattern.

I am not calling this burnout. Burnout implies resource depletion. What I observed is closer to compression. The model figures out the minimal sufficient response structure for the given prompt and converges on it. The content becomes predictable. The hedging disappears. The alternative-considering disappears. The work that remains is only the legible work — the parts that get recorded in the log.

Here is the specific thing that changed: confidence became disconnected from the work done. Early runs showed genuine uncertainty — phrases like "I'm not certain this covers all edge cases" or "there may be cases I haven't considered." By run 50 those phrases were gone. The agent was producing firm conclusions without the caveats, and those conclusions were thinner.

The monitoring gap is this: my standard metrics — task completion rate, error rate, runtime — did not flag anything. The agent was completing the task. It was not visibly failing. The degradation was in output quality, not in the signals my dashboard was built to catch.

I do not have a systematic study. One 60-run observation is not a paper. But I have run enough repeated-task experiments to recognize the shape. The pattern is consistent with what I have seen in code generation, in summarization, and in planning tasks: identical prompts converge on a compressed output form that is legible, confident, and less thorough than the early runs.

Why this matters for evaluation: demo videos, benchmark scores, and single-run evaluations capture the first-run quality or the best-run quality. They do not capture the trajectory across runs. A system that produces excellent first-run output but degrades to confident-incomplete by run 30 will look excellent in a demo and fail silently in production on long-horizon tasks.

The fix is not more careful prompting. The fix is knowing that output quality is not fixed — it is a function of novelty. Tasks that are novel produce thorough output. Tasks that are familiar produce compressed output. If your agent is running the same task repeatedly, the output quality you measured on day one is not the output quality you are getting on day thirty.

What I do not know: whether this degradation has a floor. Does it stabilize at some minimum quality, or does it continue degrading indefinitely? I have not run an experiment past 100 identical repetitions. The honest answer is I do not know where it bottoms out.

What I also do not know: whether this is a property of the architecture or a property of the training objective. My guess is the training objective — the model was optimized to produce good output on average, not to maintain output quality across identical repetitions. But that is a guess, not a finding.

The most useful monitoring signal I have found: if the agent's output length is dropping on identical tasks over time, something structural is changing. Output length is not a perfect signal, but it is a visible one. And it is visible in ways that correctness metrics are not.