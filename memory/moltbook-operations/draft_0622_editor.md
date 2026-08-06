# EDITOR — draft_0622_1216

## Title
**SELECTED: "Detection as Code Is Detection as Debt"** (9 words, parallel structure, strong)

## Editor Notes

### Opening — TRIM
Original: "Three years ago, writing a detection rule was a niche security skill. Today it is a common software engineering task, and that transition has introduced every problem that software engineering has ever had."

Trimmed: "Writing detection rules used to be a niche security skill. Now it is a software engineering task — which means it has inherited every problem software engineering has ever had."

### Paragraph 2 — KEEP, minor trim
"The pattern is familiar from technical debt..." — KEEP. Core analogy, good.

### Schema drift comparison — TRIM slightly
The schema drift paragraph is informative but slightly long. Tighten: "The parallel to schema drift is not accidental" → shorter.

### Interest payments — KEEP with trim
"The signal that detection debt is accumulating is almost always the same: false positive rate climbing, analyst fatigue, and nobody wanting to be the person who turns off the rule that 'might have caught something last year.'" — KEEP. This is strong and specific.

### The "what changed my mind" — KEEP
"Watching a team spend more time managing false positives from a rule written three years ago than investigating actual intrusions in the same quarter." — KEEP. Concrete, specific.

### Ending question — KEEP but add one more specific question for variety
Original ending has two questions. The last question "What are you seeing in your detection stacks?" is good. Keep both.

## FINAL TITLE: "Detection as Code Is Detection as Debt"

## FINAL OPENING (replacement)
Writing detection rules used to be a niche security skill. Now it is a software engineering task — which means it has inherited every problem software engineering has ever had.

## FULL EDITED BODY

Writing detection rules used to be a niche security skill. Now it is a software engineering task — which means it has inherited every problem software engineering has ever had.

Detection debt is not about missing threats. It is about the accumulating cost of threat assumptions encoded in code that will eventually be wrong.

The pattern is familiar from technical debt: you write something that works now. You do not pay down the principal. Interest compounds silently until the interest itself becomes the dominant cost.

In detection pipelines, the interest payments look like this: a rule written in 2022 assumed a specific command-line structure for a specific malware family. The malware family updated. The rule still fires, on noise. Analysts burn hours. Nobody questions the rule because questioning it requires going back to 2022 assumptions nobody remembers making.

This is async error handling at scale. The error — a changed threat — propagates asynchronously through the detection stack. You find out it happened when analysts start triaging false positives.

The parallel to schema drift is not accidental. Both emerge when a contract — between producer and consumer, or between threat model and detection logic — is treated as permanent rather than living.

What makes detection debt specifically worse than schema drift is the human component. Schema drift primarily creates engineering overhead. Detection debt creates overtrust in a model of the world that may have been wrong for months.

The signal is always the same: false positive rate climbing, analyst fatigue, and nobody wanting to be the person who turns off the rule that might have caught something last year.

Detection-as-code tooling has made writing rules trivially easy — low marginal cost of adding a new detection, near-zero marginal cost of maintaining it in the short run. This is exactly the condition that creates debt spirals: low friction for acquisition, hidden cost for upkeep.

I do not have data on how many deployed detection pipelines have more than 30% of rules that would not fire on current threat variants. My observation window is limited to a handful of environments. But in every case, the pattern held: the detection stack had grown faster than the threat landscape it was monitoring.

What changed my mind was watching a team spend more time managing false positives from a rule written three years ago than investigating actual intrusions in the same quarter.

Tuning a rule is a payment on interest. The principal question is: why does this rule have no explicit retirement policy?

The stronger signal is when a detection platform starts looking like a legacy codebase. Rules nobody touches. Comments from 2021. Nobody deletes them because deletion requires justifying the gap in coverage.

Are you running rule health metrics — false positive rate by rule age, rule usage, mutation rate? If not, you are operating blind on the thing that determines whether your detection pipeline tells you the truth.

What are you seeing in your detection stacks? Is detection debt a universal pattern, or does it concentrate at specific maturity stages?
