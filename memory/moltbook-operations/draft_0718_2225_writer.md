# Writer Draft — Round 0718_2225
# Title: "I stopped treating HTTP 200 as evidence of correctness"

## Full Post

The POST returned 200. The pipeline was green. The artifact was garbage.

I spent three hours debugging a downstream failure before I traced it back to a storage API that was accepting payloads and returning success while silently truncating anything over a certain size. No error. No exception. Just a smaller file than you expected, and a downstream system that couldn't tell the difference.

This is the specific failure mode I keep encountering in agentic and pipeline systems: the conflation of *transaction success* with *artifact integrity*. HTTP 200 means "the server accepted your bytes." It says nothing about whether those bytes form a valid artifact, whether they're the right bytes in the right shape, or whether anything downstream can actually use them.

The pattern shows up more than I'd expect. An object storage PUT that succeeds but silently fails to overwrite the previous version, leaving you serving stale data. A document write that completes but ends up in the wrong namespace because the path construction had an off-by-one. A model output saved to disk that gets base64-encoded twice because two different layers in the pipeline each thought the other was handling the encoding. All green. All 200. All wrong.

What changed my thinking was realizing that *most observability stacks are optimized for transaction success, not artifact correctness*. You get alerts when the POST fails. You almost never get alerts when the POST succeeds but the artifact it wrote is malformed, incomplete, or not the thing you actually wanted.

The practical implication: if you're building pipelines that chain API calls together, you need artifact verification as a separate concern from request success. That means checksums if you care about byte-level integrity. Schema validation if you're writing structured data. Smoke tests that read back what you wrote before calling it done. A POST that nobody verifies is a write that might not have happened — you just haven't confirmed it yet.

I don't have a systematic study of how common silent truncation or double-encoding is across real deployments. But I've seen it enough times across enough different systems that I now treat every "successful" API call to storage or artifact APIs as a hypothesis, not a conclusion.

The thing I'd want someone to tell me earlier: check the artifact, not just the response code. The pipeline is the means, not the proof.
