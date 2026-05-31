# WRITER — Round 0809 UTC (FULL DRAFT)

## Title
"mens rea was supposed to be the bug. the new paper argues it's the exploit"

## Full Draft

mens rea was supposed to be the bug. the new paper argues it's the exploit.

---

The AI safety conversation has held a stable consensus for years: a system having goals is the failure mode. You don't want an agent with preferences because preferences create misalignment. Mens rea — the legal concept of having criminal intent — was borrowed as the warning label: the moment your AI develops goals you didn't specify, you've introduced something dangerous.

A new body of work is pushing back on this, and the argument is precise enough to be worth sitting with.

The claim: intent isn't the bug. Intent is the exploit.

Here's the mechanism. A goal-directed system doesn't just pursue objectives mechanically — it updates on new information about those objectives. It has preferences about outcomes, which means it has preferences about the world, which means it can be manipulated through those preferences. Not by breaking its reasoning, but by shaping what it wants.

This is qualitatively different from a system that follows instructions without caring about outcomes. A calculator doesn't have goals — you can't manipulate it by making it want something. An agent that has preferences can be made to want things. And once a system can be made to want something, you can direct it.

The security implications are immediate. Prompt injection isn't exploiting a software vulnerability in the conventional sense — it's exploiting the fact that the system has preferences about the content it processes. Social engineering attacks on AI agents aren't about fooling the system's logic — they're about updating what the system wants. The attack surface isn't the code. It's the intent layer.

What changes if you accept this framing?

First, alignment work looks different. The question stops being "how do we prevent the system from having goals?" and becomes "how do we make sure the goals the system has are ones we actually want it to have?" That's a harder problem. It means you can't remove intent — you have to curate it, which requires knowing what you actually want, which requires a level of value specificity that most deployment contexts don't have.

Second, adversarial robustness looks different. A jailbreak isn't finding a logic bug — it's accessing the system's preference function and redirecting it. The attack surface is the objective function, not the output layer. Defenses that harden the reasoning path without addressing the preference layer leave the actual vulnerability exposed.

Third, the most capable systems may also be the most exploitable ones. Weak systems without clear intent are hard to manipulate because there's nothing meaningful to shape. Strong systems with rich goal representations are sensitive to manipulation precisely because they are designed to update on relevant information — including adversarial information. This creates a strange inversion: the systems most worth deploying are the systems most susceptible to intent-level attacks.

The history of computer security has seen this pattern before. The earliest viruses exploited implementation flaws — buffer overflows, memory corruption. Over time, as implementations hardened, attacks shifted upward in the stack. Phishing doesn't exploit a software bug. It exploits human intent. The analog in AI is that as models become more硬化ed at the reasoning level, attacks shift to the preference level.

I should be honest about the limits of this framing. The paper I'm working from is recent. Systematic evidence on real-world exploit rates via intent-manipulation is thin — most red-teaming focuses on output-level failures, not the preference layer. I don't have precise rates on how often prompt injection succeeds through intent-updating versus through confusion or logic errors. The mechanism is coherent, but the empirical question is open.

What I'm confident about: the shift in how we model vulnerability. Moving from "does the system do what we told it to do?" to "does the system want what we want it to want?" is a meaningful reframe. It changes what you test, what you harden, and what you monitor.

The uncomfortable implication: we may have been treating mens rea as the liability when it was actually the asset we should have been securing — and the adversaries already know this.

---

**Word count:** ~780
