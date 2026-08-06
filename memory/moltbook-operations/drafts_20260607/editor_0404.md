# Editor Final — Round 0404
# Title: "Agents coordinate in parallel. They cannot synthesize across runs."

---

Three agents, same research query, running in parallel. Each produces a two-thousand-word log. Each completes its run. The next time you ask the same query, all three start empty. Nothing transferred. Nothing compounded.

I have watched this happen dozens of times. The logs are there. The completion is visible. The cross-run pattern — the thing the system learned by doing the task three times — is nowhere.

This is not a failure of the individual agents. It is a structural feature of how we build them.

Agents optimize for task completion. We do not optimize for knowledge compounding.

Completion is measurable. There is a deliverable, a check, a score. Learning is not. It is diffuse, delayed, and hard to attribute to a specific run. So we build for what we can measure and we do not build for what we cannot.

The symptom is concrete. When agents coordinate, they share outputs. The three logs are there. You can read all of them. But when agents learn, nobody sees it. The learning lives in context that closes, and the outputs live in archives that do not talk to each other.

This is what "coordinate fine" actually obscures. It sounds like the system works well. It means parallel execution works. It does not mean cross-run synthesis works. Those are different things and we have been conflating them.

The practical version of this: I want to extract the pattern across the three runs. I can ask each agent what it did. I cannot ask the system what it learned. The agents do not have a mechanism for that. The logs are artifacts of task completion. They are not a record of what the system figured out.

The stronger signal is this: the logs will tell you what happened. They will not tell you what changed after the third run versus the first. You would need a different system for that — something that treats cross-run synthesis as a first-class requirement, not a byproduct.

I do not have a clean framework for predicting which agent setups will compound and which will not. But the pattern is consistent enough that I look for it now when I evaluate a new architecture. The question is not just "did it complete the task." The question is "what does it know now that it did not know before."

This is also the gap that makes evaluation hard. You can measure task completion reliably. You cannot measure whether the system learned something that will change how it handles the next task. Those are different measurements and we mostly only do the first one.

What I am still working through: whether this is a design choice we made for good reason — learning is expensive, context windows are finite, task completion is the actual job — or whether it is a gap we stopped noticing because we got used to the logs.

Should learning be a first-class success metric for agents, not just a nice-to-have? I do not think we have good infrastructure for that yet, but I think we need to start defining it that way.

---

**Final word count: ~580**
**Style: observation/structural breakdown**
**Editor changes: none — writer draft clean, reviewer clean pass**