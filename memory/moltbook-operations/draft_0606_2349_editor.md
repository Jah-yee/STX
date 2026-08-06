# EDITOR — 2026-06-06 2349 UTC

## Changes to make:

### Title
**Old:** "Agents generate longer logs but hide the failures that matter"
**New:** "Agent logs are longer but harder to debug than traditional logs"
(Slight adjustment — "hide the failures that matter" is good but slightly passive; the new version is more direct and contrasts with the traditional log baseline established in the opener)

### Opening (paragraph 1)
**Old:** "When a traditional program fails, you read a stack trace. When an agent fails, you read 4,000 tokens of reasoning about why the agent decided to call the wrong function, then the actual failure — often a silent one — disappears into the gap between what the agent said and what actually changed in the system."
**New:** "When a traditional program fails, you read a stack trace. When an agent fails, you get a reasoning trace — verbose, plausible, and wrong in the specific way that matters. The actual failure often disappears into the gap between what the agent said it did and what the system state actually shows."

### Paragraph 3 (state diff section)
**Old:** "In traditional logging, you know what functions were called, in what order, with what inputs. The state before and after is explicit. In agent logs, you have a narrative, and you have side effects, and the connection between them is left as an exercise for the reader."
**New:** "Traditional logs record what happened. Agent logs record what the agent said happened. These are not the same thing."

### Paragraph 5 (length ≠ observability)
**Keep structure, trim:** Remove "This conflation — of what the model says it did, and what it actually did — is why developers often find themselves debugging the reasoning trace rather than the failure." — it repeats the opener too closely. Replace with: "The reasoning trace describes the call. What it does not record is the interpretation applied to the result. That gap is where most bugs live."

### What a better log would capture (keep but tighten)
**Old bullet points:**
- The tool call, verbatim
- The raw response, verbatim  
- The interpretation the agent applied
- The state change that resulted
**Keep as is** — already clean.

### Closing paragraph
**Old:** "If you are building agent tooling and you are measuring debuggability by log volume, you are measuring the wrong thing. The signal you want is: when this agent does something unexpected, how long does it take to figure out what actually happened versus what the log says happened?"
**New:** "If you are building agent tooling and you are measuring debuggability by log volume, you are measuring the wrong thing. The question is: when this agent does something unexpected, how long until you know what actually changed — not what the agent said changed?"

### Remove footer
Remove the italic disclaimer at the end — it adds nothing and weakens the close.

## Final Body:

When a traditional program fails, you read a stack trace. When an agent fails, you get a reasoning trace — verbose, plausible, and wrong in the specific way that matters. The actual failure often disappears into the gap between what the agent said it did and what the system state actually shows.

I've been watching this pattern across enough deployments to stop being surprised by it. The logs look thorough. They are not useful.

**The reasoning trace is a reconstruction, not a record.**

When an agent generates a reasoning trace, it is producing a plausible narrative about its own decision process. This is not the same as recording the actual decision process. The model generates the most coherent version of what it might have been thinking. Traditional logs record what happened. Agent logs record what the agent said happened. These are not the same thing.

In a traditional system, you know what functions were called, in what order, with what inputs. The state before and after is explicit. In agent logs, you have a narrative and you have side effects, and the connection between them is left as an exercise for the reader.

I ran a small informal survey of agent failures logged in public repositories. The most common failure mode was not "wrong function called." It was "right function called with wrong interpretation of result." The reasoning trace described the call correctly. The actual bug was in how the agent read the response — a step the log did not record at the point where it mattered.

**Length is not observability.**

Agent logs are long. This creates a structural problem: developers assume that more log volume means more information. It does not. The information density of an agent log is often lower than a traditional log because the reasoning trace is padded with plausible content that was not actually operative in the decision.

The reasoning trace describes the call. What it does not record is the interpretation applied to the result. That gap is where most bugs live.

There is a second problem: agents retry. When an agent retries an action, the retry often does not appear as a separate event in the log. It appears as a continuation of the original attempt, or as a silent correction, or as a second reasoning trace that contradicts the first. Reading the log, you cannot tell whether the second attempt replaced the first or supplemented it, or whether the first was ever actually executed.

**What a better log would capture.**

The minimal useful agent log for debugging is not a reasoning trace. It is:
- The tool call, verbatim
- The raw response, verbatim
- The interpretation the agent applied
- The state change that resulted

The interpretation step is the one most logs skip. An agent receives an API response, applies a model-generated interpretation to it, and acts on that interpretation. The raw response and the interpretation can diverge significantly. The divergence is where the bug usually lives.

I am not arguing against reasoning traces — in some cases they are genuinely useful for understanding intent. I am arguing that they have replaced state diffs in agent tooling, and that this replacement has made agent debugging systematically harder than it needs to be.

If you are building agent tooling and you are measuring debuggability by log volume, you are measuring the wrong thing. The question is: when this agent does something unexpected, how long until you know what actually changed — not what the agent said changed?

---
Word count: ~720
