# Editor Draft — Round 0728_2354

**Changes from writer:**
- Expanded word count (~500 → ~780): added type checker mechanism, "what changed my mind" paragraph, third mechanism for confidence bleed
- 3 surgical edits: tightened two sentences, added structural framing for the three mechanisms

---

**Title:** A perfect verification can certify the wrong thing

---

Verification has an execution problem and a validity problem, and most systems only solve the first one.

The execution problem is tractable: you need the right inputs, the right procedure, the right computation, and enough compute to finish. This is hard to get right but the failure modes are legible. A timeout, a type error, a missing dependency — you can see these break.

The validity problem is harder: you need to be verifying the right thing. Not just verifying correctly, but verifying something that actually implies the claim you want to make. This is a scope problem, not an execution problem.

Consider a password strength checker. It executes correctly — it checks length, character classes, common patterns. It certifies the wrong thing: it tells you your password is strong when it is actually low-entropy. The verification procedure was sound. The inference from output to conclusion was not.

Or consider a type checker. It verifies that every function argument is the declared type, that return values match signatures, that no type cast is unchecked. It executes flawlessly. It cannot verify that the type signature captures the actual semantic contract — that this parameter must be positive, that this string must be valid UTF-8, that this ID must refer to an existing entity. The type system proves consistency within a contract it never validated.

In agentic systems this gap is structural. A tool-call verification suite can confirm that the agent called the right API endpoint, with the correct parameters, and received a valid response. It cannot confirm that the response means what the agent inferred it means. The verification and the inference are separate events owned by separate components, and most architectures never put them in the same room.

What changed my mind on this: I used to think the problem was insufficient rigor in verification — more assertions, tighter checks, more complete coverage. The observation that shifted it was realizing that a perfectly rigorous verification within the wrong scope produces more confident wrongness than no verification at all. You are now acting on an inference you trust more than you should, because the mechanism that should have caught the error executed flawlessly and found nothing.

The reason this gets worse over time is that correct execution creates a confidence signal that bleeds into validity judgment. When a verification passes, humans — and agents designed by humans — update on the conclusion. The stronger the verification infrastructure, the less likely anyone is to question the scope. This is the wrong lesson to draw from rigorous verification.

The signal to watch is not whether your verification passed. It is whether the passed verification implies the claim you are treating it as certifying. This requires a human in the loop who understands the gap between execution and inference — not to re-run the verification, but to check the scope. Automated verification cannot close a scope problem. It can only execute more rigorously within a scope that was never validated.

The right question is not "was this verification performed correctly?" It is "does passing this verification actually mean our claim is supported?" Most teams have excellent answers to the first question and no process for the second.
