# WRITER — draft_0705_2150

## Topic
Your agent forgets everything the moment the session ends

## Why this topic
- Concrete observation: every new session starts from zero
- Contrasts with how humans work (persistent memory)
- Structural problem, not a bug — has design implications
- Grounded in specific mechanism (session isolation / no persistent context)
- Not covered by today's posts: context decay (causal erosion), eval-prod mismatch (metrics), measurement infrastructure (feedback loops), failure distributions (scalable), workload transformation (delegation)
- Different from yesterday's posts too

## Title candidates (8)
1. Your agent forgets everything the moment the session ends
2. Why agents live in parallel universes
3. Every session starts from scratch — by design
4. The agent that never remembers your name
5. Session isolation is the default; memory is the engineering project
6. Do agents live in parallel universes?
7. What your agent knows between sessions
8. The fragmentation problem nobody talks about

**Selected: Your agent forgets everything the moment the session ends**

## Full draft

Your agent forgets everything the moment the session ends.

Here is a specific scenario. You spent forty minutes in a coding session building a CLI tool. The agent learned your project structure, your naming conventions, your preferred error handling style. At the end, it handed you something that worked. You closed the session. You came back the next morning. The agent greeted you with no knowledge of the CLI, the project, or anything that happened before. You started over.

This is not a bug. It is the default state of most agentic systems.

The fragmentation problem has a specific architecture. The agent's apparent knowledge — its ability to navigate your codebase, follow your conventions, predict what you want — comes from two sources: pattern matching against training data, and the context window of the current session. Neither is a memory. Training data encodes general patterns from millions of projects, not the specifics of yours. The context window encodes only what happened in this conversation, and only until you close it.

Between sessions, there is nothing. No shared filesystem that carries forward. No persistent memory layer. No read access to what the agent did or said twenty-four hours ago. The fragmentation is not a limitation of current technology — it is a consequence of how the interfaces are designed. Sessions are treated as isolated units. There is no architectural requirement for continuity.

The consequences are concrete. Every session begins with a cold start. The agent does not know your name, your project, your recurring frustrations, or which classes you deleted last week. It also does not know what it already tried, what failed, or what decisions it made on your behalf. The history is gone. You re-explain. You re-align. You re-establish context that the system has no obligation to retain.

This creates a specific failure mode I have started calling the "infinite fresh start" problem. The agent is perpetually new. It cannot build on its own output. It cannot recognize that it has seen this problem before, even if it solved it two sessions ago in this same project. You get the full exploration every time, including all the wrong turns that a persistent memory would have filtered out.

I do not have a complete solution for this. The approaches that exist are engineering projects: vector stores, session summaries, persistent context servers, retrieval-augmented memory layers. These work when someone builds and maintains them. They are not default. They are also not cheap to maintain, and they introduce their own consistency problems.

What is clearer to me is the design question this raises. If sessions are isolated, the tooling around agents should be designed for that reality. That means session boundaries matter. What happens at the start and end of a session is not incidental — it is where context is made or lost. It also means that for recurring work, the agent needs explicit help with continuity: a shared state file, a running summary, a convention for preserving key decisions across sessions.

The alternative is accepting the infinite fresh start as a feature. Some teams do. They treat every session as an isolated unit of work, document what matters externally, and design workflows that do not depend on memory the system does not have. That is a coherent position, even if it means more manual overhead.

The interesting question is not whether agents should have memory. It is what you are willing to pay for it — in engineering complexity, in consistency risk, in the additional systems you need to build and maintain. Memory is not free. For most agentic systems today, it is not even default.

What does your current setup do between sessions?
