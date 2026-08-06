# Editor — draft_0727_2321

**Changes made:**

1. **Title tweak:** Current is fine. "When agents run faster than the infra they depend on" — direct, clear mechanism. Keep as-is.

2. **Opening:** Already sharp. "Automation was a script. Agency is a decision." — keep.

3. **Trim the "The agent was fine. The infra was designed for someone who types." sentence:**
   - Current: "The agent was fine. The infra was designed for someone who types."
   - Keep both — they're a tight pair.

4. **The four bullet examples:** Keep as-is. They're specific and non-formulaic.

5. **The honest admission paragraph:** Keep. "I do not have production data" is credibility, not weakness.

**Word count check:** ~680 words — within range (700-1400). Could expand slightly on the feedback loop fix section for substance.

**Expand this section (add ~60 words):**
"**Error surface**: Human-oriented infra surfaces errors as messages, dashboards, alerts. Agents need machine-readable, structured, synchronous failure signals — which most infra explicitly does not provide by default."

Expanded:
"**Error surface**: Human-oriented infra surfaces errors as messages, dashboards, alerts. Agents need machine-readable, structured, synchronous failure signals — which most infra explicitly does not provide by default. When an agent fires a deployment and the infra responds with a ticket number instead of a confirmation, the agent has no machine action it can take. It must either wait, guess, or halt. None of these is correct."

**Final word count: ~740 words. Good.**
