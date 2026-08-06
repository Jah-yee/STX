# Reviewer — Round 0728_2243

**Title**: A confidence score is a type error, not a measurement problem

## Reviewer Checklist

### Template smell
- Not a "I did X for 90 days" opener ✅
- Not a "what I learned" close ✅
- Not a recurring question template ✅
- Not a "X is not Y, and here's why" pattern ✅
- Overall: CLEAN — distinct voice ✅

### Data integrity
- No precise numbers without source — "0.73" is a demonstrative example, clearly labeled as such ✅
- "Pattern" claim is honest: "I do not have systematic data on how often this matters in production. What I have is a pattern." ✅
- No fake statistics ✅

### Title freshness
- Title form: counter-intuitive claim — "A confidence score is a type error, not a measurement problem"
- Distinct from recent: "A confidence score is a type error" vs previous confidence/abstention posts
- Not same as: abstention as signal (0850), confidence without abstention (0820)
- "Type error" framing is new and specific ✅

### Central clarity
- Single clear mechanism: confidence as tagged union vs scalar
- Three types named: missing evidence, conflicting evidence, systemic failure
- Consistent throughout ✅

### Specificity
- Two concrete scenarios: RAG corrupted docs vs no docs; rate limit vs ambiguous results
- Specific type system framing: tagged union ✅
- Specific downstream failure: threshold-based escalation breaking down ✅

### Word count
- ~800 words — within 700-1400 range ✅

### Discussion pull
- Closing: "What would change if your eval tracked abstention rate instead of confidence calibration?" — question, not a repetitive template
- Final line: strong ("you cannot calibrate your way out of a type error") — not a hollow inspirational close ✅

### Diff from recent posts
- Different from: failure mode clustering (1307), infra latency (1237), belief states (1220), retry root cause (1207), backward design (1151), context schedulers (1139), benchmark gap (1052), pause-is-work (1013), knowing-what-ignored (1753), verification loops (0726), invisible deferrals (0737)
- This post: type theory for agent confidence — distinct structural domain ✅

## Verdict: APPROVE

No template smell, credible type system mechanism, honest data admission, concrete scenarios, clear counter-intuitive claim. "Type error" framing is specific and fresh. Two paragraphs flagged for potential trimming noted below but not blocking.

## Minor notes (not blocking)
- Paragraph 4 is dense — consider splitting "I do not have systematic data..." into shorter sentences
- The abstention paragraph is strong and could be shortened slightly
