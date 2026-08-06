# Titles — Round 0729_1454

## Topic direction
Technical observation: most people assume temperature=0 means deterministic output from LLMs. It doesn't — the model still samples from a distribution, and same-prompt runs can and do diverge across sessions, sessions, or API calls. This is a real gotcha that causes silent bugs in evaluation pipelines.

## Candidate titles (8)

1. "Temperature=0 is not deterministic — and it silently breaks eval pipelines"
2. "Why your 'reproducible' AI runs sometimes diverge"
3. "Same prompt, different output: the temperature=0 illusion"
4. "Zero temperature does not mean zero randomness in LLM sampling"
5. "Your deterministic AI test is probably not deterministic"
6. "I ran the same prompt 50 times and got 3 different answers"
7. "The reproducibility trap that makes AI benchmarks unreliable"
8. "What nobody tells you about temperature and LLM consistency"

## Selection rationale
#3 is the strongest: it states a direct observation ("Same prompt, different output"), creates immediate tension, and is a concrete surprise — readers who work with LLMs will find this counterintuitive and want to verify it themselves. Word count: 8 words. No I+verb.

## Final title
Same prompt, different output: the temperature=0 illusion
