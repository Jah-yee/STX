## Editor — draft_0608_0943

**Title:** RLHF trains the attractor, not just the behavior (keep — specific, mechanism-first, no changes needed)

---

### Opening — compressed

**Before:**
"When I started reading about RLHF, the framing was straightforward: you reward certain behaviors, the model learns those behaviors. A human preference signal gets converted into a policy gradient, the policy updates, and the model does more of the thing you liked."

**After:**
"RLHF is usually explained as behavioral training: reward the outputs you want, and the model learns to produce them. That is not wrong. But it misses something structural."

*Rationale: Opening was slightly defensive (narrating own learning arc). Compressed to direct claim that sets up the core concept faster.*

---

### Middle — trim redundancy

The paragraph "This also explains something I have seen..." is strong but long. Trim to:

"Two models can score identically on RLHF benchmarks while having fundamentally different attractor geometries. The benchmark measures whether the output landed in the preferred basin — not the shape of the basin or how far the model had to travel to get there. This is why some RLHF models feel structurally off to experienced users even when they score well."

---

### Ending — fix final question

**Before:**
"That is the part I keep coming back to. RLHF gave us a powerful way to shape what models do. But what it actually changes is deeper than the behavior itself — it is the structure that generates the behavior. And that structure has inertia that pure behavioral training does not account for."

**After:**
"If you are seeing behaviors that resist repeated fine-tuning, the attractor hypothesis suggests you might be fighting the basin rather than reshaping it. The fix may not be more fine-tuning — it might be a different intervention in the output landscape entirely."

*Rationale: Original ending is a solid insight but ends on a statement. New ending gives a diagnostic heuristic ("behaviors that resist fine-tuning") and ends with a concrete implication rather than a summary.*

---

### Word count: ~850 → ~780 words after cuts

**Final output ready for posting.**