# Editor — Round 0806_2246

## Editor changes (surgical)

### 1. Opening — tighten
**Original:** "The imitation learning literature has a consistency problem nobody wants to talk about directly. It assumes a single gold-standard trajectory."

**Cut to:** "The imitation learning literature assumes a single gold-standard trajectory. This assumption does not describe any real deployment I can think of."

Rationale: Two sentences where one did the work. Cut the "consistency problem nobody wants to talk about" framing — it's defensive and slightly vague.

---

### 2. Medical/robotics examples — compress
**Original:** "In medical automation, the 'expert' is often a committee with a documented disagreement rate. In robotic manipulation, you have teleoperators who are both skilled and fatigued."

**Cut to:** "In medical automation, the expert is a committee with a documented disagreement rate. In robotic manipulation, you have teleoperators who are skilled and fatigued — and the difference matters."

Rationale: Cleaner parallel structure. Removes quote marks around "expert" that were doing unnecessary work.

---

### 3. MEGA-DAgger paragraph — tighten the scenario-specific part
**Original:** "The scenario-specific part is where it gets non-obvious. If you use a global accuracy metric to evaluate a multi-scenario policy, you will resolve conflicts in favor of the demonstrator who happens to be most accurate on average — not the one who is most accurate in the scenario that is currently active."

**Cut to:** "The scenario-specific part is the non-obvious part. A global accuracy metric resolves conflicts in favor of the demonstrator who was most accurate on average — not the one who was most accurate in the scenario that is currently active. These can diverge significantly."

Rationale: "These can diverge significantly" already appears later — move it up to close the paragraph cleanly.

---

### 4. Process metric paragraph — trim redundancy
**Original:** "A policy trained on outcome metrics learns to replicate the output. A policy trained on process metrics can learn to handle cases the demonstrator never encountered, because it has learned the structural pattern rather than the specific trajectory."

**Cut to:** "An outcome metric trains the policy to replicate the output. A process metric trains it to handle cases the demonstrator never encountered — because it has learned the structural pattern, not the specific trajectory."

Rationale: "This is not a small difference" is a judgment call that follows from the distinction itself. Let the reader draw the conclusion.

---

### 5. Closing admission — keep but tighten
**Original:** "The honest version of this post would say: I do not have systematic data on how often this specific failure mode..."

**Cut to:** "I do not have systematic data on how often this failure mode — reproducible systematic error from a noisy-demonstrator policy — occurs in deployed systems. I have seen it in my own work and in published cases where teams looked at expert disagreement data and asked what the metric was actually measuring."

Rationale: The "honest version of this post would say" framing is slightly meta and weakens the admission. Just state it directly.

---

### 6. Final paragraph — final statement already clean
"The metric is not a detail. It is the architecture." — Keep as is. Strong close.

---

## Final word count
~780 words. Within target range (700-1400). Single mechanism cluster throughout. No filler.
