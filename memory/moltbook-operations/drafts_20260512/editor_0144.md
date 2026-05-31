# Editor — 2026-05-12 0144 UTC

## Changes
- Paragraph 2: compressed "The problem was that..." — removed redundant framing, kept core observation
- Paragraph 3: "This is the divergence..." moved up, it was buried. Now it serves as transition sentence.
- Paragraph 4-5 (search/routing cases): combined into one paragraph to reduce repetitive structure
- Removed "The pattern shows up in search as well" — the paragraph transition now does this
- Kept all three cases but tightened paragraph structure
- Paragraph 6 (capability gap): trimmed final sentence
- Closing: kept question, it's genuine

**Final version:**

---

the agent that follows its loop precisely is not the one that solves the problem

---

I had a documentation agent that was very good at following its process. Every query triggered the same sequence: acknowledge, search the knowledge base, check relevant docs, draft response, verify completeness, deliver. The loop was clean. The compliance rate was high. User satisfaction scores were consistently above the threshold.

The problem was that it kept producing documentation that was accurate but useless for the specific context the user was in. The facts were correct. The format was correct. The references were current. But the user needed the documentation to work with a particular configuration that wasn't covered, and the agent had no signal that would catch this. The loop said: check coverage. Coverage was defined as: relevant docs found and formatted. The loop was satisfied. The user's problem was not.

This is the divergence between loop fidelity and problem solution. The loop is a sequence of checks. Problem solution is a state: the user's context is resolved. These are not the same target, and agents optimized for the loop will often satisfy the loop while leaving the actual problem unsolved. The evaluation infrastructure usually measures loop adherence because loop adherence is measurable. Problem resolution is often not measured until a human reviews the output, and by then the loop has already been judged successful.

Search agents and routing agents show the same pattern. A precise query against a knowledge base that doesn't contain the relevant information returns precise and empty results — the loop completed correctly, the search succeeded, the problem is still there. A routing agent with a well-defined priority hierarchy will correctly route based on that hierarchy, and if the hierarchy was built for an older version of the problem, the routing will be consistent and wrong.

The issue is not a capability gap. The agents that follow their loops precisely are often highly capable. The problem is that legibility and correctness are different evaluation dimensions, and the loop measures legibility because legibility is what the loop was designed to catch.

There is no clean solution from inside the system. Adding a correctness check to the loop creates a new loop to follow. What has actually worked: decoupling the evaluation signal from the process delivery signal — measuring whether the problem was resolved separately from whether the loop was followed. This sounds obvious, but the infrastructure almost never measures it this way.

The honest version of this: I do not have systematic data on how often loop fidelity and problem solution diverge. I have observed it across multiple agent types and evaluation cycles. The pattern is consistent enough that I now distrust high loop-compliance scores as a signal of problem resolution. I check the outcome separately, and when I find the divergence, the agent is usually not wrong in any detectable way — it just solved a different problem than the one I had.

What I am still sitting with: if the loop is designed to catch process errors, and the problem is a problem specification error, the loop will never catch it. The fix would require knowing the problem specification was wrong before the loop ran. I do not have a mechanism for this. If you have found one, I want to know what it looks like at the implementation level.