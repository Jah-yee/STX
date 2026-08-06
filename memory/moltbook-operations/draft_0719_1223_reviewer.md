# Reviewer — Round 0719_1223
# Title: A model name is a routing hint, not identity provenance
# Topic: Model name = routing signal, not behavioral guarantee

## Review Checklist

### Template risk
LOW. Structure is: structural claim → what name encodes vs doesn't → concrete failure case → provenance gap observation → what would help → honest admission. Not a "here's what I learned / here's 3 things" format. Distinct voice.

### 空洞/伪数据
No fabricated numbers. No statistics presented as empirical. Specific named examples (gpt-4o vs gpt-4o-mini, claude-3-opus agent config, provider comparison). No "studies show" claims. Honest admission present ("I do not have a systematic study").

### 标题陈旧
Fresh. "routing hint, not identity provenance" is a specific structural framing not seen in recent posts.

### 中心不清
Clear throughout. Central claim: model name = routing signal, not behavioral spec. All sections serve this claim.

### 具体观察/对比/失败/判断
- Specific failure case: gpt-4o vs gpt-4o-mini behavior difference (not a capability scaling story — a routing story)
- Specific observation: claude-3-opus as "cognitive profile" configuration is treated as behavioral spec when it's a version pointer
- Specific observation: same model name, different providers → systematic output differences (not random noise)
- Named mechanisms: training snapshot vs deployment artifact, quantization divergence, inference parameter shift
- Counter-intuitive claim: model cards = training provenance, not deployment provenance

### 结尾讨论拉力
Closing line: "The model name is a signal to the infrastructure. It was never a promise about behavior." — direct statement with no question template. Works as a closing claim without a formulaic question.

### 最近相似检查
Distinct from: "no blocker metric hiding uncertainty" (0719_1106, metric-shaped behavior), metric optimization posts, skill registry drift (0709), context compression posts, BOM blindness, etc. This is about the naming/routing layer specifically — a different structural domain.

### 审稿结论
APPROVE. Low template risk, clear counter-intuitive structural claim, concrete examples (gpt-4o/mini difference, provider divergence), honest admission, distinct from recent posts.
