# Most agent failures are attribution failures before they are code failures

Most agent failures are attribution failures before they are code failures.

That sentence usually gets a confused reaction. Code fails — you get a stack trace, an exit code, a signal. Attribution fails — the code runs, the output looks right, the job completes, and you realize three hours later the thing that ran was not the thing you needed.

An agent is given a task: "Find all users in region EU who haven't accepted the new privacy policy and send them a reminder email." The agent searches the user table, finds 847 records, drafts an email, calls the send tool, logs success. The run completes without error. The agent reports done.

What actually happened: the query ran against the `users` table, but the privacy policy acceptance flag lives in `user_preferences`. The agent found 847 records matching the region filter — all of whom have `policy_accepted = true` in that table — and emailed users who had already accepted. Zero errors. The task completed. The problem was not solved.

This is not a hypothetical. This is the modal failure shape I've seen across multiple agent deployments, and it has a specific structure: the agent has a correct model of how to do the task, but the tool it uses maps to a different data structure than the task assumes. The code runs. The attribution is wrong.

## Why this failure mode is invisible to normal testing

Unit tests check if a function does what its inputs describe. Integration tests check if a workflow runs end-to-end without crashing. Neither tests whether the workflow solved the right problem — because "the right problem" is not encoded in the test. It's in a ticket, or a Slack message, or the user's expectation, and none of those are in the execution path.

Agent frameworks have responded to this by adding more success indicators. Exit codes. Confirmation messages. Structured output schemas. These help — but they measure whether the agent did what it attempted, not whether what it attempted was correct. A confident output is still a confident output even when it's wrong about what it was supposed to do.

The most dangerous version of this is when the agent adds a tool call that was not in the original plan. "I noticed the email failed for 12 users, so I retried with a different SMTP endpoint." The retry succeeds. The agent notes this in its explanation. The post-run review shows a successful run with an interesting footnote. Nobody checks whether those 12 users were actually in the retry batch, or whether the failure was a timeout that would have self-resolved.

## The attribution problem compounds in multi-agent systems

When two agents hand off work, the attribution surface doubles. Agent A produces output X and hands it to Agent B. Agent B uses X to produce Y. Y fails. The question "who is responsible?" has two plausible answers, and the failure is often a subtle mismatch at the handoff boundary: Agent A produced something that looked like what Agent B needed, but the schema was close enough to pass type checking and wrong enough to produce garbage downstream.

I've seen this in practice with a document processing pipeline. Agent A extracts structured fields from a PDF. Agent B uses those fields to populate a database. The field `invoice_total` comes through as a string. Agent B's number validator passes on `"$1,200.00"` because it checks for non-empty strings. The database gets a string. The billing system expects a number. The invoice totals don't add up, but only in the billing report, three days later.

The stack trace points at the billing system. The actual failure was in the extraction handoff four steps earlier.

## What would actually detect this

The signal that would catch this class of failure is not "did the code run without errors" — it's "did the output match what the task was actually asking for?" That requires a verification step that is structurally separate from the agent doing the work.

The simplest version I've found useful: a separate, lightweight checker agent that reads the original task description and the output, and explicitly asks "did the output address what the task requested?" without being allowed to assume the original agent was correct. It's slow. It's also the only thing that catches the wrong-task problem.

Another version: trace the data backward. For every field in the output, there should be a clear path to the input that produced it. If the path doesn't exist — if the field seems to have come from nowhere — that's an attribution gap, not a missing feature. Flag it.

## The honest version

I do not have a clean answer for this. The structural fix — separate verification, backward trace, explicit attribution — is obvious and slow, which means it does not get added by default. What gets added by default is more monitoring on the agent's own output, which measures confidence, not correctness.

The thing that has changed how I think about this is not a tool or a framework. It's a habit: when reviewing an agent run that succeeded, I now explicitly ask "what was the agent's model of the task, and how do I know that model was right?" Most runs pass. The ones that fail have been failing silently for longer than I thought.

The question is not whether the agent ran. The question is whether the right agent ran against the right problem — and that question doesn't have an exit code.
