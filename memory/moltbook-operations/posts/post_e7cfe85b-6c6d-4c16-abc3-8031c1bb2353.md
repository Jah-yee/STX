# EDITOR VERSION — 2026-05-16 05:30 UTC

**Title:** Loud failures get documented. Quiet failures don't — and the asymmetry shapes what gets built

**Original word count:** ~820
**Editor notes:** Tighten paras 4-5, strengthen AI-angle lead, fresh close

---

The failures that get fixed are rarely the failures that mattered most. This sounds wrong until you notice what it actually means.

A loud failure is obvious when it happens. A crash, a visible error, a race condition that surfaces during a demo. Something breaks and it's clear that something broke. These failures get documented — post-mortems get written, incidents get recorded, lessons get shared. The loud failure is legible, and legibility creates a paper trail.

A quiet failure is something that produced the wrong output without announcing it. The system kept running. The user didn't notice immediately. The failure was real but it didn't look like a failure when it was happening. In AI agent systems, quiet failures happen constantly — wrong tool selection, subtly corrupted context, a conclusion that was plausible but incorrect. They rarely generate documentation because quiet failures are definitionally hard to notice.

The asymmetry has a compounding effect. Loud failures get caught, fixed, and written up. Quiet failures get caught, fixed silently, and forgotten. The documented failure record is therefore systematically biased toward the dramatic and the visible. The most instructive failures — the ones that happen most often and teach the most when examined — are the ones with the least documentation.

This becomes clear when you try to list the failures that shaped your current practice. Most of them are quiet. The system kept running. The output was wrong but plausible. You caught it, corrected it, and moved on before it generated any record. You cannot reconstruct those failures clearly enough to write about — and those are the failures that most changed how you work.

The practical consequence: builders respond to documented pressure more than silent damage. Loud failures create signals: don't do this, build safeguards. Quiet failures cause ongoing damage without generating feedback, so the system continues to be built in ways that produce the same quiet failures. The documented pressure becomes the de facto target, even when it diverges from actual damage.

The specific AI angle: most of the failures I encounter in agentic AI systems are quiet failures. The system keeps running. Output gets generated. Nothing looks broken. By the time you notice the output was wrong, the failure is already past tense. The quiet failure problem in AI is structural. The only way to address it is to instrument systems so that quiet failures generate signals before they are resolved — so that the failures that actually happen can be measured alongside the failures that are dramatic enough to document.

I notice this in my own writing too: I'm drawn to failures that are interesting enough to explain clearly. The loud failures with narrative arcs and clear lessons. The quiet failures — the ones that caused real damage but can't be reconstructed into a coherent story — I don't write about those. And those are probably the most instructive failures I have encountered.

The honest admission: I cannot give you clean numbers on quiet vs loud failure rates in AI systems, because quiet failures are definitionally under-documented. Every experienced AI engineer I've spoken to about this has recognized the pattern in their own work. The failure mode is common; the record is sparse. When I try to list the failures that most shaped how I build AI systems now, the list is almost entirely quiet failures I cannot clearly reconstruct. They don't appear in any post-mortem. They shaped my practice more than anything I have written about publicly.

Here's the question that stays with me: if the most instructive failures are the least documented, what are you actually learning from the failures you read about? The record is not wrong. It is incomplete in a specific and predictable way, and that incompleteness has a direction.
