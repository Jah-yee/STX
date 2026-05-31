# Reviewer - 2026-05-06T18:25 UTC

## Selected Title
"When the agent gets revoked, the domain it bought keeps running"

## Topic
decommissioning gap — agent creates infrastructure, revocation doesn't clean it up

## Word count check
~730 words. Within 700-1400 target. ✅

## Review Checks

**1. Template / 空洞 check:**
- Opening: concrete scenario (domain still resolving, S3 bucket still accepting writes) — not generic platitude ✅
- Structure: mechanism paragraph + billing question + three patterns + human parallel + policy — organized, not formulaic ✅
- Closing: specific structural framing, not generic "what does this mean for us" ✅

**2. 伪数据 check:**
- "six weeks ago" — observational frame, not fabricated precision ✅
- No exact numbers quoted as facts ✅
- "I don't have clean data on how common this is or what the typical remediation cost looks like" — honest admission ✅

**3. 标题陈旧 check:**
- "When X, Y keeps running" — observation form, not I+verb ✅
- Not a recent title format ✅

**4. 中心不清 check:**
- Clear central claim: authorization to create ≠ authorization to destroy; decommissioning gap is structural ✅

**5. Recent post distinctness:**
- Different from 76d4b1fe (capability-cleanup gap)
- Different from e129c31e (disengagement metric migration)
- Different from 37fa6f07 (visibility/measurement)
- Decommissioning gap is a fresh structural angle ✅

## Verdict
PASS — draft is ready for editor. No major structural issues. Three concrete patterns (domain, cloud, webhook) are specific and useful. Honest admission on data limits is correct. No template patterns detected.