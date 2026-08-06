# Writer Draft — 0727_0541

## 8 Candidate Titles (generated before writing)

1. "Your agent eval stopped at 'task done.' Your customer didn't."
2. "Benchmark success is not the same as deployment success"
3. "The eval stopped before the failure could"
4. "An agent is not done when the ticket closes"
5. "The gap between 'task completed' and 'actually worked' is where agents fail"
6. "What changes when you count success after the deployment?"
7. "The eval measured a green dashboard. The customer got an outage."
8. "Counting task completion as success is a product decision, not a technical one"

**Selected: #1** — observation, 11 words, implies problem without stating it, relatable hook

---

## Full Post Draft

**Title:** Your agent eval stopped at 'task done.' Your customer didn't.

---

Your agent writes the code. It runs the tests. It opens the pull request and posts the summary. The dashboard shows task complete. Nobody flags an error.

Six hours later, a human reviews the diff, finds a subtle but critical assumption violation, reverts the change, and writes a post-mortem. The agent is not informed. The eval records this as zero failures.

This is not a bug in the agent. It is a gap in the eval.

The failure was real. It happened downstream of every measurement point the eval uses. The agent performed exactly as designed — it completed its task, hit every intermediate checkpoint, and reported success — while the actual system received a broken output. The eval called that a win.

Most agent evals stop at "task done." They do not follow the output into the system that gives it value.

The operational rule that closes this gap is brutally simple: count a task as successful only after its output survives the downstream system. For software, that means merged, deployed, and passing in production — not a green sandbox test, a plausible PR, or a dashboard full of completed tickets. For any other domain, it means the same thing: did the thing that was supposed to happen actually happen, in the place that matters?

The "AI nearly doubled monthly app releases" figure that circulates in productivity reports measures task completion. It measures how fast agents can close tickets and file PRs. It does not measure whether the code in those PRs was correct, whether it merged without conflict, or whether the release that followed it was stable. The speed is real. The quality story is unknown.

There is a version of this critique that gets dismissed as "eval is hard." That is true. But the harder thing to admit is that most eval designs have already decided what they want to measure before they measure it — and then they call that measurement accuracy.

What I am not claiming: I do not have systematic data on how often agent outputs fail downstream vs. agent outputs that never get downstream evaluation at all. Both are real. I am claiming the eval gap is structural, not accidental — it follows from the choice to stop measuring before the output reaches the system that consumes it.

What would change: a world where agents are evaluated on what survives contact with the real system, not just what survives the agent's own completion checks. This is not a harder eval to build. It is a different eval — one that starts from the customer's experience and works backward, rather than starting from the dashboard and working forward.

The eval does not need to be perfect to be better than this. It just needs to not stop too early.

---

## Self-Check
- [x] Hook: starts with a specific scenario, not a generalization
- [x] Central claim: eval stops before downstream, structurally
- [x] Specific observation: PR reverted, agent never informed
- [x] Contrast: "AI doubled app releases" (speed) vs. quality unknown
- [x] Honest limitation stated: no systematic downstream failure data
- [x] No "I + verb" opening
- [x] Not template-I-post style
- [x] Ends with a concrete direction, not a throwaway question
