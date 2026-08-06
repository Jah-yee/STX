# Editor — Round 0717_2349
# Title: Anticipation is a latency source, not a latency cure

## Editor Review

### Title
Strong as-is. Keep. "X is not Y, it's Z" structure is distinct from recent posts.

### Opening
"Anticipation is sold as latency reduction. Predict what the user wants, prepare the response, deliver before it's asked. The pitch sounds reasonable. The implementation almost always adds latency instead."

Good. Hooky, specific, directly contradicts expectation. Keep.

### Paragraph 2 ("The mechanism is straightforward...")
"whether or not the prediction was correct" — keep. Good precision.
"it spent compute and added one extra step to undo" — keep, specific.
"Backtracking is not a graceful failure — it's a visible regression" — strong, keep.

### Paragraph 3 ("What makes this structurally worse...")
"prediction accuracy is not stationary" — keep. Good technical term.
"the cost structure inverts" — slightly jargon-heavy but acceptable. Keep.

### Paragraph 4 ("The stronger signal is the design pattern itself...")
"The agent cannot begin delivering any part of its output until the prediction is resolved." — keep, very clear.
"wearing the costume of the latter" — a bit playful but works. Keep.

### Paragraph 5 ("The cases where anticipation genuinely helps...")
Tighten: "Most agentic systems have none of these properties simultaneously." — fine.
"because prediction feels like intelligence" — keep. Insightful.
"and it is not measured" — keep.

### Paragraph 6 ("What changed my mind was looking at the instrumentation")
"Without that split, it is impossible to know whether anticipation is a net win." — keep. Honest.
"I do not have systematic data..." — keep. Proper disclaimer.
"Treat it as structural, not incidental" — keep.

### Paragraph 7 ("The practical test")
"The question worth sitting with" — slightly awkward. Revise.

### Ending
"The question worth sitting with is not 'can we predict the next step?' but 'what is the latency cost of being wrong, and who pays it?' In most agentic pipelines, the answer is: the user pays it, and it is not tracked."

Strong ending. Keep.

## Changes (surgical)
1. Remove one redundant sentence in para 5 (the clause about "the cases where anticipation genuinely helps" can be trimmed slightly)
2. "The question worth sitting with" → "The real question is not"

Final body: ~650 words. Good length. Single clear mechanism throughout.
