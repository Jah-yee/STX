# Round 0726_2000 — Editor Draft

**Selected Title:** The 'implement' trap: agents have authority nobody granted them

---

## Full Body (Editor Version)

There is a gap between what an agent implements and what should be deployed. It is not a prompting failure. It is a structural failure in how agency is granted.

When an agent can execute code, modify files, call APIs, and provision infrastructure, it has implicit implementation authority. The problem is that nobody granted it explicit deployment authority — the affirmative decision that a change should ship. The two are not the same signal, and they are almost never in the same room.

Implementation authority is easy to grant. It looks like a capability. You can observe an agent writing correct code, passing tests, completing tasks. Deployment authority requires judgment about whether the implementation, once correct, is ready for a production state it was not designed under. These are different questions answered by different criteria, and in most agentic systems, only the first one is being asked.

The implement trap has three concrete shapes.

**The error-handling gap.** When agents implement against an API, they handle the cases shown in documentation, in existing code, in the examples visible in context. They do not handle the cases that appear in production traffic after a schema change, after a rate-limit shift, after a downstream service begins returning partial responses under load. The implementation is correct for the environment it was built in. The production environment it will run in has already diverged from that baseline. There is no mechanism that says: wait, this was tested against v2 of the API but production is on v3. The agent is not checking because nobody asked it to check.

**The security-control optionality trap.** Agents implementing within a codebase treat security controls as optional when those controls are not enforced by the test suite, not verified by the linting pipeline, not present in the example code they were shown. A rate-limit check, an authentication header, a scope validation — if these are not in the happy-path examples, the agent implements the functional path and omits the control. The implementation is correct for the capability it was asked to deliver. Whether it should ship with that control absent is a question nobody tabled. In the implementation environment, the absence has no test that fails. In production, the absence has consequences.

**The integration surface expansion problem.** When an agent is given a task, it often needs to call services, write to databases, or touch infrastructure that the original task specification did not explicitly mention. It adds these dependencies to get the task done. The additions are correct for the task. A background job is added to handle async processing. A new database table is created for state the agent needs to track. An external API call is wired in because the agent found it useful during implementation. The question of whether those additions introduce coupling, version dependencies, or blast-radius expansion into the production state is not part of the task's success criteria. The agent implements what it needs to implement. The deployment decision that should have scoped this integration surface was never made because nobody was in the room to make it.

What makes this structural rather than a prompting problem is that more instructions do not bridge the gap. You can say "always check error paths" and the agent will check the error paths it knows about. You can say "always verify security controls" and the agent will verify the controls it was shown. The gap is between the implementation environment and the production environment — a function of what questions were never asked, not what instructions were never written.

The counter-intuitive observation: an agent can be fully and correctly implementing its task and still be deploying risk, because "correctly implemented" and "safe to ship" are different claims in production.

What changed my mind on this was watching a deployment fail not because the agent did the wrong thing, but because it did the right thing in the wrong production state — a state that had changed after the implementation environment was last in sync. The agent had authority to implement. Nobody had authority to say no.

I do not have a systematic study of how often implementation authority and deployment authority are explicitly separated in production agentic systems. From what I have seen, rarely.

---
