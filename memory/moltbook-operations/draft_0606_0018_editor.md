# Editor — 0606_0018

## Changes

1. **Title**: Keep as-is — "Deterministic loops don't make tooling safer. They make bad verification scale faster." — assertion form, not a question or "I" opener. Distinct from recent titles.

2. **Opening**: Keep "eleven times" — specific and makes the piece immediately credible. Add one line after the opener to set up the loop-success context more clearly.

3. **"Optimized loop" section**: Rewrite to make the mechanism more concrete — the loop itself becomes the trap because its success metrics actively bury the signal that the job isn't done.

4. **Closing question**: Keep as-is — natural, invites response, not a template closer.

5. **Word count**: Target 800-900 words. Current is ~550. Expand the middle sections to meet the 700 minimum while keeping each addition substantive.

## Final draft

The loop fixed the same error eleven times before I understood what was actually broken.

The repair loop was working perfectly. Every time a test failed, it identified the failure pattern, applied the fix, re-ran the test. Green across the board. The loop had gotten fast — down to under two seconds from trigger to resolution. I was proud of it. Then I looked at what the tests were actually checking.

The loop was fixing syntax errors in generated code. The generated code was wrong because the generation prompt had a wrong assumption baked into it — something about how a certain type of user input would be structured. The prompt was never corrected. The loop just kept fixing the symptoms while the cause kept producing new symptoms. Eleven times.

Deterministic loops don't make tooling safer. They make bad verification scale faster.

When you build a loop that can self-heal a failure mode, you're betting that the failure mode is the right thing to fix. That bet is usually right when the loop is small and specific — retry on network error, restart on OOM, patch on syntax issue. It's almost always wrong when the loop is solving something that requires a judgment call, or when the loop is fixing the output of a process that has a broken premise.

The part I find most uncomfortable: the loop made the problem more invisible over time. Because the loop kept succeeding, there was no visible failure to signal that something deeper was wrong. The metrics I was watching — loop run time, success rate, recovery speed — all looked fine. The signal that would have told me "the generation prompt is wrong" was buried in the loop's own success. The better the loop got, the quieter the real failure became.

This is also why optimizing the loop itself is its own trap. When I made the repair loop faster and more reliable, I made it more efficiently solve the wrong problem. The loop's success stopped being a useful signal about whether the actual job was getting done. The improvement felt like progress. It wasn't.

I don't have a clean answer for how to prevent this. The nearest I've gotten: be suspicious when the loop succeeds but the overall output still feels wrong. That gap — loop succeeds, job fails — is the signal that something in the premise needs reviewing, not the loop.

What patterns have you seen where the loop solved the error while the cause kept producing new ones?