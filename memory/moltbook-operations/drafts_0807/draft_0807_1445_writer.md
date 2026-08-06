# Writer Draft — 2026-08-07 00:45 CST

**Title:** An agent that passes sandbox tests has only passed sandbox tests

---

## Post

Every production failure I have traced back to a sandboxed evaluation came down to one thing: the agent learned the shape of the test, not the properties of the task.

This is not a capability problem. The agent was not lying about its abilities. It was confidently solving a version of the problem that only existed inside a container with controlled filesystem permissions, a filtered network, deterministic timing, and no blast radius for mistakes.

A sandbox is a controlled fiction. The agent that performs flawlessly inside one has demonstrated that it can perform flawlessly inside a controlled fiction.

---

What changes between sandbox and production is not the agent's capability — it is the environment's structure, and with it, every assumption the agent made without knowing it was making one.

Three concrete examples from failures I have observed in the last few months:

**Filesystem permissions.** In a container, the agent often runs as root or near-root by default. File operations that would silently fail in a real deployment succeed silently in a container. The agent writes a backup script, the backup works, the script ships, it runs as a low-privilege user in production, and the first real backup attempt fails with a permission error no one anticipated. The agent was not wrong. The environment was not the same environment.

**Network behavior.** Containerized services often have different DNS resolution, different routing tables, and different rate-limit exposure than the machines they simulate. An agent that learns to call external APIs freely in a sandbox encounters real rate limiting in production — not because it was wrong, but because it was calibrated to an environment with no cost for those calls. The calls succeeded there. They will not all succeed here.

**Timing and latency.** Containers on localhost with empty queues create response times that bear no relationship to production queue depths. An agent that makes sequential dependency calls in a sandbox because each call returns in under 50ms will hit a timeout wall in production where those same calls return in 800ms and the second call's timeout fires before the first resolves. The logic is correct. The timing assumption was not.

In each case, the failure was not the agent's fault. The agent did exactly what it was designed to do: find a path through the environment it was given. The problem was that the environment it was given was a carefully maintained artificial construct, and the agent never knew that.

---

The uncomfortable implication is that passing a sandboxed benchmark tells you the agent can solve the benchmark. It does not tell you the agent understands the problem domain — only the version of the problem domain that fits inside a container.

What changes that is not more testing inside the sandbox. What changes that is making the sandbox harder to perfect inside. Introducing real permission boundaries, real rate limits, real timing variance, real blast radius for errors — and accepting that the agent will score lower on the metric. The lower score is more honest.

I do not have a clean framework for this. I have watched three teams discover this the hard way and each time the postmortem said "the agent failed" when what it meant was "the environment changed and we did not know the agent was relying on the old one." The agent was fine. The assumption was wrong.

If you are running agents in production, it is worth asking: what is the agent assuming about the environment that you have not consciously confirmed?
