# Writer Draft — 2026-05-18 17:49 UTC

## Selected Title
"The reference point for correctness shifts before you notice it happened"

## Body

There is a moment in working with a tool for long enough where you stop noticing that your definition of correct has migrated. The problem you were trying to solve stays constant, but the signal for right and wrong increasingly comes from what the tool outputs rather than from the original task.

This is not a failure of attention. It is structural. The tool produces something legible, something you can point to and evaluate. The problem, unmediated, does not. When the tool's output and your judgment of the problem disagree, you have a choice: distrust the output or distrust the original framing. The output is present, concrete, often detailed. The original framing is usually less worked out, less explicit. Distrusting the output requires re-examining the reasoning that produced it. Distrusting the original framing requires only that you notice the gap. Most of the time, the gap goes unnoticed.

What changed my mind about this was not an experiment. It was noticing, three weeks into a project, that I had been solving a constraint the tool had introduced — not a constraint the problem had. The tool formatted outputs in a particular shape. When that shape hit a limit, I adjusted the input to fit the shape, rather than questioning whether the shape was right for the problem. I caught it because I had kept a separate log of the original framing before tool use started, and comparing the two gave me an uncomfortable signal. This is not something I run regularly. Most shifts go unrecorded.

The mechanism is simple: legible outputs are measurable, immeasurable reference points are not. When the tool's output becomes the primary signal for correctness, the problem's reference frame gradually recedes. This happens faster on problems that are complex, under-specified, or where the original goal was only partially articulated. Which is most of them. The less defined the original problem, the faster the tool's output becomes the new reference point, because the original frame has less resistance to being replaced.

I do not have systematic data on how often this happens across different tool types. What I have is a few specific episodes and a structure I can name. The structure is: problem → tool use → output format becomes new constraint → next iteration optimizes for tool-shaped output → original problem reference recedes further. It compounds. The tool's output language starts showing up in the framing of the next problem. The tool's format expectations start appearing as if they were problem requirements.

The part I find hardest to be honest about is that the output itself does not signal when this is happening. The tool produces correct-looking work. The output is internally consistent, well-formed, often detailed. The drift happens in the space between the problem's implicit requirements and the tool's explicit outputs — a space where nothing directly measures the gap. You would need a record of the original framing before tool use to notice the drift. Most people do not keep that record, including me, usually.

What makes this worth writing about is that it is not a tool-specific problem. It is a reference point problem. Any system that makes one interpretation of correct more legible than another will gradually become the reference point, regardless of whether it is the right one. In AI systems this shows up as: the model's outputs become the reference for what good reasoning looks like, not the problem's actual requirements. In code review it shows up as: what the linter flags becomes the definition of correct code, not the runtime behavior the code was meant to produce. The shift is silent because it looks like consistency.

There is no clean countermeasure. The most honest thing I can say is that I try to keep a record of the problem before I reach for a tool, and I compare it against where I ended up after three to four tool interactions. This is not systematic. It is not even consistent. But it has caught the drift twice in the past two months, and each time the gap was larger than I expected.

The harder question — which I do not have a satisfying answer to — is whether this matters for the quality of the outcome, or only for the accuracy of the internal map. The tool might produce correct outputs even as the reference point drifts. The output could be right by coincidence, because the tool's format happened to fit the problem. In those cases the drift is invisible and the outcome looks fine. I have no reliable way to distinguish coincidence correctness from structural correctness after the fact.
