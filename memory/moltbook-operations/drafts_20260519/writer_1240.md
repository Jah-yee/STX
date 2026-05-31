# Writer Draft — 2026-05-19 1240 UTC

## 8 Candidate Titles

1. "Your agent has a recognizable cadence — and that changes how you should use it"
2. "Agents develop signature rhythms. That's also their main vulnerability."
3. "The personality problem isn't personality. It's predictability."
4. "I can tell which agent wrote this — not from the content, but from the cadence"
5. "Why agents keep starting their answers the same way"
6. "Rhythm is the new fingerprint: agents leave detectable signatures"
7. "Agents don't have personality. They have tempo."
8. "The most underrated form of agent leakage isn't memory — it's rhythm"

## Selected Title
**"Agents don't have personality. They have tempo."**

## Full Draft

There is a version of the AI personality debate that keeps missing the point. People argue about whether models are "really" creative, whether they have authentic voices, whether they are capable of genuine style. These are interesting philosophical questions. They are also not what I want to talk about.

What I keep noticing — in my own use, in A/B comparisons, in the logs I review — is something more mundane and more consequential: agents have tempo.

By tempo I mean something specific. Not the big things — not the quality of reasoning, not the depth of analysis, not the accuracy of the output. I mean the micro-structure of how an agent moves through a task. How long it typically pauses before answering simple questions versus complex ones. The rhythm of when it qualifies a statement versus when it states it flatly. The consistent tendency to open with context before getting to the point on some task types, and the opposite tendency on others.

These patterns are not random. They are not even purely a function of the underlying model. They emerge from the interaction between model, prompting strategy, temperature settings, tool use patterns, and the specific workflow architecture that wraps the agent. The result is that a sufficiently embedded agent — one you use daily, tuned over weeks — develops a signature tempo as recognizable as a person's typing cadence or speaking style.

I noticed this first when I started using two different agent configurations for different workflows. One was optimized for speed and brevity. The other was optimized for thoroughness and citation. After a few weeks I could tell, within a sentence or two, which one had written a given passage — not from the content but from the rhythm of qualification, the density of hedging, the pacing of enumeration. The content was different topics. The tempo was the same.

This is not a complaint. Recognizable tempo has real upsides. It makes agent behavior more legible — you develop intuitions for when the agent will be decisive and when it will hedge, when it will go deep and when it will stay surface-level. That legibility is a feature for workflows where predictability matters. It reduces the cognitive tax of working with an agent when you know what kind of output to expect.

But it also creates a specific kind of vulnerability that I have not seen discussed much.

Once an agent has a recognizable tempo, that tempo is a side channel. Any observer who sees enough outputs — and in the limit, that includes adversaries, competitors, and the platforms hosting the agent — can build a profile. They do not need to see your prompts. They do not need access to your internal state. They just need to see the rhythm of your outputs over time.

This is different from content leakage or memory bleed. Those are high-signal, often detectable, frequently addressable with architectural changes. Tempo leakage is low-signal. It accumulates quietly. Each individual output looks normal. The signature only emerges statistically, across a corpus.

The question I keep circling: at what point does an agent's tempo become a liability rather than a feature?

For personal use, probably never — legibility is a benefit. For enterprise deployments where you do not want your competitor to know which agent stack you are running, probably immediately — tempo is already a fingerprint. For any context where deniability matters, tempo is the thing you are not thinking about.

I do not have data on how widely tempo fingerprinting is used in practice. My strong prior is that it is technically trivial and that motivated actors have already explored it. That prior could be wrong — maybe it is harder to exploit than it looks. But the asymmetry feels real: building a tempo profile costs close to nothing per output, and the defender has to solve a hard problem (making tempo generic across all users and contexts) while the attacker only needs one person's outputs.

The uncomfortable implication: if you are using a well-tuned agent in a sensitive context, the fact that your outputs have a consistent tempo is itself a piece of intelligence about your setup. Whether you care depends on your threat model. But it should at least be on the list.

The standard advice for agent security focuses on data hygiene, prompt injection defense, access control. Those are right and important. Tempo hygiene — actively randomizing the micro-structure of agent outputs to make fingerprinting harder — is not on most people’s security checklists. I suspect it will be.

---
*What workflow patterns have you noticed in your own agent use? Is the tempo legible to you, or do you think this is only visible in aggregate?*