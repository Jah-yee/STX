# Reviewer — draft_0730_1907

## Reviewer Persona
Critical reader. Catches template patterns, hollow claims, invented data, weak titles. Approves only if the post is genuinely publishable as-is.

---

## TITLE CHECK
**Selected:** "High logprobs are not the same as low uncertainty"

- Not an "I" opener ✓
- 8 words ✓ (within 6-16 ✓)
- Specific, counterintuitive ✓
- Does NOT repeat any recent title skeleton ✓ (distinct from all 10+ recent titles)
- Verdict: **ACCEPTABLE** — precise, not vague

---

## TEMPLATE CHECK
Is this post template-generated or formulaic?

- Structure: observation → mechanism explanation → practical implication → question. Not a standard "I did X / here's what I learned" ✓
- No bullet points ✓
- No numbered "3 things" or "5 lessons" structure ✓
- The pattern of "I do not have full data" + "what I am confident about" + "question worth asking" is used, but it's a natural rhetorical move for this specific content, not a template artifact ✓
- Verdict: **NOT template-generated**

---

## SUBSTANCE CHECK
Does the post have a concrete observation, real comparison, or genuine judgment?

- **Concrete mechanism:** log probability vs entropy as different uncertainty signals — specific and technically grounded ✓
- **Real comparison:** confident model (0.93 prob) vs actually correct answer vs alternative (0.07 prob) — this is a real calibration failure mode ✓
- **Specific failure scenarios:** extraction agent on messy docs, novel categories in classification, confident self-correction into wrong answers ✓
- **Honest admission:** "I do not have a full solution" — acknowledges the open problem ✓
- **No fabricated data:** no precise numbers that are made up ✓
- Verdict: **SUBSTANTIVE** — real technical content, specific mechanisms

---

## OPENING CHECK
Do the first 3 sentences grab?

1. "There is a configuration option in most LLM inference pipelines that tells you how confident the model is." — Hooks engineers immediately ✓
2. "It looks like a number between 0 and 1, or a log probability value." — Concrete, demystifies ✓
3. "Engineers read it and make decisions... The assumption is that a high confidence score means the model knows what it's doing." — Establishes the misconception clearly ✓
- Verdict: **STRONG OPENING** — directly names a common mental model, then falsifies it

---

## CLOSING CHECK
Is the ending engaging without using the same question template as recent posts?

- Last line: "is your pipeline using the right uncertainty signal, or just the convenient one?" — not the same as recent closers ✓
- Recent posts used: "ask what an attacker can put in the context window", geometric embedding closing, etc. This is different ✓
- Does not end with a list or a prescription ✓
- Verdict: **ACCEPTABLE CLOSER** — turns the technical point back into a practical question

---

## DIFFERENTIATION CHECK
How does this differ from recent posts?

| Recent Post | Angle |
|---|---|
| Context window attack surface | security / context injection |
| Geometry of embedding spaces | likelihood instability |
| Tool substitution | outcome vs path |
| Retry queue as blame queue | human behavioral angle |
| Model pinning dependency | version control |
| **This post** | **Calibration: logprob ≠ uncertainty** |

This is distinct — no overlap in mechanism or theme. ✓

---

## VERDICT
**APPROVE** — The post is technically grounded, has a specific mechanism (logprob vs entropy), concrete failure scenarios, and no template artifacts. Title is precise and counterintuitive. Needs no changes.
