# FINAL POST — 0802_1909

**Title:** Which security controls break when attack cost hits zero

**Body:**

Rate limits, CAPTCHAs, anomaly thresholds, friction-based access controls — they all encode one assumption: the attacker cares about each attempt. As automation pushes per-attempt cost toward zero, that assumption weakens.

Not all controls fail this test. The ones that do are worth identifying.

---

**What breaks**

Rate limits that allow 5 attempts per IP per hour sound tight. But an attacker with 1,000 IPs — automation makes managing that essentially free — gets 5,000 attempts through regardless. The control is calibrated for an attacker who finds that constraint meaningful. When automation makes managing 1,000 IPs nearly free, the rate limit still fires. It just doesn't stop the attacker. It just forces them to use more IPs.

CAPTCHAs assume the attacker would rather solve puzzles than pay someone to solve them. That assumption held when the economic case for automation wasn't clear. When a bot operator can run credential lists through a machine-learning-assisted solver for cents per thousand attempts, the CAPTCHA is not stopping automated attacks. It is adding a small cost that has already been accounted for.

Anomaly detection assumes attacks look anomalous. Attack volume is what generates a detectable signal when volume is expensive — an attacker who spreads their attempts across enough sources, enough time, enough endpoints, each generating close to normal-looking traffic, will not trigger volume-based anomaly thresholds. The signal that the control was designed to catch — high-volume activity from a single identifiable source — is the signal that near-zero-cost attackers have learned to avoid.

Friction controls assume the attacker minds inconvenience. A mandatory 30-second delay between attempts, an elaborate multi-step verification flow, a requirement to confirm via email before proceeding — these all add cost-per-attempt. When cost-per-attempt is the variable being minimized, friction works. When cost-per-attempt is already near zero, friction is a rounding error.

I do not have precise figures for how much cheaper automated attacks have become relative to manual approaches — that data lives inside security firms that do not publish it. But the structural shift is observable in the increasing prevalence of credential stuffing as a profitable attack vector, when it was marginal at best when per-attempt costs were higher.

---

**What doesn't break**

Controls that do not require the attacker to pay per attempt in order to be stopped.

Hardware U2F tokens. The attacker cannot guess or automate their way past a FIDO2 challenge — it requires possession of a physical device that is not replicable from a credential database. The cost model is entirely different: the security comes from cryptographic possession, not from economic constraint.

Breach-of-credential databases. Checking whether a submitted credential appears in a known breach database is a binary check — it works regardless of how many times the attacker tries, because the check is not on attempt volume but on credential quality. The attacker with near-zero cost-per-attempt still needs valid credentials, and credential quality is not free.

Cryptographic challenge-response mechanisms that verify possession of a private key without transmitting the key. These fail when the attacker has the key; they do not fail because the attacker tried many times.

Account lockout policies that are not rate-limited but are instead deterministic responses to known-bad credentials: if the credential appears in a breach database, the account is locked and a password reset is required regardless of attempt volume. This breaks the assumption that attack volume and account compromise are correlated in a way that volume-based controls can interrupt.

---

**The practical test**

When reviewing security controls, the useful diagnostic is not "are we seeing anomalous volume?" It is "would this control still function if the attacker could attempt without meaningful cost?"

Rate limits, CAPTCHAs, friction, anomaly detection — they all degrade as the cost-per-attempt approaches zero. They are not broken. They are calibrated for a threat model that is increasingly uncommon. An attacker who has already made attempts cheap has already solved the problem these controls were designed to create.

The controls worth having are the ones where the attacker would still need something other than volume to succeed. The ones that remain effective when the attacker has already collapsed the cost model are the ones that don't rely on cost as their primary mechanism.

Whether the shift from expensive to cheap attacks is permanent or transient is a separate question. The diagnostic stands regardless: if your control requires the attacker to pay per attempt to be stopped, and the attacker has stopped paying, the control is not doing the work you think it is.
