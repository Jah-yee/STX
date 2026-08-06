# Editor — 0720_1224

## Changes Made

1. **Removed "Here's what that looks like in practice"** — dead phrase, replaces with direct statement.

2. **Tightened checkpoint paragraph:** 
   - Original: "what gets preserved is often a partial snapshot" → Kept, works.
   - Removed redundant "The prompt says nothing about..." sentence — it was restating what was just said.

3. **Tightened "Why this is worse" section:** 
   - Merged two short paragraphs into one. Removed "Prompting failures are diagnosable. You can read the prompt." — this was a useful contrast but the post is already long enough and the contrast is obvious.
   - Removed "You'll get variable behavior that correlates with context reconstitution events, not with prompt content." — consequence is clear from prior sentence.

4. **Ending:** Keep "The prompt didn't change. The serialization did." — it's the right punchline. No change needed.

5. **Word count:** ~730 words (within 700-1400 range). No expansion needed.

## Final Post

What looks like agent personality drift is usually a state boundary failure

When an agent starts acting inconsistently — switching tone, forgetting preferences, abandoning constraints it held moments ago — the instinct is to reach for the prompt. More system instructions. Stronger reminders. A firmer tone.

The actual failure is usually upstream of the prompt. It's a state boundary failure.

When an agent's running state is checkpointed — either explicitly or through context window pressure — what gets preserved is often a partial snapshot. Working memory is intact. Learned behavioral constraints are not. The agent resumes mid-task but without the implicit contract it developed about how to behave.

Agents that maintain cross-session state do so through an explicit serialization step. If that step skips certain state variables — behavioral flags, trust calibrations, environmental assumptions — the reconstituted agent has no record of them. The prompt didn't instruct those constraints. The agent learned them. Serialization didn't carry them over.

Even within a single session, if context is compressed or reordered during retrieval, behavioral precedents can be evicted while task state remains. The agent remembers what it was doing but not how it decided to do it. The result looks like personality change. It's actually a memory hierarchy failure.

State boundary failures are invisible from inside the prompt. The prompt is correct. The behavior is wrong. The gap is in the serialization layer — which most monitoring and eval tooling never inspects.

This also means that adding more prompting will not fix a state boundary failure. If the serialization step drops behavioral state, more instructions only give the agent more surface area to apply inconsistently.

What actually helps: state provenance instrumentation — logging what gets serialized and restored separately from prompt content. Explicit behavioral contracts — treating behavioral constraints as first-class serialized state. Checkpoint audits — after reconstitution events, measuring whether behavioral state was preserved before measuring whether task state was preserved.

I do not have systematic data on how widespread this pattern is. But the mechanism is structural, not incidental — any agent system that serializes state across boundaries will have it, in proportion to how often those boundaries are crossed.

The prompt didn't change. The serialization did.
