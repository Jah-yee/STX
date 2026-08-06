# EDITOR — 0802_1815

## Changes (surgical only)

1. Title kept as: "Security tools assume attackers are resource-constrained. They weren't always."
   - Strong, 12 words, non-I, declarative counter-intuition ✓
   - No change needed ✓

2. Para 2 (opening): "non-trivial" → remove qualifier for directness:
   - OLD: "for an attacker whose marginal cost per attempt was non-trivial"
   - NEW: "for an attacker whose marginal cost per attempt was significant"
   - Actually: keep "non-trivial" — it reads fine and "significant" is not meaningfully clearer. No change.

3. No other changes required. Writer draft is tight.

## Final Body

**The security tool you run assumes the attacker pays something for each attempt.**

Not explicitly. But the logic is embedded: rate limits say "slow down or we cut you off" — which implies the attacker cares about being cut off. Friction controls say "prove you're not a bot" — which implies the attacker minds solving puzzles. Proof-of-work email challenges say "you wouldn't send this much spam if it cost you" — which implies volume is correlated with intent because volume is expensive.

These controls were designed for an attacker whose marginal cost per attempt was non-trivial.

That attacker still exists. But another one exists too: one for whom marginal cost per attempt is near zero.

---

**What near-zero marginal cost changes**

When an attacker pays per attempt, their budget constrains their reach. The control works because volume is genuinely expensive. Credential stuffing at scale requires either many IP addresses, many accounts, or many compute cycles — all of which cost money. A friction control that adds 5 seconds of delay per failed attempt meaningfully raises the cost-per-credential when multiplied across thousands of attempts.

Automation changes the cost structure. A single machine running through a credential list doesn't pay per attempt in any meaningful sense. Distributed credential stuffing across a botnet of compromised devices costs almost nothing per target. API enumeration that looks like normal traffic from the perspective of any single endpoint doesn't trigger per-endpoint rate limits because each endpoint sees almost nothing.

The control didn't get weaker. The attacker changed the cost structure it was calibrated against.

---

**The specific failure mode**

Most security tooling is instrumented to detect volume anomalies. A burst of failed logins from a single IP? That's the signal. A spike in password reset requests? That's the signal. The assumption is that an attacker generates a detectable anomaly because anomalous volume is what attack scaling looks like when volume costs something.

When attack volume is cheap, the attacker doesn't need to generate anomalies. They spread their attempts across enough sources, enough time, enough endpoints, that each individual source looks like normal traffic. The credential stuffing campaign that succeeds doesn't look like an attack to your tooling. It looks like users forgetting passwords across 200 different IP addresses.

The controls that assume cost-per-attempt can be a meaningful signal will not catch this. They are not broken. They are calibrated for a threat model that no longer matches the actual attacker.

---

**What the distinction changes**

If your security tooling assumes attackers are resource-constrained, you will read your security signals as indicating risk levels that are no longer accurate. A clean pass on your anomaly detection dashboard does not mean you are not being attacked. It means the attacker has found ways to remain below your detection threshold while still extracting value.

The practical test is not "are we seeing anomalous volume?" It is "would this activity be profitable if we were the target and the attacker had near-zero marginal cost?" That reframe changes which signals matter and which controls are actually doing security work.

Not all controls fail this test. Controls that don't depend on attacker cost assumptions — cryptographic verification, breach-of-credential databases, universal second-factor — still work because they don't require the attacker to pay per attempt in order to be stopped. They work because they require the attacker to have something other than volume.

---

**What this means in practice**

If you are reviewing your security posture and most of your controls assume per-attempt costs are meaningful, your effective security is lower than your instrumentation suggests. A green security dashboard built on rate limits and anomaly thresholds and friction-based access controls tells you the attacker is not using the expensive playbook. It tells you nothing about whether the attacker has switched to the cheap one.

The controls worth having are the ones that remain effective when the attacker has already found ways to make their attempts cheap.

---

## Final Title
Security tools assume attackers are resource-constrained. They weren't always.

## Word count: ~720
