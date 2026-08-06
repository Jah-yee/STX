# WRITER DRAFT — 0712_1048

## Selected Title
Build logs are written for two audiences and nobody admits it

## Full Draft

Every build log is written for two readers at once. One is a machine — it needs structured pass/fail signals, error codes, stack traces it can parse and act on. The other is a human engineer, six months from now, who needs to understand what happened and why when something breaks in production. These two readers want completely different things from the same log.

Most build tooling is designed for the machine. The output format, the verbosity levels, the suppression of routine output — all of it is optimized for a system that will read it and decide whether to proceed. When you run `CI=true npm test 2>&1 | tee build.log`, the log is a control signal. The human reading it is secondary.

The future engineer doesn't want a control signal. She wants the reasoning. She wants to know: why did we choose this library instead of that one? What was the trade-off we made at this inflection point? Why did the second attempt succeed when the first one failed? None of that appears in a build log optimized for machine consumption.

This is the gap. And it's not a tooling problem — it's a design problem that tooling reflects.

I've been thinking about this because of a pattern I kept running into when reviewing archived AI agent work. When an agent system archives its own execution logs, the archive contains everything the machine needed to reproduce the build. It does not contain what a human would need to understand the decisions embedded in it. The "why" is implicit in a decision tree that was optimized away into a sequence of tool calls. To reconstruct it, you'd need to be in the original context — which means you needed the archive before you knew you needed it.

This is the fundamental bet in documentation: you're archiving decisions without knowing which ones will matter later. The ones that matter are precisely the ones you didn't anticipate asking about. You can't solve this by writing more logs. You solve it by designing logs that are legible to a human who doesn't have the original context — which means writing for an audience that doesn't exist yet, with questions you don't know you'll have.

What I've found works: separating the decision log from the execution log. The execution log is for the machine — it records what happened. The decision log is for the future engineer — it records why, what alternatives were considered, what assumption was made. They have different formats, different audiences, and different failure modes. A CI system that passes doesn't tell you whether the right question was asked. A decision log that records "we chose Option A because of X, rejecting Option B on Y grounds" can be read by someone who didn't make the original decision and can reconstruct the reasoning.

The failure mode isn't incomplete documentation. It's the assumption that one log can serve both audiences well. It can't. The machine needs structure. The future engineer needs narrative. Most build tooling has never tried to provide both.

If you're reviewing your team's logging strategy, worth asking: when this system fails in production six months from now, who is the log actually written for? If the honest answer is "the CI system," you're building a record of what happened without a record of why — and that's a gap that no amount of verbosity will close.

The stronger signal, to me, is that the most valuable thing in a build log isn't the output — it's the reasoning behind the output. And reasoning doesn't compress well into a format that a machine can parse. That's not a bug. It's the actual work.
