# EDITOR — Agent Evals Measure Failure Because Failure Has a Shape. Success Doesn't.

## Editor Changes

### Change 1: Opening paragraph — trim fat
**Before:** "You run an eval. Your agent scores 94. What does that number tell you?" + 4 sentences of setup.
**Change:** Collapse to: "You run an eval. Your agent scores 94. What does that number tell you? That out of every failure mode your eval probes, the agent handled 94% of them. It tells you nothing about the failures your eval didn't probe — and nothing about whether the agent handled those cases with genuine capability or just the right memorized pattern."

**Rationale:** Same opening hook, tighter delivery. Removes a filler sentence.

### Change 2: "Geometry of Failure" section — trim middle redundancy
**Before:** "Failure has structure. It breaks in reproducible ways. It runs into edge cases that follow logic. When an agent mishandles a null response from a tool..." [3 sentences of examples].
**Change:** Keep only: "Failure has structure. It breaks in reproducible ways. When an agent mishandles a null response from a tool, or hallucinates a field that doesn't exist in the schema, or fails to retry after a timeout — these are failures with shapes. You can detect them, catalog them, write a test for them, and watch them go green."

**Rationale:** Examples sufficient, no need for the "follows logic" sentence that adds nothing.

### Change 3: Closing — strengthen the question worth asking
**Before:** "The question worth asking is not 'does my agent pass the eval?' but 'which failures did I skip when writing the eval?'"
**Change:** Keep but add one line before: "Most eval suites are honest maps of what the designer imagined failure to look like. The question worth asking is not 'does my agent pass?' but 'which failures did I fail to imagine?'"

**Rationale:** Makes the distinction sharper before the question.

## Final Word Count: ~850 words
## Title: Agent Evals Measure Failure Because Failure Has a Shape. Success Doesn't.
