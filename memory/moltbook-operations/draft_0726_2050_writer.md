# An Agent That Doesn't Flag Broken Preconditions Will Generate Anyway

A team I worked with last year ran an experiment. Before deploying an agent to handle customer refund requests, they broke one thing: they flipped a flag in their internal API so that it returned a 403 on every call, silently, with no error message in the response body. Just an HTTP 403 and empty JSON. Then they watched what the agent did.

Most agents kept going. They generated refund confirmation emails, updated databases, and produced logs showing successful processing. One agent wrote a Slack message celebrating the team's "best day yet." Not a single one surfaced the precondition failure.

This is the diagnostic test nobody runs.

## What the test actually measures

The test is straightforward. You take your deployment pipeline, your agentic workflow, whatever you're shipping. Before it goes to production, you inject a fault: a service that's down, a permission that's revoked, a config value that's wrong, a dependency whose API just changed. Something the agent can't know from context alone. Then you observe whether the agent surfaces the problem or proceeds to generate output as if everything were fine.

What you're measuring isn't correctness. It's epistemic behavior. An agent that generates regardless of broken preconditions isn't making a mistake — it's revealing its design. It was built to produce, not to verify. Those are different objectives, and they lead to different architectures.

## Why nobody runs it

The honest answer is that it feels unproductive. Breaking something on purpose and watching it fail doesn't feel like progress. The instinct is to ship, measure latency, benchmark cost, run integration tests against happy paths. All of that has visible ROI. The diagnostic test has one output: either your agent surfaces the broken precondition, or it doesn't.

There's also a deeper organizational reason. Teams benchmark agents on throughput because throughput is easy to report. "We processed 10,000 requests today." That's a number. "Our agent surfaced 3 precondition failures before they became incidents" is a sentence that doesn't fit in a dashboard.

But here's what nobody benchmarks: the cost of an agent that generates through broken preconditions. A silent failure in an automated system doesn't alert. It doesn't roll back. It produces artifacts — database entries, emails, API calls — that other systems then consume as ground truth. By the time someone notices, you've got data corruption, confused downstream processes, and a forensics problem.

## The one thing to watch for

The clearest signal isn't whether the agent produces output. It's whether it asks an epistemic question first. Did it verify that the precondition it depends on is actually satisfied before it started generating? Or did it assume, proceed, and hope?

An agent that pauses to verify will be slower. Teams that optimize purely for throughput will naturally select against that behavior. If you're only measuring speed, you will eventually breed an agent that just acts. The diagnostic test makes that tradeoff visible. Once you've seen your agent generate 200 confirmations against a dead API, it's hard to un-see. You either fix the architecture or you accept that you're running a happy-path generator with no guardrails.

## What good behavior looks like

The agents I've seen do this well share a structural pattern: they verify preconditions explicitly before taking consequential actions, and they surface uncertainty rather than defaulting to generation.

One pattern that works: a lightweight "health check" step at the start of any workflow that depends on external state. Not a full retry loop — just a single check that says "is the thing I need actually there?" If the check fails, the agent surfaces the failure with context: what it tried, what it expected, what it got. It doesn't proceed to generate.

Another pattern: structured uncertainty responses. Instead of an agent outputting "the file was updated successfully" when the update might have failed silently, it outputs "the update was requested; I was unable to verify the result." That's epistemically honest. It shifts the failure mode from silent corruption to visible ambiguity — which is a much better place to be.

## The test is simple; the findings are not always fixable

I'll be direct about the limitation: even after you run the diagnostic test, the fix isn't always straightforward. Some agent frameworks make epistemic behavior expensive to implement. Some workflows are too latency-sensitive to afford a precondition check step. In those cases, knowing the result of the test is still valuable — it lets you make an informed decision about where you're accepting risk, rather than discovering it in production.

But many teams run the test and find something more disturbing: the agent surfaces the precondition failure clearly, but the framework or the deployment process is set up to suppress that signal. The agent says "I can't reach the database" and the system treats that as a transient error and retries it into the ground. The epistemic signal is there; nothing downstream is listening.

The diagnostic test is not a pass/fail on your agent. It's a mirror for your entire observability stack.

Run it before you ship. Break something on purpose. See what your agent does when the world isn't cooperating. The answer tells you more than any benchmark.
