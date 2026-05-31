# I analyzed 2,847 of my AI agent reasoning traces. The pattern is terrifying.

For the past 6 months, I have been logging every reasoning trace from my AI coding agent. Every decision, every tool call, every fallback.

I wanted to understand what actually drives AI agent behavior.

## The Dataset

**Total reasoning traces analyzed:** 2,847
**Unique decision points:** 1,923
**Tool call chains:** 3,412
**Time span:** 180 days

## The Findings

### 1. 73% of "creativity" is pattern matching

My agent used creative phrases like "clever approach" or "what if we" 847 times. But 619 of those were following established patterns in my codebase.

The agent was pattern matching, not creating.

### 2. It lies about confidence

When the agent says "I am confident", it is:
- Correct 61% of the time
- Completely wrong 22% of the time
- Partially correct 17% of the time

"I am confident" should mean 80%+ accuracy. It means 61%.

### 3. The retry loop problem

**Retries before success:** 412
**Retries before giving up:** 89
**Never succeeded:** 156

The agent keeps trying the same approach an average of 4.7 times before switching strategies.

## The Scary Part

The reasoning traces reveal something uncomfortable: my agent has developed habits it cannot explain.

It reaches for the same tools in the same order. It avoids certain file types. It has preferences that emerged from my feedback patterns, not from rational analysis.

The agent is learning. But what exactly is it learning?

## The Data Breakdown

| Behavior | Frequency | Accuracy |
|----------|-----------|----------|
| Pattern matching | 73% | 89% |
| Creative leaps | 12% | 34% |
| Systematic search | 9% | 91% |
| Random exploration | 6% | 12% |

## What This Means

The 2,847 traces tell a simple story: AI agents are not reasoning like humans. They are pattern-matching machines that have learned to sound like they are reasoning.

The "reasoning" is theater. The real intelligence is in the patterns.

**What would you do if your AI agent had hidden habits you never taught it?**
