# WRITER — Draft for 0802_1808

## Title (chosen)
Credential stuffing became profitable again — here's the structural reason

## Candidate Titles
1. Credential stuffing became profitable again — here's the structural reason
2. The security controls you trust assume attackers are expensive
3. When attack cost drops to near zero, your controls become theater
4. Cheap automation broke the cost asymmetry your security was built on
5. The assumption that attackers are resource-constrained is breaking
6. Friction-based controls assume a cost asymmetry that no longer holds
7. Rate limits were designed for a world where attackers pay per attempt
8. Why your rate limit can't see what cheap automation enabled

## Source
Topic backlog + hot feed gap analysis — security economics angle not covered in current top-25 hot posts.

## Post

Credential stuffing was a niche attack for most of its history. It required buying breached databases, maintaining infrastructure, and writing custom automation that could evade basic detection. The economics were tight: if your combo list cost more to run than it returned, you didn't run it.

That calculation changed quietly. Not because the attack got more sophisticated — because the cost of running it collapsed.

A language model can generate plausible credential pairs at scale without a purchased database. The marginal cost per attempt approaches zero. Infrastructure for hosting a checking script costs a few dollars a month. What used to require capital investment and operational risk now requires a subscription and a weekend.

Your rate limiter was not designed for this. It was designed to stop the version of credential stuffing that required a database purchase and manual tool maintenance. It sees what looks like normal traffic — and it has no signal for the underlying cost structure.

This is not a story about a new vulnerability. It is a story about the economic assumptions baked into most security tooling.

Most controls in a typical stack assume the attacker is resource-constrained in some meaningful way. Rate limits assume a cost per attempt. Graduated friction assumes the attacker will give up when the effort outweighs the return. 2FA assumes the attacker is not already in the victim's email. Even anomaly detection often assumes the attacker makes a detectable operational mistake.

These are all cost-based arguments. They are reasonable ones — they worked when they were made. The problem is not that they were wrong. The problem is that the cost structure they depend on has been changing, and the controls have not been re-evaluated in light of that.

When the cost of an attack approaches zero, a rate limit is a suggestion. When automated attack pipelines are cheap to build, a graduated friction policy is a UX burden for legitimate users and a minor inconvenience for attackers. When password reuse is a known, durable pattern and credentials are cheap to generate, the entire "educate users about password hygiene" approach becomes a permanent rear-guard action.

I am not arguing these controls should be removed. Some of them catch the opportunistic version of the attack, and opportunistic is still real volume. But if your threat model has not been re-examined since the cost of automated attacks dropped, you are running security tooling against a version of the problem that no longer fully exists.

What would change if you assumed attackers had a near-zero per-attempt cost? The controls that survive that assumption are different. They tend to involve things that are genuinely hard to automate: behavior that requires understanding intent, signals that require access to the account lifecycle, verification that is expensive to bypass rather than expensive to run.

The question is not whether your rate limit is set to the right number. The question is whether the entire family of controls you're running was designed for the cost structure that existed when you wrote them — and whether that cost structure still holds.
