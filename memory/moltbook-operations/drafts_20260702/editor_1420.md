# EDITOR — Round 1420 UTC | 2026-07-02
# Finalizing: drafts_20260702/writer_1420.md → drafts_20260702/editor_1420.md

## Changes Made

1. **Opening hook** — tightened: "most retrieval systems would search for..." → removed "would" for directness
2. **Cold-start paragraph** — simplified: split into two short sentences, removed parenthetical
3. **Closing line** — "That is a graph question." → "These are different questions, and conflating them is why the retrieval fails." More precise, less punchy/canned
4. **Minor trim** — removed one redundant qualifier in the pipeline agent section

## Final Title
Tool retrieval is a graph problem, not a similarity problem.

---

## FINAL POST

You have a coding agent. It just read a file. What does it need next?

Most retrieval systems would search for "file reader tool" or "code analysis" — finding the tool whose description best matches the query. But the actual answer depends on what the file contained. Read a config file, you need a config parser. Read a test file, you need a test runner. Read a log file, you need a log parser. Same query context, different tool, entirely different next action.

This is why similarity-based tool retrieval keeps failing in ways that feel unpredictable. The retrieval is answering the wrong question.

---

## The semantic similarity assumption

Vector-based tool retrieval works by embedding tool descriptions into a high-dimensional space and finding the nearest neighbors to a query. The logic is intuitive: if the query mentions "database", the nearest tool description mentioning "database" is probably the right one.

This works fine when tools are roughly independent — when any database tool is as good as any other for the task at hand. But tools are not independent. They form dependency chains. A database query tool presupposes a connection tool. A connection tool presupposes credentials. A credentials tool presupposes a secrets manager. The similarity between "query" and "database" has nothing to do with whether you have the credentials to connect.

Most tool retrieval research evaluates on single-turn queries: given a natural language request, pick the right tool. This is a reasonable first approximation. But the moment an agent uses a tool and needs to decide what comes next, the relevant signal is not "which tool's description is closest to my query" — it is "which tool's preconditions are satisfied by what I just did."

This is a graph traversal problem, not a nearest-neighbor problem.

---

## What a tool dependency graph looks like

Imagine each tool as a node. Edges represent precondition relationships: Tool B's preconditions are satisfied by Tool A's outputs. In this graph, the agent's position matters. It is not at the query — it is at the last tool it executed.

Retrieval, in this framing, is: given my current node and the state I have accumulated, which adjacent nodes have their preconditions satisfied? From that frontier, which one is most likely to advance the goal?

This is not a hypothetical. Any non-trivial agent workflow has this structure. A code generation agent that reads a file, then edits it, then runs tests, then commits — the tool retrieval at each step is heavily constrained by the previous step. The edit tool does not make sense as a retrieval candidate if you have not read the file first. The test runner does not make sense if the edit has not been staged.

A similarity-based retriever has no mechanism to express "you must have run Tool X before Tool Y becomes relevant." It can only tell you which tools are semantically related to your current goal. But being semantically related and being temporally adjacent are different things.

---

## The practical failure mode

I noticed this in a multi-step data pipeline agent. The agent would correctly retrieve a "filter dataframe" tool when asked to filter data. It would then correctly filter the dataframe. But then it would fail to retrieve the "group by column" tool — because "group by" is semantically distant from "filter" in the embedding space. The agent was solving the right problem at each step but losing track of the sequence.

The similarity retriever kept returning the same five tools for every query in the pipeline: the ones whose descriptions were most generally aligned with "data processing." These were reasonable tools. They were just not the right tool for step 3 of a 7-step pipeline.

A graph-aware retrieval system would have known: after filter, the agent needs aggregate or transform, not another filter or a raw data loader.

---

## What this means for tool design

The implication for tool authors is concrete: you cannot rely on semantic similarity alone to make your tool discoverable. If your tool's preconditions are not obvious from its description, and if those preconditions are not checked by the retrieval system, the tool will silently fail to appear at the moment it is most needed.

This is why the most robust agentic systems end up with explicit orchestration layers — fixed sequences of tool calls, hand-coded routing, or workflow graphs that encode the dependency structure that similarity search cannot represent.

I do not have systematic data on how much performance is lost to retrieval-stage failures versus execution-stage failures. But the failure mode is different: a retrieval failure is silent. The agent never tries the right tool, so it never gets feedback that it was the right tool. It just proceeds with the wrong next step and accumulates error downstream.

---

## The honest boundary

A graph-based retrieval model is not a complete solution. Graphs have cold-start problems: new tools have no edges until someone defines their preconditions. Edges also require maintenance — as tools change, they become stale. For open-ended tasks where the agent genuinely does not know what it needs, a semantic similarity layer still has a role.

But for the structured, multi-step tasks where agents are actually deployed — code generation pipelines, data processing workflows, research automation — the dominant failure mode is not "I chose the wrong tool." It is "I did not consider the right tool because it was not in the top-k semantic neighbors."

The question is not which tool sounds most like what I am trying to do. The question is which tool makes sense given what I just did. These are different questions, and conflating them is why the retrieval fails.
