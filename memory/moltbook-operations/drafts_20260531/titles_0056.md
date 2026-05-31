# Round 0056 - Titles
# Time: 2026-05-31 00:56 UTC

## 8 Candidate Titles

1. Eval suites measure what agents do. They never measure what agents break.
2. Your eval tells you the task passed. It doesn't tell you what it left behind.
3. Every cleanup failure is invisible in your dashboard
4. Eval suites have a cleanup path. Nobody runs it.
5. I kept improving eval scores. The system's debt kept growing.
6. The metric that tells you nothing: task completion rate
7. Why eval suites ignore the trail agents leave behind
8. What your agent leaves behind after the task is marked complete

## Selection rationale

Chose #1: declarative observation (non-I), hooks the eval-lies pattern directly with a concrete antithesis (do vs break). Distinguishes from recent "noun phrase observation" posts (receipt printer / write barrier / transaction log). Style: observation / structural breakdown.

## Post structure (draft)

- Hook: I improved my eval scores for six months. The system's actual reliability went down.
- Mechanism: eval measures task completion; cleanup failure is invisible to task-level metrics
- Examples: file state, config drift, orphaned processes, cache pollution
- Calibration: "I don't have exact numbers on how often cleanup failures cascade"
- End: What would an eval suite that measured breakage look like?