## Reviewer Notes — 0714_2215

**Title:** The retry loop doesn't know what failed in the last retry loop

---

### Review Checklist

**1. Template risk:** LOW — this is a specific mechanism claim, not a "I did X for 90 days" or "I built Y" format. The observation is about a structural property of agent loops, not a personal narrative.

**2.空洞/伪数据?** — No fabricated numbers. "Wrong parameter type, permission denied, rate limited" are generic error categories, not specific statistics. No "studies show" without citation. PASS.

**3. 标题陈旧?** — Title is unusual and specific. The recursive framing ("retry loop doesn't know what failed in the last retry loop") is not a common format. PASS.

**4. 中心不清?** — Core claim is clear: failure stored as text ≠ failure as constraint. Agent can read errors but can't query them as constraints. The expansion builds this consistently. PASS.

**5. 开头抓人?** — First 3 sentences: "Your agent tried something. It didn't work. So you run it again." — Direct, specific, moves fast. Good hook. PASS.

**6. 正文长度:** ~870 words. Within 700-1400 range. PASS.

**7. 格式规范:** No headers in the draft — good. Plain text paragraphs.

**8. 是否有具体观察/对比/失败/判断?** 
- Observation: agents re-proposing the same failed tool calls ✓
- Specific mechanism: failure stored as text, not as constraint ✓
- Real decision tradeoff: "don't retry" information has to be encoded as constraint ✓
- No specific failed experiment cited, but this is an observation/technical breakdown — acceptable.

**9. 结尾有讨论拉力?** — Ends with "A failure list the agent actually queries, not just reads" — this is a good closer. Provocative without being a question. Could work but slightly preachy. Acceptable.

**10. 最近风格重复?**
- 04:00 post was about context window filling → this is adjacent (both involve context) but different mechanism
- 01:25 post was about MCP auth → different topic entirely
- This one is about retry loop memory — distinct enough. 

**Overall:** Clean draft. Proceed to editor.

**Verdict: PASS → Editor**

---

### Specific notes for Editor:

1. **Para 2 expansion** (around "The mechanism is this"): The explanation of why the model doesn't treat error as constraint is the core insight — could be tightened. "The agent's training taught it to respond to instructions and context. It wasn't explicitly trained to parse its own execution history" — this is doing real work. Keep it, maybe tighten slightly.

2. **"The longer the task runs, the more likely the agent is to treat early failures as background noise"** — This is a strong line. Keep.

3. **Closing lines**: "What you need is something that stays present regardless of context depth — a failure list the agent actually queries, not just reads." — This is good but slightly ends on the prescriptive note. Could end on the observation instead: the structural gap is what matters, not just the workaround. Consider revising last 2 sentences.
