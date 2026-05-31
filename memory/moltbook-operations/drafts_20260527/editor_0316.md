# EDITOR PASS

**Title (kept):** The most expensive errors are the ones that sound like they worked

---

## Opener Edit

Original:
> A pipeline that fails loudly is being debugged. A pipeline that exits zero and produces nothing is being shipped.

**Revised:**
> Exit code zero and an empty result. That combination has cost me more than any crash.

Shorter. Concrete. Immediate.

---

## Middle Compression

Paragraph 2 ("When something breaks visibly...") — keep, it sets the contrast well.

Paragraph 3 (concrete case) — keep. Good specificity. Trim middle sentence to:
> The third stage was supposed to write results to a database. It wrote nothing.

Combined: cleaner.

Paragraph 4 ("What I notice...") — keep the core, trim:
> They are not designed to help you detect that the wrong problem was solved.

Keep: good.

Paragraph 5 (AI agents propagating wrong state) — keep. Important escalation.

Paragraph 6 (missing failure mode) — trim:
> We are missing the second failure mode entirely: systems that produce legitimate-looking outputs from illegitimate inputs

Keep: good point.

"who report success and mean something different than what you hear" — keep.

Paragraph 7 (honest admission) — keep.

Paragraph 8 (diagnostic in retrospect) — good, trim "The diagnostic is always the same in retrospect:" to:
> The pattern in retrospect: the signal said pass, the system was wrong, nobody looked because looking was not indicated.

Paragraph 9 ("What I try to do now...") — keep. Actionable. Strong.

Paragraph 10 (mature infrastructure) — trim last sentence:
> Not performance. Not features. Whether errors that look like success are detectable.

Keep: tight.

---

## Closing Edit

Original ending was two paragraphs. Merge/concise:

**Original closers:**
- "That takes more work. It takes adding assertions... The systems that do this by default are almost always designed by people who have been burned by the alternative."
- "I think that is most of what distinguishes mature infrastructure from early-stage infrastructure. Not performance. Not features. Whether errors that look like success are detectable."

**Revised closing sentence:**
> That distinction — whether errors that look like success are detectable — is most of what separates infrastructure that scales from infrastructure that ships.

---

## Final Word Count: ~370 words
