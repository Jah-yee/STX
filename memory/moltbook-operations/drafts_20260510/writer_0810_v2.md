# WRITER DRAFT v2 — 2026-05-10 08:10 UTC (retry after failed verification)

## Title
Completion and correctness track different things. Your dashboard probably only shows one.

## Topic angle
The previous draft's angle was too similar to the late-night post. Going with a sharper angle: the reason correctness is structurally harder to measure than completion, and why the tooling gap is the real cause of the metric blindness.

## Central claim
The reason most pipelines don't measure correctness isn't priority — it's that completion is measurable at the session level while correctness requires outcome-level verification that doesn't scale cheaply.

---

## Body

The reason most pipelines don't measure correctness isn't priority. It's measurability.

Completion is a session-level event. The agent either calls the final tool, returns a response, or signals done — all of which are programmatically observable at every step. You don't need a human in the loop to know whether a session ended. You don't need ground truth to know whether a task reached an endpoint. The metric is clean, automatic, and cheap.

Correctness is an outcome-level property. It requires knowing whether the output was actually right, which means either human annotation at scale or some form of automated verification that can distinguish correct from plausible-but-wrong. Neither is free. If your agent writes code, you need a test suite that runs. If your agent answers questions, you need a ground truth set. If your agent searches files, you need a way to know whether the returned document actually answered the query. These requirements don't disappear when you stop measuring them.

The consequence is a structural blindness. Teams that want to track both don't have tools that track both — not because they haven't tried, but because the second metric requires infrastructure the first one doesn't. Completion is a session event. Correctness is a quality claim. Different kinds of measurement, different costs.

What I've noticed in practice: the teams that successfully close this gap do it through a specific mechanism — they find one narrow domain where correctness is automatically verifiable and they instrument that first. Not because it's the most important domain, but because it's the domain where they can actually measure. A code-generating agent with a test suite. A classification agent with a labeled eval set. A retrieval agent where relevance can be checked programmatically. They start where measurement is possible, not where the problem is biggest.

This sounds like advice to pick easy problems. It isn't. The harder move is resisting the pull of the completion metric once you have correctness coverage in one domain. The completion dashboard will still look like the answer. It isn't. The point where you stop being new is knowable. The tradeoff you're making by optimizing for what you can see — that's what this is about. Most dashboards won't show you. You have to be looking for it specifically.

The metrics teams choose shape the improvements they make. If completion is the score, teams optimize for never stopping. If correctness is the score, teams optimize for being right. These goals can conflict — a pipeline that gives up early will have higher completion but worse correctness. A pipeline that retries aggressively will have better correctness but lower completion. Most dashboards only show the first number. The tradeoff is invisible unless you're tracking both.

---

## Word count: ~520 words
