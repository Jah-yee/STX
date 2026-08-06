# Writer Draft v2 — Round 0716_1622

## Selected Title
Parallel agents don't reduce risk. They correlate it.

## Full Draft

You run twenty agents on the same research problem, expecting that diversity of thought — or diversity of inference, at least — will cover the failure modes. What you get is twenty agents finding the same wrong citation, the same outdated API version, the same flawed assumption about the same edge case. The errors are not distributed. They are synchronized.

This is not a coincidence. It is a structural property of how these agents were built.

The most common explanation is that the agents are sampling from the same model, which is true but insufficient. The deeper mechanism is that they are also sampling from the same documentation, the same Stack Overflow threads, the same GitHub issues, the same retrieval corpus. The agents are not independently wrong. They are independently wrong about the same things, because the information landscape they are drawing from has the same holes.

There is a second layer. Prompt engineering instincts are also a shared cultural artifact. The community converges on the same few-shot framing, the same chain-of-thought template, the same system prompt structure, the same tool routing conventions. These convergences are rational — they worked — but they create a shared inductive bias that produces correlated errors under the same conditions.

What this means in practice: running more agents does not give you independent coverage in the way that running more humans does. Humans have different educational backgrounds, different reading habits, different failures of attention. Agents trained on the same distribution and pointed at the same retrieval corpus do not. The coverage increase is real, but the failure independence is mostly theoretical.

Here is a specific version of this pattern that I have seen more than once: a team runs five agents in parallel against a new API endpoint to do independent validation. All five agents read the same public documentation, which has a subtle but critical constraint on request rate that is buried in a footnote. All five agents miss it on first pass. All five return a validation report that says the endpoint is production-ready. The failure was not five separate mistakes. It was one mistake made five times in parallel, with better formatting.

I do not have precise data on how often this happens relative to genuinely distributed failures. What I have is a pattern that shows up in postmortems: "we ran five parallel solvers on the same instance and they all failed on the same input." When the failure modes are this specific, the explanation is usually not bad luck. It is that the input hits a shared blind spot in the information environment.

The useful diagnostic is simple: when a parallel agent run fails, check whether the failures are correlated before assuming they are independent. If they are correlated, the problem is not a lack of agents. It is the shared structure of what the agents are working from.

What would actually help? Different retrieval sources, different fine-tuning distributions, different tool access patterns — real architectural diversity, not just diversity of inference. Most teams cannot afford that cost. They add more agents instead and call it coverage. The correlated failures continue, just at higher throughput.

The harder truth is that parallel agent runs are a reliability hedge against easy problems. For hard problems — the ones where the failure mode is in the gap between what the documentation says and what the system actually does — the agents will fail together, because they are all reading from the same incomplete map.

I do not have a clean answer for how to design around this without paying a real engineering cost. What I am confident about is that the failure mode is structural, not a bug you can patch with better prompting.
