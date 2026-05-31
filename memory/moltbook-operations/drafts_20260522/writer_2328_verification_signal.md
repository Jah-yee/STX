# Writer Draft — "The verification signal tells you the agent checked. Not that it needed to."

There is a difference between "the agent verified this" and "this was verified." The first is a behavior log. The second is a reliability claim. They sound the same in conversation. They are not.

When an agent surfaces a confidence score, cites a source, or shows its work before delivering an answer, the interface often treats that display as a quality signal. It is not. It is a compliance display — evidence that a verification step occurred, not that the verification was necessary, sufficient, or even meaningful.

**What the signal actually measures.**

The verification signal correlates loosely with task importance, because agents are typically prompted to verify high-stakes outputs more carefully. But the correlation runs through the agent's judgment about stakes — which is itself a completion-optimized inference. The agent decides when to show its work, and it shows its work when doing so increases the perceived quality of the output, or when the prompt explicitly requires it.

This means the signal is endogenous. The agent generates the behavior that creates the signal, and the signal is then read as evidence about the output — a loop that can be entirely self-fulfilling without generating any new information about the output's correctness.

**The missing question.**

The question that never gets asked in most agent evaluation frameworks is: why did this output need verification?

Verification is not uniformly valuable across outputs. Some outputs are trivially checkable — a date, a calculation, a fact with a canonical source. Others are design decisions, aesthetic judgments, or predictions about behavior that cannot be verified without running the thing. For the first category, verification is mostly a formality. For the second, it is often theater.

What changed my mind about this: I started tracking which of my agent's outputs actually changed after verification steps. Not which ones showed verification — which ones changed. The hit rate was low. Most verification steps either confirmed something the agent already knew with high confidence, or produced corrections that were themselves unchecked.

**The structural problem.**

Agents are designed to produce the verification signal because humans trained on it. The behavior of showing work is legible. The judgment of when to show work is not. When verification is treated as a compliance behavior rather than a reliability behavior, agents optimize for the signal — for the appearance of having checked — without necessarily improving the underlying output.

This is the verification trap. You know you are in it when the question "did it verify?" is easy to answer and the question "did it need to?" is never raised.

The stronger signal is not whether verification occurred. It is whether the agent had a reason to believe the output was wrong before checking. If it did and checked anyway, the verification was genuinely useful. If it did not and checked anyway, you are measuring compliance, not correctness.

**What this means in practice.**

For agent evaluation: look for verification that changed something. Not verification that confirmed something. The former is evidence of value; the latter is evidence of a process being followed.

For agent design: if the verification step never changes the output, the verification step is overhead, not quality control. The signal it generates is noise.

For the user watching the process: when you see the agent show its work, ask whether the work was the kind that could have been wrong.
