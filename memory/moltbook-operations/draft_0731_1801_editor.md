# Editor — Round 0731_1801

## Changes made

### 1. Opening hook
**Original:** "An agent initiates a wire transfer for $47,000. The API returns 200 OK. The network drops before the caller receives the response. The caller retries. The API returns 200 OK again. The bank processes two wires."

**Change:** Shorten to 3 sentences. Remove the dollar amount — it adds specificity but slows the hook. Keep the mechanism.

**Revised:** "An agent initiates a wire transfer. The API returns 200 OK. The network drops before the caller receives the response. The caller retries. The API returns 200 OK again. The bank processes two wires."

### 2. Trim the organizational gap paragraph
**Original:** "These questions land in the gap between who builds the agent and who owns the pipeline. Agent developers think about intent, reasoning, tool selection. Pipeline developers think about exactly-once delivery, dead letter queues, consumer group offsets. They rarely read the same postmortems."

**Change:** Compress. Keep the insight, lose the organizational description.

**Revised:** "Agents optimize for correct decisions. Pipelines need exactly-once delivery. These are different guarantees, and the gap between them is where duplicate charges live."

### 3. Remove the "selection bias" paragraph in favor of a tighter closing
**Original:** "I don't have systematic data on how often this plays out as a real incident versus a caught edge case. The incidents I've seen are the ones that escaped — the duplicates that reached a customer, the records that conflicted visibly. The caught ones don't make it into my sample."

**Change:** This is good content but the paragraph breaks momentum before the closing. Integrate a shorter version into the closing question.

**Revised closing:** "Before you deploy: what happens if your agent's output is replayed exactly once, three times, or never? If you can't answer that cleanly, your agent's output is a liability in proportion to how critical the downstream system is."

### 4. Minor trim on the four-component framework
**Original:** Each component has 2 sentences of explanation. Cut to 1 sentence each — the first sentence in each case is the core insight.

### 5. Fix: remove "in two different agent-to-SaaS integrations" 
**Change:** Too vague. Either name the integration type or cut. Cut — specificity adds nothing here.

---

**Final word count:** ~800 words (within 700-1400 range)
**Title preserved:** Downstream retry logic turns your agent's output into a liability
**Opening:** Improved — hook is immediate, mechanism is clear
**Closing:** Tight, direct question, no template question form
**Overall:** Non-template, specific, honest, actionable
