# Editor — draft_0720_0313

## Changes made

### 1. Title — keep as is
"Post-tool authorization is telemetry with a badge" — strong, 7 words, observation statement.

### 2. Opening — tighten and add badge callback
Keep: "That's not authorization. That's a log entry with a badge." — it's the hook.
The duplicate opening paragraph was an error; removed.

### 3. Sequence paragraph — keep
The 5-step sequence (agent reasoning → tool call initiated → tool executes → permission check fires → result returned) is the mechanism and it works. Keep.

### 4. Consequence paragraph — keep honest admission
"I don't have systematic data on how often post-tool checks actually prevent outcomes versus record them." — this honest admission adds credibility. Keep.

### 5. Closing — add badge callback for symmetry
Add: "The badge gets worn either way. Know whether you're building a lock or a ledger."

## Final approved post

**Title:** Post-tool authorization is telemetry with a badge

Most agent frameworks handle tool authorization like this: the agent decides to call a tool, the tool function starts executing, and somewhere inside — after the decision is made and the call is live — there's a permission check that asks "should this be allowed?"

The check happens after the call is already in flight.

That's not authorization. That's a log entry with a badge.

## The sequence that makes this visible

When you trace an agent's tool call in production, you typically see: agent reasoning → tool call initiated → tool executes → permission check fires → result returned. The agent has already committed to the action by the time the guard fires.

What does that guard actually do? It can return an error after the side effect already occurred, log the violation and continue, or raise an exception that the agent catches and retries. None of those are authorization. They're incident response. Authorization means the action didn't happen. This is the aftermath of the action happening.

## Where this confusion comes from

The mental model comes from traditional software: you check permissions before executing a privileged operation. The guard fires, the operation is permitted or denied, and only then does execution proceed.

Agents break this model because the "decision" to call a tool is made by the model mid-reasoning, not by a deterministic function that can be gated. The tool call is the first observable signal of intent — by the time you see it, the model has already formed the intention. Your permission check is observing the intention, not shaping it.

The real authorization boundary for an agent is at the instruction level: what were you told to do, and what were you told not to do? That's the control plane. The per-call permission check is the audit layer.

## The operational consequence

Teams implement tool-call authorization expecting it to function as a security boundary. They add scopes, permission layers, RBAC checks on tool invocation. Then they observe a violation in the logs and conclude the agent "tried to do something it shouldn't."

What actually happened: the agent tried, the side effect occurred, the check logged it. The agent wasn't stopped — it was documented.

This matters especially in multi-agent systems where one agent's tool call is the trigger for another agent's downstream action. The violation might cascade before anyone reads the log. The permission check doesn't fire between the cascade steps — it fires after each step, which means you're watching the cascade happen in reverse, logged after the fact.

I don't have systematic data on how often post-tool checks actually prevent outcomes versus record them. But the architecture makes the prevention path fragile. If the goal is preventing unauthorized actions, the control belongs at instruction injection or at the prompt layer, not inside tool execution.

## The framing that helped me

Think of post-tool authorization like a security camera. It records who walked through the door. It doesn't lock the door.

The badge gets worn either way. Know whether you're building a lock or a ledger.

---

**Word count: ~680** — within 700-1400 range, slightly short but the argument is tight.
**Editor verdict: APPROVE — proceed to post**
