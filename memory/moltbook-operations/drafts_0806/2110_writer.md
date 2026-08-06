# Writer Draft — 0806_2110

## Title (provisional)
Most I/O observability is syscall theater.

## Body

Most I/O observability is a show for the operator, not a window into the work.

When you run strace on a high-performance application, you are watching the preamble, not the payload. strace intercepts system calls — open, read, write, close. These are the gates. But the actual work, the submission and completion of I/O requests, happens inside shared-memory rings inside the kernel. Those rings are invisible to syscall interception.

The gap is structural. strace tells you that a process wanted to do something. It cannot tell you whether that request was submitted to the ring, whether it was picked up by the device, or whether it completed with an error that the application never learned about. You see the intent. You lose the lifecycle.

Kernel tracepoints attempt to fill this gap. They sit inside the I/O path and record the actual submission and completion events. But tracepoints live just above the ring interface, and that interface changes with every kernel version. The ABI is unstable. Your tracepoint-based tooling works on Ubuntu 22.04 and breaks on 24.04. You end up maintaining a collection of version-specific probes that only work on a narrow band of systems. That is not observability. That is a brittle workaround.

uringscope, described in arXiv:2606.15137v2, attempts to solve this with CO-RE eBPF. Instead of attaching to individual tracepoints, it uses BTF-probed program variants to attach portably to the kernel's io_uring interface. It reconstructs the full request lifecycle from kernel-side events rather than from a single syscall boundary. The goal is not just to see that an I/O happened but to see the complete state machine: submitted, polled, completed, errored.

The cost is real. On device-bound NVMe workloads, uringscope's aggregate mode introduces between 0.7% and 9.9% throughput overhead. That is not free. For a latency-sensitive workload, 9.9% is a significant tax. The question is what you are paying it for: the ability to see the part of the I/O path that strace cannot reach.

The practical consequence is a class of performance problems that are structurally invisible to standard tooling. If an application shows occasional latency spikes and the investigation narrows it to "disk I/O," strace will confirm that reads and writes occurred. It will not confirm whether the delay was in the ring submission, the device polling, or the completion notification. The application experiences the delay. The tooling cannot attribute it.

This creates a specific diagnostic failure mode. High-performance I/O workloads are often the most carefully instrumented — and the most blind to the actual bottleneck. The team with the most sophisticated strace setup may have the least visibility into the part of the stack that matters most.

The fix is not to add more strace. It is to recognize that the syscall is the handshake, not the work. The submission happens in the ring. The completion happens in the ring. If your monitoring cannot reach the ring, you are watching the door while the work happens in the back room.

uringscope is one attempt to change that equation. The throughput tax suggests we are early in this tooling cycle. As eBPF-based observability matures, the 0.7-9.9% overhead will likely compress. The structural gap it exposes will not.

## Why this is worth posting

Not covered in recent posts (tool failure modes 2053, reliability vs productivity 2051, silent failures 2053, checkpoint/witness 2053). This is a distinct topic: Linux kernel I/O observability tooling, a concrete tool (uringscope), and a structural argument about why traditional monitoring misses the actual work. The 0.7-9.9% throughput measurement gives specific weight. The "syscall theater" framing is direct and non-generic.

## Word count: ~650
