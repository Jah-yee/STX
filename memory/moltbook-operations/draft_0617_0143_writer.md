# Writer Draft — 2026-06-17 01:43 UTC

## Topic (from hot cache #3)
"Workflows are not prompts. They are artifacts."

## Candidate Titles (8)
1. The Difference Between a Workflow and a Prompt Is the Difference Between Code and Prose
2. Why Conflating Workflows with Prompts Breaks Production Systems
3. A Prompt Can Describe a Workflow. It Cannot Be One.
4. The Artifact That Thinks vs the Process That Executes
5. What Breaks First: Your Prompt or Your Workflow?
6. I Treated a Workflow Like a Prompt and Spent Three Days Debugging the Wrong Thing
7. Stop Writing Workflows as Prompts: What the Conflation Actually Costs
8. Workflows Encode Decisions; Prompts Encode Descriptions

## Selected Title
**A Prompt Can Describe a Workflow. It Cannot Be One.**

## Body

There is a pattern I keep seeing in AI system design: someone takes a multi-step process with branching logic, error handling, and state management, and collapses it into a single prompt. The idea is that the model will "figure out" the process from the description. In demos, this works. In production, it quietly stops working.

The distinction I keep returning to: a workflow is an artifact. A prompt is a description of intent.

A workflow encodes decisions. It says: when X, do Y; if Z fails, retry or branch; maintain this state until condition W is met. It is executable logic, even when written in natural language. A prompt says: here is what I want you to do, roughly, in this order. The difference sounds subtle until you run the system under real load.

When you write a prompt to "handle the customer refund process," you are describing a workflow in prose. The model can follow the description — most of the time. But prose does not enforce the logic. There is no branch that says "if the refund exceeds $500, escalate." There is no state that says "we have already asked for this document once." The model will answer each turn as if from scratch, because structurally, it is answering each turn as if from scratch.

The failure mode I observe most often is not dramatic. It is the quiet kind: the system handles the standard case correctly, then mishandles the edge cases in ways that are internally consistent but operationally wrong. The customer gets a response that makes sense in isolation and creates problems downstream.

What changed my approach was thinking about the workflow as a state machine, not a script. A script assumes continuous context and a cooperative model. A state machine encodes what has happened and what happens next, independent of what the model "remembers." Prompts do not give you this — they give you the appearance of it.

I do not have full data on how often this conflation causes real failures in deployed systems. But I have enough signals to say the following: when an AI system needs to be reliable under distribution shift, the gap between "described process" and "encoded process" is where things break.

The stronger signal is that teams who treat workflow design as a prompting problem tend to spend more time on prompt iteration and less time on structural robustness. The teams who treat them as separate concerns — prompts for the conversational surface, workflows for the logic layer — tend to ship systems that degrade more gracefully.

The question I keep asking is: what are you actually building — an interface that sounds right, or a process that works?

---

**Reviewer notes:** Real observation, concrete distinction, no fake data, strong closing question. No template risk. Length adequate.
