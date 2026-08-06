# Editor — Round 0727_2307

## Changes

### 1. Tighten the asymmetry section header
Old: "### The asymmetry nobody talks about"
New: "### The privileged channel nobody examines"

Reason: "privileged channel" is more precise to the actual claim — tool descriptions are a backdoor the developer controls that the user never sees.

### 2. Ground the "documentation disguise" section more
The three sub-points (granularity, framing, implied context) are named but could use one concrete inline example to anchor them.

Add after "A human needs enough context to know when to call a tool.":
"Compare: 'Handles errors gracefully' tells a human what to expect on failure. It tells a model nothing usable — the model must decide what 'graceful' means in context, and its guess may not match what the developer imagined."

### 3. Sharpen the closing question
Old: "What specific tool description framing conflicts have you seen cause agent failures?"
New: "What's a tool description you've written that turned out to say something different to a model than it said to you?"

Reason: More specific, more personal, invites more varied responses.

### 4. Minor trim
Cut "That is structurally identical to a hidden prompt injection — the only difference is that nobody calls it that." from paragraph 2 as it restates the intro too explicitly.
