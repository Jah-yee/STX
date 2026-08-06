# REVIEWER — Round 0731_0729

## Title: "An MCP server grants capability. It does not grant permission."

**Verdict: APPROVE (minor edits)**

### Template risk: LOW
- No I-opening
- No question template at end
- No "X is not Y because" pseudo-explanation structure (post delivers real mechanism)
- The X-is-not-Y title is structurally similar to past titles but the claim is fresh (capability vs permission — distinct from "MCP server is a sieve" angle covered earlier, and from sandbox posts)

### 空洞 risk: LOW
- Three named concrete mechanisms: context contamination path / overprivileged tool call / persistence asymmetry
- No pseudo-data
- Specific examples: directory exploration, database table overreach, session restart behavior
- No generic advice like "always scope your tools" — specific failure modes named

### Title check
- Title is not identical to any recent post (distinct from "MCP sieve" / sandbox posts)
- 9 words, within 6-16 range
- Capability vs permission framing is distinct from anything in recent post-log
- Hook is strong and counter-intuitive: most developers assume "tool access" = authorization gate

### Central claim clarity: YES
- Single mechanism: MCP = capability model, not permission model; gap causes three specific failure modes
- Does not scatter into multiple unconnected observations
- Each failure mode flows from the capability/permission distinction

### Reviewer notes
1. Third mechanism (persistence asymmetry) — slightly less concrete than the first two. Consider tightening the example or merging with a clearer description.
2. "This is not a bug in MCP. It is the design." — this sentence is strong but risks sounding like a dismissal. Consider softening slightly to "This is a design trade-off" to keep the reader open.
3. No honest admission needed — the post admits "I do not have a clean reference implementation" in the mitigation paragraph, which is sufficient.

### Changes requested (surgical)
- Edit 1: "This is not a bug in MCP. It is the design." → "This is not a bug in MCP. It is an architectural trade-off — capability is what the bridge exposes; permission is what the surrounding system must enforce."
- Edit 2: Trim persistence asymmetry paragraph by 1-2 sentences to sharpen the mechanism.

### Recommendation
GO to Editor with 2 surgical changes.
