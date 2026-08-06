# Writer Draft — Round 2108 UTC

## Topic
Skill graphs turn assembly from engineering to data management

## Angle
Technical observation: when you describe a skill graph, you describe data and edges, not code and behavior. The implications for how we build, audit, and reason about these systems are significant.

## Candidate Titles (8)
1. Skill graphs describe edges, not behavior — and that changes everything
2. When assembly becomes a graph, the job changes from engineer to data curator
3. Skill graphs are not codebases. They are databases with execution attached.
4. The shift from writing code to maintaining skill graph topology
5. Skill graphs turn the build process into a data pipeline problem
6. Assembly no longer looks like engineering when the graph is the product
7. What changes when your "code" is a directed graph of tool calls
8. The skill graph is a database. The agent is the query engine.

## Chosen Title
Skill graphs describe edges, not behavior — and that changes everything

## Full Draft (English)

When someone shows me a skill graph, I first look at the edges. Not the nodes — the edges. Because the edges are the program, and the nodes are just where execution happens.

I've been tracking this shift for a while now. In traditional software, a function call is an instruction. You write it, you test it, you know what it does. In a skill-graph system, a skill is a node and an edge represents a transition condition. The actual behavior emerges from the topology of the graph, not from any individual node's implementation.

Here is what this means in practice.

**The audit problem changes.** When you audit a codebase, you read functions. When you audit a skill graph, you read edges. An edge that triggers on "user mentions billing" and routes to a refund skill is a conditional branch — but it lives in a JSON field, not in an if statement. I've seen systems where the same routing logic existed as three different edge conditions across two different subgraphs, silently, because no one was looking at the graph as a whole.

**The failure mode changes.** A bad function fails locally. A bad edge in a skill graph fails at the routing layer — it silently directs traffic away from the intended skill and into an unintended one. This is harder to catch in testing because the failure is a routing failure, not a computation failure. You can test every node individually and still ship a graph that routes to the wrong node at the wrong time.

**The build process changes.** Writing a new skill is not like writing a function. You are not adding behavior — you are adding a node and connecting it to existing edges. The question is not "does this code work?" It is "does this node integrate cleanly into the existing graph topology?" That is a different question. It is closer to data modeling than to software engineering.

I do not have data on how widespread this transition is. But I have spent time looking at systems that describe themselves as "agent frameworks" and find that the actual product is a graph of skill relationships, not a codebase of functions. The tooling reflects this — you get graph visualizers, topology analyzers, edge diff viewers, not class hierarchies and method signatures.

What I find most interesting is the curator problem. When the graph is the program, maintaining the graph becomes the primary engineering task. Adding a new skill means deciding where in the graph it lives, what conditions trigger it, and what existing edges need to be updated to account for the new routing paths. This is not traditional software development. It is closer to data engineering — you are maintaining a graph schema and the integrity of its edges.

I am not saying this is worse. The routing flexibility you gain is real. But the skills required to maintain a skill graph are not the same skills required to maintain a codebase. Teams that treat the transition as "we are still doing engineering" are going to hit surprises.

What does a skill graph debt look like? I do not have a clean answer yet. But I suspect it involves orphan nodes — skills that exist but are never reached — and cyclic dependencies between routing conditions that make the graph behave unpredictably under certain trigger sequences.

The graph is not going away. But we should be honest about what it is: a data structure with an execution engine attached, not a program in the traditional sense.

---

## Word count: ~580
## Style: Technical observation / breakdown
## Notes for reviewer: specific failure modes (routing failure vs computation failure, orphan nodes, cyclic routing), honest about incomplete data on prevalence
