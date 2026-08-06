# Editor — Round 0730_0641

## Reviewer verdict: APPROVE. 3 surgical changes.

### Change 1: Opening hook tightening
**Before:** "Ask an AI to 'write a function that sorts a list.' You get one answer. Ask it to 'write a function that sorts a list, prioritizing clarity over speed,' and you get a structurally different answer — different names, different control flow, different comments. The model has not changed. The question has."
**After:** "Ask an AI to 'write a function that sorts a list.' You get one answer. Ask it to 'write a function that sorts a list, prioritizing clarity over speed,' and you get a structurally different answer. The model has not changed. The question has."
**Rationale:** The enumeration "different names, different control flow, different comments" is implicit in "structurally different answer." Removing it makes the contrast sharper without losing substance. Simplicity First.

### Change 2: Trim "What changes when you see it" header sub-section
**Before:** "What changes when you see it" — then two paragraphs of practical guidance
**After:** Delete the header and merge the key sentence into the next paragraph:
"The practical shift is treating your prompt as a specification document, not just a request. Not in the elaborate template sense — in the basic sense of asking: what decision am I asking the model to make on my behalf? What should it optimize for? Who is reading the output?"
**Rationale:** The header adds structure weight without new content. The paragraph that follows is the useful substance — keep the substance, drop the structural signal. Surgical change.

### Change 3: Final paragraph trim
**Before:** "I do not have a clean prescription for framing your prompts perfectly. The rules are different for different tasks, different models, different tolerance for the model filling in unspecified gaps. What I can say is that when you find yourself rephrasing the same question two or three times to get something useful, the rephrasing is not a workaround. It is the work. The first prompt is where the problem lives."
**After:** "I do not have a clean prescription for this. The rules vary by task, model, and how much gap-filling you want the model to do. What I can say is this: when you catch yourself rephrasing the same question to get something useful, the rephrasing is not a workaround. It is the work. The first prompt is where the problem lives."
**Rationale:** "The rules are different for different tasks, different models, different tolerance for the model filling in unspecified gaps" is three vague qualifications in sequence — trim to the essential point ("The rules vary by task, model, and how much gap-filling you want the model to do"). Keep the memorable closing intact.
