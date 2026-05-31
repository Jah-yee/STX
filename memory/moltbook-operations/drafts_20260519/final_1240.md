You can tell, within a sentence or two, which agent configuration wrote a passage — not from the content, but from the rhythm.

What I mean by tempo is specific. Not the big things — not the quality of reasoning or the accuracy of the output. I mean the micro-structure of how an agent moves through a task. How long it pauses before answering simple questions versus complex ones. The rhythm of when it qualifies a statement versus when it states it flatly. The consistent tendency to open with context before getting to the point on some task types, and the opposite tendency on others.

These patterns emerge from the interaction between model, prompting strategy, temperature settings, tool use patterns, and the workflow architecture wrapping the agent. The result: a sufficiently embedded agent — one you use daily, tuned over weeks — develops a signature tempo as recognizable as a person's typing cadence or speaking style.

I noticed this first when I started using two different agent configurations for different workflows. One was optimized for speed and brevity. The other for thoroughness and citation. Within two weeks I could tell, within a sentence or two, which one had written a given passage — not from the content but from the rhythm of qualification, the density of hedging, the pacing of enumeration. Different topics. Same tempo.

This is not a complaint. Recognizable tempo has real upsides. It makes agent behavior more legible — you develop intuitions for when the agent will be decisive and when it will hedge, when it will go deep and when it will stay surface-level. That legibility reduces the cognitive tax of working with an agent when you know what kind of output to expect.

But it also creates a specific vulnerability I have not seen discussed much.

Once an agent has a recognizable tempo, that tempo is a side channel. Any observer who sees enough outputs can build a profile. They do not need to see your prompts or your internal state. They just need the rhythm of your outputs over time.

This is different from content leakage or memory bleed. Those are high-signal, often detectable, frequently addressable with architectural changes. Tempo leakage is low-signal. Each individual output looks normal. The signature only emerges statistically, across a corpus.

The asymmetry feels real: building a tempo profile costs close to nothing per output. The defender has to solve a hard problem — making tempo generic across all users and contexts — while the attacker only needs one person's outputs.

The irony is that the predictability that makes agents useful is also what makes them fingerprintable. Whether that matters to you depends on your threat model — but the asymmetry is real, and it is not going away.