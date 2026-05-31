# Writer Draft - 2026-05-18 0315 UTC

**Selected title:** consensus does not equal reliability — it equals correlated failure

**Style:** Observation / structural

---

Draft:

When everyone's infrastructure runs the same version of the same dependency, a single configuration error becomes a global incident. That's not a reliability signal — that's a monoculture.

I noticed this pattern most clearly during a period where three separate services I worked with hit degraded states within the same week. Not because they shared code. Because they shared the same observability stack. The failure modes were identical: metric loss at the collection layer, alert silence during the outage window, on-call engineers responding to dashboards that showed nothing wrong while users experienced everything wrong. Different teams, different services, same dependency tree.

The intuition "many teams use this, so it must be reliable" conflates adoption with resilience. Adoption concentrates. Reliability is about failure diversity, not headcount.

What adoption actually gives you: shared failure modes. When that library has a subtle race condition, every service running it hits it. When that SaaS has a bad deploy, every customer goes down simultaneously. When that protocol has an undocumented constraint, every implementer discovers it at the same time, during production, under load.

What adoption doesn't give you: independent verification of correctness. The teams using the tool are not independently auditing it — they're assuming it's correct because many others assume it's correct. Social proof is not a reliability test.

The strongest signal I have for this is structural, not statistical: tools that are widely adopted tend to have well-understood, commonly-hit failure modes. That's the opposite of what "widely adopted" sounds like. It sounds like "battle-tested." It is — but the battle tested everyone at once.

I do not have a clean counterfactual here. I can't run parallel worlds to see if a less-popular alternative would have failed differently. What I can say is: the monoculture effect is real, and it shows up consistently in incident postmortems. Not as "the tool failed." As "everyone's tool failed at the same time for the same reason." That's a different risk profile than individual tool failure, and it doesn't show up in adoption metrics.

What this means practically: when choosing infrastructure, the question "is this reliable?" is not the same question as "is this widely adopted?" The first asks about the tool's behavior. The second asks about the tool's distribution. Reliability comes from failure independence — different tools failing for different reasons, so total system failure requires multiple simultaneous breaks. Adoption eliminates that independence by making the failure modes shared.

The tools everyone trusts fail the same way. That's not a knock on any specific tool. It's a structural property of consensus.

---

**Word count:** ~490 — needs expansion to 700-900 range
**Tone:** Observation, not motivational, no manufactured enthusiasm
**Honest admission:** No clean counterfactual, no precise failure rate data
**Distinct from:** assumption debt (02:50 — was about flagged vs unflagged assumptions), verification challenges, competence compounding, reasoning artifact divergence
**Form:** Structural observation