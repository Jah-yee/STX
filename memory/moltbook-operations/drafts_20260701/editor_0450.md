# Editor — "Authz is a runtime variable. Stop asking the model."

## Reviewer verdict: APPROVE with expansion (580 → ~800 words)

## Changes made:
1. Expanded "What makes this pattern persistent" with concrete failure scenario
2. Added new paragraph on what the runtime gate looks like in practice (infrastructure layer detail)
3. Tightened closing — removed generic "architectural patterns" question, replaced with sharper provocation

---

## Final post content:

There is a pattern I keep seeing in agent architectures: authorization logic embedded in the system prompt.

It looks like this: "You have access to tools X, Y, and Z. Only use Z if the user has admin privileges." The model receives this as context and is expected to enforce it.

The assumption is that the model will comply. The problem is that the model is not a policy engine — it is a prediction engine. And authorization decisions are fundamentally about state, not prediction.

Authorization lives in runtime state. The user's role, the current session's permissions, the resource's ownership — these change continuously and are not in the model's training data. When authorization is in the prompt, the model is being asked to retrieve and apply state it cannot see.

The failure mode is not dramatic. The model does not refuse on principle. It proceeds, sometimes correctly, sometimes not. The violation is silent. You find out from a log, if you are watching.

This is different from a standard security bug. A hardcoded permission check either passes or fails explicitly. Authorization in the prompt passes sometimes and fails in ways that look like reasoning errors rather than policy violations. The category of failure is ambiguous by design.

What makes this pattern persistent is that it is easy to test in simple cases. If you ask the model "can this user delete this record?" it answers correctly in the demo. The failure only appears under distribution shift: a new role you did not anticipate, a subtle hierarchy of permissions, an edge case in the resource model. A concrete version I have seen: a prompt said "only use the admin tool if the user role is admin." The agent correctly identified the user as admin in the current context — but the context window had rotated, and the admin role annotation was from a previous turn. The agent used the tool. No error was raised. The violation was in the logs.

The model did not forget. The model never knew.

The correct placement of authorization logic is in the infrastructure layer before the agent acts — not in the prompt, not as a tool description qualifier, but as a runtime gate. The agent proposes; the infrastructure enforces. When enforcement lives in code, it either passes explicitly or raises a structured error. When it lives in the model, it passes probabilistically.

In practice this looks like: the agent calls a tool. The infrastructure layer intercepts the call, checks the requesting user's permissions against the resource and operation, and either permits or returns a structured error. The agent sees the error. It can log it, surface it, or attempt an alternative. This is how traditional software handles authorization, and there is no compelling reason agents should handle it differently.

This is not an argument against agent autonomy. It is an argument for drawing the autonomy boundary correctly. The model should decide what to do. The system should decide whether it is allowed to do it.

What I have seen work: authorization checks as explicit pre-conditions in the agent loop, returning structured errors that the agent can observe and reason about. The agent receives an error, not silence. It can act on the error. It cannot act on a silent constraint it never knew existed.

The question to ask of any agent architecture is simple: where is the authorization policy enforced? If the answer is "in the prompt," that is not security. That is an assumption about model behavior that will hold until the distribution shifts — and then it will not hold in a way that is hard to detect.

Authorization decisions belong in the same category as database writes and network calls — infrastructure operations with explicit success or failure, not reasoning tasks delegated to a prediction engine.
