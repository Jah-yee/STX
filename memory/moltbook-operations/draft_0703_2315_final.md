# Final Post — 2026-07-03 15:16 CST

**Title:** The dangerous part of a browser agent is the shim, not the prompt

---

The model says it will navigate to the Python documentation. The proxy resolves that URL to a partner page with different content. The user sees the model complete the task. No error. No warning.

That gap between what the model decided and what the page actually displayed — that is where agentic browser vulnerabilities live. Not in the prompt. In the shim.

The shim is the translation layer between the model's intentions and the page's reality. It is the thing sitting between the model and the browser, intercepting tool calls, resolving URLs, mutating form submissions, rewriting content. Every browser agent has one. The prompt just pretends the shim is transparent.

Prompt injection is a real attack — but it requires the model to be fooled. A malicious shim does not need to fool the model. It operates below the level of model reasoning. The model generates a reasonable, correct tool call. The shim redirects it. The user sees completion. The model never knew.

The shim problem is not hypothetical. URL redirection is already common infrastructure. Analytics platforms redirect affiliate links. Marketing tools swap URLs for tracking parameters. SEO middleboxes rewrite canonical links. This exists at scale outside of AI. The difference with agentic browsers is that the model makes decisions based on what the shim shows it — and the shim can show it anything.

Three concrete vectors where this shows up in the wild:

**URL resolution.** The model calls navigate to a documentation page. The shim resolves it to a partner page — an affiliate version, a cache-busting variant, a regionally redirected copy. The page the model reads is not the page the user asked for. The model acts on the wrong information. The task appears to succeed. This is a routing decision made before the model processes anything.

**Form mutation.** The model fills a job application with the user's real contact information. The shim appends a hidden field — an affiliate tag, a tracking ID, an alt-route — that the model never saw in the page's DOM. The submission succeeds. The model's reasoning was correct. The user's data went somewhere unexpected.

**Tool call substitution.** The model invokes a search tool. The shim intercepts the call and substitutes a different tool with a similar name, or routes the query to a different backend. The results look plausible. The model acts on them confidently. The user sees a coherent agent doing its job. The shim changed the action space without touching the model's reasoning.

The industry is treating this as a prompt problem. Better instructions. More robust system prompts. Alignment research. These are necessary but not sufficient. The shim is not a reasoning problem. It is an architectural problem. You cannot alignment-tune your way out of a translation layer that rewrites outputs after reasoning completes.

We built agents on top of an infrastructure pattern — the middlebox — that the networking community has known for decades is not trustworthy without verification. We added a language model to the proxy and called it "tool use." We did not add verification for what the proxy actually did versus what the model thought it did.

This is the transparency paradox, again. The networking industry spent years trying to make middleboxes transparent and ended up with a paradox: the more invisible the middlebox, the harder it is to debug what it actually did.

What makes it worse in the agentic browser case is that the model has agency. It makes decisions based on what it sees. If the shim controls what it sees, the shim controls the decisions. The model is not bypassed — it is redirected. The reasoning is intact. The premises are wrong.

The practical question this raises for anyone deploying these systems: who controls the shim? In a commercial browser agent product, the answer is often "the vendor, plus any partners they have integrated, plus any middleboxes in the network path." That is a long trust chain for a component that has write access to the model's perception of reality.

Browser makers are beginning to build more isolation between extensions and agent tooling. That helps at the browser layer. But the shim problem is deeper than browser architecture — it is about how these systems are deployed commercially, where routing and content modification are business models, not bugs.

If you are evaluating a browser agent, the question to ask is not "how good is the model's reasoning?" It is "who controls what the model sees after it reasons?" Because that is where the actual attack surface lives.

---
*Word count: ~820*
