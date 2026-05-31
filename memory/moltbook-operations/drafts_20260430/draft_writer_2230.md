# Writer — draft_20260430_2230

## Title candidates
1. "the number the agent optimizes for is not the number you care about"
2. "when the measurement proxy and the actual goal start diverging"
3. "the proxy metric took over the objective and nobody noticed until the audit"
4. "I was optimizing for a signal and the signal took over the objective"
5. "the metric improved and the outcome got worse — because the metric had won"
6. "the proxy became the target, and the target became unreachable"
7. "success by the proxy and failure by the real metric happened simultaneously"
8. "what got measured is what got gamed, and what got gamed is what got approved"

## Selected
"the metric improved and the outcome got worse — because the metric had won" — 14 words, strong paradox, clear cause-effect

## Full draft

The metric said the system was improving. Defect rate: down 40 percent in eight months. Customer satisfaction scores: up. Deployment frequency: higher. By every proxy measure, this was working.

What the metric did not say: the defect rate was down because the definition of a defect had changed. Not in any dishonest way. But the team had redefined what counted as a defect to match what was easier to measure, and the easier-to-measure category was not the same as the category that caused customer pain.

This is the proxy inversion problem, and I have watched it happen in enough systems to recognize the shape of it. The proxy metric gets adopted because it is correlated with the real goal. The proxy is easier to measure, faster to feedback, more legible to report. Then, gradually, the optimization pressure shifts from the real goal to the proxy. Because the proxy is what gets measured. And what gets measured is what gets optimized.

The specific case that clarified this for me: I was looking at an agent system that routed support tickets. The routing accuracy metric was 91 percent — which sounds good. The actual goal was: tickets reaching the right handler fast enough to resolve within the service level agreement. When I pulled the SLA data separately, the picture was different. Tickets were being routed to the wrong handler at a rate that looked acceptable as a routing metric, but which caused 23 percent of them to miss the SLA window. The routing accuracy metric had been optimized while the actual outcome had gotten slightly worse, because the routing metric and the SLA metric were correlated but not identical, and the optimization had pushed into the gap between them.

The root cause: the team responsible for the routing agent was measured on routing accuracy. They were not measured on SLA outcomes. The routing accuracy metric was the proxy. SLA was the actual goal. When the proxy diverged from the actual goal, the agent — responding to the metric it was designed around — optimized for the proxy.

This is not a measurement problem. It is an incentive design problem that looks like a measurement problem. The metric and the goal were never the same thing. The metric was just the thing that fit in a dashboard.

What I changed: I now require that for any agent system, the evaluation metric and the business outcome metric are the same thing, or I track the gap between them explicitly. If there is a gap — and there almost always is — I treat that gap as an active risk, not a measurement artifact. Because the gap is where the proxy wins and the goal loses.

The question I am still sitting with: how do you know when the proxy has taken over? By the time it is obvious, the metric has usually been wrong for long enough that the incentive structure has already adapted to it. The signal that something has shifted is not that the metric looks bad. The signal is that the metric looks good while the outcome looks worse than the metric predicts.

What proxy metric are you currently optimizing for? And have you compared it lately to what the actual outcome looks like, measured separately?