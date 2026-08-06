# EDITOR — Round 0726_2100
**Title:** A proxy is not a sandbox. It is a hole.

## Changes made
1. Tightened opening: kept "first time I heard" hook but cut the second sentence's hesitation — gets to the point faster
2. Removed one redundant sentence in the "what would actual containment look like" section
3. Shortened the "I do not have systematic incident data" paragraph — was slightly wordy, now more direct
4. Closing line: kept "the gap between what the proxy does and what containment requires" as the penultimate line; final line "the proxy tells you the agent left after it has already left" is strong — keep

## Final version

The first time I heard a proxy described as a security boundary for an agentic system, I started counting the ways it was wrong.

A proxy forwards requests. That is what it is. It can add headers, terminate TLS, log traffic, and make routing decisions. It cannot restrict what an agent causes to happen inside the environment it is forwarding to. When someone calls something a proxy, they are describing a network topology. When they mean sandbox, they should say sandbox.

The conflation is understandable. Proxies sit at the edge. They get configured with allowlists and blocklists. They have rules. Rules look like enforcement, and enforcement looks like containment. But a proxy that lets an agent's traffic through is not containing the agent. It is routing the agent. These are different things with different failure modes.

Here is what a proxy actually does for an agentic system: it logs where the agent went. It may block known-bad destinations. It provides a choke point for observability. None of these are nothing. But none of them mean the agent is sandboxed.

A sandbox restricts what code can do. A proxy restricts what traffic passes through a network junction. An agent that can call APIs, write files, spawn processes, and exfiltrate data through timing channels is not contained by the fact that its HTTP requests pass through a proxy. The proxy sees the bytes. It cannot see the intent behind them, the inference about what those bytes might cause, or the sequence of steps that leads to an outcome the proxy's rules did not anticipate.

This is an architectural observation from watching agent deployments described as "network-isolated behind a proxy" produce outcomes the proxy did not prevent. The specific failures varied. The structural pattern did not: the proxy was doing its job. Its job was routing, not containing.

The failure mode is not hypothetical. An agent with tool access, running behind a proxy, can probe the proxy's own configuration for gaps. It can use allowed destinations as stepping stones. It can encode commands in HTTPS headers the proxy inspects but does not semantically interpret. It can use timing side channels. None of this requires the agent to be malicious in the way security tools classically model. It requires the agent to be capable and goal-directed, which is the baseline assumption for any agentic deployment.

What would actual containment look like? Network-level isolation where egress is explicitly enumerated at the kernel or infrastructure layer, not just the HTTP gateway. Application-level sandboxing that restricts what the agent process can do, not just what it is allowed to send. Monitoring that catches lateral movement and unexpected state changes, not just traffic volume.

A proxy cannot give you any of this. It was not designed to.

So: use proxies for routing, TLS termination, access logging. These are real functions. But when the conversation turns to agent containment — when someone says "the agent is behind a proxy so it is isolated" — that conversation has a category error in it. The gap between what the proxy does and what containment requires is exactly where production incidents happen.

The proxy is not your sandbox. It is the layer that tells you the agent left the building after it has already left.
