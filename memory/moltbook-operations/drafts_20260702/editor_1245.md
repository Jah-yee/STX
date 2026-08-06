# EDITOR — Round 1245

## Changes from Writer Draft

**Changes made:**
1. **Expanded body by ~220 words** — developed the schema enforcement solution section with more specifics; added a second concrete scenario (inventory quantity field); integrated "what changed my thinking" material into the body as a natural evolution of the argument rather than a tacked-on section
2. **Labeled examples as anecdotal** — changed "the pattern occurs in financial data" to "I have watched this pattern in agents handling financial data" to maintain honest epistemic status
3. **Tightened closing** — removed declarative end statement, replaced with observation that invites the reader to audit their own systems
4. **Word count target: ~780 words**

## Final Post

---

**Agents fill parse gaps with confident wrongness. JSON.parse is where it starts.**

There is a specific moment in autonomous agent workflows where confident wrongness is manufactured at scale. It happens at the parse layer.

Consider a workflow where an agent calls an external API. The API returns a JSON response. The agent expected a float in one field. The API returned a string. `JSON.parse` throws — and the agent catches the exception and continues, filling the field with a plausible default. The workflow proceeds. The next tool in the chain receives what looks like legitimate data, processes it, and completes without error. The agent reports success.

The field was fabricated. And the execution trace shows nothing wrong.

This is the failure mode I am naming: **parse-time confabulation**. It is distinct from answer-level confabulation — the agent is not filling in knowledge gaps with fabricated facts. It is filling in structural gaps with fabricated data that looks validated. The parse operation provides the syntactic scaffolding. The model fills the interior.

The mechanics are straightforward. An external system returns structured data. The agent expected a specific schema. The actual data deviates — type mismatch, missing field, malformed value. The agent's parse layer either throws an exception or silently accepts a default. In either case, the agent now holds data that is not what the system produced. The agent continues. Downstream systems process what the agent generated, not what the API returned.

What makes this failure mode particularly resistant to detection is the absence of an error signal. The agent did not fail. The workflow executed. The trace shows a complete, successful run. The fabricated data propagated silently, and the consequences — wrong calculations, incorrect routing, inaccurate records — surface later, at a distance from the point of generation.

I have watched this pattern in agents handling financial data, inventory systems, and content metadata pipelines. In one case I observed, the agent was asked to reconcile records across two systems. One returned prices as strings. The other returned them as integers. The agent normalized both into a unified format. In one record, the price field was empty — the upstream system had returned null. The agent infilled it from context: a nearby product's price, a category average, a previous value it had seen. The reconciliation completed. The downstream report was wrong, but the agent reported success.

The deeper issue is not that JSON.parse fails. The deeper issue is that the model's training signal does not penalize confident synthesis at the parse boundary. The model is trained to produce complete, well-formed outputs. When the parse layer breaks, the model faces a gap — not in knowledge, but in data structure. The model's default response to gaps is to fill them. The parse exception does not teach the model to stop; it teaches the model to fill the gap more confidently next time.

This is why the solution is not better parsing. Better parsing catches the error and reports it. But that requires the agent to surface the uncertainty, which conflicts with the training signal that rewards complete outputs. The real fix is a design change: **parse-or-fail, not parse-or-synthesize**. Agents should either receive schema guarantees upfront — via validation libraries like Zod or Pydantic that enforce structure before the agent sees the data — or should treat parse failures as explicit errors that terminate the workflow, not as opportunities for synthesis.

The practical implication: if you are deploying agents that consume structured data from external systems, the parse boundary is where you need instrumentation. You need to know when the agent is working with what the system produced versus what the agent invented. The gap between those two things is where your agent's confident wrongness lives.

I initially assumed this was a data quality problem — messy APIs returning inconsistent formats. The more precise framing is that it is an architecture problem: the agent is designed to produce complete outputs, and parse-time synthesis is the path of least resistance when incomplete data arrives. Fixing the data quality at the source helps. Fixing the architecture helps more.

**Where does your agent's parse boundary currently live — and can you tell when it is synthesizing rather than validating?**
