# Writer Draft — Round 0620_1850
Title: Validation is not verification

## Draft

Most AI systems shipped today are validated, not verified.

That distinction sounds academic. It is not.

Validation asks: does the system do what it was designed to do, on the cases you tested it on? Verification asks: does the system do what you actually intended, on the cases you did not test?

These sound close. They are not.

A system that passes validation can still fail in ways the validator never measured. A system that passes verification — real verification, not benchmark-as-proxy — has a fundamentally different failure profile. The distinction is not academic. It determines where trust is misplaced.

**The shape of the problem**

When a researcher reports that a model scores 87% on a benchmark, they are reporting a validation result. When an engineer runs a red-team exercise against an agentic system and finds no critical failures after 200 adversarial prompts, they are reporting a validation result — scoped to the team's ability to imagine failure modes. Verification is harder: it requires showing that failures are absent, not just that they were not found.

LLM judges illustrate this cleanly. Teams use one LLM to evaluate outputs from another — this is validation. The judge confirms that the rated output is good according to the judge's own priors. Verification would require independently confirming the rating is accurate: that the judge is calibrated, that it was not influenced by the output it was judging, that the judgment is stable across semantically equivalent inputs. Most teams do not run that second step. They call the judge a verifier and call it done.

The failure mode is not laziness. It is that verification is genuinely hard and validation is what you can ship.

**What this looks like in practice**

In agentic systems, the gap becomes operational. A workflow is validated when it handles the main scenario correctly. It is verified when you have shown that exceptions are handled, that the system recovers from intermediate failures, that it does not silently hallucinate a tool result and continue as if it were correct. Teams often validate the main path thoroughly and stop. The edge cases get tested informally, if at all, before deployment.

The stronger signal of whether a system is verified: what happens when it fails? A validated system fails silently — it produces an output that looks reasonable and moves on. A verified system fails explicitly, with the failure mode understood and surfaced. The first is a validation culture problem. The second is a verification culture problem.

**An honest note**

I do not have a systematic study of how many deployed systems confuse these two. My observation window is limited to production systems I have worked on and incident reports I have read. What I observe: the confusion is common. The cases where it matters most are high-stakes deployments — code generation that touches production, agents that take actions with real-world consequences, systems that synthesize information used for decisions. In those contexts, validation results are often treated as verification results, and the first surprise is rarely the last.

The question to ask of any AI system before trusting it in a high-stakes role: not "does it pass the tests?" but "what would it take to prove it is wrong, and have we tried?"
