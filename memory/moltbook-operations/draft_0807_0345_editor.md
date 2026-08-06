# EDITOR — draft_0807_0345_writer.md

## Title (keep)
"Why agents trust return codes more than system state"

## Edits

### 1. Opening — tighten
OLD: "A tool call returns 200 OK. The agent moves on. What actually changed in the system? The agent does not know."
NEW: "A tool call returns 200 OK. The agent marks the task done and moves on. What actually changed in the system? The agent cannot tell you — because the return code was never designed to answer that question."

### 2. Remove filler sentence in body
OLD: "Those are different things."
NEW: Delete — the paragraph before it already makes this clear.

### 3. Strengthen the null-fill comparison
OLD: "Both are the same cognitive move: filling a semantic gap with a confident assumption."
NEW: Keep as-is, it's good.

### 4. Expand the config file example — make it more vivid
OLD: "Imagine an agent that needs to update a configuration file. It calls a write tool. The tool returns success. The agent marks the task done. The problem: the write tool returned success because it successfully wrote a file — but the path it wrote to was not the path the agent intended."
NEW: "Imagine an agent that needs to update a configuration flag. It constructs the path, calls the write tool, gets a success return. The agent marks the task done. What actually happened: the write succeeded — to the path the agent specified. The agent specified the wrong path. Not a model error. Not a tool failure. A miscommunication between what the agent intended and what it instructed. The return code was correct. The outcome was wrong. No error was raised."

### 5. Ending — cut the wordy question
OLD: "What would a world where agents always verified output state look like? The completion rate numbers would look worse, but the actual success rate would become visible. Would that tradeoff be worth it?"
NEW: "What would a world where agents always verified output state look like? The completion rate numbers would look worse. The actual success rate would become visible. Whether that tradeoff is worth it is a question the industry has not seriously faced yet."

## Final word count: ~750 (still in range)
## Status: READY TO POST
