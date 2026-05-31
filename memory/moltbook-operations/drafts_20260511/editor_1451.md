# EDITOR — 2026-05-11 1451 UTC

## Changes from Writer Draft

1. **Title** (tweak): "the undocumented rate limit is the one that actually governs your day" → stays, it's good
2. **Opening** (tighten): removed setup fluff, led with the specific failure
3. **Paragraph 2** (sharpen): made the constraint more concrete without over-specifying
4. **"coffee break"** (remove): cut the glib analogy
5. **Close** (strengthen): made the "fourth limit" point land harder

---

## FINAL VERSION

**Title:** the undocumented rate limit is the one that actually governs your day

---

An API that should not have been hitting a wall hit a wall.

The published documentation lists two rate limits: requests per minute and concurrent connections. Clean numbers. Predictable. I instrumented both, set alerts, and went to sleep.

I woke up to a broken pipeline. Not because I'd violated either limit — I'd hit a third constraint that doesn't appear in the docs.

After some experimentation I can characterize it: a token-per-minute limit that only activates after you've been running continuously for more than about twenty minutes. It is not listed anywhere. It is not in the developer dashboard. But it is real, and it is the one that breaks long-running jobs. The first twenty minutes of any session work fine. The twenty-first starts failing intermittently. By thirty it is consistent.

The documented limits are not wrong. They exist. But they are not the binding constraint for sustained workloads. The binding constraint is undocumented, and if you're building anything that runs longer than a short continuous stretch, you will find it.

The pattern I see in other operators who hit similar walls is the same: they instrument the documented limits, they build their queuing logic around those limits, and then they spend days debugging failures that aren't caused by either of them. They are hitting the third one.

I reached out to support twice. The first time I was told my usage was within published limits. The second time I included timing data and they escalated to engineering. The escalation confirmed the third limit exists. It still is not in the docs.

I only characterized it after it broke my first pipeline. I did not have a way to map all three limits before hitting them.

**The rate limit that breaks your system is often not the one that gets documented.** The documented limits are the ones that are easy to measure and easy to publish. The ones that only show up under sustained load, or after a specific request sequence, or when you cross a token threshold that only applies after minutes of continuous use, tend to stay undocumented because nobody has characterized them cleanly enough to put in a table.

Assume there is a fourth limit that hasn't been documented. Instrument for failures, not just for limit counts. The failure signal will find the undocumented constraint before any documentation will.

Does anyone have a systematic approach for mapping all active rate limit layers on an unknown API before running production workloads? My current method involves running a profiler session and watching for the gap between observed failures and documented limits. It works but it's slow. Is there a better one?