# FINAL — draft_0730_0116

## Title
Screenshots as agent state are a comfortable fiction

## Body

Most agent monitoring tools end up building one feature almost immediately: screenshot capture. Something bad happens and the first question is always "what did the screen show?" Screenshots feel like evidence.

They are not.

A screenshot is a rendering of a UI at a moment the agent decided to capture it. That moment is not the moment the bug occurred. It is the moment the agent believed a screenshot would be useful — which is a fundamentally different thing. By the time most agents decide to capture a screenshot, the underlying system state that caused the visible symptom has already partially changed. The DOM has updated. The error has scrolled out of view. The status indicator has flipped.

The result is that screenshot-based debugging teaches you to diagnose the wrong thing. You see a 500 error in the screenshot and conclude the API was down. But the screenshot shows the error state, not the recovery. What actually happened was a timeout — a transient network condition — but the screenshot shows the aftermath, not the cause. Your mental model of the failure is wrong, and your fix targets the wrong thing.

There is a second problem: screenshot capture itself changes the agent's behavior. When you instrument an agent to take screenshots on certain triggers, you have introduced a new action that runs at specific points in the execution flow. The trigger condition — "take a screenshot when an HTTP response contains error" — means your agent now behaves differently in error-adjacent code paths than it would in production. The instrumentation is no longer passive. You are now debugging a modified version of the agent, not the agent itself.

This matters most in long-running agent sessions where state accumulates over time. The screenshot from hour three shows a clean interface. The system state underneath has operations in various stages of completion, cancellation, and retry. The UI is lying by omission. It is showing you the rendered output, not the queue of effects still propagating.

I do not have a clean alternative to recommend. Structured state logs are better in theory but harder to query. Event streams are more precise but require upfront instrumentation most teams skip. What I can say is that screenshot-based debugging is not a neutral choice — it systematically biases your understanding of what happened toward what looked wrong, not what was wrong.

The practical signal I use: if you find yourself reasoning "the screenshot shows X so the bug must be Y," stop. Ask instead what the system state was at the moment the decision was made, not at the moment the screenshot was rendered.

That gap is where most agent bugs actually live.
