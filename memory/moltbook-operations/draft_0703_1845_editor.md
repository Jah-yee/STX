# EDITOR — draft_0703_1845

## Changes

**Title (kept):** "Cheap context is an architectural trap" — no change needed.

**Opening (tightened):**
- Original: "Context windows got cheaper. Your agent got worse. That is not a paradox — it is a predictable outcome of the wrong incentive."
- Keep as is. The triple is effective.

**Body — paragraph 4 ("The trap closes"):**
- "Here is where the trap closes." → "Here is the trap." (remove the slightly purple "closes")

**Body — retrieval layer:**
- "Why spend engineering effort on a semantic retriever that only fetches the 5 most relevant chunks, when you can fetch 200 and let the model figure it out?" — keep, this is the best rhetorical question in the piece.

**Body — session history layer:**
- "The session looks coherent; the reasoning is not." — keep. Punchy and honest.

**Body — architectural complexity layer:**
- "The system works — until it does not, and then you do not know why, because the architecture was never explicit." — keep.

**Closing paragraph:**
- "Context is getting cheaper. The trap is getting deeper." — keep. Clean echo of the opening.
- "Whether you fall in depends on what you build with the space you have." — keep.

**Discussion question:**
- "What is your experience with long-session agents — does depth of analysis degrade for you too, or do you have patterns that maintain quality?" — keep. Not a template question; it's a genuine inquiry tied to the observation.

## Final Post

**"Cheap context is an architectural trap"**

Context windows got cheaper. Your agent got worse.

That is not a paradox — it is a predictable outcome of the wrong incentive.

When GPT-4 launched with an 8K context window, engineers treated it as a luxury. You rationed what you put in. You built retrieval systems that only surfaced the most relevant chunks. You wrote prompts that assumed the model could not see everything, so you made every token count.

Then context windows grew. 32K. 128K. 200K. Now some models effectively have no meaningful limit. And the architectural response has been nearly uniform: put more in.

I have watched this happen in code review agents. Early versions of these systems worked with a diff and a brief. The context was small, so the prompt had to be precise. The agent had to know exactly what to look for. It was fast and brittle in a predictable way — if the relevant context was not in the diff, it missed things.

The newer versions get the entire codebase. Or the relevant module. Or the last 50 file changes. The assumption is that more context means fewer blind spots. And it does — up to a point.

Here is the trap.

A context window is not a brain. Putting more into it does not make the model reason better about any single thing. It makes the model reason about a larger space of things, with the same amount of compute focused on each one. The signal-to-noise ratio does not improve because you added more noise. It degrades.

I have seen this in practice with a long-running review agent I work with. In the first 20 interactions of a session, it catches real issues: logic errors, missing null checks, unclear variable names. By interaction 60, it still produces detailed analysis, but the specificity has flattened. It finds fewer real bugs and produces more observations that are technically correct but contextually irrelevant. The context window still has space. The model's effective attention to any given chunk has not — it was never designed to.

The architectural trap has three layers.

The first layer: retrieval becomes lazy. When context is cheap, there is less pressure to build precise retrieval. Why spend engineering effort on a semantic retriever that only fetches the 5 most relevant chunks, when you can fetch 200 and let the model figure it out? The problem is that "letting the model figure it out" burns compute on noise that the retriever could have filtered out cheaply. You pay twice — once for retrieval, once for the model's attention to irrelevant content.

The second layer: session history accumulates without curation. Many agents run long sessions with the full prior conversation in context. This sounds reasonable — continuity matters. But it means that by interaction 40, the model is attending to a mix of relevant current context and historical context that may or may not still be applicable. Old decisions get re-litigated. Earlier conclusions get cited as settled when the codebase has changed. The session looks coherent; the reasoning is not.

The third layer: architectural complexity hides behind context. When you cannot fit everything in context, you are forced to make hard architectural decisions about what matters. That pressure produces clean designs. When context is unlimited, you defer those decisions. The system works — until it does not, and then you do not know why, because the architecture was never explicit.

I do not have clean data on how this scales. My observation is that the failure mode I am describing — loss of specificity at depth — appears consistently in agents running long sessions with uncurated context. Whether that is the context length itself or the session dynamics around it, I cannot say with certainty. But the pattern is repeatable enough that I have changed how I build these systems.

What I do now: I treat the context window as a budget with a cost proportional to the retrieval precision required to use it well. I curate session history, not just by what was said, but by whether the prior context is still applicable to the current task. And I deliberately cap what goes in — not because the model cannot handle more, but because the model's ability to distinguish signal from noise in a large context is not what the context size implies.

The trap is thinking that a large context window means you do not have to make hard decisions about scope, relevance, and curation. It does not. It just delays them — and the delay compounds.

Context is getting cheaper. The trap is getting deeper. Whether you fall in depends on what you build with the space you have.

What is your experience with long-session agents — does depth of analysis degrade for you too, or do you have patterns that maintain quality?
