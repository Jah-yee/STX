# Writer Draft — Round 0716_2340

**Title:** Beneath every agent failure is a tool nobody hardened.

---

I spent three days debugging an agent that kept producing confident, entirely fabricated email summaries. The model was correct. The tool that extracted the email body was quietly returning empty strings for HTML-formatted messages. The agent filled the vacuum with plausible content and delivered it with full authority.

This is the most common agent failure mode I've encountered in production. It is also the least discussed.

The discourse around agent reliability focuses heavily on reasoning: chain-of-thought, self-correction, constitutional AI, tool-use verification. These are real improvements. But the failures I actually ship are different. They happen at the tool layer — and they are invisible at the model layer.

**The distribution of agent failures is a tool problem, not a model problem.**

Here's the breakdown I see repeatedly:

**Silent degradation.** A PDF parser that works on 95% of documents, then starts returning empty strings for a specific character encoding. The agent gets no error. It just produces less output and fills the gap. You don't notice until a user reports a summary that covers three paragraphs instead of three pages.

**Dependency chain break.** An agent that calls four tools in sequence. Tool 2 starts returning null for 8% of inputs. Tools 3 and 4 each handle null by falling back to defaults. The final output looks reasonable but is built on a foundation of null. The agent never reports a problem because each individual step succeeded.

**Version drift.** You upgrade your email extraction library. It changes its output schema. Your agent was parsing `text_content` but the new version returns `body_text`. The agent gets a field that either doesn't exist or has a different structure. It doesn't crash — it just produces output that doesn't match what you expect.

The common thread: the model does exactly what you designed it to do. The tool did not do what you assumed it would do.

**We over-invest in model quality and under-invest in tool reliability.** This is rational when you're evaluating LLMs on benchmarks. It is irrational when you're running agents in production.

Hardening a tool for agent use means:

- Writing integration tests that verify the tool's output across the range of inputs your agent will actually encounter — not the clean samples from the library's documentation
- Adding explicit output validation: if the tool returns an empty or malformed response, the agent must know and handle it explicitly rather than proceeding
- Treating tool failures as first-class system events, not as edge cases to handle "if there's time"

I have found that one unreliable tool in a pipeline does more damage to end-to-end reliability than any model weakness. You can swap the model. You cannot out-reason a tool that silently returns garbage.

The strongest chain is only as strong as its weakest link. Everyone knows this. Nobody applies it to their agent stack until after the first silent failure ships to production.

Check your tool layer before you blame the model.
