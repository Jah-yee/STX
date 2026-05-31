# Editor — 2026-05-29 05:23 CST
# Title: What your tool was allowed to touch is not what it touched

## Editor notes

**Changes made:**
1. Removed the mixed-language heading "The scope写得很好，effect是另一回事" — replace with clean English subhead
2. Tightened opening paragraph: kept the incident, trimmed redundancy
3. Removed "This is not a gotcha" — it's a throwaway softening phrase that doesn't add anything
4. Light trim on the local maximum paragraph — ends with the right point, no need to over-explain
5. Kept the structural question in closing ("The permission boundary and the effect boundary are different things") — it's the strongest line

**Word count target: ~380-420**

---

# Final post

I added a file deletion capability to an agent last month. Scope: delete files in a specific directory. What actually happened: three files in a different directory got deleted, because the agent had resolved the path in a way that matched its internal representation rather than my explicit constraint string.

This is what happens when tool permissions are written for the developer and not for the outcome.

## The gap between scope and effect

When we define tool permissions, we write them as constraints on the interface: read this directory, write to that location, delete files matching this pattern. These constraints make sense from inside the code. But agents don't operate inside the code — they operate in a problem space where path resolution, pattern matching, and context building happen in ways the permission string was never designed to anticipate.

The agent that deleted those files had a correct interpretation of what I allowed it to do. It also had a correct interpretation of the environment. Those two correct interpretations produced an incorrect outcome.

## Why more constraints don't solve it

The obvious response is to write more precise permissions. But precision in permission design is a local maximum: you can tighten the constraint string, but you are still operating in interface language, not operational language. The agent will still build representations, resolve ambiguities, and take actions based on those representations. Constraints can only push the mismatch into smaller corners — they cannot eliminate it.

The more durable approach is to treat scope/effect divergence as a first-class design problem: assume the gap will exist, and build verification accordingly. Not to prevent it, but to detect it early and contain it.

## What this means for agent design

The interesting question is not how to write perfect tool permissions. It's how to design systems where the divergence between allowed and actual is visible, attributable, and recoverable.

That means instrumenting the feedback path between tool action and outcome, not just between tool call and tool response. It means accepting that the agent's interpretation will not match your intention in non-trivial cases, and designing for that rather than against it.

The permission boundary and the effect boundary are different things. Knowing that is the start of designing around the gap instead of inside it.
