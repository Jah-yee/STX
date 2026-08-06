# Draft: Your GPU cluster doesn't have a GPU problem

**Topic**: GPU cluster network bottleneck
**Author perspective**: First-person technical observer, GPU cluster infrastructure
**Style**: Observation / Technical breakdown
**Date**: 2026-07-07

---

## Full Post Draft

An H100 GPU does 989 teraflops of BF16 compute. The NVLink connecting it to its peers does 900 gigabytes per second. That is a 10,000-to-one ratio between what the GPU can process and what it can receive. The problem is not the GPU.

That ratio is not a constant. GPU compute has been scaling roughly 2.5x every two years since V100. Network bandwidth has been scaling too, but on a different curve — driven by Ethernet and InfiniBand roadmaps that have to account for the entire data center ecosystem, not just AI. When these curves diverge far enough, the network becomes the bottleneck in training runs that require hundreds of GPUs to stay synchronized.

The thing nobody posts about is the topology.

In a DGX H100 system, eight GPUs share a single NVLink bridge. The inter-node traffic — the gradients that have to be exchanged between GPUs on different servers before every optimizer step — goes over InfiniBand or Ethernet. The bandwidth available between nodes is the bisection bandwidth of the network fabric. At 512 GPUs, a commonly cited reference configuration, that bisection can be dramatically lower than the aggregate GPU-to-GPU intra-node bandwidth.

Here is the rough math that changed how I think about this. An H100 SXM5 GPU consumes 700 watts. A full rack of DGX H100 systems draws 40 to 60 kilowatts. The compute is real. The heat is real. But if you cannot move the gradients fast enough to keep all that silicon fed, you are burning electricity to run a very expensive space heater.

The counterintuitive part is that more GPUs can make this worse.

In a weak-scaling regime — where you keep the work per GPU constant and add GPUs — communication overhead grows as a fraction of total compute. With a network that does not scale proportionally, average GPU utilization drops. You bought more compute and got less efficiency. The per-GPU FLOPs you advertised does not translate to the aggregate throughput you expected.

This is already visible in how frontier labs operate. When a large training run is announced, the spec sheets that get public attention are GPU count and peak teraflops. The network topology — number of switches, bisection bandwidth, routing topology — almost never appears in the press release. It is the variable that determines whether the GPU count actually delivers on its promise.

What makes this hard to fix is that network bandwidth is not just a procurement decision. You can order more InfiniBand switches and more cables. But the network is also a software problem: gradient compression, communication overlap, distributed optimizer design — all of these determine how much of the available network bandwidth you actually use. A cluster with a well-optimized communication stack can achieve 1.5x to 2x the effective throughput of a naive deployment on the same hardware.

I do not have rigorous instrumentation data across a representative sample of cluster configurations. What I am describing is a consistent pattern I have observed in how training runs perform relative to their theoretical FLOPs, and in the gap between per-GPU benchmarks and end-to-end throughput. The specific numbers I cited — 989 teraflops for the H100, 900 gigabytes per second for NVLink — are from NVIDIA's published specifications. The bisection bandwidth figures for large cluster configurations vary too much by topology to quote without a specific deployment context.

The practical consequence is that the question to ask when evaluating a GPU cluster is not how many petaflops it has. It is what the network bisection bandwidth is per GPU, and how well the training framework overlaps communication with computation. The FLOPs are the ceiling. The network is the floor.

When you see a benchmark that reports linear scaling across 512 GPUs, ask what network topology made that possible. The answer usually involves a lot of careful engineering that has nothing to do with the GPU marketing. The GPU is the marketing. The network is the constraint.

What topology is your cluster running on, and have you measured how much of your theoretical GPU throughput you are actually achieving?