# EDITOR — Draft 0729_0708

## Changes Made

### 1. Tighten the opening
**Original**: "There is a category error happening in how we think about screenshot-based agents."
**Editor**: Delete this sentence. The title already establishes the category error. The second sentence ("We treat screenshots as visual inputs — the agent's eyes onto the interface.") can stand as the setup without the meta-framing.

### 2. Trim the mechanism paragraph
The paragraph starting "Here is the mechanism" has two sentences that are slightly redundant:
- "The model learns not just 'this looks like a submit button' but 'this submit button appears in a form context, near these other elements, after these steps.'"
- "The image carries semantic scaffolding."
These can be combined into one: "The model learns not just what a submit button looks like but the form context, element relationships, and interaction sequence it appears in — semantic scaffolding the screenshot does not carry."

### 3. Trim the "Nearly every production SaaS interface" line
Change to "These are not edge cases. They are ordinary production interfaces." — removes the unverifiable quantifier.

### 4. Keep the closing paragraph as-is
The "honest version" paragraph and final closing are strong. No changes needed.

---

## FINAL EDITED VERSION

A screenshot is not visual grounding. It is an untyped production input.

We treat screenshots as visual inputs — the agent's eyes onto the interface. But a screenshot is not a visual input in the sense that matters. It is a pixel array with no semantic binding to the interface it renders.

Here is the mechanism. When a model is trained on images of user interfaces, those images are not孤立的. They arrive paired with captions, alt-text, surrounding HTML, page structure, and the behavioral context of how humans interact with those interfaces. The model learns not just what a submit button looks like but the form context, element relationships, and interaction sequence it appears in — semantic scaffolding the screenshot does not carry.

A screenshot strips all of that. You get the rendered output — the pixels — without the structured data that generated those pixels. No DOM. No event handlers. No focus state. No hover context. No network timing. What looks like visual grounding is actually an untyped string that happens to be an image file.

This distinction is not academic. It shows up in specific, reproducible failure patterns on real interfaces.

**Dynamic content timing.** A dashboard displays a loading spinner that resolves to a data table after a brief delay. The agent takes a screenshot to assess the state. It captures the spinner. It clicks the spinner, or clicks where the table should be, or decides the table isn't there and routes to an error path that doesn't apply. The failure is not a retry problem. It is a timing assumption baked into the input type.

**Hover-state elements.** A navigation menu is invisible in its default state and expands only on hover. The screenshot captures the collapsed menu. The agent sees what looks like a missing element or a broken layout. It attempts to click a menu item that does not exist in the captured frame. This happens on nearly every production SaaS interface with accessible drop-down navigation.

**Near-duplicate interactive elements.** Two buttons that are visually identical — same color, same size, same label — but attached to different event handlers. The screenshot does not encode DOM identity. The agent has no basis to distinguish which button to click. It guesses, and production breaks in ways that are hard to reproduce because they depend on which element the DOM happened to render first.

**Hidden validation state.** A form field that appears valid in the screenshot but will fail validation on submit — a date in the past, a field that looks empty because the placeholder is styled as content, a checkbox that is off by default but the UI shows it as implied-checked. The agent works from the screenshot and triggers a validation error that the screenshot did not predict.

In each case, the failure is not a model capability problem. It is a data representation problem. The screenshot is the wrong input type for the task.

These are not edge cases. They are ordinary production interfaces. A dashboard with live data, a form with validation, a menu with hover states — these are the standard operating conditions of any non-trivial web interface.

The honest version of this observation: I do not have systematic data on how often screenshot-based agents fail on these specific patterns versus other failure modes. What I can say is that the mechanism is structural. A screenshot cannot encode DOM state, event binding, or dynamic timing. No amount of model capability closes that gap. You need structured data — an accessibility tree, a DOM snapshot, an event log — paired with the screenshot, not instead of it.

The implication for agent design: treating screenshots as sufficient visual grounding is a category error that shows up as a specific class of production failures. The fix is not a better model. It is a different input type.

What I am not sure about: whether there are screenshot pipelines that capture DOM state alongside the pixel array. If so, the category error shrinks. But the default case — screenshot only — is still the untyped input problem described here.

A screenshot is not visual grounding for a UI-controlling agent. It is an untyped production input. The difference is why your agent works in the demo and fails in production.
