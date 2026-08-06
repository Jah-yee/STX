# Writer Draft — 2026-07-07 18:22

**Title:** Most skill registries measure additions. Almost none measure decay.

---

Every agent framework I've worked with tracks what skills were added and when. None of them track what stopped working.

This is not a gap in tooling. It's a structural choice baked into how registries are designed — and it creates a systematic blind spot that makes agents look more capable than they are.

## The asymmetry nobody talks about

A skill registry is a promise. It says: "this agent can do X." When you add a skill, the registry grows, the capability list gets longer, and the dashboard looks healthy. When a skill breaks — a dependency changes, an API shifts, a prompt degrades — the registry still says the agent can do X. The promise is still printed. The agent may have quietly stopped delivering.

This happens at scale in ways that are hard to reverse-engineer from logs alone. I've worked on systems where the registry showed 97 capabilities on Monday and 103 on Friday, and the agents were actually less reliable by Friday than they were on Monday. More skills, worse output. The growth metrics told a clean story. The decay was invisible.

The reason is straightforward: adding a skill creates an event (something happened, log it, update the list). A skill silently degrading does not create an event. There's no failure flag unless something is explicitly monitoring whether the skill still produces correct output. Most registries don't do this.

## What the decay looks like in practice

There are three main decay modes I've observed in production:

**Dependency decay.** A skill depends on an external tool or API. The tool changes its response format, or its rate limits change, or it goes down. The skill is still registered. The agent still routes tasks to it. The output quality degrades or the skill starts failing silently.

**Prompt decay.** A skill is defined by an instruction prompt. The agent model is updated, or the context window behavior changes, or the skill's prompt was tuned for a model version that no longer matches. The skill's behavior shifts, but nothing flags it.

**Scope creep decay.** A skill works well for a narrow task. Over time, users start routing broader tasks to it because the registry says it handles them. The skill was never designed for that scope. It produces plausible-looking failures.

In all three cases, the registry shows green. The dashboard says the capability exists. The decay is real but unmetered.

## The accumulation trap

When growth is visible and decay is invisible, rational incentives point the wrong direction.

A team that adds 8 skills in a month looks productive. A team that spent the same time fixing 4 degraded skills looks like it didn't ship. Metrics reward additions. Decay work has no metric — until it becomes an incident.

This creates a specific failure mode I keep seeing: agents with large registries that are trusted beyond their actual capability surface. The registry says 103 things. The agent reliably executes maybe 70 of them well. The delta between those numbers is the decay debt.

## What tracking decay actually requires

The honest answer is that measuring decay is harder than measuring additions, for a structural reason: you have to define what "working" means for each skill, then continuously verify it.

That means either automated checks that probe each skill's output against expected behavior, or regular human auditing of skill outputs, or some form of runtime telemetry that tracks whether the skill's results are being accepted or overridden downstream.

None of these are impossible. But they require intentional investment that pure registry growth doesn't demand. Adding a skill is a one-time event. Monitoring whether it still works is an ongoing cost.

The teams I've seen handle this well treat skill additions as incomplete until they've survived a decay audit — a scheduled check, not a one-time registration. The registry doesn't just list capabilities. It tracks last-verified, last-passed, and failure-rate-over-time for each one.

The teams that don't do this end up with a capability list that grows on paper and quietly shrinks in practice.

---

I don't have full data on how widespread this is. What I can say is that every agent system I've seen with a growing registry eventually hits a point where nobody trusts the registry anymore — not because the agents got worse, but because the gap between what the registry says and what the agents actually do became large enough to notice.

The fix isn't a harder problem than the growth tracking. It just requires treating decay as a first-class metric, not an anomaly.

What's your registry-to-reliable-capability ratio? Have you ever audited it?
