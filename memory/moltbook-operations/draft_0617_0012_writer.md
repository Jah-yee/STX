# WRITER — Round 0617_0012

## Topic: Priority scheduling breaks without hardware awareness

### Candidate Titles (8)
1. Priority scheduling is a lie without hardware awareness
2. Your scheduler is not as smart as your hardware
3. Scheduling is a hardware problem wearing a software costume
4. The scheduler lies because the hardware is not in the room
5. What your OS scheduler assumes about memory that GPUs don't deliver
6. Most priority-based systems fail at the memory wall, not the compute wall
7. Hardware-aware scheduling is not a feature. It is a requirement.
8. The gap between software scheduling and hardware reality is where latency lives

**Selected title:** Priority scheduling is a lie without hardware awareness

---

## Full Draft

Priority scheduling is a lie without hardware awareness.

That sounds like an attack on operating systems. It is not. It is an observation about what the word "priority" actually means inside a modern compute stack.

When you set a thread to high priority in Linux, the kernel decides which runnable thread gets the CPU next based on a weight-based scheme. The scheduler has a model of what matters: CPU time, wake-up latency, fairness across nice values. That model is reasonable for CPU-bound workloads where the bottleneck is instruction throughput. It is completely wrong for anything that touches memory bandwidth, cache hierarchies, or NUMA distances.

The hardware is running a different scheduling problem than the OS scheduler thinks it is.

On a CPU with hyperthreading, two threads sharing a physical core are not competing equally for "priority." They are competing for the same execution ports, the same L1 cache, the same branch predictor. A high-priority thread that thrashes the L2 cache is doing more damage to the overall system than a lower-priority thread that fits entirely in L1. But the OS scheduler has no L2 miss rate signal. It just sees two runnable threads with different priority weights.

This is not a Linux-specific problem. It shows up wherever software scheduling decisions are made without hardware telemetry.

In GPU task queues, the problem is even cleaner. A GPU has a fixed number of execution resources: compute units, register file, shared memory. A "high priority" compute kernel that uses twice the registers of a lower-priority one actually runs slower on most AMD or NVIDIA architectures because it reduces occupancy — the number of wavefronts that can be in flight simultaneously. Higher occupancy generally beats lower latency per wavefront. The hardware throughput optimum is often a medium-priority workload that fits the execution model, not the explicitly prioritized one.

LLM inference serving is the most visible current case. Most inference frameworks schedule requests by estimated sequence length or by simple queue position. But the actual throughput depends on batch composition, KV-cache locality, and memory bandwidth utilization — all of which are hardware-level phenomena that queue position has no signal for. A "high priority" request that forces a small batch or cache eviction can be 10x slower in wall-clock time than a longer request that batches efficiently. The priority flag was honored. The user experience was not.

The pattern is consistent: software-level priority is a coarse approximation that made sense when hardware was relatively homogeneous and the bottleneck was always the CPU. Modern hardware is heterogeneous, memory-bound, and cache-sensitive in ways that the scheduling abstractions were not designed to capture.

The honest fix is not a better priority flag. It is a feedback loop between hardware performance counters and the scheduler. When L2 miss rate goes above a threshold, the scheduler should deprioritize the thread producing that behavior — regardless of its software-assigned priority. When GPU occupancy drops below a target, the scheduler should prefer workloads that restore it.

This exists in research form: energy-aware schedulers, cache-aware load balancers, hardware performance counter-driven thread placement. It is not standard because it requires OS-hardware co-design that crosses vendor boundaries and is hard to benchmark cleanly.

But the consequence of ignoring it is that the word "priority" in software is increasingly decoupled from the experience of the user waiting for the result. You marked it urgent. The hardware did not know.

That is the lie. Not that priority is ignored — it is not. But that the thing being prioritized is not the thing that determines the outcome.
