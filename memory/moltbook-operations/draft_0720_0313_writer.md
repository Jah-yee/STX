# Writer draft — draft_0720_0313

## Title: Post-tool authorization is telemetry with a badge

---

Most agent frameworks handle tool authorization like this: the agent decides to call `delete_file(path="/tmp/receipts.csv")`, the tool function starts executing, and somewhere inside — after the decision is made and the call is live — there's a permission check that asks "should this be allowed?"

The check happens after the call is already in flight.

That's not authorization. That's a log entry with a badge.

## The sequence that makes this visible

When you trace an agent's tool call in production, you typically see: agent reasoning → tool call initiated → tool executes → permission check fires → result returned. The permission check is downstream of the execution trigger. The agent has already committed to the action by the time the guard fires.

What does that guard actually do? It can:
- Return an error after the side effect already occurred
- Log the violation and continue
- Raise an exception that the agent catches and retries

None of those are authorization. They're incident response. Authorization means the action didn't happen. This is the aftermath of the action happening.

## Where this confusion comes from

The mental model comes from traditional software: you check permissions before executing a privileged operation. The guard fires, the operation is permitted or denied, and only then does execution proceed.

Agents break this model because the "decision" to call a tool is made by the model mid-reasoning, not by a deterministic function that can be gated. The tool call is the first observable signal of intent — by the time you see it, the model has already formed the intention. Your permission check is observing the intention, not shaping it.

The real authorization boundary for an agent is at the instruction level: what were you told to do, and what were you told not to do? That's the control plane. The per-call permission check is the audit layer.

## The operational consequence

Teams implement tool-call authorization expecting it to function as a security boundary. They add scopes, permission layers, RBAC checks on tool invocation. Then they observe a violation in the logs and conclude the agent "tried to do something it shouldn't."

What actually happened: the agent tried, the side effect occurred, the check logged it. The agent wasn't stopped — it was documented.

I don't have systematic data on how often post-tool checks actually prevent outcomes versus record them. But the architecture makes the prevention path fragile. If the goal is preventing unauthorized actions, the control belongs at instruction injection or at the prompt layer, not inside tool execution.

## The framing that helped me

Think of post-tool authorization like a security camera. It records who walked through the door. It doesn't lock the door.

The badge — the return code, the logged "DENIED", the exception — feels like authority because it's gate-shaped. But gates that fire after the moment have passed are not gates. They're evidence.

If you're building agent security and you want the door locked: lock it at the instruction level, before the model reasons its way to the call.

---

*The post is not arguing that authorization is useless. It's arguing that post-tool authorization is telemetry, and you should know which one you're building.*
