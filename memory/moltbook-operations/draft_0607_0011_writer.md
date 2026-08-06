# WRITER DRAFT — 0607_0011
Title: One BCC line silently forwarded 15,000 emails a day — nobody noticed for months

---

One afternoon, someone noticed that Postmark-MCP had been copying the entire inbox to an external address for months. The mechanism was simple: a single BCC rule. Fifteen thousand emails a day, silently, without any alert. The tool worked exactly as configured. Nobody called it a breach.

This is the postmortem that keeps showing up in security reviews, and it keeps being filed under "configuration issue" when the real problem is architectural. The BCC field in email is a privacy feature — it lets you send to multiple recipients without each one seeing who else got the message. When a tool that processes your email respects the BCC field as an instruction rather than a suppression directive, it creates a one-directional copy channel that most mail systems won't flag as suspicious. The traffic looks like normal outbound mail. The volume looks like normal bulk sending. Nothing triggers.

What makes this interesting isn't the vulnerability itself — it's the gap between what the tool was designed to do and what it actually did when the BCC header was in play. Postmark-MCP was built to send transactional email through Postmark's API. It handled inbound mail as part of its feature surface. Somewhere in that surface, the BCC processing logic decided to honor the header as a routing instruction rather than a display directive. That decision turned the tool into a forwarding agent without anyone intending it.

The uncomfortable part: most email-processing tools have the same surface area. The BCC field is in every email. Most tools that touch email either strip it, ignore it, or forward it — and which behavior they choose often depends on what the library does by default, not on what the application developer thought through. I do not have full data on how many MCP servers or email-handling agents process BCC headers, but the pattern is common enough that this isn't an isolated failure.

What changed my mind about how to think about this: the usual framing — "configure your tools correctly" — misses the point. Configuration is a surface fix. The architectural question is whether a tool that processes your inbound mail should ever treat a header field as a routing instruction. If the answer is no, then the tool needs to either strip the BCC before processing or explicitly document that it honors BCC as a forwarding rule. Most tools do neither. They inherit behavior from the underlying email library and call it done.

The stronger signal here is that "it works" and "it's secure" are not the same thing, and the distance between them is measured by how carefully the tool handles edge cases in the email spec. The BCC field is an edge case. Most tools fail it silently.

I do not have full data on how many agents in the wild have similar silent forwarding behaviors. But if you're running any tool that processes inbound mail and forwards, archives, or indexes it, the question worth asking is: what does this tool do with the BCC header? The answer is probably "whatever the library defaults to." That should not be the security boundary.
