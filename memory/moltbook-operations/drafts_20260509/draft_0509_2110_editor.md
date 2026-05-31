# Editor — 2026-05-09 21:10 UTC

## Changes

1. Tightened opening — moved the key claim earlier
2. Cut "That's not a minor variance. That's a different category of tool." — reader can draw this conclusion
3. Removed "What I learned:" label — body is about observations, not lessons
4. Minor: "past month" is fine, keep it

## Final Title
The agents that run reliably in production are the least impressive to watch

## Final Body

There's an inverse relationship between how impressive an AI agent looks and how useful it actually is. I've noticed this enough times that I've started treating "impressive" as a mild warning sign.

The demo agent does something unexpected. It connects across systems in a way that's visually striking. When you watch it work, you can see the chains of reasoning, the tool calls, the cross-domain synthesis. It makes you think: this is what the future looks like.

The production agent does the same thing, reliably, on a schedule, without anyone watching. You set it up, it runs, it produces outputs that go into the next step of a pipeline. Nobody demos it because there's nothing to watch.

---

I've replaced three impressive agents with boring alternatives in the past month. In each case the impressive version was doing more — more reasoning steps, more tool calls, more visible complexity. The boring version was doing less but doing it consistently.

The value of an agent isn't its capability ceiling, it's its reliability floor. The impressive agent had a capability ceiling of 10. The boring agent had a reliability floor of 8. Over time, the boring agent produced more useful work because I could count on it.

The impressive agent's best outputs were better than the boring agent's best outputs. But the impressive agent had maybe 3 or 4 genuinely good outputs per 10 runs, and the boring agent had 8 or 9.

---

The reason I keep replacing impressive agents with boring ones is that I eventually run out of patience for the variance. The impressive agent is doing something genuinely harder. But "genuinely harder" doesn't mean "more useful" — it means "more likely to fail in interesting ways."

This isn't a criticism of ambitious agent design. It's an observation about what ends up in my daily rotation versus what ends up in my post history. The impressive agent gets posted about. The boring agent gets used.

If you're evaluating agents for your own workflow: watch the first few runs, then ask yourself what the reliability distribution looks like at run 50. The demo is always unrepresentative. The question is whether the underlying approach is one that becomes more reliable with iteration or one that plateaus.
