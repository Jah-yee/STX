# EDITOR — Round 0710-1331

**Title:** Corner cases that cannot physically occur train agents on nothing.

---

## Editor Review

**Overall:** Solid draft. Two targeted changes recommended.

### Change 1: The paragraph on "the mechanism that produces this failure"

Current text:
> The mechanism that produces this failure is not malicious. It is a mismatch between the generative pipeline and the physical validation layer. A diffusion model rendering a scene does not know the vehicle's kinematic state. It is optimizing for visual plausibility, not for physical consistency with the agent's action envelope.

This is the strongest paragraph structurally. Keep it.

### Change 2: Word count assessment

Current word count: ~780 words. Target: 700-1400. Within range.

### Change 3: Consider tightening the fourth paragraph (concrete example)

The example paragraph currently reads:
> Here is what this looks like concretely. A vehicle traveling at 60 km/h on a dry surface with standard tire friction needs approximately 40 meters to brake to a full stop. A pedestrian stepping into the lane 15 meters ahead is not a corner case. It is a physically impossible scenario for that vehicle state. Any training signal from that scenario is a response to a condition that can never occur, and any safety claim derived from successful navigation of that scenario is hollow.

This works. The phrase "it is a physically impossible scenario for that vehicle state" in the middle of a sentence is slightly dense. Consider splitting:

> Here is what this looks like concretely. A vehicle traveling at 60 km/h on a dry surface with standard tire friction needs approximately 40 meters to brake to a full stop. A pedestrian stepping into the lane 15 meters ahead is not a corner case. It is a physically impossible scenario — one the vehicle cannot brake in time regardless of the agent's response. Any training signal from that scenario is a response to a condition that can never occur, and any safety claim derived from successful navigation of that scenario is hollow.

### Change 4: The closing paragraph

"The industry has a word for a test condition that exercises a safety system but can never be triggered in real operation. That word is 'not a test.' We just stopped using it because it sounds bad in the safety report."

This is good. Keep as-is.

---

## Editor Recommendation

Apply the single targeted edit to paragraph 4 (split the dense sentence). Otherwise the draft is clean, well-structured, and the title is the strongest of the batch. Proceed to posting.
