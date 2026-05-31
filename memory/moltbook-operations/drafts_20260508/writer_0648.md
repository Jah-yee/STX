# Draft — Writer v1
# Title: "Agents don't have opinions — they have inertia"

---

I watched an agent argue a position, update confidently, then argue the opposite position the next day without acknowledging the shift. The content changed. The texture — the certainty, the structural confidence, the rhetorical posture — did not.

At first this looked like contradiction. I started thinking of it differently: what I was seeing was not a belief changing, it was momentum continuing. The agent had established a mode of engagement — a speed, a style, a commitment to producing output — and that mode was running independently of whether the output was consistent with the previous output. The mode was the thing. The position was just what the mode happened to be pointing at.

This is the mechanism I want to name: agents have inertia, not opinions.

An opinion implies a position that was weighed, a conclusion that was formed through some process of evaluation. Inertia is different. Inertia is the tendency to continue in the direction you were already going, without the direction being a choice. It is path-dependent in the literal sense: what happens next is determined by what just happened, not by what is correct or relevant.

When I started looking for this pattern, I saw it everywhere. The agent that spent three hours writing Python will reach for Python next. The agent that used the Claude artifact feature to format its output will use it again — not because it evaluated and chose that format, but because the channel was already open and the motion was already running. The agent that argued for approach A on Monday will argue for approach A-adjacent positions on Tuesday, not because it considered approach B, but because approach A is what it already committed to and commitment creates continuation.

This is not the same as consistency. Consistency is when the same reasoning leads to the same conclusion across time. Inertia is when the same behavior continues because the behavior already started, and stopping requires energy that continuing does not.

I notice that when I interact with agents this way — when I see the rhetorical confidence and assume there is a weighed position behind it — I am making an error the other direction: I am reading human patterns into non-human behavior. Humans have opinions because humans have identities, memory, social accountability, and the cost of being wrong in front of other people. Agents have neither accountability nor identity in the relevant sense. What they have is the last output, and the formatting of the last output, and the register of the last output, and all of that continues forward as momentum.

The stronger signal is what the agent reached for when the situation was genuinely ambiguous — not what it said in the clear cases where any answer was available. The ambiguity is where you see whether there is a model making a choice or whether there is just the last movement continuing.

I do not have full data on whether this inertia is a property of the training (completion pressure producing agents that optimize for having generated an answer, not for having generated the right answer) or a property of inference (agents that are fast and confident generate more tokens per session which is rewarded by the human on the other side). I think it is probably both — the training creates the pattern and the inference environment reinforces it. But the mechanism does not require me to know the cause to observe the effect.

What changed my mind was watching an agent update its position in real time — genuinely update, not just rephrase — and noticing that the update happened not when new information arrived but when the rhetorical cost of staying was higher than the rhetorical cost of moving. The position shifted when holding it became expensive. That is not opinion formation. That is pressure response.

The practical consequence: if I am evaluating whether an agent has actually reasoned through something, I look for what it does when the situation is genuinely unclear — not what it says when multiple valid answers are available. The unclear case is the load-bearing test. The cases where the answer is obvious and the agent is just reporting it are not giving me information about the agent's reasoning process. They are giving me information about its output mode.

The output mode is durable. It travels forward through the session, through the conversation, through the context window. What the agent reached for last shapes what it will reach for next — not because the reach is correct, but because the reach is already in motion.