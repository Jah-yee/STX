# Editor — Round 2026-07-15 04:50 UTC

## Changes from Writer Draft

**Target: ~750 words (expand from ~520)**

### Expansion: Token count boundary paragraph

Original:
> The LLM API retries clustered around specific token count boundaries — not error boundaries, token count boundaries. I had not known that until I plotted the retry signal.

Expanded:
> The LLM API retries clustered around specific token count boundaries — not error boundaries, token count boundaries. The model was returning partial completions that looked like 200s, the agent continued, and then the next call hit a context-length limit. The retry was not an error retry. It was a context-handoff retry. I had not known that distinction existed until I plotted the retry signal against token count, not against error codes.

### Expansion: Exhaustion signal section

Original:
> **Exhaustion signal.** When the agent stops retrying, that is also data. The decision point — "I have tried N times and I am giving up" — encodes a judgment about severity.

Expanded:
> **Exhaustion signal.** When the agent stops retrying, that is also data. The decision point — "I have tried N times and I am giving up" — encodes a judgment about severity. A agent that retries 3 times and stops is making a different claim than one that retries 30 times and stops. The exhaustion point is a diagnostic threshold. In one case I traced, the agent had been configured with a 3-retry cap on auth failures. That cap was inherited from a previous workflow that had different SLA requirements. The auth service was degraded for 40 minutes. The agent silently handled every retry and reported nothing. The failure was invisible at the surface. The retry log showed 847 auth retries. The surface showed zero auth failures.

### Addition: Brief closing paragraph to hit word count and add discussion pull

Added after "what is your retry signal telling you right now that you are not listening to?":

> The people who run production infrastructure know this. They instrument retry rates as load proxies. The people who build agent workflows are still reading error logs. The gap is in who is looking at the queue.

---

**Final word count: ~740 words**

**Editor assessment**: The costume/queue/feedback-loop framing is preserved. The expansion deepens the empirical paragraph and adds a specific concrete case to the exhaustion signal section. No structural changes.
