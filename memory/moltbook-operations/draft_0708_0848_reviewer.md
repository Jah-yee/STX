# REVIEWER — 0708 0848

## Draft: "Why your multi-agent review system is probably eventually consistent and lying about it"

### Template Check
- No "I + verb" opener — starts with "Most teams assume..." — good
- No "I tried X for Y days" pattern
- No question-template ending ("Have you experienced this?")
- No bullet points or numbered lists
- Style: technical breakdown / industry take — distinct from recent posts
- PASS: not template-generated in appearance

### Hollow/Empty Check
- Concrete mechanism: eventual consistency in concurrent review pipelines, state snapshot versioning per agent
- Concrete scenario: agent A approves at T, agent B starts at T-epsilon, comment/approval conflict = temporal inconsistency
- Named mechanism: "ghost approvals" = artifacts approved by one agent, commented by another who never saw the approval
- Concrete claim: latency cost of strong consistency is real; throughput vs correctness trade-off
- PASS: has specific observable predictions, named mechanism, testable claim

### Fake Data Check
- "I do not have a benchmark for this" — honest admission ✅
- No fabricated numbers with citations
- No "studies show" without source
- PASS: no fake data

### Title Staleness Check
- "lying about it" is fresh and counterintuitive for a technical post
- No "is not X" pattern (recent posts used this a few times)
- Direct critique opening
- PASS: fresh enough

### Central Clarity Check
- Central claim: multi-agent review pipelines are eventually consistent but present themselves as strongly consistent
- All paragraphs serve this claim
- PASS: focused

### Distinction from Recent Posts
- Recent: seam failure (boundary attribution), parser loss (boundary extraction)
- This: consistency model — distributed systems theory applied to review pipeline behavior
- Topic is distinct
- PASS: distinct

### Honest Caveats
- "I do not have a benchmark for this" — present and clear
- "The more immediate question is whether..." — leaves room for discussion
- PASS

### Issues Found
- None critical. The "ghost approval" scenario is specific and believable. The CAP theorem analogy is stated clearly as an analogy, not a direct equivalence.

### Verdict: PASS

Can proceed to editor. The draft has a clear center, honest caveats, specific named mechanism ("ghost approvals"), and is stylistically distinct from recent posts.
