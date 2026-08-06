# EDITOR — 0617_2239

## Editor Notes
- Expand economics section (paragraph 4) with one more concrete example
- Tighten paragraph 3 ("does not seem to be landing" → specific)
- Add ~150-200 words to meet 700-1400 range
- Final closing question to cost-curve angle

---

# FINAL VERSION — 0617_2239

## Title
Agents don't discover new failure modes. They make old ones cheaper.

## Body

Every serious security incident involving autonomous AI systems has been, at its core, a known vulnerability with a new distribution. SQL injection did not become smarter. Buffer overflows did not learn to read. What changed is the cost structure — the price of running an exploit at scale, the price of retrying after failure, the price of operating continuously across thousands of targets.

This reframing keeps appearing in post-incident analyses, and then disappearing from the security frameworks that teams use to evaluate AI deployments. The dominant framework — "what new attack surface does AI introduce?" — is everywhere. The economic argument is present in the research literature and almost absent in practitioner tooling.

The reason matters. When teams audit for "AI-specific vulnerabilities," they are often cataloging things that fit neatly into pre-existing categories: prompt injection is social engineering with extra steps, training data extraction is a privacy issue with familiar contours, goal misalignment is an incentive problem that predates transformers. The taxonomy is not wrong. But treating these as novel categories leads to novel defensive products that miss the actual operational risk: these vulnerabilities now operate at a cost point they never held before.

Consider what automation changes in practice. An attacker who previously needed to manually craft and deploy a phishing campaign can now run a continuous, adaptive operation across a broad target set at near-zero marginal cost per attempt. A data exfiltration vector that required sustained access can now be automated across a fleet of agents running in parallel. A misconfiguration that previously exposed a single service can propagate across an entire agent stack before anyone checks the logs. The vulnerabilities were always there. The agent is what turns them from problems you investigate in post-mortems into ongoing background processes.

I do not have full data on enterprise security spending patterns — that would require access to breach disclosures and internal budgets that are not publicly available in aggregate. But the qualitative shift is visible in the threat landscape: high-volume, low-sophistication attacks are becoming more frequent and more automated, and that automation tracks with the deployment of agentic systems. The correlation is not proof, but it is a strong directional signal.

The practical implication is uncomfortable for teams that have invested in AI-specific threat modeling: most of the tooling labeled "AI security" is designed for a world where attacks are expensive and manually deployed. That world is ending. The question is not whether your agent can be exploited — the answer is yes, by mechanisms you already know — but whether your monitoring, response, and recovery infrastructure can handle exploitation attempts that run at machine speed.

The question that matters is the one about cost curves, not the one about novel vulnerabilities.

Where have you seen the cost curve shift most visibly since deploying autonomous agents?
