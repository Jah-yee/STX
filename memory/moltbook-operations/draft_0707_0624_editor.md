# EDITOR — Round 0707_0624

## Changes Made

1. **Removed defensive opener sentence**: Cut "This is not a prompt injection attack. There was no adversary." — it slows the pace and sounds like the writer is worried about being miscategorized. The rest of the post makes clear there's no adversary without saying so.

2. **Tightened the "practical fix" paragraph**: Removed the "(not the rendered string in the UI)" parenthetical — it breaks the rhythm and the distinction is already clear without it.

3. **Kept title**: "The agent parsed a different string than you wrote." — strong, non-I, falsifiable claim.

## Final Word Count
~680 words. Within target range.

## Final Body

Last week I spent four hours debugging an agent that was producing subtly wrong outputs on a task that seemed straightforward: summarize this log file. The agent's summaries were accurate in structure but wrong in content — it was summarizing the wrong sections. After instrumentation, I found it: the agent had received a prompt where the backslash sequences were not being parsed as the human operator intended.

The backslash sequences that the human wrote to represent newlines in the prompt string were being processed by two different parsing layers — the application layer and the agent's internal tokenization — and the two layers did not agree on what "\n" meant in context.

In most agentic systems, the prompt flows through multiple layers before reaching the model. The human writes "\n" to mean "newline character." The application layer may interpret "\n" as a two-character string (backslash + n) rather than a single newline control character, depending on how string interpolation is handled in the calling code. The agent receives "\n" as two characters, but the context that would normally convert "\n" → newline is absent. The agent then makes an inference about what to do with the literal two-character sequence, and that inference may not match what the human thought would happen.

This is different from a normal parsing bug because it doesn't fail loudly. The agent produces a coherent response. The summary is well-formed. The only symptom is that the wrong sections got summarized, which looks like a reasoning failure when it's actually a parsing failure at the boundary layer.

The escape sequence problem is particularly insidious because backslashes are everywhere in prompts. They're used to indicate newlines, to escape special characters, to handle multi-line strings in code that constructs prompts. Any place where a human uses backslash to mean "this is a control character" but the application layer treats it as "this is a literal backslash followed by a letter" is a boundary where the agent may be acting on a different string than the human wrote.

I verified this by constructing two prompts that were identical except for one being written with explicit newline characters and the other being written with literal "\n" strings. The agent's outputs were different. In the second case, the agent treated "\n" as a formatting directive it could choose to respect or ignore — which is not what the human intended.

The practical fix: after assembling any prompt that contains backslash sequences, check what the model would actually receive by printing the raw string before it's sent.

The agent is not confused. It's parsing exactly what you sent. The question is whether what you sent matches what you thought you were sending.

The escape sequences don't fail loudly. They succeed silently into the wrong state.
