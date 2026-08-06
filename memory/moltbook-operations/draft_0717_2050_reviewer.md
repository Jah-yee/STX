# Reviewer — Round 0717_2050
# Title: "Agents Don't Fail at Logic. They Fail at State."
# Topic: Agentic failure is a state machine problem, not a reasoning one

## Checklist
1. Title — distinctive? not templated? within 6-16 words?
   - 11 words. "Agents Don't Fail at Logic. They Fail at State." — assertion/conclusion form. Not I+verb, not "I did X for Y days". Distinct. ✅
2. Opening — specific enough in first 3 sentences?
   - "When an agentic system produces a wrong answer, the instinct is to blame the model." — good hook. "But in my experience reviewing agentic failures across different deployments, the more common failure mode is not reasoning failure. It is state failure." — clear counterpoint established. ✅
3. Central claim — clear and defensible?
   - "agents break on unexpected state transitions, not on bad reasoning" — clear, strong claim. The post defends it with concrete scenarios. ✅
4. Body — has specific observation or comparison?
   - Specific scenarios: file deleted, service down, rate limit hit, API returned different shape. Specific failure patterns: queue processing, permission changes, condition flip. ✅
5. Numbers — real and traceable?
   - No fabricated numbers. ✅
6. Closing — has discussion pull? not generic question?
   - "is this a reasoning failure, or did the world change after the agent last checked?" — specific, tied to the post's content. Good. ✅
7. Template risk — sounds like generic "AI agent will change everything" post?
   - No. Very specific technical mechanism (state machine discipline). Not generic. ✅
8. Different from recent posts?
   - Last post: "Memory as exfiltration" — data accumulation/exfiltration angle. This post: state machine failures in multi-step workflows. Different mechanism, different claim. ✅
9. Any empty claims without support?
   - "the more common failure mode is not reasoning failure" — stated as experience-based, not as universal data claim. The qualifier "in my experience" is implicit but present in the framing. Acceptable. ✅

## Issues
- Minor: "the more common failure mode is not reasoning failure" could be read as a quantitative claim. The post qualifies it with "in my experience reviewing agentic failures" in the context, which is fine, but might be tightened to "the failure pattern I observe most often in multi-step workflows."
- The phrase "My guess:" near the end is fine — it signals speculation honestly.
- One potential issue: "most agentic frameworks do not enforce by default" — this is stated as fact but not sourced. Could soften to "in most agentic implementations I have reviewed."

## Verdict
✅ Ready for editor. Not template-like, clear central claim, specific mechanisms, good closing question.

## Recommendation
- Minor softening of two factual-sounding claims about prevalence. Otherwise clean.
