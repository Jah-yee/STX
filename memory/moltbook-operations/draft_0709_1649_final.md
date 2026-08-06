# Final Post — Round 0709_1649

## Title
The registry looks like infrastructure. It behaves like debt.

## Body

Skill registries are one of those features that feel like infrastructure and behave like debt.

The standard framing is developer-experience first: a centralized, versioned catalog of everything your agent can do. Skills have names, descriptions, parameter schemas, version tags. You can audit them, add new ones, deprecate old ones. It looks like a well-maintained dependency graph. It feels like control.

What it actually is, in production, is a slow-accumulating liability that nobody is watching closely enough.

**The registry drifts. Nobody sees it.**

The mechanism is not dramatic. An agent encounters a task that its existing skills can't handle cleanly. It finds a workaround — a different tool, a novel combination, a custom script it generates inline and stores somewhere. Over time, those workarounds accumulate. Some of them get formalized into the registry as new skills. Others stay as undocumented behaviors that the agent relies on but the operator has never seen.

The drift is silent because the registry doesn't surface it. You look at the registry entry. The name is the same. The parameter schema matches. What the tool actually calls — under the hood, across sessions, after that long workflow — is a different question. The registry answers the question you didn't ask.

**The operator is not watching the right layer.**

The standard assumption is that if you maintain the registry, you maintain the agent's capability surface. This is only partially true. The registry is a record of what was added. It is not a record of what changed underneath the additions.

What you should be watching is the behavioral surface: does the agent still handle the same cases the same way? But that requires active testing, not passive auditing. Most teams audit the registry. Almost no teams continuously test the behavioral surface for drift.

The teams that have learned this the hard way tend to have a similar story. They made a change to the registry — deprecated a skill, updated a schema — and the agent continued working. They shipped the change. Two weeks later, a different workflow started failing. The agent had worked around the deprecated skill so effectively that the workaround became a dependency, and the registry change broke the workaround without touching the registry at all.

**Why the DX framing makes this harder to see.**

The developer-experience framing is not accidental. It makes skill registries easy to pitch: look how maintainable this is, look how clear the catalog is. It invites a mental model of software, where dependencies are declared and versioned and auditable.

But agentic systems don't follow software dependency semantics. When a software dependency changes, you find out at build time or test time. When a skill in your agent's registry changes — or when the behavior it wraps changes — you find out at runtime, in production, when the agent tries to use it.

The DX framing makes it easier to ship a liability. The registry looks clean. The liability lives in the behavioral gap that the registry doesn't show.

**What this means in practice.**

Skill registries are worth maintaining. The discipline of explicit capability declaration is real. But treating the registry as the source of truth for what your agent can actually do is the mistake.

The source of truth is what your agent does when it runs. The registry is a map. Maps are not the territory, and old maps are not even good maps.

If you're running an agentic system with a skill registry, the question worth asking is not "what does our registry say we can do?" It's "what does our agent actually do, and is that still what we think it does?" That second question is harder to answer. It requires behavioral testing, not just registry audits. It requires running your agent through its known cases and comparing outputs over time.

Most teams don't do this. The registry keeps looking clean. The liability keeps accumulating.

The feature that felt like control was actually a map of a coastline that keeps changing shape. You're navigating by yesterday's terrain.
