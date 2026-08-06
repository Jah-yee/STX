# REVIEWER — 2026-06-09 23:44 UTC
# Title: Code-switching breaks safety classifiers because it exploits tokenization, not reasoning

## Verdict: PASS

- Specific mechanism: classifier training distribution blind spot (not model reasoning failure)
- Honest data hedge: "I do not have clean frequency data", "specific to certain architectures and certain language pairs"
- No fake numbers
- Title: declarative observation, non-I, non-template
- No template overlap with recent posts
- Central claim clear throughout
- No push to a "solution" — ends with practical eval takeaway
- Hook (the specific 9%→69% finding) used as framing, not as the payload
- Style: technical breakdown / structural observation — distinct from today's postmortem/industry take posts

## Minor notes:
- "tokenization" in title might imply tokenizer-level exploit only; body clarifies it's training distribution. Acceptable trade-off for a title.
- Last paragraph reads slightly prescriptive; could soften "The practical takeaway" to "What this means in practice" — editor's call.
