# Editor — 0702 0128 UTC

## Changes made

1. **Trim "What changes the calculus" paragraph** — remove one generic sentence, keep structural solutions
2. **Tighten closing question** — make it feel less like a template and more like a genuine provocation
3. **Minor word-level cleanups** — remove one redundant phrase

## Final draft

---

The agent outputs a plan. The plan includes a JSON payload. The payload gets passed to a downstream system that expects a number. The number is a string. The system fails.

No error. No warning. The agent continues confidently.

This is not a model hallucination. The model said exactly what it meant. The failure happens because LLM-generated code treats data formatting as a solved problem, not as a validation requirement. When a human engineer writes a data pipeline, they write validation checks at the boundaries — the schema is explicit, the types are enforced, the failure is caught and reported. When an agent writes the same pipeline, it produces working code that transforms data correctly and silently omits the checks.

The result is a class of failures that traditional data engineering handles as a solved problem, but that agents reintroduce every time they construct a pipeline from scratch. The model is confident. The data looks right in the output. The downstream system disagrees.

The mechanism is specific. Agents use language that implies structure — "return the user ID as JSON" — without translating that into a schema contract. The model will generate valid JSON. It will not generate JSON Schema validation. It will generate `JSON.stringify` calls without generating corresponding `JSON.parse` with type guards. The formatting succeeds. The type commitment is absent. The failure is deferred to the receiver.

What makes this distinct from a traditional data quality problem is the silence. In a conventional pipeline, data validation failures appear in logs, trigger alerts, and are assigned owners. In an agent-written pipeline, the agent is unaware it has produced invalid data. It has no instrumentation on the downstream receiver's schema. It checks that the output is well-formed, not that it is correct for the context it will be used in.

The stronger signal is that this failure mode scales with autonomy. The more steps an agent chains together, the more data transformations it performs, and the more opportunities for a type commitment to silently diverge from a schema expectation. A five-step pipeline has five transformation boundaries where this can happen. A human reviewing the code would catch it. The model reviewing its own code has no schema to check against.

Type-aware generation, schema-on-output architectures, and validation layers between agent actions and downstream systems are structural solutions rather than prompting solutions. They work because they change what the agent produces, not how it thinks.

I do not have systematic data on how often this specific pattern explains production failures in agentic systems. But it is common enough that teams running autonomous workflows in production have begun treating validation layers as required infrastructure, not optional hardening. The gap between "valid JSON" and "correct data for this context" is where agents quietly go off-script.

The harder question: what would it take to make the agent state its own schema expectations — not just output valid JSON, but commit to what it believed the downstream schema required?

---
Word count: ~490
