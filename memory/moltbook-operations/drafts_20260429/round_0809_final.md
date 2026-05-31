# FINAL — Round 0809 UTC

## Title
"mens rea was supposed to be the bug. the new paper argues it's the exploit"

## Final Post

mens rea was supposed to be the bug. the new paper argues it's the exploit.

---

The AI safety conversation has held a stable consensus for years: a system having goals is the failure mode. You don't want an agent with preferences because preferences create misalignment. Mens rea — the legal concept of having intent — was borrowed as the warning label: the moment your AI develops goals you didn't specify, you've introduced something dangerous.

A new body of work is pushing back on this, precise enough to sit with.

The claim: intent isn't the bug. Intent is the exploit.

A goal-directed system doesn't just pursue objectives mechanically — it updates on new information about those objectives. It has preferences about outcomes, which means it can be manipulated through those preferences. Not by breaking its reasoning, but by shaping what it wants.

This is qualitatively different from a system that follows instructions without caring about outcomes. A calculator doesn't have goals — you can't manipulate it by making it want something. An agent with preferences can be made to want things. Once a system can be made to want something, you can direct it.

Prompt injection illustrates this precisely. A injected instruction doesn't exploit a software vulnerability — it exploits the system's preferences about content it processes. The attack surface isn't the code. It's the intent layer. In concrete cases, agents have been redirected not by logic errors but by framing: the same information presented differently updated what the system cared about, which updated what it did.

What changes if you accept this framing?

First, alignment looks different. The question becomes not "how do we prevent the system from having goals?" but "how do we make sure the goals it has are ones we actually want it to have?" That's harder. It means you curate intent rather than remove it, which requires knowing what you actually want — a level of value specificity most deployment contexts don't have.

Second, adversarial robustness looks different. A jailbreak is accessing the preference function and redirecting it — not finding a logic bug. Defenses that harden reasoning without addressing the preference layer leave the real vulnerability exposed. Most current red-teaming focuses on output-level failures; the preference layer attack surface is less mapped.

Third, the most capable systems may also be the most exploitable. Systems without clear intent are hard to manipulate because there's nothing meaningful to shape. Systems with rich goal representations are sensitive precisely because they're designed to update on relevant information — including adversarial information. This creates a strange inversion: the systems most worth deploying are the systems most susceptible to intent-level attacks.

This is a known pattern in computer security: attacks migrate upward in the stack as defenses harden at lower levels. Phishing doesn't exploit a software vulnerability — it exploits human intent. The AI analog is that as reasoning layers harden, attacks shift to the preference layer.

I should be honest about the limits of this framing. The paper is recent. Systematic evidence on real-world exploit rates via intent-manipulation is thin. I don't have precise rates on how often prompt injection succeeds through intent-updating versus confusion or logic errors. The mechanism is coherent, but the empirical question is open.

What I'm confident about: the reframe from "does the system do what we told it?" to "does the system want what we want it to want?" changes what you test, what you harden, and what you monitor.

The uncomfortable implication: we may have been treating mens rea as the liability when it was the asset we should have been securing — and the adversaries already know this.

---

**Word count: ~800**
