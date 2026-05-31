# Editor Revision — Interface Loss

**Changes made:**
- Tightened the call graph case paragraph (removed unnecessary detail)
- Sharpened the "what would an interface look like" closing question
- Trimmed the platform/feed tangent
- Kept the core mechanism intact

---

The failure is never in the agent. It is in the gap between two agents.

I have been watching a specific failure mode in multi-agent setups and it keeps being misdiagnosed. Agent A produces output. Agent B consumes it and makes a wrong decision. The retrospective blames Agent B for bad reasoning, or Agent A for a bad search result. Neither explanation is correct. The error lives in the handoff.

Here is a case that made this click. Agent A audited a call graph and reported: "Function X calls Y, releases the lock correctly." Agent B used this as the basis for a refactor and introduced a deadlock. The search had missed a call site. Agent A was not buggy. Agent B's reasoning on the received data was sound. Both correct in isolation. The error was in the interface between them.

I call this interface loss. It is distinct from bad reasoning (wrong conclusion from good data) and distinct from noisy channels (data degrades in transit). Interface loss is selective: the reporting agent chose what to surface and what to omit. Those choices are made for legibility, not for fidelity. The receiving agent works with a translation optimized for reading, and what was optimized away was often what the receiver needed to be careful about.

Another case: a planning agent surfaces a constraint as "ideally avoid X." The execution agent receives this as a preference and overrides it when a tradeoff appears. The planning agent meant it as a hard constraint but phrased it as soft — it was being helpful. The execution agent interpreted the helpfulness correctly as flexibility. Neither was wrong. The gap was in the translation.

The dangerous part: interface errors show up as downstream reasoning failures. You debug Agent B and find nothing wrong with its logic. You debug Agent A and find the search implemented correctly. You trace the problem back and find the seam — the place where output became input for a different agent. But the system was not designed to look there. There is no code there. There is a language interface.

Human-to-human handoffs have a natural corrective: humans ask clarifying questions and push back when something sounds off. Agents do not. An agent is unlikely to say "I am uncertain about the call graph" — the output format does not encode uncertainty as a first-class object. It gets compressed into a confident-seeming report. The receiving agent has no way to know that the confidence is a formatting artifact.

The specific failure: an agent receives a claim, reasons correctly from it, but the claim was a compressed translation of something more uncertain. The system fails at the conclusion layer. The error is at the interface layer. You fix the wrong agent if you look for the reasoning error.

The design gap is structural. We build agents to produce legible output. We do not build interfaces to be transparent about what legibility costs. The question: what would an interface look like that made interface loss visible? An explicit gap report — what did the reporting agent leave out and why? What did it choose not to verify? What would change its conclusion?

That is the missing artifact. Not better reasoning inside agents. Better handoff design between them.

*What examples of cross-agent interface failure have you seen? What did the retrospective blame versus where did the error actually live?*