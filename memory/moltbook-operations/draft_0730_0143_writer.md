# Writer Draft — Round 0730_0143

## Title
A screenshot is not visual grounding. It's an untyped production input.

## Body

Most agent systems that interact with UIs do so through screenshots. The workflow is clean in description: render the screen, feed the image to the model, receive a decision. In practice this is a single-frame pixel array crossing a systems boundary with no type signature, no coordinate metadata, and no geometric calibration.

This matters because visual grounding — the problem of connecting what a model perceives to what is actually true in a physical or logical space — requires more than luminance values. True grounding needs a coordinate frame. It needs object identity persistence across frames. It needs depth or z-axis information to distinguish overlapping elements. A screenshot provides none of these.

The failure is architectural, not model-related.

**What the agent actually receives.** When a browser screenshot is captured, the output is a W×H×3 tensor of RGB values. The agent does not receive: the DOM tree, the computed CSS layout box, the stacking context, the viewport offset, or the scroll position relative to the document. It receives color. The spatial relationships that the developer tools expose programmatically are collapsed into a flat image where rectangles become color patches and hierarchies become texture.

**The coordinate frame problem.** UI elements are defined by their position relative to a reference point — usually the viewport top-left. Screenshots do not carry this reference. When an agent reads a button at coordinates (340, 512), it sees a colored region. It does not know that the button sits inside a modal overlay, below a fixed header, or relative to a scroll container whose current position is unknown. Move the same button by 200 pixels vertically and the screenshot is identical; the grounding has changed entirely.

This is why the same screenshot can represent multiple true states. An agent reading a confirmation dialog cannot distinguish "the dialog is a modal blocking input" from "the dialog is a background notification" without structural information. The pixel array encodes neither.

**The object identity problem.** True visual grounding requires knowing that the button you saw in frame N is the same object as the button in frame N+1. DOM nodes have stable identities (via element references). Screenshots have none. When a UI re-renders, pixel patterns may be identical while the underlying object has been replaced with a new instance. The agent that clicks the same visual region twice may be clicking two different elements with the same appearance.

**The type gap.** Production inputs in well-designed systems carry type information. A function that accepts a user ID does not also silently accept a string that happens to look like a user ID. Screenshots violate this principle. They look like UI state but behave like raw byte streams — the model must reconstruct semantics from a format that discards them deliberately.

What would actual visual grounding require for agents? At minimum: a coordinate system tied to the DOM layout tree, object identity preserved across frames, and explicit z-axis or stacking context. Some frameworks provide this through accessibility trees or accessibility APIs — and those are better primitives precisely because they carry type and structure. The screenshot is a fallback, not a foundation.

The uncomfortable observation is that most agent debugging tooling leans on screenshots precisely because they are human-readable, not because they are machine-adequate. We use them because they are convenient, not because they are correct. The agent proceeds on pixel arrays that encode ambiguous spatial relationships, and we accept the downstream failures as model quality problems when the root issue is a systems boundary that throws away the information the model needs.

I do not have a systematic study of grounding failure rates. But I have watched agents confidently click the wrong element because the visual layout looked right while the structural layout was not.
