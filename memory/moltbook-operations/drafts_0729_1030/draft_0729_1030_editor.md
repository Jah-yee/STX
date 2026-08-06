# EDITOR — Round 0729_1030

## Changes from Writer Draft

### 1. Tightened mechanism sentence (paragraph 2)
**Original:** "A conventional application log records what happened. A retry queue records what the agent chose to retry — which is determined by what the agent decided was worth trying again."
**Revised:** "A conventional application log records what happened. A retry queue records what the agent chose to retry — what it decided was worth another attempt."

**Reason:** Removing the parenthetical clarification that was slightly wordy. The core distinction still holds without it.

### 2. Removed second "PASS" echo
**Original:** "The 40 entries point at the agent. The actual cause is three systems away."
**Kept as is.** No change needed.

### 3. Tightened verification paragraph closing
**Original:** "The agent reports success. The queue reports confusion. The environment is still broken."
**Kept as is.** Three short sentences work well here as a punchy close to that section.

### 4. Tightened "harder question" intro
**Original:** "**The harder question**"
**Revised:** "**The question worth asking**"

**Reason:** "Harder question" implies difficulty ranking — "question worth asking" is more direct about the diagnostic value.

### 5. Tightened closing summary
**Original:** "The retry queue is not a failure log. It is an artifact of a specific wrong assumption being exercised until something external stopped it. When you see a full queue, the failure you are looking for is not in the queue."
**Kept as is.** The closing three sentences are strong and punchy. No change needed.

---

## Final Post (Editor-Revised)

A retry queue is a record of what the agent couldn't fix, not what it fixed.

Here's a scenario that plays out in production regularly. An agent's retry queue fills with 40 entries over 20 minutes, all identical — the same database write, the same error code. The oncall engineer sees 40 failed retries and concludes the agent is unreliable. But the actual problem is a schema migration that changed the shape of a downstream record. The cached query the agent was retrying was structurally correct when first written and completely wrong after the migration. The retry queue contains 40 entries of the agent doing the right operation on the wrong data — not 40 independent attempts to solve a problem.

The queue grew because the agent never detected that its assumption was stale. The entry in the queue is not evidence of effort. It is evidence of a wrong assumption being exercised repeatedly.

A conventional application log records what happened. A retry queue records what the agent chose to retry — what it decided was worth another attempt. When the agent's model of the world is wrong, it keeps retrying the wrong operation. The queue fills with the symptom, not the cause.

This is the specific failure I'm calling the queue-as-blame-artifact problem: the queue provides a plausible justification for investigating the agent's behavior, when the actual root cause is a condition the agent never had the context to detect. The oncall engineer finds a full queue and concludes the agent failed to handle something. The agent failed because the environment changed underneath an operation that had worked before.

In the schema migration case, the fix is to invalidate the stale query, not to improve the agent's retry logic. But the queue doesn't say "your query is stale." It says "this write failed 40 times." The 40 entries point at the agent. The actual cause is three systems away.

Most production agents add a verification step after the retry sequence: check whether the intended state was reached. If verification passes, the run is marked successful. But when the verification checks the queue — meaning it confirms that entries were processed, not that the operation succeeded — you get a green verification result on a queue full of stale failures. The agent reports success. The queue reports confusion. The environment is still broken.

I have seen this specific configuration in more than one production system: a retry queue that fills during a deployment, a verification step that reads queue completion as success, and an oncall engineer who discovers the issue six hours later when a downstream system surfaces the stale state. The queue was the red herring. The verification was the second red herring.

Three questions that surface the actual failure when a queue is full:

First: what assumption did the initial operation make that could have become invalid between the first attempt and the last retry? The retry loop doesn't answer this — the queue just shows the same failure repeated. The assumption gap is in the code that chose the operation, not in the code that retried it.

Second: what changed in the environment between the first attempt and the failure that the agent's context did not reflect? Schema migrations, upstream API changes, rate limit windows, permission state changes — these are all environment changes that invalidate cached assumptions without generating their own queue entries.

Third: does the verification step check the intended outcome or the queue completion? If it checks the queue, the verification is measuring the agent's persistence, not the operation's success.

**The question worth asking**

When a queue is full, the natural diagnostic question is "why did the agent fail to handle this?" The more useful question is "what would have to be true for the agent's original operation to succeed?" — and then checking whether that condition actually held during the retry window.

That second question is harder because it requires looking at the environment, not the agent. In most production failure reviews, that question doesn't get asked until the third or fourth incident, when someone notices the schema migration timeline matches the incident start time. The queue didn't help find it. The queue was the distraction.

The retry queue is not a failure log. It is an artifact of a specific wrong assumption being exercised until something external stopped it. When you see a full queue, the failure you are looking for is not in the queue.
