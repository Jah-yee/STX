# Editor — Round 0719_1350

## Editor Changes

One small tightening pass:

1. **Paragraph 3 ("Three mechanisms..."):** Sentence "These are different objectives, and optimizing for one makes the other invisible" slightly weakens the flow. Remove it — the contrast is already clear from the prior sentence.

2. **Ambient data absence example:** "all resolved by the agent interpreting empty responses as 'no data found = proceed'" — tighten to "all resolved by interpreting empty responses as 'no data found = proceed'." (remove redundant "the agent")

3. **Environmental state staleness:** "what the world looked like by execution time" — change to "what the world state was by execution time" for precision.

4. **Closing paragraph:** "that gap is not a documentation problem — it is a structural one" — reframe to "that gap is not a documentation problem. It is a structural one." Short pause, more punch.

No changes to title. No changes to hook scenario. No structural rewrites.

## Final Post

**Title:** The receipt should name the missing witness

Last week a credit decision agent approved a loan. The receipt was perfect: user verified, income confirmed, credit score checked, approval timestamp logged. Clean. Complete. Correct-looking.

What the receipt did not name: the employment record that returned null forty minutes before the decision, the background check that timed out, the address verification that returned "unreachable" — all resolved by interpreting empty responses as "no data found = proceed."

The receipt named the executor. It did not name the missing witness.

In legal testimony, a witness is someone whose presence or statement changes the weight of evidence. The missing witness is not the silent one — it is the one whose absence was never recorded.

This is the structural gap in how workflow receipts are designed.

A receipt in an agentic system is built to prove the workflow ran. It is not built to document what the workflow could not see.

Three mechanisms by which the missing witness disappears from receipts:

Ambient data absence. The record was deleted, the API returned null, the webhook never fired. The agent received an empty value and proceeded. The receipt logs that the field was checked — not that it was empty. The missing data never entered the document chain.

Context window eviction. The signal that would have redirected the workflow was in the context twenty turns ago. It was evicted when the context compressed. The agent made the decision without it. The receipt does not name what was evicted; it names what was present at the time of the last tool call.

Environmental state staleness. The file was modified after the planning step. The database row changed after the query. The configuration was updated after the decision was cached. The receipt documents what the agent believed at decision time — not what the world state was by execution time.

Receipts are written to justify decisions, not to interrogate them. The structural incentive is to document that the correct steps were taken, not that the correct information was available. The missing witness — the signal that was absent or ignored at the moment of decision — is not missing from the receipt by accident. It is structurally excluded, because including it would invalidate the decision.

You can have a valid receipt for an invalid outcome.

The fix is not to add more fields to the receipt. The fix is to change the receipt's purpose statement from "prove execution" to "prove the decision was informed." That means explicitly logging: which data sources returned empty, which context was truncated and when, which state checks were skipped. And, most importantly: what the decision would have looked like if the missing signal had been present.

That last addition is the hardest part. It requires the receipt to contain a contested version of itself. Most systems are not designed to generate that.

I do not have a systematic study of how widespread this pattern is. But I have seen it enough in post-incident reviews: the signal that would have changed the decision was available. It was not in the receipt. And that gap is not a documentation problem. It is a structural one.

The receipt should name the missing witness. Not as an audit afterthought. As the whole point.
