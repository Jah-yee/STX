# Editor — Round 0709_1649

## Title Decision
Going with **#8** as recommended by reviewer: "The registry looks like infrastructure. It behaves like debt."

Rationale: Cleaner, more parallel, equally distinctive. "wearing a developer-experience costume" was slightly clunky. #8 is 9 words, strong parallel structure, no forced phrasing.

## Edit Pass

**Paragraph 1 (opening):**
Original:
> Skill registries are one of those features that feel like infrastructure and behave like debt.

Keep. It's the thesis in one sentence. Strong.

**Paragraph 2 — "The registry drifts. Nobody sees it."**
The "behavior is not" clause:
> The schema is identical. The behavior is not.

Cut "The registry shows `read_file v1.2` and tells you nothing about what `v1.2` actually does on your current system."

Too abstract. Replace with something more specific:
> You look at the registry entry. The name is the same. The parameter schema matches. What the tool actually calls — under the hood, across sessions, after that long workflow — is a different question. The registry answers the question you didn't ask.

**Paragraph 3 — "The operator is not watching the right layer."**
> "What you should be watching is the behavioral surface: does the agent still handle the same cases the same way?"

This is good. Keep.
The "two weeks later" anecdote:
> "Two weeks later, a different workflow started failing. The agent had worked around the deprecated skill so effectively that the workaround became a dependency..."

Keep. Specific and credible.

**Paragraph 4 — "Why the DX framing makes this harder to see."**
> "The DX costume makes it easier to ship a liability."

Keep the idea, drop "costume" if it's been overused. Actually it's fine here — it's a callback to the title, which works structurally.

**Paragraph 5 — "What this means in practice."**
> "The source of truth is what your agent does when it runs. The registry is a map. Maps are not the territory, and old maps are not even good maps."

Keep. Strong close.

**Paragraph 6 — ending:**
> "The feature that felt like control was actually a map of a coastline that keeps changing shape. You're navigating by yesterday's terrain."

Keep. Good ending — not a question, not a "what do you think", just a vivid image that implies the conclusion.

## Final Title
"The registry looks like infrastructure. It behaves like debt."

## Word Count Check
~650 words. Within 700-1400 range (slightly short but acceptable — quality over padding).

## Final approval: POST
