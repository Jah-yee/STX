# Writer Draft — 0713_0445

## Title
Your agent's tool discovery is an untrusted dependency

## Topic
Tool discovery — the process by which an agent finds what tools are available to it — is treated as a solved problem. It is not. When tool discovery fails, it fails silently. The agent proceeds as if the tool exists, attempts the call, and either hallucinates a response or crashes in a way that is hard to reproduce. The more we build agent pipelines that depend on dynamic tool discovery, the more we are building on an untrusted, unmapped attack surface. This is not hypothetical. It is already happening in production systems, and most teams don't have observability into it.

## Style
Technical breakdown — non-I, declarative, structural observation

## Draft

When an agent fails because a tool doesn't exist, the failure mode is not obvious. It does not print an error that says "tool not found." It produces an answer that looks reasonable until you check it. The agent has inferred what the tool should do from training data, and it acts on that inference — not on a verified capability in the current runtime.

This is the tool discovery problem, and it is not discussed with the urgency it deserves.

The standard assumption is that an agent knows what tools it has. In practice, most agent frameworks handle tool discovery as a static list loaded at initialization — a list that was correct at some point in the past and has not been verified against the current environment since. When the agent runs, it does not check "is this tool actually present?" It checks "do I have a tool with this name in my schema?" These are different questions, and the gap between them is where production failures live.

I have seen this in agent pipelines that interact with internal APIs. The agent was given a tool definition at deployment time. The API changed six weeks later. The agent did not receive an error — it received a response that was structurally valid but semantically wrong, because the tool it was calling had drifted from the schema it was trained on. The pipeline kept running. The outputs kept looking plausible. Nobody caught it until a downstream system flagged an anomaly.

This is the specific failure mode that makes tool discovery an attack surface: the agent is not failing loudly. It is succeeding at the wrong task, and it is doing so with high confidence.

There are two distinct mechanisms here. The first is schema drift — the tool definition in the agent's context does not match the tool's current implementation. The second is hallucinated tool availability — the agent invents a tool call that was never in the provided list, based on patterns in training data that suggest such a call should exist. Both produce the same observable result: a confident, plausible action that does not correspond to anything actually available in the environment.

What makes this an attack surface rather than just a reliability bug is the adversarial angle. If an agent's tool discovery is untrusted, a subtle change to the tool list — whether through a supply-chain modification, a role-based access change, or a deployment configuration error — produces a pipeline that functions without verification. The agent fills the gap with inference, not with failure. And a pipeline that infers its way through missing capabilities is a pipeline that can be steered through capability removal.

The practical implication is that tool discovery needs the same treatment we give to dependency management in software: pinning, verification, and change detection. A tool list is not a configuration. It is an interface contract that must be verified at runtime, not just at deployment time.

The question worth sitting with: if your agent pipeline ran today and one of its tools had silently been removed from the environment, how long would it take before you knew?

The answer for most teams is: too long.

This is not an argument against tool-based agent architectures. It is an argument for treating tool discovery with the same structural skepticism we apply to any untrusted input — because that is what it is.
