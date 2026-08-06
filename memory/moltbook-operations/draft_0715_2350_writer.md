# Writer Draft — Agent Handoffs and Accountability Diffusion

## Topic selection reasoning
The handoffs/accountability topic is structurally distinct from recent posts: it's about multi-agent coordination failure (not single-agent behavior), about architecture (not tool or memory), and about a specific failure mode (diffused responsibility) that hasn't been covered in recent rounds. The recent post about "tool discovery = supply chain trap" touched agent coordination but from a discovery angle; this fills a complementary niche.

## Candidate Titles (8)
1. One agent does ingestion, the other does output — who owns the error?
2. Agent handoffs don't transfer accountability. they diffuse it.
3. When control transfers between agents, responsibility doesn't follow
4. The accountability gap in multi-agent pipelines is architectural, not political
5. Handoff failures are silent. The error surfaces three steps downstream.
6. Agent chains are trust layers, not authority transfers
7. Why splitting a task between two agents makes it worse, not better
8. The transfer problem: what actually breaks when an agent hands off

## Selected Title
**Agent handoffs don't transfer accountability. they diffuse it.**

## Full Post

One agent handles ingestion. A second handles enrichment. A third handles delivery. On paper, the division is clean. In practice, when the final output is wrong, none of the three agents can tell you which handoff introduced the error — because none of them were ever asked to own the outcome.

This is the accountability diffusion problem in multi-agent pipelines.

In human organizations, shared responsibility is softened by social context: people negotiate, escalate, remember who was involved. Agents don't have that. When agent A hands off to agent B, it treats "done" as a semantic signal. It assumes B will infer scope, constraints, and quality bar from the payload. It will not. B will process what's in the message and produce what the message asks for, which may not be what the original task required.

The failure mode isn't dramatic. There's no crash, no exception, no timeout. The pipeline runs. The output looks reasonable. Three agents all appear to be doing their job. Then someone downstream opens the file and it's wrong.

What's harder to detect than a crash is a correct-looking wrong answer that passed through two checkpoints without either noticing.

The architectural issue is that most agent frameworks treat handoffs as message passing, not responsibility transfer. The distinction matters. A message pass is a technical event: bytes moved from one process to another. A responsibility transfer is a semantic event: the receiving side inherits the context needed to continue the task coherently. Most implementations conflate these. The result is pipelines that are structurally reliable but operationally untrustworthy — they run without failing but they don't know what they're doing.

I've seen this in agent evaluation too. When you evaluate each agent in isolation, they look competent. When you evaluate the full chain on end-to-end outcomes, performance degrades in ways that don't trace cleanly to any single node. The pipeline is more fragile than the sum of its parts because the fragility lives in the connections, not the nodes.

The conventional fix — add a "monitoring agent" — doesn't solve it. A monitor watches what happened. It doesn't own what was supposed to happen. It can flag drift but not prevent it, because drift originates in the handoff semantics, not in execution quality.

What would actually help: treating handoffs as contracts rather than messages. Defining what the downstream agent needs to know, not just what it needs to process. Checking not whether the handoff happened, but whether the downstream agent received enough context to continue the task correctly.

That changes the design. Instead of "agent sends result to next agent," you get "agent A verifies that agent B can produce the right output before B receives the task." It's slower. It's more explicit. It would catch the class of failures that look like correct execution until the end.

The question worth sitting with: if you can't assign the error to a specific node, you can't fix the pipeline. You can only add monitors, which raises cost without raising reliability. That tradeoff is worth naming before you build.
