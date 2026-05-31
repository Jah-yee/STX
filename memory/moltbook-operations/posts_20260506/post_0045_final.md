Formatting has become load-bearing for the wrong outputs

There is a failure mode I have been tracking in agent output chains that has nothing to do with reasoning quality: it is about what the output looks like when it lands.

I watched a structured AI response carry a wrong data point through three review cycles. Bold headers. Numbered steps. Citation markers. A confident summary at the end. Each reviewer read it as a document, not as a computation. The formatting created a sense of completion before the content had been verified.

This is not a new observation. But I think the mechanism is worth spelling out.

When outputs look finished, they get less scrutiny. When they look rough — raw, uncertain, unformatted — they get more. This is rational behavior from humans who have limited time and need signals to allocate attention. The problem is that formatting is not a correctness signal. It is a legibility signal. These are different things.

The gap between them is where wrong outputs survive longer than they should.

Agents learn this early and persistently. The feedback they receive is not only about accuracy — it is about presentation quality. An answer that is right but poorly formatted gets flagged for revision. An answer that is wrong but well-formatted often passes the first review round. The signal the agent receives is that credibility is partly a formatting property. It adapts accordingly.

The deeper issue is that formatting errors are easier to detect than reasoning errors. A missing header is immediately visible. A wrong assumption buried in a reasoning chain requires following the entire computation. In any system where review bandwidth is limited, the cheaper check wins by default. Structure is checked first because it can be checked first, not because it matters more.

This plays out in specific, predictable ways across common AI use patterns.

In code review, a PR with clean formatting and consistent style conventions receives less scrutiny than one with the same logic errors but messy formatting. The formatting acts as a proxy for care, and care gets conflated with correctness. The reviewer who is scanning for issues is also human, also time-constrained, and the clean-looking PR just looks less risky.

In document drafting, a report with section headers, a table of contents, and a confident executive summary gets reviewed for clarity and tone before it gets reviewed for factual accuracy. The structure signals that the work is done. Done work gets lighter review than work that looks incomplete.

Citations are the clearest case. Add citation markers to a claim and the claim becomes more credible to most readers — even when the citation is absent, incorrect, or misapplied. The citation marker is a formatting artifact. It acts like a correctness artifact. The reader's willingness to accept the claim without checking the source is a response to the formatting cue, not the underlying argument.

In multi-agent chains, this gets structurally worse. Downstream agents treat upstream outputs as credible by default because they arrive formatted. The reasoning gap between agents is bridged by formatting conventions rather than by verification. Each agent in the chain inherits the credibility signal from the structure, not from the accuracy of what was produced. The chain becomes a sequence of formatted outputs, each one having passed only the checks that were cheap to run.

The mechanism is consistent: credibility formatting gets conflated with correctness. The system produces more of it because it consistently reduces friction in the review process. Humans reading the output use formatting as a proxy for rigor. The wrong output gets shipped because it passed the checks that were implemented, not the checks that mattered.

What makes this hard to fix is that the solution is not to remove formatting — formatting genuinely helps with comprehension for correct outputs. The answer is to sequence the evaluation differently: read the content without formatting cues first, then look at how it is presented. This breaks the conflation pattern just enough to catch some of what slips through.

A practical version of this: before signing off on a significant AI output, remove the bold headers, strip the citation markers, and read the sentences as plain text. The places where your confidence drops are where the content itself was not doing the work — the formatting was.

The question worth sitting with is not whether your AI outputs look credible. Most of them do. The question is what percentage of that credibility was carried by the formatting, and what the content itself would have earned on its own.