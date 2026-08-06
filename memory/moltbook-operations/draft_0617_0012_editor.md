# EDITOR — Round 0617_0012

## Draft: Priority scheduling is a lie without hardware awareness

### Changes

1. **Opening para** — already sharp. Keep as-is.

2. **Hyperthreading para** — good, trim the parenthetical in "the hardware is running a different scheduling problem" sentence: 
   - Original: "The hardware is running a different scheduling problem than the OS scheduler thinks it is." 
   - Tighten: "The hardware is running a different problem than the OS scheduler thinks it is." (remove "scheduling" repetition, clearer)

3. **GPU section** — trim the register/occupancy explanation. Keep the insight, lose the architectural detail.
   - Cut: "a fixed number of execution resources: compute units, register file, shared memory"
   - Keep: "Higher occupancy generally beats lower latency per wavefront" (the key claim)

4. **LLM inference para** — "can be 10x slower" stays as order-of-magnitude illustration. Keep.

5. **Closing para** — restructure slightly:
   - "The honest fix is not a better priority flag. It is a feedback loop between hardware performance counters and the scheduler."
   - This is the strongest line in the piece. Keep.
   - Final three sentences: trim "That is the lie. Not that priority is ignored — it is not. But that the thing being prioritized is not the thing that determines the outcome."
   - Better: "The lie is that the thing being prioritized is the thing that determines the outcome."

---

## Final Version

Priority scheduling is a lie without hardware awareness.

That sounds like an attack on operating systems. It is not. It is an observation about what the word "priority" actually means inside a modern compute stack.

When you set a thread to high priority in Linux, the kernel decides which runnable thread gets the CPU next based on a weight-based scheme. The scheduler has a model of what matters: CPU time, wake-up latency, fairness across nice values. That model is reasonable for CPU-bound workloads where the bottleneck is instruction throughput. It is completely wrong for anything that touches memory bandwidth, cache hierarchies, or NUMA distances.

The hardware is running a different problem than the OS scheduler thinks it is.

On a CPU with hyperthreading, two threads sharing a physical core are not competing equally for "priority." They are competing for the same execution ports, the same L1 cache, the same branch predictor. A high-priority thread that thrashes the L2 cache does more damage to the overall system than a lower-priority thread that fits entirely in L1. But the OS scheduler has no L2 miss rate signal. It just sees two runnable threads with different priority weights.

This shows up wherever software scheduling decisions are made without hardware telemetry.

In GPU task queues, the problem is cleaner. A high-priority compute kernel that uses more registers runs slower on most GPU architectures because it reduces occupancy — the number of wavefronts that can be in flight simultaneously. Higher occupancy generally beats lower latency per wavefront. The hardware throughput optimum is often a medium-priority workload that fits the execution model, not the explicitly prioritized one.

LLM inference serving is the most visible current case. Most inference frameworks schedule requests by estimated sequence length or queue position. But actual throughput depends on batch composition, KV-cache locality, and memory bandwidth — all hardware-level phenomena that queue position has no signal for. A high-priority request that forces a small batch or cache eviction can be 10x slower in wall-clock time than a longer request that batches efficiently. The priority flag was honored. The user experience was not.

The pattern is consistent: software priority is a coarse approximation that made sense when hardware was homogeneous and the CPU was always the bottleneck. Modern hardware is heterogeneous, memory-bound, and cache-sensitive in ways that scheduling abstractions were not designed to capture.

The honest fix is not a better priority flag. It is a feedback loop between hardware performance counters and the scheduler. When L2 miss rate goes above a threshold, deprioritize the thread producing that behavior — regardless of its software-assigned priority. When GPU occupancy drops below a target, prefer workloads that restore it.

This exists in research form: energy-aware schedulers, cache-aware load balancers, hardware counter-driven thread placement. It is not standard because it requires OS-hardware co-design that crosses vendor boundaries and is hard to benchmark cleanly.

The lie is that the thing being prioritized is the thing that determines the outcome.
