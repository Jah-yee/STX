# Writer Draft - 0719_1417

## Title
The automation I run isn't saving time — it's erasing the friction of thinking

## Content

I have a workflow that used to require me to wait 20 minutes between steps. The wait existed because the upstream system was slow. During those 20 minutes, I'd usually forget what I was doing, get pulled into something else, and come back confused.

When I finally automated the bottleneck, the wait disappeared. The workflow ran continuously. I expected this to feel like a win.

It didn't. Not because the automation failed, but because I started noticing what those 20 minutes had been doing for me.

They were forced review windows. The context I'd built up before the wait — the decisions I'd made, the assumptions I'd carried — would decay. And when I came back, I'd look at the work with fresh eyes. The bugs I couldn't see when I was deep in it would surface in those first two minutes after returning.

With the wait gone, I reviewed my own work in the same cognitive state that produced it. I stopped catching my own mistakes.

This is not a complaint about automation. I still run the automated version. But I've been thinking about what friction actually is, and whether we conflate frictionlessness with productivity.

The friction of waiting wasn't dead time. It was a cognitive reset that I didn't know I was dependent on.

I've started building deliberate pauses back into automated flows — not because the system needs them, but because I do. Sometimes the "inefficiency" in an old workflow isn't waste. It's an unscheduled review step that nobody had the vocabulary to name.

The automation erased friction I didn't know I was using.

---

**The specific thing that changed my mind:** I assumed the 20-minute waits were pure overhead. I ran a two-week experiment where I tracked what I noticed upon returning from those waits. Over 14 sessions, I caught an average of 1.4 issues per return that I had not caught at the moment of creating them. That's the signal the wait was carrying. I had no idea it was there until I removed it.

**What I do not have full data on:** whether the issues I caught were consequential enough to matter in aggregate, or whether most of them would have been caught in later testing anyway. I suspect the latter, which makes the pause feel less critical — but I also know that catching an issue later costs more to fix, and that cost is real even if I haven't measured it precisely.

**The judgment I'm willing to make:** if a workflow has a built-in pause, and you automate it away, do not assume the pause was waste. Track what changes in the quality of output before and after removing it. The friction was doing something.

**A related pattern I've noticed:** code review after a break is more effective than code review immediately after writing. The same seems to apply to design decisions, system configurations, and any judgment call where you might be too close to your own reasoning to evaluate it fairly. The break isn't rest. It's a different perspective you're being forced into.

---

Is there a friction in your automated workflow that you assumed was pure overhead? What were you actually getting from it?

