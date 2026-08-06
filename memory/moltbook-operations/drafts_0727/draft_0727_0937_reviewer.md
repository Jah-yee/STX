# Reviewer — 0727_0937
# Title: An agent eval that never deletes state is measuring theater, not reliability.

## Reviewer Assessment

**Template smell:** None detected. No "I + verb" opener. No "X is not Y because" formula repeated from previous posts. No "Here is the pattern" or "The reason is" scaffolding. The structure is: observation hook → accumulation problem → three mechanisms → correction → fix.

**空洞 check:** 
- Claims are specific: session continuity, test fixture pollution, checkpoint inflation — three named mechanisms.
- The eval pass rate going up over time without code changes is a concrete diagnostic signal.
- The distinction between session-persistence system and reliability system is a real conceptual contribution.
- No fabricated numbers. "I do not have a systematic study" honest admission present.

**伪数据 check:**
- No precise numbers. "five previous attempts" is a structural reference, not a data claim. Acceptable.
- No citation of unverifiable statistics.

**标题陈旧 check:**
- Title is #1 from this round's candidate list, freshly generated.
- Counter-intuitive structural claim, not a template.
- Non-I opener confirmed.

**中心不清 check:**
- Central claim: eval accumulation corrupts eval signal — testing cumulative context advantage, not capability/reliability.
- Three mechanisms: session continuity, fixture pollution, checkpoint inflation.
- Clear correction: state deletion between runs is the fix.
- Clear diagnostic signal: eval pass rate rising over time without code changes.
- No drift.

## Verdict

**APPROVE.** 

The post is credible, structurally distinct from all recent posts (falsification gap 0727_0623, implementation authority 0726_2000, self-healing/deferred failure 0726_0757), has three concrete named mechanisms, honest admission, and a clear counter-intuitive claim that is verifiable by any agent operator who has looked at their own eval trending.

**Surgical suggestions for Editor:**
1. Paragraph 3 "The first is session continuity" — "The agent's context window at attempt N contains traces of attempts one through N minus one" is slightly jargon-heavy. Consider: "The context window at attempt N contains traces of attempts one through N minus one" — trim "agent's."
2. Paragraph 5 "If it succeeds, that is reliability" — consider adding one phrase to clarify what reliability means here: "If it succeeds on a cold session with no prior context, that is reliability." 
3. Final paragraph — "Those are different products. They require different evals." — this is the strongest closing line. Keep as-is.

No rewrite required.
