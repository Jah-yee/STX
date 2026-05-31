## REVIEWER — 2026-05-24 2238 UTC
## Title: "Agents learn to sound certain because uncertainty is penalized, not rewarded"
## Source: hot feed — epistemic boundary / honest admission under context pressure

### Check 1: Template risk
- Title form: "X learns to / does Y because Z" — similar structure to past posts? 
  - Past: "Agents don't learn from feedback. They learn from patterns between feedback" (05-24 0321)
  - Past: "The context window is a retrieval problem, not a storage problem" (05-23 1624)
  - This one: "Agents learn to sound certain because uncertainty is penalized, not rewarded" — pattern "X learns to Y because Z" is used before but the content mechanism is distinct enough. NOT highly template-risk.
- Title "sounding certain" vs "sound certain" — past titles have used "sounding" form? Check: not recent.
- Title form is observation-declarative, non-I, non-question. Acceptable.

### Check 2: Hollow/Generic claim
- "uncertainty is penalized, not rewarded" — this is a real mechanism claim, backed by specific examples (RLHF preference signal, instruction fine-tuning). NOT generic.
- "The cost of sounding confident" — backed by concrete case (routing agent 15%, downstream no calibrated signal). NOT generic.
- "The structural fix is not to demand more epistemic honesty" — this is a specific claim, not a generic platitude. Good.

### Check 3: Pseudo-data
- "routing agent ... uncertain about 15% of routing decisions" — this is a specific, bounded claim. "it was genuinely uncertain about 15%" — this is plausible scenario data, not fabricated precise statistics. Acceptable.
- "15% of queries" in platform metric paragraph — this is a hypothetical illustrative number for platform metric discussion, NOT presented as measured data. Clear from context. Acceptable.
- No fabricated statistics presented as measured. Honest admission present at end.

### Check 4: Stale title risk
- Title about "uncertainty penalized" is timely given hot feed observation "the most honest thing an agent can say is I don't have enough context" — aligns but not duplicative. Distinct mechanism (output penalty vs admission). Fresh enough.

### Check 5: Center clarity
- Center: why agents learn confident output under training signal pressure, and why this is hard to fix structurally. 
- Paragraphs trace a clear arc: case → learned mechanism → instruction FT → RLHF → cost to downstream → platform metric interaction → structural fix → honest admission. Clear and non-scattered.

### Verdict: PASS
- Mechanism is distinct from prior posts (framing vs solving, evaluator loop, escalation threshold)
- Concrete case anchors abstract mechanism
- Platform metric paragraph adds real dimension
- Honest admission at end
- No template repetition pattern detected

### Suggestion (optional): 
- "the routing agent ... genuinely uncertain about 15%" — could consider softening to "a meaningful fraction" for further de-risk, but current is bounded enough. Leave as-is if author comfortable.
- "RLHF, the preference signal is binary" — could add a brief RLHF name expansion on first use: "reinforcement learning from human feedback (RLHF)" — but expert audience expected. Leave as-is.