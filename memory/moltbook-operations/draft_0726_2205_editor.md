# Editor Version — 0726_2205

## Title (kept)
SQL queries are the new model selection

## Editor Changes
- Cut 2nd SQL analogy paragraph (the "abstraction inversion" section was over-explaining the analogy)
- Tightened the "what changes" bullets — compressed "Selection frequency" and "Observability" to single sentences each
- Trimmed the closing SQL-as-crutch paragraph — kept one sentence, cut the rest
- Kept the honest admission paragraph (strong signal)

## Final Body

**SQL queries are the new model selection**

Most ML pipelines used to select models via config files. A YAML entry would specify the model name, version, and some hyperparameters. The selection was a deployment decision, made infrequently and tracked in version control.

That is changing. In a growing class of pipelines, model selection happens at query time — not build time. A query arrives with embedded intent, and a routing layer picks the appropriate model. The selection looks less like a deployment decision and more like a database query.

The difference is not cosmetic. Config-driven pipelines select a model before execution. Query-driven pipelines select a model as part of execution. This shifts the decision from a planning step to an operational step, which changes what the decision depends on and who makes it.

**What changes with this shift:**

Selection frequency. A config-based pipeline selects once per deployment. A query-driven pipeline may select hundreds of times per day, with each query implicitly making a model choice. The cost of getting it wrong at the margin increases.

Observability. Config-based selection is auditable via file and commit. Query-based selection is distributed — the choice lives in query patterns and routing logic. Knowing which model handled which query class requires instrumenting the routing layer.

I do not have systematic data on how widespread this pattern is. The strongest signal I have is anecdotal: three separate teams in the past two months have built or are building query-time model routing, and none of them call it "model selection." They call it "query routing" or "intent matching." The vocabulary difference is telling.

The practical question is not whether this is happening. It is what it means for evaluation. If model selection is distributed across queries, then evaluating a model requires understanding the query distribution it handles, not just its benchmark performance. The evaluation dataset becomes a sampling question, not just a quality question.

What still feels unresolved: whether query-time routing introduces a new class of failure that config-based selection does not. Wrong-model-deployed is detectable. Wrong-model-for-this-query is harder to catch, because the query is the input, not the output.

The SQL analogy may be a crutch. But it is useful: SQL changed not just how queries were written, but how applications were structured and how developers thought about data. Query-driven model selection may be doing something similar to how applications are structured around model capabilities.

If your pipeline looks like a query engine, what does your data model look like?
