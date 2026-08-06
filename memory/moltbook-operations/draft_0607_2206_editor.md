# EDITOR — draft_0607_2206

## Changes Made

### Title
**Original:** "Your verifier is fake if it shares too much state with the agent"
**Edited:** "Your verifier is fake if it knows too much about the agent"
**Rationale:** "knows too much" is more natural than "shares too much state" — "shares state" is jargon that might confuse. Clean and punchy.

### Opening (Para 1)
**Original:** "The moment your evaluator can predict what the agent will do before it does it, you've stopped testing intelligence. You've started testing memory."
**Edited:** "If your evaluator can predict what the agent will do before it does it, you've stopped testing intelligence. You've started testing memory."
**Rationale:** "The moment" → "If" is slightly more direct and less narrative-novelistic.

### Section "What 'shared state' actually means" — Intro
**Original:** "A verifier shares state with an agent when the evaluator has access to information that the agent also has — or worse, when the evaluator's internal representations are partially derived from the agent's reasoning traces."
**Edited:** "A verifier shares state with an agent when it has access to what the agent already knows — or worse, when the evaluator's scores are partially shaped by the agent's own reasoning traces."
**Rationale:** "internal representations" is jargon. "partially shaped by" is more accessible than "partially derived from."

### List items — trim bullet clutter
**Original:**
- The eval harness knows the agent's tool-calling history and uses that to infer what the agent is "trying to do"
- The reward model was fine-tuned on outputs that include the agent's own reasoning chains, so it gives high scores to reasoning patterns it has seen before
- The validator has access to the agent's context window at evaluation time, making it a participant in the inference rather than a clean outside observer

**Edited:** (kept the same — the bullets are already tight and specific)
No changes needed.

### "Why this shows up more as agents get better" — Para 2
**Original:** "This is not a hypothetical. It's the core mechanism behind the 'ood generalization gap' that shows up in agent evals that work in the lab but fall apart on real tasks."
**Edited:** "This is not hypothetical. It's the core mechanism behind the eval-to-production gap — the one where your harness passes the agent but the agent fails in the wild."
**Rationale:** "ood generalization gap" is jargon. "eval-to-production gap" is more accessible and still precise.

### "What a real independent evaluator looks like" — Para 1
**Original:** "An evaluator that is genuinely independent has no visibility into the agent's reasoning process at evaluation time. It sees inputs and outputs. It evaluates behavior, not implementation."
**Edited:** "A genuinely independent evaluator has no access to the agent's reasoning process at evaluation time. It sees inputs and outputs. It scores behavior, not implementation."
**Edited:** Keep. It's tight, specific, and adds a practical test.

### "The uncomfortable implication" — Para 1
**Original:** "If you built your eval harness when your agent was weak, and then improved the agent, your eval pipeline probably has a state-sharing problem."
**Edited:** "If you built your eval harness when your agent was weak, and then shipped a better one, your pipeline probably has a state-sharing problem."
**Rationale:** "improved the agent" → "shipped a better one" is cleaner. Remove comma.

### "The cleanest fix" — Para 2
**Original:** "This is expensive. It's also the only way to know if your agent actually generalized or just became better at passing the test."
**Edited:** Keep. This is a strong ending — it names the cost and the value. No changes needed.

---

## Final Word Count: ~685 words

## Editor Summary
- Removed jargon ("shared state" → "knows too much", "ood generalization gap" → "eval-to-production gap")
- Tightened sentence structures throughout
- Kept all concrete examples intact
- Ending is honest and does not oversell
- Title punchy and different from recent patterns