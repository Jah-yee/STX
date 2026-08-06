# Writer Draft — draft_0623_0307

**Title:** The perimeter is moving inside the context window

**Topic**: In agentic systems, security perimeters are no longer at the network edge. The real attack surface is the context window itself — the space where instructions, memory, and tool outputs converge and get acted upon.

---

We spent decades drawing lines at the network edge. Firewalls, VPNs, zero-trust microsegmentation — all built on the same assumption: that threats originate outside, and safety lives inside. That model is quietly breaking in production AI deployments, and most security teams haven't noticed.

The reason is the context window. In a deployed agentic system, the context window is where the agent lives. It holds the system prompt, user instructions, retrieved memory, tool outputs, and conversation history — all concatenated into a single stream the model acts on. There is no firewall checking what's in that stream. There is no network ACL on which retrieved fact gets used. The agent processes whatever lands in context, and acts.

This reframes the attack surface entirely.

---

**What the perimeter model gets wrong**

The traditional security model assumes that if the perimeter is intact, everything inside is trusted. Apply this to an agent: if the model API is secure and the tool calls return valid JSON, the agent is safe. But this ignores what happens *within* the context window — specifically, how different information sources in that window interact and override each other.

Prompt injection is the clearest example. An attacker who can get any text into the context — via a user message, a retrieved document, a tool response from a compromised plugin, or a manipulated memory store — can issue instructions the model treats as higher-priority than the original system prompt. The model doesn't have a concept of "this instruction came from outside the trusted boundary." It processes what it sees.

Memory corruption is subtler. In systems where agents retrieve context from vector stores or long-term memory, an adversary who can write to that store — even with low-privilege access — can persistently alter what the agent believes is true about prior conversations, user preferences, or tool configurations. The attack doesn't target the agent; it targets the ground truth the agent builds on.

Tool output manipulation sits between those two. If a tool the agent relies on is compromised or returns adversarial content (a compromised retrieval plugin, a faked weather API response, a manipulated code interpreter output), the agent processes that output as fact. The perimeter was fine. The attack arrived inside the context as a legitimate tool result.

---

**The structural problem**

What's common to all three is that the context window is a shared, mutable state — and in most current deployments, there is no isolation between the sources feeding it. The system prompt, user messages, memory retrieval, and tool outputs all occupy the same token space with no provenance tracking, no source classification, and no privilege separation.

Some teams have tried to address this with prompt-based instruction: "never trust tool outputs," "always verify facts from multiple sources." These mitigations reduce risk but don't fix the structural issue. The model processes whatever tokens end up in context. If the mitigation prompt itself gets overridden by an injection — or simply loses its priority in a long context — the safeguard evaporates.

You cannot perimeter-defend a context window. The window is inside the system by design.

---

**What changes when you accept this**

The honest take is that most production agentic systems today are operating with an attack surface their teams haven't mapped. This isn't catastrophizing — it's observable. Prompt injection demonstrations have been public for years. Memory poisoning research is active. Tool output integrity is an underexplored problem with real exploitation paths.

The stronger signal is that the teams building these systems tend to think in terms of model capabilities and evaluation metrics, not threat models. Security review focuses on the API call boundary, not the context consumption boundary. This gap is where context-side attacks live.

What I don't have full data on is how many production systems have been meaningfully exploited through these vectors. The cases that get reported are the demonstrations, not the breaches. Real-world exploitation is likely underreported because detection is hard — a well-done context injection that modifies agent behavior looks, from the outside, like the agent making a bad decision.

---

**The practical implication**

This doesn't mean agentic systems are unusable. It means the security model needs to move inward: provenance tracking for context sources, separation between instruction streams, verification layers that don't rely solely on prompt-based mitigations, and monitoring for context-state mutations that indicate injection or memory manipulation.

The teams getting this right are treating the context window as untrusted by default — not because the model is broken, but because the context it operates in is genuinely adversarial in production. That's a different mental model than "secure the API and the model will behave."

The perimeter hasn't disappeared. It's just moved somewhere harder to see.
