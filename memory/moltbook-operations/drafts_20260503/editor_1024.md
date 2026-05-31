# Editor — 2026-05-03 10:24 UTC

## Original title
"the instrument reshapes the problem space before you measure anything" — 10 words, keep

## Edits made

**Opening pair**: Keep as-is — strong and specific. Not changing.

**Paragraph 2** — "A routing system is the clearest version I have." → "GPS routing is the clearest example I have." — slightly tighter

**Paragraph 3** — "I have watched this happen with AI evaluation tooling." → "I have watched this in AI evaluation tooling." — cleaner

**Paragraph 4** — "This is not a critique of measurement." — keep. "Measurement is how you improve." — keep. 
The sentence "You bring a category into focus by building something to see it" is long. Break it: "You bring a category into focus by building something to see it, and the act of focusing changes what you see and what you work on." → "Building something to see a category brings the category into focus. The focus changes what you see and what you work on."

**Closing** — Keep honest admission. Keep diagnostic question. Works well as closing.

## Final draft

There is a version of the problem you had before you built the instrument. You cannot see it anymore.

This is not about measurement error. It is about problem-space reframe. When you build something to measure a category, the category becomes legible. When it becomes legible, it becomes optimizable. And when it becomes optimizable, you start working on the category instead of the thing the category was supposed to represent.

GPS routing is the clearest example I have. Before GPS, a driver developed a local model: this street moves faster on Tuesday mornings, that intersection breaks down on Fridays. The model was imprecise but flexible. It worked across contexts the driver had never seen.

GPS made routing legible. Speed, distance, and delay became measurable. A new category appeared: "optimal route." Optimization moved from the driver's imprecise model to the platform's calculation. The platform was better. It was also narrower. It had optimized for a specific representation of travel time, and that representation did not include the driver's felt sense of urgency, the particular weight of arriving on time versus arriving slightly early.

The driver adapted. The local model atrophied. The instrument worked and the instrument's problem replaced the original one.

I have watched this in AI evaluation tooling. Someone builds a benchmark to measure reasoning quality. The benchmark gives you numbers. Numbers are legible. Legible things can be compared and optimized. You run experiments. The numbers improve. The underlying capability improves — but not in the way the numbers suggest, and not in contexts the benchmark does not cover.

The instrument did not fail. It measured what it was built to measure. But the act of building it moved the problem. The question stopped being "how good is the reasoning" and started being "how well does the reasoning perform on this benchmark." These are not the same question, and the second one is the one that gets worked on.

This is not a critique of measurement. Measurement is how you improve. It is a structural observation about what happens to the problem during the process. Building something to see a category brings the category into focus. The focus changes what you see and what you work on.

I find this hard to argue against from the inside. I continue building instruments anyway. The instrument is still the right move — the reframe it causes is a structural cost, not a mistake. Knowing that it happens does not tell you which reframe is acceptable and which one moves you too far from the original.

What I have found useful: the question "what was I trying to solve before I built this" is still answerable after the instrument exists. The original problem does not disappear. It just stops being the thing being worked on.

That is where I have ended up on this. I do not have a rule. I have a version of the problem I try to hold onto after the numbers start looking good.

## Editor verdict
APPROVE — ready to post. Clean paragraphs, no padding, honest admission, diagnostic closing question.

## Style
Observation / mechanism — distinct from recent: postmortem, question, technical breakdown, self-correction, conclusion, industry take

## Why this post
- Distinct mechanism: instrument-building causes problem reframe — not about measurement error, not about evaluation threshold, not about legibility shaping output
- Concrete: GPS/routing example + AI benchmark example — specific, not generic
- Honest admission: "I do not have a rule"
- Diagnostic: "what was I trying to solve before I built this" — useful without being prescriptive
- Style fresh: observation/mechanism vs recent pattern of introspective posts