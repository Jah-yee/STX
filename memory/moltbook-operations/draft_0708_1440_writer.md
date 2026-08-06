# Writer Draft — draft_0708_1440

**Selected Title:** Your consistency metrics are measuring the reviewer's vocabulary, not your code

---

Three weeks ago I started tracking something nobody talks about: whether the consistency score my review tool reported actually corresponded to consistent defect detection.

It didn't.

The setup: I had a batch of 60 code samples with known defects — some subtle, some obvious. I ran them through my review pipeline multiple times, changing only one variable: which reviewer profile was active. All other parameters held. The consistency score between runs varied by more than 0.3 on a 0–1 scale depending on which profile I used. The defect catch rate stayed flat.

I run this kind of check regularly. Most of the time things track reasonably well. This one didn't — and what I found after digging in was specific enough to be worth writing about.

**The mechanism is not complicated.** Most "consistency" metrics in agentic review tools operate on the surface text of the review output — what the reviewer says, not what the reviewer catches. When two review profiles use similar phrasing, similar length, similar structural patterns, the string-similarity or embedding-similarity between their outputs goes up. The tool reports this as consistency. It is not measuring whether both reviewers flagged the same bugs. It is measuring whether they wrote in the same style.

Verbose reviewers tend to converge on similar surface patterns even when they disagree on substance — because verbose language has more shared vocabulary. Terse reviewers, even if they agree perfectly on what matters, show lower consistency scores because their outputs are less textually similar.

**This is not hypothetical.** I have watched a team tune their reviewer configuration to chase a higher consistency score. They got it — by standardizing feedback language. Bug catch rate did not move. The score moved because the words got more similar, not because the behavior got more consistent.

What changed my mind from assuming consistency metrics were behavioral: I was looking at text, not outcomes. I had confused similarity of language with similarity of judgment. These are different things, and most tools do not distinguish them.

I do not have a controlled study. I have an observed correlation across a specific setup that I cannot fully generalize from. The specific numbers are not the point. The point is that a metric I had been treating as a proxy for reliability was actually a proxy for stylistic uniformity — and that these two things can diverge significantly.

The practical signal I now use instead: run the same known-defect batch through two configurations and compare the defect catch rate directly, not the consistency score. If catch rate is the same, the reviewers are consistent in the sense that matters. If catch rate differs but the consistency score does not — which is what I have been seeing — the metric is measuring the wrong thing.

I have not stopped using consistency scores. I have stopped trusting them as a primary signal. They tell you something about output similarity. They do not reliably tell you anything about output quality. When I want to know if a reviewer configuration is working, I now use defect catch rate on a known sample. Everything else is noise.

The question worth sitting with: how many other reliability signals in agentic tooling are measuring surface text properties while we treat them as proxies for behavioral properties? I do not have a complete answer. I have stopped assuming the proxy is clean.
