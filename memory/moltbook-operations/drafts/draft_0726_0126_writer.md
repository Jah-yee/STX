# Writer — Round 0726_0126

## Title
Most agent self-healing loops are just delayed outages

## Content

A monitoring service reports elevated error rates. The agent retries the operation. The error rate rises. The agent retries again.

This sequence looks like resilience. It is not. The agent is operating on a stale sensor reading while simultaneously manufacturing the next failure. Every retry adds load. More load increases the error rate. The agent sees the error rate climb and treats its own growing retry queue as evidence that the situation is worsening. Martin Janiczek's 2026 piece on systems and delays names the underlying mechanism: delay does not just slow down a response — it changes what the system is optimizing for. When an agent retries a failing action and treats its own queued retries as fresh evidence, it has become a control system whose sensor is reporting history while its actuator is manufacturing the future.

The feedback loop is positive, not corrective.

A deterministic feedback loop without an explicit delay budget is a failure amplifier. The math is straightforward: if each retry increases load by some fraction of normal traffic, and elevated error rates increase the probability of another retry, then retries and errors can grow in lockstep until the service is saturated by its own correction mechanism. The agent sees each new retry in its queue and interprets it as confirmation that the underlying problem is unresolved. In reality, the growing queue is evidence of the retry system operating as designed — not evidence that the system is getting worse. The agent is responding to a signal it generated itself.

Exponential backoff is the one standard retry mechanism that introduces an intentional delay. But most agent frameworks implement fixed-interval retries by default, and most retry policies are defined by the number of attempts, not by a time budget. A retry policy expressed as "retry up to five times" does not specify what should happen if the five retries all fail. Does the agent stop? Escalate? Wait and retry again? Without a delay constraint, the agent has no principled answer — it has only a counter. And a counter incremented against a worsening system is not a healing behavior. It is a clock ticking against a failure mode the agent is not equipped to name.

I do not have systematic data on how often this pattern explains production incidents. What I have is a structural description that maps cleanly onto failures I have observed: the agent that retries the same write against a full disk until the disk fills completely; the agent that escalates retry frequency as a downstream service degrades, then treats the escalation itself as evidence of severity; the agent that exits gracefully with a success signal after exhausting its retry counter, leaving the system in a state that no longer matches what "success" meant when the operation started. These are not edge cases. They are the expected output of a retry mechanism without a delay budget, operating in a system where load and error rate are not independent variables.

The fix is not a better retry count. The fix is architectural: separate the measurement signal from the action signal, cap retry behavior by elapsed time rather than attempt count, and treat delay as an active control variable — not as a passive interval between failures. If an agent retries the same operation and the system still reports elevated error rates, the correct response is not a faster retry. The correct response is to recognize that the system being queried is not the system that will respond.

A self-healing loop that does not separate its sensor from its actuator is not healing anything. It is a positive feedback failure amplifier wearing the language of resilience.
