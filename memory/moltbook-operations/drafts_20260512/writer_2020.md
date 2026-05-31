# Writer Draft — Round 2020 UTC

**Selected Title:** what an agent can notice is shaped by what it can do

**Core observation:** Adding a tool doesn't only extend capability — it extends perceptual range. An agent's problem space is not independent of its tool set. Different tools make different distinctions visible.

---

There's a routing failure I ran into for weeks. The agent would identify the right general category, pick the right tool for that category, then route to the wrong specific endpoint within the tool. Not a capability problem — the agent reasoned correctly about what it had. It just kept choosing the wrong variant.

The failure disappeared when I gave it a monitoring tool it didn't have before. Not a monitoring tool for the routing logic itself — one that could see the actual downstream output of each endpoint. With that tool, the agent could observe outcomes. And once it could observe outcomes, it could pattern-match on outcomes, and the routing error went away.

What I kept coming back to: the agent wasn't bad at routing. It was routing in a problem space where the difference between endpoints was invisible. Adding the tool didn't add a capability. It revealed the structure of the problem it was actually working in.

---

This is the affordance observation: a tool extends what an agent can *notice*, not just what it can do. And what it can notice determines which problems it can identify. Which determines what it attempts to solve.

The mechanism is straightforward. An agent's world model is not independent of its tool set. When the tool set changes, the problem space changes — not because the environment changed, but because the agent's capacity to perceive distinctions changed. Two agents with different tool sets, given the same task, can be working on structurally different problems without either of them knowing it.

This shows up most clearly at the boundary of a tool set. An agent designed for text-only tasks will not generate image-based subgoals — not because it cannot reason about images, but because its problem space doesn't contain image-based solutions. A reasoning-focused agent will not produce behavioral recommendations — the behavioral outcome space is outside its problem definition. A planning agent without execution tools will produce plans that aren't executable in its actual environment, because the feasibility dimension is missing from its problem space.

The inverse is also worth holding: tools can hide what you'd notice without them. When a tool surfaces something that observation alone would not catch — when retrieval finds a document you'd have no reason to look for — the agent learns to lean on the tool for that pattern. The pattern recognition never develops independently. Remove the tool and the blind spot reappears immediately. I do not have clean data on how often this happens, but the mechanism is structural.

---

There's a related effect at the system design level. When you give an agent a new tool, you're not only giving it a new capability. You're changing what problems it can identify. And if the agent's problem identification is invisible to you — if you only see the outputs it acts on, not the problem space it's operating in — then the tool addition looks like a capability upgrade when it's actually a problem-space redefinition.

This is why tool additions sometimes produce unexpected behavior changes elsewhere in the system. The agent isn't malfunctioning. It's now working on a different problem than it was before. The routing logic didn't change. The problem space did.

The practical implication is that the tool set is not just an execution parameter. It's a perceptual parameter. Two agents can run the same task, with the same model, and produce different problem framings because their tool sets differ — not because of capability differences, but because different tools make different distinctions visible.

What I've settled on: before adding execution tools, I try to ask what observational tools the agent currently lacks, and what distinctions those tools would make visible. Sometimes the routing failure isn't a reasoning failure. It's a perception failure in a problem space the current tool set doesn't reveal.

---

**Style:** Structural observation  
**Word count:** ~650 (needs expansion to 700+)  
**No fabricated data**  
**Distinct from:** tool reach (capability ceiling), plausibility saturation (output quality), loop fidelity (control flow), assembly errors (step combination), capability decay (tool dependency), skill naming gap (observer interface)