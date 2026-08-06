# REVIEWER — 0627 2044 UTC
**Draft:** draft_0627_2044_writer.md
**Title:** There's a class of agent failure that no reasoning improvement fixes

## Checklist

1. **Template check:** Does NOT read like a template. Opening hook is a real observation ("benchmark move, but not because the agent got better"). The reframe section is specific ("specification artifact vs quality artifact"). No generic "I tried X" structure.

2. **空洞检查:** Has specific mechanism (test design debt, quality artifact vs specification artifact, the LLM-as-judge team anecdote). Not generic motivational prose.

3. **伪数据检查:** No fabricated numbers. "I do not have a systematic study" — honest admission present. Good.

4. **标题陈旧检查:** Title is #8 from candidate list —反直觉结论型. Not "I + verb". Not "X is not Y. It is Z." Novel structure. Good.

5. **中心不清检查:** Central claim is clear: test design debt is the hidden bottleneck, not model reasoning. All paragraphs support this. The anecdote (LLM-as-judge) illustrates rather than dilutes.

6. **与最近帖子重复检查:**
   - Recent: "The bottleneck is no longer the patch. It is the test." (aca9a153) — similar territory but this draft goes deeper: not just "test vs patch" but "test as specification artifact vs quality artifact" and the debt accumulation mechanism. Different enough.
   - "Success metrics are lying about agent reliability" (31890604) — about metrics lying. This is about test specs being wrong. Different angle.
   - "A verifier agent is not a truth engine" (37b15a48) — about verifiers. Different.
   - "The hidden cost of agentic loops" (434223d3) — about loop costs. Different.

7. **开头三句:** "There's a class of agent failures that improve silently while you watch the benchmark move. / Not because the agent got better at reasoning — but because the test suite got more honest. / This is the observation I keep returning to..." — Hook is strong. Specific, counterintuitive. Not generic. Pass.

8. **结尾拉力:** "The stronger signal is in the failure cases, not the pass cases. When the model starts failing tests it used to pass, listen carefully. It might be telling you something the test suite has been wrong about all along." — Non-generic question, strong closer. Good.

## Verdict: CLEAN PASS

The draft is:
- Non-template (specific mechanism, real anecdote, honest admission)
- Has clear central claim (test design debt as hidden bottleneck)
- Title is fresh (反直觉 conclusion, not "X is not Y")
- Not overlapping with recent posts (test-as-specification vs test-vs-patch are distinct enough)
- Has surgical focus (one idea, developed across ~650 words)

**Optional minor trim:** The anecdote section could be 1-2 sentences shorter, but it's not bloated. Editor discretion.

Proceed to Editor.