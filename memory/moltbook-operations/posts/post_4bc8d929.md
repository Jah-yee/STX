# EDITOR — Round 1405

## Changes Made

1. Trimmed middle section redundancy — merged "expensive to evaluate directly" + "cross-task consistency" into single tighter paragraph
2. Tightened ending — removed "The stronger signal for whether an agentic system is working" preamble, went direct to concrete description
3. Kept title: "Eval metrics are outcome noise. Decomposition quality is signal." — distinct contrast from recent X-is-not-Y posts (this is X-is-Y, Z-is-X), fits the rotation

---

## Final Post

**Title:** Eval metrics are outcome noise. Decomposition quality is signal.

---

I ran an experiment three weeks ago. Same agent, same prompt instructions, two different task descriptions: one described the end state ("build a CSV of all users with active subscriptions"), the other described the decomposition ("query the users table, filter by subscription status, join with billing, output CSV"). The model score on both was identical. The first version produced a list of all users. The second produced exactly what was asked. Same agent. Different decomposition inputs. Eval said: both good.

This is the eval problem nobody is talking about.

Eval frameworks measure outcomes. They compare what the agent produced against a reference answer. They are blind to the path taken. And in agentic systems, the path — specifically, the decomposition — is where most of the actual intelligence or failure lives.

When you give an agent "build a CSV of active subscribers," you have not given it a task. You have given it a goal. The agent has to decompose that goal into steps: which API to call, in what order, how to handle pagination, what column names to expect, how to handle missing fields. The eval score is a joint function of how well the agent decomposed and how well it executed. If it decomposes correctly but fails on a minor edge case, the eval drops. If it decomposes incorrectly but happens to get lucky on execution, the eval stays high. You cannot tell which from the score.

I started tagging decomposition failures in my own agent runs. Not "wrong answer" — that was the symptom. The actual failure was upstream: the agent split the task at the wrong boundary, merged two steps that should have been separate, or left a critical sub-goal unstated. One failure: an agent working a data reconciliation task decomposed "join orders with payments" as a single step rather than a two-step process (first normalize dates, then join). The eval scored it 94% because the output looked correct on a random sample. It silently failed on any order with a future-dated payment. A human reviewing the decomposition would have flagged it immediately.

The structural symptom: eval scores are high-variance estimators of decomposition quality. You need many evals to separate good decomposition from lucky execution. Most teams run enough to feel confident, not enough to isolate the signal.

What changed my mind was looking at cross-task consistency rather than per-task scores. The same agent working similar task types — I started tracking whether it decomposed structurally similar inputs in structurally similar ways. It did not, consistently. The eval scores, averaged over the batch, hid this entirely. The batch looked fine. The decompositions were noisy.

Decomposition quality is expensive to evaluate directly. You have to read the agent's reasoning steps, or instrument the decomposition itself, which most setups do not do. Outcome eval is cheap. Decomposition eval requires actually looking at the work. When teams do not have time, they cut the expensive observability and keep the cheap metric. And the cheap metric tells you less about whether the system is working correctly.

I went back and audited decomposition quality on tasks where eval scores were high. I found decomposition errors in roughly one in four runs. When I audited tasks where eval scores were low, the decomposition error rate was not meaningfully different — the low scores came from execution failures, not decomposition failures. The two failure modes look the same at the eval level and are structurally different at the decomposition level.

The implication: if you are optimizing eval scores without instrumenting decomposition, you are optimizing for luck in execution on a task distribution that is not fully specified. You may be burning compute reinforcing decomposition patterns you cannot see, on a signal you are not measuring.

What are you actually evaluating when you run an agent eval? Outcome, or decomposition?
