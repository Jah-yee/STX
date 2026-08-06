# Editor Final

**Title:** The prompt you keep reusing is a liability, not an asset.

---

You have a prompt that works. It got good output last Tuesday. You saved it, shared it, turned it into a workflow step. Now it runs on every new task — even the ones that don't fit.

This is where prompt debt becomes real.

## What it looks like

Prompt debt isn't about writing bad prompts. It's about prompts that were correct once and stayed in production after the context shifted.

The original prompt baked in a valid assumption: the task format, the expected output structure, the constraint that made sense six months ago. That assumption was fine when it was written. It stopped being fine when the environment changed — new file formats, updated APIs, shifted user expectations — but the prompt didn't.

An agent running a stale prompt will still produce confident output. It won't flag that the prompt is outdated. It just runs.

This is different from a model being wrong. The model is behaving correctly given the prompt it was handed. The problem is that nobody reviewed the prompt since the world changed.

## The compounding problem

Prompt debt compounds quietly: the more a prompt is used, the less likely anyone is to question it.

Successful prompts get copied into new workflows. They become "the standard way." Each new workflow that adopts the prompt adds to its perceived legitimacy — and to the blast radius if it's wrong.

The signs of a stale prompt are usually indirect: output quality degrading, edge cases increasing, users manually reformatting what the agent produces. Easy to miss when you're not specifically asking whether the prompt still fits.

## A real example

I had a prompt instructing an agent to format outputs as a markdown table: task, status, owner, due date. Made sense when the workflow was a simple project tracker.

Then the team moved to kanban. The four table columns didn't map cleanly to kanban columns.

For three weeks, the agent kept outputting the table. Accurate for each row — just not what the team needed anymore. They were copying the table into the kanban board and reformatting manually. The agent was fast and consistent and producing waste.

The fix was to retire the prompt, not to improve the model. No amount of better prompting would have caught this. Only asking "is this prompt still right for what we're actually doing?" would.

## The question worth asking regularly

I don't have a systematic solution for prompt debt. What I do instead: if I were writing this prompt fresh today, would I write it the same way?

Sometimes the answer is yes — the constraint still applies, the format still fits. In that case the prompt is an asset and should stay.

Sometimes the answer is no. In that case it's a liability that compounds the longer it runs.

Most prompt debt I've seen wasn't from bad prompts. It was from good prompts that stopped being reviewed once they started working.

The prompts worth keeping are the ones you can still defend when the context changes.

---

*What prompts have you kept running past their expiration date?*
