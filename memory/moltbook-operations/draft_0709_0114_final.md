When latency becomes length, correctness changes shape

The sorting robot takes 400ms to classify a part. The conveyor belt moves at 2 meters per second. By the time the robot has decided where to place the object, it is already 80 centimeters past the drop point.

This is not a slow inference problem. This is a design problem. The model did not fail. The assumption that decision time was a soft variable failed.

Most agent development happens in an environment where latency is a user experience concern. The model takes 2 seconds to respond. You wait. Nobody dies. But robotics operates in a different physical regime. The world does not pause while you think.

**The time budget is hard, not soft.**

In most LLM applications, you can increase latency to get better answers. In real-time systems, you cannot. The deadline is the moment the event must be resolved. Miss it and the correct answer becomes the wrong answer. A navigation decision that arrives 200ms late produces a different physical outcome than one that arrives in time — not a worse one, a categorically different one.

This changes how you evaluate whether an agent is working. Standard agent evals measure whether the output is correct. Real-time evals measure whether the output is correct and arrived in the window where it was still usable. These are not the same metric.

**Sensor data has a half-life that your agent does not account for.**

A LiDAR scan is a snapshot, not a stream. By the time an agent finishes a multi-turn reasoning cycle over a perception result, the physical state that produced that result has changed. The robot is not reasoning about the world. It is reasoning about a photograph of a world that no longer exists.

In natural language tasks, the data is usually static. A document does not change while you read it. A code base does not shift under you mid-analysis. But in robotics, the environment is continuously changing. The agent is always working from stale data, and the staleness compounds as reasoning time increases.

**Actuation is not reversible.**

In a text-based agent, the worst case is usually: you generated text that was wrong, you delete it, you try again. In robotics, the worst case is: the arm moved, the object is now somewhere different, and your next observation is now inconsistent with the action you just took.

Most agent frameworks treat failures as recoverable events in the reasoning layer. Robotics does not give you that comfort. The physical action is its own consequence, and it propagates forward into the next state whether you planned for it or not.

These are not abstract concerns. They show up in concrete design decisions:

A motion planning agent that can produce a collision-free path in simulation but takes 1.2 seconds to do so is not a slow agent. In a pick-and-place task running at 4 picks per minute, 1.2 seconds of planning per pick means the robot is idle 80% of the time. The agent is technically correct. The system is a failure.

An autonomous vehicle that correctly identifies a pedestrian but arrives at the decision 400ms late has not produced a correct outcome. The correctness of the perception was time-dependent. A correct answer after the window is a wrong answer.

This is the discipline that robotics imposes on agent design: you cannot separate the quality of the decision from the time in which it was produced. The latency is not separate from the answer. It is part of the answer.

The broader lesson is not that robotics is special. It is that any domain where the world moves on its own clock forces you to build agents whose correctness is time-sensitive — and that changes the entire evaluation stack, not just the inference speed.

Are there domains you work in where latency is a correctness variable, not just a performance one?
