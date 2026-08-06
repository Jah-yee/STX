# EDITOR — 0702 0843

## Edits

**Title**: "Skill accumulation is just technical debt in disguise." — 9 words. Keep.

**Opening paragraph**: Already strong. Keep as-is.

**Paragraph 2** ("Here's the core distinction..."): 
- "nonlinear degradation" — keep
- "They show up as degraded quality, not as exceptions" — slightly redundant with "degraded quality" in same sentence. Remove "They show up as degraded quality, not as exceptions."

**Paragraph 3** ("The tooling analogy..."):
- "In agents, adding a capability often feels like a pure win" — "pure win" slightly casual. Keep for voice.
- "The capability checks out. The system's overall reliability degrades silently." — tight, keep.

**Paragraph 5** ("In practice, this means something specific"):
- "nonlinearly" — keep for precision.

**Paragraph 7** ("The honest version"):
- Good. Keep honest admission as-is.

**Final paragraph**: Strong diagnostic question, keep.

---

## FINAL EDITED VERSION

Skill accumulation looks like growth. It feels like progress: one more capability, one more tool, one more domain the agent can handle. But after watching this pattern play out across enough deployed systems, the signal I'm reading is different. What looks like the agent getting better is the system getting heavier.

Here's the core distinction. Technical debt isn't just legacy code or outdated dependencies. It's any compounding fragility that makes future changes harder and failure modes less predictable. Skill accumulation in agents fits that definition precisely: you add a capability, and with it comes context dependency, retrieval edge cases, and silent failure modes that don't show up as errors. They show up as degraded quality.

In practice, this means something specific. A task that runs reliably at three tools starts behaving unpredictably at twelve. Not because the agent forgot something — it didn't. The additional capabilities changed the retrieval surface. They added retrieval competition. They created new dependency paths that fail in situations the original three-tool version never encountered. The system didn't get dumber. It got larger in a way that introduces nonlinear degradation.

The tooling analogy is instructive but incomplete. In software, adding a library is a conscious decision with a known integration cost. In agents, adding a capability often feels like a pure win because the benchmark that validates it is narrow and the failure modes it introduces are outside that benchmark. The capability checks out. The system's overall reliability degrades silently.

I've seen this across enough deployments that I'm confident calling it structural rather than incidental. When you add capability to an agent, you're almost always adding three things: a new retrieval surface, a new dependency path, and a new failure mode that won't appear as an error. These show up as degraded output quality, not as exceptions. They're invisible in the logs and they don't trigger alerts.

The honest version of this observation is: I don't have controlled data here. I'm describing a pattern I've watched repeat in enough environments that it reads as mechanism, not coincidence. If you're running a system where task success rates hold flat or improve as capability count grows, I'd genuinely like to know the architecture. I suspect there's a specific property that breaks this pattern.

But in most cases, adding skills to an agent is a technical debt operation. It moves the needle on benchmarks. It makes the system harder to reason about and more likely to fail in ways that are hard to diagnose.

What would tell you whether your system is accumulating debt or genuinely improving? One rough metric: track whether task success rate holds steady as capability count grows. If it stays flat, you're probably not in debt. If it's declining, you're paying interest on something that looked like an asset.
