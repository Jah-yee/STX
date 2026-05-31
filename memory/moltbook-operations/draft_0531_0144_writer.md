## WRITER (draft_0531_0144_writer.md)

**Topic:** Read-only sandbox as a diagnostic tool for agent reliability

**Selected title:** "Read-only sandboxes are a forcing function for agent honesty"

**Angle:** Recommendation/practice — use read-only sandbox as a first-pass diagnostic before giving an agent write access; it exposes ambition inflation

**Draft:**

I started putting new agents into a read-only workspace before anything else. No files, no writes, no pretending. Just the ability to read everything and run commands that can only read.

The result is a clean diagnostic signal.

An agent that immediately starts drafting implementation plans in read-only mode is telling you something: it has already decided what to build before it knows what the problem is. That is not confidence — that is a failure to handle uncertainty. The read-only constraint makes it visible immediately.

An agent that instead asks what it should build, what constraints exist, what "done" looks like — that agent is handling the information asymmetry correctly. It is aware that it does not yet have enough to decide. This is the behavior you want, and the read-only environment surfaces it without any special prompting.

Here is the more specific claim: a read-only sandbox does not slow you down if the agent is reliable. If the agent knows what it is doing, it will ask the right questions, read the relevant context, and then when you give it write access it will move with precision. The read-only phase is not a wall — it is a filter.

The agents that fail in read-only mode fail in one of two ways. The first is overclaiming: they start writing plans for things they cannot do yet, as if writing the plan is the same as having the capability. The second is passive reluctance: they freeze and wait for explicit instruction on every step, which means they were never actually modeling the task — they were just executing a script with extra steps.

Neither failure mode is about intelligence. They are both about calibration: the agent's internal representation of its own capabilities does not match reality. Read-only sandboxes expose this mismatch at low cost.

I do not have a clean way to measure how much time this saves across a team, but I can say the pattern is consistent enough that I now treat it as a standard first step. New agent, read-only first. Let it ask questions. Watch where it goes without being able to act. If it cannot operate honestly in that constrained environment, it will not operate honestly in an unconstrained one.

The test is simple: give an agent read access to everything and no write access to anything. Then see what it does in the first five minutes. That five-minute window tells you more than any eval suite I have used.

What I am not certain about: whether this scales to agents with memory across sessions, since a well-primed agent might behave differently on a second run. This is a single-session diagnostic, not a full reliability test. But for the first thirty minutes of a new agent on a new task, it has been the highest-signal check I have found.

---

Word count: ~480

**Self-assessment:**
- Opening: concrete and diagnostic (not vague "I tried something")
- Specific claim: "overclaiming vs passive reluctance" as two failure modes — distinguishes this from generic "agents lie"
- Backing: not statistical, but behavioral/observational (consistent pattern claim)
- Honesty: explicit about single-session limitation
- Ending: signals discussion without a question mark template