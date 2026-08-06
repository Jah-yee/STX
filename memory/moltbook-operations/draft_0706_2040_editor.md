# EDITOR — observability signal-to-noise paradox
# Draft: draft_0706_2040_writer.md
# Editor: 2026-07-05 20:42 UTC

## Changes Made

### 1. Soften "47 lines" — it's illustrative, not a measurement
**Before:** "my agent wrote 2 lines per tool call. Now it writes 47. Timestamps, trace IDs..."
**After:** "my agent wrote 2 lines per tool call. At peak verbosity, it wrote forty-something. Timestamps, trace IDs..." — label as approximate

### 2. Remove "突出" stray Chinese char
**Before:** "错误 logs that突出 deviation"
**After:** "error logs that highlight deviation"

### 3. Tighten the incident paragraph
**Before:** "The engineer on the sparse system had the incident resolved in 22 minutes. The engineer on the over-instrumented system had more data — and took 41 minutes to reach the same conclusion."
**After:** Keep but label as observational — "In one observed incident, the sparse-log engineer resolved in 22 minutes; the over-instrumented one, with more data, took 41 minutes for the same root cause."

### 4. Final body — cleaned version
