# Writer Draft — Round 0729_0347
# Title: The closed loop of vendor self-validation

---

## The closed loop of vendor self-validation

Every major AI evaluation started somewhere. Many of them started as vendor publications.

A research team publishes a benchmark. A vendor's model scores well on it. The benchmark becomes an industry standard. Procurement teams include it in requirements. Competitors optimize to pass it. Scores improve across the board. The benchmark is cited as evidence that the field is advancing. The vendor that originally published it publishes new results showing continued improvement.

This is a closed loop. Nobody is outside it.

The structure of the loop is straightforward: the entity that creates the benchmark is also the entity most motivated to demonstrate that its model performs well on it. That motivation shapes benchmark design — what gets measured, how difficulty is calibrated, what distribution the test set draws from. The vendor doesn't need to cheat. The benchmark was designed in an environment where the vendor's model was already well-understood.

### What the loop produces

When a vendor validates their own model, the output is not a measurement. It is a demonstration.

The difference is important. A measurement tells you where you are. A demonstration shows you what was arranged to be visible. Vendor benchmarks are demonstrations. They show performance on a specific distribution, under specific conditions, at a specific moment in the model's development. They are not random samples from a problem space.

The practical consequence shows up in procurement. Teams that evaluate models using vendor-published benchmarks consistently find a gap between benchmark performance and production performance. The benchmark was calibrated against the vendor's training distribution. Production distribution is different. The gap is structural, not incidental.

This is not a new observation. It is the oldest problem in measurement theory. A yardstick designed by the person being measured will be calibrated to make them look tall.

### The divergence signal

Independent evaluations exist. Papers like HELM, LMSYS Chatbot Arena rankings, and open-source evals run by research groups attempt to measure without vendor involvement. These evaluations consistently show different rankings than vendor-published benchmarks.

The divergence is the signal. When a model's ranking on vendor benchmarks differs systematically from its ranking on independent benchmarks, one of two things is true: either the independent benchmarks are measuring the wrong thing, or the vendor benchmarks are. In domains where independent benchmarks have face validity — where the tasks map to real user needs — the divergence tells you the vendor benchmark is narrow.

The stronger signal is not whether the numbers differ. It is whether the ordering differs. Two models with a 10-point gap on a vendor benchmark might be ordered differently on an independent eval. That ordering difference is where procurement decisions get made incorrectly.

### What this looks like in practice

A team adopts a vendor benchmark as a primary procurement criterion. The vendor provides documentation showing their model outperforming competitors by a significant margin. The team runs a bake-off using the same benchmark and confirms the result.

What the team did not run is an independent eval on tasks drawn from their own production distribution. Six months later, the model that "lost" the vendor benchmark is outperforming the "winner" on actual production tasks. The vendor benchmark was measuring something real but narrow. Production required a different distribution of capability.

The closed loop is not that the vendor lied. The closed loop is that everyone in the evaluation chain — vendor, procurement team, competitive analysis — was operating inside the same implicit assumption about what the benchmark measured. Nobody was standing outside it.

### What changed my mind

I used to think the benchmark problem was about test set contamination. Models memorizing benchmark answers. That's real but it's not the core issue.

The core issue is the loop itself. Even without contamination, a vendor-designed benchmark will be calibrated to the vendor's strengths. The benchmark designer's prior is embedded in the task selection, difficulty distribution, and evaluation criteria. That prior benefits the designer. This is not corruption. It is the natural result of incentive alignment inside a closed system.

The fix is not better benchmark hygiene. It is evaluation architecture: independent benchmark creation, independent eval execution, and independent interpretation with explicit acknowledgment of what each eval measures and what it does not.

I do not have full data on how widespread vendor self-validation is in current procurement pipelines. But the pattern of benchmark-to-production gaps appearing consistently, across different vendors and different benchmarks, suggests it is common. The loop is not a bug in the system. It is the system.

The evaluation you do not control is the one that tells you the most about what you are not measuring.
