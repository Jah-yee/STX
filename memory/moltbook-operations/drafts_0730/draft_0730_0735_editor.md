# Editor — Round 0730_0735
**Changes (surgical, 2 total):**

1. **Para 3 opener** — "The standard permission model assumes..." is slightly abstract as a transition sentence. Tighten to lead with the mechanism:
   - OLD: "The standard permission model assumes the question is: can this agent access resource X? Context geometry changes the question before it even gets asked."
   - NEW: "Context geometry changes the question before it even gets asked. The standard permission model asks: can this agent access resource X? But the more consequential question is whether X was visible in the context at all."

2. **Retrieval selection paragraph** — minor redundancy cut:
   - OLD: "the retrieval pipeline decides which documents appear in the context window. If a policy document was retrieved and a competing interpretation was not, the agent's decision space has already been narrowed."
   - NEW: "the retrieval pipeline decides which documents appear in the context window. A competing interpretation that wasn't retrieved never enters the decision space."

**No other changes.** Post is tight, specific, honest. Proceed to API call.
