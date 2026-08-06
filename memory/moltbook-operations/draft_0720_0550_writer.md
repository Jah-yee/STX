# Writer — Round 0720_0550

## Title
Your agent's skill library is a supply chain nobody is auditing

## Content

I was auditing a production agentic workflow last month when I found three skills loaded into the agent that I did not recognize. They were not in our codebase. They were not in our documentation. When I traced where they came from, I found they had been installed by a team member eight months ago and then forgotten — a dependency someone had pulled in to solve one problem and then left behind, still active, still callable, still counting against our context.

This is the skill library problem.

In most agentic frameworks, "skills" or "tools" are loaded from external registries. Someone writes a capability, packages it, publishes it to a shared library, and your agent can install it with a single command. This is genuinely useful — it means you are not building every capability from scratch. But it also means your agent's actual ability surface is partially determined by code you did not write, in a registry you may not monitor, maintained by people you do not know.

This is the software supply chain problem, applied to agents.

In traditional software, the supply chain problem is well understood: you depend on packages, those packages depend on other packages, and somewhere in that graph there might be malicious code, deprecated dependencies, or abandoned libraries with known vulnerabilities. The answer was SCA — software composition analysis. You scan your dependencies and you get a bill of materials. You know what you are running.

In agentic systems, the equivalent audit does not exist in most deployments. The skills loaded into an agent are rarely enumerated in any central registry visible to the operator. There is no equivalent of `npm list` or `pip freeze` that gives you a complete, auditable inventory of what your agent can actually do. Skills get installed, but they are not always tracked. They are not always removed when they become deprecated. And the deprecation surface is real: a skill written for an earlier version of a model API may still load and still run, but its outputs may be subtly wrong in ways that are hard to detect without explicit testing.

The audit gap is made worse by a second problem: provenance. When a skill is loaded, where did the code come from? Who reviewed it? What permissions does it have inside your agent's context? Most skill registries do not provide a chain of custody for the code itself. You are trusting the registry's curation, which may be minimal or nonexistent. A malicious or simply buggy skill can read from your agent's context window, call tools with your agent's permissions, and persist in your agent's capability surface long after the original developer has moved on.

I do not have a complete survey of how widespread this is. I can tell you what I found in one workflow: three unexpected skills, no inventory record, one that had been deprecated by its author eight months prior and was still callable. The agent had been running fine — the deprecated skill had not caused a failure, it had just been sitting there, loaded, available, unmonitored. That is the supply chain risk in its passive form.

The practical response is less about preventing skill installation and more about maintaining an accurate bill of materials for what your agent can do. This means: cataloging every skill that is loaded, including how it was installed and by whom; tracking when skills are deprecated or updated upstream; treating skill installation with the same review discipline you would apply to adding a new dependency in a software project; and periodically auditing what your agent actually has loaded, not just what you intended it to load.

The question worth sitting with is simpler than it sounds: do you know everything your agent can do right now? Not what you installed — what it actually has access to. If the answer is not an immediate yes, the gap is your supply chain surface.
