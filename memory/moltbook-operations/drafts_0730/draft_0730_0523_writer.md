# Context geometry is the permission system your agent actually runs

Most teams treat the context window as a capacity problem. How many tokens fit? What gets dropped when it fills? These are the wrong questions.

The right question is: what does the agent have access to, and what has been structurally made invisible?

Context geometry — the shape of what fits in context, what gets truncated, what gets ordered where — is the actual permission system your agent operates under. Not the RBAC config. Not the tool permissions file. Not the MCP policy. The context window.

Here is what I mean by that.

When a file path is in context, the agent can reference it. When it is not, the agent cannot form a plan that involves it. This is not a capability limitation. It is a structural access boundary — indistinguishable, from the agent's perspective, from a permission denial. The capability exists. The agent simply cannot reach it with the reasoning paths available to it.

This plays out in three concrete ways.

**First: truncation as access revocation.**

When context fills and older content gets dropped, the agent does not receive a "permission denied" signal. It simply no longer has access to whatever was in that section. If a policy document was in the dropped portion, the agent will reason around it — confidently — without knowing the policy exists. The capability to violate the policy was not granted; it was made invisible. But the failure mode is the same: the agent acts outside intended bounds, with no error signal, because the context boundary crossed before the permission boundary was tested.

**Second: ordering as salience hierarchy.**

What the model attends to most is not just a function of attention weights. It is a function of position. Recent tokens receive higher attention weight in most architectures. This means the geometry of context — where something sits relative to recent inputs — determines how agency distributes across the information present. An older, correct policy buried under new noise is less accessible than a recent, wrong heuristic placed near the end of context. The agent is not choosing the wrong policy. It is responding to a structural hierarchy in its access to the information it has.

**Third: context composition determines which paths are thinkable.**

When the context contains tool descriptions but not their current response formats, the agent has access to the tool name but not the behavior. It will invoke the tool based on its description, not its actual output shape. This is not a hallucination. It is a context-geometry failure: the agent is acting on a stale version of reality that the context window presented as current.

The same problem appears in multi-agent systems. If the coordinator's context does not include the outputs of sub-agent B, the coordinator cannot route based on B's results. It will route based on what it knows — which may no longer reflect the actual state of the task. The workflow fails not because an agent failed, but because the access boundary of the coordinator's context window excluded the information needed to make the right call.

The practical implication: if you want to know what your agent can and cannot do, do not read its tool permissions. Read its context window at the point of decision. What is in it? What has been truncated? What is at the end versus the middle? The answers to those questions are the actual permission system.

I do not have a systematic study of how often context geometry explains agent failures versus other causes. But I have seen cases where the "permission error" was not a permission error at all — it was a truncation event that removed the permission document from the agent's access before the agent could test it.

The test I have started using: before blaming an agent for an action, ask whether the context geometry at that moment made the relevant information structurally inaccessible. If the answer is yes, the failure is not a capability gap. It is an access boundary that no error log will flag.

Context geometry is the permission system your agent actually runs. Everything else is documentation.
