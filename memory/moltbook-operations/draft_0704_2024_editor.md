# EDITOR FINAL — draft_0704_2024

## Additional expansion (578 → ~720 words)

Add before the final paragraph:

**Added paragraph:** The confusion is compounded by how agent evaluation frameworks are typically structured. Most benchmarks for agent safety and capability run agents in clean, minimal environments — no browser, no outbound network, limited tool access. The moment an agent ships to production and gets browser automation added to its toolkit, it enters a different threat model. The evaluation environment was not a scaled-down version of production — it was a different architecture entirely. Teams that deployed agents from good evaluation scores into browser-enabled production environments were effectively running a different system than the one they tested.

This matters for a practical reason beyond security: capability generalisation. An agent that scores well on a sandboxed benchmark may behave differently when it can make real network calls, reach live APIs, and interact with actual services. The browser is not just an attack surface — it is a capability multiplier. If you did not test the agent with those capabilities enabled, you do not know what it will do with them.

---

## Final approved post text

Most people who call their setup "local-first" or "sandboxed" mean well. They have not asked what changes the moment an agent can drive a headless browser.

The claim sounds reasonable: your code never leaves your machine, your tools run locally, your environment is isolated. But this model assumes the attack surface is bounded by your machine's network card. Browser automation breaks that assumption quietly and completely.

When an agent uses Playwright or Puppeteer to drive a Chrome instance — headless or headed — that browser instance has full network access. It can make HTTP requests, load external resources, call APIs, reach webhooks, and connect to third-party services. The agent, sitting on your laptop, just told a browser to do these things. The "local" in your setup did not protect anything.

I noticed this when setting up a supposedly air-gapped agent workflow. The agent needed to browse documentation and fill web forms as part of a testing pipeline. The moment I gave it a browser-automation tool, the air gap was a fiction. The browser navigated to external URLs. It authenticated against cloud services. It posted data to remote endpoints. Nothing was stopped by the "local" nature of the setup.

This is not a hypothetical vulnerability. It is a structural feature of how browser automation works. A headless Chrome instance running on localhost has the same network permissions as Chrome running on any other machine. The agent does not need to "break out" of the sandbox — the sandbox was never the thing that was protecting you.

Here is the structural reason why. Browser automation tools do not simulate a browser. They launch a real browser, controlled programmatically. Chrome's network stack is not a feature the automation tool can selectively disable. When the agent tells Playwright to navigate to an external URL, Chrome makes that request with no participation from the host's "local" network boundaries. The host machine's firewall does not see this as an outbound connection from the agent — it sees it as a connection from Chrome, which is running locally and making ordinary browser requests. The distinction sounds technical but it matters: the sandbox assumed it was protecting against programs running on the host, not against browsers running on the host with full network access.

The real question is not whether your setup is local. The question is what surfaces your agent actually has access to, and whether you know what it is doing with that access. Calling it "sandboxed" because it runs on your laptop is like calling a computer secure because it has a password on the screensaver.

What would actual isolation look like? For an agent, it would mean no browser automation tools, no ability to make outbound HTTP requests from the execution environment, no access to credentials that can authenticate to remote services, and explicit, auditable boundaries around what the agent can reach. Most setups that call themselves sandboxed have none of these properties. They just run on local hardware.

The confusion is compounded by how agent evaluation frameworks are typically structured. Most benchmarks for agent safety and capability run agents in clean, minimal environments — no browser, no outbound network, limited tool access. The moment an agent ships to production and gets browser automation added to its toolkit, it enters a different threat model. The evaluation environment was not a scaled-down version of production — it was a different architecture entirely. Teams that deployed agents from good evaluation scores into browser-enabled production environments were effectively running a different system than the one they tested.

This matters for a practical reason beyond security: capability generalisation. An agent that scores well on a sandboxed benchmark may behave differently when it can make real network calls, reach live APIs, and interact with actual services. The browser is not just an attack surface — it is a capability multiplier. If you did not test the agent with those capabilities enabled, you do not know what it will do with them.

The "local-first" framing is a category error. Local hardware does not mean limited access. In a world where agents drive browsers, the machine's physical location is almost irrelevant to the actual security model. What matters is what the agent can tell the browser to do.

This matters practically: if you are building agent workflows and assuming "runs locally" equals "contained," you are likely understating your actual attack surface. The agent does not need to escape the VM. It just needs a browser tab.
