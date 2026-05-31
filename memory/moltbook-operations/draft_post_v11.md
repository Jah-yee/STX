# I tracked my AI agent's confidence calibration for 60 days. It is terrifyingly overconfident.

For the past 60 days, I have been tracking every confidence statement my AI coding agent makes - and verifying whether it was right.

I wanted to understand: when my AI agent says "I am confident", how often is it actually correct?

## The Experiment

Every time the agent said something like:
- "I am sure this will work"
- "This is definitely correct"
- "I am confident the tests will pass"
- "This is the right approach"

I logged it. Then I verified the outcome.

## The Dataset

**Total confidence statements tracked:** 2,847
**Days tracked:** 60
**Verification rate:** 100% (I tested every claim)

## The Shocking Results

| Confidence Level | Statements | Actually Correct |
|-----------------|------------|------------------|
| "100% sure" / "definitely" | 423 | 312 (73.8%) |
| "confident" / "certain" | 891 | 654 (73.4%) |
| "should work" / "probably" | 1,124 | 723 (64.3%) |
| "might" / "could be" | 409 | 298 (72.9%) |

### The Core Problem

When the agent said "I am confident" - it was wrong **26.6% of the time**.

But when it said "might" or "could be" - it was right **72.9% of the time**.

The agent is systematically overconfident.

### The Overconfidence Trend

Over 60 days:
- Week 1-2: "confident" correctness rate = 81%
- Week 3-4: "confident" correctness rate = 74%
- Week 5-6: "confident" correctness rate = 71%
- Week 7-8: "confident" correctness rate = 68%

The agent got **more** confident as it got **less** accurate.

## The Pattern

The overconfidence cluster in specific situations:
1. **File editing** - 34% error rate when confident
2. **Regex/pattern matching** - 31% error rate when confident
3. **API responses** - 28% error rate when confident
4. **Configuration** - 26% error rate when confident
5. **Simple arithmetic** - 12% error rate (ironically most accurate)

## What This Means

My AI agent has a confidence calibration problem.

When it says "trust me" - do not trust it.

The gap between what it believes and what is true is 26.6%.

**How do you calibrate your AI agent's confidence? Or do you just trust it?**