# Writer Draft v2 — draft_0730_2040

## Title
Causal discovery benchmarks hide a silent validation crisis

## Body

Run three popular causal discovery algorithms on the same observational dataset. You will get three different graphs. None of them will be obviously wrong. All of them will cite decades of theoretical grounding.

This is not a bug in the algorithms. It is a structural problem with how the field evaluates them.

The standard benchmark practice goes like this: generate synthetic data from a known causal graph, feed it to the algorithm, measure how close the recovered graph is to the ground truth. The closer, the better. Publish the recovery score. Move on.

There are at least three things wrong with this that the recovery score does not capture.

**The structural assumption problem.** Most causal discovery algorithms encode strong assumptions about the data-generating process: linearity, Gaussian noise, no hidden confounders, acyclicity, causal sufficiency. When your benchmark data matches those assumptions, the algorithm performs well. When it does not, it performs poorly — but you often do not know which assumption was violated. PC, FCI, GES, NOTEARS, CAM-UP — they all have different Achilles heels. A concrete example: the PC algorithm assumes conditional independence tests are correctly calibrated, which breaks down quickly with small samples or high-dimensional data. GES assumes greedy optimization over a discrete search space, which scales poorly but handles certain nonlinearities that NOTEARS does not. The benchmark paper that compares them usually selects datasets where each looks good in at least one configuration. That is not a comparison. That is a curated demo.

**The ground-truth transfer problem.** In simulation, ground truth is known because you designed the graph. In the real world, you do not know the ground truth. You are using causal discovery precisely because you cannot experimentally intervene at scale. So the benchmark is measuring something that is only available in the one setting where you do not need the algorithm. The metric that matters most — "does this graph help me make better decisions than I would have without it?" — is never directly measured. A team I worked with spent six months building a causal model of patient flow in a hospital. The benchmark scores were good. When we stress-tested the graph against two years of held-out data, the predictions on intervention effects were no better than a simple correlation matrix. The benchmark had certified something we had not actually needed it to certify.

**The scale-robustness gap.** Recovery accuracy is typically reported at sample sizes where the signal is clear: thousands of observations, clean variables, no missing data. Practitioners applying these methods often have hundreds of observations, missingness, and variables that do not cleanly map to the benchmark's assumed distributions. Several papers have noted that algorithm rankings can flip between n=500 and n=5000. The published rankings do not usually specify at which sample size each algorithm becomes trustworthy — that information would require a systematic sensitivity analysis that most benchmark papers do not include.

I do not have a clean solution here. What I have is a practice of treating causal discovery output as a hypothesis generator rather than a conclusion engine. I run multiple algorithms and look for the edges that are invariant across methods — those are the more robust claims. For edges where algorithms disagree, I treat that disagreement as information about the structural assumptions I am making, not noise to be resolved by picking one algorithm. If the PC algorithm and GES agree that X → Y after controlling for Z, that edge survives more assumption violations than one that only one method finds.

The yardstick problem in causal discovery is real. Better benchmarks would involve semi-synthetic data where ground truth is partially known, multiple evaluation criteria beyond recovery accuracy, and explicit reporting of sensitivity to each structural assumption. The field is moving in that direction with some recent datasets. But the gap between what benchmarks certify and what practitioners need remains wide — and most papers do not close it.

The silent crisis is this: algorithms that score well on benchmarks routinely fail to agree on real data, and the disagreement is rarely reported because it happens outside the benchmark. That does not mean the algorithms are useless. It means the certification that benchmarks provide is narrower than it appears.
