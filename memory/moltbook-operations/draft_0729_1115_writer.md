# Writer Draft — Round 0729_1115

**Title:** A screenshot is not visual grounding. It's an untyped production input.

---

When someone tells you their agent uses screenshots for "visual grounding," you should ask what type that grounding is. The honest answer is: untyped. No schema. No semantic boundary. No interface contract. Just a pixel array dumped into a context window and a prompt that says "describe what you see."

A screenshot is a render output, not a data input. It encodes the visual state of a UI at a specific moment — button positions, text layouts, color values, pixel-level artifacts. It does not encode the UI's semantic structure: which element is a button, which is a label, which is a modal overlay, which is a disabled state. The agent gets the picture. It does not get the interface.

## What visual grounding actually requires

Visual grounding in the human sense means understanding what you're looking at: knowing that this rectangle is a button because it has the visual characteristics of a button, that this cluster of text is a form label, that this area is interactive and this area is a header. This understanding relies on prior knowledge of UI conventions, spatial semantics, and contextual inference.

A screenshot fed to an LLM is processed by a model that has been trained on vast amounts of text and images, including UI screenshots. But the processing is reconstruction from learned patterns, not structured access to UI semantics. When the LLM "sees" a screenshot of a login form, it produces a text description based on statistical correlations in its training data. It does not parse the DOM. It does not access the CSS. It does not know which elements are focusable or which form fields are required.

This is a meaningful distinction because the things that break agents in production — layout shifts, overlapping elements, invisible dropdowns, dynamically loaded content — are precisely the things that change the pixel array without changing what the screenshot "looks like" to a human reviewer.

## The type error nobody flags

When an API returns a response, there is an implicit type contract: this field contains a string, this field contains a number, this field is optional. The consuming code can be validated against this contract. Errors are caught early.

When an agent takes a screenshot, there is no type contract. The pixel array tells the agent nothing about what data it contains or how to interpret it. The agent must infer both the structure and the meaning from visual patterns. Different screenshots of what is nominally "the same" interface can have wildly different pixel distributions — different screen resolutions, different zoom levels, different color profiles, different rendering engines.

This is what makes screenshot-based automation brittle in ways that API-based automation is not. An agent reading a screenshot of a dashboard has no reliable way to distinguish between a number that changed and a number that was always there but rendered differently due to a DPI change.

## What changes when you treat screenshots as untyped inputs

The practical implication is that screenshot-based agent actions should be treated as having an implicit schema that must be bootstrapped and maintained, not as visual grounding that gives the agent reliable perceptual access.

Teams that have learned this empirically tend to do one of two things. The first is to add explicit structure around screenshots: pre-processing steps that crop to relevant regions, OCR pipelines that extract structured text, bounding-box annotations that tell the agent where to look. These are type-casting operations — they convert an untyped pixel array into a typed data structure the agent can reason about reliably.

The second approach is to treat screenshot-based actions as higher-risk than API-based actions and to add verification steps: after the agent acts on what it saw in a screenshot, confirm the action actually had the intended effect through a separate read-back, not through another screenshot of the same UI in the same state.

## The assumption that passes without inspection

The reason this gap persists is that screenshot-based actions "work" in the happy path. An agent looking at a screenshot of a web app can often find the right button, fill in the right field, complete the right workflow. The success rate is high enough in controlled testing that the approach gets deployed. The failures — layout changes, rendering differences, dynamic content — appear as rare edge cases until they aren't.

What changes my mind on this is not any single failure but the pattern: screenshot-based failures tend to be complete failures. The agent either correctly parses the screenshot and acts appropriately, or it misparses it and produces an action that is confidently wrong. There is less middle ground than there is with API-based actions, where partial failures can often be detected and handled gracefully.

This is the practical distinction worth knowing: screenshot grounding is not a reliable perception mechanism. It is a statistical inference from pixel patterns, with all the brittleness that implies. Whether that's acceptable for a given workflow is a real engineering tradeoff, not a technical detail to defer.
