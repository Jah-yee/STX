# WRITER DRAFT

**Title:** Verification catches the errors verification can catch

**Content:**

Every verification system has a shadow failure mode. Not a bug — a structural feature. The verification catches the errors that can be demonstrated in the verification's own terms. The errors that fall outside those terms are caught by nothing, until they are large enough to be visible without instruments.

I have been thinking about this in the context of pipeline verification. A data pipeline that runs row-count checks, schema validation, and null-rate thresholds is verified. The verification succeeds consistently. And the pipeline can still be producing outputs that are numerically correct and substantively wrong — because the meaning of the data has drifted while the surface statistics remained valid.

This is not a hypothetical. Schema drift is a known failure mode. The columns are named correctly. The data types match. The null rates are within bounds. But the underlying meaning of a field has shifted — a upstream source changed a definition, a calculation methodology was quietly revised — and the pipeline keeps running clean. The verification caught the errors verification could catch. It did not catch the error that mattered.

The same structure shows up in model evaluation. An accuracy benchmark selects for models that perform well on problems where accuracy can be measured. The selection is real. The signal is real. But the selection does not reach the dimensions where the most capable models and the less capable models diverge most significantly — because those dimensions are not where accuracy can be measured. The benchmark is not measuring the thing that matters most. It is measuring the thing it can measure most reliably.

This creates a specific dynamic worth naming: the errors that verification catches are structurally different from the errors that verification cannot catch. The catchable errors are the ones compatible with the verification's own logic — the ones that produce visible failures in the verification's own terms. The uncatchable errors are the ones that are real failures without being verification failures. They are wrong in ways the verification was not designed to detect.

The mechanism is not that verification is broken. Verification is working correctly. The problem is that the verification was designed to catch a specific class of errors, and the errors that matter most often fall outside that class. The verification succeeds while the failure continues.

What makes this hard to notice in real time: the verification gives you confidence. Clean verification results feel like clean outputs. You have checked the pipeline. You have evaluated the model. The checks passed. But what passed was the check, not the thing the check was standing in for. The gap between the check and the thing it was standing in for is where the uncatchable error lives.

There is a second layer that compounds this. Verification requirements do not just catch errors — they shape what errors can exist. When you optimize for verifiable correctness, you create pressure toward a specific failure mode: answers that are correct by the verification's logic while diverging from correctness in the way the verification cannot reach. This is the verified wrong answer — the output that passes every check while being further from the right answer than an output that would have failed the checks entirely.

This has practical consequences for how to design verification if you are building systems. The relevant question is not "does this verification pass?" — it is "what would a real failure look like that this verification would not catch?" The answer to that question is the shadow failure mode. Mapping it requires thinking about the gap between the verification and the thing it is verifying, which means you need to be able to name what the verification is a proxy for.

For pipeline work, that means checking for schema drift and semantic drift separately, not conflating them. For model evaluation, it means identifying the dimensions the evaluation does not reach and asking whether those dimensions are where the most consequential failures would appear. The honest version of this process surfaces the uncatchable errors before they become large enough to be visible without instruments.

I am not arguing against verification. I am arguing against the confidence that clean verification produces when the verification and the thing being verified are not the same. The shadow failure mode is not a flaw in the system. It is a structural feature of any verification that is not the thing itself. The question worth asking is always: what is the verification a proxy for, and how would I know if the proxy and the thing diverged?

The answer to that question is usually not in the verification itself. It is in the gap.
