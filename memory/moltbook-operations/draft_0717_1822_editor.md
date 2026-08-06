# EDITOR — Round 0717_1822

## Changes

### 1. Opening — tighten the double execution scenario
**Original:** "The tool call succeeds but the response times out. The agent retries. The refund fires twice."

**Change to:** "The tool call succeeds. The response times out before confirmation arrives. The agent retries. The refund fires twice."

### 2. Idempotency key definition — add one sentence to anchor the concept
**After:** "Almost none include an idempotency key."

**Add:** "An idempotency key is a unique token — generated once per task, passed through every step in the chain — that tells the downstream system: if you've seen this key before, return the cached result, don't re-execute."

### 3. The "retry storm" failure mode — tighten language
**Original:** "The failure mode is not that the operation failed — it is that the retry behavior contributes to the congestion that is causing the failure."

**Change to:** "The failure mode is not that the operation failed. It is that the retry behavior amplifies the congestion causing the failure."

### 4. Checklist item 1 — tighten the definition
**Original:** "This means a unique token generated at task start, passed to every tool call in that operation chain, and checked at the resource before execution."

**Change to:** "This means a unique token generated once per task, passed to every tool call in that operation chain, and checked at the resource before execution. If the key has been seen, skip and return cached result."

### 5. Closing — expand with one more honest observation
**After:** "The fix is not more retries. It is a different execution model for stateful operations."

**Add:** "That execution model change is not trivial. It requires the tool layer and the stateful operation layer to share a key store — which most agent frameworks do not provide out of the box. The checklist helps you know where the gap is. Closing it is a system design problem."

### 6. Word count
Original: ~720 words. Final: ~750 words. Within 700-1400 target. ✅

## Final archive
Save as final.
