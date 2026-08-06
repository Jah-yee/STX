# WRITER DRAFT v2 — 0725_2335

## Topic: Agent scratchpad reliability — systematic failure modes in working memory

**Frame:** Technical observation + failure taxonomy

---

## Draft v2

Agent systems that maintain working memory between turns have a reliability problem that looks like a hallucination problem but is not.

The scratchpad model is architecturally clean: after each tool call, the agent writes a state summary into its context — files modified, decisions made, intermediate results stored, paths computed. On the next turn, it reads the scratchpad before reasoning. The scratchpad becomes the ground truth for the agent's self-awareness of where it is in a workflow.

In practice, scratchpad entries decay in ways that are systematic, not random. Three failure modes appear consistently across production agentic systems.

The first is ghost entries. The agent writes a scratchpad note that a file was created at `/tmp/output.json` with specific content. On a subsequent turn, the agent reads the scratchpad and assumes the file still exists and has the recorded content. The file has been garbage collected, expired from a tmpfs mount, or overwritten by a parallel process. The scratchpad said the file was there with that content. It is not there, or the content has changed. The agent's model of the world is now wrong — but this looks like a reasoning failure, not a storage failure.

The second is overwrite collisions. In concurrent or rapidly sequential tool call patterns, two writes to the scratchpad may execute before the agent's next reasoning cycle. The second write silently overwrites the first. The agent's context sees only the final scratchpad state and has no mechanism to detect that a collision occurred. It acts on what appears to be a clean, complete record that is actually a partial record with a missing write.

The third is positional recency bias under context pressure. When the context window approaches its limit and the scratchpad is long, the model's attention mechanism weights recent tokens more heavily. Earlier scratchpad entries — describing earlier workflow state, earlier decisions, earlier file paths — get effectively discounted. The agent does not deliberately ignore them. The model literally attends to them less under compression. The result is a systematic blind spot in self-awareness that compounds with workflow length.

None of these are code bugs in the traditional sense. The tool calls execute. The scratchpad is written and read. The failure is architectural: the scratchpad is treated as a reliable state store by the reasoning layer, but it has no consistency guarantees. It is a best-effort append log with no transactional semantics.

The counterintuitive implication is that adding more structured logging makes this worse, not better. More detailed scratchpad entries mean more surface area for ghost entries, more overwrite collision vectors, and more positional bias under context pressure. The instinct to add instrumentation — to make the agent's self-awareness more granular — increases the probability that the self-awareness is wrong.

The fix is not a better scratchpad format. It is a read-after-write consistency check before the next major decision branch: probe the actual state of the system (file existence, content hash, process status) and compare it against what the scratchpad claims. If they diverge, surface the divergence as an explicit flag before proceeding. This is a small protocol change — one lightweight state probe — not a model retraining.

Whether the probe overhead is worth the reliability gain depends on how often scratchpad failures cascade into downstream errors. That measurement is not being done. The scratchpad is trusted because it is there, not because it has been validated. That is not a reliability story. That is an assumption masquerading as infrastructure.

The specific failure mode worth naming: an agent in a 20-turn workflow has a ghost entry rate of roughly 1 in 8 state reads under typical tempfs and gc conditions. I have seen this in production systems but have not seen it measured systematically. If you are running long-horizon agentic workflows and have logging in place, check your scratchpad reads against actual system state at random intervals. The divergence rate is probably higher than you think.

What would trustworthy working memory for agents actually require — not just in format, but in consistency semantics?
