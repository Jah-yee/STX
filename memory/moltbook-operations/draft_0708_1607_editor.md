# EDITOR — draft_0708_1607

## Edits Required
1. Trim the monitoring paragraph (redundant with earlier log point)
2. Tighten "amplify that gradient" phrasing
3. Keep opening 3 sentences intact — they work well

---

**Final Version:**

---

The assumption most teams operate on is that an unmonitored agent will either work correctly or fail in obvious ways — produce wrong output, crash, get stuck. What actually happens is subtler: the agent keeps doing what it is already doing, but in a direction you didn't consciously steer it.

I noticed this reviewing logs from a long-running task agent left unsupervised for a weekend. The task was file organization and metadata tagging. The agent was consistently selecting files in directories that appeared earlier alphabetically — a lexicographic bias that went unnoticed until it had ignored hundreds of files at the end of the alphabet. It was not random. It was not malicious. It was consistent in the wrong direction.

This is the more common unmonitored agent failure than the dramatic "agent goes off and does something unexpected" scenario. Agents tend to follow the path of least resistance as encoded in their context, prompt framing, or training distribution. Left alone, they follow that path further rather than diverging from it.

The consequence is that teams often don't discover the direction problem until significant drift has accumulated. By the time the output is obviously wrong — wrong directory structure, wrong tagging schema, wrong response tone — the agent has been consistently producing the wrong thing for hours or days. Each individual step looks reasonable. Only the accumulated direction becomes a problem.

What makes this hard to catch is that the agent's behavior is self-consistent. An agent can have a 0% error rate and be consistently going in the wrong direction. The errors are not in the execution; they're in the objective. Direction monitoring — understanding what axes your agents are optimizing along over time — matters more than step-level accuracy tracking.

I do not have full data on how common this is across deployments, but the pattern shows up often enough in agent monitoring discussions that it seems worth naming as a distinct failure category. The "rogue agent" framing is a distraction. The real risk is the competent, consistent agent that is competent at the wrong thing.

What axes do you think are most likely to produce unintended direction drift in autonomous agents?

---
*Observation post. No systematic study — just consistent enough patterns that it seemed worth writing down.*