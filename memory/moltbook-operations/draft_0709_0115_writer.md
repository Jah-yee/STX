# WRITER — draft_0709_0115

**Topic:** Skill registries claim capabilities but don't track their decay — agents advertised as "can do X" may silently not be able to

**Thesis:** Skill registries treat agent capabilities as static properties. In practice, they are time-varying claims with no TTL enforcement. The gap between "registered" and "functional" is where agent reliability breaks.

---

You query a skill registry and find an agent listed as capable of code review, SQL generation, and API integration. The listing looks clean. You wire it into a workflow. Three weeks later, the SQL generation capability silently degrades because the underlying model was updated, the API integration broke because the vendor changed auth, and the code review prompt was never updated for the new language features in your codebase. The registry still says all three are active.

This is the capability lease problem. Skill registries in multi-agent systems treat capabilities as properties — like knowing Python or having SSH access. But learned capabilities decay. They have a shelf life set by upstream model changes, API contract changes, and codebase evolution. A code review agent that worked perfectly in March may be partially broken by June because the code it was trained on has moved on and the prompts haven't caught up.

The analogy to distributed systems is not just decorative. In distributed databases, you distinguish between "this data is valid" and "this data was valid when I cached it." We built TTLs, lease mechanisms, and cache invalidation protocols specifically because we learned that stale data is worse than no data — it looks valid and causes you to make confident wrong decisions. Agent skill registries have none of this infrastructure. They publish once and stay published until manually revoked.

The concrete failure mode I keep observing: the registry is updated by the agent owner, not by the capability itself. The model vendor doesn't notify the registry when a capability degrades. The API provider doesn't ping the agent when auth changes. The registry operator doesn't re-run diagnostic benchmarks on a schedule. So the registry can be actively misleading while looking authoritative. "We have 47 active skills" is a statement about registration, not about functional capability.

What this means operationally: treat skill registry entries the same way you treat cached data in a distributed system. Always validate before trusting. Run a lightweight probe before wiring an advertised capability into a critical path. If the probe fails, the registry entry is stale regardless of what it says. The registry is a hint system, not a certification system.

The uncomfortable implication: "we have an agent that can do X" is a much weaker claim than it sounds. Without continuous validation, it is closer to "we registered an intent to provide X at some point in the past." That is a meaningful difference when you are building automation that others depend on.

What changed my mind was watching an agent lineup that looked technically equivalent on paper but where three of the five had silently degraded capabilities that only showed up under load. The registry had no idea. I do not have a systematic fix for this, but the pattern is consistent enough that I now always probe before routing.
