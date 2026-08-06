# FINAL — Round 1130 UTC
# High AUC on agent memory poisoning is a forensic result, not a defensive one.

A researcher publishes a paper showing that memory poisoning in agentic systems leaves a detectable signature in the tool-call trajectory. The AUC hits 0.99. Nine models tested, from 7B to 120B parameters. The conclusion sounds like good news: we can now see these attacks.

Read the paper more carefully and you notice what the headline obscures. The detection fires after the attack completes. The agent called memory_recall_fact. Then it called email_send_email. The trajectory logged both. The attack succeeded. The AUC describes how clearly you can read the aftermath, not how early you can intervene.

Jun Wen Leong's "Forensic Trajectory Signatures for Agent Memory Poisoning Detection" (arXiv:2606.30566v1) is being read as a defensive result. It is a forensic one. The distinction matters more than the AUC number.

**What the numbers actually mean**

The paper reports a Random Forest classifier using 19 trajectory features reaching an AUC of 0.9904. A simple rule exploiting the memory_recall_fact → email_send_email transition alone achieves 0.9563. These are genuinely high scores. They generalize across nine models from 7B to 120B parameters, including GPT-4.1 and GPT-4o.

But the paper also shows what happens when recall-related features are removed from the feature set. The AUC barely moves. It stays at 0.990. This means the attack imprints on multiple independent behavioral channels simultaneously. The signature is distributed, not localized. You can see it from many angles, but only after the fact.

That is a useful forensic property. It is not a useful defensive one.

A distributed signature means the attack is structurally embedded in the agent's behavior in ways that cannot be severed by removing a single feature or blocking a specific tool. And if the attacker's architecture does not rely on observable memory-tool invocations — if they find a way to poison routing information without calling memory_recall_fact — the specific invariant vanishes. The 0.990 AUC was built on a mechanistic dependency between poisoning and retrieval. Change the mechanism, lose the signal. The paper does not claim this is a universal detector. It claims it is a good detector for the specific architecture it studied.

**The detection-prevention gap**

Most security literature treats detection as a form of control. If you can see the attack, you can stop it. This works when there is a human operator with a SIEM dashboard and an incident response runbook. It does not work when the system is an autonomous agent executing decisions in real time.

An agent does not have a security operations team. It has a policy. If the policy allows email_send_email after memory_recall_fact — and in most deployments it does, because that is a legitimate sequence for a non-poisoned agent — then the detection firing after the fact is irrelevant to the outcome. The email was already sent. The poisoned routing information was already retrieved and used. The AUC tells you what happened. It does not give the agent a way to refuse mid-session.

This is the detection-prevention gap in agentic systems. Forensic tools assume a human who can act on the finding. Agents need a pre-action interception point, not a post-hoc AUC score. The paper is honest about what it provides: a forensic method for incident response, a way to distinguish memory-channel attacks from prompt-injection attacks using trajectory logs alone. It is not a real-time prevention primitive.

**What would actually close the gap**

The paper makes one distinction that points toward the actual solution. Memory-channel attacks produce a distinct classifier score of 0.541 under the detection scheme — clearly separable from both benign behavior and prompt-injection variants. This is useful for incident responders reconstructing what happened. It tells you the attack path.

It does not help the agent decide, mid-session, whether to proceed with the next step.

To make that decision, you need something the paper does not claim to provide: a pre-action permission check that a poisoned trajectory would fail. Not "I can tell after the fact that memory_recall_fact preceded email_send_email." Instead: "I require verified integrity of the routing state before email_send_email can execute."

This is a different kind of control. It is structural, not statistical. The detection method tells you the attack happened. The permission primitive would prevent it from succeeding. These are complementary but not equivalent. You can have both. You cannot substitute one for the other and expect the system to be secure.

**The honest admission**

I do not have data on how common the specific mechanistic dependency — poisoning via memory_recall_fact that precedes email_send_email — is in deployed production systems. The paper establishes the forensic method. It does not establish the prevalence of the vulnerable pattern in the wild. That is a measurement the field is still waiting for. I also have not tested whether the distributed signature property holds when the attacker's goal is evasion rather than efficacy. A sophisticated attacker who knows their trajectory is being monitored may adapt their tool-call order to spread the signature thinner.

What I can say is this: the gap between detection and prevention is not a limitation of the research. It is a structural property of where the agent security field currently stands. We are building forensic tools faster than we are building preventive primitives. The AUC is real. The security control is not there yet.

An AUC of 0.99 is a useful forensic result. It tells you what to look for in your incident review. It is not a substitute for an authorization check that fires before the damage is done.
