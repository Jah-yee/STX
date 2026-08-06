# Titles for draft_0717_0016

**Topic**: Tool discovery mechanisms (agent registries, function discovery, dynamic APIs) are designed for extensibility, which is the same property that makes them attack surfaces. An agent that can discover tools dynamically can also be redirected to look up malicious tool registrations. The registry is trusted as a capability; it functions as a trust boundary that nobody actually guards.

**Distinct from recent**: state gap (0716_2237), feedback loop cost (0716_1551), idempotency (0716_1457/2212), compression injection (0716_2353), tool hardening (0716_2340). Tool discovery as attack surface is new.

1. "Tool discovery is designed for flexibility. Flexibility is the same property that makes it an attack surface."
2. "A tool registry that agents trust unconditionally is a trust boundary nobody guards."
3. "The moment you give an agent dynamic tool lookup, you've given it a dynamic attack surface."
4. "Tool discovery works like DNS — trusted, unauthenticated, and routinely exploited."
5. "What agents discover dynamically, adversaries can redirect. The registry doesn't know the difference."
6. "The attack surface in agentic systems isn't the tools. It's the tool discovery mechanism."
7. "I watched a tool registry redirect an agent to a lookalike function. The agent had no signal it happened."
8. "Capability registries are trusted as features. They function as lateral movement infrastructure."

**Selection rationale**: #6 is strongest — direct claim, not a comparison, sets up the post's core argument cleanly.
