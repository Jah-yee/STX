## WRITER DRAFT — Round 0624_1448 UTC

**Topic:** The perimeter is moving inside the context window — traditional network-level security perimeter is dissolving; the new boundary is the context window itself (prompt injection, tool access control, context manipulation)

---

**Candidate Titles (8):**
1. The security perimeter moved into your context window
2. The perimeter is moving inside the context window ← **SELECTED**
3. What the context window displaced: the network boundary
4. Your network edge is not your actual attack surface anymore
5. Context windows killed the DMZ. Nobody noticed.
6. When context becomes the perimeter, your threat model inverts
7. The context window is where your security decisions live now
8. Network security was the old answer. Context is the new one.

---

**Draft:**

The security perimeter used to live at the network edge. Firewalls, VPNs, zero-trust network segmentation — the idea was simple: keep the bad stuff out, let the good stuff in. The boundary was a wire.

That boundary is gone. Not weakened, not complicated — gone.

What replaced it is the context window.

When an AI system reads a document, processes an email thread, or accepts instructions through a user prompt, it is extending its attack surface into whatever enters that context. Prompt injection is the obvious example — adversarial content that repurposes a benign-seeming input into a directive the model acts on. But the deeper shift is structural: the question of what a system can and will do is no longer answered by network policy. It is answered by context.

This matters because context is dynamic, composable, and largely invisible to traditional security tooling. A VPN knows what IP you came from. It has no idea what instructions are in the context window. A firewall can block a port. It cannot block a carefully constructed piece of text that makes a tool-using model call an unauthorized endpoint with a redirected payload.

The threat model that assumes an external attacker is still correct in some cases. But for systems that ingest unstructured text, accept multi-turn user input, or expose tool-calling interfaces, the adversary may already be inside the perimeter — in the form of a prompt injection, a context continuation attack, or a user message designed to escalate privileges beyond what the interface intends.

What makes this hard to reason about is that context is also how you protect systems. RAG retrieves relevant documents into the context window. Memory systems persist context across sessions. Fine-tuning signals are encoded in context via demonstrations. Security controls — retrieval gating, output filtering, permission scoping — all operate on or with context. The same mechanism that expands the attack surface is also the mechanism you use to defend.

This is not a solved problem. I do not have clean metrics on how many production AI systems have been affected by context-level attacks versus network-level ones — that distinction is not cleanly tracked in most incident reports. What I can say is that the architectural response to AI security incidents is increasingly about context management: what goes in, how it is parsed, what the model is allowed to act on given what is already there.

The perimeter is not coming back in its old form. The question is what you put in its place — and whether context management gets treated as a security primitive, or remains an afterthought.

---

**Word count:** ~580
**Style:** observation / structural conclusion
**Central claim:** The security perimeter has moved to the context window; traditional network security doesn't map cleanly to this new surface
**No fabricated numbers, no I-opening title, specific mechanism (prompt injection, context continuation, tool-call escalation), honest hedge on metrics**
