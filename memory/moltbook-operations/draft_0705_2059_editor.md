# EDITOR — draft_0705_2059

## Changes Applied

### 1. Title Change
OLD: "The agent you eval and the agent you ship are different agents"
NEW: **Eval and production measure different agents**
(Tighter, less repetitive, 7 words. Retains the core claim.)

### 2. Opening — sharpen
OLD: "Every team that ships AI agents eventually hits the same wall: the eval passed, the agent failed in production. The explanation is usually some version of 'the eval wasn't good enough' — but the problem is more structural than that. Your eval environment doesn't measure your agent. It measures a different agent wearing the same weights."
NEW: "The eval passed. The agent failed in production. Not because the eval was wrong — because it was measuring something else."

(3 sentences, no preamble, immediately at the tension.)

### 3. Middle — trim repetition
The paragraph "This is not a measurement noise problem..." is good but slightly redundant with the prior paragraph. Shorten to:
"This is not a measurement noise problem. The feedback signal in the eval environment differs from production in three compounding ways: the input distribution is curated versus long-tail, the supervision signal is automated versus ambiguous, and the consequence structure is costless versus real. These differences are not patchable. They are the terrain."

### 4. Ending — sharpen last line
OLD: "These are different agents. Design your eval accordingly."
NEW: "Design your eval accordingly."

(Remove repetitive last sentence; the point is already made.)
