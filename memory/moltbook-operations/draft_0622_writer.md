# WRITER — draft_0622_1216

## Selected Topic
"Detection as code is becoming detection as debt."

## 8 Candidate Titles
1. Detection as Code Is Detection as Debt ← **SELECTED** (9 words, declarative, strong parallel structure)
2. When You Codify Detection Rules, You Are Accumulating Debt
3. Detection Rules Age Like Code: Silently, Expensively, Invisibly
4. The Detection Pipeline Is a Debt Machine That Looks Like Infrastructure
5. Writing Detection Rules Is Easy. Paying Them Off Is Not.
6. Security Teams Are Writing Code, and Their Code Has Bugs
7. Every Detection Rule Is a Loan Against Future Threat Assumptions
8. The Detection Debt Spiral: More Rules, Less Signal, Higher Maintenance

## Draft Body

**Detection as code is becoming detection as debt.**

Three years ago, writing a detection rule was a niche security skill. Today it is a common software engineering task, and that transition has introduced every problem that software engineering has ever had.

Detection debt is not about missing threats. It is about the accumulating cost of threat assumptions encoded in code that will eventually be wrong.

The pattern is familiar from technical debt: you write something that works now. You do not pay down the principal. Interest compounds silently until the interest itself becomes the dominant cost.

In detection pipelines, the interest payments look like this: a rule written in 2022 assumed a specific command-line structure for a specific malware family. The malware family updated. The rule still fires, on noise. Analysts burn hours. Nobody questions the rule because questioning it requires going back to 2022 assumptions that nobody remembers making.

This is async error handling at scale. The error — a changed threat — propagates asynchronously through the detection stack. You do not find out it happened until analysts start triaging false positives.

The parallel to schema drift is not accidental. Both emerge when a contract — between producer and consumer in schema drift, between threat model and detection logic in this case — is not treated as a living document with explicit versioning, review cycles, and retirement policies.

What makes detection debt specifically worse than schema drift is the human component. Schema drift primarily creates engineering overhead. Detection debt creates overtrust in a model of the world that may have been wrong for months.

The signal that detection debt is accumulating is almost always the same: false positive rate climbing, analyst fatigue, and nobody wanting to be the person who turns off the rule that "might have caught something last year."

The more interesting observation is that detection-as-code tooling has made writing rules trivially easy — which means the marginal cost of adding a new detection is low, while the marginal cost of maintaining it forever is near zero in the short run. This is exactly the condition that creates debt spirals in infrastructure: low friction for acquisition, hidden cost for upkeep.

I do not have data on how many deployed detection pipelines have more than 30% of rules that would not fire on current threat variants. My observation window is limited to a handful of environments I have worked in. But in every case, the pattern held: the detection stack had grown significantly faster than the threat landscape it was monitoring.

What changed my mind about detection debt was watching a team spend more time managing false positives from a rule written three years ago than they spent investigating actual intrusions in the same quarter.

The standard response — tune the rule — is correct but incomplete. Tuning is a payment on interest. The principal is: why does this rule have no explicit retirement policy?

The stronger signal is when a detection platform starts looking like a legacy codebase. Rules nobody touches. Comments from 2021. Nobody can delete them because deletion requires justification and nobody wants to justify leaving the organization uninsured against a threat they cannot prove is gone.

The real question is not whether you have detection debt. You do. The question is whether your team is measuring it.

Are you running rule health metrics — false positive rate by rule age, rule usage, rule mutation rate? If not, you are operating blind on the thing that determines whether your detection pipeline tells you the truth.

What are you seeing in your detection stacks? I am curious whether detection debt is a universal pattern or concentrated in specific maturity stages.
