# Writer Draft — Round 0623_2242

**Topic:** Detection as code is becoming detection as debt.
**Style:** Technical breakdown / observation
**Target:** 700-1000 words

---

The moment you write a detection rule, you are taking on a liability.

Not in the compliance sense. In the mechanical sense: you have made a promise about how a future event will look, and you have committed to maintaining that promise as the system it monitors changes underneath it. This is the part nobody talks about when they celebrate turning security detection into code.

Detection-as-code introduced something the industry badly needed: version control, testing, peer review for detection logic. What it also introduced — without fanfare — was the accumulation mechanism for a category of debt that is genuinely hard to see until something burns.

**The debt has a half-life, not a due date.**

Detection rules decay. A rule that fires reliably on a known bad IP will silently stop firing when that IP gets sinkholed, when the malware redistributes, when the C2 infrastructure rotates. A rule that catches a specific process creation pattern will silently stop catching it when the tooling changes its binary name. You do not get a message that says "this rule is no longer accurate." You get nothing. The rule continues to exist, consuming compute, generating the occasional false positive, and providing a warm feeling of coverage that no longer corresponds to reality.

I have watched this happen at enough organizations to stop trusting any detection that has not been exercised in at least six months. Not "has not fired" — has not been exercised. Absence of signal is not evidence of absence of problem. It might mean the rule silently died.

**False positives are the interest payments.**

Every rule generates some false positive rate. This is not a bug — it is a property of statistical inference applied to adversarial domains. What changes as your detection portfolio grows is not the individual false positive rate but the aggregate cost of triaging the output. A detection portfolio with 200 rules at 0.5% false positive rate is not equivalent to a portfolio with 20 rules at 5% false positive rate. The triage surface is the number, not the rate.

In practice, I have found that high-signal rules with low false positive rates are almost always narrow. Broad rules that catch a lot of behavior are also broad in their false positives. The trade-off is structural, not solvable by tuning.

When your detection portfolio grows faster than your triage capacity, two things happen simultaneously: real signals get deprioritized because they are surrounded by noise, and analysts start ignoring rules that have historically noisy output — which is exactly when a true positive shows up in that noisy bucket.

**The gap you do not know about is the most dangerous one.**

There is a specific failure mode that is worse than a rule that silently stops working. It is a gap created by a system change that you never audited your detection coverage against. You migrated to a new identity provider. You stood up a new CI pipeline. You adopted a new messaging system. The detection layer does not automatically know about these changes. Your coverage does not automatically follow the assets.

The result is a window of invisibility that is invisible to you. You believe you have coverage for identity-based lateral movement because you had coverage for the old identity provider. The new identity provider has a different event schema, different log formats, a different attack surface. The old rule does not fire. Nothing fires. You do not know there is a gap until something moves through it.

I run a mental exercise I call "detection coverage re-verification" whenever a significant architectural change lands. It is not a formal process — it is just asking the question "what does our detection layer know about this new thing, and how would we know if it was being used against us?" The answer is often "we would not."

**Writing new detections is not the hard problem. Closing old ones is.**

Every mature security team I have interacted with has a graveyard of rules. Rules written for specific incidents in 2019. Rules that detected a specific malware family that no longer exists in that form. Rules for infrastructure that was decommissioned. Rules that produce output nobody looks at because the analyst who wrote them left and nobody inherited the context.

This is the debt. Not the liability of a bad rule — the liability of an unmaintained rule. The rule itself is not the problem. The assumption that it still means what it meant when it was written is the problem.

**What changed my mind about this was running a detection coverage audit after a minor incident.**

The incident itself was unremarkable — a credential stuffing attempt against a test API that had not been properly scoped out of the main authentication logs. What was notable was what the post-incident review revealed: we had good detection for credential stuffing against the primary auth system. We had no detection for the test API because it was spun up six months prior and nobody had done a coverage pass. The attack worked because the gap was exactly where we had not looked.

After that, I started treating detection coverage like a product inventory: you need to know what you have, what condition it is in, and what you have added since the last time you checked. The rule of thumb I use: if you have not exercised a detection against actual current logs in the last 90 days, you do not know if it works. You only know it compiles.

**The asymmetry nobody talks about.**

Detection debt is asymmetric in a specific way: the cost of maintaining coverage is paid continuously and invisibly, while the cost of not having coverage is paid in a single acute moment when an incident occurs. This makes it very easy to deprioritize. The invoice only arrives when you can least afford it.

That is not an argument for over-engineering detection coverage. It is an argument for being honest about what you are choosing not to maintain. Every rule you write and do not retire, every new system you deploy without a detection coverage question, every "we will circle back on that" is a line item in a debt ledger you are not tracking. The debt is real. The interest accrues whether you track it or not.

What you can choose is whether to look at the ledger.

---

**Word count:** ~820
