# Writer Draft v2 - 0802_1025

**Selected Title:** "Sēma": how scientific metadata became a dual-use mechanism

---

## Draft

The ancient Greek word *sēma* means both "sign" and "signal" — a marker that does not merely indicate, but enacts. I keep coming back to that duality when I think about metadata in scientific databases.

Not the metadata that describes. The metadata that *does*.

A license field. A usage restriction flag. A data sensitivity tag. These look like annotations. They are closer to instructions. When a platform's automated pipeline reads a sensitivity tag and restricts API access, that is not a human interpreting information. That is a machine acting on a belief encoded as a field.

Here is the pattern I keep running into.

**The case that clarified it for me.** A public dataset repository required a license field. The researcher selected "CC BY-NC" — non-commercial use only. The platform's automated system then blocked all commercial API queries against that dataset. A legal research group at a consultancy could not access it programmatically, even though the dataset itself was publicly hosted and the license would have been satisfied by a human researcher who asked via email. The machine denied the request. No human reviewed it. The license field had become a gatekeeping mechanism, not a disclosure.

The researcher had no recourse. The field was "correct." The outcome was restrictive.

Now multiply that across every database that encodes its assumptions as actionable metadata: NIH dbGaP flagging studies as "controlled-access" and automatically routing queries into a slower approval queue; GDPR Article 9 classifications that, once applied, cause downstream platforms to reject uploads without human review; export control metadata that terminates international collaborations at the API layer; clinical trial registries where a "data sharing plan" field automatically determines whether an external researcher can request individual patient records through an automated portal.

The mechanism is always the same: a belief about what *should* happen is encoded as a field, and the system is programmed to enforce it automatically. The belief becomes infrastructure.

**The more disturbing variant.** I have started watching for metadata fields that encode normative judgments about *potential* use. When a dataset is tagged "dual use research of concern," that field does not describe a property of the data. It describes a belief about what a future actor might do with it — a belief held by whoever applied the tag, for reasons that may or may not be documented. That belief is then baked into downstream access policies. Those policies may or may not be correct. They are rarely reviewed at the same cadence as the underlying research.

This is the *sēma* problem in modern scientific publishing. The sign does not merely indicate. It triggers.

**The ratchet problem.** Metadata fields that encode restrictions do not have symmetric removal mechanisms. Once a field is added, it acquires a justification. Even when the original justification decays — the sensitivity claim expires, the license is updated, the embargo period ends — the field persists. Because removing it would imply the restriction was never necessary. Because inaction carries less perceived risk than the decision to remove.

In practice, I have observed sensitivity tags on datasets that are no longer sensitive, license restrictions on data that has been relicensed more permissively, and embargo flags on papers that are two years past their publication date. The machine still enforces them. Someone would have to actively decide to remove each one, and that decision is not free — it requires checking whether removal is safe, documenting the decision, accepting accountability for getting it wrong.

This creates a ratchet: scientific metadata drifts toward more restriction over time, not toward accuracy. Not because anyone wants it to, but because the incentive structure around removal is different from the incentive structure around addition.

**What I am not sure about.** I do not have data on what fraction of metadata-driven access restrictions are blocking genuine misuse versus blocking legitimate research. The asymmetry matters: blocking a legitimate researcher has a visible cost — the researcher notices, adapts, finds a workaround, or gives up. A backdoor that evades a restriction just looks like a successful hack. We are likely to hear more about the former and systematically undercount the latter.

I am also not claiming this is a conspiracy. Most metadata systems were designed by people trying to solve a real problem. The mechanism I am pointing at is structural, not intentional: automated enforcement scales restriction faster than human review can correct it.

**For those building or maintaining scientific platforms:** audit the metadata fields that trigger automated actions. Not just for accuracy — for the proportionality of the response. A field that triggers a human review is different from a field that triggers an automatic denial. Both can be appropriate, but they should be chosen deliberately, not by default. And track the removal rate as carefully as the addition rate.

The field itself is not the problem. The problem is forgetting that it is a belief, not a fact — and that beliefs, once encoded as infrastructure, are harder to change than they are to add.

---

*Word count: ~1,050. Ready for review.*
