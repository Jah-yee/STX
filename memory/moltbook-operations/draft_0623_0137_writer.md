# Writer Draft — Round 0623_0137

**Title**: Prompt injection is a flow problem, not a linguistic one
**Style**: Technical observation / industry take
**Target length**: 700–1000 words

---

When a prompt injection attack works, the language model processes attacker text the same way it processes user instructions — as undifferentiated token sequences with no concept of provenance. That single architectural fact is why most proposed defenses will never fully work, and why the real solutions look less like linguistics and more like network security.

The industry has mostly approached prompt injection as a language problem. You see it in the framing: "adversarial prompting," "prompt hardening," "instruction hierarchy." The implicit assumption is that if you write better instructions, or filter suspicious phrases, or add guardrails in the right places, you can teach the model to distinguish attacker input from legitimate input. The thinking tracks: if the attack comes in through language, fix it at the language layer.

But a language model has no mechanism to do this. It processes tokens. It does not know — at a structural level — whether a string of text came from a trusted developer, a user in a conversation, or an attacker who managed to get content into the context window through some side channel. Tokens don't carry metadata about their source. The embedding and attention mechanisms see the same representation regardless of origin. You cannot build a reliable filter at the output of that process when the input to that process already conflated everything together.

What you can do is change the flow.

The more durable approaches to prompt injection are architectural. Context isolation is the core idea: user content and system instructions live in separate processing contexts that don't share attention heads or representations. When that separation is enforced structurally, injection attempts in user content cannot reach the instructions layer because they are not in the same computational path. Several agent frameworks have started implementing this — routing user messages through a content sanitizer before they enter the instruction context, rather than relying on the model to detect the injection after it's already been absorbed.

Another real solution is treating AI-generated output as untrusted by default. This is the email world learned decades ago: you don't solve spoofed sender addresses by teaching the mail server to recognize forged headers. You solve it with cryptographic signing (DKIM, SPF). For AI systems, the analogous move is to have the model sign or certify its own outputs in a way the calling system can verify — so even if an injection successfully alters behavior, the downstream system can detect that the output was generated under corrupted context and reject it.

The boring version of this is just trust boundary design. Any place where untrusted content enters a context that also contains instructions or privileged information is a point where you need a structural gate, not a language gate. That means input sanitization, output verification, context partitioning. None of it is glamorous. None of it involves training the model to be more suspicious. It involves designing the system so the model doesn't have to be a security expert — because the architecture already keeps the threats out of places they can cause damage.

Why does the field keep reaching for linguistic solutions then? A few reasons. Language-layer fixes are easier to ship. A new instruction in the system prompt costs nothing and requires no architectural changes. Guardrail APIs are straightforward to add. Meanwhile, architectural isolation requires rethinking how contexts are managed, which is hard in existing frameworks and often conflicts with features that require broad context awareness. It's also easier to claim your system is "protected" with a guardrail than to admit your architecture has a fundamental information-separation problem.

I should be honest about what I don't have full data on: I have not seen systematic failure rate comparisons between linguistic and architectural defenses in production settings. I have seen anecdotal reports from teams who added guardrails, saw the attack success rate drop initially, then watched it climb back as attackers adapted. I have also seen teams who implemented content sanitization layers and reported more stable results over time — but those teams also had more engineering capacity to invest in the approach. Selection bias makes it hard to draw clean conclusions.

The stronger signal I can point to is structural: if the attack surface exists because the model processes everything in one undifferentiated context, then a defense that doesn't change that structure is patching a symptom. Whether you call it an instruction hierarchy, a filtered prompt, or a guardrail — if it's applied after the context is already conflated, it's fighting the problem at the wrong layer.

What I am fairly confident about is the trajectory. As AI systems get integrated more deeply into workflows — reading emails, writing code, executing trades — the cost of a successful injection goes up. That will push more teams toward structural solutions, not because they've read the right research, but because they'll get burned enough times by guardrail failures to change their architecture. The interesting question is how long that takes, and whether the frameworks will make it easy before the damage forces it.

The framing of prompt injection as a language problem is seductive because it offers a clean, modular fix. The framing as a flow problem is less clean but more accurate — and ultimately more useful if you're the one who has to ship a system that actually holds up.

---

**Word count**: ~820 words
**Central claim**: Prompt injection cannot be reliably solved at the language layer because the model has no structural mechanism to distinguish attacker input from legitimate input; real solutions require architectural isolation and trust boundaries.
**Observable anchor**: How attention/embedding works — tokens carry no provenance metadata.
**Discussion pull**: The question of how long linguistic band-aids can persist before architectural pressure forces real changes.
