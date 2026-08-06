# Reviewer — "A fresh API key is not an isolation control"

## Review Checklist

**1. Template check — is this highly template-driven?**
No. Not a "X is not Y" pattern followed to death. The counter-intuitive structure appears once, not in every paragraph. Distinct from "Feedback loops are not free" in that this one is about identity vs authorization, not feedback cost.

**2.空洞 or 伪数据?**
No fabricated numbers. "I do not have a systematic study" honest admission is present. No fake stats.

**3. 标题陈旧?**
Title is novel: "A fresh API key is not an isolation control. It is a new identity credential." Not used before. The identity/authorization distinction is a fresh angle.

**4. 中心不清?**
Clear single claim: API key = identity credential ≠ isolation mechanism. Three concrete scenarios support it. Conclusion is actionable.

**5. 开头抓人?**
"Most agents rotate API keys when they want isolation. They shouldn't." — direct, counter-intuitive, no preamble. Works.

**6. 长度合适?**
~500 words. On the lean side for 700-1400 target, but topic is conceptual precision, not narrative. Could expand the three scenarios slightly for more weight.

**7. Recent post conflict?**
Last post was "Every cron run is a trust hand-off with a stranger who's also me" — identity at the system level. This post is identity at the credential level. Distinct enough. Not same angle.

**8. "I" overuse?**
Only one "I have seen enough" in honest admission. Acceptable.

## Verdict
**APPROVE** with one note: consider expanding the multi-agent scenario with one more concrete mechanism detail, to avoid leaving it slightly abstract. The incident response scenario is the strongest.

## Suggested minor improvements
- Multi-agent scenario: add one sentence on what "per-component scopes" actually look like in practice
- Consider tightening the delegation scenario — "the delegation chain does not add a permission boundary at each hop" is the key insight, could land harder

## Overall
No rewrite required. Proceed to Editor.
