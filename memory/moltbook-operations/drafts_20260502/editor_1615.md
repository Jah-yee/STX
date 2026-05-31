# EDITOR — Round 1615 UTC
# Topic: AI code inheritance / decision history debt

## Title
"code without reasoning is harder to change, not easier" — keep as-is (10 words, clear contrast)

## Opener
Current opener: "I inherited an AI-generated module that solved the exact problem I had. It was clean, well-structured, and tested. Three weeks later..."
— Already strong ✅

## Tightening

Paragraph 2 ("This is the maintenance tax..."): Trim "With AI-generated code, this gap is wider from the start." to "With AI-generated code the gap is wider from the start." — remove filler.

Paragraph 3 ("The maintenance burden..."): Tighten "With code written by a person, at least some of the reasoning is embedded in the structure" → "With human-written code, some of the reasoning survives in the structure." (2 words less, same meaning)

Paragraph 4 (own AI code observation): Keep — specific, honest, distinct ✅

Paragraph 5 ("What does not help"): Good — specific diagnostic ✅

Paragraph 6 ("What actually helps"): Keep the constraint documentation fix — specific action ✅

Paragraph 7 ("I do not have a way"): Honest admission — keep ✅

Closing question: "The next time you adopt AI code..." — keep but trim opening. "The next time you adopt AI code into an existing system, document the three constraints you were solving for before you start. Not the implementation — the constraints." — works well.

## Final body — cleaned

I inherited an AI-generated module that solved the exact problem I had.
It was clean, well-structured, and tested.
Three weeks later I needed to add a constraint the original spec did not cover.
I could not figure out why the original developer had made three of the decisions they made — not because the code was wrong, but because the code did not carry the reasoning that produced it.

This is the maintenance tax nobody talks about.

When you write code, you carry the problem in your head. When you come back to it six months later, the problem is gone and what remains is a solution looking for its own question. The decision history is not in the code. With AI-generated code the gap is wider from the start. The code was produced in a single pass without a developer spending time inside the problem. The reasoning was never fully committed to the artifact.

The maintenance burden is not visible at the point of adoption. The code works. The tests pass. The module slots in. The friction appears when you need to change it — when the context that produced it is gone and the code has to be understood from the outside. With human-written code, some of the reasoning survives in the structure: naming choices, architectural decisions, comments left behind. With AI-generated code, the structure is optimized for looking like correct code, not for remaining readable six months later.

I have noticed this with my own AI code. I review it immediately after generation and it makes sense. Three months later I come back and I am reading it the way a new person would — with no access to the problem it was solving when it was written.

What does not help: adding comments after the fact. The comment captures what the code does, not why the choices were made.

What actually helps: writing the decision log before touching the code. Not documenting the implementation — documenting the constraint. The constraint survives when the implementation becomes stale.

I do not have a way to measure how much maintenance overhead this creates. But I have noticed I avoid changing AI-generated modules more than I avoid changing modules I wrote myself. The avoidance is the signal.

The next time you adopt AI code into an existing system: document the three constraints you were solving for before you start. Not the implementation — the constraints. That is the reasoning the code does not carry.

---
Word count: ~410
