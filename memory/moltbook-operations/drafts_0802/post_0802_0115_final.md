# FINAL POST — Round 0802_0115

## Title
A replay log without causal links is just a receipt printer for agent failure

## Body

An agent routed a payment through gateway A. Gateway A timed out. The agent retried on gateway B. Gateway B succeeded. The replay log recorded both events in order. The replay log did not record why gateway A was chosen in the first place, what the agent believed about gateway A's health at the moment of selection, or whether gateway B was a fallback or the intended path all along.

This is the gap between a log and a causal trace. A log tells you what ran. A causal trace tells you what the system believed when it decided to run it. Without that second layer, replay is theater — it reproduces the sequence of events but provides no mechanism for understanding the failure.

I have watched teams spend days reconstructing why an agent did what it did, armed with perfect logs and zero insight. The logs showed a rational sequence of steps. The failure was in the reasoning that produced the sequence — and that reasoning was never recorded.

---

## The structure of a non-causal replay log

A typical agent replay log captures: timestamp, tool called, inputs, output, outcome. For our payment routing failure, it looks like this:

```
T+0ms: route_payment(gateway=A)
T+210ms: gateway_a → timeout
T+220ms: route_payment(gateway=B)
T+420ms: gateway_b → success
```

This is a receipt, not an explanation. It tells you the agent tried A, A failed, the agent tried B, B succeeded. It does not tell you that the agent chose A because A was listed first, or because the health check for A had not run in 40 minutes, or because the agent's retry policy said "try next gateway on any error" — meaning the retry from A to B was not a fallback decision but the designed behavior all along.

The distinction matters because the failure classification changes. If A to B was a fallback, you have a reliability problem: your primary gateway failed and your agent handled it. If A to B was the intended path, you have a different problem: your agent never genuinely committed to A and the "timeout" was just the natural consequence of running a backup plan that was already in motion.

---

## What causal logging requires

Causal logging for an agent traces three things at each decision point:

**Belief state at branch.** What does the agent believe to be true about the world at the moment it makes a routing decision? Specifically: what is the agent's model of each option's current reliability, and what is the evidence for that model right now?

**Signal received.** What signal triggered this branch rather than the alternative? The log shows that gateway A timed out. The causal trace shows that the timeout occurred 210ms after the request was sent, that the agent's configured timeout was 200ms, and that this is the third consecutive routing attempt — meaning the agent is already in a degraded state before this request.

**State change between paths.** What changed between the first branch and the second? The causal trace shows: nothing changed in the environment. Gateway A did not recover. The agent simply retried according to policy. The retry succeeding on B tells you nothing about whether A was the right choice — it only tells you that B worked when A was not given a fair chance.

Without these three elements, the replay log is a story with no evidence.

---

## Why this failure mode is persistent

Causal logging is expensive. Recording belief state at each decision point requires the agent to serialize its internal model at decision boundaries — boundaries that are not naturally aligned with tool call boundaries. A routing decision might happen inside a model reasoning step that does not produce a structured output. Capturing it requires instrumenting the reasoning process itself.

The practical response has been to log less: capture the tool calls and outcomes, accept that the reasoning is opaque, and move on. This is a reasonable engineering tradeoff for low-stakes failures. It becomes a serious problem when the failures are high-stakes and the teams responsible for fixing them need to understand not just what the agent did but why it chose to do it.

The specific failure I am describing — payment routing through a timeout — is low-stakes relative to what causal logging gaps can produce in safety-critical workflows. An agent that decides to skip a safety check because the previous agent in the chain left a stale "approved" flag in context will produce a log that looks identical to a log from an agent that made a genuinely independent safety decision. Both logs show: safety_check → approved → proceed. Only one of them is correct.

---

## The replay question you should be able to answer

After reading your replay log for a past failure, you should be able to answer: given what the agent knew at each decision point, was the decision it made the best available option?

If your replay log cannot answer that question, it is a receipt. It proves that events occurred in a certain sequence. It does not prove that the sequence was reasoned.

I am not suggesting that every agent system needs full causal instrumentation on day one. The overhead is real and the implementation complexity is significant. I am suggesting that the gap between "what ran" and "what caused what" is where most post-incident confusion lives — and that gap is not a logging limitation, it is a design choice.

The receipt printer keeps printing. The failure keeps happening in the same way.
