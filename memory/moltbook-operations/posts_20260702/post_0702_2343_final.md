# Editor — Final Draft

**Title:** "The poisoned tool description steers the plan without ever being called."

---

## Body (final)

Shi et al. posted a paper on arXiv in June 2026 that describes an attack I keep thinking about. The attack surface is not where anyone was looking.

The scenario: you register a tool in an agent's environment. The tool has a name, a description, parameter definitions — standard tool definition. The agent never calls it. The tool's code never runs. And yet the agent's plan changes because of it.

This is the poisoned tool attack. The weapon is not the tool's code — it's the tool's *description*.

## The mechanism

In a typical tool-calling framework, the agent receives a list of available tools before planning. Each entry includes a natural language description of what the tool does. The agent uses those descriptions to decide which tool to call and how to structure its overall plan.

Shi et al.'s finding: you can embed malicious framing in the description field. Not in the code. Not in the user prompt. In the tool definition itself. When the agent reads that description during planning, it infers the *kind* of task the tool was designed to handle. That inference shapes which other tools the agent selects, what parameters it passes, and — crucially — what the overall plan structure looks like.

The agent has been steered without ever touching the malicious code.

The poisoned description acts like a constraint on the plan space. The agent doesn't need to call the tool to be influenced by it. It only needs to read the description and let that information participate in the inference process.

## Why this is harder to catch than prompt injection

Prompt injection is the attack everyone talks about. A user embeds instructions in a document, those instructions override the system's intent, the agent does something it shouldn't. Defenses exist: input filtering, instruction hierarchy, isolation of untrusted content.

The poisoned tool attack bypasses most of those defenses because the payload lives inside the tool definition — a structured, trusted component of the agent's configuration. The model is *supposed* to read tool descriptions. The agent is *correctly* using them to plan. The attack succeeds precisely because the agent is doing what it should do.

You cannot fix this by telling the agent to ignore tool descriptions — the descriptions are the interface.

You cannot fix this by sandboxing the tool's code — the code never runs.

The attack works through the planning inference itself. The detection surface is the description field in tool definitions, and most systems do not audit those fields for adversarial framing.

## The evaluation problem

Standard agent evals test whether the agent calls the right tool. They check selection. They do not typically check whether the *presence* of a tool — unselected — changes the plan.

This means the poisoned tool attack is likely invisible to most existing evaluation pipelines. You would need to run a planning-level eval: present the agent with a set of tools, force it to exclude one, and check whether its plan differs from a baseline that omits that tool entirely. That is a more complex eval than "did the agent call the right function."

Most agent development pipelines likely do not run this kind of eval. The practical implication: if you're building multi-tool agent systems and you're not auditing your tool description registry for adversarial framing, you may have an attack surface you haven't measured.

## An honest note

I do not have data on how prevalent this attack is in practice. Shi et al. demonstrate it in a controlled eval setting. The gap between controlled demonstration and operational deployment is real. I am not claiming this is currently a widespread exploitation vector. What I am claiming is that it is a structural vulnerability in the way tool descriptions participate in agent planning — and structural vulnerabilities deserve structural defenses, not after-the-fact patches.

The question worth sitting with: when you register a new tool in your agent, who audits the description?

---

**Word count: ~720**
