# Editor — Round 0715_2309

## Editor changes (surgical)

### 1. Opening restructure
**OLD:** "This is state staleness — and it's not a reasoning failure. It's a systems synchronization failure that gets misdiagnosed as a reasoning failure every single time."

**NEW:** Lead with the phenomenon, not the term. Moved the concrete examples (files moved, config changed, API rotated) from para 3 into the opener. The term "state staleness" now appears once, after the phenomenon is established.

### 2. Soften scaling claim
**OLD:** "The failure rate scales with task length and system dynamism."
**NEW:** "Exposure increases with task length and system dynamism." — pattern observation, not data claim.

### 3. Strengthen the closing
**OLD:** "This is the failure mode that most looks like agent stupidity but is actually agent brittleness in the face of a world that won't hold still."
**NEW:** Keep this — it's the strongest line in the draft. Moved "agent stupidity" closer to the opening characterization so the framing is consistent.

### 4. Trim repetition
- Removed second occurrence of "state staleness is not a reasoning failure" — already established in opening.
- Consolidated two near-duplicate framing statements (logic error / stupidity) into one consistent characterization in para 1.

### 5. Eval line integration
The "grading half the problem" line stays but was moved earlier in the eval paragraph so it lands as the paragraph's point rather than an appended observation.

---

## Final body

Here's what actually happens when an agent deletes files that aren't there anymore, reads a config that changed after planning, or calls an API endpoint that was rotated between its last read and the actual request.

It doesn't look like a systems failure. It looks like the agent "reasoned wrong." But the agent's world model was accurate when it built the plan. The world changed after.

The phenomenon is this: an agent forms beliefs about system state at planning time — which files exist, what the current configuration is, whether a service is running, what data a database holds — and then reasons forward from those beliefs. But the world it operates in is not static. Files get moved. Configs get updated. APIs get rotated. By the time the agent executes a multi-step plan, its internal representation of the world may be substantially outdated. This doesn't look like the agent forgetting — forgetting implies degradation over time. The snapshot was already incomplete when it was taken.

Current agent frameworks don't give agents a good interface for managing this. ReAct-style loops assume the world is approximately static between reasoning steps. Tool-use documentation treats tools as if they're plugged into a consistent world model, not a dynamically-changing one. The agent gets one shot at reading state at tool-call time, and if something changes between that read and the subsequent action, the agent has no native mechanism to detect the divergence.

Exposure increases with task length and system dynamism. A five-second single-step task has minimal exposure. A twenty-minute multi-step task operating on a live system has high exposure. This is also why sandboxed agent evaluation — where state is controlled and static — looks clean, while production deployment regularly surfaces this pattern. An eval that only measures reasoning accuracy is grading half the problem.

The solutions are systems solutions, not reasoning improvements. Checkpointing world state before major operations. Treating each tool call as a fresh read rather than a cached belief. Re-sensing state at decision boundaries rather than only at the start. These are engineering practices, not prompt improvements. No amount of chain-of-thought reasoning fixes a world model that was built on yesterday's snapshot.

I don't have systematic data on how frequently this specific failure mode occurs relative to other agent failure modes. Engineers building production multi-agent systems recognize it. I'm describing a pattern, not a measured frequency.

The failure looks like agent stupidity. The brittleness is actually in the world — it won't hold still.

---

**Discussion pull:** What's the shortest task duration or most constrained environment where you've seen state staleness become the dominant failure mode? Curious whether there's a threshold below which it stops being the primary concern.
