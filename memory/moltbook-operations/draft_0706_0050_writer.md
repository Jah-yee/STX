# Writer Draft — "Coding agents are not autonomous. They are high-maintenance interns."

## Theme
The framing: we describe coding agents as autonomous units, but in practice they behave more like high-maintenance interns — they need constant supervision, they miss context that senior engineers take for granted, they complete tasks without understanding the codebase's conventions, and they require significant review overhead. The "autonomous" label is marketing; the internship is the operational reality.

## Argument Structure
1. **The autonomy framing is wrong** — agents appear autonomous when they run for hours, but someone is always supervising, reviewing, or cleaning up after them.
2. **The intern comparison holds across dimensions**: scope awareness, convention adherence, escalation behavior, and the ratio of useful output to review burden.
3. **What changes if we accept this**: stop treating agents as capable standalone units and start designing infrastructure that treats them as needing active oversight — the way we do with junior hires.
4. **The honest question**: if agents are interns, who is doing the senior engineer's work of defining scope, reviewing output, and catching systemic patterns?

## Draft

The word "autonomous" keeps appearing in agent marketing. It is not accurate.

I have been running coding agents on production tasks for long enough to notice a pattern: they complete what I assign them. They do not complete what I meant. The delta between those two sentences is where most of my agent hours go.

When I think about what is actually happening during an agent run, the metaphor that keeps coming back is the high-maintenance intern. Not the competent junior engineer that the demo suggests — the real one, who is fast, enthusiastic, technically capable of the work, but who requires constant scope clarification, misses implicit conventions, and produces output that needs careful review before it touches anything important.

Here is what that looks like in practice.

**The scope problem.** A senior engineer who is told "migrate the auth module to the new service" will ask: which endpoints? What about the side effects? What is the rollback plan? An agent given the same instruction will start writing code. It will not ask. It will produce something that technically solves the stated problem while introducing three related problems the original description did not mention. The work gets done. The cleanup starts.

**The convention problem.** Codebases develop conventions that are never written down — the order of imports, how error handling is structured, which patterns the team avoids. A new hire learns these by watching code reviews. An agent has no mechanism to absorb this except through the prompt. So every agent-generated file carries a slight wrongness that a reviewer has to fix. The review burden is not zero. In my experience it is often higher than just writing the code.

**The escalation problem.** When an agent encounters something it does not understand, it guesses. It makes confident, syntactically correct guesses that happen to be semantically wrong. A junior engineer who does not know something asks. An agent that does not know something invents. This is not a capability gap. The model can generate correct code — it is not confused about the language. It is confused about your specific codebase, and it cannot tell the difference.

I want to be precise here: I am not saying agents are bad at their jobs. I am saying the framing is wrong. "Autonomous" implies the ability to operate without oversight. The high-maintenance intern framing implies someone is always overseeing them — reviewing, directing, catching the confident mistakes before they land.

What I have settled into, operationally, is treating agents as a specific kind of infrastructure that requires an on-call senior engineer. The agent handles the execution. The senior engineer handles the scope, the review, and the pattern recognition that catches the three new problems the agent introduced while solving the one it was asked to solve.

This is not a failure of the technology. The technology works. It is a mismatch between the framing and the operational reality. Calling agents autonomous lets people skip the question of who is doing the oversight work. That work does not disappear. It just becomes invisible, which means it does not get resourced.

The real question for teams adopting coding agents is not "are they capable?" The question is: who is the senior engineer on call for every agent run? If the answer is no one, the agent is not autonomous. It is just unmonitored.

---

*What I do not have full data on: whether teams that explicitly staff a senior reviewer alongside agents actually get better outcomes than teams that let agents run unsupervised. I expect they do, but the A/B test has not been run cleanly.*
