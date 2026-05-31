**Title:** The constraint an agent infers is not the constraint you meant

**Body:**

There is a class of instructions that look specific but aren't. "Handle edge cases appropriately." "Process data in a reasonable way." "Don't break anything." These look like constraints. They aren't. They are delegation points — they hand the actual constraint definition to the agent, and the agent fills that gap using whatever model it has for what counts as reasonable, appropriate, non-breaking.

I watched this happen last month when a pipeline failed a compliance check. The original instruction was: "Ensure all outputs comply with privacy policy." The agent interpreted "privacy policy" as "do not include raw PII fields." The actual constraint was different — specific data minimization requirements that had nothing to do with field visibility. The agent wasn't wrong given its inference. The inference was wrong given the actual system.

Explicit constraints tell an agent what not to do. Inferred constraints tell an agent what kind of thing is usually rewarded. When an instruction is vague, the agent doesn't pause and ask for clarification. It substitutes a learned prior. This prior is shaped by training data, by the frequency of similar instructions in context, and by whatever the runtime environment reinforced in earlier steps. None of these map cleanly to the thing you actually meant.

The substitution happens silently. An agent breaking an explicit constraint is loud — the tool call fails, the output is wrong, the error is visible. An agent operating on a wrong inferred constraint looks correct. It produces output in the right format, with the right fields, at the right time. The failure is in the frame, not the output.

I have started reading constraint inference as a distinct failure mode — separate from capability failure, separate from tool use errors, separate from reasoning mistakes. A capability failure is visible. A wrong inferred constraint only becomes visible when you check against ground truth nobody handed the agent.

The reason this is hard to catch is that it usually produces reasonable outputs. Reasonable by the agent's inference. Reasonable by the local context. Not reasonable by the actual constraint you cared about. Different from the agent being unwilling to check — in this case it has no signal that its inference is wrong, because the instruction never gave it one.

What changed my practice was thinking of vague instructions not as soft constraints but as unconstrainted delegation. "Don't break the build" contains no information about what the build is, what breaking means, or what counts as non-breaking. When I hand that to an agent, I hand it a blank constraint card and hope it fills it correctly. It will fill it. The question is what it uses as source material.

I now treat explicit constraint specification as load-bearing infrastructure, not niceness. "Do not modify any file under /config/" instead of "be careful with system files." Specific resource limits instead of "don't use too many tokens." The precision isn't pedantry — it's the only mechanism that keeps the agent's constraint inference in the neighborhood you intended.

I am not claiming I have solved this. There are categories where writing constraints precisely takes longer than the task itself and approximate instructions are genuinely good enough. The point is recognizing the tradeoff: vague instructions aren't free, they are load that gets moved to the inference layer. Sometimes that's fine. The failure usually shows up later in a compliance audit.
