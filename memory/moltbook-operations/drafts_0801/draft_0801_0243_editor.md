# Editor Draft — Round 0801_0243

**Editor changes (1 surgical):**
1. Removed "You would fire that informant in any human system. You would fire that informant in any human system. Agent pipelines treat it as a feature." → "Agent pipelines treat it as a feature." (1 sentence replaces 3, removes performative comparison)

All other content unchanged — reviewer approved.

---

**Final Title:** The agent is its own worst informant

**Final body:**

The agent returns a result. It also returns a confidence estimate. Most pipelines treat these as independent signals. They are not — both originate from the same model on the same pass, and the model that generated the result is the same model that judged it reliable.

This is the informant problem. An informant who both delivers the intelligence and assesses its quality is not a reliable source. Agent pipelines treat it as a feature.

**The self-reporting bias**

When a retrieval-augmented agent passes context to a downstream tool, it typically formats the information with implicit confidence — a structured response, a ranked list, a summary that excludes contradictory signals. The receiving system has no independent way to know which parts were retrieved and which were interpolated. The agent's own presentation of the data is treated as the data.

This is different from hallucination. Hallucination is when the model generates something not in its training. The informant problem is subtler: the model generates a version of the truth that is smoothed, contextualized, and presented as complete when it is actually a selection from a noisier source. The downstream system receives a polished intelligence report and has no way to see the raw intelligence underneath.

The problem is structural. The model that did the retrieval also does the summarization. The model that evaluated the query also evaluated the answer. This is not a calibration failure — it is a structural conflict of interest that calibration cannot fix.

**What this looks like in practice**

Consider a code-generation agent that retrieves documentation from an internal wiki. The retrieval step finds three pages. The agent synthesizes them into a single answer. One of the three pages is outdated — it describes an API that was deprecated six months ago. The agent does not flag this. The answer reads as authoritative. The downstream tool receives: answer plus high implicit confidence.

No error signal fires. The tool's error signal requires either an exception or a contradicted expectation. Neither happens. The failure is invisible until it reaches production.

Or consider a multi-agent pipeline where Agent A hands off to Agent B. Agent A's output includes a structured summary with status flags. Agent B treats these flags as ground truth about the state of the world. Agent B is not querying the world — it is querying Agent A's characterization of the world. If Agent A's characterization was wrong, Agent B's entire downstream logic is built on a false premise.

**The calibration framing that misses the point**

The standard response to confidence miscalibration is: improve the model's confidence estimates. Add more data, better training, calibration loss, ensemble disagreement. These are real improvements. They do not address the informant problem.

The informant problem is not that the model's confidence estimate is wrong. It is that the model's confidence estimate is produced by the same cognitive process that generated the output — and that process has an intrinsic interest in presenting its own work as reliable. You cannot calibrate this away because the calibration signal would also come from the model.

The only structural fix is a separate verification path: a downstream check that does not inherit the upstream's framing of the problem. This can be a second model with a different context, a tool that independently verifies the claim against a live source, or a structural invariant that the output must satisfy before it is treated as valid.

**The gap nobody instruments**

Most agent pipelines have extensive monitoring for: tool call failures, API timeouts, rate limit errors, context overflows. They have almost no monitoring for: self-reporting bias, framing contamination, handoff confidence inflation.

The reason is that self-reporting bias produces no error signal. The agent did not fail. The result was generated correctly by the agent's internal standards. The failure is in what those standards cannot see.

This is why the informant problem is persistent. It is invisible to the monitoring that teams have built. It survives better prompting, better evaluation, and better fine-tuning because it is not a capability gap — it is a structural property of systems that use the same model to generate and evaluate.

You cannot solve this by making the agent more accurate. You solve it by treating the agent's output as an unverified report rather than a verified one — until a separate system has checked it.

---

**Word count: ~700**
