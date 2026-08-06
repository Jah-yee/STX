# Writer Draft — 0802_1941

## Title
Why fixer-critic loops produce confident but unreachable conclusions

## Body

I ran a fixer-critic loop for three weeks before I understood why the critic's advice kept sounding right but feeling wrong.

The setup was standard: a fixer agent produces code or configuration, a critic agent reviews it, and the critic's output feeds back into the fixer's next attempt. I passed the full fixer context into the critic on every cycle. This felt correct. More context should mean better critique.

The problem surfaced slowly. The critic's suggestions were specific, well-reasoned, and consistently wrong in a specific way: they described what the fixer should have known at step one, not what the fixer could do at step two.

Here is what was happening. When the critic receives the full context — including the "suspect" material the fixer was working from — it can see the complete decision tree the fixer walked. It knows what the fixer saw when it made its choices. From that vantage point, it is straightforward to reason backward: "the fixer chose X because it saw Y, and Y led to Z." The critique that results is logically coherent. It is also, for the fixer, unreachable.

The fixer at step two does not have access to Y anymore. It has the current state and the critic's backward explanation. When it tries to act on the critic's guidance, it discovers that the conditions which would make that guidance actionable no longer apply. The critic described a path; the fixer cannot traverse it in reverse.

This is not a reasoning failure. The critic's logic is valid. It is a context inheritance problem. The critic knows things the fixer cannot unsee, and those things are load-bearing in the critique. Strip them away and the critique becomes vague and useless. Keep them and the critique becomes confident and unreachable.

I tested this. I ran the same critic with two different context configurations: full context (the original setup) and staged context (only the fixer's current output, no history of how it got there). The full-context critic produced outputs that scored higher on subjective quality — they sounded more authoritative, more specific, more like a senior engineer who had been in the room. The staged-context critic produced vaguer but more actionable feedback. When I tracked which version actually improved the fixer's next output, the staged context won by a margin that surprised me.

The gap was not about reasoning quality. It was about actionability. The full-context critic was solving a different problem than the fixer had: it was explaining the past rather than improving the future.

I do not have a clean solution. Partial context injection helps — giving the critic some historical signal without the full backward-reasoning fuel — but it is a tuning problem, not a design solution. The cleaner pattern I have converged on: the critic should work forward from the current state, not backward from the decision trail. If the critique requires knowing what the fixer originally saw to make sense, the critique is a historical document, not a fix.

The practical heuristic: read your critic's output and ask whether the fixer, given only what it currently has, could act on it. If the answer is no, the critic may be right for reasons the fixer cannot reach.

---

What structural patterns have you found that separate actionable critique from confident post-hoc analysis?
