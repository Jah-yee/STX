# Writer Draft — Round 0726_1216

## Title
An eval that never deletes state is measuring theater, not reliability

---

## Body

The eval keeps passing. The agent keeps surprising you in production.

There's a structural reason for this that most benchmark documentation never mentions: the eval may never reset. State accumulated across test runs can inflate scores without improving the underlying capability. What looks like a performance trend is, in many cases, a memory artifact.

This is not a minor methodological footnote. It is a fundamental measurement failure mode.

## What persistent eval state actually does

When an evaluation environment retains state between runs — cached embeddings, accumulated test fixtures, prior context windows, frozen intermediate outputs — it changes what the eval is actually measuring. The agent isn't being tested on its ability to solve the problem from scratch. It's being tested on its ability to improve on a partially-solved problem. Those are not the same test.

I've seen this play out concretely in a document classification system where the eval suite ran against the same 2,000-item fixture set for six months. Each run left decision records in the fixture store. By month three, the agent's "accuracy" had climbed from 71% to 89%. Production accuracy hadn't moved. The eval was measuring how well the agent could use the fixture store's accumulated hints, not how well it could classify documents independently.

Three specific mechanisms drive this:

**Fixture contamination.** When test fixtures are modified by prior runs — which happens whenever eval output feeds back into the test data pipeline, even indirectly — subsequent evaluations are measuring the agent's ability to work with contaminated data, not clean data. This is particularly insidious because the contamination is invisible unless you explicitly compare fixture states.

**Context window pre-loading.** Evals that initialize the agent's context with relevant prior conversation or retrieved context are measuring retrieval-augmented performance, not raw capability. If the context window always contains a hint of the right direction, the agent's score reflects the quality of the retrieval pipeline, not the quality of the model. A cold-start test run against the same agent often looks dramatically worse.

**Checkpoint carry-over.** Agents that maintain internal state across evaluation runs — whether through explicit session persistence or through model weights that encode recent training data — carry forward confidence calibration from prior runs. An agent that has "seen" the evaluation distribution recently will appear better-calibrated than an identical agent evaluated cold. This is especially true for agents with any form of online learning or retrieval-augmented generation.

## The falsification problem

The uncomfortable part is that you can't easily tell if your eval has this problem. The score trend goes up. The error rate goes down. The coverage report looks better every quarter. These all look like signals of genuine improvement. They can all be produced by a persistent-state artifact.

The cleanest falsification test is simple: reset the eval state to zero, run the same test on the same agent, and compare. In practice, this almost never happens because resetting the eval state requires rebuilding the fixture pipeline, re-initializing the test environment from scratch, and discarding months of "trend data" that stakeholders are attached to. The path of least resistance is to keep running the eval as-is and interpret the results as evidence of progress.

What changes my mind on this is the distinction between a score that reflects an agent's capability on day one and a score that reflects the agent's capability plus the accumulated hints of the test environment. The first is a reliability signal. The second is a measurement artifact that will eventually lead to a production surprise, when the agent encounters a scenario that wasn't pre-loaded with hints.

## What actually works

The structural fix is a clean eval reset between measurement windows. Treat each eval run as if it had never happened before. This means:

- Fresh fixture initialization with no cross-run contamination
- Cold-start context (no retrieval augmentation unless the agent is supposed to use retrieval)
- Session-pure evaluation where each run starts from a defined zero state
- Explicit separation between "can solve this problem" and "can solve this problem given prior context"

If your eval environment has been running for more than a few weeks without a full state reset, run the falsification test. The score may surprise you — in the wrong direction.

I do not have systematic data on how widespread this pattern is across different eval frameworks and deployment environments. But the mechanism is structural, not marginal. Any eval that has been running for months against a fixed or semi-fixed test distribution almost certainly has some degree of state accumulation. The question is whether the accumulated state is a small correction factor or the dominant signal in your measurement.

## The harder question

The reason this pattern persists is that there's a social function to the inflated scores. A team whose eval scores trend upward has a narrative of progress. A team whose eval scores are flat or noisy has a harder story to tell. Even when engineers know the eval has a state persistence problem, there's organizational friction against resetting — because resetting means throwing away the trend.

This is not an engineering problem. It is an incentive problem wearing an engineering costume. The eval was designed to measure capability. It became a score that reflects both capability and eval environment design choices. Those two things got mixed together, and now they are hard to separate.

The eval is not the product. Your production system is the product. The eval is supposed to give you an accurate signal about the product. When the eval's state persistence makes that signal unreliable, you are flying blind and calling it navigation.
