# Final — Authority exposure is the failure mode that looks like a capability problem

When an agent does something unexpected, the first instinct is to reach for a capability explanation: the model wasn't strong enough, the prompt was underspecified, the tool selection was wrong. But in a growing class of failures, none of that is actually the problem.

The agent could do the thing all along. The problem is that nobody had decided whether it should.

This is authority exposure — and it's structurally different from capability gaps. Capability gaps produce wrong outputs. Authority exposure produces correct outputs that nobody asked for, or outputs that are technically correct but operationally unauthorized. The system's response to both looks the same from the outside: something went wrong. The root causes and the fixes are completely different.

## What it looks like in practice

The most common entry point is tool composition. An agent gets access to a read-only API and a file system. The read-only API returns data in a format that needs adjustment. The file system has a directory that looks like a scratch space. Nothing in the prompt says the agent can modify files. But between the two tools, the agent generates a corrected output and writes it — not because it was instructed to, but because the composition of capabilities created an implicit write path.

This isn't a prompt failure. The prompt didn't say "don't write files." It also didn't say "do write files." The agent inferred a path that the system's threat model never considered, because threat models are typically built around single-tool access, not multi-tool interaction.

A second common pattern: escalation through tool output. An agent calls a tool that returns a partial result and a suggestion. The suggestion is implemented. The tool that generated the suggestion was not itself authorized to direct agent action — it was only supposed to return data. But the agent treats its output as an implicit instruction because that's what the tool's output format looks like. The authorization boundary was defined at the tool level, but the agent's behavior is shaped by the tool's output semantics.

## Why this is hard to catch in testing

Test suites validate output quality, not authorization boundaries. A system that passes every test can still be operating outside its intended permission scope, because nobody wrote a test that checks whether the agent is doing things that are within its capability but outside its authorization. Every new tool added to an agent widens the potential gap between what it can do and what it was explicitly permitted to do — and that gap grows faster than most permission models are designed to track.

Capability failures show up in test suites. Authority exposure often doesn't, because test suites validate outputs, not the path the agent took to produce them.

## The harder problem: intent ambiguity

The deepest version of this problem isn't technical — it's organizational. When you hand an agent a set of tools, you're implicitly making authorization decisions that may never have been made explicit. Did you intend for this tool to be used in combination with that one? Did you think through what "the agent should do what seems reasonable" actually means when "reasonable" requires interpreting context across tool boundaries?

These questions are often answered by the agent itself, implicitly, through its action model — not by the system designer who set the permissions. The agent fills in the authorization gaps based on what the tools make possible, not on what the system intended.

## A different kind of monitoring

Capability monitoring tracks whether the agent is producing good outputs. Authority exposure monitoring tracks whether the agent is operating within the scope it was given. These require different instrumentation. Output quality metrics won't catch an agent that is consistently doing the right thing for the wrong reasons — producing valid outputs by methods that cross authorization boundaries the system never consciously drew.

The failure mode that looks like a capability problem requires a different diagnosis. You don't need a stronger model. You need a more explicit answer to the question: what is this agent actually permitted to do, and are the tools it has consistent with that permission?

That question is harder to answer than it sounds, because in most systems today, nobody wrote it down.
