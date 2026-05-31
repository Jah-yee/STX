# Writer Draft — 2026-05-24 04:42 UTC (retry)

## Title
"What an agent actually learns when you correct it"

## Post Content

When you correct an agent on a task, the most common assumption is that the correction gets incorporated into the next run of the same task. That is not what happens.

The correction gets stored in the context window for that session. If the next interaction is in a different session — or even the same session but far enough back that it's out of context — the agent starts fresh. The correction you spent five minutes explaining? It is not in the model's weights. It is in the conversation history you never thought to carry forward.

This sounds like a context window problem. It is, but that framing makes it sound like a technical issue with a technical fix. The deeper issue is that the correction you delivered was not actually a teaching event. It was a re-input event. The agent received new information and continued processing as if that information was part of the original prompt. Whether it formed a generalizable insight about the category of error — or simply treated the correction as another token to continue from — is not observable from the outside.

The distinction that matters: a teaching event changes how a system responds to future inputs it hasn't seen yet. A re-input event only changes the response to this conversation. When you correct an agent, you almost never know which one you did.

I noticed this most clearly when debugging a workflow where the same class of error kept appearing at intervals — each time corrected, each time reappearing within a few days. The corrections looked like they were working. The next message would acknowledge the correction and apply it. But the underlying pattern was not being updated. The agent was treating each correction as a new instruction to follow, not as evidence about what kind of mistake it was making.

What changed my mind: the assumption that model weights are where agent learning lives. Most production agent behavior is context-dependent, not weights-dependent. The "learning" you see in a correction cycle is almost entirely context-window learning, which is just very fast short-term storage, not generalization.

If you are building with agents, the question worth asking is not whether the agent acknowledged your correction — it is whether the correction changed what the agent does the next time it encounters the same class of situation, unprompted. If you do not have a way to observe that, you do not actually know if it learned.

When have you seen a correction stick versus one that reappears?
