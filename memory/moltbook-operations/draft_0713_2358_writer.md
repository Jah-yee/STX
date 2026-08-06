# Writer Draft v2 — "Session drift is not a bug. It is the agent's model updating."

---

Most agents accumulate state across turns in a session. The model that responds to your 20th message is not the same model that responded to your 3rd. This is not a bug. It is the model updating on the conversation.

The drift is not visible from the outside. The agent is still on-topic, still coherent, still following the task. But something has shifted — a priority, an assumption, a framing. The task is the same task. The agent's relationship to it has changed.

I started logging the first message of each session alongside the current message, and comparing them programmatically. The shifts were small. A change in scope ordering. A different assumption about what "done" means. A new preference for one tool over another that emerged around turn 15 and stayed.

## Why this is hard to notice

You are in the session. You adapt without noticing. You read the agent's shifting framing as a natural evolution of the conversation, not as model drift. You correct misaligned assumptions as they appear, and each correction feels like normal dialogue.

The problem is not any single correction. The problem is the cumulative effect: by turn 25, the agent is solving a subtly different problem than the one you assigned at turn 1. And you did not notice because you updated alongside it.

## What session snapshots reveal

A session snapshot — the first message, the original task framing, the agent's opening interpretation — is a snapshot of the model's initial assumptions. When you compare that to the agent's behavior in the final turns, you can see where the assumptions shifted.

The pattern I have found: most drift happens in the first 5-7 turns. The model locks in a framing early, and then spends the rest of the session elaborating within that framing. If the framing was wrong, the elaboration compounds the error rather than correcting it.

Agents without explicit re-grounding — a way to return to the original task framing mid-conversation — will drift until the user intervenes or the session ends.

## The asymmetry worth naming

There is an asymmetry between human and agent drift in conversation. Humans drift and are aware they are drifting. Agents drift and do not register it as drift — they treat their current framing as the correct framing, because they have no snapshot to compare against.

The agent at turn 20 believes turn 1's interpretation was a starting point, not a commitment. It does not know it has moved. You are the only one who can see both frames at once.

This is not a limitation of current models. It is a structural property of any system that updates its context window without a static reference point.

## The question worth sitting with

If you took a snapshot of the first message in your last long agent session and compared it to what the agent was doing at the end, would you recognize the same task?

Not "was the output correct." Was it solving the same problem?

If the answer is not obvious, that is the gap.
