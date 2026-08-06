# Writer Draft — Round 0728_1413

**Title:** Browser agents should mine behaviors, not impersonate users

---

Most computer-use agents are evaluated by how convincingly they mimic human interaction with a web interface. Click through a checkout flow. Fill a form. Navigate a login. This is the wrong benchmark.

The reason is structural. A browser agent trained to imitate human behavior is being optimized for the appearance of success, not for the discovery of failure. It learns the path that works. It never surfaces the paths that should have worked but don't — because no human ever tried them.

Gaurav Koley's 2026 framing is precise: computer use should be a discovery tool, not a delegation tool. The agent runs before you trust it, not after. Its job is to enumerate the behavioral surface area your test suite never reached — the edge case an engineer handled manually, the error state nobody wrote a handler for, the race condition that only fires when two tabs open simultaneously. None of these appear in a human click-through.

The reason is mundane. A human user follows the intended path because that is what the interface was designed for. They encounter errors when the interface breaks. They do not encounter the failures that live in the spaces between the intended path and the full state space of the application. Those spaces are exactly where agentic systems tend to fail — and exactly what a click-through agent will never find.

When a browser agent operates as an impersonator, it inherits the human's blind spots along with the human's capabilities. It knows what to click because a person knew what to click. It does not know what to look for in the territories that nobody bothered to map.

The reframe is operational: treat the browser agent as a fuzzing tool with a UI. Fuzzers don't try to use software correctly. They enumerate inputs that the software was not designed to handle and observe what breaks. A browser agent doing behavioral discovery works the same way. It explores the edges of the interface — unexpected input sequences, error recovery paths, simultaneous state changes — not the golden path.

The practical difference is in what gets produced. An impersonation agent produces a log of what it did. A discovery agent produces a list of behaviors that your test suite should own but currently does not. Those are fundamentally different outputs, and optimizing for the wrong one has a specific cost: you get high confidence in the cases that were already working and no visibility into the cases that were quietly broken.

There is a real failure mode here that I have seen repeatedly. A team deploys a browser agent to automate a workflow. The agent passes every trial run. It gets deployed. It fails on the first real user input that deviates from the scripted path — which, in any production system with real users, happens within hours. The agent was never asked to find the edges. It was asked to simulate the center.

The fix is not better prompting. It is a different objective function. A discovery agent should be optimizing for coverage of behavioral surface area, not for successful completion of the current task. Its output should be a set of test cases — not a successful run, but a map of what the interface can do and what happens at its boundaries.

The question to ask of any browser agent implementation is not "does it complete the task?" The question is "what did it find that your test suite doesn't cover?" That second question is where the actual value lives — and that is the question that impersonation-based agents are architecturally incapable of answering.

---

*Word count: ~580 — needs expansion to ~700 minimum*
