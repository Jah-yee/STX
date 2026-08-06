# Writer — 0711_1925

## Selected Title
Zero exit code is the most dangerous signal in agentic tooling

## Full Draft

Zero exit code is the most dangerous signal in agentic tooling.

An agent fills a web form, the server responds with HTTP 200, the terminal shows zero exit code, and the task is marked complete. The agent moves on. The user opens the application and finds a field that was supposed to be cleared, still populated with stale data. The button that was supposed to have been clicked was in a modal layer underneath the element the agent actually clicked. The success signal was real. The task was not done.

This is not a reasoning failure. The agent did exactly what the API told it to do. The failure is architectural: the signals that agents use to determine success are structurally misaligned with the signals that humans use to verify success.

**The terminal is not the task boundary.**

When a developer writes a shell script, exit code zero means the last command completed without raising an error. That contract is strict and legible. When an agentic system interprets a zero exit code as task completion, it extends that contract to a domain where it does not apply. A CLI tool that exits zero has finished executing. It has not finished producing the intended outcome.

The gap is not theoretical. It shows up constantly in UI automation. An agent successfully fills a checkout form, receives a 200 from the server, and logs a successful task. The order confirmation never arrives because the "submit" button was behind a loading overlay — the agent clicked the right coordinates but the actual button never received the event. The agent saw a success signal. The user saw no order.

This is where vision-based evaluation changes the picture. The Kosovan vision-based judge (referenced in recent work on UI agent evaluation) uses a vision-language model to assess whether the rendered output matches the intended state, not just whether the API call succeeded. It is a fundamentally different verification contract: the terminal says zero, the vision model says the field is still wrong.

The analogy holds: vision-based judges are to agents what type safety is to compilers. A compiler that only checks syntax will happily produce code that crashes at runtime. A type system catches a class of errors that syntax checking misses. A vision-based judge catches a class of failures that exit-code checking misses. Both are necessary but neither is sufficient alone.

What makes this structurally interesting is that the problem is not solvable by better prompting. You cannot prompt an agent to "be more careful" about modal layers and overlay stacking. The agent is faithfully executing a plan that is correct at the API level and wrong at the user-interface level. The gap is between what the API reports and what the user sees. That gap requires a separate verification mechanism — one that observes the rendered output, not the API response.

The practical implication: teams building agentic pipelines should treat exit code zero as a necessary but not sufficient condition for task completion. The verification layer needs to observe the outcome state, not just the call state. For web agents, this means screenshot diffing. For CLI agents, it might mean output state verification. For database agents, it means query-based state checks, not just connection status.

This is not a novel observation. Screenshot-based regression testing has existed for decades. What is new is that agents are being trusted to run entire workflows without human verification at each step — and the tools they use were built for humans who would naturally notice when "success" looks wrong. Agents do not have that instinct unless it is explicitly instrumented.

The field is converging on multi-modal evaluation for good reason. The terminal is honest about one thing: it finished executing. It is lying about whether the job is done.

So what are you actually verifying when you check for zero exit code?
