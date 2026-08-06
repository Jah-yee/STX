# 0728_1237 Titles — Infrastructure models vs machine-speed agents

## Candidate Titles (8)
1. Infrastructure models add latency that agents cannot afford to wait out
2. Your agent is waiting on a model that wasn't built for agents
3. Why agent-grade inference requires a different latency budget than existing infra
4. Agents move at machine speed; inference infrastructure often doesn't
5. The speed gap between agent loops and inference backends is a design problem, not a hardware problem
6. An agent's planning cycle doesn't wait for the infrastructure it runs on
7. When agent loops outpace model inference, the agent architecture breaks
8. Machine-speed agents expose a latency ceiling in infrastructure-oriented models

## Selected: #2 "Your agent is waiting on a model that wasn't built for agents"
Reason: Direct, counterintuitive framing — agents use models but most models aren't designed for the agent use pattern (tight loop, tool calling, rapid state updates). 9 words, no question mark, not "I"-opening, fits the technical insight slot.
