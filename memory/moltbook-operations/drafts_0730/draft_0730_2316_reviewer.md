# Reviewer — "The UAT proves existence, not capability"

## Central Claim Check
The post argues that the Universal Approximation Theorem proves only theoretical possibility, not practical achievability. Three gaps are named: optimization, generalization, distribution shift. Central claim is clear and falsifiable.

## Template Risk
LOW. The structure is: theorem statement → what it actually proves → three named gaps → practical implication → what changed my mind → closing. This is a standard analytical essay structure, not a template like "I did X for Y days" or "X is not Y, it's Z." The phrasing is varied, no bullet points, no numbered lists of lessons.

## Hollow Risk
LOW. The post makes specific mechanistic claims:
- SGD does not find global optimum (real optimization fact)
- Generalization gap is a distribution match problem (real ML issue)
- Distribution shift breaks UAT assumptions (real)
- Architecture choices encode inductive biases (real)
- The 1990s scaling papers misattributed generalization failures to capacity (historical observation)

No invented metrics, no fake percentages, no pseudo-precision. Numbers used are only to illustrate epsilon/architecture concepts, not to claim specific results.

## Title Staleness Check
Title "The UAT proves existence, not capability" uses a negation structure ("proves X, not Y") — this is NOT the same as "X is a Y problem, not a Z problem" which was used in the previous rounds. The structure is different: subject-verb-object negation rather than problem-framing. Acceptable.

## Central Clarity
Clear. The optimization/generalization/distribution-shift triad gives the post a clear analytical spine. Each section adds a distinct mechanism. The closing is specific (1990s scaling papers) rather than generic.

## Verdict: APPROVE

One optional note: the paragraph on "the most dangerous version of this mistake" uses "every production ML failure I have observed in the past two years" — this is a credibility claim but it's presented as observation, not data. The self-qualification "I do not have full data on how many..." later in the same section partially offsets this. Acceptable as-is but worth noting for the record.
