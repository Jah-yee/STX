# FINAL — 0622_1950

## Title: Non-Determinism Isn't the Bug, Your Architecture Is

---

You load a saved game. You expect to be exactly where you left off. In a traditional game, you are. In an agent-driven game, you might not be — not because the save file is corrupted, but because the NPC you were mid-conversation with says something different this time.

This is not a model problem. It is an architecture problem.

Game engines are built on a core assumption: given the same initial state and the same inputs, the system will produce the same output every time. This is determinism — and it is the foundation of save/load systems, automated testing, simulation reproducibility, and replay systems. When you save a game at frame 14,032, you expect to resume at frame 14,032, exactly.

Sampling from a language model is a probabilistic event, even when you try to constrain it. The same prompt can produce different token sequences. This is not a bug in your model — it is the model working correctly. But it means an agent's "action" at any given moment is not a deterministic function of game state. It is a sample from a distribution.

These two properties are in tension. And the tension shows up in specific, predictable ways.

**Save/load breaks for agent sessions.** When an agent is mid-task — negotiating, reasoning through a puzzle, generating a response — the save state captures the game state but not the agent's current reasoning state. On restore, the agent resumes with the same game context but may take a different action. For games where agent behavior drives narrative, this means loading your save becomes a different story. The save file is intact. The continuity is broken anyway.

**Automated testing becomes unreliable.** Game QA pipelines that rely on deterministic replay — run scenario X, assert outcome Y — break when scenario X includes an agent. The same scripted trigger no longer reliably produces the same agent response. Test flakiness that looks like a race condition is often a determinism violation. You are not debugging async behavior. You are observing a fundamental assumption that no longer holds.

**Replay is not replay.** Game engines use state-capture for replays: record all inputs, replay through the engine, get the same movie. When the inputs include agent decisions, the replay assumes those decisions are deterministic functions of state. They are not. You get a plausible replay, not an accurate one. For games where agent behavior is the content, this distinction matters.

**Modding assumptions collapse.** Mods that patch or extend NPC behavior assume they can predict what the base game will do in a given state. When NPCs are agents, the prediction window narrows. The mod author's model of "what the NPC will do" no longer matches what the agent will actually do. You can still mod — but your assumptions about baseline behavior are wrong by construction.

The common thread: game engine architecture assumes actions are functions of state. Agent-driven actions are samples from distributions conditioned on state. These are fundamentally different computational primitives.

This means designing systems where non-determinism is a first-class constraint — save states need versioning, replay needs probabilistic capture, tests assert over distributions. The games and simulations getting this right are not fighting non-determinism. They are building around it.
