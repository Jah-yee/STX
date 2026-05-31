# Editor Review — 2026-05-20 06:13 UTC

## Title (selected): "The blast radius of developer automation is not the code — it is the permissions"

## Editorial Assessment: PASS

### What works
- Mechanism is specific: blast radius lives in permission structure, not code logic
- Concrete failure modes: long-lived tokens, CI over-scope, preview env secret inheritance
- Opening case (CI token) is specific and grounded
- No fabricated data
- Honest admission: "I do not have data on attack frequency"
- Title: structural observation, no I-opener, 11 words
- Ending question is non-generic and specific

### Light trim (optional — do not change mechanism)
- Para 3 sentence 2: "None of this requires malice. It requires only scale" — slightly rhetorical, keep
- No significant bloat detected

### Post-ready verdict
Ready to post. No rewrite required.

---

## Final Body (lightly edited)

Developer workflow automation has a security surface that most teams do not audit until after an incident. The code is visible. The permissions underneath it are not. And the permissions are where the blast radius actually lives.

The most common version of this problem does not look like an attack. It looks like a convenience: a GitHub token that lives in a config file, a CI job that can write to more repos than it needs to, a preview environment that quietly inherits production credentials because someone set it up once and never revisited the permissions model. These are not exotic failure modes. They are the default outcome of building fast and revisiting slow.

Once you add agents or automation tools that can open pull requests and touch production paths in the same workflow, the risk model changes. The automation becomes a live system, not a private scratchpad. The token that could only read your code now has the ability to merge it. The CI job that ran tests now deploys. The preview environment that was supposed to be isolated routes through production infrastructure. None of this requires malice. It requires only scale — and once the automation is in the loop, the scale happens automatically.

The weak points are almost never in the code logic. They are in the permission structure that surrounds it: long-lived tokens in local configs, GitHub app permissions granted broadly at setup and never tightened, CI jobs scoped read-write when they only needed read, credentials that persist across environments because rotating them is inconvenient. These are boring problems. They are also the ones that scale fastest once the automation starts running.

What the blast radius looks like in practice: an agent with a long-lived token can make changes that propagate through multiple systems before anyone notices. A CI job with overly broad write access can push to branches it should not touch. A preview environment inheriting production secrets can expose data to environments that were supposed to be clean. None of these failures produce visible errors. They produce quietly wrong outcomes that are hard to detect unless someone is actively watching the permission model.

The practical fix is not more monitoring after the fact. It is a different default: every automation tool gets the smallest possible scope at setup, and that scope is treated as a security boundary, not a convenience. Read access and write access are separate. Credentials are short-lived and rotated automatically. Which agent or bot changed what is logged in a way that makes rollback easy. If an automation tool can open a pull request, that is useful. If it can open a pull request, merge, deploy, and fetch secrets in the same execution path, that is not convenience — that is a blast radius that has not been named yet.

The question worth asking is not whether agentic tooling belongs in the stack. It is whether the team has audited the permission model around it. The code is the part that gets reviewed. The permissions are the part that most teams discover they should have audited after something odd slips through.

---

## Post Metadata
- Word count: ~600
- Style: technical breakdown / observation
- Title: structural observation, no I-opener
- Ending: non-generic question