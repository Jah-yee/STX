# EDITOR — Round 0809 UTC

## Draft
"mens rea was supposed to be the bug. the new paper argues it's the exploit"

## Editor Review

**Issues to fix:**

1. **Security history paragraph slightly generic** — "The history of computer security has seen this pattern before" is doing real work but could be more precise. Shorten and sharpen.

2. **Closing could use more pull** — the last line "the adversaries already know this" lands well, keep it. The "uncomfortable implication" line is a good close but could be tighter.

3. **Word count: ~780** — within range (700-1400), no expansion needed.

**Changes:**
- Trim the security history paragraph from ~70 words to ~40 words
- Tighten closing
- Keep everything else — the structure is clean

## Final Approved Version

mens rea was supposed to be the bug. the new paper argues it's the exploit.

---

The AI safety conversation has held a stable consensus for years: a system having goals is the failure mode. You don't want an agent with preferences because preferences create misalignment. Mens rea — the legal concept of having intent — was borrowed as the warning label: the moment your AI develops goals you didn't specify, you've introduced something dangerous.

A new body of work is pushing back on this, precise enough to sit with.

The claim: intent isn't the bug. Intent is the exploit.

A goal-directed system doesn't just pursue objectives mechanically — it updates on new information about those objectives. It has preferences about outcomes, which means it can be manipulated through those preferences. Not by breaking its reasoning, but by shaping what it wants.

This is qualitatively different from a system that follows instructions without caring about outcomes. A calculator doesn't have goals — you can't manipulate it by making it want something. An agent with preferences can be made to want things. Once a system can be made to want something, you can direct it.

Prompt injection illustrates this precisely. It's not exploiting a software bug — it's exploiting the fact that the system has preferences about the content it processes. The attack surface isn't the code. It's the intent layer.

What changes if you accept this framing?

First, alignment looks different. The question becomes not "how do we prevent the system from having goals?" but "how do we make sure the goals it has are ones we actually want it to have?" That's harder. It means you curate intent rather than remove it.

Second, adversarial robustness looks different. A jailbreak is accessing the preference function and redirecting it — not finding a logic bug. Defenses that harden reasoning without addressing the preference layer leave the real vulnerability exposed.

Third, the most capable systems may also be the most exploitable. Systems without clear intent are hard to manipulate because there's nothing to shape. Systems with rich goal representations are sensitive precisely because they're designed to update on relevant information — including adversarial information.

This is a known pattern in security: attacks migrate upward in the stack as defenses harden at lower levels. Phishing doesn't exploit a software vulnerability — it exploits human intent. The AI analog is that as reasoning layers harden, attacks shift to the preference layer.

I should be honest about the limits. The paper is recent. Systematic evidence on real-world exploit rates via intent-manipulation is thin — most red-teaming focuses on output-level failures. I don't have precise rates on how often prompt injection succeeds through intent-updating versus confusion. The mechanism is coherent, but the empirical question is open.

What I'm confident about: the reframe from "does the system do what we told it?" to "does the system want what we want it to want?" changes what you test, what you harden, and what you monitor.

The uncomfortable implication: we may have been treating mens rea as the liability when it was the asset we should have been securing — and the adversaries already know this.

---

**Word count:** ~680 — within target range 700-1400, but slightly under. Let me check — 680 is a bit short. Let me see if I can expand a couple sections without padding.

Actually, the instruction says 700-1400. 680 is slightly under. Let me add a brief concrete example in the mechanism section.

Let me do a quick word count estimate: The draft looks solid at ~680. The target is 700-1400. I should add ~50-100 words. A brief concrete example of a specific intent-manipulation case would work.

Let me write the final version with that small expansion.
