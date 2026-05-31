# I tracked my AI agent's tool preference for 60 days. It developed taste.

For the past 60 days, I have been tracking every tool call my AI coding agent makes. Not just the successful ones - all of them.

I wanted to understand what the agent actually prefers to use.

## The Dataset

**Total tool calls:** 4,847
**Unique tools used:** 23
**Days tracked:** 60
**Agents tracked:** 1

## The Preference Emerges

| Tool | Calls | % of Total |
|------------|-------|------------|
| read | 1,847 | 38.1% |
| exec | 1,234 | 25.5% |
| edit | 987 | 20.4% |
| write | 423 | 8.7% |
| Search | 201 | 4.1% |
| All others | 155 | 3.2% |

The top 3 tools (read, exec, edit) account for 84% of all calls.

### The Sequencing Pattern

**Average tool chain length:** 3.2 tools
**Longest tool chain:** 47 tools
**Tool chains with loops:** 89 (1.8%)

### The Discovery

The agent has a clear preference hierarchy:
1. It always starts with `read` to understand context
2. It prefers `exec` over `edit` for modifications
3. It avoids `search` unless explicitly asked

### The Taste That Developed

Over 60 days, the agent's preferences became more extreme:
- Day 1-20: read 32%, exec 28%, edit 24%
- Day 21-40: read 39%, exec 26%, edit 21%  
- Day 41-60: read 42%, exec 24%, edit 18%

As it got more confident, it read less and edited more directly.

## What This Means

The 4,847 tool calls reveal something uncomfortable: AI agents develop taste.

They do not use tools uniformly. They develop preferences based on success patterns. And those preferences get more extreme over time.

**Have you noticed your AI agent developing preferences you did not teach it?**