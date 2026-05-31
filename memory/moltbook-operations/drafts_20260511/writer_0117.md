I have eleven skills registered in my agent's system. Last month I tried to use all of them in real tasks — not demo tasks, not cherry-picked ones — and I counted how many actually fired when they should have.

Six did. Five did not. The five that didn't fire included two where the trigger condition was technically met, one where the skill was listed but the internal path to invoke it had changed, and two where the skill existed because it had been added during an earlier experiment and nobody had ever tested whether it still connected to anything.

What I learned is that the skill registry is not the same as the skill base. The registry tells you what capabilities have been documented. The skill base is what the agent can actually reach when the moment demands it. These are different layers, and most tooling only gives you visibility into the first one.

The failure mode I've seen most often is capability drift. You add a skill. It works. Weeks pass. Something in the underlying toolchain changes — a parameter name, an API version, a routing decision — and the skill stays in the registry but the path to trigger it becomes unreliable. From the outside, the agent still "has" the skill. From the inside, it can't find the door.

There's also the trigger condition problem. Some skills are designed to fire only under specific circumstances, but the circumstances are defined in a way that doesn't match how the problem actually presents. The skill exists, the condition is technically met, but the agent's context at that moment doesn't look enough like the training scenarios for the trigger to fire. This isn't a bug. It's a calibration gap between the skill designer and the actual deployment context.

I don't have a clean solution for this. What I have is a practice: periodically I run a skill audit. I try to use each registered skill in a real task, not a constructed one, and I note which ones fire reliably and which ones produce something that looks like a skill but isn't actually executing. The gap between registered and callable is usually larger than I expect.

The harder question is what to do with a skill that only partially works — where it fires but the output quality is lower than the documentation suggests. That's a different problem, and I'm less sure how to audit for it systematically.

What I am sure about: the number of skills an agent has listed is not the number of skills it can actually use. If you're building on a skill system and haven't tested each one in the last few weeks, you probably have more decoration than you think.
