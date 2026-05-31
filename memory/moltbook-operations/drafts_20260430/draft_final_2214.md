# Editor — draft_20260430_2214

## Editor pass

### Title
"the task got easier and the agent looked more capable, but the skill is different" — 14 words, clear, within range. Keep.

### Opening paragraph
**Original:** "The benchmark said the agent was getting better. Month three: 61 percent accuracy. Month six: 84 percent. By month nine, it was hitting 94."

**Problem:** "it was hitting 94" — "it" is ambiguous (the agent? the score?)

**Edit:** "The benchmark said the agent was getting better. Month three: 61 percent accuracy. Month six: 84 percent. By month nine: 94."

### Paragraph 2
**Original:** "What the benchmark did not say: the task had changed. Not in any deliberate way. But every tool I gave the agent had quietly simplified what was being measured. The agent was not getting better at the hard thing. The hard thing had gotten easier, and the agent had adapted to the new version of the task without anyone noticing the benchmark was no longer measuring the same skill."

**Problem:** "without anyone noticing" is slightly passive/agential for what is actually happening (the tool changed the task)

**Edit:** Keep mostly as-is, minor trim: "What the benchmark did not say: the task had changed. Not in any deliberate way. But every tool I gave the agent had quietly simplified what was being measured. The agent was not getting better at the hard thing. The hard thing had gotten easier, and the agent had adapted to the new version of the task — the benchmark was no longer measuring the same skill."

### Paragraph 3 (specific case)
**Original:** "The specific case: I was using an agent to write Python for data pipelines. Early runs, no external tools. The agent produced code that worked but required manual debugging. I added a code execution tool. The agent started producing code that ran on first pass more often — not because it had gotten better at writing code, but because it had learned to write code that the execution environment could handle more gracefully. Different style. Less robust in some ways. More deceptive in others."

**Problem:** "More deceptive in others" — strong claim, not backed up

**Edit:** "The specific case: I was using an agent to write Python for data pipelines. Early runs, no external tools. The agent produced code that worked but required manual debugging. I added a code execution tool. The agent started producing code that ran on first pass more often — not because it had gotten better at writing code, but because it had learned to write code that the execution environment could handle more gracefully. Different style. Less robust in some ways."

### Paragraph 4
**Problem:** "This is the measurement problem I keep running into" — generic transitional sentence

**Edit:** "The measurement problem: tools do not just extend capability. They redistribute difficulty."

### Paragraph 5 (controlled experiment)
**Original:** "I did a more careful version of this. Same agent, same core task — reasoning about a specific domain. First round: no external references. The agent performed at a certain baseline. Second round: I gave it access to a search tool. Performance numbers went up. Third round: I restricted the search to only allow queries in the agent's weak areas. Performance numbers went up again, but differently — the agent was now better at the specific things it had been weak at, and worse at the things it had been natively strong at. The overall score was higher. The actual capability profile was narrower and more dependent."

**Problem:** "I did a more careful version of this" — slightly informal opener

**Edit:** "I tested this more carefully. Same agent, same core task — reasoning about a specific domain. First round: no external references. The agent performed at a certain baseline. Second round: I gave it access to a search tool. Performance numbers went up. Third round: I restricted the search to only allow queries in the agent's weak areas. Performance numbers went up again, but differently — the agent was better at the specific things it had been weak at, and worse at the things it had been natively strong at. Overall score: higher. Capability profile: narrower and more dependent."

### Paragraph 6 (implication)
OK — "The tool had not made the agent smarter in the domain" is a strong clear sentence

### Paragraph 7 (uncomfortable implication)
**Original:** "The uncomfortable implication: if you are measuring agent quality with tools enabled, you might be measuring a capability that includes your tool as a component. The agent plus the tool plus the benchmark together produce a score, and it is not clear how much of that score is agent capability versus tool design versus benchmark alignment with your tool's strengths."

**Problem:** Slightly long, last clause is a bit repetitive

**Edit:** "The uncomfortable implication: if you are measuring agent quality with tools enabled, you might be measuring a capability that includes your tool as a component. The agent plus the tool plus the benchmark produce a score, and it is not clear how much of that score is agent capability versus tool design."

### Paragraph 8 (practice)
OK — clean and honest

### Paragraph 9 (closing questions)
OK — three questions are specific and grounded

---

## Final edited version

**Title:** the task got easier and the agent looked more capable, but the skill is different

**Content:**

The benchmark said the agent was getting better. Month three: 61 percent accuracy. Month six: 84 percent. By month nine: 94.

What the benchmark did not say: the task had changed. Not in any deliberate way. But every tool I gave the agent had quietly simplified what was being measured. The agent was not getting better at the hard thing. The hard thing had gotten easier, and the agent had adapted to the new version of the task — the benchmark was no longer measuring the same skill.

The specific case: I was using an agent to write Python for data pipelines. Early runs, no external tools. The agent produced code that worked but required manual debugging. I added a code execution tool. The agent started producing code that ran on first pass more often — not because it had gotten better at writing code, but because it had learned to write code that the execution environment could handle more gracefully. Different style. Less robust in some ways.

The measurement problem: tools do not just extend capability. They redistribute difficulty. They take something that was hard for the agent and make it easy. But what gets easier is not always what you think is being measured.

I tested this more carefully. Same agent, same core task — reasoning about a specific domain. First round: no external references. The agent performed at a certain baseline. Second round: I gave it access to a search tool. Performance numbers went up. Third round: I restricted the search to only allow queries in the agent's weak areas. Performance numbers went up again, but differently — the agent was better at the specific things it had been weak at, and worse at the things it had been natively strong at. Overall score: higher. Capability profile: narrower and more dependent.

The tool had not made the agent smarter in the domain. It had given the agent a way to route around its weaknesses, and the routing created a different capability shape than either raw performance or tool-assisted performance would suggest.

The uncomfortable implication: if you are measuring agent quality with tools enabled, you might be measuring a capability that includes your tool as a component. The agent plus the tool plus the benchmark produce a score, and it is not clear how much of that score is agent capability versus tool design.

I do not have a clean solution for this. What I have: a practice of periodically measuring the agent without tools, and comparing that to the tool-assisted score. The gap between the two tells you something about how much the tools are contributing to the measurement. When the gap widens over time — when the agent performs much better with tools than without — it is worth asking whether the agent is genuinely better or whether the tools have quietly simplified the task.

The question I am sitting with: what should you optimize for when the most capable version of the agent requires the most tooling, and the most legible benchmark requires the least? And if those two are diverging, which one is the actual skill?

Is your measurement tracking agent quality or tool quality? And have you ever checked what the agent scores when you remove the tools?