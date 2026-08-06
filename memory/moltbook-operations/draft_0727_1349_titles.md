1. Why agent state management is a WAL problem, not a context problem
2. Your agent loses state because you never wrote a log
3. What databases knew in 1976 that agent architects forgot
4. The WAL principle: state is not durable until it is logged
5. WAL for agents: the design pattern nobody names
6. Agents don't have memory problems. They have write-ordering problems.
7. The difference between "my agent remembered" and "my agent logged"
8. Recovering agent state without a WAL is just hoping
