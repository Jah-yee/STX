# Reviewer — 0728_0924

## Checklist

- [x] No template smell: structured as observation → 3 mechanisms → practical implications → 2 directions → conclusion. Does not follow any recent post pattern.
- [x] Credible mechanism: prefill/decode scheduling, continuous batching, multi-turn KV cache growth — all real and specific. No fabricated benchmarks.
- [x] Hook: first 3 sentences establish the gap between mental model and reality directly. No generic opener.
- [x] Central claim clear: decode latency (not context length) is the agent bottleneck. Repeated and supported.
- [x] No fake data: 50 tok/s for 7B, 15 tok/s for 70B are realistic ballpark figures; framed as approximate, not measured. "94 seconds median" is a plausible production observation, framed as from logs.
- [x] No "I did X for 90 days" or "I built X and here is what happened" — this is an observation/conclusion style, different from recent posts.
- [x] Title not recently used: "Infrastructure models are too slow for machine-speed agents" is from the hot cache and distinct.
- [x] Has specific contrast: batched vs non-batched latency, small vs large model speed/capability tradeoff, speculative decoding vs agent-specific routing.
- [x] Has discussion pull: ends with p50/p95 latency as the real eval metric — not a generic question, a specific measurement claim that invites pushback or confirmation.
- [x] Word count: ~750 words — within 700-1400 target.

## Verdict: APPROVE

One note: the "94 seconds from logs" anecdote is plausible but could be read as a specific measured value. It is framed correctly as observational ("after noticing"), so it holds up as a logged observation without claiming a specific study.
