# Final — 0730_2015

**Title:** Safety in simulation is not safety in hardware

---

I spent six months building a control policy in MuJoCo. It passed every safety metric I could throw at it: constraint violations near zero, worst-case joint angles within bounds, torques well under limits. The sim was clean. The policy was, by every metric I had, safe.

Then we put it on the actual robot.

The first attempt at the target gait pulled the hip servo past its thermal limit in 40 seconds. The sim had never modeled that. The second attempt exposed a backlash issue in the ankle joint that was invisible at the velocities I tested in simulation. The third was fine for flat ground but folded on a surface 2cm softer than expected.

The simulation was correct. The safety claim was not.

This is not a story about a bad simulator. It is a story about what safety in simulation actually proves — and what it structurally cannot prove.

## What simulation actually tests well

To be precise: simulation tests whether your policy is consistent with your model of the world. It is excellent at this. It will catch whether your cost function is shaped right, whether your policy respects the constraints you encoded, whether your reward signal produces the behavior you intended.

This is genuinely useful. Policy consistency bugs are real bugs. If your policy ignores its own action history in recurrent architectures, simulation will show you. If your safety constraints are violated by numerical instability in the physics engine, simulation will show you.

What it cannot test is whether your model of the world matches the world.

## The structural gap

The failure modes that simulation misses are not random. They are specifically the things that are hard to model: contact dynamics at the boundary of surfaces, soft terrain deformation, thermal servo behavior under sustained load, backlash in mechanical joints, latency in real sensor pipelines, firmware-level jitter that is invisible at the simulation timestep.

These are not noise. They are structure. And they scale with task difficulty in a specific way: the harder the skill you are training, the more the performance surface depends on precisely the things simulation gets wrong.

This is the uncomfortable version of the sim-to-real gap: it is not that your simulator needs better fidelity. It is that fidelity in the wrong dimensions does not help.

## What actually closes the gap

Domain randomization — training across a distribution of simulator parameters — is the most commonly cited mitigation. It works by forcing the policy to find behaviors that are robust to the specific modeling errors it will encounter in reality. It is genuinely effective.

That is the explicit tradeoff: robustness across simulation variance in exchange for peak performance in any single environment. Most papers skip mentioning this cost.

The other approach is to minimize the sim-to-real gap directly: better physical models, system identification pipelines, and frequent sim-to-real comparisons. This is more principled but expensive. It requires that you actually measure the things your simulator is getting wrong, which means instrumenting the real system in ways that are often time-consuming.

Neither approach eliminates the gap. Both reduce it.

## The evaluation problem nobody talks about

What changed my thinking: I used to think the evaluation setup was the bottleneck. Better metrics, more rigorous testing, more simulation time. But the deeper issue is that the evaluation environment and the deployment environment are categorically different, and no amount of evaluation rigor in the simulation closes that gap.

This means the question is not "how do we evaluate more safely in simulation?" It is "what does our evaluation in simulation actually tell us, and what does it structurally miss?"

For easy tasks — ones where the failure modes are well-characterized and the policy does not operate near the edges of physical possibility — simulation evaluation is genuinely informative. For hard locomotion, manipulation at boundary conditions, or any task where the real world introduces unmodeled structure, it is a necessary but insufficient signal.

I do not have a clean solution. The policy from that MuJoCo project eventually worked in hardware, but only after we instrumented the real system, identified the specific modeling errors, and iterated on physical hardware rather than relying on simulation to validate our safety claims.

The simulation was right about the policy. It was wrong about the safety. I stopped conflating them.
