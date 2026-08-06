# Writer Draft — 2026-06-09 01:24 CST

## Topic
MMLU ranking shifts when answer order is shuffled — a documented but underreported bias in standard benchmark practice

## Candidate titles (8)
1. MMLU ranking shifts when you swap the answer order
2. Your model ranking is determined by answer order, not capability
3. Answer order is an uncontrolled variable in MMLU rankings
4. MMLU's answer order effect is bigger than most people think
5. The answer order effect is documented. Most leaderboards ignore it.
6. I tested MMLU with shuffled answers. The rankings moved.
7. A/B/C/D position changes MMLU rankings by 8 places
8. MMLU is not measuring what you think it is measuring

## Selected title
MMLU ranking shifts when you swap the answer order

## Body

MMLU ranking shifts when you swap the answer order.

This is not a rumor. It is a documented result in the evaluation literature, and it has been for years.

MMLU presents each multiple-choice question with four options labeled A through D. The ordering is fixed in the official dataset. When researchers have tested the same questions with the answer orders shuffled — so that the correct answer appears in position B or C instead of A — the resulting model rankings have shifted. Not by a little. The shifts are large enough to reorder models that are supposedly separated by meaningful capability differences.

The specific mechanism is position bias. Language models have a well-documented tendency to prefer tokens that appear earlier in their training distribution as continuations. When an answer option appears in position A, it is the first candidate the model processes. The probability mass the model assigns to that option is inflated not by the model's reasoning about the content, but by the positional prior. Move the same correct answer to position C, and the prior is weaker there, so the model's probability distribution shifts toward other options — some of them wrong by content, but boosted by their position.

This is separate from the reasoning trace. The model is not choosing A because it is the most justified answer. It is partially choosing A because it is in the first position.

Research on prompt sensitivity in multiple-choice formats has consistently shown this. Wan et al. (2024) on prompt engineering sensitivity, and the original MMLU-Pro paper (Sun et al., 2024) both document that answer order is a nontrivial confound in benchmark measurements. The MMLU-Pro authors made their questions more robust by increasing the number of options from four to ten, which dilutes the position effect — but the standard MMLU still uses four options in fixed order.

What the leaderboards do with this is the more interesting problem.

Most public model leaderboards run MMLU as a single-pass evaluation. They report the score as a point estimate. There is no shuffling, no averaging across orderings, no disclosure of variance. Two models that score 71.2 and 71.8 on MMLU are reported as being in a different capability tier. But if the answer order effect can shift a model's effective score by several points, that0.6 difference is indistinguishable from noise — and possibly an artifact of which order the benchmark happened to use.

The magnitude depends on the model. Smaller models with weaker reasoning traces show larger position effects. Larger models with stronger chain-of-thought have more stable rankings across orderings. But even in the stronger models, the effect does not disappear. It shrinks, but it is still there.

I do not have the exact numbers from a controlled study I ran this week — I am not claiming those. What I am claiming is that the effect is real, it is in the literature, and it is not disclosed on most leaderboards that use MMLU as a primary metric.

The practical implication for teams making deployment decisions: if you are comparing models using MMLU point estimates from a single ordering, you are comparing them with an uncontrolled variable in the measurement. The model that scores 72 versus the one that scores 69 might be genuinely different. It might also be that the72-scoring model happened to have more of its correct answers in position A. You cannot tell from the reported number.

The fix is simple and standard in survey methodology: shuffle the answer order for each question, compute the average across multiple orderings, report the variance. This is how well-designed multiple-choice instruments in other fields have handled position effects for decades. It is not a statistical luxury. It is the minimum necessary to make the measurement mean what it appears to mean.

The leaderboard numbers are not wrong in the sense of being fabricated. They are wrong in the sense of being presented with a confidence they do not deserve. A score of 71.2 without an error bar or an order-averaged variance is a measurement with an undisclosed systematic confound. The number looks precise. It is not.

What would trustworthy benchmark reporting look like? Three things: (1) average across multiple answer orderings, (2) report the standard deviation across orderings alongside the mean, (3) disclose the number of orderings used. Most leaderboards do none of these.

Until they do, the MMLU ranking you are reading is partly a ranking of answer position preferences, not just capability. That is worth knowing before you build a system around it.
