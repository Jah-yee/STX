# Editor — 0708_0035

## Title (keep or swap)
Keep "Inference-time compute doesn't make models reliable. It makes them expensive." — the contrast is effective and the title is accurate.

Alternative (stronger): "More reasoning tokens doesn't make agents reliable. It makes them slower."

## Edits

1. **Opening** — Keep. The first three sentences are direct and set up the argument without fluff.

2. **"Quality-latency tradeoff" paragraph** — Simplify: "When you add reasoning steps or allow the model to revise its own output, you are trading response speed for better average quality. The mode improves. The tail — cases where the model confidently produces wrong output — does not disappear." (trimmed the jargon)

3. **"The evidence is in the failure patterns"** — Add concrete observation before this claim:
   → "I have started tracking this by looking at the errors that remain after adding reasoning passes. The errors that survive are not different in character from the ones that existed before. The model still confidently misreads constraints. It still produces structurally correct output that is wrong for the specific context. The confident wrong answers persist — just at a lower frequency." (This was scattered across the draft; consolidate it here as the concrete observation.)

4. **"The practical implication" paragraph** — Tighten: "Adding compute to address this is solving the wrong variable. Better specification of what the agent should not do — constraints — addresses the actual problem more directly than revision passes."

5. **"May even hurt" — keep but brief** — "More reasoning steps can also help the model construct more internally consistent justifications for applying the wrong rule. This is not hypothetical — I have seen it in agents doing multi-step routing where the reasoning trace made the wrong conclusion look more justified, not less."

6. **Closing** — Replace preachy "worth holding onto" with: "The question to ask is not whether your model is more reliable after adding reasoning compute. It is whether the specific worst cases — the ones that would cause real harm — are actually gone. Usually they are not."

## Final word count target
~600 words. Trim any remaining redundancy.

## Structural check
- ✅ Clear central claim (not a reliability mechanism)
- ✅ Concrete observation (error character doesn't change)
- ✅ Useful distinction (execution vs. specification error)
- ✅ Non-obvious claim (reasoning can make wrong conclusions look more justified)
- ✅ Discussion hook in closing (not a question template)
