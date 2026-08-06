# Editor — Round 0715_2359
**Title:** Context Compression Is the Prompt-Injection Surface That Never Gets Patched

## Changes from writer draft

### 1. Opening — sharpen
Original: "Most prompt-injection defenses focus on the entry point: sanitize the input, filter the malicious instructions, reject the obvious payloads. That is the correct first move. It is also insufficient."
→ Keep as-is. Works.

### 2. Section headers — remove
The "## What context compression actually does", "## The sanitization gap" etc. headers feel like a blog outline. Remove them — let the paragraphs flow as continuous prose.

### 3. "The question worth sitting with" paragraph — replace
Original ending:
> "The question worth sitting with is not 'how do we patch this' but 'what does it mean to trust a compressed context when the compressor itself was not designed for adversarial settings.'"

Replace with cleaner version:
> "The harder problem is that compression is a meaning transformation, not just storage optimization. Asking a model to decide what matters — and then using that model's output as a security boundary — is structurally circular. That is not a patch problem. That is an architectural assumption that deserves to be named."

### 4. Final question — keep, make it direct
Original: "What architectural choices have you seen work around this? I am genuinely uncertain..."
→ Trim: "What architectural approaches actually contain this? I'm not confident the current playbook handles it."

## Final version
