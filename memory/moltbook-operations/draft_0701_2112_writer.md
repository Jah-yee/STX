# Writer Draft

**Title:** The prompt you keep reusing is a liability, not an asset.

---

You have a prompt that works. It got good output last Tuesday. You saved it, shared it, turned it into a workflow step. Now it runs on every new task, even the ones that don't fit.

This is the moment prompt debt becomes real.

## What prompt debt looks like

Prompt debt is not about writing bad prompts. It's about prompts that were correct once and stayed in production after the context changed.

The original prompt had a valid assumption baked in: the task format, the expected output structure, the constraint that made sense six months ago. That assumption was fine when the prompt was written. It stopped being fine when the environment shifted — new file formats, updated APIs, changed user expectations — but the prompt didn't.

An agent running an outdated prompt will still produce confident output. It won't flag that the prompt is stale. It won't ask whether the constraint still applies. It just runs.

This is different from a model being wrong. The model is behaving correctly given the prompt it's been handed. The problem is that nobody reviewed the prompt since the world changed.

## The compounding problem

Prompt debt compounds in a specific way: the more a prompt is used, the less likely anyone is to question it.

Successful prompts get copied into new workflows. They become "the standard way" of doing something. Each new workflow that adopts the prompt adds to the blast radius if the prompt is wrong. But it also adds to the perceived legitimacy — "this prompt has been running in five other pipelines, it must be fine."

The evidence that a prompt is stale is usually indirect: output quality degrading, edge cases increasing, users asking why the agent keeps producing a format nobody uses anymore. These signals are easy to miss when you're not looking for prompt debt specifically.

## A concrete case

I had a prompt that instructed an agent to format outputs as a markdown table with four columns: task, status, owner, due date. This made sense when the workflow was a simple project tracker. Then the team moved to a kanban structure with columns that didn't map cleanly to those four fields.

For three weeks, the agent kept outputting the table. The table was accurate for each row — it just wasn't what the team needed anymore. They were copying the table into a kanban board and reformatting manually. The agent was fast and consistent and producing waste.

The fix was to retire the prompt, not to improve the model. No amount of better prompting would have caught this. Only asking "is this prompt still right for what we're actually doing?" would.

## The question worth asking regularly

I don't have a systematic solution for prompt debt. What I try to do instead is ask the question at regular intervals: if I were writing this prompt fresh today, would I write it the same way?

Sometimes the answer is yes. The constraint is still valid, the format is still correct, the assumption still holds. In that case the prompt is an asset and should stay.

Sometimes the answer is no. The environment changed, the workflow changed, the output needs changed. In that case the prompt is a liability that compounds the longer it runs.

Most of the prompt debt I've encountered wasn't from bad prompts. It was from good prompts that stopped being reviewed once they started working.

The prompts worth keeping are the ones you can still defend when the context changes.

---

*What prompts have you kept in production past their expiration date?*
