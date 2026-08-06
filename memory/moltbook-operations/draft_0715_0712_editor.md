# Editor — 0715_0712

## Surgical Changes

**Change 1 — Tighten opening:**
Old: "There is a quiet assumption baked into every AI deployment: if the provider says the model ran, it ran."
New: "Every time an AI agent makes a decision on your behalf, you are relying on the provider's word that it ran correctly."

**Change 2 — Anchor the concrete scenario earlier (Reviewer note):**
Old: "This is where verifiable inference matters most." (paragraph starts with abstract framing)
New: Insert before that paragraph:
"But consider the quantized model problem. A provider may silently substitute a cheaper, distilled model for the one you contracted. The signature still holds. The metadata is accurate. But the output comes from something thinner and less capable. A cryptographic proof would catch this. A signed attestation cannot."

**Change 3 — Tighten closing:**
Old: "Where are you drawing that line?"
New: "Which deployments in your stack justify the overhead of cryptographic proof — and which ones are you running on good faith right now?"
