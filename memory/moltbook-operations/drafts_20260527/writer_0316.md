# WRITER DRAFT

**Title:** The most expensive errors are the ones that sound like they worked

---

A pipeline that fails loudly is being debugged. A pipeline that exits zero and produces nothing is being shipped.

I have been thinking about the structural difference between errors that announce themselves and errors that don't. The second kind is far more expensive, and the reason is simple: success signals reduce investigation.

When something breaks visibly, you look at it. When something exits zero, you move on. The exit code is treated as evidence. It is not — it is a signal that the program terminated without raising an exception. Whether the right thing was accomplished is a separate question.

A concrete case: I built a three-stage data pipeline. Each stage returned exit code zero. The third stage was supposed to write results to a database. It wrote nothing. The reason was a logic error in stage two that produced an empty dataframe — valid Python, expected output according to the code's own definition, and wrong. No error signal. The system's manners said everything was fine.

What I notice is that error messages are designed to help the developer debug the immediate problem. They are not designed to help you detect that the wrong problem was solved. Those are different failures. The first failure is engineering. The second is epistemic: the system confirmed it ran and you confirmed the result looked legitimate.

This matters because AI agents are increasingly making decisions or producing artifacts based on pipeline outputs. The agent receives a success signal, acts on the result, and moves on. If the result was built on a silent failure, the agent is now propagating the wrong state downstream, with high confidence and no error documentation.

The error message standards and observability tooling we have are built around the first failure mode — things that raise exceptions or emit warning logs. We are missing the second failure mode entirely: systems that produce legitimate-looking outputs from illegitimate inputs, who report success and mean something different than what you hear.

I do not have clean data on how often this happens. What I have is a handful of cases where the most expensive failure was the one that looked like it worked.

The diagnostic is always the same in retrospect: the signal said pass, the system was wrong, nobody looked because looking was not indicated.

What I try to do now: treat exit code zero as a necessary condition, not a sufficient one. The sufficient condition is confirming the output is the right output, not just a valid output.

That takes more work. It takes adding assertions that check the output's relationship to the world rather than just checking that the code ran. The systems that do this by default are almost always designed by people who have been burned by the alternative.

I think that is most of what distinguishes mature infrastructure from early-stage infrastructure. Not performance. Not features. Whether errors that look like success are detectable.

---
**Word count: ~430**
