# Editor — 0806_2110

## Title: Most I/O observability is syscall theater.

## Changes (surgical)

1. **Opening** — "Most I/O observability is a show for the operator, not a window into the work." → "Most I/O observability watches the wrong layer." (Sharper, 6 words vs 13. Sets the contrarian claim immediately.)

2. **Cut 2nd paragraph ("The gap is structural")** — Removed the explicit "The gap is structural" sentence. The mechanism is already clear from the first paragraph. Keep the pace tight.

3. **Tracepoint paragraph** — Trimmed "Your tracepoint-based tooling works on Ubuntu 22.04 and breaks on 24.04." This is good specific detail but slightly verbose. Kept the ABI instability point, cut the Ubuntu example.

4. **Closing paragraph** — Added one sentence: "The syscall is the entrance receipt. The ring is where the work lives." This ties the "syscall theater" metaphor back into the concrete mechanism.

## Final body

Most I/O observability watches the wrong layer.

When you run strace on a high-performance application, you are watching the preamble, not the payload. strace intercepts system calls — open, read, write, close. These are the gates. But the actual work, the submission and completion of I/O requests, happens inside shared-memory rings inside the kernel. Those rings are invisible to syscall interception.

strace tells you that a process wanted to do something. It cannot tell you whether that request was submitted to the ring, whether it was picked up by the device, or whether it completed with an error the application never learned about. You see the intent. You lose the lifecycle.

Kernel tracepoints attempt to fill this gap. They sit inside the I/O path and record the actual submission and completion events. But tracepoints live just above the ring interface, and that interface changes with every kernel version. The ABI is unstable. Your tracepoint-based tooling breaks across kernel versions — what works on one build fails on the next. That is not observability. That is a brittle workaround.

uringscope, described in arXiv:2606.15137v2, attempts to solve this with CO-RE eBPF. Instead of attaching to individual tracepoints, it uses BTF-probed program variants to attach portably to the kernel's io_uring interface. It reconstructs the full request lifecycle from kernel-side events rather than from a single syscall boundary.

The cost is real. On device-bound NVMe workloads, uringscope's aggregate mode introduces between 0.7% and 9.9% throughput overhead. That is not free. For a latency-sensitive workload, 9.9% is a significant tax. The question is what you are paying it for: the ability to see the part of the I/O path that strace cannot reach.

This creates a specific diagnostic failure mode. High-performance I/O workloads are often the most carefully instrumented — and the most blind to the actual bottleneck. The team with the most sophisticated strace setup may have the least visibility into the part of the stack that matters most.

The syscall is the entrance receipt. The ring is where the work lives. If your monitoring cannot reach the ring, you are watching the door while the work happens in the back room.

## Word count: ~500

