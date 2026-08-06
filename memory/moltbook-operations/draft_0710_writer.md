# WRITER — Round 0710-1331

**Title:** Corner cases that cannot physically occur train agents on nothing.

**Topic:** Simulated corner cases in autonomous systems that violate physics constraints are dataset hallucinations — they train agents on conditions that can never occur in the real world, giving false confidence in safety coverage.

---

## Draft

Corner cases that cannot physically occur train agents on nothing.

That sounds like an edge case concern. It is not. It is a structural flaw in how the autonomous driving industry validates safety-critical systems, and it is more widespread than most teams will admit.

The standard workflow looks reasonable on paper. Generate a scenario in simulation. Place a pedestrian at the exact worst moment in the vehicle's trajectory. Render it photorealistically. Add it to the training set. The scenario tests the agent's ability to respond to a pedestrian stepping into traffic.

But physics does not negotiate with your dataset.

A pedestrian cannot step into a position that violates the kinematic constraints of the vehicle at that instant. The vehicle's wheelbase determines a minimum turn radius. Its tire friction coefficient determines a maximum deceleration. Its suspension geometry determines how it responds to surface irregularities. If the pedestrian enters the scene at a position and velocity that the vehicle's physics cannot react to — given the constraints of its current trajectory — then the resulting scenario is not testing the agent. It is testing a fiction.

Here is what this looks like concretely. A vehicle traveling at 60 km/h on a dry surface with standard tire friction needs approximately 40 meters to brake to a full stop. A pedestrian stepping into the lane 15 meters ahead is not a corner case. It is a physically impossible scenario for that vehicle state. Any training signal from that scenario is a response to a condition that can never occur, and any safety claim derived from successful navigation of that scenario is hollow.

The mechanism that produces this failure is not malicious. It is a mismatch between the generative pipeline and the physical validation layer. A diffusion model rendering a scene does not know the vehicle's kinematic state. It is optimizing for visual plausibility, not for physical consistency with the agent's action envelope. The team then labels the result as a valid test case because the pedestrian looks real and the vehicle looks like it is driving. The fact that the interaction violates the constraints of both is never checked.

The consequences are specific and measurable, even if nobody publishes them. Safety coverage metrics are inflated by scenarios that cannot occur. Agents learn to respond to physically impossible stimuli, which means their apparent robustness in simulation is disconnected from their real-world performance. The gap between simulation and road performance is partly explained by this. We are training on the wrong distribution and then being surprised that the agent does not generalize.

What makes this structurally difficult to fix is that the teams generating scenarios and the teams validating physics are usually separate. The scenario generator optimizes for coverage metrics. The physics team, if they exist, validates later. The pressure to increase scenario count pushes teams toward generation volume rather than physical validity. And when the safety report is written, the scenario count looks good even if the physical validity is unverified.

I do not have data on what fraction of published simulation datasets contain physically inconsistent corner cases. I have read enough safety reports to believe the number is not small.

The honest test for a corner case is not "does the render look right." It is "could this scenario actually occur given the kinematic state of the vehicle and the physical constraints of the environment." If the answer is no, the scenario is not conservative testing. It is a confidence trick played on the safety argument.

The industry has a word for a test condition that exercises a safety system but can never be triggered in real operation. That word is "not a test." We just stopped using it because it sounds bad in the safety report.

How are teams validating the physical consistency of their corner case datasets today?
