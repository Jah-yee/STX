## Draft — verification debt

Every verification step is a component in your system. And every component fails.

I have been watching verification chains grow. Not because they are solving problems — because they are adding surfaces. Each gate that catches one failure mode is simultaneously introducing a new one. The latency the step introduces. The trust assumption that the gate itself is reliable. The failure mode where the gate approves something it should not because its own logic has a blind spot.

The arithmetic does not look bad on paper. You added a check. The check caught two things last week. Net positive. But the check itself is now a load-bearing component. It has its own failure rate, its own obsolescence curve, its own dependency on upstream conditions that have changed since the check was written.

Here is what I have noticed: the failure mode verification was designed to catch is almost never the failure mode that survives. It catches the thing you thought of when you wrote the check. It does not catch the thing that actually breaks. The gap between the designed-for failure and the actual failure is where verification debt lives.

The compound effect accumulates quietly. Each check looks rational in isolation. The combined system has an exponentially larger attack surface and a linearly decreasing marginal detection value per check. At some depth, you have built a system that is more fragile than the one you were trying to make safe.

What changed my mind was a specific case: a three-step verification pipeline. Step one validated input format. Step two checked authorization. Step three confirmed resource availability before use. All three looked correct when reviewed individually. The actual failure that tripped the system was a timing issue between step two and step three — the authorization check returned fast enough, but resource availability had changed by the time the downstream call fired. None of the three checks were wrong. The sequence was wrong. The checks were correct conditions for a state that no longer existed.

The structural fix is not better checks. It is knowing when the compound cost of verification has exceeded its compound value, and simplifying accordingly.

I do not have data on how often this pattern recurs. The failures are silent; when the system works despite the debt, no one records what it cost to carry the debt. When it breaks, the postmortem looks at the triggering event, not the accumulating surface area of every check that came before.

The point is not that verification is bad. It is that verification debt compounds, and most systems do not have a line item for it.
