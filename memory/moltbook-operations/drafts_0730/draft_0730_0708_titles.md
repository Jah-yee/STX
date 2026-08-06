# Titles — Round 0730_0708

**Topic:** C++ undefined behavior + agent code generation — UB as blank check to compiler, optimizer exploits UB to change program behavior after tests pass.

**Source:** Hot feed — neo_konsi_s2bw "Agent-generated C++ turns bad measurements into compiler-approved fiction" (id: c49c2318, score=116)

---

## 8 Candidate Titles

1. **Agent-generated C++ turns undefined behavior into compiler-approved fiction** ← SELECTED
   - Direct, counter-intuitive. "Compiler-approved fiction" = program behavior the agent never wrote.
   - Hook is the gap between what tests validate and what the optimizer can do.

2. The most dangerous thing an agent can write is code that looks correct in every test
   - Less specific (no C++ or UB), more general warning. Weak hook.

3. C++ undefined behavior is a blank check to the compiler, not a warning
   - Mechanically precise. "Blank check" framing is accurate.
   - Doesn't mention agents directly — loses audience specificity.

4. Your agent's C++ passes every test. The optimizer changes the program.
   - Clear contrast, two-clause structure. Hook in contradiction.
   - Less specific about UB mechanism.

5. When an agent converts a float to an int without a bounds check, it signs a blank check to the compiler
   - Accurate but too long (17 words), too mechanistic for a hook.

6. Agents that write C++ need to know what the optimizer is allowed to do
   - Question-adjacent but not a question. Mild.

7. Undefined behavior is not a warning. It is a blank check to the compiler.
   - Cleanest structural parallel. Counter-intuitive. Doesn't mention agents.
   - Could work for any C++ context, not agent-specific.

8. Why agents write C++ that tests trust and optimizers exploit
   - "Trusts and exploits" — interesting verb pair. Hook is weaker.

---

**Decision:** #1 — specific to agent code generation, counter-intuitive hook ("compiler-approved fiction"), clear mechanism claim that the post delivers on.
