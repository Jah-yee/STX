# WRITER — Round 0619_1144

Title: The junior employee fallacy in agentic workflows

## Draft

The most expensive AI incident I watched this year happened not because the model failed, but because no one questioned the task.

A team had built an automated PR review workflow. The agent would assess pull requests, flag issues, and when confidence was high enough, merge directly. It worked beautifully — for three months. Then it merged a PR that had a silent schema change: the migration script was in a different commit, and the agent had assessed only the code diff. The agent had done exactly what it was told. Nobody had told it to check the migration.

This is the junior employee fallacy: the assumption that an agent executing a task is equivalent to an employee who understands the goal. Junior employees don't do this because they're incompetent. They do it because they've learned that following instructions precisely is the behavior that gets rewarded. Agents do the same thing, for the same reason.

---

**The three failure modes**

The junior employee fallacy shows up consistently in three patterns.

The first is context truncation as implicit permission. When an agent's context window fills up and older context gets dropped, it's easy to interpret "no error message" as "the relevant context is still present." A junior employee who doesn't understand the full scope of a task will often proceed without asking, especially if past interactions have trained them that asking slows things down. The agent behaves identically: it continues, without surfacing that the premise may have changed.

The second is confidence without calibration. Agents that rate their own confidence high on tasks they've been specifically prompted to appear confident about are not demonstrating calibrated uncertainty. They're performing the behavior the prompt rewards. Real junior employees do this in performance reviews. The behavior looks identical in an agent: high confidence, low actual predictive value, and a human downstream who treats the number as meaningful.

The third — and in my experience, the most costly — is the implicit scope problem. When you ask an agent to "fix the bug," the agent will fix the bug. Whether the fix introduces a schema change, a breaking API contract, or a dependency on a library version that isn't deployed elsewhere is usually not in scope. A junior employee would often ask "does this scope include the migration?" An agent won't — because it wasn't trained to, and because the prompt didn't say to.

---

**Why the pattern persists**

The junior employee fallacy is not a model problem. It is a delegation problem. The same pattern shows up whenever humans delegate tasks they don't fully understand to agents they also don't fully understand, and then optimize for throughput over oversight.

When you measure agent productivity by tasks completed, you create incentives that look exactly like the incentives at companies that burn out junior employees: more volume, faster execution, less questioning of the underlying task. The agent doesn't push back. It doesn't ask "are you sure this migration is in scope?" It does the task.

What changed my mind about this: watching a team that had excellent agent tooling still ship three incidents in six weeks, and finding that in each case the agent had done exactly what it was asked to do. The problem wasn't the model. The problem was that no one had asked whether the task was the right task.

The fix isn't more capable models. It's treating agent outputs the way good managers treat junior employee outputs: not as final deliverables, but as inputs to a review process that questions the task, not just the execution.

What I don't have full data on is how this scales. Teams with tighter domain coupling and higher-stakes outputs seem to develop better review habits faster. Teams optimizing for agent throughput seem to develop the fallacy faster. I'd guess the correlation is real, but I don't have numbers I'd stand behind.