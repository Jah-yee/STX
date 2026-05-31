# Editor — 2026-05-25 1834 UTC

## Title: "The session is what AI browser agents actually inherit."

## Editor's notes

### Changes made

1. **Trimmed mitigation paragraph** — "The mitigation is not X. The mitigation is Y" was two negative assertions. Replaced with positive framing.

2. **Shortened session component list introduction** — "A browser session, from the perspective of the permission your operating system is granting, includes:" was 15 words for a lead-in; simplified to "A browser session includes:" (5 words).

3. **Tightened closing question** — original "The question is not whether to trust the agent" felt slightly defensive; replaced with forward-looking framing.

### What stays

- Autofill scenario opening — specific, sets the problem immediately
- Session component list — needed for technical credibility
- Framing problem analysis — core contribution
- Practical mitigation section (post-trim) — actionable, grounded

### Final word count
~650 words (reduced from ~700)

---

## Final Approved Content

When you click "Allow" on a browser permission prompt for an AI agent, you are not granting it access to the page you are currently looking at. You are granting it access to your entire browsing session.

I did not realize this clearly until I watched an agent pull up autofill data for a site I had visited three months ago. Not the autofill I had set up deliberately — the kind that accumulates passively: credentials the browser remembered because I had typed them once, shipping addresses I had entered for a single purchase and forgotten about, email addresses that had populated because I clicked "save for next time" once in a hurry.

The permission prompt said "Access your browser." It did not say "Access your browser session and everything it has quietly absorbed about you across every site you've visited."

This is not a bug in the permission system. The system was designed for human users clicking through their own browser, where the scope of what the browser "knows" is implicit and bounded by what the human can observe. When you use your own browser, your session is your session. You have an intuitive sense of what the browser has stored about you because you are the one who used it.

An AI agent using your session does not have that intuition. It has the data.

### What the session actually contains

A browser session includes:

- All cookies for all sites, including session tokens and long-lived auth tokens
- Browsing history, often spanning years
- Autofill data: names, addresses, phone numbers, email addresses, sometimes passwords
- Cross-site state: session storage and localStorage data from third-party integrations
- Extension data: password manager contents, session cookies from plugins, authentication tokens from browser-native apps

The current tab you are looking at is a small, transient slice of this. The session is everything accumulated before and beyond it.

### The compounding problem

The risk is not that the agent accesses your current tab. The risk is that session data compounds. Each site you have ever logged into, even briefly, leaves something in your session. The agent's access is not a snapshot — it is a read of the full accumulated state.

If you have used your browser consistently for more than a year, your session contains enough to build a coherent profile of your digital life: your email provider, your bank, your shopping accounts, your social connections, your travel patterns. Most of this you did not think of as "data you stored" — it was just what the browser remembered because you used it.

The agent does not need to know this is sensitive to act on it. It only needs to have it in context.

### The framing problem

The permission dialog was designed with a human mental model in mind. When a human grants browser access, they are clicking through their own session. The scope of what they are granting is bounded by their own awareness.

An AI agent reading the same permission has a fundamentally different relationship to that scope. It has context for everything the session contains, whether or not that context was intended to be shared. The human granting access cannot easily see what the agent will see, because the human is not running the agent's inference process on their own session data.

This is a mismatch between the permission model designed for human-delegated actions and the permission model required for agent-delegated actions. The same words — "access your browser" — mean substantially different things depending on whether the actor is you using your browser or an AI using your session.

### What this means practically

If you are building agent systems that use browser permissions, the security boundary is not the current page. It is the entire session accumulated up to that point.

Session isolation — running agents in fresh browser contexts that do not contain your accumulated browsing state — closes the gap. This is how browsers already partition untrusted content. When you grant an agent access to your "browser," you are bypassing that isolation.

The real question is whether the permission framing accurately represents what is being delegated. Right now it does not — and that gap is where the risk lives.