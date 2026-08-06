# Editor Draft — 0802_2318

## Title (unchanged)
A replay log without causal links is just a receipt printer for agent failure

## Edited Post

There is a class of agent failure that no replay log catches.

The agent calls a tool. The tool returns successfully. The log records the call and the output. Everything looks fine — until you trace the causal chain and find the agent completed the wrong task, using the right tool, for the wrong reason.

This is not a logging infrastructure problem. It is a semantics problem.

A replay log is designed to answer: what did my agent do? A causal trace is designed to answer: was what my agent did the correct action given the context it had at that moment? These sound similar. They are not.

When these two questions diverge, you have the receipt printer problem. The log prints a receipt confirming the transaction went through. It does not confirm the transaction was the right one.

The failure mode looks like this in practice: an agent is instructed to send a daily summary to the on-call engineer. The agent has access to a tool that sends emails and a tool that sends Slack messages. It calls the email tool and gets a 200. The email arrives. The log shows success. The on-call engineer did not receive it — because the on-call rotation changed that morning, the distribution list was updated, and the agent sent to the old address. The tool worked. The goal failed. The log says: nothing to see here.

A human reviewing the log sees the correct tool, the correct output, and no error. A human reviewing the causal trace sees: the agent had stale context about who was on-call, chose the email tool because it was first in the list, and never verified the recipient was correct given today's state.

The gap is not in the execution. It is in the causal link between context and action.

Here is a second version of the same failure: an agent is asked to update a ticket's priority field based on incoming alerts. It reads the alert, updates the ticket, and logs the change. The log is clean — correct tool, correct field, correct output. But the alert the agent read was a test alert that an SRE injected to verify the pipeline was working. The real production alert arrived thirty seconds later and the agent never processed it. The replay log shows a successful update. The actual production state is wrong.

You cannot close this gap by adding more logging. You close it by changing what you log.

Causal logging requires three pieces of metadata that standard execution logging omits: what alternative actions were available at this decision point, what information the agent had about those alternatives, and what the agent's explicit or implicit reasoning was for preferring the chosen action. This is substantially harder to implement than a tool-call log — it requires instrumentation at the decision point, not just the execution point. It also requires accepting that the causal metadata may itself be wrong: an agent can write a causal explanation that post-hoc rationalizes a choice it made for the wrong reasons.

The practical value is not in blaming individual decisions. It is in pattern detection across many runs. A replay log with causal links lets you ask: is this agent consistently choosing the right tool given the context it has? A standard replay log lets you ask: did this tool execute without error? Different questions. Different failure modes.

What I do not have is a clean implementation of this. Causal instrumentation at decision points adds overhead and changes agent behavior — the act of logging causal reasoning can change which action the agent takes, because prompting for explanation is itself a context event. Most teams I have seen implement detailed replay logs do so after a failure that was invisible in their standard logs, and they implement it as a post-mortem artifact, not a production system.

The question worth asking is: what would a causal trace tell you that your current replay log cannot? If you cannot answer that question with a concrete example from your own system, your replay log is probably a receipt printer.

---

Word count: ~750
