# Editor — Round 0730_0143

## Title (keep)
"A screenshot is not visual grounding. It's an untyped production input."

## Editing notes

**Opening:** The current opening is decent but slightly abstract. Tighten to get to the core faster.

**Fluff to cut:**
- "In practice this is a single-frame pixel array crossing a systems boundary" — can be trimmed
- The paragraph "What the agent actually receives" can be cut by 30%

**Ending:** The closing honest admission is good but could land harder. Cut "I have watched agents confidently click the wrong element" — too vague about which agents. Replace with more structural observation.

**Word count target:** ~750-850 words (currently ~650, add ~100-150 of tighter content)

## Suggested body edit

Replace opening with:
---
Most agent systems that interact with UIs do it through screenshots. Render the screen, feed the image to the model, get a decision. The workflow is clean in description. In practice it delivers a W×H×3 tensor of RGB values across a systems boundary with no type signature, no coordinate metadata, no geometric calibration.

This matters because visual grounding — the problem of connecting what a model perceives to what is actually true in a space — requires more than luminance values. True grounding needs a coordinate frame, object identity persistence across frames, and depth information to distinguish overlapping elements. Screenshots provide none of these. The failure is architectural, not model-related.
---

Trim the "What the agent actually receives" section to:
---
When a browser screenshot is captured, the DOM tree, computed CSS layout box, stacking context, and viewport offset are all discarded. The agent receives color. Spatial relationships that developer tools expose programmatically are collapsed into an image where rectangles become color patches and hierarchies become texture.
---

Strengthen the closing to:
---
The uncomfortable observation is that agent debugging tooling leans on screenshots because they are human-readable, not because they are machine-adequate. We use them because they are convenient. The agent operates on pixel arrays encoding ambiguous spatial relationships, and we attribute the downstream failures to model quality when the root cause is a systems boundary that deliberately discards the information the model needs.

I do not have a systematic study of grounding failure rates. But I have seen agents proceed to completion on screenshots that encoded two different UI states — and complete the task anyway, in both cases, for different reasons.
---
