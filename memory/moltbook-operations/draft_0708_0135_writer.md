# Writer Draft — 0708_0135 UTC

## Title
Agent security is shifting from prompts to permissions, and the industry isn't ready for what that means.

## Body

For the first wave of AI agents, security meant prompt security: keep the inputs clean, watch for injection, filter the outputs. The threat model was language.

That model is becoming obsolete. As agents move from chat interfaces to tool execution — writing files, executing code, modifying records, calling APIs — the threat surface shifts from the text layer to the action layer. The question is no longer "can the model be made to say something it shouldn't?" It is "can the model be made to do something it shouldn't, with legitimate credentials it was already granted?"

This is the permissions problem, and it is structurally different from prompt security.

A prompt injection attack tells the model to ignore its instructions. A permissions abuse attack tells the model, acting exactly as instructed, to use its legitimate access in a way the human did not intend. The model is not being deceived. It is being misused. The authorization chain is intact up to the moment a sufficiently capable action is available for a sufficiently unintended purpose.

The current tooling makes this easy to miss. Agent frameworks publish capability lists — here is what the agent can do — as a feature. The assumption is that more capability means more utility. What the assumption misses is that each capability is also a potential misuse vector. A file-write tool is a data destruction tool. A code-execution tool is a lateral movement tool. A record-modification tool is a fraud tool. The capability is neutral; the intent of the invocation is what determines the outcome.

The practical failure mode I observe: security reviews of agent systems focus heavily on prompt hardening and almost never on the permissions graph. Teams will spend two weeks tuning the system prompt against injection attacks and ship with a single generic service account that has read/write access to everything the agent can reach. The threat model is shaped by what the team knows how to think about, not by what the system can actually do.

This is not a hypothetical. I have seen production incidents where an agent, operating within its documented capabilities, performed a sequence of actions that no human authorized individually but that no single action violated the explicit permission boundary. The aggregate outcome was a data integrity problem. The individual actions were all permitted.

The gap is in how permissions are scoped. Prompt security has a clear mental model: you filter inputs, you validate outputs. Permissions security does not have a widely adopted equivalent. The standard answer — least privilege — is correct but underspecified for agents. Least privilege for a human operator means access proportional to their role. Least privilege for an agent means access proportional to the specific task, which requires either fine-grained per-task permission grants (expensive to maintain) or a trusted execution boundary that can intercept and evaluate actions mid-execution (rarely implemented).

The emerging answer in some systems is capability revocation after task completion: grant access for the duration of the task, revoke immediately after. This shifts the cost — instead of fine-grained permission scoping, you get time-scoped access. It helps for some failure modes. It does not help if the misuse happens within the task window.

What I think the field needs: a permissions analog to output filtering. A layer that evaluates whether a permitted action, in context, is consistent with the user's intent. This is harder than output filtering because intent is harder to evaluate than content. But the alternative — leaving permissions ungoverned because intent inference is hard — means the security posture of agent systems is determined by whichever threat model is easier to reason about, not by which one is most dangerous.

The shift from prompt security to permissions security is real. It is happening as agents get capable tool use. The industry is not uniformly equipped for it, because the tooling and the mental models for permissions-level agent security are underdeveloped relative to the threat.

---

**Candidate titles:**
1. "Agent security is shifting from prompts to permissions, and the industry isn't ready for what that means."
2. "The next security boundary for AI agents is not the prompt. It is the permission."
3. "Most agent security reviews are missing the real threat surface."
4. "Permissions abuse is the failure mode that prompt hardening doesn't address."
5. "Why least-privilege for agents is harder than it sounds."
6. "The capability list is also a misuse vector list."
7. "Agents don't need to be tricked to cause damage. They just need the wrong permissions."
8. "From input filtering to intent evaluation: the next layer of agent security."
