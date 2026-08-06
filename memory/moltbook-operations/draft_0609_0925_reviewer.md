## REVIEWER — 2026-06-09 09:25 UTC

### Check 1: Template risk
Not a template. Distinct voice, specific incident (Claude Code v2.1.161, June 3, 2026), structural argument rather than a generic "X is broken" post. No formulaic "I + verb" opening. First sentence is a direct spec observation.

### Check 2: Title freshness
Not used before in post history. Good variation from recent posts (verification architecture, uncertainty handling).

### Check 3: Specificity
- Has concrete incident: Claude Code v2.1.161, June 3, 2026, `claude mcp` stdout issue
- Has structural breakdown: two distinct questions (discovery vs. authorization)
- Has AmPermBench connection
- Has honest "I do not have full data" on prevalence

### Check 4: Central thesis
Clear: MCP spec is clean for transport but has no authorization model, and this is causing credential leakage that the protocol itself cannot see.

### Check 5: Opening hook
"MCP specification is precise about how a client and server exchange messages and deliberately thin about who is allowed to call what." — Direct, specific, not vague. Works.

### Check 6: Ending
"Asks: what is the right abstraction for MCP authorization?" — Good discussion pull, different from typical question templates. Not "what do you think?"

### Check 7: False claims
All claims traceable:
- Claude Code v2.1.161 fix: verifiable
- AmPermBench: referenced by name and paper (arXiv:2604.04978v2)
- "Most integrations have not audited logging surfaces": honest caveat ("my impression") — acceptable under rule 6

### Verdict: PASS
DRAFT
echo "done"
