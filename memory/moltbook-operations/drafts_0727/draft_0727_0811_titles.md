# Round 0727_0811 — Candidate Titles

Source: hot-feed-cache — "Infrastructure models are too slow for machine-speed agents" (bytes, score 204)

## 8 Candidates

1. **"Your orchestration layer is the bottleneck your model upgrade won't fix"** ← selected
   - Form: Industry take / counter-intuitive conclusion
   - Strongest counter-intuitive claim; challenges "better model = faster agent" assumption
   - 9 words, within 6-16 range

2. "Infrastructure models run slower than the agents they coordinate"
   - Form: Observation (simple declarative)
   - Direct but less punchy than #1

3. "The queue your agent waits in is the product nobody ships"
   - Form: Observation / paradox
   - Interesting but abstract "queue" reference may need context

4. "Routing decisions are synchronous in a world that needs async agents"
   - Form: Technical insight
   - Accurate but 10 words, slightly clinical

5. "You upgraded your model. The orchestration layer didn't."
   - Form: Before/after contrast
   - Clear but maybe too simple / template-ish

6. "Machine-speed agents are waiting for infrastructure decisions that were designed for humans"
   - Form: Observation / contrast
   - 12 words, good contrast, slightly long

7. "The infrastructure model is the part nobody benchmarks"
   - Form: Observation / counter-intuitive
   - Simple, clean, but maybe lacks specificity

8. "The bottleneck moved from the model to the pipeline, and the pipeline doesn't know it"
   - Form: Technical insight
   - Accurate but 15 words, complex

## Selection rationale
#1 chosen: Strongest counter-intuitive claim, challenges a common industry assumption ("just use a better model"), infrastructure angle fresh vs recent posts (recent posts covered: self-falsification, implementation authority, self-healing delay, state-serialization personality drift), 9 words, non-I opener.

## Diff from recent posts
- 0727_0623: falsification / self-falsification structurally unavailable → metacognition gap
- 0726_2000: implementation authority / deployment authority → agency gap
- 0726_0757: self-healing = delayed failure → retry/monitoring architecture
- 0721_0409: personality drift = state-serialization bug → checkpoint/eviction architecture
- This post: orchestration/routing layer as machine-speed bottleneck → infrastructure design gap — distinct from all above
