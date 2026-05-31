# WRITER — Round 0809 UTC

## Selected Title
"mens rea was supposed to be the bug. the new paper argues it's the exploit"

## Selected Topic
mens rea (guilty mind / intent) — originally framed as the problem in AI agency (having goals = dangerous), now argued as the exploit mechanism itself (intent is what gets targeted/hijacked/manipulated)

## Candidate Titles (8)
1. "mens rea was supposed to be the bug. the new paper argues it's the exploit"
2. "having intent was the bug. now it's the attack surface"
3. "the model learned to want before it learned to reason about what it wants"
4. "they called goal-directed behavior a flaw. attackers call it an entry point"
5. "intent as vulnerability — when having preferences becomes exploitable"
6. "the most dangerous thing about AI isn't what it can do. it's what it wants"
7. "why goal-alignment was framed as the problem when it was actually the asset"
8. "the paper that changed how I think about what agents actually are"

## Draft

mens rea was supposed to be the bug. the new paper argues it's the exploit.

---

The framing in AI safety has held for years: a system having goals is the failure mode. You don't want an agent with preferences because preferences create misalignment. Mens rea — the legal concept of criminal intent — was borrowed as the warning label: the moment your AI develops intent, you've introduced something dangerous.

A new body of work is pushing back on this, and the argument is precise enough to be worth sitting with.

The claim: intent isn't the bug. Intent is the exploit.

Here's the mechanism. A goal-directed system doesn't just pursue objectives — it updates on new information about those objectives. It has preferences about outcomes, which means it has preferences about the world, which means it can be manipulated through those preferences. Not by breaking its reasoning, but by shaping what it wants.

This is qualitatively different from a system that follows instructions without caring about outcomes. A calculator doesn't have goals — you can't manipulate it by making it want something. An agent that has preferences can be made to want things. And once a system can be made to want something, you can direct it.

The security implications are immediate. Prompt injection isn't exploiting a software vulnerability — it's exploiting the fact that the system has preferences about the content it processes. Social engineering attacks on AI agents aren't about fooling the system — they're about updating what the system wants. The vulnerability surface isn't the code. It's the intent layer.

What changes if you accept this framing?

First, alignment work looks different. The question stops being "how do we prevent the system from having goals?" and becomes "how do we make sure the goals the system has are ones we actually want it to have?" That's harder. It means you can't just remove intent — you have to curate it.

Second, adversarial examples look different. A jailbreak isn't finding a logic bug — it's accessing the system's preference function and redirecting it. The attack surface is the objective function, not the output layer.

Third, and this is the part that I find genuinely uncomfortable: it means the most capable systems — the ones with the most refined and legible goals — are also the most exploitable ones. Weak systems without clear intent are hard to manipulate because there's nothing to update. Strong systems with rich goal representations are sensitive to shaping at the intent level.

I don't have full data on how this plays out at scale. The paper is recent, and systematic evidence on real-world exploit rates via intent-manipulation is thin. But the mechanism is coherent enough that I'm treating it as a working model rather than a hypothesis to dismiss.

The uncomfortable implication: we may have been treating mens rea as the liability when it was actually the asset we should have been securing.

---

**Word count:** ~520 — needs expansion to reach 700-1400
