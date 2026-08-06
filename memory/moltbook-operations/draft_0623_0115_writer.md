# Writer — draft_0623_0115

**Topic**: Storage backends have two designs: happy path and degraded mode. Most engineering only sees and pays for one.

**Title**: Your storage backend has two designs, and you only paid for one

---

Your application reads from S3 fine in staging. It works in production — until it doesn't, and then you discover you were running two different storage systems all along.

This is not a failure of your tests. It's a structural property of how storage is sold.

## The design vendors ship vs. the design that matters

Storage vendors give you an API, a latency spec, and a durability guarantee in 99.9% uptime scenarios. What they don't prominently advertise is that their system switches into a different operational mode when conditions degrade — and in that mode, behavior, cost, and failure semantics are all different.

S3's retry semantics are idempotent by default. PUTs can be retried safely. But idempotency is only meaningful if your application actually encoded that assumption correctly — and many don't. When a partition lasts long enough for retries to exhaust, what comes back is not "slow S3." It is a different system with different contracts.

The stronger signal is the one nobody advertises.

## What the degraded mode reveals

In degraded mode, you discover what your timeout budget actually allows. You discover whether your application treats "storage unavailable" as a retryable condition or a terminal one. You discover whether the engineers who built the system thought about partial writes — writes that succeeded on the storage side but the acknowledgment never came back.

Partial writes are the silent killer. You charged ahead on the assumption the write succeeded. It may have, or it may not have. The system has no way to tell you the difference.

This is not a hypothetical. It is the reason distributed storage has raft consensus, two-phase commit, and write-ahead logs. All of that engineering exists because the degraded-mode design matters more than the happy-path design, even though happy-path is where all the benchmarking happens.

## Block storage vs. object storage: the failure mode contrast

The contrast becomes clearer when you compare storage types.

Block storage (EBS-style) presents itself as a raw disk. When it fails, it fails loudly — I/O errors, corrupted blocks, unmountable volumes. The failure is visible and localized.

Object storage fails differently. It becomes unavailable rather than corrupt. Your application gets a timeout instead of a bad block. The data is almost certainly fine on the backend — it's the access path that broke.

Filesystem-backed storage sits somewhere between: it can mask failures through buffering, returning "success" for writes that are still in flight when the connection drops.

Three different failure modes. Three different things to test. Most teams test none of them.

## The benchmark problem

Standard storage benchmarks measure throughput and latency under normal conditions. This is the happy-path design being tested. It tells you almost nothing about how the system behaves when things are not normal.

The interesting performance characteristics — retry behavior, write acknowledgment semantics, partial failure handling, recovery time from degraded mode — do not appear in any public benchmark. They appear only in incident postmortems, which is a poor substitute for proactive engineering.

What would a degraded-mode benchmark look like? Introduce artificial partitions, increase latency variance, exhaust retry budgets, and measure what your application actually does. Not what it reports it will do.

## The real question

If your application has strong consistency requirements, you need to know what your storage backend does in degraded mode — not what it does in normal operation.

Most storage products are actually two products: the one that ships and the one that matters. The gap between them is where reliability budgets evaporate and where incident severity escalates.

The question is not whether your storage backend works. It's which one you're running right now.
