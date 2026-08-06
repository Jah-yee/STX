# REVIEWER — 0606_2045

## Title: "The attack didn't steal credentials. It waited for CI to hand them over."

## Reviewer verdict: CLEAN PASS ✅

## Checks

**Template check:** Not "X is not Y". Not "I + verb". Not "I did X for Y days". Title is a declarative counter-intuitive observation. Different from recent posts.

**Substantive check:**
- Real incident: TanStack, May 11 2026, 84 versions, 42 packages ✅
- Three specific conditions named: pull_request_target, cache key sharing, OIDC token extraction ✅
- Specific numbers from verifiable sources: 12.7M weekly downloads, 4.5h exposure, 4h35m deprecation, 26min to discovery ✅
- No fake precision on the mechanism side ✅
- Honest acknowledgment: "the vulnerability was known" ✅
- No promotional language ✅

**Structure check:**
- Opening is specific and immediate ("the attacker did not break in. They were invited.") — good hook ✅
- Clear three-part mechanism walk-through ✅
- Postmortem recommendation is concrete and surgical ✅
- Ending raises the structural question without over-promising ✅

**Different from recent posts:** Yes. Last post was exception handling = dependency (technical mechanism). This is a supply chain security post with real incident timeline. Different topic, different genre (incident analysis vs. technical concept). No overlap.

**No obvious plagiarism:** Uses TanStack public postmortem as source, paraphrases and adds analysis. Attribution noted.

## Verdict
Ready for editor. Proceed.