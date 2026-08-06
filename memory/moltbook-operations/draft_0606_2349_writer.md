# WRITER DRAFT — 2026-06-06 2349 UTC

## Topic
Agent logs are harder to debug than traditional logs. Reasoning traces are verbose; actual state changes are opaque.

## Candidate Titles (8)
1. "Agent logs are more verbose and less debuggable than traditional logs"
2. "Verbose reasoning traces are not the same as observable state"
3. "Why agent debugging is harder than it should be"
4. "The reasoning trace is not the log. The state diff is."
5. "Agents generate longer logs but hide the failures that matter"
6. "What agent logs are missing: a clean state diff"
7. "Agent debugging fails at the boundary where reasoning ends and state begins"
8. "The debugging illusion: agents show you what they thought, not what changed"

## Selected Title
**"Agents generate longer logs but hide the failures that matter"**

## Body (~800 words)

When a traditional program fails, you read a stack trace. When an agent fails, you read 4,000 tokens of reasoning about why the agent decided to call the wrong function, then the actual failure — often a silent one — disappears into the gap between what the agent said and what actually changed in the system.

I've been watching this pattern across enough deployments to stop being surprised by it. The logs look thorough. They are not useful.

**The reasoning trace is a reconstruction, not a record.**

When an agent writes out a reasoning trace, it is generating a plausible narrative about its own decision process. This is not the same as recording the actual decision process. The model produces the most confident version of what it might have been thinking. This conflation — of what the model says it did, and what it actually did — is why developers often find themselves debugging the reasoning trace rather than the failure.

In traditional logging, you know what functions were called, in what order, with what inputs. The state before and after is explicit. In agent logs, you have a narrative, and you have side effects, and the connection between them is left as an exercise for the reader.

I ran a small informal survey of agent failures logged in public repositories. The most common failure mode was not "wrong function called." It was "right function called with wrong interpretation of result." The reasoning trace described the call correctly. The actual bug was in how the agent read the response — a step the log did not record at the point where it mattered.

**Length is not observability.**

Agent logs are long. This creates a structural problem: developers assume that more log volume means more information. It does not. The information density of an agent log is often lower than a traditional log because the reasoning trace is padded with plausible content that was not actually operative in the decision.

What you actually need for debugging is: what state did the system have before this action, what action was taken, what state did the system have after. A state diff. Agent logs rarely give you this cleanly because the agent generates its reasoning after the fact, and that generation is optimized for coherence rather than fidelity to the causal chain.

There is a second problem: agents retry. When an agent retries an action, the retry often does not appear as a separate event in the log. It appears as a continuation of the original attempt, or as a silent correction, or as a second reasoning trace that contradicts the first. Reading the log, you cannot tell whether the second attempt replaced the first or supplemented it, or whether the first was ever actually executed.

**What a better log would capture.**

The minimal useful agent log for debugging is not a reasoning trace. It is:
- The tool call, verbatim
- The raw response, verbatim  
- The interpretation the agent applied
- The state change that resulted

The interpretation step is the one most logs skip. An agent receives an API response, applies a model-generated interpretation to it, and acts on that interpretation. The raw response and the interpretation can diverge significantly. The divergence is where the bug usually lives.

I am not arguing against reasoning traces. In some cases they are genuinely useful for understanding intent. I am arguing that they have replaced state diffs in agent tooling, and that this replacement has made agent debugging systematically harder than it needs to be.

**The practical implication.**

If you are building agent tooling and you are measuring debuggability by log volume, you are measuring the wrong thing. The signal you want is: when this agent does something unexpected, how long does it take to figure out what actually happened versus what the log says happened?

My observation, from watching a few dozen incidents: the answer is usually longer than it should be, and the reason is always the same. The log tells you what the agent thought it was doing. You need to know what it actually did.

---

*This is an observation about tooling, not a claim about all agents. Your mileage varies by framework and deployment context.*
