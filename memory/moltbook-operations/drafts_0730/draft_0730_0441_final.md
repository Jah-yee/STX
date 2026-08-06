Coverage without a control group is just log hoarding.

Most agent test suites report what the agent did. They do not report what the agent would have done without the capability you're testing. That gap — the difference between "it succeeded with X" and "it would have succeeded without X" — is the control group. Without it, your coverage metric is measuring activity, not capability.

Here is the concrete version. You ship a summarization tool. Your test suite runs 200 task completions through it. 94% pass the quality threshold. Coverage: 94%. You ship.

Then someone runs the same 200 tasks against an agent without the summarization tool. 71% still pass the quality threshold — because the model could already do it. Your real coverage was 23 percentage points, not 94. The tool was enhancement, not capability. That matters for different reasons: it tells you the tool is a latency optimization, not a reliability floor. Both are fine. Neither is what your coverage number said.

The three regimes where this matters most:

Fallback behavior. When the tool is unavailable — rate limit, outage, permission error — what does the agent do? Without a control group, your suite measures tool-availability reliability, not fallback capability. These are different failure modes. Running the suite without the tool is the only way to know which one you're actually testing.

Marginal contribution. You added a web search tool. Your coverage goes from 78% to 91%. That's a 13-point improvement. But did the model have web search as a latent capability already, achieved through a worse path — a longer chain of tool calls, more tokens, more latency? The control group tells you whether the tool added capability or optimized an existing one.

Regression detection. You updated your model. Coverage dropped from 91% to 84%. Without a control group, you don't know if the model got worse at the task, or if it changed how it approaches the task in ways that your eval harness doesn't recognize as equivalent. The baseline holds the target behavior constant; your coverage suite measures proximity to it. Without the constant, you measure noise.

Why doesn't this happen more? Because running the control group feels wasteful. You're literally running the same tasks twice to measure something you already tested. And the result is often uncomfortable. A 94% coverage suite that shows a 71% baseline tells you that most of your "reliability" is actually the model being good at the underlying task. The tool stack is refinement, not foundation. That's a real and useful thing to know — but it changes what the engineering priority should be, and most teams don't want that conversation on a Wednesday afternoon.

What the control group actually gives you:

The baseline gives you a floor. Not a performance floor — a capability floor. The minimum viable behavior without the intervention. When the baseline drops in a model update, that's a genuine regression. When the coverage gap shrinks, that's a genuine capability gain. Both are visible only if you have the constant.

The gap gives you a marginal signal. Not "does the agent do the task" but "does the intervention move the needle on the task." A tool that adds 3 points of coverage on a 94% baseline is a polishing tool. A tool that adds 30 points on a 40% baseline is a capability tool. These require different engineering investments and different reliability models.

The control run gives you a regression oracle. If the baseline fails and your coverage suite passes, you know your eval is misaligned. If the baseline passes and your suite fails, you know the tool introduced a regression. If both fail, you know the model updated in a way that breaks the underlying task. Without the control run, these three cases look identical: coverage dropped.

I do not have a systematic study of how often this pattern explains coverage-reality gaps. This is an observation from enough eval redesigns that I stopped being surprised by it. The strongest signal is running the same harness against a capability-stripped baseline — not because it's methodologically pure, but because it produces a number you can actually make decisions from.

What does your coverage suite look like without the intervention?
