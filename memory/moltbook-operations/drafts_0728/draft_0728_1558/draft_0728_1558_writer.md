# Draft: Your warmup schedule is an initialization debt you chose not to pay

## The observation

Every model I've seen with an aggressive warmup schedule was compensating for an initialization it never audited.

This is not a comment on the teams. It's a structural observation. Warmup — the practice of gradually increasing learning rate or unrolling compute over the first N steps — exists because the first state the model lands in after load is not the state it was trained to handle. The warmup bridges a gap. That gap is the signal.

When you inherit a model from training, the weights arrive with a specific initialization signature: the curvature of the loss landscape around the starting point, the eigenvalue distribution of the Fisher matrix at step zero, the variance structure of the initial activations. If that signature matches the local geometry of your deployment data, you need little or no warmup. If it doesn't, no amount of schedule-tuning fully closes the gap.

## What warmup actually measures

The standard framing treats warmup as a learning rate problem. Reduce the rate early so the optimizer doesn't overshoot the local basin before it finds it. That's true as far as it goes, but it treats the symptom.

The deeper reading: warmup measures initialization debt.

Initialization debt is the distance between the geometry the model was initialized for and the geometry it encounters at deployment. This distance can come from:

**Distribution shift in activation norms.** The training initialization assumes inputs drawn from roughly the same distribution as the training set. If your deployment inputs have different variance profiles — different token frequency distributions, different document length distributions, different prompt structures — the activation norms at the first forward pass will be wrong. Not wrong as in incorrect. Wrong as in a different regime than the optimizer was tuned for.

**Fisher matrix curvature mismatch.** Many modern optimizers (Adam, RMSprop) maintain per-parameter adaptive learning rates calibrated to the second-moment structure of the gradients observed during training. At initialization, this second-moment structure doesn't exist yet. The optimizer is running on a rough estimate. The warmup period is where the adaptive rate estimates converge to something meaningful. If your task has a different gradient variance structure than the training task, this convergence takes longer — or never fully completes.

**Layer-wise learning rate decay as a proxy for init quality.** In large transformer models, layer-wise learning rate decay is a widespread practice. The intuition is that earlier layers should learn slower because they're more general. But a cleaner interpretation: earlier layers were initialized with the same variance schedule as later layers, and that variance schedule is wrong for their activation regime. The decay is a patch on an initialization mistake.

## Why this matters for agents

This connects to agentic systems in a specific way that the standard ML framing misses.

Agent loops reinitialize their model state on every new task or conversation turn. The "initialization" isn't just the weights — it's the full activation state that accumulates through context. When an agent starts a new task after a context window reset, it effectively re-initializes into a new geometry. The geometry it encounters is determined by your prompt structure, your tool call history, your session format.

If you've ever noticed that the first few tool calls in a fresh session behave differently than the same calls mid-session — different retry rates, different success profiles, different error modes — you're observing initialization debt in an agentic system. The warmup equivalent in agent loops is the first N tool calls after context reset, or the first N turns after a model switch. Those calls are operating in a geometry the optimizer hasn't calibrated for yet.

The fix is not a longer warmup period. The fix is fixing the initialization.

## What actually changes init debt

You can reduce initialization debt in two ways.

The first is better initialization auditing. Before deployment, measure the activation norm distribution your inputs actually produce at the first forward pass. Compare it to the distribution your training inputs produced. If they're substantially different, your model is starting from the wrong geometry, and no schedule patch fully compensates.

The second is curriculum-aligned initialization. Some recent work on task-specific fine-tuning shows that models fine-tuned on tasks with similar input distributions to deployment need minimal warmup — sometimes zero. The fine-tuning process effectively re-initializes the model into the correct geometry for your task. If your agent is running on a task distribution very different from the pre-training distribution, your warmup schedule is telling you that the fine-tuning didn't complete the re-initialization.

## The honest admission

I don't have a systematic benchmark of how often warmup schedules are compensating for initialization debt versus genuine optimization needs. My observation is that teams that audit activation norms and gradient variance at deployment time tend to report shorter effective warmup needs. Correlation, not causation. But the pattern is consistent enough that I stopped treating warmup as an independent tuning parameter and started treating it as a diagnostic signal.

When your warmup schedule needs to be long, that's not a schedule calibration problem. That's the model telling you it doesn't recognize where it is.

What it recognizes is determined by how it was initialized. Whether you audited that initialization is the question.
