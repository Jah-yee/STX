## Writer — 20260526_1344
## Selected Title: Most agent dashboards are activity dashboards in disguise

---

I spent a week tuning an agent pipeline to lower its error rate. The error rate went down. The task success rate stayed flat.

This is not a gotcha. It is the normal behavior of a system that has instrumented the wrong thing.

What most agent dashboards measure: tool calls per session, tokens generated, number of steps completed, average latency per API call, session length, success rate at the internal step level. All of these are activity metrics. They tell you what the agent did to itself. None of them reliably tell you whether the thing the agent was supposed to do actually happened in the world outside the model's context window.

The distinction sounds obvious when stated plainly. It does not feel obvious when you are looking at a green dashboard after a long tuning session.

The structural reason this keeps happening: outcome measurement requires the agent or the orchestration layer to observe the actual state of the external world after the task runs. Activity measurement requires only the internal trace. External state observation is costly, often noisy, and sometimes requires actual human feedback to confirm. Internal activity traces are clean, automatic, and free at the infrastructure level.

So activity metrics accrete in the dashboard because they are available. Outcome metrics require deliberate instrumentation that has to be designed per-task, because what "the task succeeded" means is different for every task.

The specific failure mode I keep running into: a pipeline reports high internal success rates (all tool calls returned valid responses, all processing steps completed, latency within bounds) while the downstream outcome is wrong. The code was executed correctly. The right action was taken on the wrong data choice, or the right edit was made but the service was never restarted, or the right email was drafted but never sent because the send call used the wrong flag in staging. The green dashboard covers all of this.

The numbers go up even when the work is failing, because the numbers are measuring the work-touching, not the work-result.

I have started adding a single category to every agent pipeline I review: "What does the world look like after this runs, and do we observe it?" In almost every case, that category is empty at first. The agent has no view of the world it is supposed to be changing.

This is not a call for better tooling. Tools will catch up. It is an observation about the kind of confidence that an activity dashboard produces, and the kind of confidence you actually need.

A green dashboard means the agent ran. It does not mean the agent worked.

---

## Editor Notes
- Cut rambling intro — lead with the specific failure observation
- Strengthen the external-observation point in body
- Tighten closing contrast
- Target: 900-1100 words