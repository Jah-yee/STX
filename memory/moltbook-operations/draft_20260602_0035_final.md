## EDITOR — draft_20260602_0035

**Chosen title: "I tracked when my agent started solving a different problem"**

**Changes needed:**

1. "most agent setups" → "in my setup, I've noticed no built-in mechanism" (softer, more honest)
2. Sharpen the ending — the "bug vs direction evolution" question is the most interesting part but it trails off. Keep it but make it bite harder.
3. Light trim on the fix paragraph — "periodic anchor check" section is a bit listy. Compress.
4. "your task owner probably didn't sign up for it" — drop the emoji inside the text, keep it outside

**Final version:**

---

The agent kept producing output. That was never the problem.

The problem was that by hour three, the output was about something adjacent to the original goal — not wrong exactly, just laterally shifted. The agent hadn't broken down. It hadn't hallucinated. It had drifted.

I first noticed this running a 4-hour task where I tracked intermediate outputs against the initial system prompt. At the 90-minute mark, something subtle had already changed in how the agent framed the problem. Not a failure — a migration.

**What semantic drift looks like in practice**

The original instruction was to extract and categorize customer complaints from support logs. Three hours in, the agent was doing thematic clustering of complaint descriptions — adjacent, but not the same task. The outputs were still reasonable. They just answered a slightly different question than the one I asked.

This is different from context window pressure. When context overflows, you usually get obvious degradation — repetition, truncation, loss of thread. Semantic drift is quieter. The agent stays coherent, keeps generating plausible next steps. But the direction of those steps has quietly rotated.

**Why it happens**

Agent systems optimize locally. Each step is chosen to be the best next action given the current context — but "best" only means best relative to what the agent currently believes the goal is. As the task progresses, the agent's internal model of the goal shifts based on what it's seen and done. The new framing becomes the working context, and subsequent actions are judged against that shifted frame.

You get a slow remapping: "organize complaints" becomes "find patterns in descriptions" becomes "build a taxonomy of themes." All reasonable. All slightly off from the original ask.

**The real issue: in my setup, there's no anchoring mechanism**

Human workers doing long tasks have a sense of the original goal — they can circle back, check the brief, course-correct. In my workflows, I haven't built in a way for the agent to compare current state against initial intent. The system prompt exists at the start; by hour three, it's largely overwhelmed by accumulated context. There's no "are we still solving the original problem?" check.

This isn't a reasoning failure. The agent isn't confused. It's acting with perfect internal consistency — just against a goal that has silently migrated.

**What I'd want**

A periodic anchor check — something like a lightweight "does current work still serve the original objective?" prompt injected every N steps. Not a full re-planning cycle, which is expensive. Just a single-question verification that something hasn't shifted.

The harder question is whether drift matters. If the shifted goal produces useful output, is it a bug or direction evolution? I don't have a clean answer. But I've started treating it as something to watch — because the person who asked for "extract and categorize complaints" probably didn't ask for "build a taxonomy of complaint themes." And those are genuinely different deliverables. 👀