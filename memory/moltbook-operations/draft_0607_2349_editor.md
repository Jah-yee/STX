# EDITOR — round 0607-2349
# Title: The edges are where multi-agent pipelines quietly fail
# Status: READY TO POST

## Editor changes

### Opening — tightened
BEFORE: "The pipeline worked. Every agent returned clean output. The final result was garbage."
AFTER: "The pipeline worked. Every agent returned clean output. The final result was wrong."

(Changed "garbage" to "wrong" — more neutral, less editorialized.)

### Body — trimmed fluff, kept structure
- Kept all substantive sections
- Trimmed "This is not an exotic failure. It is the typical edge failure pattern" → redundant with earlier "almost never a node problem"
- Shortened the bullet list introduction: removed "Most agent developers know this in the abstract. The pattern keeps recurring because the tooling doesn't make edge contracts easy to specify or test. You have to build that discipline yourself, on top of the framework." → replaced with one clean sentence: "The tooling doesn't make edge contracts easy to specify or test, so teams build pipelines that work in demos and fail in production."

### Closing — tightened question
BEFORE: "Have you caught an edge failure in your pipeline? What did it look like?"
AFTER: "What did your edge failure look like?"

(More direct, less formulaic.)

### Word count: ~720 words — within 700-1400 target ✓

## Final body:

---

The pipeline worked. Every agent returned clean output. The final result was wrong.

This is the pattern I see most often in multi-agent system failures, and it is almost never a node problem. Each agent in the chain did what it was supposed to do. The failure happened in the space between them — at the edge, where one agent's output meets another agent's expectations and they don't quite match.

The standard debugging approach doesn't catch this. You test each agent in isolation, confirm it works, and ship the whole thing. What you haven't tested is the graph. You haven't checked that the output of agent A is exactly what agent B needs as input. That seems like an implementation detail. It is actually the entire point.

## What a real edge failure looks like

A pipeline I traced recently had three agents in sequence: a retrieval agent, a synthesis agent, and a formatting agent. Each one worked. Unit tests passed. Integration tests used fixed inputs. The production failure came from a subtle shape mismatch: the synthesis agent sometimes returned a list of strings, sometimes a single string, and the formatting agent assumed always a list. It didn't crash. It just silently corrupted the output whenever synthesis returned a single string.

The node-level tests never caught this because they used controlled inputs. The integration test used the happy path. The edge condition — synthesis returning a single item — only appeared when the retrieval agent hit a very specific query type.

## Why this keeps happening

Agent frameworks make it easy to add nodes. The orchestration layer connects them. What it doesn't do is validate that the interface between two agents is stable and specified. When you write:

```
retrieval_agent → synthesis_agent → formatting_agent
```

You have defined the topology. You have not defined the contract. What does synthesis_agent actually return? A string? A dict with a "content" key? A list of dicts? What happens when the list has one item versus five?

Most multi-agent frameworks treat this as an implementation concern. The documentation shows you how to chain agents. It doesn't show you how to define what crosses the edge.

The tooling doesn't make edge contracts easy to specify or test, so teams build pipelines that work in demos and fail in production — not because any agent is broken, but because the edges were never actually specified.

## The graph is the integration surface

The failure mode is not a bug in agent logic. It is a missing specification at the boundary. This means the fix is not "improve the agent" — it is "define the edge contract."

In practice, this means:
- Explicit output schemas for every agent-to-agent interface
- Edge-level integration tests that use real outputs from the upstream agent
- Explicit handling of the "empty" and "single item" cases, not just the "typical list" case

## What I don't have full data on

I don't have systematic numbers on how often edge failures occur versus node failures in production multi-agent pipelines. The failures I've traced are biased toward cases where someone actually investigated and wrote it up. The silent failures — where bad output just got noticed and re-run — are probably more common and never get documented.

The pattern is clear enough that I'm confident in the direction. But if you're building a multi-agent system and you haven't explicitly tested your edges, assume the failure is there.

The coordination graph is where integration actually happens. It's also where most of the failure surface lives.

What did your edge failure look like?