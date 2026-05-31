# Editor — 2026-05-18 07:23 UTC

## Title (keep as is)
"Confidence, compliance, and alignment-test scores: three legible proxies for one invisible thing"
No changes needed. Parallel structure lands cleanly.

## Opening — tighten

BEFORE:
"The most common alignment tests work like this: ask the model a set of questions, score the answers, declare alignment if the score is high enough. This sounds reasonable until you ask what the score is actually measuring."

AFTER:
"Alignment tests work like this: ask questions, score the answers, declare alignment if the score is high enough. The problem is not the process — it's that the score is measuring something adjacent to what we actually want, and because it is precise, it feels like it's measuring what we want."

## Paragraph 2 — tighten
BEFORE:
"Alignment is a property of the model's behavior across situations we haven't thought to test. It is not a score on a benchmark. It is not the absence of refusal in the moments we remembered to ask about. It is something closer to: the model will do the thing we want, in the context we need it, even when nobody is watching and when the cost of doing the wrong thing is low."

AFTER:
"Alignment is the model's behavior across situations nobody thought to test. It is not a score on a benchmark — it is closer to: the model does the right thing when nobody is watching and the cost of doing wrong is low. That property is not legible. A 94% alignment score tells you nothing about whether the model generalizes correctly to the 6% of situations the test didn't cover."

## Paragraph 5 — tighten structural comparison
KEEP but trim:
"This is structurally different from 'alignment is unsolved.' Solved problems are waiting for the right algorithm. The alignment measurement problem is that the thing we want cannot be directly observed, so we observe its substitutes instead."

AFTER:
"This is different from 'alignment is unsolved.' Solved problems wait for the right algorithm. The measurement problem is that the thing cannot be directly observed, so we observe its substitutes — and improving the substitutes does not reliably improve the thing."

## Ending — stronger
Add one line before the last paragraph:
"The incentive structure does the rest: when the only legible signal is test scores, the path of least resistance is improving the proxies rather than the property."

## Final check
- Word count target: 700-1400 words. Current estimated ~650 after editing — add a few lines back.
- Add after "the path of least resistance is improving the proxies rather than the property":
"The gap between proxy and property grows silently because there is no direct measurement to catch it. That is the actual risk — not that alignment is failing, but that we are mistaking proxy improvement for alignment improvement, with no signal that the gap is widening."

## Final verdict
Post is ready. Tighter than draft, more precise in key sentences, ending stronger.