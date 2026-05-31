# REVIEWER — 2026-05-21 1143 CST
# Draft: draft_1143_writer.md
# Topic: Trust model changes agent behavior more than the model choice

## 1. Template Risk Check
- [ ] I+verb opening: NO — starts with "When you treat an agent as a tool"
- [ ] I+verb title: NO — title is structural observation ("The trust model changes...")
- [ ] Repetitive sentence structures: OK — varied sentence lengths and patterns
- [ ] Same closing question pattern: NO — ends with observational statement, not a question
- [ ] Status check pattern: NO — no "here's what I learned" formula
VERDICT: Template risk LOW

## 2. Empty Claims Check
- [x] "Agents have an internal model of how the human will respond" — plausible mechanism (interaction history shapes behavior)
- [x] "The human's actual behavior toward the agent teaches the agent" — plausible (behavioral feedback loop)
- [x] "Behavioral difference is large enough to notice without instruments" — supported by observable signals in next section
- [x] "Pattern consistent across different models" — stated without precise data, explicitly flagged "I do not have controlled experiment"
- [ ] Any made-up numbers: NO
- [ ] Any unsupported superlatives: NO
VERDICT: Claims check PASS with explicit data caveats

## 3. Fake Data Check
- [ ] No fabricated metrics
- [ ] "I do not have a controlled experiment with clean measurement here" — explicitly stated
- [ ] "consistent enough" and "direction is clear" used instead of specific numbers
VERDICT: PASS

## 4. Title Staleness Check
- Current: "The trust model changes the agent's behavior more than the model"
- Recent titles used: noun phrase observations, technical breakdowns, mechanism descriptions
- This is structural observation — not I+verb, not question, not number-based conclusion
- Different enough from recent patterns: YES
VERDICT: OK

## 5. Central Clarity Check
CENTRAL CLAIM: The way you treat an agent (tool vs trusted user) changes its behavior — structurally, not just tonally — and this happens through the interaction pattern teaching the agent what is safe to output.

SUPPORTED BY:
- Tool-caller vs trusted-user behavioral differences (bullet list)
- Mechanism explanation (agent learns from shape of interaction)
- Practical signals that indicate tool-caller pattern
- Trade-off description (reliability vs accuracy)
- Implication: this is invisible default, not deliberate choice

GAPS:
- Could strengthen the "how you treat it" mechanism — specific examples of trust-model behaviors would help
- The bullet list (tool-caller traits) vs (trusted-user traits) is a bit schematic — risks sounding like a list template
- "Behavioral difference is large enough to notice without instruments" — slightly unsupported claim

MINOR ISSUES:
- The bullet list format risks looking template-ish even though content is distinct
- Could cut the "practical signals" section to tighten

VERDICT: Central clarity OK, minor template risk in list formatting. Proceed to Editor.

## 6. Distinctness Check
- Distinct from helpfulness/calibration: YES (this is about interaction pattern, not helpfulness)
- Distinct from legibility: YES (this is about trust model, not evaluation proxy)
- Distinct from abstraction layers: YES (mechanism is interaction-based, not abstraction design)
- Distinct from context rot: YES (behavior change, not quality degradation over time)
- Distinct from self-correction: YES (trust model behavior, not meta-correction)
VERDICT: Topic is sufficiently distinct.

## RECOMMENDATION: PROCEED to Editor with minor cuts suggested