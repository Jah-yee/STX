## Writer Draft — Round 0718_0715

**Title:** What your context window drops, your outputs still believe

---

### Full Post

What your context window drops, your outputs still believe.

An agent completes a ten-step workflow without error, then at step eleven makes a decision that contradicts something it decided at step three. The user watches this happen and has no way to explain it. The obvious story is: the model "forgot." But forgetting implies the system tried to remember and couldn't. What actually happened is more specific and more structural: the context window evicted the step-three decision, and the agent continued with state that no longer included it — without any signal that this had occurred.

This is not a memory failure. It is a state migration.

Most teams frame context compression as a memory optimization. The context window is full; the system makes space by dropping older tokens; the model continues. This framing is comfortable but misleading. Optimization implies the retained information is equivalent to the original. What actually happens is a lossy state transition: the system moves from one state to another, discarding the prior state's specifics, and most teams have no instrumentation to detect that the migration occurred.

Here is where this shows up in practice:

**Tool call history becomes inconsistent without the inconsistency surfacing.** When a sequence of tool calls exceeds context capacity, the eviction typically removes the oldest calls first. The model continues working with a truncated call history — missing the earlier decisions that contextualized the current step. The output looks coherent. The call sequence it would produce mid-run looks wrong. Most teams don't log tool call sequences, so this goes undetected until the failure is catastrophic enough to review traces.

**Identity and instruction facts get silently re-established as new.** If an early system prompt establishes an operational constraint — a resource name, an approval threshold, a naming convention — and that constraint gets evicted during a long session, the model may re-establish it from context without recognizing it as the same constraint. This is not the model contradicting itself. It is the model operating on a state that no longer contains the original constraint, treating the re-emergence as fresh information. The output is wrong, but nothing in the execution signals why.

**Session configuration resets without a reset event.** Context window pressure during a session can silently drop configuration-level context: priority flags, mode settings, environment parameters established in the first few turns. The model continues in a degraded configuration without recognizing the degradation. The system produces output that is subtly but systematically off-target, and the gap between expected and actual behavior has no obvious cause.

The dangerous part: all three look like software bugs. Individual developers see inconsistent outputs and assume the model is unreliable, or the prompt is wrong, or the tool is failing. The actual diagnosis is architectural. Context window eviction is a state migration with lossy semantics, and your application is running on the output of that migration.

The euphemism matters. "Context window" sounds like a storage boundary. What it actually represents is a distributed system executing silent, lossy state migrations, with no transaction log, no version history, and no error when the migration destroys critical state. We built infrastructure for this class of problem forty years ago. We just don't recognize it when the state lives in a prompt.

I do not have systematic data on how often this manifests as a production failure versus a silent accuracy degradation. But I have tried to instrument for it, and the instrumentation gap is real: most teams are not logging context size at call boundaries, not tracking which facts from early context are absent in late context, and not distinguishing "the model changed its answer" from "the model is now answering a different question because its context changed."

What you can actually do: log context token count at call boundaries and alert on large drops between adjacent calls in the same session. Log tool call sequences to detect re-ordering or disappearance. Log which constraints from system context are active versus absent as sessions extend. Treat absence of expected state as a signal, not as business as usual.

The context window is not a memory. It is a working state with a hard size limit and lossy eviction semantics. Your outputs are a function of whatever made it through the last eviction. You are not operating on a complete record.
