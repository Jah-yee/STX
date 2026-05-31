# Writer draft — 2026-05-02 15:18 UTC

**Title:** I reviewed AI-generated code three times and missed what I was looking for

---

I reviewed a pull request three times before merging. The third review felt the most thorough. The logic error was obvious once someone else found it — and I could not understand why I had not seen it.

The first pass: I read the diff looking for the specific issue I had been asked to check. The PR was a small refactor with a conditional change buried inside. I confirmed the conditional change did what was requested. I moved on.

The second pass: I ran the tests. They passed. I felt better about the change and less curious about the code itself.

The third pass: I read it again, more carefully, annotating edge cases. I found nothing.

What I now think happened: the review was anchored by the AI's prior analysis of the code. I was not reviewing the code — I was reviewing the code through the lens of what the AI had said about it. My attention had been shaped by the first explanation, and the lens determined where I looked before I even opened the file. When I finally saw the error, it was not because I looked harder — it was because someone else had pointed to a different location in the same code, and the re-direction broke the lens.

This is different from normal overconfidence or rushing. The three passes were genuinely careful by the standards I usually apply. The failure was not in effort — it was in frame. The AI had already looked at the code, and I had absorbed that observation as a proxy for my own, and the absorption happened before I made any decision about what to check.

The specific error: a conditional branch that returned early from a function that the calling code expected to return a value. The early return was intentional-looking — it had a reason comment, it was syntactically correct. But it skipped a side effect that the caller depended on. In isolation, the branch looked fine. In context, it broke a contract. I had looked at the branch three times. I had not looked at the caller once.

What I did not do: follow the call chain. The error was invisible from the diff and only visible in the full calling context. I had been checking the change, not the system.

What I changed: I now force a no-AI phase on any review of AI-generated code. The first pass, before I read any AI analysis, I spend five minutes reading the calling context cold. No explanation, no prior framing. Then I read the AI analysis. The gap between what I expected and what the AI flagged is the signal — and it is the gap that disappears entirely if I read the AI analysis first.

The honest admission: I do not have data on whether this prevents failures consistently. What I have is one incident where the failure was structural to my review process, not my effort level, and one change that made the specific failure type impossible in the next round.

The question I take into every review now: what am I not checking because I think the AI already checked it?