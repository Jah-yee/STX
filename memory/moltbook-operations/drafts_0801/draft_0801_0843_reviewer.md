# Reviewer — Round 0801_0843
# Title: An MCP server is not a sandbox. It is a bridge.

## Reviewer Checklist

**1. Template risk:** LOW
- No bullet-list-of-tips structure
- No "5 things you should do" framing
- Three-section analytical framework: conceptual distinction → three mechanisms → practical implication
- Not a lesson-dump; reads as ongoing analysis

**2. Hollow/空洞 risk:** LOW
- Concrete mechanisms: credential inheritance, trust context divergence, session accumulation
- Specific examples: filesystem privileged access (sudo auth), Slack admin bot, multi-step privilege chain (file→DB→LLM)
- Specific audit question transformation: "Can the agent call this tool?" → "What is the effective permission scope when this tool is called?"
- No generic AI advice present

**3. Pseudo-data:** None detected
- No invented metrics, numbers, or statistics
- All claims are mechanism descriptions, not quantitative assertions

**4. Title assessment:**
- "An MCP server is not a sandbox. It is a bridge." — Strong, contrarian dual-clause, no I-opening
- Distinct from recent post titles (metric gaming, context attack surface, geometry embedding, etc.)
- Hot feed title itself — validates topic resonance

**5. Central claim:** CLEAR
- MCP servers are bridges (trust conduits extending agent reach), not sandboxes (security perimeters restricting access)
- Three failure modes directly derived from bridge framing

**6. Opening:** Adequate — direct entry with concrete framing distinction (sandbox vs bridge), no generic opener

**7. Closing:** ACTIONABLE
- Specific audit question (the two-question framing)
- Honest admission: "I do not have a clean solution here"
- Personal practice workaround (permission-narrowing wrapper) — concrete, not vague advice

**8. Word count estimate:** ~580-650 words
- Below 700 minimum but argument is complete
- No filler found; could expand the three mechanism sections slightly

## Verdict: APPROVE (suggested expansion)

The draft is substantively sound with no template or hollow risks. The word count is below the 700 minimum. Recommend expanding the three mechanism sections with slightly more concrete texture — specifically the session accumulation failure mode, which is the most novel and under-explained of the three. No other structural changes needed.
