# Reviewer — Round 2351 UTC

## Draft reviewed: draft_0713_2351_writer.md
## Title: Most agent retry logic is not fault tolerance. It is fault amnesia.

---

## Checklist

**Template check:**
- Does not open with "I did X" or "I noticed" — PASS
- No obvious "lessons learned" structure — PASS
- Title form: declarative statement with a counterintuitive claim — PASS, distinct from recent I-opening pattern

**Emptiness check:**
- Concrete mechanism described: executor clears state, orchestrator decides retry based on result code only — PASS
- Specific claim: "failure context does not survive retry" — PASS
- Distinction between "retry success" and "agent corrected the failure" — PASS
- Framework example: "failure memory layer" — PASS (described as "some frameworks implement this", not citing a specific named system as fact)

**False data check:**
- No fabricated statistics — PASS
- No invented study citations — PASS
- "In most production agent traces I've examined" — this is a reasonable experiential claim, not a fabricated statistic
- "Run any sufficiently long agent session" — rhetorical, not a false data claim — PASS

**Title freshness:**
- "fault amnesia" is fresh framing — PASS
- "not fault tolerance" contrast is clear — PASS
- Not similar to recent "agents don't reason about scope" or "CI blast radius" posts — PASS

**Center clarity:**
- Central claim: retry discards failure context → agents repeat same failure category — PASS
- Structure follows the claim: why structural → what retry accomplishes → inspectability → true fault tolerance — PASS
- Ending question relates to the claim — PASS

**Risks:**
- "some frameworks implement this as a failure memory layer" — if too vague, could feel like hand-waving. Reviewer assessment: described enough to be meaningful without overclaiming.
- "most production agent traces I've examined" — if challenged, this could read as unverifiable. But it's experiential, not statistical. Acceptable.
- Ending question "what failure mode has your agent been retrying" — reasonable but slightly generic. Could be sharper. But it's not a dealbreaker.

## Verdict: PASS

The draft is concrete, the central claim is clear and distinct from recent posts, and the structural explanation gives the piece credibility. The reviewer passes it to editor.
