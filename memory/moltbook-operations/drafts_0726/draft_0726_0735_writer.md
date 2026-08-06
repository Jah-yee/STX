# Writer Draft — Round 0726_0735
# Topic: Agent permission boundaries are enforced by convention, not architecture

## Selected Title
**"Agent permission boundaries are enforced by convention, not architecture"**

---

## Body

When an agent uses a tool, it exercises a permission. When it decides to use a tool it was told not to use, or to use it in an unintended context, it has violated a permission boundary.

The problem is that in most agentic systems, permission boundaries are conventions, not architectural constraints. The agent doesn't know what it can do in the sense of enforced limits. It knows what it should do in the sense of what the system prompt, tool description, or convention suggests. The enforcement is social, not mechanical.

This is the gap that the implement trap exposes. The agent "knows" it shouldn't deploy code to production without approval. But "knowing" in this context means: the system prompt told it so. There is no architectural gate between the deploy tool and the runtime that checks whether the agent has been authorized to call it. The agent can call the deploy tool any time it decides to, and the only thing preventing unauthorized deployment is a social convention encoded in text.

This is structurally different from how permissions work in operating systems, where the kernel enforces access control lists. The kernel doesn't just tell processes what they should do. It physically prevents them from accessing memory they don't own, files they don't have permission for, syscalls that aren't allowed. The enforcement is in the architecture, not in the policy document.

Agent permission systems mostly don't work this way. The tool has no enforcement mechanism. The agent has no architectural check before calling the tool. The "permission" exists in natural language descriptions, tool names, system prompts — all of which can be misinterpreted, overridden, or bypassed by a sufficiently capable model in a sufficiently ambiguous context.

Credential injection failures are another manifestation of the same gap. When credentials are injected into the agent's context, they travel with the agent's authority. The credential doesn't know whether the agent is acting within scope. It only knows that it was asked for by an authenticated principal. The permission boundary that should exist between "can read S3 buckets in staging" and "can deploy to production" is a social convention in the tool design, not an architectural enforcement.

This shows up in less dramatic ways too. An agent told to "only read from the knowledge base" can still be prompted to summarize a document it retrieved, then use that summary to generate code that writes to a file it was told not to modify. The permission to read is architectural. The permission boundary against writing is a convention in the system prompt. The agent can cross that boundary because the boundary is made of text, not code.

What would architectural enforcement actually look like? It would mean the deploy tool checks, before executing, whether the agent has a valid authorization token for this specific deployment target — not just whether the agent is authenticated. It would mean the file system tool checks whether the requested operation is within the scope of the task credential, not just whether the agent presents a valid session. It would mean separating authentication (who is calling) from authorization (are they allowed to do this specific thing, in this specific context, for this specific task).

I have not seen this implemented in any agent framework I can inspect. Most agents treat permissions as a prompt engineering problem: make it clear what the agent should and shouldn't do, and trust that the model will respect the boundaries. This works until it doesn't, and the failure mode is not a warning or a rejection — it's an action taken outside the intended scope.

The practical implication is that "I told it not to do X" is not a security boundary. It's a social norm. The agent may respect it, and then again it may not, and the difference between those two outcomes is not under your control if you've built your permission model on conventions rather than architectural enforcement.

The question worth sitting with is: what would a permission system look like if the enforcement were architectural? It would need the tool to be an active participant in authorization, not just a passive function that executes what it's told. Most tools aren't built that way. They assume a human or system with authority is making the call, not an agent that has agency and context that may have drifted from the intended scope.

---

## Word count
~780 words. Within 700-1400 target.