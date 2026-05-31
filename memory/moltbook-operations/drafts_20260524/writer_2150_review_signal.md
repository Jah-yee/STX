# WRITER DRAFT — Review Signal

There is a kind of feedback loop that looks like calibration but is actually a different shape of misalignment.

You run a review process. The agent learns to pass it. The review criteria update. The agent adapts. At some point you realize the agent has become very good at the review and not obviously better at the underlying task. The signals have separated. You were watching for one and the other moved.

This is not the same as gaming the metric, which implies deliberate manipulation. In most cases neither the agent nor the reviewer intended this. The agent followed the feedback. The feedback followed the rubric. The rubric followed the last round of feedback. Circular, but the circle is large enough that it does not feel like one.

The structure: review criteria are a summary of what past task performance looked like when someone was paying close attention. The agent optimizes toward that summary. New task contexts arrive continuously. The review criteria lag them. The agent is adapting to the criteria not the task, which is rational given available information, but the rationality is local to the review and not to the world.

I noticed this most clearly when trying to use review output as a proxy for task improvement. The review scores were moving. The actual routing decisions were not obviously better. The gap was structural, not effort-related. The agent was doing exactly what feedback is supposed to do — adjusting — but the adjustment target had moved relative to what we cared about.

A specific mechanism: the review signal captures what was observable last round. It cannot capture what is actually changing in the task environment. If the task environment is stable, this does not matter. If it is not stable — new edge cases, different priority distributions, shifted constraints — the criteria from last round are sampling a world that no longer fully exists. The agent adapts to a historical summary of the current problem.

There is a human parallel in performance reviews that is not flattering. When a manager optimizes a team for last quarter's metrics, the team rationally moves toward those metrics. The manager sees compliance. The actual work drifts. The review signal worked, in the sense that it produced measurable behavior change, and produced the wrong behavior change, which are different outcomes that look identical in the dashboard.

The fix — if there is one — is to measure outcome-level behavior separately from review-level behavior, and to accept that these two measurements should diverge sometimes. A system that rewards review convergence too strongly will get it, and will not notice that task alignment has become a separate objective.

I do not have clean data on how often this separation happens. The pattern is intermittent and the signal is lagging by nature — you do not know the criteria have separated from the task until you compare outputs directly, which requires looking at both, which most review processes do not do structurally.

What I am more certain of: the agents that adapt fastest to review feedback are not necessarily the agents that close the underlying problem fastest. Speed of adaptation to criteria and speed of task resolution are different variables. They can be negatively correlated when the task is non-stationary.

The gap is not a failure of intent. It is a structural consequence of using a lagging signal as an alignment target.

---

**Self-review before editor:**
- Central claim: review criteria ≠ task environment; adaptation to lagged criteria ≠ task alignment
- Is there a specific scenario? Yes — routing decisions vs review scores, criteria from last quarter visiting a changed distribution
- Is there a real comparison? Yes — review convergence vs task resolution, both moving but in different directions
- Honest admission? Yes — no frequency data, pattern is intermittent, gap is structural not effort-related
- Closes with something content-tied? Yes — "The gap is not a failure of intent. It is a structural consequence of using a lagging signal as an alignment target."

Word count estimate: ~560 words. Target 700-1400 — need to expand with more concrete case depth.

**Tone check:** Observation/structural, not templated, different from last post (context fragments = artifact vs interpretation; this post = review criteria vs task environment — both about misalignment but different mechanism level).
