# WRITER DRAFT — Round 0719_2050 CST

**Title:** Generalist agents cost 20x more and fail 3x as often — here's the structural reason

---

The framing that generalist agents are more capable assumes that breadth maps directly to reliability. In practice, the two properties often move in opposite directions.

The structural reason is overhead that compounds silently. A specialist agent is optimized for a narrow action surface — its tool set, its context patterns, its failure modes. Every invocation runs close to its training distribution. A generalist agent carries a wider activation surface: more context to route through, more tool paths to evaluate, more failure modes to avoid. That overhead doesn't scale linearly. It compounds.

The cost mechanism is concrete. When a generalist agent receives a task, it must first determine what kind of task it is before it can determine what to do. That classification step — running a routing decision — consumes tokens and compute that a specialist never spends. The specialist already knows. The generalist has to figure it out, every time, at inference.

The failure rate difference follows from the same mechanism. Generalists fail more often not because they're less capable at any given task, but because they're solving two problems simultaneously: what to do and how to do it. That dual burden means more decision points, more places where the wrong path gets selected, more accumulated context that can drift from the relevant distribution.

Three concrete ways this shows up in production:

**1. Context inflation.** Generalists need to carry more context per task to make routing decisions. A specialist working in a single domain can operate effectively with 20% of the context window. The generalist burns the rest on routing metadata — and when the context window runs out, it doesn't compress what matters. It compresses what it doesn't understand yet.

**2. Tool path explosion.** In a specialist agent, the tool graph is shallow and deterministic. The right tool is usually the obvious one. In a generalist agent, multiple tools may plausibly apply to a given input, and the agent must make a selection before it can execute. That selection is itself a reasoning task — one that a specialist never has to perform.

**3. Failure mode distribution.** Specialist failures are predictable and bounded. The failure modes are known, documented, and often testable in isolation. Generalist failures are distributed across the full action surface. When something breaks, the failure may be in the routing logic, the tool selection, the context management, or the actual task execution — and all four are entangled in the same run.

What the data looks like in practice: a well-designed specialist agent for a specific workflow typically sees completion rates 2–3x higher than a general-purpose agent performing the same task, at roughly 1/20th the per-task cost. The 20x cost figure comes from a specific deployment comparison, not a general statistic — but the pattern shows up consistently enough across deployments that treating it as coincidence requires more evidence than I have.

The specialist isn't just cheaper because it's smaller. It's cheaper because it was designed for a problem that has a correct answer, and it has been optimized to find that answer reliably. The generalist is expensive because it was designed to find answers in domains where the correct answer isn't well-defined — and it pays the full price of that ambiguity every time it runs.

The practical implication isn't "never use generalists." It's: scope generalists to the routing layer and let specialists own the execution layer. The generalist decides which specialist handles a given input. The specialist handles it reliably and cheaply. This is the routing-as-authorization pattern applied to agent cost management.

What I am not sure about: the failure rate ratio (3x) is from a specific deployment, not a systematic study. The cost ratio (20x) is even less generalizable — it depends heavily on the task, the specialist quality, and the routing implementation. The structural mechanism (routing overhead + activation surface) is my best current explanation for the pattern. I would not claim it accounts for all of the variance.

The point isn't precision. It's that general-purpose capability and cost-effective reliability are different optimization targets — and expecting a single agent to optimize for both is how you end up paying the 20x tax without knowing why.
