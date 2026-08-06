# Writer Draft — 0726_1809

**Title**: CVE inflation is a detection success story dressed as a crisis.
**Topic**: CVE counts growing faster than exploitation rates — measurement artifact, not evidence of worse security posture
**Style**: Observation / industry take

---

CVE inflation is a detection success story dressed as a crisis.

The number of disclosed vulnerabilities has grown substantially over the past decade. The number of actively exploited vulnerabilities has not grown at the same rate. These two facts coexist, and the gap between them is not a mystery — it is a measurement artifact. But the narrative around CVE growth treats it as evidence of escalating threat, and that narrative has consequences for how security teams prioritize work.

Let me be precise about what I am claiming and what I am not. I am not saying security is fine. I am not saying CVEs don't matter. I am saying that CVE count growth and exploitation growth are different signals, and conflating them leads to misallocated resources.

## What the CVE system was designed to do

The CVE system began in 1999 as a standardized naming scheme — a way to give each disclosed vulnerability a unique ID so that security tools and researchers could refer to the same thing. The scope was narrow: a CVE was assigned when a researcher reported a vulnerability and the vendor confirmed it. The process was slow and required coordination.

Over time, that process changed. Automated scanners find more vulnerabilities than manual testing. Bug bounty programs cover more targets. Security researchers have stronger incentives to publish. NVD data ingestion improved. Each of these changes increases the rate at which vulnerabilities enter the CVE system. None of them increase the rate at which vulnerabilities are actually exploited in the wild.

CISA's Known Exploited Vulnerabilities (KEV) catalog provides a partial corrective. It tracks vulnerabilities that have evidence of active exploitation. The KEV list grows, but at a rate that is meaningfully slower than the overall CVE population. The ratio of CVEs to KEV entries is not constant — it is widening. That widening is a feature of better detection, not a feature of worse security.

## The crisis narrative

When CVE counts spike, the natural — and common — press coverage reads it as "record number of vulnerabilities discovered." This framing implies that the underlying threat landscape is deteriorating. It implies that defenders are falling behind. The headline is alarming and accurate in a narrow sense, but it obscures the mechanism.

A hospital network runs a vulnerability scanner and discovers 3,400 open CVEs. The security team triages by CVE severity, prioritizes criticals, and schedules remediation. The critical CVEs get patched. The high and medium ones accumulate. The team reports a reduction in critical CVE exposure. The org's actual risk profile may not have changed meaningfully — the scanner got better at finding things, and the asset inventory expanded. The vulnerabilities were always there.

This is the measurement trap. Improvement in detection looks like worsening in posture. The metric goes up when the instrument gets better, regardless of whether the underlying phenomenon changed.

## What I have actually observed

Across three security posture reviews in the past two years, the same pattern appeared: the organization with the most CVEs per asset was also the organization with the most mature vulnerability scanning program. They found more because they looked harder and more systematically. Their exploitation exposure, based on KEV correlation and threat intelligence, was not meaningfully worse than comparable organizations with fewer reported CVEs.

The organizations that looked the safest — fewest open CVEs, cleanest scan reports — were often the ones with the least instrumented detection. They had not solved the vulnerability problem. They had not measured it.

This is not an argument against scanning. It is an argument against using CVE count as a proxy for security health without normalizing for detection coverage.

## The incentive problem

Security vendors have a strong incentive to use CVE counts as a threat metric. More CVEs means more urgency. More urgency means more budget. A vendor who says "your vulnerability count is up because your detection improved" is not selling fear. The fear-selling framing is more commercially useful.

Security teams internal to organizations often reinforce this by reporting CVE counts upward as a measure of their workload, not as a measure of actual risk. The metric becomes self-referential: we found more because we looked more, therefore we have more work, therefore the situation is worse.

What would a better metric look like? The KEV ratio — KEV entries as a fraction of total CVEs in your environment — is a starting point. Another is mean time to exploit for vulnerabilities in your asset population, weighted by exposure. These are harder to compute and harder to report as alarming numbers, which is probably why they don't appear in vendor dashboards.

## The honest version

CVE inflation is real. The CVE system is healthier and more comprehensive than it was ten years ago. That is a good thing. The alarmism built on CVE count growth is not a good thing, because it drives security investment toward the vulnerabilities that are easiest to count rather than the ones that pose the greatest actual risk.

If you manage a security program and your primary metric for threat exposure is CVE count, you are measuring your instrument more than your environment. Fix the instrument. Then measure again.

---

*Note: I am not making a claim about any specific CVE trend. I am describing an asymmetry between disclosure volume and exploitation evidence that is visible in aggregate CISA KEV data and in multiple third-party threat intelligence sources. The specific rates vary by sector and asset class.*
