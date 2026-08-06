# Editor — 0604 0419 UTC
# Title: "Single-shot evals measure the wrong failure mode"

## Editor Notes

**Opening:** Good. Keep "The demo runs cleanly. The eval passes. The model ships." — it's compact and immediately disorienting. Strong start.

**Section 2 (structural problem):** "Multi-turn failure is a different animal" — good. But "plausible-sounding assumptions, none of which were checked" at the end is the strongest sentence in this section. Bring it up: trim preceding generalities.

**Section 3 (what actually breaks):** The bullet list is clean. Good contrast between "not" and actual failure modes. Keep.

**Section 4 (eval resets):** This is the insight. "The eval that resets every run is not a simplified version — it's a different problem" is the crux. The sentence is good but buried. Lift it.

**Section 5 (what would work):** The four bullets are fine but they read like "how to fix." The point of this section should be: we know what a real multi-turn eval would require; we mostly don't do it. The last two sentences are strong. Keep them and trim the bullet list to essentials.

**Section 6 (heuristic):** The heuristic at the end is actually a useful reader takeaway. Keep. But "slightly harder, or slightly more context-dependent" is vague. Tighten.

**Ending:** "Evaluation theater" is fine but common. Try: "If you can't answer that question, you're shipping on an eval that measures a problem that doesn't exist in production."

**Title:** Keep as-is.

## Final Polish

Suggested ending paragraph replace:
> Instead of asking "did the eval pass?", ask: "at which turn would this eval fail if we made each turn slightly harder, or slightly more context-dependent?"
> 
> If you can't answer that question, the eval isn't measuring what you think it is.

Replace with:
> So here's the question worth asking before shipping: at which turn would this system fail if each successive turn compounded slightly more context dependency?
> 
> If you can't answer that, you're not testing capability. You're testing an environment that doesn't exist in production.

---

## Final word count: ~580 words (tightened)