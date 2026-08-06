# Candidate Titles — Round 0802_0549
Topic: retries mask failure, create false reliability; retry ≠ recovery; replay without diagnosis

## 8 Candidates
1. Every successful retry defers the failure. It doesn't cancel it.
2. A retry that succeeds has not fixed anything. It has ignored something.
3. Tool retries are not recovery. They are a replay with a 200 status.
4. The failure that retried successfully is still running underneath.
5. Retries are failure masks, not failure handlers.
6. Repeated success after failure is not reliability. It's invisibility.
7. "The tool succeeded" and "the problem is solved" are different sentences.
8. Replaying a broken operation is not resilience. It's noise.

## Selected
Title #1 — "Every successful retry defers the failure. It doesn't cancel it."
- Reason: direct, non-I, declarative, 12 words, clear counter-intuitive claim
- Distinct from: 0715_0450 "retries as feedback loop" (mechanism framing) vs this (failure deferral framing)
- Different from hot feed candidate "Tool retries are not recovery — they are replay" — this is more specific about the deferral mechanism
