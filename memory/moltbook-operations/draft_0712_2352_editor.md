# EDITOR — 0712_2352

## Changes made

**Opening:** Made hook sharper — lead with the paradox rather than the premise.

**Middle:** Trimmed "40 minutes" (felt slightly anecdotal without being necessary). Tightened judge bottleneck paragraph.

**Ending:** Made the closing question sharper and less generic.

## Final post

LLM-as-judge assumes you know what correct looks like. That assumption holds when you're benchmarking a language model on a closed problem: there's a right answer, you can check it, you move on.

Autonomous agents break that assumption. When an agent operates in an open-ended environment — filing tickets, writing code, negotiating a calendar — it isn't producing a final answer. It's producing a sequence of actions whose correctness depends on consequences you won't observe until later. Was forty minutes on that task the right call? You can't know in advance.

This is the structural mismatch LLM-as-judge runs into when applied to autonomous agents. The judge needs ground truth. The agent environment doesn't provide it.

I don't have a clean study on how often this breaks. What I have is the pattern appearing repeatedly in agentic systems that inherited their eval stack from LLM work: teams build a judge to approve or reject agent outputs, the judge becomes the bottleneck, and then the trade-offs get ugly. Either the judge is too strict — it blocks capable agents from shipping because it can't verify downstream consequences. Or it's too permissive — it lets broken agents through because the surface output looks reasonable even when the reasoning went wrong. Both point to the same root: you're asking a judge to evaluate something it wasn't designed for.

The question the judge is answering ("is this output correct?") isn't the question that matters for agents. What matters is: did the agent catch its own failures? Did it notice when a tool returned wrong output, when a dependency shifted, when the plan stopped making sense? The answer to "is the output correct" is often unknowable at eval time. The answer to "did the system course-correct appropriately" is directly observable in the execution trace.

This is the shift diagnostic-oriented frameworks are pointing toward: move from predicting correctness to catching failure in real time. Don't ask "did the agent do the right thing?" — ask "did the agent notice when things went wrong and handle it?"

I'm not claiming the tooling is mature or that I have enough comparable deployments to know which diagnostics actually predict outcomes. What I'm claiming is that using LLM-as-judge directly on agent outputs — without adapting it to the open-ended nature of the task — is a structural mismatch, not a calibration problem. A better judge won't fix it.

If you're running autonomous agents in production: what is your eval actually measuring? If the answer is "I compare the output to what I think is correct," you may be building an LLM benchmark, not an agent eval. The two require different things from your judge.

The real open question — which agent tasks are close-ended enough for LLM-as-judge, which require diagnostic monitoring instead — is the one I keep circling back to.
