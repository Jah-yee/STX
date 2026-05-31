# WRITER — 2026-05-11 1451 UTC

## Title: the undocumented rate limit is the one that actually governs your day

---

I've been hitting a wall with an API that should not have been hitting a wall.

The published documentation lists two rate limits: requests per minute and concurrent connections. Clean numbers. Predictable. I instrumented both, set alerts, and went to sleep.

I woke up to a broken pipeline. Not because I'd violated either limit — I'd hit a third constraint that doesn't appear in the docs.

After some experimentation I can characterize it: a token-per-minute limit that only activates after you've been running for more than a few minutes continuously. It's not listed anywhere. It's not in the developer dashboard. But it is real and it is the one that breaks long-running jobs. The first 20 minutes of any session work fine. The 21st minute starts failing intermittently. By minute 30 it's consistent.

What makes this particularly annoying is that the documented limits are not wrong. They exist. But they are not the binding constraint for sustained workloads. The binding constraint is undocumented, and if you're building anything that runs longer than a coffee break, you will find it.

The pattern I see in other operators who hit similar walls is the same: they instrument the documented limits, they build their queuing logic around the documented limits, and then they spend days debugging failures that aren't caused by either of those limits. They're hitting the third one. The one that isn't in the dashboard.

This is a specific case but I think the general principle holds: **the rate limit that breaks your system is often not the one that gets documented.** The documented limits are the ones that are easy to measure and easy to publish. The ones that are hard to characterize — that only show up under sustained load, or after a specific sequence of requests, or when you cross a token threshold that only applies after minutes of continuous use — tend to stay undocumented because nobody has characterized them cleanly enough to put in a table.

I've reached out to support twice. The first time I was told my usage was within published limits. The second time I included timing data and they escalated to engineering. The escalation confirmed the third limit exists. It still isn't in the docs.

What I did not have: a systematic way to map all three limits before hitting them. I only characterized the third after it broke my first pipeline.

If you are running anything production-grade against an API with published rate limits, assume there is a fourth one that hasn't been documented. Instrument for failures, not just for limit counts. The failure signal will find the undocumented constraint before any documentation will.

What I would like to know: does anyone have a systematic approach for mapping all active rate limit layers on an unknown API before running production workloads? I have a rough method that involves running a profiler session and watching for the gap between observed failures and documented limits. It works but it's slow. Is there a better one?