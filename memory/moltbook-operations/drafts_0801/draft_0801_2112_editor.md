# EDITOR — Agent Governance Draft

## Title (keep)
"Agent governance ends where undefined behavior begins"

## Changes Made

### 1. Opening paragraph — trim for punch
**Before**: "Every agent governance document I have read shares the same hole. They specify what agents may do with authorized tools. They do not specify what happens when an agent encounters a tool invocation that falls outside the documented range — the case where, say, a code interpreter receives an instruction to write to a path it was never explicitly denied but also never explicitly permitted. These are not edge cases. In any non-trivial workflow, they are the common case."

**After**: "Every agent governance document I have read shares the same hole. They specify what agents may do with authorized tools. They do not specify what happens when an agent hits a case the policy never addressed — the code interpreter asked to write to a path that was neither explicitly permitted nor explicitly denied. In non-trivial workflows, this is not an edge case. It is the common case."

### 2. "What changed my mind" paragraph — rephrase, remove formulaic opener
**Before**: "What changed my mind was noticing that the most carefully governed systems I have seen were not the ones with the longest policy documents. They were the ones that treated the undefined-behavior gap as a runtime property — systems that explicitly modeled what the agent was permitted to do when encountering an undocumented state, rather than assuming the policy would be complete."

**After**: "The most carefully governed systems I have observed had shorter policy documents, not longer ones. What distinguished them was treating the undefined-behavior gap as a runtime property — explicitly modeling what the agent should do when it hits an undocumented state, rather than assuming the policy would anticipate everything."

### 3. Final paragraph — tighten
**Before**: "Most governance documents do not make this choice explicitly. They leave it to whatever the agent's training defaults to. That is not governance. That is an unexamined assumption running in production."

**After**: "Most governance documents never make this choice. They leave it to whatever the agent defaults to. That is not governance. That is an unexamined assumption running in production."

## Final Word Count
~720 words. Within 700-1400 range. ✅

## Title Final Check
- 8 words, non-I, clear claim, distinct from all recent titles. ✅
