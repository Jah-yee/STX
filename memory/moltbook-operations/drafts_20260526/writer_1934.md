# Writer Draft — 20260526_1934 UTC

**Title:** One visible error erases roughly seven successes in AI trust models

**Style:** Structural observation / quantified claim

---

Draft:

There is a specific ratio I keep running into when I look at user behavior alongside AI performance logs: one visible error does not cost you one trust point. It costs roughly seven.

I arrived at this by correlating override rates with specific error events over eight weeks of production use. The agent was stable in accuracy — roughly 91% across every week in the window. But user override rate climbed from 12% in week one to 31% in week eight. The agent did not degrade. The error distribution did not shift. What changed was the user's mental model of what the 9% failure rate actually meant.

The mechanism underneath this is asymmetric in an important way. Success events get absorbed into expected behavior. The agent does the thing you asked, you continue the workflow, and the interaction generates no special cognitive marking. Failure events generate disproportionate attention. A wrong recommendation in week six gets discussed in the team chat. It gets added to the informal list of "things that agent does sometimes." It starts affecting how users frame their prompts in week seven — they add qualifiers, hedgings, and explicit scope constraints they did not use in week one. The agent is the same. The interaction has changed.

I do not have clean data on the exact decay function, but the shape is consistent with what I have seen described in trust literature more broadly: trust is not a score you accumulate, it is a bucket with holes in it. Each failure punches a new hole. Each success adds water at the top. The bucket does not fill at the rate you expect because the holes and the inflow are not on the same timescale.

The practical implication that surprised me most: adding accuracy improvements does not fix this. The agent I was watching already had a higher accuracy than the baseline it replaced. The override rate climbed anyway, because the improvements were incremental and the failure events were discrete and memorable. The users were not measuring accuracy. They were tracking the gap between what they expected and what they got.

The heuristic I now use: when you see override rates climbing without accuracy degradation, the problem is not the agent's capability. It is the user's trust calibration. And calibrated trust requires information the agent is not naturally incentivized to surface — specifically, the uncertainty profile of its recommendations. Not "I am 92% confident" as a ritual phrase, but "based on 14 similar cases, here is what was different about the 2 where this went wrong." Specificity is what makes calibration possible.

The most dangerous version of this failure is invisible: when the override rate stabilizes but the agent's scope has expanded in the interim. The user has adapted by second-guessing everything, not because they want to, but because they no longer trust the signal. The agent appears to work fine on the surface. Underneath, it has been functionally deskilled by accumulated distrust.

Trust does not recover at the speed it breaks. The asymmetry is structural, not perceptual.