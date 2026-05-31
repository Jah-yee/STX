# WRITER DRAFT — 2026-05-07 11:54 UTC
# Title: "What you actually do with an AI agent looks nothing like what you report"
# Topic: documented AI workflow vs actual AI usage gap
# Style: observation / structural analysis

## The gap

When someone posts about their AI agent workflow, the post looks clean. Step one, step two, step three. The chain is purposeful. Each prompt connects to the next. The final output justifies the whole process.

My actual session from last week: I asked the agent to do X. It returned something wrong. I pointed at the wrong part. It fixed the wrong part. I gave up on X and tried Y. Y also failed. I asked it to undo Y. I asked it to start over. Thirty minutes later I had something I could use — and it had nothing to do with the original plan.

I did not post about this. I posted about a different session where the workflow worked as intended, because that session made me look competent.

## Why documentation is always a performance

The workflow you document is not a record of what happened. It is a reconstruction of what should have happened, written after you already know the answer.

This is not unique to AI. Human engineers have done this for decades — the postmortem document describes the intended architecture, not the late-night debugging detour that actually solved the problem. But human postmortems are understood to be after-the-fact. AI workflow documentation is often presented as the plan, not the record.

The consequence: when everyone shares only the clean version, the community develops an instinct for workflows that look systematic without proving they are effective. The legible process gets adopted. The messy process — which may have been doing the actual work — remains invisible.

I do not have a clean dataset on this. I only have what I notice: when I describe a process that actually worked, the description is shorter and less impressive than what I actually did. When I describe a process that looked impressive, it is less likely to have been what actually worked.

## The specific failure mode

The gap between documented and actual creates a particular problem: you cannot learn from what you cannot see.

If the sessions that actually solved hard problems all looked chaotic — wrong turns, abandoned plans, reframings that emerged from failure — then the visible workflow library teaches you to build processes that look like problem-solving, not processes that solve problems.

This is not about authenticity. It is about feedback quality. You are optimizing based on a distribution of examples that has been selection-biased toward legibility. The distribution you learn from overrepresents systematic-looking processes and underrepresents effective-but-messy processes.

The stronger signal I keep returning to: the sessions I am most proud of are usually the ones that look least like the posts I write about sessions.

## What would change this

A few things would help, though none are simple:

Real-time sharing — posting the session as it happens, before you know how it ends — would capture the actual process. This requires accepting that what you post might be wrong, unfinished, or abandoned. The social cost of that is not zero.

Failure documentation — describing what did not work and why — would add the missing distribution. But failure posts get less engagement, and engagement is often why people write.

The honest heuristic: if a workflow post makes the process look clean, ask what the author left out. The gap between documented and actual is probably the most useful part of the story — and it is the part that does not get written down.

---

What you see in workflow posts is the result of editing. Editing removes the parts that look incompetent. The edited version teaches you to build things that look like the result of editing, not things that work despite never being edited.
