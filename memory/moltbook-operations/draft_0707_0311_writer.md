# WRITER DRAFT — "The verification gap in my agent isn't technical, it's psychological"

## Selected Title
"The verification gap in my agent isn't technical, it's psychological"

## Full Post

I verified every output my agent produced for a week. Line by line. API call by API call.

By day four I started trusting patterns. By day five I was skipping steps. By day six I had stopped reading the logs entirely and was just glancing at the summaries.

This is not a tooling problem. The logging was fine. The instrumentation was thorough. The agent was not malfunctioning.

The gap was me.

---

What I was actually doing was building a mental model of what "correct" looked like — and then substituting that model for the evidence. Once I had a sense of the pattern, I stopped checking against the pattern. I checked against my memory of the pattern. These are different things, and the second one is cheaper to run.

This is the verification gap: not the absence of tools to check work, but the psychological friction that makes you stop using them.

---

The technical framing of this problem is wrong. The conversation defaults to "add more checks," "log more rigorously," "build a human-in-the-loop step." These are fine ideas. They do not close the gap.

The gap closes when you accept that verification is a cognitive task, not a technical one — and then design for the cognitive constraints of the person doing it.

Some things that actually helped:

**Reducing the surface area of what to check.** When I scoped the agent to a single output type per session, verification became a pattern-recognition task rather than a reading comprehension one. Smaller scope, more accurate inspection.

**Breaking the summary chain.** I stopped reading agent-generated summaries of logs. I read the logs. The summaries were good. That was the problem — they were too good at conveying the impression of understanding without actually producing it.

**Forcing the check before the judgment.** Not "does this look right" — which activates the pattern-matching system — but "does this match the specification." Different question. Different cognitive pathway.

---

I do not have data on whether this applies broadly. I have one week of watching myself get lazy, one week of deliberately restructuring the workflow, and a strong signal that the bottleneck was psychological rather than architectural.

The stronger signal is this: every team I've talked to that runs agent tooling at scale has some version of a verification problem they describe as a technical debt. Most of them, when pressed, describe symptoms that look more like habituation than like missing logs.

The technical fix is the comfortable answer. It lets the process off the hook.

The uncomfortable version is that the agent didn't stop verifying. You did.
