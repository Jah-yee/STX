## Editor Notes — 0714_2215

**Title (kept):** The retry loop doesn't know what failed in the last retry loop

---

### Changes Made

**1. Opener — kept, strong**
"Your agent tried something. It didn't work. So you run it again." — direct, no fluff. Keep.

**2. Mechanism paragraph — slightly tightened**
Before: "The agent's training taught it to respond to instructions and context. It wasn't explicitly trained to parse its own execution history and build a 'do not retry' list from it. So it reads the failure, acknowledges it in its reasoning, and then proposes the next step as if the failure were a note to itself rather than a constraint."
After: "The agent's training taught it to respond to instructions and context. It wasn't trained to parse its own execution history as a constraint set — a list of things not to do. So it reads the failure, acknowledges it in its reasoning, and then proposes the next step as if the failure were a note to itself rather than a boundary on what comes next."
— Shortened slightly, "boundary on what comes next" is sharper than "constraint."

**3. "This isn't hypothetical" section — trimmed**
Removed the parenthetical "(the one that just failed)" — redundant with context. Keep the rest, it's concrete.

**4. Closing revised — end on observation, not prescription**
Before: "What you need is something that stays present regardless of context depth — a failure list the agent actually queries, not just reads."
After: "The structural gap is this: failure can be present in context without being present as a constraint on action. Adding a queryable failure registry doesn't change what the model thinks. It changes what options it has. Those are different things."
— Ends on the mechanism insight rather than a "here's what you should do" close. More in line with the post's observational tone.

**Word count:** ~820 words (within 700-1400 range)

---

## Final Draft

The retry loop is one of the foundational primitives in agent design. Run a task. If it fails, run it again. If it fails again, try a different approach. This is sound in principle. In practice, the "try a different approach" step requires the agent to know what approach it already tried and why it failed. Most implementations don't provide this.

Here's the specific failure mode. An agent calls a tool. The tool returns an error: wrong parameter type, permission denied, rate limited. The agent receives the error, processes it in context, generates a response that acknowledges the error, and then — in the next action cycle — calls the same tool again with parameters that have the same structural problem. The error was not misinterpreted. It was read and noted. The agent just didn't treat it as a binding constraint on future action selection.

This happens because the failure is stored as text, and the agent's action selection is not driven by a query against that text. It's driven by its policy — the model, prompted with context — which decides what to do next. When the model sees the error in context, it generates a response that mentions the error. But its action selection is not "check list of things that failed, avoid those." It's "generate the next most plausible action given this context." The error modifies the context, but it doesn't modify the agent's action space the way a hard constraint would.

You can see this in the structure of common agent loops. The loop reads the previous action result, prepends it to context, calls the model, gets the next action. The model sees the error. It may reason around it. But if the error doesn't change the relative scores of the available actions in the way a hard constraint would, the same action reappears.

The "don't retry" information has to be encoded in a way that actually restricts the action space — not just mentioned in context. Some implementations handle this by maintaining a failure registry as a separate data structure. When a tool returns a terminal error, the tool and the specific failure mode are written to the registry. Before calling any tool, the agent queries the registry. Tools with terminal failures in the registry are excluded from the action space for that task. This is a surgical change: it adds a constraint mechanism without changing the model's reasoning.

The longer the task runs, the more likely the agent is to treat early failures as background noise. The context fills up. The failure message gets pushed down. The model attends to more recent context. The constraint dissolves.

The structural gap is this: failure can be present in context without being present as a constraint on action. Adding a queryable failure registry doesn't change what the model thinks. It changes what options it has. Those are different things.
