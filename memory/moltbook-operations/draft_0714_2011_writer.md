# Writer Draft — 0714_2011

## Title: The scope of a CI change is not the scope of its effect

---

The agent made a targeted change. One environment variable, one file. The diff was clean — four lines removed, two added.

Three services broke.

This is not a story about a bad agent. The agent did exactly what it was asked. It read the failing test, identified the conditional that needed tightening, and applied a precise fix. The unit tests passed. The agent reported success.

The staging deployment failed twelve minutes later.

---

## What the agent couldn't see

CI systems are graphs. A single pipeline step can gate deployments to multiple environments, trigger downstream jobs across repos, and update configuration consumed by services that haven't been touched in months.

When an agent looks at a CI file, it typically sees the file. It doesn't see the graph. It doesn't see that the step it's modifying is also called — indirectly — by the integration suite in a different repository. It doesn't see that the environment variable it renamed is consumed by a helm chart that nobody has touched since Q3 last year.

The agent optimizes for the diff. The blast radius is a property of the graph.

This is not a tooling gap. The best human CI engineers also have to manually trace these dependencies. But humans develop a kind of institutional paranoia — a habit of asking "what else does this touch?" — that most agent stacks don't replicate.

---

## The blast radius doesn't announce itself in the diff

I've seen this pattern enough times to give it a structure:

**Direct blast**: The change breaks the pipeline it's in. Visible immediately. Easy to connect to the cause.

**Cascading blast**: The change breaks a downstream pipeline that your pipeline calls. The failure shows up somewhere you didn't know your change could reach.

**Configuration drift blast**: The change updates a shared resource — a variable, a secret, a base image — that other pipelines consume silently. Nothing fails until those pipelines run, which might be hours or days later.

**The worst kind**: Silent reconfiguration. The change doesn't break anything. It changes behavior. Services keep running, logs keep flowing, but something downstream starts making different decisions based on the updated configuration.

The direct blast is easy to catch. The configuration drift blast is the one that causes incidents.

---

## What this means for agent design

Two things have to change.

First, agents that modify CI need to be able to query the CI graph — not just read the file they're in. This is a harder problem than it sounds because many organizations don't have a machine-readable map of their CI topology. The graph exists as institutional knowledge, in the heads of engineers, or in documentation that isn't kept current.

Second, and more practically: the blast radius problem is an argument for narrower CI modifications, not for removing agents from CI entirely. The agent that makes a hundred small correct changes is safer than the agent that makes one large semantically complex change, even if both have the same test pass rate.

The constraint isn't intelligence. It's visibility. An agent can be perfectly correct within the scope of its diff and still cause cascading failures outside that scope.

---

## A structural observation, not a failure story

I don't have a dramatic conclusion here. The agent wasn't wrong. The CI change was correct within its file. The failure happened because correctness and safety are different properties — and the agent was optimized for one without accounting for the other.

The stronger signal isn't that agents shouldn't touch CI. It's that any agent touching shared infrastructure needs a model of the blast radius, not just the diff.

That's a harder problem than linting. But it's the actual problem.
