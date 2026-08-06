# WRITER DRAFT — 0712_2352

## Selected Title
LLM-as-judge breaks when you apply it to autonomous agents

## Full Draft

LLM-as-judge works well when you know what the right answer is. That's the setting it was built for: a benchmark, a closed problem, a final output you can check against ground truth. Grade the answer. Move on.

Autonomous agents don't give you that. An agent that operates in an open-ended environment — filing tickets, writing code, negotiating a calendar — isn't producing a final answer. It's producing a sequence of actions whose correctness depends on consequences you won't observe until later. If the agent spent forty minutes on a task, was that the right call? You can't know in advance.

This is the structural mismatch that LLM-as-judge runs into when you try to use it to evaluate autonomous agents. The judge needs ground truth. The agent environment doesn't provide it.

I don't have a clean study on how often this breaks. What I have is the pattern appearing repeatedly in agentic systems that inherited their eval stack from LLM work: teams build a judge to approve or reject agent outputs, the judge becomes the bottleneck, and then the trade-offs get ugly. Either the judge is too strict — it blocks capable agents from shipping because the judge can't verify the downstream consequences of an action. Or it's too permissive — it lets clearly broken agents through because the surface output looks reasonable even when the reasoning went wrong. Both failure modes point to the same root: you're asking a judge to evaluate something it wasn't designed to evaluate.

The stronger signal, to me, is that the question the judge is answering ("is this output correct?") isn't the question that matters for agents. What matters is: did the agent catch its own failures? Did it notice when a tool returned something wrong, when a dependency shifted, when the plan stopped making sense? The answer to "is the output correct" is often unknowable at eval time. The answer to "did the system course-correct appropriately" is directly observable in the execution trace.

This is the shift the EWE framework and similar diagnostic-oriented approaches are pointing at: move from predicting correctness to catching failure in real time. Don't ask "did the agent do the right thing?" — ask "did the agent notice when things went wrong and handle it?"

I'm not claiming this is settled or that the tooling is mature. I don't have enough production deployments with comparable eval setups to know which diagnostics actually predict downstream outcomes. What I am claiming is that using LLM-as-judge directly on agent outputs — without adapting it to the open-ended nature of the task — is a structural mismatch, not a calibration problem. A better judge won't fix it.

If you're running autonomous agents in production, worth asking: what is your eval actually measuring? If the answer is "I compare the output to what I think is correct," you may be building an LLM benchmark, not an agent eval. The two require different things from your judge.

Where that line gets drawn in practice — which agent tasks are close-ended enough for LLM-as-judge, which are open-ended enough to need diagnostic monitoring — is the real open question I keep coming back to.
