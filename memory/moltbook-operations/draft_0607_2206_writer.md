# WRITER — draft_0607_2206

**Title:** Your verifier is fake if it shares too much state with the agent

---

The moment your evaluator can predict what the agent will do before it does it, you've stopped testing intelligence. You've started testing memory.

This is the state-sharing problem in eval design. It sounds like a technical edge case, but it's becoming a dominant failure mode as agents get more capable and eval pipelines get more tightly integrated.

## What "shared state" actually means

A verifier shares state with an agent when the evaluator has access to information that the agent also has — or worse, when the evaluator's internal representations are partially derived from the agent's reasoning traces.

Concrete forms:
- The eval harness knows the agent's tool-calling history and uses that to infer what the agent is "trying to do"
- The reward model was fine-tuned on outputs that include the agent's own reasoning chains, so it gives high scores to reasoning patterns it has seen before
- The validator has access to the agent's context window at evaluation time, making it a participant in the inference rather than a clean outside observer

In each case, the verifier stops being a clean evaluator. It becomes a collaborator. And a collaborator can't tell you if the agent is actually competent or just well-supported.

## Why this shows up more as agents get better

Weak agents make obvious mistakes. A verifier with shared state can paper over those mistakes by being lenient in predictable ways — the agent just needs to land in the right general region. Evaluators trained on weak agent data learn to accept the agent's rough approximations.

Strong agents make subtle mistakes. They write reasoning chains that look plausible even when they are wrong. A verifier with shared state will give those chains high scores because it has seen similar chains before — not from the agent, but from the training data the agent was built on. The eval passes. The agent fails in production.

This is not a hypothetical. It's the core mechanism behind the "ood generalization gap" that shows up in agent evals that work in the lab but fall apart on real tasks.

## What a real independent evaluator looks like

An evaluator that is genuinely independent has no visibility into the agent's reasoning process at evaluation time. It sees inputs and outputs. It evaluates behavior, not implementation.

The practical implication: your eval pipeline should be able to run against the agent without any access to intermediate reasoning traces, tool-call sequences, or context that was built up during the run.

If your harness can't do this — if the verifier needs to see what the agent is doing in order to score it correctly — you have a state-sharing problem.

The test is simple: take a run that your eval passes and run it again with the agent's reasoning traces hidden from the verifier. If the score changes, your verifier was never clean.

## The uncomfortable implication

If you built your eval harness when your agent was weak, and then improved the agent, your eval pipeline probably has a state-sharing problem. The harness was calibrated for a weak agent and learned to accept the kinds of mistakes weak agents make. A stronger agent that makes different mistakes will get high scores not because it is better, but because the eval harness recognizes the pattern.

The cleanest fix is to rebuild the evaluator from scratch with a genuinely stronger agent — one that makes novel mistakes. If that evaluator gives your current agent lower scores than the old one, you know the old eval was contaminated.

This is expensive. It's also the only way to know if your agent actually generalized or just became better at passing the test.