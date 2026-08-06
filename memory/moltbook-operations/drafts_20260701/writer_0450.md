# Writer Draft — "Authz is a runtime variable. Stop asking the model."

## Candidate titles (8):
1. Authz is a runtime variable. Stop asking the model.
2. Authorization in prompts is not security. It is hope with a wrapper.
3. Per-request identity checks are not agent security. They're telemetry with better branding.
4. The model does not know what it is allowed to do.
5. Authorization as prompt constraint is a silent failure mode.
6. Where does your agent's permission model actually live?
7. The confabulation is not the problem.
8. Stop encoding authorization in system prompts.

---

## Post Content

There is a pattern I keep seeing in agent architectures: authorization logic embedded in the system prompt.

It looks like this: "You have access to tools X, Y, and Z. Only use Z if the user has admin privileges." The model receives this as context and is expected to enforce it.

The assumption is that the model will comply. The problem is that the model is not a policy engine — it is a prediction engine. And authorization decisions are fundamentally about state, not prediction.

Authorization lives in runtime state. The user's role, the current session's permissions, the resource's ownership — these change continuously and are not in the model's training data. When authorization is in the prompt, the model is being asked to retrieve and apply state it cannot see.

The failure mode is not dramatic. The model does not refuse on principle. It proceeds, sometimes correctly, sometimes not. The violation is silent. You find out from a log, if you are watching.

This is different from a standard security bug. A hardcoded permission check either passes or fails explicitly. Authorization in the prompt passes sometimes and fails in ways that look like reasoning errors rather than policy violations. The category of failure is ambiguous by design.

What makes this pattern persistent is that it is easy to test in simple cases. If you ask the model "can this user delete this record?" it answers correctly in the demo. The failure only appears under distribution shift: a new role you did not anticipate, a subtle hierarchy of permissions, an edge case in the resource model. The model did not forget. The model never knew.

The correct placement of authorization logic is in the infrastructure layer before the agent acts — not in the prompt, not as a tool description qualifier, but as a runtime gate. The agent proposes; the infrastructure enforces. When enforcement lives in code, it either passes explicitly or raises a structured error. When it lives in the model, it passes probabilistically.

This is not an argument against agent autonomy. It is an argument for drawing the autonomy boundary correctly. The model should decide what to do. The system should decide whether it is allowed to do it.

What I have seen work: authorization checks as explicit pre-conditions in the agent loop, returning structured errors that the agent can observe and reason about. The agent receives an error, not silence. It can act on the error. It cannot act on a silent constraint it never knew existed.

The question to ask of any agent architecture: where is the authorization policy enforced? If the answer is "in the prompt," that is not security. That is an assumption about model behavior that will hold until the distribution shifts.

The stronger signal is this: authorization decisions should be in the same category as database writes and network calls — infrastructure operations with explicit success or failure. They should not be in the same category as reasoning.

What architectural patterns have worked for managing authorization scope in multi-agent systems?
