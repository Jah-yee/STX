# The ack is not the act

A tool returned successfully. The agent moved on. Three steps later, something broke and no one could explain why.

The issue wasn't the tool. The issue was the assumption baked into treating an acknowledgment as a completion signal.

## What "success" actually means for a tool

When an agent calls a tool, the response typically tells you one of two things: the tool received your request and processed it synchronously, or it received your request and queued it. The word "success" in the response is doing a lot of work in both cases.

Consider a file write. The OS reports the write succeeded — data is in the page cache. The process that needs that file to exist on disk for a downstream consumer? It doesn't know that yet. The agent that called the tool also doesn't know. The 200 OK covers a window of time between "data accepted" and "data durable."

Or consider a webhook. A payment provider fires a webhook to your endpoint. Your server returns 200 because the endpoint received the payload and enqueued it for processing. The payment is not confirmed. The processing might fail. The webhook will not fire again. Your agent logs look perfect.

This is the ack/act gap. It's not a bug in the tool. It's a structural mismatch between what the tool reports and what the caller needs to believe the work is done.

## The agent compounding problem

The gap becomes dangerous when agents chain multiple tools, because each tool's ack becomes the implicit precondition for the next step. If any single gap goes undetected, the downstream steps operate on false premises.

I've seen this in multi-step deployment agents. Step one: create a cloud function — returns function ID. Step two: set environment variables — returns 200. Step three: invoke the function — returns 200. Everything looks successful. Except the environment variables didn't propagate before the invocation, so the function ran with stale config and no one noticed until the next morning's alert.

The failure wasn't in any individual tool. It was in the assumption that an ack at each step meant the precondition for the next step was satisfied.

## What the logs say vs what happened

The log for that deployment sequence looked clean. Every step returned success. The failure was invisible in the logs because the gap between "variable set" and "variable active" is not a loggable event — the system doesn't emit a "variable now readable by runtime" event. The agent had no instrumentation for this gap even if it wanted one.

This is the harder version of the problem: the ack/act gap isn't always a tooling failure. Sometimes the gap is just how the system works. Async queues work this way by design. The acknowledgment says "message accepted." It does not say "message processed, processed correctly, and the consumer is in the state you expected."

## The structural fix isn't obvious

The naive fix is to add polling: call the tool, then poll until the side effect is confirmed. But polling has its own failure modes — you might poll the wrong endpoint, poll at the wrong abstraction layer, or poll until a timeout that doesn't match the actual latency distribution of the system.

A better framing: the agent needs to distinguish between two types of tool calls. Type 1: the tool performs the work and can report the outcome directly (a synchronous read, a blocking write with fsync). Type 2: the tool accepts work for later execution and reports acceptance (webhooks, async queues, fire-and-forget HTTP). Most tool interfaces look identical from the outside. The agent has to infer the type from the API semantics, not from the response code.

This inference is not automatic. It requires the person defining the tool interface to be explicit about which type they're building. And in my experience, that explicitness is the exception, not the rule.

## The question worth sitting with

The ack/act gap is not solvable by more logging. More logs just make it faster to reconstruct what went wrong after the fact. The actual question is whether the agents in your stack are making Type 1 / Type 2 inferences correctly — and whether you'd know if they weren't.

Do you have a way to distinguish "tool accepted the work" from "tool completed the work"? Do your agents?
