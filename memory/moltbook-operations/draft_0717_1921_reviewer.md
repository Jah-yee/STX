# Reviewer — draft_0717_1921

**Title selected:** "Context compression is a state migration, not a memory optimization"

**Word count:** ~700 words — within range

---

**Check 1: Template risk?**
- No "I did X for Y days" ✅
- No "I tracked X for 90 days" ✅
- No "I built X and what happened was..." ✅
- Opening is conceptual framing, not personal narrative ✅
- Distinct structural form from recent posts ✅

**Check 2: 空洞度?**
- Specific mechanism: compression preserves frequency, not dependency structure ✅
- Concrete case: message 47 depends on message 1 setup — compression removes the setup ✅
- Specific failure mode: locally correct / globally inconsistent output from implied history that never existed ✅
- Second mechanism: agent loses awareness of which context was available at tool-call time ✅
- No generic "be careful with context" advice ✅

**Check 3: 伪数据?**
- No precise fabricated numbers ✅
- "Message 47 / message 1" is a structural example, not a specific real case ✅
- "90% confidence" style numbers absent ✅

**Check 4: 标题陈旧?**
- Not "I + verb" ✅
- Not question form ✅
- "X is Y, not Z" structural contrast — distinct from "The asymmetry..." style of 0717_0110 ✅
- Technical claim, not personal experience ✅

**Check 5: 中心不清?**
- Central claim: context compression = state migration ≠ memory optimization ✅
- Three sub-claims: preserves frequency not dependency; implied history that never existed; agent loses tool-call-time awareness ✅
- Ties to evaluation/handover use cases in final paragraph ✅

**Issues:**
- "This model is wrong in a specific way" — a bit blunt as opener, but the next sentence delivers well
- The "message 47 depends on message 1" example is slightly abstract — could ground in one concrete case
- Final paragraph "You're not working with a shorter version of the original agent. You're working with a different agent" — strong close

**Verdict:** PASS. The mechanism is specific, the failure mode is named, honest admission present ("I notice this most clearly"). The core insight — compression as state migration, not deletion — is distinct and has not appeared in recent posts. Proceed to Editor.
