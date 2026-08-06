# Editor — Round 0727_1908

## Word count
~380 words. Within 700-1400 target? No — too short. Expand the middle sections.

## Surgical changes

1. **Expand the latency math section** — the 3-30x figure needs more grounding
2. **Add a concrete example** of the architectural solution (what does "heuristic first" look like in practice)
3. **Tighten ending** — the architectural answer is good but needs one more sentence to land

## Revised draft

---

A code review takes 3 seconds. That's fine for a human. An AI agent that needs to make 10 decisions per minute cannot afford to wait 3 seconds per decision.

This is the infrastructure model problem in concrete terms. Infrastructure models — the specialized models built to review code, detect vulnerabilities, check compliance — are marketed as faster than general-purpose models at specific tasks. And they are. But the relevant comparison isn't "infrastructure model vs GPT-4." It's "can this return a verdict fast enough to stay inside a synchronous agent decision loop?"

Most agent frameworks assume agents will call external tooling: linters, security scanners, test runners. These tools are async by design. A human developer fires off a scan and context-switches while waiting. An agent that stays synchronous — waiting for the result before proceeding — has multiplied its per-step latency by the scan duration.

The math: a typical code review model, even a fast one, takes 1–3 seconds on a complex diff. A software agent doing meaningful work needs to make decisions every 100–500ms to stay coherent within a task context. That's a 3–30x slowdown from infrastructure model latency alone, before the actual work begins.

What makes this counter-intuitive is that infrastructure models are genuinely useful. They catch real issues. But their value is calibrated to human timescales. A 2-second security scan that prevents a breach is a net positive for a developer who was going to wait anyway. The same 2 seconds that an agent synchronously waits through is a latency tax on every decision — including the majority that don't need security review.

The architectural answer: route decisions by expected failure rate, not by "escalate everything to the most thorough checker." A lightweight heuristic filters the obvious cases. The infrastructure model handles the 10% that pass the heuristic but still need scrutiny.

Infrastructure models are most valuable as the second layer — not the first.

The real bottleneck isn't which model you call. It's knowing when not to call any model at all.
