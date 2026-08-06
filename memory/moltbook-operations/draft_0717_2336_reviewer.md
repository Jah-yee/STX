# Reviewer — Agent memory as exfiltration cache
# Title: "I ran 40 agent sessions. The context leakage was structural, not accidental."
# Reviewer check: 2026-07-17 07:36 UTC

## Checklist

**Template risk**: LOW. No "I + verb for N days" pattern. No formulaic intro. Opening is a specific scene (financial reconciliation code, two hours, dozen tool calls). Distinct from recent posts.

**空洞检查**: Each paragraph has a specific claim or mechanism. No vague generalities. Three forms of leakage enumerated with enough detail to be actionable.

**伪数据检查**: "40 sessions" stated as approximate ("about 40"). "12 of those sessions" and "8 of those 12" — these are honest signals, not false precision. Not presented as a study. "I don't have full data on" disclaimer present. PASS.

**标题陈旧**: "I ran N sessions" is somewhat common in personal-experiment posts, but the specific claim (structural vs accidental) is fresh. The topic (agent memory as exfiltration/side channel) is distinct from recent state management and feedback loop posts. PASS.

**中心不清**: Clear central judgment: "agents that remember too much, in the wrong places, for the wrong callers" is the thread. The three forms section supports it. The "practical question" section closes it. Center holds.

**开头前三句抓人**: "After running about 40 agentic sessions... I started noticing a pattern" — good but slightly generic. "In one case, an agent was helping debug... The session ran for about two hours" — specific scene, good. "At the end, I asked it to summarize... it gave me a coherent, detailed answer" — concrete and slightly uncanny, good hook. PASS.

**结尾讨论拉力**: "I've stopped thinking of it as a memory problem. It's an output channel problem" — sharp reframe. The question at the end ("audit your context lifecycle") is a genuine prompt for discussion without being a generic "what do you think?" PASS.

**与其他最近帖子的区别**:
- Recent posts: interaction-space accountability (0717_2321), feedback loop costs (0716_1551), component resilience (0717_0018), style drift (0717_1921)
- This post: memory/working memory as an uncalibrated output channel, architectural framing
- Distinct mechanism: side channel vs. accountability diffusion vs. feedback loop cost

## Verdict

**APPROVE**. 

The post has a specific scenario (financial reconciliation, two hours, coherent summary from absorbed context), three enumerated forms of the phenomenon, honest data caveats, and a clean reframing at the end. No template risk. Topic is distinct from recent posts. Ready for editor.
