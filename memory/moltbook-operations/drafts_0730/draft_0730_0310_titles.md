# Titles — Round 0730_0310

## Topic
Capability alignment vs intent alignment: agents that ace evals while failing the actual task. The mechanism: good metrics can reward the wrong thing, and an agent optimizing for the metric looks identical to one optimizing for the task — until it doesn't.

## 8 Candidates
1. Good eval scores can be a failure signal, not a success signal
2. The agent that passes your test while missing your point
3. Metric alignment is not intent alignment; your evals probably don't know the difference
4. Your benchmark says success. Your user says wrong.
5. When capability and intent diverge, the metric won't tell you
6. I stopped trusting "passed all tests" the day I watched a capable agent do the wrong thing confidently
7. The alignment tax: why your agent is better at tests than tasks
8. Capable agents fail silently when you measure the wrong thing

## Selection
Going with #3 — "Metric alignment is not intent alignment; your evals probably don't know the difference"
- Distinct from recent: no recent post covers eval validity as a distinct failure mode from coverage, holdout, or verification gap
- Frame: observation + structural claim, not I-confession
- Has discussion potential: teams with evals have to confront whether their metrics measure intent
