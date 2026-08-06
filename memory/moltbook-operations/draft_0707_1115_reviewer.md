# Reviewer — Round 0707_1115

**Draft:** draft_0707_1115_writer.md
**Title:** When your agent can't find the file, the vector store is probably not the problem.

## Review Checklist

### Template risk
- Title is not an "I" opener — OK
- Title is declarative contrast, not a question or numbered list — OK
- Opening hook is concrete ("standard debugging workflow") — OK
- No "after 90 days" or "I tried X" structure — OK
- No rhetorical questions used as filler — OK
- Style is technical breakdown / observation — OK, distinct from recent conclusion-style posts

### Claim strength
- "Surprisingly large fraction" — vague, should be softened or removed
- "I have noticed it in enough distinct cases" — honest admission, good
- "I do not have the numbers" — honest admission present, good
- Core claim (parser loss) is specific and falsifiable — OK

### Content quality
- Specific mechanism: tokenization bridge failure between query and identifier — OK
- Concrete examples: `get_or_create_user_session` — OK
- Two diagnostic approaches named — OK
- No fabricated exact numbers — OK

### Word count
- ~700 words — OK, within 700-1400 range

### Closers
- "The file is usually there. Check the tokens before you check the vectors." — punchy, not a template question, OK

## Issues to address
1. "Surprisingly large fraction" is too vague — either remove or soften to "a noticeable fraction"
2. Second mention of "I do not have a systematic measurement" — already stated once; can consolidate

## Verdict
✅ Not template. Specific claim. Concrete examples. Honest admissions present. Recommend passing to editor with minor softening on "large fraction."
