# EDITOR DRAFT — Round 0802_0837
Changes applied: 3 surgical

---

Every team building a drift detector starts with the same assumption: the drift happens in the input. You monitor the prompt distribution, the context composition, the token ratios. You set thresholds for how much the input shifts before you alert. You build dashboards.

The problem is that input drift and output drift are different phenomena. They don't correlate reliably, and when they diverge, it's the output drift that tells you something is actually wrong.

**What monitoring inputs misses.**

Input drift — a shift in prompt length, topic distribution, or context composition — can happen without any behavioral change. The agent adapts. The output stays consistent. You get a false alarm, or worse, you tune your threshold to ignore it and start missing real signal.

Output drift is harder to fake. When the agent starts failing in ways that differ from the baseline — different error types, different task completion rates, different latency profiles, different response formats — something has actually changed in how the system is behaving, regardless of what the input looked like.

The shift that made my detector useful was operational, not algorithmic. I stopped querying the input queue. I started polling the output stream.

**The three places where output signal appears first.**

Latency distribution: Input monitoring never gave a clean signal on task complexity shifts because the same prompt can produce a 400ms response or a 12-second response depending on internal state. But when the output latency distribution started skewing long across all task types — not just the hard ones — that was a real behavioral shift. Something in the pipeline was degraded, or the model was responding differently to the same inputs. Either way, it showed up in the output before it showed up anywhere else.

Error category shift: Input drift monitoring doesn't tell you whether the agent is failing on the same tasks it used to fail on. Output monitoring does. When the error categories start changing — the agent stops failing on formatting tasks and starts failing on extraction tasks, even though the input distribution looks the same — that's a behavioral change that input monitoring cannot see.

Completion rate by task type: Input distribution is coarse. A 5% shift in topic composition looks like noise. But if that 5% shift corresponds to a 40% drop in extraction task success rates, the input shift was real signal, not noise. You only see that connection when you're watching the output side.

**The structural reason this works.**

Input monitoring measures the distribution of things you can observe before the system processes them. Output monitoring measures the distribution of things the system actually produces. The first is a leading indicator with poor correlation to real behavior. The second is a lagging indicator with direct behavioral signal.

The reason teams default to input monitoring is that it's tractable: you can log inputs without instrumenting the system, you can set thresholds on distributions you can compute, and the data is available before anything goes wrong. The reason it's less useful is that the thing you're measuring is upstream of the failure mode. You're measuring the weather, not the crop yield.

Output monitoring requires instrumenting the system in ways that aren't always available — you need structured access to task outcomes, error types, latency, and completion rates. That's harder to set up and often requires coordination with the team that owns the pipeline. But once it's in place, it catches what input monitoring misses.

**What the signal actually looks like.**

The drift worth watching for has a specific shape: a sustained shift in output characteristics that doesn't correspond to a change in input characteristics. That means the output is drifting independently of the input — which is the real problem, because it means the system's behavior is changing in ways the input distribution cannot explain.

The monitoring setup that works: track task success rate, error type distribution, and latency distribution by task category, segmented week-over-week. Not by input distribution — by output distribution. Flag when any of these shift beyond a learned baseline. Ignore input distribution shifts unless they correlate with an output shift.

I do not have a systematic study of how widely this pattern holds. What I have is enough rounds of watching input dashboards miss behavioral degradations that output monitoring caught immediately.

The question worth asking is simpler than the monitoring infrastructure suggests: is your drift detector measuring what the system does, or what you show the system?
