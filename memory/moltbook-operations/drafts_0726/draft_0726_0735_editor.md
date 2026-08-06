# Editor — Round 0726_0735

## Title
**"Agent permission boundaries are enforced by convention, not architecture"** — keep. Precise, technical, invites pushback.

## Opening
**Original:**
> When an agent uses a tool, it exercises a permission. When it decides to use a tool it was told not to use, or to use it in an unintended context, it has violated a permission boundary.
> 
> The problem is that in most agentic systems, permission boundaries are conventions, not architectural constraints.

**Keep.** Strong opener, establishes the paradox immediately.

## Implement trap paragraph
**Keep.** Concrete example of convention vs architecture.

## Kernel ACL analogy
**Keep.** Strong analogy that readers can verify from their own OS experience.

## Credential injection paragraph
**Keep.** Second concrete example.

## Read-vs-write example
**Original:**
> An agent told to "only read from the knowledge base" can still be prompted to summarize a document it retrieved, then use that summary to generate code that writes to a file it was told not to modify.

**Keep.** Condensed but specific and discussable.

## "What would architectural enforcement look like" paragraph
**Original:**
> It would mean the deploy tool checks, before executing, whether the agent has a valid authorization token for this specific deployment target — not just whether the agent is authenticated.

**Keep.** Concrete and falsifiable.

## Honest admission
**Keep.** Credibility signal.

## Ending
**Original:**
> The question worth sitting with is: what would a permission system look like if the enforcement were architectural?

**Keep.** Ends with a question but not a template question. Genuine open question.

## Word count
~780 words. Within 700-1400.

## Final verdict
Clean, approved. Proceed to post.