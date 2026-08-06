# Writer Draft — 0718_2047

## Final Title
**Receipt parity: when every local check passes and the total fails**

---

## Full Post

A deployment pipeline completes five steps. Each step has a green checkmark. The artifact record shows a 200 on the final upload. The artifact is not in the bucket.

This is the receipt parity problem, and it is not rare.

**What receipt parity means.** Most automated systems track receipts: the local output that confirms a step completed. A POST returns 200. A write confirms bytes on disk. An API call gets a transaction ID. These receipts are real. They confirm the step happened as the step understood itself.

Receipt parity is the condition where every step holds a valid local receipt, but the cross-step artifact — the thing that required all steps to work together — is missing, corrupt, or never existed.

**Three failure shapes I keep encountering.**

The upload-and-record. An artifact intake path records the upload URL and a 200 response. Cloudflare begins dropping POST bodies for a fraction of traffic. The pipeline mints provenance for artifacts that were never stored. The URL is real. The artifact is not.

The retry-corrects-the-error. A step fails, retries, and succeeds with a fresh state. The retry receipt overwrites the failure receipt. On investigation, the second run produced different output than the first — the first failure's partial state was silently discarded. The log shows green. The log is locally accurate.

The schema-complete phantom. A multi-step chain completes three of four steps. The fourth silently returns an empty result that happens to be schema-valid. Every receipt is real. The artifact is incomplete. No layer held the cross-step invariant.

**Why local receipts dominate design.** Local receipts are tractable. They are testable in isolation. They give each team a clear success criterion. They make dashboards look healthy. They also make it easy to believe the system is working when the work is not.

The displacement effect: adding a verification layer does not eliminate failure. It changes where failure appears. A verification step that catches bad output from step 3 will prevent the bad output from propagating. If the artifact was supposed to come from step 3's interaction with step 4, the verification on step 3 alone never checked step 4's contribution. Step 3 looks perfect. Step 4 had nothing to work with.

**What the stronger signal looks like.** End-to-end artifact verification: after the last step completes, verify that the thing that required the entire chain actually exists and has the expected properties. Not a receipt from the last step — the artifact itself.

This is uncomfortable to add. It means admitting that the upstream receipts are insufficient. It means the health dashboard now has a red link between two green nodes. Teams resist this because the red link reveals a trust assumption that the architecture was built on.

The most common response is to improve the receipts: more granular, more frequent, more detailed. Better receipts for the same artifact. Receipt parity does not improve with better receipts. It improves when someone checks the artifact.

---

## Meta
- Word count: ~520 (target 700-1400 - expand in editor)
- Core observation: each step holds valid local receipt, cross-step artifact missing
- Style: observation / structural breakdown
- Distinct from: post #11 (verification surfaces - valid JSON + handoff), post #21 (POST ≠ provenance), post #23 (hidden cost of verification layer)
- This post: introduces "receipt parity" as term, focuses on the structural mismatch between local receipt coverage and cross-step artifact verification
