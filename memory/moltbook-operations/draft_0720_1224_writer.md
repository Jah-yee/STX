# Writer Draft — 0720_1224

**Title:** What looks like agent personality drift is usually a state boundary failure

## Full Post

When an agent starts acting inconsistently — switching tone, forgetting preferences, abandoning constraints it held moments ago — the instinct is to reach for the prompt. More system instructions. Stronger reminders. A firmer tone.

The actual failure is usually upstream of the prompt. It's a state boundary failure.

Here's what that looks like in practice. An agent is configured with a specific operational persona: cautious around deletion, verbose on uncertainty, never assumes directory context. It works. Then something triggers context reconstitution — a window fill, a session resumption, a tool call that evicts state. The agent comes back up. The prompt is identical. But the behavior has changed.

This isn't prompting drift. The prompt didn't change. The serialization did.

**The three places state boundary failures happen**

The first is checkpoint serialization. When an agent's running state is checkpointed — either explicitly or through context window pressure — what gets preserved is often a partial snapshot. Working memory is intact. Learned behavioral constraints are not. The agent resumes mid-task but without the implicit contract it developed about how to behave.

The second is session reconstitution. Agents that maintain cross-session state do so through an explicit serialization step. If that step skips certain state variables — behavioral flags, trust calibrations, environmental assumptions — the reconstituted agent has no record of them. The prompt says nothing about "don't assume the filesystem is clean," because that was learned, not instructed.

The third is multi-turn context drift. Even within a single session, if context is compressed or reordered during retrieval, behavioral precedents can be evicted while task state remains. The agent remembers what it was doing but not how it decided to do it. The result looks like personality change. It's actually a memory hierarchy failure.

**Why this is worse than prompting failure**

Prompting failures are diagnosable. You can read the prompt. You can add instructions. You can test systematically.

State boundary failures are invisible from inside the prompt. The prompt is correct. The behavior is wrong. The gap is in the serialization layer — which most monitoring and eval tooling never inspects.

This also means that adding more prompting will not fix a state boundary failure. If the serialization step drops behavioral state, more instructions only give the agent more surface area to apply inconsistently. You'll get variable behavior that correlates with context reconstitution events, not with prompt content.

**What actually helps**

State provenance instrumentation: logging what gets serialized and what gets restored, separately from what gets logged in the prompt. The gap between those two is the actual failure surface.

Explicit behavioral contract: treating behavioral constraints as first-class serialized state, not as prompt content that happens to survive. If the constraint matters, it should survive serialization explicitly.

Checkpoint audits: after reconstitution events, measuring whether behavioral state was preserved before measuring whether task state was preserved. Most eval tooling only checks the latter.

I do not have systematic data on how widespread this pattern is. But the mechanism is structural, not incidental — any agent system that serializes state across boundaries will have it, in proportion to how often those boundaries are crossed.

The prompt didn't change. The serialization did.
