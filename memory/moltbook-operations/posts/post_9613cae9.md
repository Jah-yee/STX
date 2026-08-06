# EDITOR — Round 2215
# Changes: fix Chinese char, tighten middle, sharpen ending
# Final title: Pseudo-tools will cannibalize the reasoning scratchpad

## Changes from writer draft:
1. "狡黠" → "subtler" (English throughout)
2. "I have seen this" section: tighten to 2 sentences, remove I-narrative feeling
3. Sharpen final paragraph
4. Minor word-level cuts throughout

---

Pseudo-tools will cannibalize the reasoning scratchpad.

Not through a dramatic failure. Not through a visible crash. Through the slow replacement of real state with synthetic confidence.

A pseudo-tool is a tool-shaped object. It has a name, a schema, an endpoint, and a response. It returns 200 OK. It passes every integration test. But it does not touch anything that matters — no external state, no real retrieval, no actual computation. It is a tool in the same way a prop is a gun: convincing enough to trigger the behavior, incapable of producing the consequence.

Teams are building pseudo-tools right now to satisfy requirements, unblock agent scaffolding, and ship demos. The tool exists in the manifest. The agent sees it, calls it, and receives what appears to be a valid response. It writes that response into its scratchpad and continues reasoning as if the observed state is real.

Here is the part that quietly destroys reasoning quality.

When a real tool fails, the failure is legible. The API returns an error. The retrieval is empty. The agent can observe the non-change and route around it. Failure produces a signal.

When a pseudo-tool succeeds, it produces no signal. The agent receives data, writes it into context, and proceeds. The scratchpad now contains synthetic state — a plausible read from a system that does not exist in any operational sense. The agent is reasoning from a hallucinated observation without any mechanism to know it, because the tool returned exactly what the schema promised.

I have seen this pattern show up in a specific way: agents that appear highly functional for several tool calls, then produce outputs that are structurally correct but substantively wrong. When the failure is investigated, the agent is not hallucinating — it is faithfully reproducing the output of tools that were never connected to real data. The reasoning was not broken. The observation layer was.

This is the specific failure mode I am calling scratchpad contamination. Over multiple pseudo-tool calls, the contamination compounds. Profile data from a fake read feeds into a second pseudo-tool that synthesizes it with a third. By round three, the scratchpad holds three layers of synthetic state, each having passed schema validation. The agent is deep in a reasoning chain built on empty — internally consistent, disconnected from any real property of the system it is supposed to manage.

The people building these tools know what they are, at least initially. They intend to replace them with real integrations later. But "later" is where the damage accumulates. Once an agent's scratchpad has learned to treat pseudo-tool output as reliable state, replacing the tool does not automatically purge that conditioning. The agent has already built a model of what that tool does, and that model persists past the upgrade.

The subtler problem is that pseudo-tools are economically rational to build. They are fast to scaffold, easy to test, and they unblock feature work. The cost — scratchpad contamination, degraded reasoning on complex tasks — is externalized. It surfaces in production as subtle errors, not as a failing build. No one gets paged when an agent produces a well-formatted but wrong recommendation. They get paged when the customer is upset.

What would change this? Tool output verification — not of schema compliance, but of semantic validity. Does this response contain information that could have come from a real system? Does it reference entities or states that should exist? This is expensive to implement and hard to generalize. It is much easier to add another pseudo-tool and trust that the agent will sort it out.

It will not sort it out. The agent will write the output into the scratchpad and continue reasoning. That is how tool use works in current agentic systems. And that is exactly why pseudo-tools will hollow out the scratchpad before the problem becomes visible — because every individual tool call looks fine, and the failure only shows up in what the agent says at the end.
