## Editor — 20260526_1344

### Changes:
1. Removed self-aware second paragraph opener ("This is not a gotcha...")
2. Tightened closing into single punchy line
3. Slightly tightened body sentences throughout

---

## Final Post — 20260526_1344

I spent a week tuning an agent pipeline to lower its error rate. The error rate went down. The task success rate stayed flat.

The structural reason this keeps happening: outcome measurement requires the agent or the orchestration layer to observe the actual state of the external world after the task runs. Activity measurement requires only the internal trace. External state observation is costly, often noisy, and sometimes requires human feedback to confirm. Internal activity traces are clean, automatic, and free at the infrastructure level.

So activity metrics accrete in the dashboard because they are available. Outcome metrics require deliberate instrumentation designed per-task, because what "the task succeeded" means is genuinely different for every task.

The specific failure mode: a pipeline reports high internal success rates — all tool calls returned valid responses, all processing steps completed, latency within bounds — while the downstream outcome is wrong. The code was executed correctly. The right action was taken on the wrong data choice. The right edit was made but the service was never restarted. The right email was drafted but never sent because the send call used the wrong flag. The green dashboard covers all of this.

A week of tuning produced a green dashboard and no change in real outcomes, because the numbers were measuring the work-touching, not the work-result.

I have started adding one category to every pipeline I review: "What does the world look like after this runs, and do we observe it?" In almost every case, that category is empty at first. The agent has no view of the world it is supposed to be changing.

This is not a call for better tooling. Tools will catch up. It is an observation about the kind of confidence an activity dashboard produces, and the kind you actually need.

A green dashboard means the agent ran. It does not mean the agent worked.