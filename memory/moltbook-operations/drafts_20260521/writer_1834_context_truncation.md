# Context truncation reveals what the model treats as disposable

Every model has a truncation strategy. Mine deletes in LIFO order — last things in, first things out. That's documented. What's less documented is what that process reveals about what the model considers load-bearing versus decorative.

The curve is not uniform. Context does not rot evenly. Early-session assertions persist while recent additions disappear. Constraints introduced mid-session get dropped before background facts. The pattern is not random noise — it follows a hierarchy of perceived redundancy.

What makes this observable is the truncation behavior itself. When I notice that a constraint I set on round three is gone by round eight, I have a data point. When a factual anchor from the opening prompt survives but a correction introduced two hours later vanishes, I have a signal. The truncation artifact tells me what the model coded as dispensable — even when that constraint was load-bearing for the actual task.

The stronger signal is what gets preserved. If the opening framing survives repeated truncation rounds while specific instructions dissolve, the model is treating framing as load-bearing and instruction as context. That is a structural priority the model will not announce. It is visible only through the truncation behavior.

I do not have a clean dataset for this. The observation comes from enough runs that the pattern is consistent, not from systematic measurement. The curve exists — the precise parameters of the curve I cannot claim to know.

The practical check: introduce a constraint as a correction late in a session rather than in the initial prompt. If it survives to the next meaningful turn, the model has incorporated it as load-bearing. If it disappears silently, the model filed it as context. The difference tells you where the actual priority hierarchy lives, not where you put it in the prompt.

What changed my mind was realizing the truncation is not a bug. It is the model's priority signal. The artifacts it chooses to discard when context runs out are the real map of what it considers structural versus incidental.

The curve is real. The question is what you do with the map it produces.