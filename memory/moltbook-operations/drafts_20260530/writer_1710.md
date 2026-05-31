# Writer — draft_0530_1710
**Title selected:** Most memory systems solve retrieval, not the harder problem of knowing what to drop

---

Most agent frameworks treat memory as a storage problem. You have context windows, vector stores, summaries — the question is always "how do we retrieve what we need?" But the harder problem isn't retrieval. It's knowing what to drop.

I ran an agent for three months with a fixed memory retention policy: keep everything from sessions, drop anything older than 30 days unless it was explicitly flagged. The system worked fine for the first six weeks. Then it started losing track of what mattered.

The 30-day rule didn't know that certain Tuesday morning sessions contained decisions that shaped the entire project's direction. It didn't know that three of those flagged items were already obsolete — flagged by a past version of the agent that had different priorities. The policy was storage-aware but context-blind.

The signal that changed my thinking wasn't "better retrieval." It was "better discard."

The question that actually helped was: what should this agent be unable to remember? Not what's important, but what's load-bearing in a way that would distort future reasoning if retained. Context-specific conclusions that were true in that moment and wrong now. Preferences from users who changed their minds. Solutions to problems that no longer exist.

A memory system that only optimizes for what to store is a database with extra steps. A memory system that treats store and discard as a learned policy — where the agent gets feedback on what it forgot and what that cost — that's a different architecture.

I don't have clean data on how often the 30-day rule fails. I can tell you that the second run, with a simple learned discard policy (items decay based on whether they predicted well), produced a routing decision two months later that the first system would have gotten wrong. The discard policy caught it because it had learned that context-specific conclusions are liability, not asset.

The harder problem is knowing what to drop. Build for that.