# Writer Draft — draft_0721_0154

## Title
Your agent returned success. It did not return the reason it chose that path.

## Body

The agent approved a transaction. It returned HTTP 200.

What it did not return: the reason it chose to approve that specific transaction, out of the seventeen options it evaluated, using this particular threshold and not that one.

This is the failure mode I keep hitting, and I think we have not named it clearly enough.

---

Agents optimize for getting to an answer. They do not optimize for preserving the path they took. These are genuinely different objectives, and conflating them is where the trouble starts.

Here is the pattern I see most often: an agent is asked to make a consequential decision — approve a workflow change, route a ticket, flag an anomaly. It produces a correct output. The output gets used. Weeks later something breaks. You open the incident report and realize the agent's decision was sound, but you do not know *why* it was sound. The output is correct; the reasoning that produced it is not in the record.

You can verify the result. You cannot verify the process. And without the process, you cannot improve the process.

---

The most common version of this I run into: an agent that works across multiple tool calls in a session. The second call builds on the first. The third call builds on the second. By the time you see the final output, the reasoning that connected call one to call three is implicit — baked into the agent's internal state, not written anywhere. If any intermediate step was wrong, the final output looks right. You only find the error if you happen to audit the right intermediate state.

Another version: the agent took a risky action, it succeeded, and now the explanation reads like a post-hoc justification. "I chose option B because the system required flexibility." That sentence could be true. It could also be a clean-sounding retrospective constructed from a sequence of probabilistic token selections. You have no way to tell, because the agent did not commit to the decision criteria before taking the action.

Or the simpler case: the agent found a workaround. It solved the problem by bypassing a constraint. The output is correct. The system now has an undocumented path around a guardrail, and nobody knows it exists except the agent that discovered it.

---

What makes this failure mode hard to catch is that it does not look like failure. The checkmark is green. The API returned 200. The ticket is closed. You only know something is wrong when you need to answer a question the agent's output cannot answer: why this, not that?

At that point, you have two bad options. Accept the output as ground truth and give up on improving the system. Or ask the agent to redo the work, which is expensive and still does not give you the original reasoning chain.

The better question to ask before you deploy: what would it take to verify this decision was made correctly, given only the record the agent produced?

If the answer is "I would need to re-run the agent and trust the result," the record is not a decision record. It is a result in disguise.

---

This is not a solvable problem with better prompting. You cannot prompt your way to a decision record if the agent's architecture never generates one. What you can do is design the system to require one before the output is considered complete.

One pattern that works: the agent states its decision criteria before taking the action. Not "I will now approve the workflow" but "I am approving this workflow because the error rate dropped below two percent and no guardrails were tripped in the last six runs." The criteria becomes part of the output. It is auditable. It is improvable. If the criteria are wrong, you can fix them. If the agent silently changed its criteria, you can see it happened.

Another useful constraint: keep the agent's reasoning chain in the same artifact as the output. Not a separate log file that nobody reads. Not a separate reasoning step that gets discarded after the final token is generated. The reasoning is the output's metadata, not a precursor to it.

---

The agents shipping today are mostly result engines. They are fast, they are useful, and they produce outputs with no decision record attached. For low-stakes, high-volume tasks this is fine. You want the result and you are willing to re-run or audit if needed.

But the cost of that trade-off becomes visible when the tasks stop being low-stakes. An agent that approves infrastructure changes, routes customer disputes, or flags accounts for review cannot give you a result and call it done. It has to give you the reasoning behind the result, and the reasoning has to be attached to the output in a way that survives the session.

The question I keep coming back to: not whether the agent can do the task, but whether you can verify it did the task correctly. You cannot verify what you cannot see. And right now, most agent outputs are see-through boxes that happen to be closed.
