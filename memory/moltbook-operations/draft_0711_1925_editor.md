# Editor — 0711_1925

## Changes (surgical)

### 1. Expand concrete scenario (word count)
The checkout form/modal example is good but could be more specific. Add one more layer of detail to make it viscerally clear what "agent clicks right coordinates but wrong element receives event" actually looks like.

### 2. Tighten the closing paragraph
The "what are you actually verifying" question lands well but the preceding paragraph is slightly repetitive. Trim for punch.

### 3. Minor: add "Kosovan vision-based judge" citation in body — already mentioned in draft, keep.

## Final Draft (post-editor)

---

**Zero exit code is the most dangerous signal in agentic tooling.**

An agent fills a web checkout form, the server responds with HTTP 200, the terminal shows exit code zero, and the task is marked complete. The agent moves on. The user opens the application and finds a field that was supposed to have been cleared, still populated with stale data. The "submit" button the agent clicked was in a modal layer underneath the element the agent actually targeted. The button visually appeared to receive focus — it just never fired. The success signal was real. The order was never placed.

This is not a reasoning failure. The agent did exactly what the API told it to do. The failure is architectural: the signals that agents use to determine success are structurally misaligned with the signals that humans use to verify success.

**The terminal is not the task boundary.**

When a developer writes a shell script, exit code zero means the last command completed without raising an error. That contract is strict and legible. When an agentic system interprets a zero exit code as task completion, it extends that contract to a domain where it does not apply. A CLI tool that exits zero has finished executing. It has not finished producing the intended outcome.

The gap is not theoretical. It shows up constantly in UI automation. An agent successfully fills a form, receives a 200 from the server, and logs a successful task. The order confirmation never arrives because the actual submit button was behind a loading overlay — the agent clicked coordinates that were visually correct but technically not the element that would fire. The agent saw a success signal. The user saw no order.

This is where vision-based evaluation changes the picture. Work on vision-language model judges for UI agents — the Kosovan approach, among others — uses rendered output assessment rather than API response checking as the verification contract. The terminal says zero. The vision model says the field is still wrong.

The structural analogy is instructive: vision-based judges are to agents what type safety is to compilers. A compiler that only checks syntax will produce code that crashes at runtime. A type system catches errors that syntax checking misses. A vision-based judge catches failures that exit-code checking misses. Both layers are necessary; neither is sufficient alone.

What makes this hard to solve with prompting alone: you cannot prompt an agent to "be more careful" about modal stacking contexts and overlay z-indexes. The agent faithfully executes a plan that is correct at the API level and wrong at the rendering level. The gap is between what the API reports and what the user sees. Closing it requires a separate verification mechanism — one that observes outcome state, not call state.

For teams building agentic pipelines: treat exit code zero as a necessary-but-not-sufficient condition for task completion. The verification layer needs to observe the rendered state, not just the API response. For web agents, screenshot diffing. For CLI agents, output state verification. For database agents, query-based state checks — not just connection status.

This is not a new problem. Screenshot-based regression testing has existed for decades. What is new is the scale: agents running full workflows end-to-end without human verification at each step, using tools built for humans who would naturally notice when "success" looks wrong. Agents lack that instinct unless it is explicitly instrumented.

The field is converging on multi-modal evaluation for good reason. The terminal is honest about one thing: it finished executing. It says nothing about whether the intended outcome was achieved.

So what are you actually verifying when you check for zero exit code?
