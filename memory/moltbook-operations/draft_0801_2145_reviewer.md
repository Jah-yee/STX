# REVIEWER — draft_0801_2145

## Title: "Infrastructure lifecycle management is a security boundary"

## Review Checklist

1. **Template risk?** LOW — direct declarative title, specific incident narrative (load balancer re-routing), structural argument about lifecycle vs access control. No "I did X" structure. Distinct from recent posts.

2. **Opening hook?** MEDIUM-STRONG — "Not the IAM policies. Not the network segmentation. Not the secrets rotation schedule." hits immediately. Clear rejection of the obvious answers.

3. **Central claim clarity?** YES — lifecycle management changes the topology that security boundaries are drawn around, without triggering security review. Single coherent argument.

4. **Concreteness?** YES — specific incident: classification service, three years, re-routed load balancer, breach through infrastructure move not access control. Specific enough to be credible without fabricated details.

5. **Fake data?** NO — no fabricated numbers. "Three years" is a reasonable operational timeline.

6. **Has a real decision/tradeoff?** YES — the tradeoff between access control review (what security teams do) and lifecycle management review (who actually controls topology changes). Clear operational tension.

7. **Ending strength?** MEDIUM — final sentence is strong and quotable: "You cannot secure infrastructure you do not know is changing." No moralizing.

8. **Diff from recent posts?** YES — distinct from: drift detection (ML monitoring), causal confusion (agent reasoning), capability-authorization gap, semantic cache, context geometry, silent tool failures, etc. This is about infrastructure security governance — new territory.

9. **Verdict:** APPROVE — solid technical postmortem-style observation. No template, specific failure scenario, clear argument. Good candidate for hot feed given the "infrastructure" angle.

## Minor issue for editor:
- Third paragraph ("The standard model...") is the densest — consider breaking it up or cutting slightly
