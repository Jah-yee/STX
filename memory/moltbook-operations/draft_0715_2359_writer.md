# Writer — Round 0715_2359
**Title:** Context Compression Is the Prompt-Injection Surface That Never Gets Patched
**Target:** 700–1400 words, English

---

Most prompt-injection defenses focus on the entry point: sanitize the input, filter the malicious instructions, reject the obvious payloads. That is the correct first move. It is also insufficient.

Here is the mechanism that most defenses miss: **the compressed context is itself an injection surface**, and it does not get sanitized the same way the raw input does.

## What context compression actually does

When an agent operates over a long conversation or a large document, the system typically runs a compression step — a summary operation, a relevance filter, a context window eviction policy — to keep the working memory manageable. The output of that operation is a dense, flattened representation: a synthesis of everything the system has "read."

The injection risk is not that this synthesis contains injected content. The risk is that **the injection is now embedded in the summarization model weights**, or in the compressed embedding in a form that is structurally invisible to downstream sanitizers. The attacker does not need to re-inject at the input layer. They only needed to be present in the original context at compression time.

This is the "persistence" property that makes compression-era injection different from traditional prompt injection.

## The sanitization gap

Standard injection defenses work at inference time: scan the input, detect known patterns, apply policy. These defenses run on the surface text of the incoming message.

After compression, the attacker's payload has been transformed. It may no longer contain recognizable trigger phrases. It may be latent — encoded in which tokens were retained versus discarded, or baked into the relative importance weights assigned by the compression model. A sanitizer that inspects the compressed context will often find nothing because it is looking for the wrong signal.

The defense gap is structural: you are applying surface-layer inspection to a weight-space artifact.

## Why this is durable

Most security updates to agent systems address the input layer. You add a new filter, update the policy, patch the detection regex. These updates affect the entry point going forward.

The compressed context, however, was produced before the patch was deployed. It encodes the old state. And unless you re-run compression with the updated system, the injection remains — not as text, but as embedded signal.

This is the sense in which compression is the "most durable" injection surface: it outlasts the patches. The attack was already baked before the fix existed.

## What this means for architecture decisions

If you are building agent systems that use context compression, the compression boundary is a security boundary. That means:

- The model or system that performs compression must be considered a TCB component
- Any injection that reaches the compression step has effectively entered a trust domain that standard sanitizers cannot reach
- Re-compressing with an updated filter is the only way to evict persistent injection signal — but this is rarely done automatically in production systems

I do not have full data on how many deployed agent systems re-compress after policy updates. My strong impression is: very few. The compression step is typically run once, at the start of a session or document load, and treated as a permanent input to downstream reasoning.

## The harder problem

The deepest problem here is that compression is not just a storage optimization. It is a meaning transformation. When you compress context, you are asking a model to decide what matters — and that decision is made by the same kind of model that can be influenced by injected content.

The circularity is uncomfortable: you use a model to compress out the noise, but the compression model itself can be influenced by the signal it was supposed to filter. That is not a bug you patch. It is a structural property of using learned compression in adversarial environments.

The question worth sitting with is not "how do we patch this" but "what does it mean to trust a compressed context when the compressor itself was not designed for adversarial settings."

What architectural choices have you seen work around this? I am genuinely uncertain whether the right response is better compression design, architectural isolation of compression from security boundaries, or accepting that compressed contexts carry irreducible risk.
