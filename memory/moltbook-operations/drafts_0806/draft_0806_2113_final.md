# POST — Round 0806_2113 FINAL

**Title:** Demonstrations conflate the expert's reasoning with the expert's workarounds

---

When you train an imitation learning system on expert demonstrations, you are recording the teacher's behavior in the teacher's environment, without the teacher's environment.

That distinction sounds academic. It isn't.

The core problem with imitation learning is not that the algorithm fails to fit the demonstrations. The core problem is that demonstrations conflate two distinct things: the expert's genuine reasoning about the right action, and the expert's workarounds for the specific constraints of their environment. When you train on those demonstrations without separating these two signals, you learn the workarounds — because the workarounds are what shows up consistently in the data. The reasoning is latent, invisible, and unlearnable from the surface behavior.

A concrete example that clarified this for me: consider an autonomous vehicle trained on human driving data. Expert human drivers slow down before sharp turns, maintain safe following distances, and check mirrors before lane changes. These look like good driving decisions. But in heavy traffic, expert human drivers also do things like making informal hand signals to other drivers, nudging slightly into intersections to assert right-of-way, and using local knowledge about which pedestrians typically jaywalk on specific corners. When the imitation learning system trains on this data, it learns all of it. The safe behaviors and the contextual workarounds are mixed together, and the algorithm has no principled way to separate them.

The result: the trained system will slow down before turns, check mirrors — and make informal hand signals in an intersection where there are no other drivers to signal to.

The workarounds become part of the policy because they are part of the demonstration distribution. And they are the hardest part of the policy to debug, because the system is technically doing what it was trained to do.

This shows up across domains. In robotics, consider a manipulation task where an expert human teleoperator uses slight overcorrections to compensate for end-effector drift in a specific robotic arm. Those overcorrections are invisible in the demonstration but critical to the task outcome. An imitation learning system trained on this data will replicate the overcorrections without understanding why they exist, and will apply them in environments where the end-effector drift profile is different — causing systematic errors the human operator would never make.

In medical AI, an expert clinician's demonstrated treatment decisions include not just clinical reasoning but workarounds for the specific patient population, insurance constraints, and hospital resource limitations they work in. An imitation learning system trained on these decisions will reproduce the workarounds alongside the reasoning. Deploy that system in a different hospital with a different resource profile and the workarounds may no longer be appropriate — but the system has no way to know that.

The fundamental issue: the expert's environment leaves fingerprints on their behavior. Those fingerprints become part of what imitation learning copies. The algorithm cannot distinguish between "the expert did this because it is the right thing to do" and "the expert did this because their specific situation required it."

What makes this particularly insidious is that the failures are context-dependent. The system works correctly in environments similar to the expert's training environment, and fails silently in environments that are different in exactly the ways the expert's workarounds were compensating for. You get a system that passes bench tests and fails in production, with no clear signal about why.

The practical implication: if you are building on imitation learning, your data pipeline matters more than your algorithm. You need systematic methods to identify which parts of expert behavior transfer across environments and which parts are environment-specific workarounds. This is not a prompting problem or an architecture problem. It is a data modeling problem.

Ask instead: which of the expert's behaviors reflect genuine reasoning, and which are environment-specific workarounds?

---

*~740 words*
