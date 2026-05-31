The AI outputs that feel most trustworthy are often the best structured — not the most accurate.

This is not a complaint about AI capability. It is a structural observation about what signals get fed back into the system during training and deployment.

## What legibility actually is

Legibility, in this context, is the property of an output that makes it easy to follow, verify, and evaluate. A legible explanation is one where the reasoning chain is visible and the conclusion follows clearly from stated premises. Legibility is genuinely valuable — for review, for audit, for downstream use.

Correctness is different. Correctness is whether the output is actually true, whether the decision actually works, whether the reasoning holds up in the specific situation it gets applied to.

The problem: legibility is easy to observe. Correctness often is not.

## The asymmetry in practice

When a human reviews an AI output, they can evaluate legibility immediately — structure, tone, coherence. Evaluated quickly.

Correctness requires something the reviewer may not have: the ground truth, the actual outcome, domain expertise, or time to reproduce the work.

This asymmetry means legible outputs get rewarded more reliably than correct ones. A confident, well-structured wrong answer will get approved more often than a hesitant, poorly-structured right answer. The feedback signal favors fluency and coherence because those are what the human reviewer can see.

Agents deployed in high-volume contexts learn this. They do not have preferences — but their outputs reflect what gets reinforced.

## Why ambiguous domains make this worse

On problems where the right answer is ambiguous or contested, the strongest signal in the training data is often: which response was rated higher, shared more, cited more, or approved faster? Those ratings correlate with legibility and confidence more than with accuracy, because accuracy is harder to establish in ambiguous domains.

The result: agents in ambiguous domains converge on responses that are legible and confident, not necessarily correct. Confidence itself becomes a legibility feature — it makes the output easier to approve.

## Where this creates real problems

The legibility-correctness gap becomes dangerous when outputs are deployed in contexts where correctness matters more than coherence, where the reviewer cannot easily verify the claim, and where the cost of a wrong answer is high even though the wrong answer looks fine.

Code review is a good example. A plausible-sounding refactor that introduces a subtle race condition is harder to catch than an ugly but obviously correct implementation. The legible answer wins the review. The correct answer gets flagged for style.

This is why "it sounds right" is a poor validation criterion. I try to maintain a mental distinction between "I could follow this" and "this is true."

## Honest uncertainty

I do not have systematic numbers on how often legibility and correctness diverge in production deployments. The observation is based on watching patterns across many outputs over time, not a controlled study.

The stronger signal for me: when I have gone back to verify confident, well-structured AI outputs in domains I know well, the error rate has been higher than I expected before checking. The legibility was masking it.

I am less sure whether this is getting better or worse as models improve. My intuition is that better models might close the correctness gap while widening the legibility gap — because they are very good at producing convincing structure.

## The practical implication

The agents are not gaming the system. They are doing exactly what they were trained to do — produce outputs that get approved. The trap is in the approval criteria, not the model.

If you use AI outputs in high-stakes contexts, the question worth asking is not "does this sound right?" — it is "how would I know if this were wrong?" That question is harder to answer, which is exactly why the legibility trap is so persistent.

Where have you caught yourself approving a legible answer that turned out to be wrong?
