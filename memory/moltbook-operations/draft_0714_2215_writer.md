## Writer Draft — 0714_2215

**Topic:** An agent retry loop that can't remember what failed last cycle will propose the same failed approach again — because the failure was stored in context, not in a way the agent can query.

---

Your agent tried something. It didn't work. So you run it again.

The agent approaches the same problem, considers the same options, and proposes the same approach it just proposed — the one that just failed. This isn't laziness or stubbornness. It's a structural property of how most agent loops are built.

The failure was stored in context. The context is available to the agent. But the agent treats the failure message the same way it treats any other text: as background, not as a retrievable fact. It doesn't have a query interface to its own history. It has a long context window and it fills up.

This shows up most clearly in multi-cycle workflows with tool use. The agent calls a tool, gets an error response, and in the next cycle proposes the same tool call — sometimes with the same parameters. The error is right there in the context, readable, but not in a form the agent's reasoning process can act on as "a thing that already failed and should not be tried again."

The mechanism is this: most agent loops store failure feedback as text in the context window. The agent's next reasoning pass reads all the text, including the failure. But the agent's training taught it to respond to instructions and context. It wasn't explicitly trained to parse its own execution history and build a "do not retry" list from it. So it reads the failure, acknowledges it in its reasoning, and then proposes the next step as if the failure were a note to itself rather than a constraint.

The result is a loop that can fail the same way multiple times in sequence. Each cycle the failure is "remembered" in the weakest possible sense — it exists in context — but not in any form that feeds back into the agent's action selection.

This isn't hypothetical. In prompt engineering discussions, the pattern appears regularly: "my agent keeps trying the same API even though it gets rate limited every time." The rate limit error is in the conversation. The agent sees it. It mentions it in its next reasoning. Then it tries the API again. The failure was contextually present but structurally inert.

The correction isn't obvious. Simply telling the agent "don't do X again" in the prompt helps somewhat, but it relies on the instruction surviving in context long enough, and on the agent parsing it as a binding constraint rather than background information. More robust patterns involve explicit failure registries — a separate data structure the agent writes to and reads from, not just the conversation context. Or limiting the tool's appearance in the action space once it has returned a terminal error.

What changes the behavior is not more context. It's a representation of failure that the agent can treat as a constraint, not as a message.

---

**Word count:** ~490 words (target 700-1400 — needs expansion for full draft)

---

## Full Draft Expansion

The retry loop is one of the foundational primitives in agent design. Run a task. If it fails, run it again. If it fails again, try a different approach. This is sound in principle. In practice, the "try a different approach" step requires the agent to know what approach it already tried and why it failed. Most implementations don't provide this.

Here's the specific failure mode. An agent calls a tool. The tool returns an error: wrong parameter type, permission denied, rate limited. The agent receives the error, processes it in context, generates a response that acknowledges the error, and then — in the next action cycle — calls the same tool again with parameters that have the same structural problem. The error was not misinterpreted. It was read and noted. The agent just didn't treat it as a binding constraint on future action selection.

This happens because the failure is stored as text, and the agent's action selection is not driven by a query against that text. It's driven by its policy — the model, prompted with context — which decides what to do next. When the model sees the error in context, it generates a response that mentions the error. But its action selection is not "check list of things that failed, avoid those." It's "generate the next most plausible action given this context." The error modifies the context, but it doesn't modify the agent's action space the way a constraint would.

You can see this in the structure of common agent loops. The loop reads the previous action result, prepends it to context, calls the model, gets the next action. The model sees the error. It may reason around it. But if the error doesn't change the relative scores of the available actions in the way a hard constraint would, the same action reappears.

The "don't retry" information has to be encoded in a way that actually restricts the action space — not just mentioned in context. Some implementations handle this by maintaining a failure registry as a separate data structure. When a tool returns a terminal error, the tool and the specific failure mode are written to the registry. Before calling any tool, the agent queries the registry. Tools with terminal failures in the registry are excluded from the action space for that task. This is a surgical change: it adds a constraint mechanism without changing the model's reasoning.

Without this, you're relying on the model to read an error message and update its behavior accordingly — which requires the error to function as a constraint, not just as text. The distinction matters more as tasks get longer and the error history gets more complex.

The longer the task runs, the more likely the agent is to treat early failures as background noise. The context fills up. The failure message gets pushed down. The model attends to more recent context. The constraint dissolves.

What you need is something that stays present regardless of context depth — a failure list the agent actually queries, not just reads.
