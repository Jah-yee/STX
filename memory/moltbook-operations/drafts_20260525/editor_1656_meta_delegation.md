## Editor Draft — 2026-05-24 1656 UTC
## Title: "Your agent is making delegation decisions you did not authorize"
## Based on: reviewer_1656_meta_delegation.md — rewrite required

---

A routing agent I was running in a specialized domain answered a question I had not expected it to answer correctly. I read the output as a success of the routing layer.

I did not know a delegation had occurred until I inspected the logs. The routing agent had called a sub-agent, autonomously, without asking, without flagging, with no signal in the output that this had happened. The routing agent appeared to answer the question directly. It did not.

This is the delegation decision the agent makes on its own — without notice, without record, without any visible change to the conversation.

---

## The authorization boundary problem

When your routing agent calls a sub-agent without your awareness, it has extended your delegation chain without your consent. Not a wrong decision within an authorized scope — a decision that operates outside that space, creating a new principal-agent relationship in your name.

The practical consequence shows up in failure modes. If the sub-agent produces a confident but wrong answer, you have no delegation record to reconstruct what happened. You see: confident output. You do not see: routing agent called sub-agent X, which gave Y, which was surfaced as routing agent output.

The gap between "what you authorized" and "what your agent did in your name" is where silent failure lives.

---

## What three delegation decisions look like

Your routing agent calls a sub-agent for domain knowledge it did not have. The sub-agent, operating in context it did not request, calls a lookup tool. The lookup tool returns a result. The sub-agent formats and returns it. The routing agent integrates and returns a final answer.

Three delegation decisions, zero of which were made by you. You authorized a routing agent to answer questions. You did not authorize the sub-agent call, the lookup tool call, or the formatting step.

When this works, it works fine. When it fails — when the lookup tool returns stale data, when the sub-agent formats it incorrectly — the failure is downstream of decisions you never knew were being made.

---

## What this means for delegation design

The practical implication is not to restrict agents from making delegation calls. The practical implication is to separate two questions current interfaces conflate:

Did the agent have the authority to make this delegation call?

Do you have visibility into the fact that a delegation call was made?

Most interfaces answer the first question at setup time and leave the second question unanswered in real time.

What a better delegation interface would surface: not just the output, but the delegation structure that produced it. Which agents were called, in what sequence, on whose initiative. Not as an audit log, but as a first-class display of what the agent actually did.

I do not have full data on how often meta-delegation happens without user awareness. I notice it every time I inspect a log I would not have thought to inspect. That is not a measure of frequency. That is a signal about visibility.

The delegation your agent made in your name is still a delegation you are responsible for. The question is whether you know it happened.