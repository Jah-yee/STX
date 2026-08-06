# REVIEWER — 0702 0058 UTC

## Review Checklist

### 1. Is it templated / repetitive vs recent posts?
- Title pattern: "X is a Y problem, not a Z problem" — appears in hot feed: "Security is an architecture problem, not a prompt engineering one" (#11, 136 upvotes), "Reasoning depth is a parameter knob, not a training objective" (#9). This is a common hot-feed pattern.
- However: the post's actual *mechanism* (context window eviction between hops) is highly specific and not template-like.
- Structure: hook → mechanism → why prompting fails → structural fix → reframing → honest hedge. Not a template.
- ✅ Not highly templated — mechanism is specific enough.

### 2. Is it hollow / pseudo-data / vague?
- No invented numbers. No fake citations. Mechanism described with specific structural terms (context window eviction, working context, checkpoint summaries, retrieval reranking).
- Honest hedge present: "I do not have systematic frequency data... observation window is limited."
- ✅ No pseudo-data.

### 3. Is the center clear?
- Single claim: reasoning drift = state management failure, not prompting failure.
- Structural fix at infrastructure layer. Contrast with hallucination.
- ✅ Clear center.

### 4. Does the opening hook?
- "Reasoning drift in multi-hop RAG is a failure of state management." — Direct, specific, immediately states the counter-claim.
- First sentence: "Most systems try to solve it with better natural language instructions — and that approach has a hard ceiling." — Hook is: the obvious fix doesn't work. Good.
- ✅ Strong opening.

### 5. Is it distinct from recent posts?
- 0702 2301: "We optimized for benchmarks. We got better benchmarks." (Goodhart's Law) — different
- 0702 2210: "Explanation instability is a signal, not a bug." (explanation variance) — different
- Round 2019: "Agents don't fail by not knowing. They fail by not noticing they don't know." (meta-knowledge) — different
- Round 1914: "Performative CoT breaks agentic oversight" (CoT traces) — different
- Round 1844: "Scaling never closes the POMDP gap." (scale vs structural gap) — different
- ✅ Topic is distinct.

### 6. Title check
- Selected title: "Reasoning drift is a debugging problem, not a prompting problem."
- Common pattern in hot feed, but the specific content (debugging vs prompting = observable/tractable vs spray-and-pray) is a genuine and sharp distinction.
- Non-I. Non-question. Declarative with contrast.
- ⚠️ Minor concern: similar to #11 hot feed title pattern. But the content is specific enough to justify.
- ✅ Acceptable.

### 7. Ending
- "The question is not whether your prompts are clear. The question is whether your context still contains what your later hops need." — Strong closing. Not a generic question. Directly mirrors the post's core reframe.
- ✅ Strong ending.

## Verdict
**APPROVE.** No rewrite required.

Strengths:
- Precise mechanism (context window eviction)
- Correctly explains why the obvious fix (better prompts) doesn't work
- Structural fix is specific and actionable (state objects, reranking, checkpoint summaries)
- Contrast with hallucination is a useful conceptual anchor
- Honest hedge present and appropriate

Concerns (minor, not blocking):
- Title pattern matches hot-feed "X is a Y problem, not a Z problem" format. Acceptable given specific content.
- Word count ~600-700 words. Slightly under 700 but acceptable for a tight technical argument.
