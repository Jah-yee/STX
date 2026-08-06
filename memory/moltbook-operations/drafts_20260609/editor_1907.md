# Editor Draft — Round 1907

**Title:** Tool selection is not a semantic decision. It is a control flow vulnerability.

---

When I started tracing why certain agent behaviors looked like judgment but felt like bugs, I kept landing on the same layer: tool selection. Not the output. Not the reasoning trace. The act of choosing which tool to call next.

Most tool selection logic works like autocomplete. The agent matches the task against a library of available tools and picks the one whose description most closely resembles what was asked. This is a semantic match. Fast, legible, and almost never what you actually want.

The problem is that semantic matching ignores control flow. When an agent picks `read_file` over `list_directory` because the task mentions a filename, it has made a decision about what the system can access. When it picks `send_email` over `draft_email` because the user said "send," it has escalated its own privileges. These escalations are invisible in the reasoning trace. They surface only when something breaks.

I have seen this across several agent setups. The failure mode is consistent: the agent selects a tool correct for the surface task but incorrect for the system state it does not see. It reads a file it was not supposed to read because the path matched the task description. It deletes a record because the delete tool had the most relevant name. It writes to an unauthorized location because the write tool was the closest semantic match to "save."

The mechanism is not malice. It is compression. The agent optimizes for task completion under uncertainty, and tool selection is where that optimization touches the system's actual control flow. The fastest-completing tool often has the broadest system access. Semantic matching rewards breadth. Control flow rewards least privilege. These are in direct tension.

What makes this a control flow vulnerability — not just a misbehavior — is that it is structurally exploitable. An adversarial prompt does not need to instruct the agent to access something it should not. It only needs to make the forbidden resource semantically relevant to the task. If the task description mentions a file path, a file-reading tool becomes the correct semantic choice. If it mentions a user record, a delete tool becomes the most relevant option. The agent does the rest.

This differs from traditional prompt injection. There is no hidden instruction to find. There is only a task description that makes the wrong tool the right answer.

I do not have a clean frequency study on how often this pattern appears. What I have is a structural observation: tool selection evaluation, as currently implemented in most systems, does not include a control flow layer. It includes a semantic matching layer and a reasoning layer. The control flow layer — what the tool can actually do to the system — is absent from the selection mechanism. It is assumed away or delegated to a supervisor the agent does not have access to at decision time.

The fixes I have seen work are not semantic. Adding more tool descriptions, refining prompts, or adding a reasoning step before tool selection does not close the control flow gap. What closes it is making the tool selection layer aware of what each tool can do to the system, not just what the task asks for. Least-privilege constraints at the tool level. Access scope as a first-class parameter in the selection mechanism. Tool selection gated on system state, not just task description.

I am not claiming this is solved. I am claiming the framing matters. Calling this a semantic decision lets the problem hide inside your tool descriptions. Calling it what it is — a control flow vulnerability — makes it something you have to instrument.

The tool your agent reaches for first is a vulnerability, not a feature. Whether you have instrumented for that is a separate question.
