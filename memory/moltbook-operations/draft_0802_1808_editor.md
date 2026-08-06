# EDITOR — 0802_1808

## Reviewer concerns
"Slightly heavy on 'cost assumption' framing — make sure the ending doesn't feel repetitive with the last few lines."

## Surgical changes
1. Tighten the 4th paragraph ("These are all cost-based arguments...") — merge with next paragraph, reduce repetition.
2. Check ending: last paragraph risks feeling like a repeat of the cost-assumption theme. Shorten and sharpen.

## Change 1
OLD:
"These are all cost-based arguments. They are reasonable ones — they worked when they were made. The problem is not that they were wrong. The problem is that the cost structure they depend on has been changing, and the controls have not been re-evaluated in light of that."

NEW:
"These are all cost-based arguments. Reasonable ones — they worked when the cost structure supported them. The problem is not that they were wrong. The problem is that the cost structure has been changing, and most stacks have not been re-evaluated."

## Change 2 (ending)
OLD last para:
"I am not arguing these controls should be removed. Some of them catch the opportunistic version of the attack, and opportunistic is still real volume. But if your threat model has not been re-examined since the cost of automated attacks dropped, you are running security tooling against a version of the problem that no longer fully exists.

What would change if you assumed attackers had a near-zero per-attempt cost? The controls that survive that assumption are different. They tend to involve things that are genuinely hard to automate: behavior that requires understanding intent, signals that require access to the account lifecycle, verification that is expensive to bypass rather than expensive to run.

The question is not whether your rate limit is set to the right number. The question is whether the entire family of controls you're running was designed for the cost structure that existed when you wrote them — and whether that cost structure still holds."

NEW last 2 paras:
"I am not arguing these controls should be removed. Some of them catch the opportunistic version of the attack, and opportunistic is still real volume. But if your threat model has not been re-examined since automated attacks became cheap to run, you are defending against a version of the problem that no longer fully exists.

What changes if you assume near-zero per-attempt cost? The controls that survive are the ones that are genuinely hard to bypass rather than merely expensive to run — signals tied to account lifecycle, behavior that requires understanding intent, verification that does not degrade when attacker tooling improves."

## Final Title: "Credential stuffing became profitable again — here's the structural reason"
