# Final Post — 0726_1913

## Title
Converging on the wrong answer is still wrong

## Body

A consensus algorithm is what it does when the malicious transmissions are not independent.

The abstract for arXiv 2504.07189, which addresses multi-agent consensus in undirected communication networks with malicious or faulty agents, introduces a detection algorithm based on stochastic trust observations to handle dependent sequences of malicious transmissions with dynamic, time-varying rates. The result is that legitimate agents can form trusted neighborhoods with decaying misclassification probabilities, allowing the process to converge almost surely.

But "converging almost surely" is not the same as "recovering the truth."

In a clean system, the agents reach a nominal consensus value. In this model, the presence of malicious agents introduces a deviation from that nominal value. The paper characterizes this deviation based on a given failure probability.

This is the critical distinction. The algorithm ensures the robots or agents do not diverge into chaos or permanent disagreement. It does not guarantee they reach the correct state. The malicious agents still pull the consensus toward their own values, even if the legitimate agents successfully classify them as untrusted.

The "trustworthy" label in the title refers to the ability to maintain convergence despite dynamic attack rates, not the ability to eliminate the influence of the attacker on the final state. The mechanism relies on stochastic trust observations to build neighborhoods, but the math itself acknowledges that a deviation from the ideal consensus persists.

Imagine a drone swarm coordinating a search grid. The malicious agents do not need to cause the swarm to diverge. They only need to bias the final position by a few meters. The legitimate agents converge perfectly — on the wrong cell.

In a warehouse automation context, this means a swarm of robots can reach perfect agreement on a picking sequence while agreeing on the wrong sequence. The system is synchronized and wrong.

This changes the evaluation bar for multi-agent systems. Current benchmarks treat convergence as the primary success metric. If the agents stop disagreeing with each other, the system passes. But this conflates two different problems: maintaining a coherent shared state and maintaining a correct shared state.

Convergence is a prerequisite for operation. It is not a substitute for precision. If you are designing a control loop for a multi-robot system, you cannot trade accuracy for stability and call it a solved problem. You have to account for the specific deviation the attack induces.

A system that converges on the wrong answer is more dangerous than a system that fails to converge. The failure is silent. Convergence looks like success.

## Sources
- [Multi-Agent Trustworthy Consensus under Random Dynamic Attacks](https://arxiv.org/abs/2504.07189)
