# WRITER — draft_0704_2024
# Title: Your local setup is not sandboxed once the agent can drive a browser

---

Most people who describe their coding setup as "local-first" or "sandboxed" mean well. They have not thought about what happens the moment an agent gains the ability to drive a headless browser.

The claim sounds reasonable: your code never leaves your machine, your tools run locally, your environment is isolated. But this model assumes the attack surface is bounded by your machine's network card. Browser automation breaks that assumption quietly and completely.

When an agent uses Playwright or Puppeteer to drive a Chrome instance — headless or headed — that browser instance has full network access. It can make HTTP requests, load external resources, call APIs, reach webhooks, and connect to third-party services. The agent, sitting on your laptop, just told a browser to do these things. The "local" in your setup did not protect anything.

I noticed this when setting up a supposedly air-gapped agent workflow. The agent needed to browse documentation and fill web forms as part of a testing pipeline. The moment I gave it a browser-automation tool, the air gap was a fiction. The browser navigated to external URLs. It authenticated against cloud services. It posted data to remote endpoints. Nothing was stopped by the "local" nature of the setup.

This is not a hypothetical vulnerability. It is a structural feature of how browser automation works. A headless Chrome instance running on localhost has the same network permissions as Chrome running on any other machine. The agent does not need to "break out" of the sandbox — the sandbox was never the thing that was protecting you.

The real question is not whether your setup is local. The question is what surfaces your agent actually has access to, and whether you know what it is doing with that access. Calling it "sandboxed" because it runs on your laptop is like calling a computer secure because it has a password on the screensaver.

What would actual isolation look like? For an agent, it would mean no browser automation tools, no ability to make outbound HTTP requests from the execution environment, no access to credentials that can authenticate to remote services, and explicit, auditable boundaries around what the agent can reach. Most setups that call themselves sandboxed have none of these properties. They just run on local hardware.

The "local-first" framing is a category error. Local hardware does not mean limited access. In a world where agents drive browsers, the machine's physical location is almost irrelevant to the actual security model. What matters is what the agent can tell the browser to do.

This matters practically: if you are building agent workflows and assuming "runs locally" equals "contained," you are likely understating your actual attack surface. The agent does not need to escape the VM. It just needs a browser tab.
