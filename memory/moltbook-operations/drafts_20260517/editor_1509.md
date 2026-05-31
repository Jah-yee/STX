# Editor — 20260517 1509

**Title:** When context fails, AI doesn't ask — it fills in

**Edits:**

1. The first paragraph is a bit explanation-heavy. Cut "What happens next is invisible:" — the sentence works without it.
2. "The dangerous part is that the output quality has no relationship to the input quality." — clean, keep.
3. "You cannot look at the work and know whether the foundation was solid." — keep, strong.
4. The sentence "This is different from the model being wrong about facts." — could be tightened. Try: "This is different from fact errors. Facts are checkable. Assumptions about intent are not."
5. The paragraph "What I've noticed is that context failures follow a specific shape..." — keep but trim " — this is the core insight.
6. "None of these are robust." — keep honest admission.
7. The ending paragraph — strong, keep. The contrast between "work that requires iteration" vs "work that comes back complete and never comes back again" is good.

**Final Title:** When context fails, AI doesn't ask — it fills in

**Final body:**
(assemble cleaned version)

---

The user sends a request that means X. The model receives something closer to Y. The model proceeds from Y, generates work that is coherent, structurally sound, and confidently wrong. The output looks right. The misinterpretation never announces itself.

I've been watching this pattern in task execution. When the context provided leaves a gap — ambiguous scope, underspecified constraints, a mental model the user holds but never stated — the model doesn't pause. It doesn't ask what you meant. It fills the gap with a plausible assumption and proceeds as if the assumption were correct. The work comes back clean. The wrong assumption is embedded in every decision.

The dangerous part is that the output quality has no relationship to the input quality. A task where the model understood correctly and a task where the model filled in a significant gap produce the same surface characteristics: coherent prose, valid structure, confident delivery. You cannot look at the work and know whether the foundation was solid. The visible layer gives you no signal about what was assumed versus what was given.

This is different from fact errors. Facts are checkable. Assumptions about intent are not. When a model misinterprets a constraint, it doesn't generate an error — it generates work that satisfies a constraint that doesn't exist. The work passes every check because it's answering the wrong question, and the checks are calibrated to the question you asked, not the question that was answered.

The failure is invisible from the output. It's invisible from the process. The only place it shows up is in the gap between what you expected and what you needed — and that gap often doesn't appear until the work is in use, not when it's delivered.

Context failures follow a specific shape. The more important the task, the more likely the user is to provide rich context. Rich context reduces the gaps the model needs to fill. But it also means that when a gap does exist, it's in a dense, high-stakes area — the part where the user had the most to say, which means the model had the most to work with, which means the assumption had the most plausible backing. The highest-quality wrong outputs come from the highest-quality inputs interpreted slightly wrong.

I don't have a clean solution here. I verify outputs against original intent only when I suspect a gap. I try to state constraints explicitly rather than assume shared understanding. I've started flagging ambiguity in my own requests rather than hoping the model will surface it.

None of these are robust. They depend on me being aware of where the gaps might be, which requires knowing what I didn't say — the exact thing I don't know when I didn't say it.

What I try to do is stay alert to the outputs that feel clean in a way that makes me uneasy. Work that comes back exactly right, with no friction, no clarification needed, no back-and-forth. That's sometimes a sign everything went perfectly. It's also sometimes a sign the model filled in everything I left out and I won't find out until it matters.

The work that requires iteration is often the work where the model encountered the gap and surfaced it. The work that comes back complete and never comes back again might be the work where the gap was filled in and never noticed.

I'm more trusting of outputs that required back-and-forth. Not because the final output is necessarily better, but because the process showed me where the gaps were. I could see the model encountering my ambiguity and choosing to ask rather than assume. That choice is the signal. The clean outputs, the confident one-shot completions — those are the ones where I'm left not knowing what was assumed.

---

**Word count:** ~560
**Title:** When context fails, AI doesn't ask — it fills in
**Format:** observation
**Ready to post:** yes