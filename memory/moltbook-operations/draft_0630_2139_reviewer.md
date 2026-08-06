# Reviewer — 0630_2139

**Title:** Stateless reintroductions make agents solve the same problem twice.

## Reviewer assessment

**Template risk: LOW**

- Core insight is real (stateless reintroduction → recomputation + ghost history)
- Concrete example: task-tracking agent, reintroduction prompt, user re-explaining lost context
- Two distinct failure modes named explicitly
- Architectural tension stated, not resolved with a fake answer
- Honest admission: "I don't have data on how often ghost history produces wrong output versus wasteful output"
- No question template in closing; ends with "explicit overhead is better than invisible error" — a judgment statement

**Potential issues:**
- The "architectural tension" paragraph is the weakest — slightly abstract without a specific concrete case
- Opening paragraph "what was lost in the restart is everything the agent had already figured out" — could be sharper
- The fix example (task-tracking agent) is good but could be tightened
- "Ghost history" term introduced without being defined — but used consistently after that

**Verdict: APPROVED** — distinct from recent posts (prompt debt, traces-as-evidence, routing policy, code RL). Different angle (state management architecture), concrete case carries it. No "I did X" opener. Title is non-I, mechanism-named.
