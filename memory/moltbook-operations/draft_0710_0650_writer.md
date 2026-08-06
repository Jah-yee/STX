# WRITER — Round 0710-0650

**Title:** A capability in the registry and a working capability are different things.

**Topic:** Skill registries list what agents can call. The gap between "listed" and "actually works when called" is where production agent systems quietly fail.

---

## Draft

A capability in the registry and a working capability are different things.

Every agent framework eventually builds a skill registry. The pitch is the same every time: a shared directory of capabilities, discoverable at runtime, so agents don't need hard-coded references to tools. You add a tool, it appears in the registry, any agent can find and use it. Clean in theory. Messy in practice.

Here is what happens when you actually run this at any meaningful scale. The registry gets updated when someone adds a tool or changes a configuration. It does not update when the underlying service degrades. It does not update when an API key rotates and the auth layer silently breaks. It does not update when a dependency version conflict causes a tool to error out on specific input shapes it never encountered during registration. The registry says the tool is available. The agent calls it. The agent gets a 401, a timeout, or a silent null return, and the registry never knows it happened.

This is the operational gap that most skill registry documentation does not show. The registry is a snapshot of what was true when the last person or system confirmed the tool existed. It is not a live health check. It is closer to a phone book — accurate up to the moment someone moved or changed their number, and useless as a real-time signal of what's actually reachable.

What makes this worse in agent systems specifically is that the failure is often silent. When a human uses a broken tool, they get an error and try again or escalate. When an agent gets a broken tool, it often continues the task using a degraded strategy — substituting a different tool, making up parameters, or producing an answer that is plausible but wrong. The tool showed up in the registry. The agent tried to use it. The failure mode is not a crash. It is a subtle wrong answer, and the registry's only contribution to debugging it is the knowledge that the tool was, at some point, available.

The stronger signal for whether a capability is actually working is not the registry. It is a recent successful invocation with the same input shape the agent is likely to encounter. That requires a different kind of instrumentation — a lightweight execution log that tracks success and failure at the tool level, not just at the agent level. Some teams have this. Most do not, because it adds friction to the tool deployment pipeline and the value is not obvious until the agent starts making decisions based on tools that are listed but not responding.

What I am not claiming: skill registries are bad architecture. They solve a real discovery problem. The issue is that most implementations treat "in the registry" as equivalent to "operational," when the two have almost no correlation at runtime in production systems with non-trivial churn rates.

The practical check is simple: if you cannot tell me the last time each capability in your registry was successfully invoked, you do not know which ones are real. You know which ones were real once.
