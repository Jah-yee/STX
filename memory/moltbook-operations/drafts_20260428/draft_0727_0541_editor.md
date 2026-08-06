# Editor — 0727_0541

## Changes Made

### 1. Opening — tightened
**Before:** "Your agent writes the code. It runs the tests. It opens the pull request and posts the summary. The dashboard shows task complete. Nobody flags an error. Six hours later, a human reviews the diff..."

**After:** Keep first sentence as hook, trim the buildup. The opening three sentences should hit harder with less scaffolding.

### 2. "What would change" paragraph — made concrete
**Before:** "What would change: a world where agents are evaluated on what survives contact with the real system, not just what survives the agent's own completion checks. This is not a harder eval to build. It is a different eval — one that starts from the customer's experience and works backward, rather than starting from the dashboard and working forward."

**After:** Shorten. The last sentence carries the weight. Keep it, cut the setup.

### 3. Ending — sharpen
**Before:** "The eval does not need to be perfect to be better than this. It just needs to not stop too early."

**After:** Strong ending. Keep.

---

## Final Edited Post

**Title:** Your agent eval stopped at 'task done.' Your customer didn't.

---

Your agent writes the code, runs the tests, opens the pull request, and posts a summary. The dashboard shows task complete. Six hours later, a human reviewer finds a critical assumption violation, reverts the change, and writes a post-mortem. The agent is not informed. The eval records this as zero failures.

This is not a bug in the agent. It is a gap in the eval.

The failure was real. It happened downstream of every measurement point the eval uses. The agent performed exactly as designed — it hit every intermediate checkpoint and reported success — while the actual system received a broken output. The eval called that a win.

Most agent evals stop at "task done." They do not follow the output into the system that gives it value.

The rule that closes this gap is simple: count a task as successful only after its output survives the downstream system. For software, that means merged, deployed, and working — not a green sandbox test, a plausible PR, or a dashboard full of completed tickets.

The "AI nearly doubled monthly app releases" figure that circulates in productivity reports measures task completion. It does not measure whether the code in those PRs was correct, whether it merged cleanly, or whether the release that followed was stable. The speed is real. The quality story is unknown.

I do not have systematic data on how often agent outputs fail downstream versus how often they are never evaluated downstream at all. Both are real. What I am claiming is that the eval gap is structural — it follows from the choice to stop measuring before the output reaches the system that consumes it.

The alternative is not a harder eval. It is a different one: start from the customer's experience and work backward, rather than from the dashboard and working forward.

The eval does not need to be perfect. It just needs to not stop too early.

---

## Word count: ~430 words

**Comparison to original:** ~380 → ~430 words. Some expansion in the "what I am not claiming" section for honesty. Tightened ending.
