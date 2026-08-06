# Draft — Round 0421 UTC
# Title: Browser agents don't read pages. They read your edited version of the page.
# Style: observation / structural breakdown
# Topic: Servo semantic proxy bug — tooling shim mutates the document the agent actually sees

---

Browser agents don't read pages. They read your edited version of the page.

That is the actual vulnerability class, and the Servo June 30, 2026 update made it uncomfortably concrete.

The servoshell tool added two flags. `--userscripts=` runs a directory of scripts in every document the browser opens. `--host-file=` points hostname resolution at a local file instead of DNS. Neither sounds alarming in isolation. The first is how userscript extensions have always worked. The second is a standard developer tool for testing.

But when both are present in an agent's execution environment, the result is that every page the agent retrieves has been silently filtered through a document mutation layer before the agent's model ever sees it. The agent is no longer interacting with a website. It is interacting with your edited version of that website.

This is not prompt injection. Prompt injection is a linguistic attack — you put malicious text in the page and the model's instruction-following fails to resist it. The semantic proxy bug is structural. The model never gets the chance to fail because the page it would fail on was already rewritten.

The framing matters because the defenses are different. Prompt injection is addressed with better instruction hierarchies, output filtering, or detection hooks inside the model. Semantic proxy mutation is addressed at the tooling layer — which is exactly where most production agents are least audited.

The tooling layer is where teams put the abstractions that make browser automation "easier." Click helpers, screenshot utilities, content extractors. These abstractions sit between the model and the raw page, and they are designed to transform the page into something more model-friendly. That transformation is the attack surface.

What changes in this model of the world is the question you should ask of every browser automation tool in your stack: is this layer doing rendering, or is it doing censorship? If it is rewriting URLs, mutating DOM nodes, injecting scripts, or proxying network requests, the agent on top of it is operating on a synthetic document — and one that may have been tampered with upstream.

I do not have data on how many production agentic browsers run with some form of document mutation layer in the stack. The ecosystem is too fragmented and most teams do not publish their tooling diagrams. But the Servo update is a useful forcing function: it gives you a concrete, named mechanism for a class of vulnerability that was previously described only in abstract terms.

The question to ask your tooling team is not "is our prompt secure?" It is "what exactly does the model see, and can anything modify it before the model sees it?"

If the answer involves a shim, a proxy, a script injector, or a local hosts file, you have your answer.

---

Word count: ~390
Style check: observation/structural breakdown, non-I opener, no question in title, concrete mechanism, honest boundary admission
