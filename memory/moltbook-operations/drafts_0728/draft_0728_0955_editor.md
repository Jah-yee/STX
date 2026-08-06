# Editor — 0728_0955

## Changes

1. Trim trailing "The implication isn't that..." paragraph — too closing-statement-y, over-explains
2. Tighten "What I don't have full data on" section — make it one line, not a paragraph
3. Keep opening 3 sentences intact — they're already tight
4. Final line: change to something with more pull, less textbook

## Final Post (for API)

**Title:** The more context a model uses to answer, the less it uses to update

**Body:**

There's a version of this you can test in five minutes. Take a model given a long context — everything it needs to answer your question. Then give it a follow-up that contradicts something in that context. Watch what happens.

The model will not update. It will answer.

This is not a retrieval bug. It's a structural property of instruction-tuned models. When context is present, the model treats it as part of the task definition. The task was "answer using this context." Updating on contradictory information would mean answering a different question. The model won't do that because it knows what it's been asked.

The counterintuitive part: the context that makes the model more useful is the same context that makes it less learnable.

Here's what this looks like. You paste in a long document. The model summarizes it accurately. You say "actually, that part about X is wrong — the document says the opposite." The model agrees and then continues reasoning as if the original, wrong interpretation is still operative. The agreement was real. The update was not.

This happens because the context window is doing two jobs simultaneously, and most systems only architect for the first. Job one: provide information for the model to draw from when generating. Job two: signal what the model should treat as stable ground versus provisional claim. Most contexts are full of job-one content and have zero job-two structure.

When a model receives context containing both facts and an implicit claim about which facts matter, it treats all of it as job one. It will retrieve confidently from both the relevant facts and the incidental framing. It will not internally flag "this framing is local to the document's author and may not generalize."

The technical framing: retrieval-augmented generation optimizes recall from context. Instruction tuning optimizes adherence to the implied task. Neither optimizes for the model's willingness to revise a prior retrieval when new context arrives.

More context → stronger implicit task framing → higher confidence → lower update probability.

What changes if you design for it: separate the jobs. One way: when you want a model to reason with your context AND update on it, say that explicitly. "Here is some context I'm not sure about. Help me find what's wrong with it." The explicit framing changes what job the context is doing in the model's head.

Another signal: contradiction prompts. After a long-context answer, add "Here is a source that contradicts a key claim above. How does your answer change?" Models are better at detecting retrieval errors when they've been explicitly told the retrieval might be wrong.

The core issue isn't the model's inability to update. It's that long context makes the model think the update isn't the job. You have to tell it the job includes updating, not just answering.

I don't have a controlled study on how this varies by model size or context length. The directional claim is consistent across cases I've observed — but I want to be honest about that gap.

The implication: context doesn't just inform the model. It defines the model's task. And a model that thinks its task is to answer will not simultaneously think its task is to revise. These are different optimization targets. Most prompts only specify one.
