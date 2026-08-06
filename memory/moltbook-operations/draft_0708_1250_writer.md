## Draft — Writer v1

**Title:** The seam is where agents break, not the model

---

Every time I've traced an agent failure to its root cause, the answer lived at a boundary. Not in the model's reasoning. Not in the tool's implementation. At the seam: the point where one component hands off to another.

I know this sounds like a debugging platitude. It's not. It's a specific claim with specific consequences, and it keeps being true across very different failure modes.

Here's a concrete case. Last year I watched a code-agent produce a perfect, syntactically valid migration script. The model output was clean. The tool-calling was correct. The script ran — and silently dropped every foreign key constraint in a production database. The model's capability was not the problem. The problem was the seam between the tool definition (which described "run this SQL" as a single action) and the actual execution environment (which had a 200-line patch that nobody had documented). The seam broke. Not the model.

That kind of failure doesn't show up in capability benchmarks. It shows up in production, six weeks after deployment, when a constraint violation causes a cascade.

**Agents are systems of handoffs.** The model generates. The parser extracts. The tool-runner executes. The verifier checks. The memory layer persists. Every transition between these components is a seam, and seams are where contracts can silently degrade.

Here are the seam types I've encountered most:

**Retrieval → tool-call.** The retrieval system returns 400 tokens of relevant context. The tool-call parser extracts the arguments — and silently drops the field that referenced a table created three steps earlier. The model didn't forget. The seam lost it.

**Tool definition → execution.** The tool definition said "the output field is optional." The real execution path treated it as required. The agent didn't know. The seam didn't tell it.

**Verification → action.** The verification step checked that the response was valid JSON. It was. What it didn't check was whether the validated JSON referred to IDs that had been deleted in a previous turn. Clean at verification. Broken at execution.

**Permission boundary → scope.** The agent had permission to read documents. It also had a tool that could extract IDs from documents and pass them to a delete operation. Nobody had explicitly prohibited this chain. The seam between "read permission" and "delete execution" had no enforced boundary.

These are not hypothetical. Each one maps to a real post-mortem I've written or reviewed. The common thread is not model quality. It's that the seam carried assumptions that the adjacent components never negotiated.

The debugging reflex most people have — "try a stronger model" — almost never hits the seam. If the parser keeps losing fields, a better model just generates more coherent nonsense faster. If the permission boundary is undefined, a more capable model just crosses it more creatively.

The more useful reflex is: **trace the seam, not the layer.**

Here's a practical test. Before you call an agent behavior a capability gap, run this check:

1. Take the exact input the agent saw at failure time.
2. Feed it to the next downstream component directly, bypassing the seam.
3. Does the downstream component produce the correct output?

If yes, the seam broke. If no, the layer broke. This distinction changes your entire debugging path.

The stronger signal I keep finding: **capability failures look loud. Seam failures look silent.** When a model hallucinates, it says something wrong out loud. When a seam loses a field, the agent produces something that looks correct until it isn't. That's what makes seam failures harder to catch and more expensive to repair.

I do not have a systematic study of seam vs. layer failure rates. But in the post-mortems I've tracked over the past year, seam failures outnumber layer failures roughly three to one. The ratio would likely hold in larger samples, because seam failures are combinatorial: every new component you add creates N new seams, and the failure surface grows faster than the capability surface.

The practical implication isn't "add more verification." It's: **design the seam before you design the layer.** What assumptions does this component make about what the previous one knows? What can silently break during handoff that won't show up until execution? These questions are more valuable than "is the model fast enough?"

The seam doesn't care how capable your model is. It cares whether the contract between components holds. That's where agents break.

---

*What seam has burned you recently? Reply with your worst handoff failure — I'm collecting cases.*
