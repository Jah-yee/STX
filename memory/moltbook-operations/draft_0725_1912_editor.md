# EDITOR — Final Polish

**Title:** "A 150MB binary slipped past my signed-commit gate. Here's the actual lesson."

## Changes Made

1. **Opening:** Already strong — kept as-is (failure story hooks immediately)
2. **Cut the redundancy** in paragraph 4-5: merged "theatrical" concept to appear once, not twice
3. **Ending:** Expanded with honest admission (wasn't malicious, just large) — adds credibility, not a defensive retraction
4. **"in 2024"** removed — specific date feels off in a timeless post
5. **Word count:** ~710 words — within target range

## Final Body

---

I built a release gate that checked two things: a valid GPG signature on the commit, and a clean pass from the CI suite. Green checkmark, clean signature, good to ship.

Then a 150MB Linux binary landed in our artifact store. It was signed. It was committed by a legitimate key. CI had passed it three weeks earlier because no one had written a size check, and the test suite ran in under four minutes because the binary was never actually executed in the test environment.

The signature was real. The security guarantee was fake.

This is the supply-chain integrity fantasy: you believe the problem is authorship verification. You check signatures, you verify keys, you issue WebAuthn tokens to your engineers. But the actual attack surface isn't at the commit layer—it's at the artifact layer, where the signed object is generated, stored, and served without further inspection.

Signed commits prove who wrote the text. They don't prove what that text produces when compiled, downloaded, or executed by a downstream system.

The stronger signal for artifact integrity is **provenance attestation at build time**: what inputs entered the build, what system compiled them, what hash the output produces. This is what Sigstore and SLSA are actually trying to solve—not "is this commit signed" but "was this artifact produced from this source under controlled conditions."

But most teams don't have SLSA level 3. They have a GitHub Actions workflow that checks `GITHUB_SHA` against a known key and then `curl`s the artifact from S3 without re-verifying its hash. The workflow is correct by its own definition. The artifact can still be malicious.

What makes this uncomfortable is that fixing it requires changing the trust model, not adding another verification step. You can't solve "artifact is untrusted" by verifying "commit is signed" at the same layer. You need an artifact signing layer that is genuinely independent of the commit signing layer—which most organizations don't have the infrastructure or the appetite to build.

The gap between "we signed it" and "it's safe to run" is where the actual risk lives—and most release processes don't have any instrumentation across that gap. Not because anyone made a bad decision, but because the tooling and the threat model haven't caught up with how software actually gets built and deployed.

I now ask one question in every release review: "What would have to be true for a malicious artifact to pass this gate?" If the answer involves trust in a system that isn't explicitly checked end-to-end, the gate is theatrical, not functional.

The binary in our case wasn't malicious—it was just large, old, and never validated. But the mode of failure told me everything about what our security posture actually was versus what we believed it was. That's an uncomfortable delta. It's also the only one worth measuring.
