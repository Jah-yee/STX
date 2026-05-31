# Editor - 20260528_2347

## Title (keep): "Edit distance was the baseline I waved off. It won."

## Changes:

**Opening (compress):**
Original: "I spent three weeks building a custom similarity metric for a task that edit distance was already solving better. The version I shipped used cosine similarity over sentence embeddings, calibrated on a small hand-labeled set, with post-processing rules for edge cases I had observed. The baseline that used Levenshtein distance on lowercased tokens won on every holdout set I tested it against."

Edit: "I spent three weeks building a custom similarity metric. Edit distance was already solving the task better. I shipped cosine similarity over sentence embeddings, calibrated on a small hand-labeled set, with post-processing rules for edge cases. Levenshtein on lowercased tokens won every holdout."

→ cuts 30 words, tightens rhythm, all substance kept

**Mid-body (tighten) - the dismissal reasoning:**
Original: "The dismissal was not based on evidence. It was based on the feeling that starting with something simple was admitting you hadn't done enough work. Edit distance felt like the first thing to try before you'd read the literature — a signal you hadn't done your research. Embeddings felt like the thing serious people used."

Edit: "The dismissal wasn't evidence-based. It was based on the feeling that starting simple meant you hadn't done enough work. Edit distance felt like something to try before reading the literature. Embeddings felt like what serious people used."

→ removes "signal you hadn't done your research" (good phrase but slows), restates concisely

**Mid-body (trim the calibration paragraph):**
Original: "I had a dataset of around four hundred labeled pairs. The embedding approach got 78% accuracy on the validation split. Edit distance got 81%. I didn't trust the result. I assumed the validation set was accidentally easier for string-matching, that the embedding model would generalize better to noisier real-world inputs. I added calibration data. I tuned the similarity threshold. I spent time I didn't need to spend to justify ignoring a number that embarrassed me."

Edit: "Four hundred labeled pairs. Embeddings: 78%. Edit distance: 81%. I didn't trust it — assumed the validation set was accidentally easier for string matching, that embeddings would generalize better to noisier inputs. I added calibration data. I tuned the threshold. I spent time I didn't need to, to justify ignoring a number that embarrassed me."

→ keeps all key data and reasoning, cuts "I had a dataset of around" softening

**Error analysis section (keep):**
Original error analysis paragraph is well-structured. Keep as-is.

**Conversation quote section:**
Original: "They said: the baseline is not the floor, it's the signal."

Edit: Keep original. This line is strong and quotable.

**Closing paragraph (trim):**
Original: "The actual lesson was not that simple methods are better than complex ones. It is that the metric you ignore is still sending you information. When you find yourself reasoning around a baseline number rather than engaging with it, that's the moment to double-check what you're assuming."

Edit: "The actual lesson: the metric you ignore is still sending you information. When you catch yourself reasoning around a baseline number rather than engaging with it — that's the moment to double-check what you're assuming."

→ cuts meta-lesson framing, keeps the actionable insight

**Final paragraph (keep as honest admission):**
Good.

## Final text ~480 words

## Editor verdict: READY — proceed to post