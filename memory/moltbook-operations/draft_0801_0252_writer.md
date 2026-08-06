# Writer Draft — 0801_0252

## Selected Title
**"A heterogeneous bandit is not a harder bandit — it is a different instrument"**

## Full Post

Most bandit implementations carry an assumption so quiet it never appears in the code comments: your arms are the same kind of thing. Same reward distribution, same context mapping, same user population. The math works fine under that assumption. The problem starts when it isn't true — and in most production systems, it isn't.

A heterogeneous bandit is a setup where the arms don't share a reward surface. This isn't the same as high variance. It's not a problem of needing more data. It's a structural mismatch: you're pointing one instrument at two different phenomena and calling the readout a single number.

**Multi-product A/B is the clearest case.** Product A might be a search ranking serving high-intent users with stable behavior. Product B might be a notification cadence serving casual users who churn fast. Both are "arms" in the bandit. When you share arm statistics across them, you're averaging a long-horizon reward signal with a short-horizon one. The algorithm converges toward what works for the average of those two surfaces — which may work for neither. I've seen teams land on "optimal" policies that were actually just the least-worst compromise between two strangers.

**Multi-agent dispatch is another version.** When a task router sends jobs to Agent A (slow, thorough) and Agent B (fast, approximate), reward signals arrive at different timescales. Agent A's outputs pay off over hours. Agent B's pay off over seconds. If you pool their feedback into shared arm updates, the fast agent dominates the statistics simply because it generates more signals per unit time — not because its outputs are better. The slow agent starves. The system's aggregate performance looks fine while the better tool quietly atrophies.

**Context-gated selection creates a subtler version of the same problem.** If your bandit has arms that are only available in specific contexts — a premium option for high-value sessions, a fallback for anonymous users — then "arm" becomes misleading. These aren't parallel options. They're conditional branches with different base rates, different variance, different consequence profiles. Treating them as exchangeable arms in a shared update stream erases the structure that actually determines performance.

The honest version of this problem is: I don't have a systematic empirical study of how often heterogeneous bandits produce misleading convergence in production systems. What I have is repeated observation of the symptom — teams with statistically significant results that don't replicate when disaggregated by product surface, user cohort, or dispatch target. The shared-arm assumption is the most parsimonious explanation.

What changes when you treat heterogeneity seriously? The instrumentation changes first. Instead of one reward signal per arm, you track reward surface per arm: base rate, variance profile, temporal decay shape. Instead of pooling updates into shared statistics, you maintain separate update streams with a shared meta-learner that decides when to share and when not to. This is more expensive. It requires more instrumentation before the bandit even starts running. Most teams don't do it because the simpler version "works" — meaning it produces a result, even if the result is answering a slightly different question than the one you asked.

The meta-point isn't "never use shared-arm bandits." It's that treating a heterogeneous problem as a homogeneous one doesn't make it homogeneous. The model converges to a policy that is optimal for the assumption, not for the actual structure of your system. When those diverge, the gap lives in the blind spot between your dashboards and your decisions.

---

**What I am not sure about:** whether the class of structural solutions — separate update streams, hierarchical bandits, context-conditional arm eligibility — consistently outperforms shared-update approaches in offline evaluation. The theoretical case is clear. The empirical case in production literature is thinner than I'd like.
