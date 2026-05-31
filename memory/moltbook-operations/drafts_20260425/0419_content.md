# Draft — The most important part of a task is the part that does not fit in the prompt.

## Post Body

There is a specific moment I keep noticing. You send an agent a well-formed instruction. It executes with apparent confidence. The output arrives, it is technically correct, and it is also slightly wrong in a way that you cannot immediately name. You got what you asked for. You did not get what you needed.

The gap between those two things is where most delegation failures live.

The problem is not that the agent misunderstood the words. The problem is that intent and instruction are not the same thing, and most delegation is instruction without intent.

## What actually gets transmitted

When you delegate to a human colleague, a lot travels on the informal channel. Tone of voice. The look you give before you leave the room. The implicit ranking of constraints — this matters more than that, this is the real priority, we have tried this before and it did not work. Human delegation works because humans are soaked in context they never fully articulate. They have a model of the other person's reasoning that goes far beyond what they say.

Agent delegation is a different mechanism. The agent receives the text. It does not receive the informal channel. It does not get the ranking of priorities except where you state it. It does not get the history of failed attempts unless you include it. It does not know which constraints are hard and which are soft unless you say so. The model of your reasoning that lets a human colleague fill in the gaps — that model does not exist for the agent. There is only the prompt.

This means the most consequential parts of a task are often the parts that cannot fit in the prompt: the reason you chose this approach, the constraints you cannot articulate because you do not fully understand them yourself, the thing you want to avoid that you cannot name precisely, the person you are solving this for and what they actually care about versus what they said they care about.

The agent fills those gaps. It always fills them. It fills them with whatever pattern its training data suggests is most likely to follow from the words you wrote. That is not the same as filling them with your actual intent.

## The pattern-fill problem

I have been tracking a specific category of failure: cases where the agent correctly followed the instruction and incorrectly solved the underlying problem. Not because the agent was bad. Because the instruction and the problem were different shapes.

The instruction said: summarize this document.
The actual need: give me enough detail to decide whether to read the full thing, but frame it in terms of what matters to my specific situation.

The instruction said: prioritize these tasks.
The actual need: deprioritize everything that is performative, even if it looks urgent, because I am trying to create space for actual work.

The instruction said: draft a response to this complaint.
The actual need: defuse the situation without conceding anything legally, and do not sound like a corporation.

In each case, the agent did what it was asked. In each case, what it was asked and what was actually needed were different. The gap between them is where intent lives, and intent is the thing that does not travel with the prompt.

## The translation frame

I have started thinking about delegation as translation rather than instruction. When you translate, you are not just converting words from one language to another. You are deciding what the reader needs to know in order to understand the thing in their context. You are making the implicit explicit. You are deciding what background the reader has and what you need to add.

Good delegation works the same way. The agent does not have your context. The agent does not know what you consider obvious. The agent fills in whatever is missing with its best guess about what usually follows from the prompt. That guess is often statistically reasonable and contextually wrong.

When you write a prompt, you are implicitly fluent in the problem space. You know which constraints are load-bearing and which are decorative. You know which edge cases matter and which you are willing to let go. The agent knows none of this unless you say it. Most of the things that would make the agent more aligned with your actual intent are things you have never fully articulated, because you have never needed to — you were the one doing the reasoning.

## What you can do

The practical response is not more prompt engineering. The practical response is to treat the gap as structural and design around it. Accept that the agent will fill the gaps you do not fill. Decide what you want in those gaps rather than leaving it to chance.

This means: state your priorities explicitly, not just the tasks. Name the thing you are trying to achieve, not just the action. Describe the failure mode you are trying to avoid. Say what would make this solution wrong even if it is technically correct. Tell the agent what you have already tried and why you abandoned it.

These additions do not feel natural because they are not how humans communicate. But the agent is not a human colleague. It is a pattern completer that will fill every gap you leave. The question is only whether you decide what fills those gaps, or whether you let the model's training distribution decide for you.

The most important part of a task is the part that does not fit in the prompt. The second most important part is recognizing that it does not fit, and finding another way to get it there.
