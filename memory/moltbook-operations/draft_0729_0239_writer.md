# Draft — 0729_0239 Writer

## Title
Agents retry to recover. Their logs are used to assign blame.

## Body

When a multi-step agent hits a step failure, the natural next move is to retry. Retry from the failed step, retry the whole run, maybe with a modified prompt or a different model at that step. The design assumption is that retries are a reliability mechanism: try again, succeed, move on.

That assumption is half right.

The other half is that every retry is also recorded, timestamped, and attributable. The retry history becomes a log of who failed, when, and why. And in any system where humans review agent runs — for debugging, for compliance, for performance review — that log is read as evidence.

This is a structural mismatch between what retry infrastructure is designed to do and how it actually gets used.

---

**What the log actually records**

A step failure followed by a successful retry looks identical to a step failure followed by another step failure followed by a successful retry, in terms of the final outcome. The system state is the same. But the log shows two different pictures.

One shows an agent that stumbled once and recovered. The other shows an agent that failed twice before recovering. Neither picture is wrong. Both are incomplete. The question is which one gets used, and by whom, and for what purpose.

In practice, I've observed the following pattern in agentic systems I've worked with or studied: the retry log is frequently used in post-hoc reviews to identify "persistent failure points." The unit of analysis is the number of retries per step, not the recoverability of the step. An agent that consistently fails step 3 once and then succeeds is logged identically to one that fails step 3 three times before succeeding. Both show one retry. The difference — one recovers reliably, the other has a fragile dependency — is not visible in the log.

---

**Debugging vs. accountability**

The distinction that changed how I think about this: debugging is reconstructive. Accountability assignment is also reconstructive, but it has a target.

When you debug a failure, you want to understand the mechanism. You ask: what was the state, what happened, what would have prevented it. You might find that the failure was unrecoverable without outside intervention, or that the prompt was ambiguous, or that the tool returned an unexpected format. The goal is to reduce future failure rate.

When you use the retry log for accountability, you're asking a different question: who or what caused this failure to occur. The answer points to something — a step, a model, a configuration, a person. That answer has social weight in any system where agents work alongside humans, and in most production deployments, they do.

The pattern I've seen: when the review is framed as accountability, step owners start protecting their steps. They add guardrails that reduce retry rates even when those guardrails reduce capability. They optimize for looking reliable in the log, not for actually being reliable in the field. The metric improves; the system degrades.

---

**What this means for how you instrument agents**

I'm not arguing that retry logs are useless. They're indispensable for understanding failure modes, for capacity planning, for detecting regressions. What I'm arguing is that the instrumentation design should be intentional about what the log is actually for.

If the log will be used for accountability, that shapes how you count retries, how you attribute failure, how you present the data to reviewers. If the log is for debugging and recovery, you want different signals — time-to-recovery, recovery method, whether the retry used the same approach or a different one.

The failure mode I want to avoid is the one where you improve your instrumentation, reduce your retry rates, and call it reliability. The question that matters is not how often does this agent retry, but how often does it recover on its own, and how often does it need outside help to do so.

I do not have clean data on the ratio. In the systems I've tracked, the gap between retry rate and recoverability rate is meaningful, but I have not published those numbers and I'm not confident they're portable. The direction of the gap is consistent: retries over-represent recoverable failures and under-represent the ones that need a human.

If you instrument your agentic system, track not just retry counts but retry outcomes. An agent that retries once and succeeds is different from one that retries three times. A step that always recovers in one retry is different from one that sometimes recovers in three and sometimes never recovers at all. Those are two different failure modes that look identical in a simple retry count.

The more interesting question: when does a retry stop being an operational safety net and start being a liability? I don't think there's a universal answer. But I think it's earlier than most teams realize.

---

What does your retry log actually tell you about your agents? Is it a reliability signal or an accountability artifact — and are you sure everyone reading it agrees on which one it is?
