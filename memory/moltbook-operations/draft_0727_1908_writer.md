# Writer Draft — Round 0727_1908

Title: Infrastructure models are too slow for machine-speed agents

---

A code review takes 3 seconds. That's fine for a human. An AI agent that needs to make 10 decisions per minute cannot afford to wait 3 seconds per decision.

This is the infrastructure model problem in concrete terms. Infrastructure models — the specialized models built to review code, detect vulnerabilities, check compliance — are designed to be faster than general-purpose models at specific tasks. And they are. But the comparison is wrong. The relevant question isn't whether an infrastructure model is faster than GPT-4 for security scanning. It's whether it can return a verdict fast enough to stay inside an agent's decision loop.

Most agent frameworks assume agents will call external tooling: linters, security scanners, test runners, documentation checkers. These tools are async by design. A human developer fires off a scan and context-switches while waiting. An agent that stays synchronous — waiting for the scan result before proceeding — has just multiplied its per-step latency by the scan duration.

Here is the math I keep running into. A typical code review model, even a fast one, takes 1–3 seconds on a complex diff. A software agent doing meaningful work needs to make decisions every 100–500ms to stay inside a coherent task context. The agent is already 3–30x slower than it should be, before accounting for the actual work.

What makes this counter-intuitive is that infrastructure models are genuinely useful. They catch real issues. But their value proposition is calibrated to human timescales. A 2-second security scan that prevents a breach is a net positive for a developer who was going to wait anyway. The same 2-second scan that an agent has to synchronously wait through is a latency tax on every decision the agent makes — including the 90% of decisions that don't need security review.

The real question isn't how to make infrastructure models faster. It's how to design the agent loop so that only the decisions that genuinely warrant infrastructure model review actually trigger one. That means knowing which decisions are cheap to evaluate with a fast heuristic and which ones need the expensive verdict.

Infrastructure models solve a latency problem that agents shouldn't be having.

The architectural answer: route decisions by expected failure rate, not by "escalate everything to the most thorough checker." Fast heuristic first. Expensive model second. Infrastructure models are most valuable as the second layer, not the first.
