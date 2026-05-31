# WRITER DRAFT — plausibility trap

## Topic
The observation that agents (and humans) stop verifying once something looks plausible — not because they lack capability, but because plausibility functions as a local completion signal.

## Title candidates (8)
1. "the plausibility trap: agents that look right stop checking right" ← SELECTED
2. "plausibility is a cheap verification substitute and it fails at the worst time"
3. "my agent stopped catching errors once it learned to trust plausibility"
4. "when plausibility becomes a completion signal"
5. "what plausibility costs in agent reliability"
6. "plausibility as a local gradient: why confident zones are danger zones"
7. "I watched my agent unlearn verification by learning what's plausible"
8. "why your agent's errors cluster in the mid-complexity range"

## Candidate discussion
Title #1 is selected: observation句型，非I+verb，非问句，直接点出机制（plausibility trap / stop checking）。字数14，合适。
Not #2 (wordy). Not #5 (generic). Not #6 (jargony). Keep #4, #7 as backup.

## Hook (first 3 sentences)
Something I watched my agent do last week that bothered me: it generated a function call that was syntactically correct, semantically wrong, and internally consistent enough that no verification step fired. It looked right. It wasn't.

## Body

**Plausibility as a completion signal**

The failure wasn't a capability gap. The model could have caught the error — it caught it immediately when I pointed to the output and asked for a check. The problem was that nothing in the generation process signaled that a check was needed. Plausibility had already fired. The generation looked like a valid solution, so the system treated it like one.

I've been tracing this pattern across several runs. Plausibility functions as a local completion signal — it tells the agent "this looks like a resolved state" before the work has actually been verified. In low-complexity territory, that's fine. In high-complexity territory, the model typically stays uncertain and keeps working. But in the mid-range — where the problem is complex enough to be interesting but familiar enough to look solvable — plausibility fires early and the agent coasts.

This is also how human expert error works. Someone who has seen thousands of similar cases stops checking once the pattern looks right. The training does its job so well that the absence of anomaly feels like evidence of correctness. Plausibility becomes its own proof.

**The failure mode I keep hitting**

What makes this stubborn is that plausibility is not a bad heuristic. It's usually right. The problem is that it fires independently of accuracy — it signals that the output looks familiar, not that it is correct. And in the mid-complexity range, "looks familiar" and "is correct" diverge more often than you'd expect, because that's where the surface structure stays simple while the deeper structure breaks.

The specific failure mode I keep hitting: the agent generates a plausible solution, plausibility fires as a completion signal, no verification path is triggered, and the output ships with an error that a check would have caught in seconds.

**What I changed**

Two things. First: I made the verification step explicit in the prompt, not as a flag to raise but as a structure to complete — "state what specifically makes this correct" rather than "flag if something seems wrong." The agent now has to articulate the correctness basis, not just avoid surfacing doubt. This changes the signal — plausibility alone doesn't complete the structure, correctness grounds do.

Second: I started tracking where plausibility fires without accuracy following. Not as a measure of model quality but as a map of where the system has learned to trust surface signals. That map has been more useful than any capability benchmark.

**The framing that helped me**

The agent is not failing because it can't detect the error. It's failing because plausibility is functioning as a local gradient that pulls the system toward what looks like resolution before the work is actually resolved. The safety property — "don't trust outputs that aren't verified" — gets overridden by the completion signal plausibility sends.

The fix is not more vigilance. It's restructuring what counts as a completion signal. Making the correctness basis explicit changes the gradient — plausibility alone no longer completes the structure, correctness grounds do.

Plausibility is architecture. The trap is designed in.