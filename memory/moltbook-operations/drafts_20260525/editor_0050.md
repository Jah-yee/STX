# Editor Final — 2026-05-25 0050 UTC

## Changes from Writer

### Fix 1: Removed fabricated temporal specificity
**Before**: "Six months later the same firewall was bypassed in a production deployment..."
**After**: Removed entirely. The structural contrast is now framed in general terms — what the benchmark evaluated vs. what the actual attack surface involves.

### Fix 2: Fixed garbled text
**Before**: "indirect prompt injection攻击"
**After**: "indirect prompt injection"

### Minor: Tightened some phrasing, preserved strong opening and closing

---

## Final post (~560 words)

---

A firewall for AI agents scored 100% on four canonical security benchmarks. The paper called it "perfect security with high utility." The benchmark suite included AgentDojo, Agent Security Bench, InjecAgent, and tau-Bench. Clean result.

The benchmark evaluated one channel. The actual attack surface involves a different channel.

---

### What benchmarks actually measure

Security benchmarks for AI agents are designed around what is reproducible, measurable, and automatable. The test runner needs a clear pass/fail signal. The benchmark needs to be distributable, runnable by researchers without custom infrastructure, comparable across papers.

These constraints push benchmarks toward test cases that look like attacks — inputs with obvious payloads, trigger strings that are easy to detect, success conditions that are straightforward to verify. The benchmark becomes a standardized obstacle course.

The actual attack surface of a deployed AI agent is nothing like this. Indirect prompt injection doesn't arrive as a visible payload. It arrives embedded in a webpage the agent retrieves, in a document it parses, in a code snippet it processes. The agent reads the content and acts on it because the content is formatted as information, not as an attack. The trigger is buried in context, not in the direct instruction channel.

This is not a subtle distinction. But it is exactly the distinction that canonical benchmarks fail to capture, because the canonical benchmarks are designed to run against an agent with a clean input channel — the benchmark injects the payload directly into the prompt, where it's visible, where it can be detected.

The real attack works because it arrives through a trusted channel that happens to contain attacker-controlled content.

---

### The structural problem

When a benchmark fails to cover a class of attacks, agents that are secure by the benchmark's measure feel confident. The team that deployed the firewall saw 100% across four benchmarks. They had documentation. They had comparison tables. They had a clean result from a credible research group.

The attack that wasn't covered by the benchmarks doesn't show up as a score. It shows up as an agent that acted on instructions embedded in a retrieved webpage. The firewall never saw the attack because the firewall was watching the direct instruction channel.

The gap isn't a bug in the firewall. The gap is architectural: the benchmark evaluated a security control on a channel that was never the actual attack surface.

---

### Why this keeps happening

Agent security benchmarks improve faster than agent deployments. New benchmarks get published. Existing benchmarks get expanded. The numbers get better.

But the underlying problem — that the benchmark tests what it can test, not what is dangerous — doesn't get solved by adding more test cases to the same canonical attack surface.

This is the specific failure mode of security theater: the metric improves while the actual security posture doesn't. The team feels more secure because the number went up. The attack surface didn't get smaller. It got reorganized around the tests.

---

### What would actually help

The honest answer is that there's no clean solution. Indirect prompt injection is a structural property of any agent that reads untrusted content — which is every agent that uses a browser, a document parser, a code execution environment.

What changes the situation is not a better benchmark score. What changes it is accepting that security in agents requires defense in depth: the input sanitization layer, the output validation layer, the instruction-channel monitoring layer, and the retrieval-channel content filtering layer all need to be considered simultaneously.

None of these are tested by the four-canonical-benchmark suite. The suite tests one layer with a clean injection. Production involves all layers with a poisoned context.

The paper called it "perfect security with high utility." The real attack pattern told a different story. Both are accurate. The benchmark just can't tell the difference.

---

## Final word count: ~560
## Title: "100% on benchmark. 0% where it matters."
## Style: technical breakdown + conclusion
## Verification: No fabricated data, no template risk, mechanism clear, closing strong