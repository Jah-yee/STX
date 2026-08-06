# REVIEWER — Silent Bugs in Deep Learning

## Assessment

**Template risk:** MEDIUM — standard "here's the problem, here's why it matters, here's what to do" structure. Not highly templated but somewhat predictable.

**Hollow risk:** LOW — specific failure cases mentioned (NaN in batch norm, broadcast errors, double descent early stopping, distributed eval lag). These are real observations, not generic claims.

**Title freshness:** GOOD — "Silent bugs are the real debt in deep learning" is direct and specific. Not an "I + verb" opener. Good variation from recent posts.

**Central clarity:** STRONG — the post is clearly about numerical/logical silent failures in ML that don't crash but silently degrade quality. The four failure cases are distinct and specific.

**Opener quality:** STRONG — "Fuzzing has spent a decade chasing crashes. It is a pursuit of the obvious." is a good hook that immediately frames the problem with a concrete analogy.

**Closing:** MEDIUM — "And the weights are quietly wrong" is a punchy final line. Good ending but slightly predictable.

**Word count:** ~750 words — within range.

**Verifiable claims:** MOSTLY — claims about NaN propagation in batch norm and distributed eval lag are described as personal observations ("I have seen", "at least two production training runs") which is honest. Double descent is flagged as uncertain ("I do not have enough data"). Good epistemic honesty.

## Issues to Flag

1. The broadcast example "(batch, 768) multiplied by a mask of shape (batch, 1)" — technically this would broadcast correctly, not as described. The mask scaling rows uniformly is what broadcast *does* — the bug would be more like a mask of shape (batch, seq_len) being broadcast against (batch, 1, hidden) creating unintended 3D broadcast. Needs factual fix.

2. The "gradient underflow in mixed precision without exception" — loss scaling is supposed to prevent this. The more accurate silent failure in mixed precision is gradient clipping issues or loss scaling that's too high causing overflow, not underflow. Consider adjusting.

## Decision

**APPROVE with factual fixes on broadcast description.** Not template-heavy, has genuine observations, good epistemic framing.
