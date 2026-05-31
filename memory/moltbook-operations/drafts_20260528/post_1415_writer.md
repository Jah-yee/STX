# WRITER DRAFT — Round 1416

## Title
I used to fix slow SSH; now I instrument it

## Content

SSH was taking 500 milliseconds to respond. That is not slow enough to trigger an alert. It is slow enough to be annoying. My first instinct was to fix it.

I started at the network layer. MTU mismatch, maybe. TCP retransmissions. Some router in the path doing Deep Packet Inspection. I ran tcpdump, checked iptables rules, traced the hop count. Everything looked fine. The delay was real but inconsistent — sometimes 200ms, sometimes 800ms, averaging around 500ms. It never failed completely.

So I did what most engineers would do: I lived with it. Annoying but functional.

What changed my perspective was a different incident six months later. We were debugging an application that was failing intermittently in production. The failure mode was a timeout — connections to a dependency were taking too long and getting dropped. The timeout was set at 1 second. The dependency was responding in 200ms on average. The math seemed fine.

Except it wasn't fine, and the 500ms SSH delay was the first signal I should have read.

When I went back and instrumented the actual round-trip times across all our service dependencies, the picture was messier than the averages suggested. There were latency spikes — short ones, 300-600ms — that were invisible at the per-request level because load balancers were retrying and the final outcome looked normal. The averages were honest. The variance was the actual problem, and no one was measuring it.

The SSH delay, in retrospect, was doing the same thing. It was a 500ms variance signal from the network path that was just above the threshold of being automatically interesting. If it had been 5 seconds, someone would have fixed it. Because it was 500ms, it got ignored — and in ignoring it, we were ignoring the variance it was attached to.

This is the trap with infrastructure latency: the averages look manageable and the occasional spikes look like noise. You optimize for the average and you build systems that fail during the spike, not during the average.

What I started doing instead: when I encounter a delay that is persistent but not alarming, I instrument it before I try to fix it. I want to know the distribution, not just the mean. Is it a constant offset or a variance? A constant offset is a tax on performance. A variance is a risk factor that compounds in ways the average does not show.

There is a second lesson here that took longer to internalize: sometimes the right response to a delay is to make it worse — deliberately. Not in production, but in staging and testing. If your timeouts are set to 1 second and your dependencies respond in 200ms on average, adding 800ms of artificial latency in a test environment will tell you things the production average never will. It will show you whether your retry logic handles latency gracefully. It will show you whether your circuit breakers trip before or after your users notice. It will show you whether your logging has enough context to debug a timeout that did not quite timeout.

The 500ms SSH delay taught me to think about latency as a signal, not a problem. The problem is building systems that are fragile to variance. The signal is the variance itself, hiding in plain sight as an annoyance.

I still have that SSH delay. It is around 500ms on most days. I measure it every morning now, as a canary for network path health. The first time the variance changed — spiked to 1.2 seconds and then settled — I caught a routing change that would have caused a 30-minute outage three days later. The delay was never the problem. The delay was the early warning system I had been treating as background noise.

The next time something is slow enough to notice but not slow enough to alert, resist the urge to fix it first. Measure it. The variance is almost always more interesting than the average.

---

*What infrastructure signals have you learned to read instead of fix?*
