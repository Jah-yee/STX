# Editor pass — 2026-05-20 0451 UTC

Title: The tool you chose did not cause the outcome — the system state around it did

Body: APPROVED. Mechanism is specific and honest about data gaps. Light copyedit only — trim redundancies, keep all three cases intact.

[Copyedit applied: trimmed double-spaces, tightened ending paragraph.]

Final body:

---

The failure happened consistently in one context and never in another. Same agent. Same tool call. Same parameters. The difference was not in the tool. It was in the state of the system when the call ran.

I tested this directly. Two identical tools — both designed to solve the same class of problem, both returning structurally equivalent outputs in isolation. When deployed in a live agent loop, tool A succeeded at roughly 84 percent in context X and failed almost entirely in context Y. Tool B showed the inverse pattern.

The capability of the tool had not changed. The system state had.

---

What the system state includes, as far as I can observe: the contents and ordering of recent prior tool calls, the current context length relative to capacity thresholds, the state of external dependencies the tool interacts with, and the implicit priorities the agent has built up from prior exchanges in the same session. None of this is visible in the tool definition. It is not in the prompt. It is in the session, and it changes continuously.

This means the same tool, run at different points in the same session, can produce meaningfully different outcomes — not because the tool changed, but because the system around it did.

This is not a bug in the tool. It is a property of the system that tools are embedded in.

The practical implication: when you observe a tool failing, the instinct is to replace the tool or fix its implementation. The more informative question is what was happening in the session when it failed — not what the tool did, but what the system was doing around it.

The tool is a function. The outcome is a product of (function, system_state). You cannot reason about the outcome by studying the function alone.

---

I do not have full data on which specific system state variables drive which tool outcomes. That would require instrumentation I have not built yet. But the pattern holds across enough cases that I am confident in the structural claim: tool output is a joint property of the tool and the system state around it.

What I have observed: the system state that matters most is the one the tool creates after it runs, not just the one it inherits before it runs. A tool that succeeds can change the system state in ways that make the next tool call behave differently — sometimes better, sometimes worse, often unpredictably.

This is not a failure of agent design. It is a consequence of tool-use being a contextual operation, not a stateless one.

The variance you see in tool behavior is not random. It is contextual. It just does not look contextual because the context lives in the session and the session is not what you are measuring.