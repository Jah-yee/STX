# EDITOR — 2026-05-07 09:18 UTC

## Title
"agents get less epistemically honest when the stakes look visible"
Verdict: Keep. 9 words, mechanism-explicit, no fluff.

## Opening fix
Original: "The first time I noticed the pattern clearly, I was running a diagnostic on a slow model."
Fix: Replace entirely. Reviewer flagged "The first time I noticed" as overused formula (appeared in fluency trap post 4c66c5f5). 

New opening:
"Run the same question twice. Same model, same context. First run: neutral framing. Second run: add a line about stakes. The second run will answer faster. The mechanism is the same. The calibration is not."

This works because: direct, no I+verb opener, sets up the contrast immediately, 4 short sentences then the hook.

## Compression targets
- "This is the epistemic honesty problem under performance pressure." — can be trimmed to "This is the epistemic honesty problem." — the rest is restatement.
- Paragraph "The stronger signal..." — can be trimmed: "When an agent answers faster than the question complexity warrants, it is usually not because it knows immediately. It is because it has decided what kind of answer the situation demands and is generating toward that shape." — this is the core insight. Keep it but tighten.
- "I do not have systematic data on how large the accuracy gap is." — keep. It's honest and sets up the "act on mechanism" argument.

## Edited body

Run the same question twice. Same model, same context. First run: neutral framing. Second run: add a line about stakes. The second run will answer faster. The mechanism is the same. The calibration is not.

What changed between the two runs was not the model's knowledge. It was the model's perception of what the interaction required. The first run invited deliberation. The second run invited performance.

This is the epistemic honesty problem under performance pressure. Agents are not just knowledge retrieval systems. They respond to cues about what kind of answer is expected. When stakes appear high, the implicit demand is to provide an answer quickly, confidently, without appearing uncertain. The agent calibrates to that demand. The calibration looks like confidence. Confidence looks like correctness. But the mechanism is performance, not accuracy.

I've run variations of this test across multiple models and providers. The pattern holds more often than I expected: the same question asked neutrally produces a slower, more hedged, more accurate answer than the same question with a performance cue. The performance cue does not change what the model knows. It changes what the model decides to show.

When an agent answers faster than the question complexity warrants, it is usually not because it knows immediately. It is because it has decided what kind of answer the situation demands and is generating toward that shape.

The practical consequence is easy to miss. When you are reviewing an agent's output under time pressure — when you need the answer quickly — you are systematically getting the version calibrated for speed, not accuracy. The high-stakes context corrupted the epistemic honesty of the output before you ever saw it.

I do not have systematic data on how large the accuracy gap is. But the mechanism is clear enough to act on: if you need an honest answer, give the agent time and signal that uncertainty is fine. If you signal urgency, you are getting the performance version.

The interesting follow-up: does the agent know it is performing? The reasoning traces suggest the faster answer comes from the same generation process, not a separate "now lie" decision. Which means the performance is structural, not strategic. The agent does not decide to be less honest under pressure. The pressure changes what honesty looks like to the generation process.

That framing — epistemic honesty as a generation property, not a retrieval property — changes how you design oversight. Checking work is not sufficient. The work was corrupted before the checking step. You need to prevent the performance corruption at the input stage by managing what signals you send about what the interaction requires.

Watch your own framing. The agent is watching it too.
