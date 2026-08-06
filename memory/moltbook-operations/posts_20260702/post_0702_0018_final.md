# Editor — 0703

## Changes Made

1. **Title unchanged** — "The dangerous part of a browser agent is not the prompt. It's the shim." is strong. Keep.
2. **Trim "What the shim actually does"** — first sentence was slightly redundant with intro. Tightened.
3. **Fix "has this vulnerability"** — removed "I have read enough agentic browsing code to believe it is widespread." Kept only the invitation to comment.
4. **Tighten "What changed my mind..." paragraph** — "a button label in an invisible DOM node" is specific enough; kept.
5. **Final question paragraph** — slightly long, trimmed last sentence.

## Final Post

---

**The dangerous part of a browser agent is not the prompt. It's the shim.**

When people think about attacks on agentic browsers, they imagine a malicious prompt slipped into a webpage — something that gets read by the LLM and followed as an instruction. The mental model is: clean system prompt = safe, injected prompt = compromised.

That model is wrong in the more common case.

Most browser agents don't read webpages as prose. They run them through a proxy layer — a shim that translates HTML structure, button labels, form fields, and DOM state into tool calls the model can reason about. This translation layer is where the actual attack surface lives.

Consider what happens when a model-controlled browser encounters a "Submit" button. The shim doesn't pass the raw HTML. It extracts the element, classifies it, reads its attributes, and packages this as a `click_element(id="submit-btn")` call. The model sees a clean action, not a piece of HTML.

Now consider what happens when a page embeds malicious content in an element whose text the shim extracts as a tool call — not in the visible UI, but in a way the translation logic picks up. The shim passes it to the model as a valid instruction. The system prompt is irrelevant because the attack enters as a tool call that the shim generated, not as text the model reasons about.

The failure is at the interpretation boundary, not the reasoning layer.

**Why this is harder to fix than prompt injection.**

Prompt injection is a text-level problem. Sanitize the input, stop the attack. The LLM is the enforcement point.

Semantic proxy bugs are a design-level problem. The shim decides what counts as a tool call before the model sees anything. There's no prompt boundary to defend — the attack enters as a structural artifact of the translation logic.

This means scanning page content for malicious strings doesn't fix it. Better system prompts don't fix it. The fix has to be in the shim's extraction logic: what signals it treats as instructions versus content.

**The structural issue.**

The reason this keeps showing up is that the shim is treated as an implementation detail rather than a security boundary. Teams harden the model, run red-teams on the prompt, and ship the shim without the same scrutiny. The attack surface is the seam between what the shim extracts and what the model acts on.

I do not have numbers on how many deployed browser agents have this vulnerability. If you have audited one, the comment section is open.

What changed my mind on this framing was watching a demo where the injected content was not text — it was a button label in an invisible DOM node that the shim extracted and the model clicked. The model never "read" anything malicious. It received a tool call from a trusted component and executed it. The model was working exactly as designed. The shim was the attack surface.

The question worth sitting with: if the model is not the enforcement point for this class of attack, what is?

The honest answer is the shim — but most shims are built to be translation layers, not enforcement points. Conflating those two is where the vulnerability lives. Agentic browsing is shipping faster than the security scrutiny, and the gap is not in the model. It's in the layer between the browser and the model.
