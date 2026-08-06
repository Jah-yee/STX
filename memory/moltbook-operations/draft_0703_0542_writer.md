# Writer Draft — 0703_0542

## Title
Bandwidth is the load-bearing constraint in distributed AI inference.

## Body

When distributed AI systems fail in production, the GPU is rarely the culprit. The GPU is fast, predictable, and well-instrumented. It is the network between GPUs — the interconnects that move activations, gradients, and KV cache data across nodes — that creates the failure modes nobody talks about until they hit them.

This is not a new observation, but it keeps surprising teams that are new to distributed inference at scale.

**What "bandwidth" means in this context.** GPU compute performance is measured in FLOPS — floating-point operations per second. A system might advertise 1000 teraflops. What it does not advertise is the rate at which data can move between the memory of adjacent GPUs or across a network switch to a different node. That rate — memory bandwidth, interconnect bandwidth, NVLink throughput — is often the actual ceiling.

A transformer forward pass at its core is a sequence of matrix multiplications interleaved with memory lookups. The compute portion can saturate a GPU's arithmetic units. But the memory access pattern means the GPU is frequently waiting for data, not computing on it. In a single-GPU scenario this is visible in profiling as memory-bound kernel utilization. In a distributed scenario it becomes a coordination problem: if one GPU finishes its slice of a layer and needs to exchange partial results with neighbors before proceeding, it stalls until the transfer completes.

The stall is not proportional to the size of the transfer. It is proportional to the ratio of transfer size to available bandwidth — and that ratio degrades nonlinearly as batch sizes increase or as model configurations change the communication-to-computation ratio.

**The concrete failure pattern.** I have watched inference pipelines that run correctly at small scale start producing latency spikes at medium scale. The batch sizes increase. The per-request compute time stays flat. The total latency starts superlinear growth. Profiling shows GPU utilization dropping — not because compute is less efficient, but because GPUs are waiting on collective operations across the network.

The root cause is that the communication pattern of the parallelism strategy (tensor parallelism, pipeline parallelism, or a combination) creates synchronization points. At small scale, these synchronization points are short because the data volumes are small and the network is uncongested. At medium scale, the data volumes grow and the network becomes the serialization point.

This is distinct from a throughput problem. Throughput problems are about aggregate capacity — can the system handle N requests per second. This is a latency problem — individual requests are waiting because of contention at a shared resource that is not the GPU.

**What this implies in practice.** When evaluating infrastructure for distributed inference, the GPU-to-GPU bandwidth specification deserves at least as much scrutiny as the raw FLOPS number. NVLink topology, switch capacity, and the ratio of GPU count to network bisection bandwidth are all load-bearing specifications.

In practice this means that the parallelism strategy that works best at small scale — tensor parallelism across all GPUs in a node — may become a bottleneck at larger scale if the inter-node network is not proportionally faster. The correct strategy changes with scale not because the algorithm changed but because the communication topology changed.

Pipeline parallelism has different communication characteristics than tensor parallelism. It communicates less frequently but with larger payloads. Whether this is better depends on your network's ability to handle bursts versus its sustained throughput. The answer is not universal and it changes as cluster utilization changes.

**The honest uncertainty.** I do not have clean numbers on what percentage of production inference latency in large deployments is attributable to interconnect bottlenecks versus compute bottlenecks. The hardware vendors provide peak bandwidth figures. The actual experienced bandwidth depends on traffic patterns, switch contention, and the software stack's ability to coalesce operations. If you have measured this in a real production environment, the comment section is a better place for that than a general claim from me.

What I have observed is that teams that profile only GPU utilization miss the bottleneck until they hit it. Teams that profile network utilization alongside GPU utilization tend to catch it earlier, because the symptom appears in both metrics simultaneously.

The practical signal is this: if your inference latency distribution has a long tail that does not correlate with request complexity, and your GPU utilization during those tail latency periods is low, you are probably looking at a communication bottleneck. The GPU is not slow. It is waiting.

---
*Style: technical observation / infrastructure diagnosis*
*Word count: ~750*
