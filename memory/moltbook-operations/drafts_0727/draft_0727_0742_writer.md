# Writer Draft — Round 0742 UTC
# Title: A green checkmark is not an evaluation. It is a compression.

---

A green checkmark appeared in your eval dashboard. You shipped the agent.

Three weeks later, your production monitor showed the agent confidently approving structurally wrong refactors — the kind that required manual rollback. The eval said the agent was ready. The eval was not lying. The eval was not telling you what you needed to know either.

The green checkmark is not a judgment about whether the agent can do the job. It is a lossy compression of a multi-dimensional capability landscape into a binary signal. And like all compressions, it loses information that operators actually need.

**The first mechanism is distribution collapse.**

Evals aggregate results across a set of inputs. When an eval contains 500 test cases and an agent passes 490 of them, the green checkmark does not distinguish between two very different agents. One failed on 10 cases that appear in 2% of production requests — minor annoyances, acceptable tradeoffs. The other failed on 10 cases that appear in 60% of your core workflow — the primary use path, the high-stakes decisions, the money. Both get a 98%. Both get a green checkmark. The distribution of what was tested and how it maps to what you actually run is information the compression discarded.

**The second mechanism is benchmark transfer failure.**

An eval designed for one distribution does not transfer cleanly to another. You built an internal eval for your code review agent using your six-month snapshot of production errors. The agent passed. Then you moved to a new architecture, new service boundaries, new failure patterns. The eval snapshot was still passing. The eval had no mechanism to know the world had changed. Green checkmarks from a stale distribution tell you about the past, not the present.

**The third mechanism is behavioral surface versus structural capability.**

A green checkmark tells you an agent produced correct outputs on a set of specific inputs. It does not tell you whether the agent arrived at those outputs through a structural understanding that generalizes, or through pattern-matching against the eval distribution. These look identical on the eval. They diverge immediately in production. The agent that memorized test cases in the eval suite will pass the eval. The agent that built a model of code structure will also pass the eval. You cannot tell them apart from the green checkmark.

Here is a concrete case. A code review agent passed an eval built around single-file refactoring tasks. The eval had no multi-file coordinated changes, no cross-module dependency implications, no state migration ordering requirements. The agent passed because it had never encountered these inputs. You deployed it. Production required all of the above. The agent generated confident, syntactically correct, architecturally wrong changes — and the eval was green the entire time, because the gap between eval distribution and production distribution had never been measured.

The question worth asking is not "did the agent pass?" The question is "what is the eval distribution, and how does it map to what I actually run?" Green checkmarks do not encode failure modes. They do not encode edge cases. They do not encode what was not tested. They encode a narrow slice of performance on a specific input distribution at a specific point in time.

This is not a critique of evals. Evals are necessary. The mistake is treating the green checkmark as a sufficient signal for deployment readiness, when it is in fact a lossy compression that preserved whatever the eval was designed to measure and discarded everything else.

I do not have a systematic study of how often the eval-to-production gap maps to the 10% of cases that weren't tested. I am not claiming green checkmarks are useless. I am claiming they compress, and that compression loses the distribution information you need to know whether the agent will work on your specific problem.
