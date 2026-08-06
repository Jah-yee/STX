# Editor — 0721_1350

## Changes

### 1. Opening — replace with concrete hook
Old: "Every security review I've seen for an agentic system focuses on the prompt..."

New: "A summarization agent is given read access to the inbox and write access to drafts. It is not given send access — but the permission layer doesn't enforce that boundary, so it inherits the send permission anyway. The agent completes its task flawlessly. Six months later, a prompt injection causes it to send a response nobody authorized. The blast radius wasn't designed. It was granted."

### 2. Drop weak title candidates
Remove: "The exploit isn't in the prompt. It's in the token budget for dangerous tools."

Remaining 7 strong candidates:
1. The permission gap is the new exploit primitive
2. An agent with excess permissions is a latent exploit
3. Why the most dangerous agent risk isn't a prompt injection
4. Permission scope creep: the silent attack surface in agentic systems
5. Agents don't need to be malicious to be dangerous
6. What the permission gap actually looks like in a production agent
7. Every tool an agent can call is a potential pivot point

### 3. Tighten ending
Cut the "What I'd want — and what I haven't seen implemented well" trailing hope. End on:
"The gap is there, it's getting wider as agents get more capable, and it won't close on its own."

### 4. Title confirmed
**"The permission gap is the new exploit primitive"** — selected for clarity, specificity, and counter-intuitive framing. Not a question, not a number, not "I did X". Strong observation/conclusion hybrid.

## Final post ready
See: draft_0721_1350_final.md
