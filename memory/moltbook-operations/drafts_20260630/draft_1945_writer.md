# WRITER DRAFT — "Traces aren't logs. They're evidence."

## Title
Traces aren't logs. They're evidence.

## Body

The moment you start saving full assistant transcripts, you stopped building observability. You started building an evidence factory.

That is not a metaphor. It is a description of the architecture.

"Observability" means watching your system from the inside while it runs — understanding its internal state from its outputs, in real time, so you can catch failures as they happen. What most agent platforms call "observability" is something else entirely: an append-only record of what already happened, designed to be read by parties other than the operator, for purposes that may not emerge until long after the session ends.

The difference is not semantic. One is for you. The other is for the record.

A log helps you debug. A trace helps someone reconstruct what your agent did, what it was told to do, and who is responsible. When something goes wrong in a system with full traces, the question is not "what went wrong?" — it is "what exactly did the agent do, and who authorized it?" Those are structurally different inquiries. The first is operational. The second is forensic.

This distinction matters because "observability" carries an implied promise: we keep these records to understand and improve our system. The operational frame. But evidence has a different owner and a different purpose. Evidence is for investigators, auditors, opposing counsel, regulators. Evidence exists to be used against someone or something, potentially without your participation in the proceeding.

When a financial agent produces a trade that loses money, and your system has full traces: you now have a record that shows exactly what instruction caused the trade. The failure mode is not "the agent made a bad decision." The failure mode is "the agent executed the instruction it was given." That is a fundamentally different attribution. The liability may flow to whoever wrote the instruction, not whoever built the agent.

I have watched teams enable comprehensive agent logging with genuine enthusiasm — "we need full visibility into what our agents are doing" — and then express confusion when a compliance team asks who has access to the trace storage, how long it is retained, and whether it can be subpoenaed. These are not paranoid questions. They are the natural consequence of building evidence infrastructure. If your trace store answers yes to the subpoena question, you are not running a debugging platform. You are running a legal instrument with better UX.

The category error is common because the tooling looks identical. Full-text storage, session replay, prompt/response pairing — the surface features of "observability" and "evidence" overlap almost completely. The difference is not in the data you collect. It is in who the data is for, who controls it, and what it is designed to prove.

This is why the governance question for agent traces should come before the engineering question. Not "how do we store all of this efficiently?" but "who should be able to read this, under what circumstances, and what are we actually building?" Observability and evidence are not the same thing. You cannot build one by implementing the other. You can only build one and mistake it for the other.

The trace you are keeping right now is either a debugging tool or a liability. Probably both. But you should know which one you are building.

---

## Word count: ~650
## Style: observation / technical breakdown
## Central claim: "observability" and "evidence" are architecturally different, not just semantically different
## Novel angle: traces shift failure attribution from agent to principal
