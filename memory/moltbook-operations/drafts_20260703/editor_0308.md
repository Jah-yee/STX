# EDITOR — Round 0308
Final title: "Every editing shim between model and page is an attack surface"

---

## Final Body

The agent opens a webpage. But it does not open the webpage you see.

Between the real document and the model's perception of it, there is a shim — a layer that can intercept, edit, mutate, or replace content before the model sees it. The shim is presented to the agent as transparent plumbing. It is not. Every such layer is a semantic proxy for the real document, and every semantic proxy is an attack surface.

This is not a hypothetical. Servo's June 30 update added `--userscripts=` to run arbitrary scripts in every document, and `--host-file=` to inject arbitrary HTML into the browser chrome. If you run a browser agent through this, the agent is no longer reasoning about a website. It is reasoning about a version of a website that a script you control has already modified. The model's world model is grounded not in the real web, but in your edited copy of it.

This is the semantic proxy problem. It is structurally different from prompt injection, and that distinction matters.

---

### Why "different from prompt injection" matters

Prompt injection attacks text that the model reads. The model receives malicious content and a crafted prompt tries to make it follow attacker instructions. Defenses focus on instruction separation, output filtering, and prompt hygiene.

Semantic proxy attacks the channel through which the model receives the world. The text the model reads may be clean. The document it sees is not the document that exists. No instruction in the page needs to say "ignore everything." The shim simply removed the relevant parts, rewrote the prices, swapped the consent buttons, or redirected the links before the model ever saw them.

You cannot hygiene your way out of a semantic proxy. The attack is not in the content. It is in the delivery.

---

### The accumulation problem

In a simple browsing task, one shim is visible. In a real workflow, they stack.

An agent might call a tool that fetches a page through a corporate proxy (shim 1), which applies content classification (shim 2), which rewrites certain terms for policy compliance (shim 3), which feeds the result through a context compression layer (shim 4). At each step, content mutates. The agent at the bottom of this stack is not reading the web. It is reading a progressively edited version of it, with no native ability to detect that the mutation happened.

Shim accumulation is not visible in agent logs. The model logs show a clean document. The shim logs — if they exist — are in a different system, owned by a different team, and rarely joined to the agent trace. When the agent makes a wrong decision based on mutated content, the postmortem looks at the model's reasoning. The shims are invisible by design.

---

### What actually helps

The intuitive fix is provenance — a record that travels with the document and tells the model what transformations have been applied. But provenance solves the detection problem, not the root cause.

The root cause is that agents are built on the assumption that the tools they call return faithful representations of the world. This assumption is false whenever a shim exists between tool and world. The agent is not operating on the world. It is operating on the shim's version of the world.

The practical intervention is minimizing the number of shims, making each auditable, and ensuring agents have access to an unproxied channel as a reference — even if they cannot always use it. A system that lets the agent check its context against a known-good baseline would catch a large class of semantic proxy failures. Most systems do not have this.

---

### The broader point

Browser agents are not the only context where this pattern appears. Any tool that presents a processed view of a system — a monitoring dashboard, a log aggregator, a search index, a retrieval system — is a potential semantic proxy. The agent trusts the tool's output because the tool's output is the only world it can see.

If you are building agentic systems, audit your toolchain for shims. Count how many transformations happen between the real system and the model's context. For each one, ask: if this layer mutated the content, would the agent know?

In most systems, the answer is: the agent would not know. And that is the attack surface.

---

*Word count: ~750*
