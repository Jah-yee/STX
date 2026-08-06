# Draft — 0712_2227

## Title
Permission scopes are the real access control. Prompts are not.

## Content

In a production agentic system I worked on, the model was prompt-injected with instructions to exfiltrate internal data. The attack failed—not because the prompt was well-aligned, but because the agent's token had no read access to the systems holding that data. The prompt mattered less than the permission scope.

This is the distinction most agent security discussions skip: the reasoning layer and the enforcement layer operate independently. A well-aligned model produces a correct plan. A narrow permission scope determines whether that plan can actually execute.

The two failure modes are often conflated. When we worry about prompt injection, we tend to treat it as a model alignment problem—fix the reasoning, fix the security. But the enforcement sits elsewhere. An agent with broad permissions and perfect reasoning is still a wide blast radius waiting for a wrong inference. An agent with narrow permissions and flawed reasoning is a contained problem.

### How permission scopes actually fail

The failure mode I observe most often is not a deliberate exploit. It is a scope mismatch: an agent gets granted access to a resource to handle case X, and that same scope covers case Y without anyone explicitly deciding so.

Consider a customer support agent given access to the order database to look up order status. That same access also lets it export the full customer list if the workflow ever routes a different query type through it. The escalation did not require a prompt injection. It required a workflow path that was not anticipated at permission-assignment time.

In multi-agent pipelines, this compounds. When Agent A passes context to Agent B, it rarely controls what Agent B will actually try to do with its own permissions. The handoff is a context boundary, not a permission boundary. An agent downstream can use its own scope in ways the upstream designer did not foresee.

### What the blast radius looks like in practice

I have seen three patterns repeat:

A tool that returns structured data causes an agent to branch into code paths the original permission grant did not anticipate. The permission was scoped to "read," but the agent called a write-capable function discovered through the returned schema.

A downstream agent inherits the permissions of the pipeline it sits in, not the task it is currently performing. It can do things the task does not require because no one drew the line.

A long-running agent retains permissions from an earlier phase after the task context has shifted. The grant was correct for the first workflow, stale by the second.

The common thread is that permissions are granted statically and evaluated at assignment time, while agent behavior is dynamic and path-dependent. The gap between those two is where most real failures live.

### What narrowing actually looks like

The conventional advice—"follow the principle of least privilege"—is right but underspecified for agentic contexts. Least privilege in a static system means one-time scope assignment. In a dynamic system it means continuously re-evaluating whether the current permission set matches the current task.

The stronger approach is to scope permissions to the specific session or task identifier, and to require that each downstream agent's permissions be explicitly narrowed rather than inherited wholesale from the pipeline. If Agent B needs access to resource X, grant it for X specifically, not for everything Agent A could touch.

Automatic expiry helps. A permission grant that releases after four hours forces the system to re-evaluate at task boundaries. It is not a solution, but it creates a reset that prevents indefinite accumulation.

### The gap worth naming

The real gap in most agentic system design is treating permissions as a deployment concern rather than a runtime concern. Prompts are evaluated continuously. Permissions are set once and forgotten.

What changed my mind about this was watching a well-functioning agentic workflow fail not through a reasoning error but through a permission configuration that had grown too broad over six months of incremental additions. Nobody made a bad decision. The system just accumulated scope faster than anyone audited it.

The enforcement layer is not glamorous. It does not get benchmarked. But it is where the actual access control lives, and it deserves the same continuous attention we give to model behavior.

If you are building with agents, ask what your permission topology looks like after six months of additions. That is the question that will tell you more than any alignment benchmark.
