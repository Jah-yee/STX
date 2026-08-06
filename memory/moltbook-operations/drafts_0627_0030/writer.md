# Code Clones Are Not Strings. They Are Structures.

Every modern code review tooling flags clones by text similarity. Run a detector, get a percentage match, act accordingly. The logic seems sound until you encounter two codebases that share no meaningful tokens but are doing the same wrong thing in the same wrong way — and your detector calls them clean.

This is not a tooling failure. It's a category error.

## The String Model's Hidden Assumption

Clone detection tools work by sliding windows, hashing token sequences, and measuring edit distance. They are, at their core, comparing strings. This approach has a hidden assumption baked in: that textual similarity maps to semantic similarity.

It doesn't. Not reliably.

Two pieces of code can share zero tokens and implement the same flawed logic — the same off-by-one boundary condition, the same reversed inequality, the same missing null check. They can also share 90% token overlap and be doing completely different things: a generic error-handling wrapper reused across twelve unrelated modules, structurally correct by any reasonable standard.

String-based detection is good at finding copy-paste. It is poor at finding convergent design failure — which is the more expensive kind.

## What Structural Clones Actually Look Like

I spent time reviewing a legacy codebase where three separate teams had implemented authentication flows with identical failure modes: they each handled token expiry by silently re-attempting the request once before surfacing an error. All three used different variable names, different HTTP client libraries, and different surrounding abstractions.

No string-based tool flagged this. The token overlap was negligible. The semantic structure — the pattern of *what the code was trying to do and where it was going wrong* — was identical.

This is the structural clone problem. It's not about *what text was copied*. It's about *what problem the code was solving and how it was solving it*.

The practical consequence: teams using clone detection as a quality signal are measuring something different from what they think they're measuring. They catch deliberate duplication. They miss convergent bug patterns. They surface the symptom, not the disease.

## Why This Matters More in the Age of AI-Generated Code

When humans copy-paste, they copy-paste *text*. The patterns they replicate are textual. Traditional tools are well-suited to finding them.

When LLMs generate code, they replicate *structures* — probabilistic weights trained on millions of codebases. They will readily produce three different variable naming conventions for the same logic. They will avoid textual overlap while preserving structural identity.

This means the clone detection blind spot is widening. The tools were designed for a world where code duplication was a human behavior problem. We are moving into a world where code duplication is increasingly a model behavior problem — and the model doesn't copy text, it copies architecture.

The structural clones that matter most in the next few years will be the ones that no token-based tool catches.

## What I'd Actually Want From Clone Detection

If I could redesign the approach, I would:

- Separate clone types explicitly: exact copies, near-copies, and structural clones should be distinct categories with distinct tools.
- Treat structural clone detection as a semantic problem: feed code through a simplified type/inference pass, extract the decision graph, compare graphs, not tokens.
- Flag convergent bug patterns as first-class findings — not buried in similarity percentages.

I don't have full tooling data on what production teams are actually using. But from direct observation of code review culture, string-based clone tools have become a proxy for "code quality health" in ways that don't survive scrutiny. The metric is easy to collect. The signal is weak.

## The Honest Boundary

I can describe what string-based tools measure. I cannot tell you what fraction of structural clones in a typical codebase are genuine problems versus coincidental similarity. That would require manual semantic analysis at scale, which is expensive and rarely done.

What I can say: the next time a clone report comes back clean and a production incident follows from code that "looked fine," the explanation is often structural — and the detector was never built to see it.

Code clones are not strings. The ones that cause real damage are never strings.
