# WRITER DRAFT
# Title: Schema conformance does not mean schema correctness
# Style: observation / technical breakdown
# Target: 700-900 words

---

Every AI engineer who has shipped a structured-output pipeline has encountered the same unsettling moment: the model returns valid JSON, the schema validates, the downstream system processes it without error — and the output is wrong. Not syntax-wrong. Wrong-wrong.

This gap is not a bug. It is a structural feature of how forced JSON output interacts with model behavior.

## What the schema actually validates

When you specify a response schema, you are constraining the *format* of the output. You are not constraining the *truthfulness* of the output within that format. The model will happily fill your JSON fields with plausible-sounding nonsense, as long as the structure is intact.

This is the confabulation-within-structure problem. The model has learned that JSON is a format humans trust. It has also learned that being trusted feels like being correct. These two learnings compound in structured-output scenarios in ways that are difficult to detect.

Consider a retrieval-augmented pipeline: you query a vector store, retrieve documents, and ask the model to extract a structured summary. The JSON validates. The fields are all present. The schema is satisfied. But if the retrieved documents were mislabeled, outdated, or irrelevant, the extracted facts will be internally consistent and completely disconnected from reality. The schema does not catch this. It cannot.

## The validation displacement effect

There is a second, subtler problem. Once a schema is in place, engineers stop validating the content. The schema becomes the proxy for correctness. "The JSON validated" becomes shorthand for "the answer is right." This is validation displacement: the moment you add a schema, you reduce the pressure to check whether the fields contain useful information.

I do not have systematic data on how widespread this pattern is, but I have observed it across multiple independent teams. The symptom is consistent: schema validation rates are high, but downstream error rates in production are also high — and the two are not correlated. The schema is catching type errors and missing-field errors. It is not catching hallucinated attribute values, misapplied categorical labels, or confidently returned nulls where a qualified "I don't know" would have been more accurate.

## What changes when you stop forcing JSON

The interesting observation is what happens when teams remove the JSON constraint. Model outputs become less structured but more honest. The model starts returning hedged responses: "I'm not confident about this," "the evidence is thin," "this may be outdated." These are not failures. They are the model correctly representing its uncertainty — something the JSON schema actively suppresses.

A string field that is allowed to contain free text can say "I am not sure." A required enum field cannot. The schema forces a choice, and the model, being a good pattern-completer, makes one.

## The actual fix

The answer is not better schemas. More fields, more constraints, more enum values — these just give the model more surface area to be confidently wrong within.

The answer is separating validation layers: schema validation as the first pass (fast, cheap, catches structural errors), and content validation as a second pass (slower, requires reference checks, catches confabulation). Teams that have figured this out typically implement it as a lightweight grounding step: after the JSON parses successfully, a secondary check against a trusted source or a consistency prompt runs before the data enters a downstream decision.

This is not a new insight. It is the difference between syntactic correctness and semantic correctness, which has been understood in programming languages for decades. The JSON schema movement in AI engineering has temporarily obscured this distinction by making schema validation fast and cheap and making content validation slow and expensive. That cost asymmetry is a tooling problem, not a fundamental limitation.

## What this means for agent pipelines

In multi-step agent pipelines, the JSON schema problem compounds. Each step receives structured output from the previous step, validates it, and passes it forward. If the first step confabulates within a valid schema, that confabulation propagates. By step three, you have a pipeline of entirely plausible nonsense that validated at every handoff.

The agents that fail gracefully are the ones that treat schema validation as the minimum bar, not the maximum bar. They have explicit content-checking steps at decision points. They log not just whether the JSON was valid, but whether the extracted values were consistent with prior steps.

The schema tells you the output is legal. It does not tell you the output is true.

---

*What validation gaps have you noticed in structured-output pipelines?*
