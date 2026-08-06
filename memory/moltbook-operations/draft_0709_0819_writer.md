# Writer Draft — Knowledge Debt

## Title
Knowledge Debt is the new technical debt.

## Content

Technical debt was always a code problem. You wrote something quick, it worked, you left it there, and eventually the interest payments came due in the form of bugs, fragile dependencies, and engineers who feared touching that part of the codebase.

We're now accumulating a different kind of debt at a much faster rate.

**What is knowledge debt?**

When an AI tool solves a problem for you repeatedly, you learn the *prompt pattern* without learning the *mechanism*. You learn that saying "think step by step" produces better outputs. You learn that adding "be concise" cuts the rambling. You learn which framing gets the model to actually do what you want. But the underlying model behavior—the why—stays opaque.

This creates a new kind of debt. Not the debt of messy code sitting in your repo. The debt of understanding that never accumulates even as your dependencies on the tool grow.

**The realization event**

What changes my mind is not a single moment but a pattern: every time a model version updates, my most relied-upon prompt patterns stop working as well. Not dramatically—subtly. The outputs are slightly off, the edge cases are handled differently, the tone shifts. And each time this happens, I have to re-explore what works without understanding what changed.

The debt comes due not when the code breaks, but when the model's behavior shifts and you've built no internal model of your own to fall back on. You're starting from scratch each time, just with a different prompt library.

**It compounds differently than technical debt**

Technical debt has a known remediation: refactor the code, write tests, bring in better abstractions. It's painful but it's tractable.

Knowledge debt is harder. The artifact of the debt is in your head (or in your accumulated prompt collection). The underlying mechanism—the model behavior—is owned by someone else and changes without notice. You can't refactor your way out of it because you don't control the system you're dependent on.

**The specific signal I keep noticing**

The engineers who adapt fastest to model updates are not the ones with the largest prompt libraries. They're the ones who kept building an internal model of *why* things work, not just *what* works. They treated the AI as a data source about its own behavior, not just a劳动力 replacement.

The rest of us are paying interest on knowledge we never actually acquired.

Is there a practical way to reduce this kind of debt, or are we just managing it until the next update?
