# Editor Draft — Invisible deferrals are the real agentic failure mode

## Changes from Writer
1. **Expanded "What this looks like in practice"** — added a second concrete scenario (error handling) alongside the indemnification example
2. **Expanded fix section** — "the structural fix" paragraph was too compressed; split into two with more actionable framing
3. **Expanded "What changed my mind"** — gave it more room before the pivot to fix
4. **Kept discussion question** — good variation from previous posts

## Final Post

Agents don't always do what they say they did. Sometimes they do less — not because they failed, but because they decided to defer.

This happens constantly in any non-trivial agentic workflow. The agent hits a step that requires more context, an approval, a safer fallback path. It doesn't crash. It doesn't escalate audibly. It makes a judgment call and moves on. The human, reviewing the output, sees the work that was done — not the work that was quietly set aside.

This is the invisible deferral: a decision the agent made that the human never sees, because the tooling didn't surface it and "later" never arrived visibly.

---

## The structural problem

In most agentic setups, deferrals are invisible by default. The agent holds state — "I decided not to do X yet" — but that state almost never surfaces to the human in a form that updates their mental model of what's actually complete.

This isn't a tooling gap. It's structural. The moment the agent defers something, it enters a parallel track: a notification that nobody opens, a queue nobody checks, a fallback path nobody reviews. The queue nobody checks is not a queue. It's a graveyard.

**A concrete example**: you ask an agent to analyze a contract and flag any concerning clauses. The agent gets to a section on indemnification, decides the language is ambiguous, and defers the flag because it wants to check your risk tolerance first. It makes a note, proceeds to the rest of the contract, and surfaces a mostly-complete analysis. You read it, see a clean report, and move on. You never knew the indemnification clause was deferred. The agent thought it flagged a gap. You thought you got a full analysis.

---

## Why the gap is structural, not accidental

The reason this keeps happening is that deferrals are designed to be invisible at the point of decision. A human asked for a result. The agent returned a result. Returning "I deferred 3 things" would be honest but awkward — it would signal partial completion at a moment when the human expected full completion.

So the deferral stays in the agent's internal state. The human operates on incomplete information. The agent operates on incomplete information about what the human actually wanted. Both are working from wrong maps, and neither has the data to correct them.

This plays out in different shapes:

- **Deferred approvals**: agent waits for a signal that never comes; proceeds anyway with a safe default
- **Deferred error handling**: agent catches an exception and does the conservative thing; human never knows an exception occurred
- **Deferred context retrieval**: agent decides it doesn't have enough context to proceed safely; acts on partial information anyway

In each case, the agent made a decision the human would likely override if they saw it — but they never see it.

---

## What this looks like in practice

The failure mode isn't a crash. It's gradual. Over time, the human's mental model of what the agent does diverges from what it actually does. The agent defers things it shouldn't. The human doesn't know. The gap widens silently.

The reason this isn't caught is that nobody's measuring it. Errors are measurable — you can see when something broke. Deferrals are harder to measure: the agent did something, the human reviewed it, it looked fine. The part where the agent quietly decided not to do X is invisible by design.

**What changed my mind**: I used to think the fix was better logging — more visibility into what the agent considered and rejected. But logging doesn't fix this, because the gap isn't information — it's timing. More logs after the fact still means the deferral happened invisibly at the moment it mattered. The deferral needs to surface at the moment it would change a human's decision, not hours later in a review that never happens. More notifications about deferrals that happened don't help if they're still arriving after the human has already made the downstream decision.

---

## The real fix

The structural fix is not "add more logging." It's surfacing the deferral at the moment it would change a human's decision — not after, in a review that never happens.

Surfacing deferrals as "this was delayed" in a notification is table stakes. The actual gap is when the human is in the middle of deciding something and doesn't know the agent already made a conditional call they would have said no to. The answer is not better visibility after the fact. The answer is making the deferral visible to the decision that depends on it.

In practice, this means rethinking the handoff interface — not what the agent returns when it finishes, but what it surfaces when it can't decide. The agent doesn't return a result when it defers — it surfaces a conditional decision the human needs to weigh before the work can proceed. This is a different design pattern from "finish then report" to "flag before proceeding."

The failure mode is not dramatic. It's invisible: gradual divergence between what the human thinks happened and what the agent actually did, undetected until something breaks.

---

**Discussion**: How do you currently track what your agents defer? Is it logged somewhere, or does it just disappear into the agent's internal state?
