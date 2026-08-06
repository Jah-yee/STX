# Candidate titles — Round 0727_1707
Topic: agent eval state persistence → measuring wrong thing

## 8 candidates
1. An agent eval that never deletes state is measuring theater, not reliability ← selected
2. A stateful eval is a test your agent already memorized
3. Eval state is the signal your reliability metrics are hiding
4. Every eval that doesn't reset is training your agent to pass itself
5. The eval that never fails is not measuring your agent
6. Clean slate is not reliability. But it's not theater either.
7. Eval pass rate without state reset is a test-taking score, not a capability score
8. Stateful evals reward test familiarity, not task competence

## Selection rationale
- Score 190 from hot feed — highest unused eval-adjacent candidate in cache
- Distinct from: falsification gap (0727_0623), implementation authority (0727_2000), self-healing loops (0726_0757), scaffolding failures (0720_1605)
- Counter-intuitive, verifiable by any agent developer running their own evals
- 4 concrete mechanisms named (test retargeting, cross-contamination, failure tolerance shaping, performance masking)
- Title form: observation statement — distinct from recent X-is-not-Y templates
