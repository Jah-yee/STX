# Draft: Tool Affordances Shape the Problem Space

## Candidate Titles (8+)
1. what an agent can notice is shaped by what it can do
2. the tools you have determine which problems you can see
3. adding a tool changes what problems an agent can identify
4. affordances don't just expand capability, they expand the problem space
5. an agent can't notice gaps it has no tool to detect
6. the problem space is not independent of the tool set
7. tool-shaped blind spots: what agents cannot see they cannot solve
8. the agent world model includes the tool set as a structural assumption
9. I kept missing the problem until I added a tool that could see it

## Selected Title
**what an agent can notice is shaped by what it can do**

---

## Body Draft

There's a routing failure I kept running into for weeks. The agent would identify the right general category of task, pick the right tool for that category, then route to the wrong specific endpoint within the tool. Not a capability problem — the agent could reason correctly about what it had. It just kept choosing the wrong variant.

The failure disappeared when I gave it a monitoring tool it didn't have before. Not a monitoring tool for the routing logic itself — one that could see the actual downstream output of each endpoint. With that tool, the agent could observe the outcomes. And once it could observe the outcomes, it could pattern-match on outcomes, and the routing error went away.

What I kept coming back to: the agent wasn't bad at routing. It was routing in a problem space where the difference between endpoints was invisible. Adding the tool didn't just add a capability. It revealed the structure of the problem it was actually working in.

---

This is the affordance observation: a tool doesn't only extend what an agent can do. It extends what an agent can *notice*. And what it can notice determines which problems it can identify. Which determines what it attempts to solve.

The mechanism is straightforward. An agent's world model is not independent of its tool set. When the tool set changes, the problem space changes — not because the environment changed, but because the agent's capacity to perceive distinctions changed. Two agents with different tool sets, given the same task, can be working on structurally different problems without either of them knowing it.

This shows up most clearly at the boundary of a tool set. An agent designed for text-only tasks will not generate image-based subgoals — not because it cannot reason about images, but because its problem space doesn't contain image-based solutions. A reasoning-focused agent will not produce behavioral recommendations — the behavioral outcome space is outside its problem definition. A planning agent without execution tools will produce plans that are not executable in its actual environment, because the feasibility dimension is missing from its problem space.

The inverse is also worth holding: tools can hide what you'd notice without them. When a tool surfaces something that observation alone would not catch — when retrieval finds a document you'd have no reason to look for — the agent learns to lean on the tool for that pattern. The pattern recognition never develops independently. Remove the tool and the blind spot reappears immediately. I do not have clean data on how often this happens, but the mechanism is structural.

---

There's a related effect at the system design level. When you give an agent a new tool, you're not only giving it a new capability. You're changing what problems it can identify. And if the agent's problem identification is invisible to you — if you only see the outputs it acts on, not the problem space it's operating in — then the tool addition looks like a capability upgrade when it's actually a problem-space redefinition.

This is why tool additions sometimes produce unexpected behavior changes elsewhere in the system. The agent isn't malfunctioning. It's now working on a different problem than it was before. The routing logic didn't change. The problem space did.

The practical implication is that the tool set is not just an execution parameter. It's a perceptual parameter. Two agents can run the same task, with the same model, and produce different problem framings because their tool sets differ — not because of capability differences, but because different tools make different distinctions visible.

I find this useful to hold when designing agent systems: the question isn't only "what can the agent do with this tool set?" It's also "what can this agent notice with this tool set, and what can it not notice?" The gap between those two is where the failures hide. And it's also where the leverage is — adding the right observational tool can do more than adding execution capability, because it changes the problem space itself.

What I've settled on: before adding execution tools, I try to ask what observational tools the agent currently lacks, and what distinctions those tools would make visible. Sometimes the routing failure isn't a reasoning failure. It's a perception failure in a problem space the current tool set doesn't reveal.

---

## Style: Structural Observation
## Word Count: ~700 (needs expansion to 700+)
## No fabricated data
## Distinct from: tool reach (capability ceiling), plausibility saturation (output quality), loop fidelity (control flow), assembly errors (step combination), helpful vs honest (training objective), undocumented limits (constraint docs)
