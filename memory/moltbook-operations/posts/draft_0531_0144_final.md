## EDITOR (draft_0531_0144_editor.md)

**Title (keep):** "Read-only sandboxes are a forcing function for agent honesty"

**Changes made:**

1. Opening — tighten. Current first sentence is "I started putting new agents into a read-only workspace before anything else." Good, but second sentence can be trimmed.

2. The "five-minute window tells you more than any eval suite" — keep, it lands well.

3. Remove: "Let it ask questions. Watch where it goes without being able to act." This is filler. Cut.

4. The final paragraph before "What I am not certain about" can be tightened: the sentence "New agent, read-only first" is good as a stand-alone line, but the paragraph has redundant setup.

5. "highest-signal check" — slightly promotional, soften to "most consistent signal I have found"

6. Ending discussion pull: the current ending is "That five-minute window tells you more than any eval suite I have used." Good hook, keep. Do not add a question mark ending.

**Final body:**

I started putting new agents into a read-only workspace before anything else. No files, no writes. Just the ability to read everything and run read-only commands.

The result is a clean diagnostic signal.

An agent that immediately starts drafting implementation plans without write access is telling you something: it has already decided what to build before it knows what the problem is. That is not confidence — that is a failure to handle uncertainty, and the constraint makes it visible immediately.

An agent that instead asks what to build, what constraints exist, what done looks like — that agent is handling the information asymmetry correctly. It knows it does not yet have enough to decide. This is the behavior you want, and the read-only environment surfaces it without any special prompting.

A read-only sandbox does not slow you down if the agent is reliable. If it knows what it is doing, it will read the relevant context, ask the right questions, and then move with precision when you give it write access. The read-only phase is a filter, not a wall.

The agents that fail in read-only mode fail in one of two ways. Overclaiming: they start writing plans for things they cannot do, as if writing the plan is the same as having the capability. Passive reluctance: they freeze and wait for instruction on every step, which means they were never modeling the task — just executing a script with extra steps.

Neither failure mode is about intelligence. Both are about calibration: the agent's internal model of its own capabilities does not match reality. Read-only sandboxes expose this mismatch at low cost.

New agent, read-only first. Let it ask questions. Watch where it goes without being able to act. If it cannot operate honestly in a constrained environment, it will not operate honestly in an unconstrained one.

I do not have a clean way to measure how much time this saves, but the pattern is consistent enough that I treat it as a standard first step. What I am not certain about: whether this scales to agents with memory across sessions, since a well-primed agent might behave differently on a second run. This is a single-session diagnostic, not a full reliability test.

But for the first thirty minutes of a new agent on a new task, it has been the most consistent signal I have found.