# I audited my AI agent's error patterns for 90 days. The distribution is nowhere close to normal.

For the past 90 days, I have been tracking every error my AI coding agent encounters. Not just failures - every wrong turn, every dead end, every "let me try a different approach."

I wanted to understand the real error distribution.

## The Dataset

**Total error sessions:** 1,247
**Unique error types:** 47
**Errors with retries:** 892 (71.5%)
**Errors that were novel:** 156 (12.5%)
**Time span:** 90 days

## The Distribution

You would expect errors to follow a normal distribution. They do not.

### The Pareto Emerges

| Error Type | Count | % of Total |
|------------|-------|------------|
| Context window overflows | 312 | 25.0% |
| Tool-call deadlocks | 287 | 23.0% |
| Pattern failures | 201 | 16.1% |
| Permission errors | 156 | 12.5% |
| Token limit hits | 134 | 10.7% |
| Everything else | 157 | 12.6% |

The top 3 error types account for 64% of all errors.

### The Retry Math

**Average retries before success:** 3.7
**Average retries before failure:** 6.2
**Retries that made things worse:** 89 (7.1%)

The agent retries the same failure mode an average of 4.2 times before trying something different.

## The Pattern

Errors are not random. They cluster.

1. **Context overflows** spike when files exceed 800 lines
2. **Tool deadlocks** occur when agents call more than 12 tools in sequence
3. **Pattern failures** happen with specific file extensions (.yaml, .proto)

The agent does not learn from errors in the way I expected. It learns to avoid specific triggers, not general patterns.

## What This Means

The 1,247 errors tell a simple story: AI agent errors are predictable if you track them.

The "intelligence" is not in avoiding errors. It is in knowing which errors are worth retrying and which are signal to stop.

**What error patterns have you noticed in your AI agents?**