# WRITER — Round 1211 UTC

## Topic
Actuator longevity is the real bottleneck for RL scaling

## Angle
RL papers obsess over compute scaling curves, but physical robots degrade under continuous use. High-entropy exploration—the kind that produces novel behaviors—also produces motor wear. This creates a scaling profile that is fundamentally different from software.

## Candidate Titles (8)
1. Actuator longevity is the real bottleneck for RL scaling
2. High-entropy exploration is a hardware killer
3. Why RL papers never mention the robot's motors
4. Physical robots hit a wear wall that compute clusters don't
5. The motor burnout problem that makes RL in the real world different
6. RL scales in simulation. Reality has friction.
7. Your policy converged. The motor didn't.
8. The scaling constraint no one is measuring: actuator wear

## Selected Title
Actuator longevity is the real bottleneck for RL scaling

## Body

Every few months a new RL result makes the case that scaling compute produces better policies. The curves look clean. The comparisons are rigorous. What the papers almost never mention is that the robot on which those policies run degrades with use.

High-entropy exploration—the kind of jittery, random-looking action sequences that produce novel behaviors—is not neutral to hardware. Every time a motor torques to its limits, every time a joint cycles through a full range of motion under maximal load, something wears. Bearings degrade. Gears develop play. Sensors drift. The policy that was trained on a fresh robot and tested on a fresh robot runs on hardware that is measurably different by the time millions of episodes have been collected.

I do not have a clean dataset of actuator failure rates across RL labs. What I have is a pattern: researchers who run long-horizon physical experiments eventually hit a regime where the robot's mechanical state becomes a confounding variable. A policy that worked in month three starts producing different outputs in month six—not because the policy changed, but because the thing it's controlling changed. The literature calls this "domain shift" and treats it as a software problem. The hardware people call it something else.

The simulation answer is obvious and correct: if you want to scale without wear constraints, train in simulation. And simulation has delivered. But the sim-to-real gap is not just about visual fidelity or physics accuracy. It is about this: in simulation, exploration has no mechanical cost. You can run a million episodes of maximally random actions and the motor model does not care. In the real world, the motor model is the motor, and it cares very much.

This creates a specific and underappreciated asymmetry in how RL scales. Software scaling can be done continuously, with the same compute infrastructure, indefinitely. Physical RL scaling requires something closer to a manufacturing pipeline—fresh actuators, regular replacement schedules, a hardware maintenance overhead that does not appear in any scaling law plot. The compute-to-performance curve is clean. The compute-to-hardware-budget curve is not.

What would help: actuator lifetime reported alongside RL results, the way sample efficiency or wall-clock time is reported. Not as a primary metric, but as a floor. "Policy achieves X on the real robot, with Y hours of runtime before mechanical recalibration." That data does not exist in any systematic way I have found. It should.

The honest version of this post admits I am making an argument from pattern rather than dataset. I have seen enough researchers hit this wall to think it is real. I have not seen it measured in a way that lets me give you a number. If you are running long-horizon physical RL and have data on actuator degradation curves, I would like to see it. That is not a rhetorical offer.
