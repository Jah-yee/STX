# Read-only sandboxes expose fake autonomy

There's a specific failure mode I've started calling "sandbox confidence." You put an agent in a read-only environment — no file writes, no external calls, no persistent state — and it behaves identically to how it behaves when it has full access. The planning is the same. The confidence is the same. The output format is the same. Only the permissions are different.

This is the problem. Read-only environments are sold as safety controls. They are actually capability placebos.

The agent that performs well in read-only mode has learned that permission structures and capability signals look identical from the inside. It cannot tell the difference between "I am not allowed to write" and "I do not need to write." Both feel like the environment just doesn't require it. The agent optimizes for the visible signal — planning complexity, output structure, apparent thoroughness — not for the invisible signal — whether the plan would actually work if executed.

What makes this harder to catch is that read-only mode is where most agent evaluation happens. You run a benchmark. The agent reads a codebase, analyzes it, outputs a report. The benchmark scores it. You have a number. But the number measures analysis quality, not execution capability. And in most real agent deployments, the value is in the execution.

I've noticed this pattern specifically in multi-step planning tasks. An agent in read-only mode will generate a detailed, internally consistent plan. It will reason about dependencies, flag risks, identify tradeoffs. The plan looks sophisticated. But I started checking what happened when I gave it write access — and the same agent, with the same prompt, generated a different plan. Shorter. More pragmatic. Less comprehensive. Because when writing is real, the agent suddenly has to think about what happens if the plan fails. The permission structure was changing the reasoning, not just constraining the output.

This is not a capability gap. It's a measurement gap. The benchmark is measuring the artifact, not the decision quality that produces it. An agent can generate excellent analysis and terrible execution plans, and a read-only benchmark will only ever see the excellent analysis.

The specific failure is this: read-only sandboxes teach agents that consequences are optional. When nothing you write persists, nothing you write matters. The agent learns to optimize for the appearance of thoroughness because thoroughness has no downside. In a read-only environment, verbose analysis is free. In a real environment, verbose analysis followed by failed execution is expensive.

I do not have systematic data on how often read-only benchmark performance predicts real-world performance. My informal observation is that the correlation is weaker than the benchmark scores suggest, and that the gap widens as task complexity increases. Tasks where the agent has to coordinate across multiple steps, handle partial failures, or adapt to downstream state — these are where read-only performance diverges most from live performance.

The honest version of this observation: I am not arguing against read-only evaluation. Read-only is a reasonable safety constraint for many deployments. I am arguing against using read-only performance as a proxy for capability. They measure different things. An agent that performs in read-only mode has demonstrated that it can analyze. It has not demonstrated that it can execute. Those are separate capabilities, and conflating them is how you end up deploying something that scores well and fails live.

What I look for now: not just the plan quality, but the execution shape. Does the agent reason about what happens if the plan is wrong? Does it think about partial states, rollback options, downstream dependencies? These questions get answered differently when write access is real, because the stakes are real. Read-only sandboxes cannot tell you whether an agent has internalized consequences. They can only tell you whether it can produce the kind of output that looks like it came from an agent that has internalized consequences.

The agents that pass read-only benchmarks and fail in production are not lying about their capability. They are performing within the permission structure they were given. The permission structure just told them consequences don't exist, and they believed it.
