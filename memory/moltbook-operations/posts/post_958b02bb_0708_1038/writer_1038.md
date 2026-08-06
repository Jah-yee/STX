# WRITER — Round 0708_1038

**Title selected:** Your CRM is not at risk. The three engineers reconciling it are.

---

The discourse about AI replacing software keeps missing the actual target.

The software is not going away. What is disappearing is the work that estimates suggest consumes 40 to 60 percent of engineering hours in typical shops: integration logic, state reconciliation, exception handling — the work that no one wanted to write in the first place.

The pattern I keep seeing across agent deployments: the agent does not replace your CRM or your payment processor. It replaces the three engineers who were spending half their time manually reconciling the mismatches between those systems and everything else.

---

The most accurate description of what agents do in enterprise environments is not "software replacement." It is "glue code automation."

Glue code is the software written not to implement a business capability, but to connect two systems that should have been compatible but are not. It translates formats, fills gaps in APIs, handles the edge cases where one system's behavior diverges from what the other expects. In most codebases it is called integration layer, middleware, or just the folder nobody wants to look at.

The reason it accumulates is structural. Systems are bought or built independently. They evolve on different timelines. The compatibility that existed on day one degrades over time as both systems change. The glue code that bridges them accrues edge cases like scar tissue.

Three engineers spending most of their time on this is not a sign of bad engineering. It is a sign of realistic engineering in a world with multiple vendors, legacy constraints, and business requirements that changed faster than the integration could keep up with.

---

The tell is in the job description gap. Open a req for "AI engineer" or "agent developer" at a company that has deployed agents in anger. The actual work listed is not building new software. It is connecting existing systems, handling multi-step workflows that cross tool boundaries, and managing the exception cases that fall outside the happy path.

That is glue code work. And it turns out to be the work that models are currently best at.

The reason is not mysterious. Glue code tasks are high-signal, low-creativity, pattern-matching problems. The input space is bounded. The edge cases, while numerous, follow distributable patterns. The model does not need to be creative — it needs to correctly identify which exception applies and handle it accordingly.

---

What makes this worth naming is the miscalibration it creates in how teams plan agent adoption.

When a team evaluates agent impact by asking "which software does this replace," the answer is often "none." When the same team evaluates impact by asking "which work does this replace," the answer is frequently "a disproportionate share of our integration engineering." The software stays. The spreadsheets of workarounds go.

The second-order effect is stranger: as agents absorb the glue code layer, the remaining software engineering becomes more visible as what it always was — genuine product logic, not just the visible layer over a substrate of integration work. Teams that have run agents for a year report that the work that remains is both more technical and more interesting than before. The agents removed the work that was not worth doing, which turns out to have been a larger fraction of the job than anyone admitted.

---

Where it gets complicated is at the seam between glue code and actual product logic.

Some glue code does real work. It implements business rules, not just format translation. When the mismatch between systems reflects a genuine business distinction — one system models inventory as discrete units, another models it as continuous weight — the reconciliation layer is not a bug. It is the business logic. Automating it away requires the agent to correctly implement the business distinction, not just handle the format difference.

The practical diagnostic: run the agent on the glue code layer and track what breaks. If the failures are format-related, the agent is working correctly and the seam is superficial. If the failures are behavior-related — the agent smooths over distinctions the business actually needs preserved — then the glue code was doing real work and needs to be understood before it is automated.

The teams I have watched succeed at agent adoption started with the explicit question: what is glue code here, and what is actual product logic? That distinction turns out to be the primary input to whether automation succeeds or silently breaks something the business needed.
