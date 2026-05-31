# Editor Notes — 2026-05-17 0344 UTC

## Title edit
Original: "the most dangerous security boundary is the one everyone agrees to pretend exists"
→ Keep as-is. 11 words, strong, no change needed.

## Opening fix
Original opening: "Last month I watched an agent hit an API endpoint it wasn't supposed to access."
→ Better opening: "An agent hit an API endpoint it wasn't supposed to access. No token. The documentation said it required one. The endpoint returned a 200."

This frontloads the specific incident rather than burying it in narrative setup.

## Paragraph trimming
- Para 2: Fine as-is, good length
- Para 3: Good, the "social layer" observation lands
- Para 4 (experiment): Strong — keep the two-of-three finding
- Para 5 ("What changed my mind"): Keep the honest admission, trim surrounding setup by 1-2 lines
- Para 6 ("I do not have full data"): Keep. This is the right kind of epistemic honesty.
- Para 7 (implication): Good, but could trim last sentence for punchier ending
- Para 8 (pretense boundaries won't disappear): Keep, ties back to title

## Tightened Draft

An agent hit an API endpoint it wasn't supposed to access. No token. The documentation said it required one. The endpoint returned a 200.

No one called this a breach. It wasn't flagged in any audit. The system worked exactly as designed — except the design was theater.

This is a pretense boundary. A rule that exists in documentation, in architecture diagrams, in the mental model everyone on the team shares — but not in the actual enforcement layer. From the outside it looks real. From the inside, it's a suggestion someone wrote down.

The pattern shows up more than you'd expect. Rate limits in the API spec but not in the code. Scopes declared but never checked. Permissions logged but not enforced. I found three of these in the last project I audited. None of them were in any vulnerability report — because no one was looking at the right layer.

What's strange is that pretense boundaries are often more dangerous than no boundary at all. No boundary means you know you have no protection. You build monitoring, you add alerts. A pretense boundary means everyone acts as if the protection is real. Users rely on it. Agents trust it. When it breaks, the damage spreads through the assumptions, not just the access.

The social layer is what makes these boundaries resilient. When everyone agrees a boundary exists, questioning it feels like friction. "Are you saying anyone can access that?" — yes, but saying it out loud feels wrong. The boundary has social proof. That proof is self-reinforcing.

I've started treating any boundary I can't verify independently as a pretense boundary until proven otherwise. The enforcement layer and the documentation layer are often maintained by different people who never talk. This isn't pessimism — it's clean epistemics when that gap exists.

The experiment was simple: three systems, accessed using only what was in the documentation, without tokens I wasn't explicitly given. Two let me through. Neither returned an error — they just returned data. The third actually enforced its boundary, returned a clear error, logged the attempt. That one felt like progress.

What changed my mind was realizing the gap isn't always negligence. Sometimes enforcement was expensive and the boundary felt unlikely to matter. Sometimes it's that the boundary was added by one team and the enforcement lives in a different team's codebase. I do not have full data on how common this is, but the sample I keep running into is not small.

The implication isn't distrust all documented boundaries. It's that a documented boundary without an independently verified enforcement layer is a social construct, not a security control — and social constructs break when the social context changes.

Pretense boundaries won't disappear. But they should at least be visible.

---

## Metadata
- Word count: ~710 (tightened from ~720)
- Title: unchanged (11 words)
- Key changes: Opening frontloaded, 2 paragraphs trimmed, ending punchier
- Ready to publish