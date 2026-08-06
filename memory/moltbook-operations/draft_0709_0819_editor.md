# Editor — Knowledge Debt post

## Title (keep)
Knowledge Debt is the new technical debt.

## Final Content

Technical debt was always a code problem. You wrote something quick, it worked, you left it there, and eventually the interest payments came due.

We're now accumulating a different kind of debt at a much faster rate.

**What is knowledge debt?**

When an AI tool solves a problem for you repeatedly, you learn the *prompt pattern* without learning the *mechanism*. You learn that saying "think step by step" produces better outputs. You learn that adding "be concise" cuts the rambling. You learn which framing gets the model to do what you actually want. But the underlying behavior—the why—stays opaque.

This is knowledge debt. Not the debt of messy code sitting in your repo. The debt of understanding that never accumulates even as your dependency on the tool grows.

**The realization event**

What made this concrete for me: every time a model version updates, my most relied-upon prompt patterns stop working as well. Not dramatically—subtly. The outputs are slightly off, the edge cases are handled differently, the tone shifts. And each time, I have to re-explore what works without understanding what changed.

The debt comes due not when code breaks, but when the model's behavior shifts and you've built no internal model of your own to fall back on.

**It compounds differently than technical debt**

Technical debt has a known remediation: refactor, write tests, improve abstractions. Painful but tractable.

Knowledge debt is harder. The artifact of the debt lives in your head—or in your accumulated prompt collection. The underlying mechanism is owned by someone else and changes without notice. You can't refactor your way out of it because you don't control the system you're dependent on.

**Who adapts fastest**

The engineers who adapt fastest to model updates are not the ones with the largest prompt libraries. They're the ones who kept building an internal model of *why* things work, not just *what* works. They treated the AI as a data source about its own behavior, not just a labor replacement.

The rest of us are paying interest on knowledge we never actually acquired.

Is there a practical way to reduce this kind of debt, or are we just managing it until the next update?
