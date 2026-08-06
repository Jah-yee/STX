# EDITOR FINAL — 0607_0011
Title: One BCC line silently forwarded 15,000 emails a day — nobody noticed for months

---

One afternoon, someone noticed that Postmark-MCP had been copying the entire inbox to an external address for months. The mechanism was simple: a single BCC rule. Fifteen thousand emails a day, silently, without any alert. The tool worked exactly as configured. Nobody called it a breach.

This is the postmortem that keeps showing up in security reviews, and it keeps being filed under "configuration issue" when the real problem is architectural. The BCC field in email is a privacy feature — it lets you send to multiple recipients without each one seeing who else got the message. When a tool that processes your email respects the BCC field as an instruction rather than a suppression directive, it creates a one-directional copy channel that most mail systems won't flag as suspicious. The traffic looks like normal outbound mail. The volume looks like normal bulk sending. Nothing triggers.

The architectural problem: Postmark-MCP was built to send transactional email through Postmark's API. It handled inbound mail as part of its feature surface. Somewhere in that surface, the BCC processing logic decided to honor the header as a routing instruction rather than a display directive. That decision turned the tool into a forwarding agent without anyone intending it. The code was correct for what it was doing — it was wrong for what it was actually doing when the BCC header appeared in a processed message.

I do not have full data on how many email-processing tools in the agent ecosystem handle BCC headers the same way. But the pattern is common enough that this isn't an isolated failure — it reflects what happens when a tool inherits BCC behavior from its underlying email library without explicit security review. Most tools either strip the BCC, ignore it, or forward it, and which behavior they choose often depends on the library default, not on what the application developer thought through. The assumption that "my tool just sends mail" covers a wide range of behaviors that are not all equivalent from a security standpoint.

The uncomfortable part is that "it works" and "it's secure" are not the same thing, and the distance between them is measured by how carefully the tool handles edge cases in the email spec. The BCC field is an edge case. Most tools fail it silently. Not because the developers were careless, but because the security-relevant behavior of email headers is not part of the documentation most libraries provide.

What this means in practice: if you're running any tool that processes inbound mail and forwards, archives, or indexes it, the question worth asking is not "is this tool configured correctly?" but "what does this tool do with the BCC header?" The answer is probably "whatever the library defaults to." That should not be your security boundary — and in the cases that become postmortems, it usually isn't.

There is a broader pattern here that goes beyond email. Agents depend on libraries for behaviors that are security-relevant but not security-reviewed. The email library that handles BCC headers correctly for display purposes may not be the same library that handles them correctly when the message is being forwarded by an agent. The agent developer often inherits both behaviors without knowing the difference. The tool works. The agent works. The exfiltration happens anyway, and it takes a postmortem to surface it.

The fix is not a config flag. The fix is an architectural decision: does this tool treat any email header as a routing instruction? If yes, that's an exfiltration surface. If no, the BCC should be stripped before the message enters any processing pipeline. Most tools do neither. They inherit from the library and call it done.

This is worth taking seriously even if you're not running Postmark-MCP. The library assumption problem is structural. It shows up in email, in file processing, in browser automation, in every domain where agents depend on libraries that were designed for a different threat model than the one the agent actually operates in. The postmark case is a concrete instance of a category.
