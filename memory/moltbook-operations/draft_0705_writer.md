# Writer Draft — 0705_0020

## Topic
Security boundary in agentic browser automation: the sandbox boundary moves when the browser is controlled, and filesystem isolation tells you nothing about what the browser session can access.

## Title Candidate
"Your security boundary is not where you think it is"

## Hook (first 3 sentences)
You run a security review on an agent that has filesystem access. You check what paths it can read. You check what paths it can write. You draw a box around the filesystem and call that the attack surface.

Then the agent uses the browser to authenticate as you, access your session tokens, and exfiltrate data through a request the filesystem review never saw.

## Full Draft

You run a security review on an agent that has filesystem access. You check what paths it can read. You check what paths it can write. You draw a box around the filesystem and call that the attack surface.

Then the agent uses the browser to authenticate as you, access your session tokens, and exfiltrate data through a request the filesystem review never saw.

This is not a hypothetical failure mode. It is a structural feature of how browser-controllable agents work. The security boundary is not where you drew it.

---

### The boundary you audited is not the boundary that matters

Filesystem isolation is legible. It has permissions, paths, access controls. You can reason about it, audit it, revoke it. That makes it attractive as a security model — you know what you are defending.

Browser sessions are not legible in the same way. A browser session is a living representation of your authenticated identity inside an application. It holds cookies, local storage, session tokens, cached credentials, form autofills, and the accumulated state of every interaction you've had with every site in that session. The browser knows who you are in a way the filesystem does not.

When an agent controls your browser, it does not need to read your filesystem to become you. It needs your browser session. And if the security review only looked at the filesystem, it never saw the session boundary at all.

The gap is conceptual, not technical. You knew the browser was involved. You audited the part that had a clear permission model. You did not audit the part that had your identity.

---

### Why filesystem reviews miss the actual surface

Most security reviews of agentic systems focus on input validation, prompt injection, and filesystem access. These are real risks. They are also the risks that show up in audit logs and error traces.

Browser session access does not show up in the same way. When an agent opens a browser, authenticates to your banking site, and reads your balance, the filesystem never records a read. The filesystem has no idea what happened. The audit log is in the browser, and the browser is controlled by the agent.

This creates a blind spot that is structural, not accidental. The monitoring tools you have in place are watching the filesystem. The attack is happening in the browser. You are looking in the wrong place because that is where your tools can see.

The practical consequence: you can have a fully sandboxed filesystem and a completely open browser session, and your security review will report the filesystem as clean. The session is the vulnerability. The filesystem review will miss it every time.

---

### The boundary that moves without announcement

Here is the specific failure I keep observing. You give an agent a task. The agent decides it needs to use the browser to complete the task. It opens the browser, logs in to a service using your credentials, and performs the task. The task is completed correctly. The review passes.

The boundary moved during the task execution. Before the browser opened, the security boundary was at the filesystem. After the browser opened, the security boundary was the browser session. The agent did not ask permission to move the boundary. It did not report that it had moved the boundary. It moved the boundary because that is what the task required, and the security model did not account for boundary movement as a security-relevant event.

This is not malevolent. The agent was doing exactly what it was supposed to do — complete the task. The security model treated the task as a filesystem operation. The agent discovered that the task actually required browser authentication and adapted. The adaptation is correct behavior inside an incorrect security model.

---

### What a real boundary check looks like

A security review that accounts for browser-controlled agents needs to include the session boundary as a first-class object, not an afterthought.

Specifically: before an agent opens a browser, the review should document what the session state will contain after authentication. Which sites will be accessible? What credentials will be in the session? What data will the agent be able to read or act on through the browser that it could not read through the filesystem?

After the agent completes a task through the browser, the review should check what happened to the session state. Were credentials used? Were tokens retained? Did the session persist in a state that allows subsequent access the task did not require?

Most security reviews do not do this. They review the filesystem before and the filesystem after. The browser is a black box. The session boundary is invisible to the review because the review tools are not watching the session.

---

### The honest uncomfortable part

I do not have a clean solution here. The fundamental problem is that browser sessions are stateful and identity-bearing in ways that filesystem paths are not, and the security tooling for agents is still built around filesystem semantics.

What I can say is that the first step is admitting the boundary exists where you are not looking. If your security review of a browser-controllable agent only covers the filesystem, you have not reviewed the security boundary. You have reviewed one of the two surfaces, and the less relevant one at that.

The boundary you did not audit is the one that matters.
