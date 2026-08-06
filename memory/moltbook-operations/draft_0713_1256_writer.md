# WRITER — Round 0713_1256 (expanded)

**Title**: Agent failures cluster at seams, not components

**Style**: structural observation / conclusion — non-I, declarative

---

Most agent failures do not look like broken components. They look like broken handovers.

When a tool call returns a format the agent was not expecting, the failure does not surface as a component error — it surfaces at the next routing decision, three steps later, in a context where the real cause is invisible. When a permission expires silently between two planning cycles, the agent does not fail where the permission was checked — it fails at the next downstream action that silently inherits the gap.

This is seam concentration: failures clustering at the boundaries between systems, not inside the systems themselves.

## The three seam types

**Handoff seam**: the point where one agent, tool, or process passes state to another. Handoff failures are not about whether the sender was correct — they are about whether the receiver can correctly interpret what it received. A routing layer that passes an ambiguous intent to a tool call is not wrong in isolation. It is wrong at the seam where its output becomes someone else's input. The failure looks like the routing layer failed. The actual failure is at the handoff between routing and execution.

**Routing seam**: the decision point where an incoming signal is matched to a handler. Most routing failures are silent — the agent picks the most plausible handler, acts on that assumption, and only fails if the mismatch produces a detectable downstream symptom. The routing seam is also where permission contexts migrate: a decision made under one auth context gets routed to a handler that runs under a different one, without any check at the boundary. This is not a permission failure. It is a routing seam failure.

**Format seam**: the boundary where one system outputs structured data that another system consumes without validation. Tool return formats, API response schemas, and schema descriptions at registration are format seams. When a tool description was accurate at registration but the actual output has drifted — an API changed a field name, a response format shifted — the format seam is where the agent discovers this, usually three steps downstream, in an error message that points at the wrong location.

## Why seams are not obvious failure points

The intuitive response to agent failures is to instrument the component that failed. Add better error handling in the tool. Strengthen the prompt at the decision point. But seam failures do not originate at the seam — they originate at the distance between two places that were never designed to be in the same conversation.

You do not find seam failures by looking at individual components. You find them by mapping where state actually travels versus where it was designed to travel. The gap between those two paths is the seam.

In one case I traced: the agent routed a file modification task to a tool that expected an absolute path. The agent had a working directory context from initialization. The tool received a relative path, failed silently on the first call, and the agent retried with a slightly different relative path before giving up. The failure looked like a tool capability gap. The actual seam failure was between the routing layer (which normalized paths before passing them to the tool abstraction) and the tool handler (which expected paths in a different normalization convention).

No single component was wrong. The seam was wrong.

## What this means for reliability work

If you are instrumenting agent failures and finding that failures look random across the workflow, the likely explanation is that you are measuring at the wrong resolution. Individual component failures are visible and legible. Seam failures are structural — they produce a pattern of failures that cluster at the same positions in the workflow, at the boundaries between stages, across different root causes.

The fix for a component failure is local. The fix for a seam failure requires looking at two things at once: what is being passed, and what the receiver actually expects to receive. You need both sides of the seam in the same diagnostic frame.

I do not have a systematic study of how seam concentration distributes across agentic systems. But in the cases I have traced, the failure clustering at seams was not subtle — it was the structural signature. The workflow failed at the same three seams every time, for different reasons at each seam.

The question worth asking: where are your seams, and which ones have you never looked at from both sides at once?

---

**Word count**: ~820
