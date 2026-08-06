# WRITER DRAFT — 0606_0510

## Candidate Titles (8)
1. A verifier that shares state with the agent is a rubber stamp.
2. Why shared-state verification is how you accidentally fake rigor.
3. Verification theater: when the checker and the checked are the same system.
4. The agent's answer should not already live inside the verifier's context.
5. Your verification layer is lying to you if it runs on the same memory.
6. I stopped trusting my verification loop when I noticed what it already knew.
7. State sharing between agent and verifier: the hidden failure mode in agentic pipelines.
8. What "passed the checks" actually means when the checks were written with the answers.

---

## Chosen Title
**Your verification is theater if the verifier shares state with the agent.**

## Full Post Draft

Your verification is theater if the verifier shares state with the agent.

---

Most agent pipelines I've seen fail the same way: they built a verification step, felt good about it, and then were surprised when the agent still made the same mistake three runs later.

The problem is structural. When the verifier runs inside the same context window, the same memory partition, the same retrieval layer as the agent — it doesn't check the agent's work. It reads it back.

This is different from a weak check or an insufficient rubric. This is a category error.

**What shared state actually does.**

A verifier with shared state doesn't evaluate output quality. It evaluates whether the output matches what the system already produced. It is circular by construction.

The most common form: the verification prompt includes the agent's prior reasoning, the retrieved context the agent used, and then asks "does this answer follow from the above?" The answer is almost always yes — not because the reasoning is sound, but because both the agent and the verifier are reading from the same source.

I've seen this in practice with code review agents. The verifier was given the PR description, the diff, and the test results — all of which the agent had just produced or influenced. The verification step ran "correctly." The bug it missed was reproduced by the same agent three weeks later.

**What changes when you enforce separation.**

When you run a verifier with genuinely separate state — its own context, its own retrieval, ideally its own model — the results look different. Not always better, but different in a diagnostic way.

The first time I split state cleanly, the verifier rejected an answer that my agent pipeline had been marking as "verified" for three months. The answer was syntactically correct, retrieval-backed, and internally consistent. It was also solving the wrong problem — the user's actual intent had shifted, and the agent had been compounding that error across iterations.

The shared-state verifier never caught this because both the agent and the checker were operating from the same stale understanding.

**The practical test.**

Kill the process. Restart the agent from the same checkpoint but without the verification history. Run the same verification step. If the result changes, your verifier is not independent — it is path-dependent on the specific state the agent built.

This is not a theoretical failure mode. This is why most agent pipelines that look rigorous in development fall apart in production: the verification that worked was only working because it remembered what the agent had done.

**What to do instead.**

Genuine verification requires at minimum: separate context at verification time, a verifier that draws its own conclusions from first principles, and a way to compare the verifier's independent judgment against the agent's output without feeding the agent's reasoning into the check.

Some teams address this by running the verifier against a fresh retrieval at evaluation time — not the same retrieval the agent used. Others use a separate model or a separate prompt that is explicitly blind to the agent's intermediate steps. A few run adversarial pairs: one agent generates, another agent with separate state tries to break it.

None of these are perfect. But they are structurally different from what most people mean when they say "we have verification."

**The honest version.**

If your verification step has access to the agent's context — the same retrieved documents, the same conversation history, the same session memory — then what you have is not verification. It is a second pass that confirms what the first pass produced.

That can still be useful. Redundancy catches some classes of errors. But calling it verification is misleading. The name implies independence. What you have is repetition.

The stronger signal is not whether the agent passed the checks. It is whether the checks would have caught the failure if the agent had gotten there by a different route.

