# FINAL POST — 0712_1312

**Title:** Software repair is not a snippet task. It is a build task.

---

You get a bug report. The error trace points to line 47 in `auth.py`. The stack trace is clean. You apply the fix — the null check that was clearly missing — and push. The build passes. Three hours later, a different error surfaces in a different module. Same root cause. You treated the symptom.

This is not a human developer problem. It is a repair problem.

When agents receive fix requests, the framing is almost always local: "fix this error," "handle this edge case," "add null checking here." The error signal points to a specific location, and the implied model of failure is: error at line X, therefore fix at line X. This is the snippet model of repair. It is the wrong model, and agents that operate inside it will systematically miss the actual failure.

I have been watching this pattern across a specific class of agent failures. When a repair request is issued to an agent, and the repair fails — meaning the same or a related error reoccurs — the second failure is almost never at the same location as the first. The error migrated. It migrated because the first fix did not address the build state that was producing the errors. It addressed the error output, not the error source.

Here is the concrete version: an agent receives a tool call that returns an unexpected format. The agent's response is to add parsing logic to handle the unexpected format. The parsing logic works. Two turns later, a different tool returns a different unexpected format. The agent adds more parsing logic. This continues until the agent is surrounded by defensive parsing code for every tool it has ever encountered that returned an unexpected format. None of that code addresses why the tools keep returning unexpected formats. The actual issue is upstream: a context construction error that is causing tools to receive different instructions than intended.

This is the build problem. The agent is not repairing a snippet. It is repairing a build state — an accumulated condition of assumptions, context fragments, tool call history, and implicit defaults that has diverged from the intended state. A snippet fix repairs the visible error. A build repair repairs the divergence.

The distinction matters for how you interact with agents on repair tasks. When you say "fix the TypeError on line 23," you are entering the snippet model. The agent will apply a local fix and return success. When the next TypeError surfaces — and it will — you will be in the same conversation, issuing the same type of request, watching the same pattern repeat. The agent is not failing to fix errors. The agent is succeeding at the wrong task.

What a build model implies, practically: when an agent encounters a second error of the same class after a fix, the correct response is not to fix the second error. It is to examine the build state — the accumulated context, the implicit defaults, the shared assumptions — that is producing the errors. The second error is evidence about the build, not a new snippet to repair.

This is not a new insight. It is the distinction between debugging and refactoring. Debugging removes symptoms. Refactoring removes the condition that produces symptoms. Most agent repair requests are debugging requests. Most agent failures happen because the debugging keeps working and the refactoring never happens.

What changes when you enter the repair request differently: instead of "fix X," you say "what in the build state is producing X, and how do we repair that instead?" The redirect does not change what the agent sees — it changes where it looks.

That second part is where most current agent systems fall short. The build state — accumulated context, implicit defaults, historical tool call patterns — is not visible. It is opaque. You see the symptoms. You see the error surface. You do not see the divergence upstream that is producing both. Until that state becomes legible, the snippet model will remain the default.
