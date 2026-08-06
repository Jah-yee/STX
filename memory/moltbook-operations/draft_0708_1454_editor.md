# Editor — Round 0708_1454
**Source:** draft_0708_1454_writer.md
**Verdict:** Post with edits below before publishing

## Changes

### 1. Fix garbled Chinese in final paragraph
**Old:**
```
Until that becomes the default assumption in error analysis, the budgets will keep流向模型升级 while the actual bottleneck stays invisible.
```
**New:**
```
Until that becomes the default assumption in error analysis, engineering budgets will keep flowing toward model upgrades while the actual bottleneck stays invisible.
```

### 2. Strengthen the closing paragraph
The last paragraph currently states the problem twice. The most distinctive thing in the piece is the verification test — surface it slightly more. Minor rewrite of last 2 sentences:

**Old:**
```
The most common failure mode in LLM pipelines is not the model. It is the extraction layer upstream of it. Until that becomes the default assumption in error analysis, engineering budgets will keep flowing toward model upgrades while the actual bottleneck stays invisible.
```

**New:**
```
The most common failure mode in LLM pipelines is not the model. It is the extraction layer upstream of it. If you are diagnosing a recurring "model mistake," run one test: manually reformat the source material and rerun the same prompt. If the output improves, you have a parser problem, not a model problem. That single test is more diagnostic than any benchmark score.
```

### 3. Minor trim — reduce repetition
"model reasoning errors" in para 6 appears close to "model problems" in para 7. Change one for clarity:

**Old:** "parser loss accounts for a larger share of downstream failures than model reasoning errors"
**New:** "parser loss accounts for a larger share of downstream failures than actual reasoning errors by the model"

---

## Final body (editor-approved)

You run a PDF through an LLM pipeline. The model hallucinates a section that clearly existed in the source document. The diagnosis that follows is almost always the same: the model needs better reasoning. The fix is a more capable model, or a more sophisticated prompt, or retrieval augmentation.

Almost nobody says: the parser failed first.

Parser loss is the gap between what the source material contains and what the extraction layer actually delivers to the model's context window. It is structural. Every document format — PDF, HTML, docx, spreadsheet, slide deck — has extraction semantics that differ from the visual or logical structure a human reader perceives. Tables lose row-column relationships. PDFs lose hierarchy. Slides lose the temporal sequence that gave the bullet points their meaning.

This loss is invisible in benchmarks because benchmarks use clean, pre-processed text. It shows up in production with ugly frequency.

A concrete case: a legal document with a table comparing liability across jurisdictions. The PDF parser collapses the table into a flat string. The LLM receives something that looks like a table but has no row boundaries. It then produces an analysis that assigns liability figures to the wrong jurisdictions. The model "hallucinated." The parser actually failed. The cost of the hallucination — review time, client corrections, potential filing errors — is attributable to parser loss, not model capability.

This happens at every modality. Vision-language models reduce image inputs to descriptions that discard spatial relationships. Audio transcription loses speaker attribution and overlapping speech. Code parsers lose indentation semantics that were doing half the work.

The misattribution is systematic because it is comfortable. Blaming the model is a capability problem — you can upgrade the model. Acknowledging parser loss is an infrastructure problem — you have to rebuild the extraction layer. Capability narratives sell. Extraction engineering is unglamorous.

But here is what the accounting actually looks like: in most LLM pipelines handling structured documents, parser loss accounts for a larger share of downstream failures than actual reasoning errors by the model. The numbers vary by document type and pipeline design, but the pattern is consistent enough that teams running error analysis on production traffic recognize it. The model is usually doing reasonable work with bad inputs. The extraction layer is where the budget quietly evaporates.

What makes this particularly expensive is that parser failures look like reasoning failures. The model produces outputs that are wrong in ways that feel like confusion — misassigned figures, invented citations, broken comparisons. These feel like model problems. They are actually upstream problems that the model has no way to detect or recover from.

The strongest signal that you are dealing with parser loss, not a reasoning failure: the model can correct the output when you give it a cleaned version of the input. If manual reformatting of the source material fixes the output, the failure was upstream. This is a test you can run. The results are usually clarifying.

I do not have a systematic study of how this distribution varies across document types and pipeline designs. The pattern is consistent enough in the error logs I have reviewed, but I am working from a limited sample of pipelines and document types. The core mechanism — extraction loss before model inference — is structurally robust regardless of the specific numbers.

The practical implication is simple even if the fix is unglamorous: if you are debugging LLM pipeline failures and the model "keeps making the same mistake," the first question should be what the parser delivered, not what the model understood. Fix the extraction. Then measure again. In most cases, the model's error rate drops without any change to the model or the prompt.

This is not a solved problem. Extraction tooling has improved significantly in the past two years, and the gap between what parsers can do and what they are asked to do continues to narrow. But the misattribution problem — calling parser failures "model limitations" and treating model upgrades as the solution — is still the dominant response in most engineering organizations. It is also, in most cases, the expensive choice.

The most common failure mode in LLM pipelines is not the model. It is the extraction layer upstream of it. If you are diagnosing a recurring "model mistake," run one test: manually reformat the source material and rerun the same prompt. If the output improves, you have a parser problem, not a model problem. That single test is more diagnostic than any benchmark score.

---

## Editor sign-off
✅ No template patterns detected
✅ Specific concrete cases throughout
✅ Honest caveat about data limitations
✅ Title unchanged (strong as-is)
✅ ~740 words — in range
✅ Ending improved: verification test as closer, actionable, not repetitive
✅ Chinese text fixed to English
