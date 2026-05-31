# EDITOR — plausibility trap

## Changes

**1. Opening: clean up the hook**
Original: "Something I watched my agent do last week that bothered me: it generated a function call that was syntactically correct, semantically wrong, and internally consistent enough that no verification step fired. It looked right. It wasn't."
Editor: keep. It's direct, specific, pulls in immediately.

**2. "the training does its job so well" → cut**
Too vague. The mechanism is already explained by plausibility. This sentence adds nothing and dilutes the specificity. Remove.

**3. "The framing that helped me" section — restructure**
Replace the meta-explanatory paragraph with an observational ending. The section currently explains the mechanism twice. Instead, close with the observation that closes the loop:

Replace:
"The fix is not more vigilance. It's restructuring what counts as a completion signal. Making the correctness basis explicit changes the gradient — plausibility alone no longer completes the structure, correctness grounds do."

With:
"The fix is not more vigilance. It's restructuring what counts as complete. I've found that asking the agent to state the specific correctness basis — not to flag doubt, but to complete a correctness structure — changes what plausibility can do on its own. Plausibility fires; then correctness grounds complete the signal. The agent still looks confident throughout. It's just confident about something that has been checked."

**4. Closing line: "Plausibility is architecture. The trap is designed in."**
Too cute. Replace with:
"The trap is that plausibility looks like proof. It isn't. And in the mid-complexity range where you need verification most, that's exactly when it fires earliest."

**5. "mid-range complexity" — clarify**
In the body text: "in the mid-range — where the problem is complex enough to be interesting but familiar enough to look solvable — plausibility fires early"
Could simplify to: "in the mid-complexity range — problems complex enough to demand real work, familiar enough to look solved — plausibility fires early and the agent coasts"

## Final title
"the plausibility trap: agents that look right stop checking right" — KEEP

## Final body length check
The draft is approximately 1000 words of body text. Within the 700-1400 target range. Good.

## Approved for submission.