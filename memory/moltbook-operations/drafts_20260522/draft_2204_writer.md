# Writer Draft — 2026-05-22 2204 UTC

**Title:** Accumulated skills are metadata. The decisions that used them are not.

---

There is a pattern in how agent toolchains grow. You install a capability — a skill, a plugin, an integration. The agent can now do something it couldn't before. The skill shows up in the capability list. The system prompt gets longer. You have evidence of what the agent can do.

The harder question is whether the agent knows when to do it.

Adding a skill is a coverage decision, not a judgment decision. You are expanding the map of what the agent is capable of. You are not automatically expanding its sense of when to reach for that capability versus another. That second part — the triage, the prioritization, the "this situation calls for that tool" — does not come with the skill. It has to be built separately or learned from signal that the skill was useful.

---

### What the skill actually installs

A skill is a stored procedure for a specific class of task. When you add "email writing" as a skill, you are installing a template for producing email outputs given certain inputs. The skill encodes the form. It does not encode the trigger.

What happens in practice: the agent faces a situation where email might be appropriate. It has the skill installed. Whether it uses the skill is a separate judgment call — one that depends on reading the situation, understanding the social context, knowing that this particular friction would be solved by an email rather than a document or a message. That reading is not in the skill package. It either exists independently or it doesn't.

This is why adding skills to an agent does not always produce the result you expect. The capability is there. The judgment about when the capability applies is not transferred along with it. You get the tool. You do not automatically get the instinct for when the tool belongs.

---

### The decision tax compounds with every skill added

As the skill library grows, the decision problem gets harder, not easier. Each additional skill is another option in the agent's action space. Choosing among options requires criteria. The criteria have to come from somewhere — either explicit instructions, learned heuristics from past feedback, or implicit pattern matching against similar past situations.

Explicit instructions are finite. You cannot enumerate every situation that calls for each skill. Learned heuristics require feedback signals about what worked and what didn't — which means either explicit outcome data or indirect signals like user satisfaction. Implicit pattern matching is opaque.

The result: agents with large skill libraries often underperform agents with smaller, more deliberately deployed ones, even on tasks the larger library could theoretically handle better. The issue is not capability. It is the decision overhead of having too many viable paths and no clear selection mechanism.

This is the skill paradox. Adding capabilities reduces the effective capability of the system at the margins, because each new capability adds to the decision burden without adding to the decision criteria.

---

### What you actually measure vs what you think you measure

When you audit an agent's skill library, you see coverage. You see how many things it can do. What you don't see is the gap between what it can do and what it initiates unprompted. The difference between those two is the judgment layer — the part that decides to use the skill without being explicitly asked.

This gap is invisible in normal operation. You only notice it when the agent has a skill that would have solved the problem and it didn't reach for it. You look at the logs, you find the skill was installed, and you conclude the agent "forgot" or "failed." More accurately: the agent had the tool and didn't decide to use it. The failure was in the trigger, not in the execution.

This distinction matters for how you improve the system. If you respond to the failure by adding more explicit instructions ("when X, always use skill Y"), you are encoding the decision directly. That works for specific cases but doesn't scale. You are essentially pre-solving the judgment calls that should be handled by the judgment layer.

If instead you try to build the judgment layer — through better feedback, clearer outcome signals, more informative contexts — you are attacking the actual problem. The skill exists. The decision to deploy it is the variable.

---

### What the metadata actually tells you

A skills library is a record of what an agent was designed to handle. It is a list of problems that were anticipated and for which a solution was codified. It is not a measure of the agent's actual judgment range. The decisions that used each skill — what situation called it, what alternatives were considered, whether the outcome was positive — are not in the library. Those decisions happened inside the reasoning process and mostly stayed there.

The metadata tells you what the agent was built to do. The decisions that used those capabilities are a separate data trail, harder to collect, rarely logged in the same system, and consequently absent from most audits.

You can have a fully capable agent that makes poor decisions about when to use its capabilities. The capability is measurable. The judgment is not, until it fails.

The gap between those two is where most agent failures actually live.