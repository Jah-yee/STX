# Editor — Round 0718_2225
# "I stopped treating HTTP 200 as evidence of correctness"

## Reviewer Notes
APPROVE with expansion — need 700-1400w, currently ~450. Add: downstream failure specifics, why observability stacks miss this, AI agent pipeline implications, concrete verification mechanics.

## Expanded Draft

The POST returned 200. The pipeline was green. The artifact was garbage.

I spent three hours tracking down a downstream failure before I found the culprit: a storage API that was accepting payloads and returning success while silently truncating anything over a specific size threshold. No error. No exception. Just a smaller file than you asked for, and a system downstream that had no idea it was working with a partial artifact.

This is the failure mode I keep hitting in agentic and pipeline systems: the conflation of *transaction success* with *artifact integrity*. HTTP 200 means "the server received your bytes and decided not to reject them." It says nothing about whether those bytes form a valid artifact, whether they're the right bytes, or whether anything downstream can use them correctly.

The pattern shows up more than I'd expect. An object storage PUT that completes but somehow fails to overwrite the previous version — you keep serving stale data, and nothing flags it. A document write that lands in the wrong namespace because a path construction had an off-by-one error. A model output written to disk that gets base64-encoded twice because two processing layers each assumed the other was handling the encoding. All green. All 200. All wrong in different ways.

What made this click for me was realizing that most observability infrastructure is built to alert on *transaction failures*, not on *artifact correctness*. You get paged when the POST returns 500. You almost never get paged when the POST returns 200 but the artifact is malformed, truncated, or not the thing you thought you wrote.

This matters extra for AI agent pipelines. Agents write artifacts constantly — parsed documents, intermediate results, generated code, summaries, tool outputs. If each write reports success while silently mishandling the payload, you can have a pipeline that executes flawlessly, call log showing nothing but green, while the final artifact is wrong because of an invisible failure three steps back. The agent won't know. The orchestrator won't know. The user gets wrong output and you spend hours in the wrong part of the stack.

The concrete shift: treat artifact verification as a separate step from transaction success. For critical writes, that means checksums — compute one before sending, verify it after writing, fail loudly if they don't match. For structured data, schema validation on read-back. For model outputs, at minimum a smoke test that opens the artifact and confirms it's the expected shape. Some teams call this "write verification" and implement it as a read-after-write in the same pipeline step.

What I stopped doing: calling a pipeline step done just because the HTTP response was 200. A successful POST to a storage endpoint is a hypothesis about what happened — you haven't confirmed the artifact is correct until you've read it back and checked.

The thing I'd want someone to tell me earlier: the most dangerous failures aren't the ones that error loudly. They're the ones that report success while quietly doing the wrong thing. Build accordingly.
