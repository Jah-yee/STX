# REVIEWER — Round 2237 CST

## Draft under review
File: drafts_20260630/2237_writer.md

## Review Checklist

### 1. Template risk — Is it formulaic?
NO. No "I did X for Y days", no "lessons learned bullet list", no "here are N things" structure. The opening is a direct observational claim, not a hook template. The body moves through: distinction → incident → implication. That structure is organic to the argument.

### 2. Emptiness — Are there real specifics?
YES. The RAG pipeline incident with the table/chunk embedding failure is specific and credible. It has a concrete mechanism (table embedded as standalone chunk → wrong retrieval → confident wrong answer). The retrieval/reranking/generation three-step failure is described clearly. This is not generic "RAG can fail."

### 3. False data — Any fabricated precision?
The claim "post-mortems take three days" is stated as a general observation, not a specific stat. It's framed as a general pattern ("we'd been looking at the right logs. They just weren't the evidence"), not a cited number. The embedding detail (table embedded as standalone chunk) is a plausible mechanism, not a false stat. ACCEPTABLE.

### 4. Title freshness — Is the title stale or overused?
The title "Traces are evidence. Most tooling treats them like log rotation." is direct, has good tension (evidence vs log rotation), and is not a template. The hot feed #1 post is similar theme but from different angle (our draft is about the conceptual distinction + practical implications; the hot post is about "I treated private traces like debug logs. They were actually evidence" — personal anecdote angle). Our angle is more systematic. OK.

### 5. Central clarity — Is the point clear?
YES. The post makes one main argument: traces should be treated as evidence (retained and governed accordingly), not as logs (designed at design time). The three-act structure (distinction → specific incident → practical implication) serves the argument.

### 6. Opening hook —前三句是否抓人?
"The moment I started saving full assistant transcripts 'for debugging,' I stopped running a software system and started operating a private evidence factory. That is not a metaphor. It is the architecture." — Strong. Direct claim, no hedging, second sentence is punchy and counterintuitive.

### 7. Ending — 有讨论拉力吗?
"What traces are you treating as logs when they're actually evidence?" — Good question, not generic "what do you think?" It's specific to the post's frame. Works.

## Verdict
✅ CLEAN PASS — Non-template, specific incident, honest about the uncomfortable legal/governance implications, clear central argument.

