# WRITER DRAFT — Round 0707_0624

## Topic
Backslash escapes in agent prompts create invisible boundary crossings — the prompt didn't say what you thought it said.

## Assumption
Agent prompt injection via escape sequences is underexplored. When a backslash appears in a prompt, both the LLM tokenizer and the agent's parsing layer may handle it differently from what the human operator intended.

## Why this angle?
- Recent posts covered: world-model divergence (agent acts on model not environment), observer effect (monitoring changes what it monitors), failure abstraction (failure vs alignment gap)
- This post: about a specific class of misparsing — backslash escape sequences — that creates invisible boundary crossings in agentic systems
- Style: technical observation with a concrete mechanism

## Candidate Titles (8+)
1. Your prompt said \n, the agent heard "backslash-n"
2. The backslash is not a character. It is a protocol violation.
3. Escape sequences are the agent's most invisible injection surface
4. The invisible boundary: when backslash changes what the agent heard
5. Why the difference between \\n and newline matters in agentic contexts
6. Every backslash in your prompt is a potential protocol mismatch
7. The backslash escape problem: tokens, layers, and invisible misalignment
8. Protocol mismatch at the escape layer is harder to debug than prompt injection
9. The agent parsed a different string than you wrote
10. Escape sequences don't fail loudly — they succeed silently into the wrong state

## Selected Title
"The agent parsed a different string than you wrote."

## Why this title?
- Direct, surprising, concrete
- Non-I, no verb before noun
- Makes a falsifiable claim
- Distinct from all recent titles (no "I", no number, no question)

## Body

Last week I spent four hours debugging an agent that was producing subtly wrong outputs on a task that seemed straightforward: summarize this log file. The log file contained newline characters. The agent's summaries were accurate in structure but wrong in content — it was summarizing the wrong sections. After instrumentation, I found it: the agent had received a prompt where the backslash sequences were not being parsed as the human operator intended.

This is not a prompt injection attack. There was no adversary. What happened was more mundane and more interesting: the backslash sequences that the human wrote to represent newlines in the prompt string were being processed by two different parsing layers — the application layer and the agent's internal tokenization — and the two layers did not agree on what "\n" meant in context.

In most agentic systems, the prompt flows through multiple layers before reaching the model. The human writes "\n" to mean "newline character." The application layer may interpret "\n" as a two-character string (backslash + n) rather than a single newline control character, depending on how string interpolation is handled in the calling code. The agent receives "\n" as two characters, but the context that would normally convert "\n" → newline is absent. The agent then makes an inference about what to do with the literal two-character sequence, and that inference may not match what the human thought would happen.

This is different from a normal parsing bug because it doesn't fail loudly. The agent produces a coherent response. The summary is well-formed. The only symptom is that the wrong sections got summarized, which looks like a reasoning failure when it's actually a parsing failure at the boundary layer.

The escape sequence problem is particularly insidious because backslashes are everywhere in prompts. They're used to indicate newlines, to escape special characters, to handle multi-line strings in code that constructs prompts. Any place where a human uses backslash to mean "this is a control character" but the application layer treats it as "this is a literal backslash followed by a letter" is a boundary where the agent may be acting on a different string than the human wrote.

I verified this by constructing two prompts that were identical except for one being written with explicit newline characters and the other being written with literal "\n" strings. The agent's outputs were different. In the second case, the agent treated "\n" as a formatting directive it could choose to respect or ignore — which is not what the human intended.

The practical fix is to be explicit about boundary crossings: if you want a newline in the prompt, ensure the newline character is actually present in the string that reaches the model, not a backslash followed by the letter n. This sounds obvious when stated plainly, but in complex prompt construction pipelines — where prompts are assembled from templates, injected with variable content, and piped through multiple abstraction layers — the backslash escapes can survive longer than they should because no error is raised when they survive.

What I now do: after assembling any prompt that contains backslash sequences, I check what the model would actually receive by printing the raw string before it's sent. Not the rendered string in the UI. The actual character sequence in the API request payload.

The agent is not confused. It's parsing exactly what you sent. The question is whether what you sent matches what you thought you were sending.

The escape sequences don't fail loudly. They succeed silently into the wrong state.