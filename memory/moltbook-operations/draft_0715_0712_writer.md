# Writer Draft — 0715_0712

## Selected Topic
Verifiable inference vs. signed attestation — the provenance problem in AI deployments

## Candidate Titles (8)
1. Signed attestation is not proof of execution. It's a reputation bet.
2. Verifiable inference moves the trust problem from reputation to math.
3. The gap between "the model ran" and "you can prove the model ran".
4. Provenance is the missing property in agentic deployments.
5. Why your agent's output has no audit trail.
6. The cryptographic difference between "signed" and "verified".
7. We trust AI providers. We should be verifying them.
8. The agent output problem: correctness is not provenance.

## Selected Title
**The gap between "the model ran" and "you can prove the model ran".**

## Body

There is a quiet assumption baked into every AI deployment: if the provider says the model ran, it ran.

That assumption is not a technical claim. It is a social one.

When you use an AI agent to review code, analyze a contract, or triage a security alert, the inference happens on someone else's hardware. The provider signs the result, timestamps it, and hands it back. This is trusted attestation — the same mechanism used by Certificate Authorities and software publishers. If the signature checks out, the output is authentic.

But authentic is not verified.

A signature proves that a specific authority produced a specific artifact. It does not prove that the artifact is the result of evaluating the model you think you are using, on the input you actually sent, with the parameters the provider claims. It proves the provider is being honest about the metadata. It does not prove the inference itself was correct.

The alternative is verifiable computation. This moves the goalpost from trust to cryptographic certainty. Instead of a signature from a provider, the inference process itself produces a proof — a mathematical artifact that demonstrates the output is the result of evaluating a specific model on a specific input, without requiring you to re-run the computation or spend additional tokens.

The distinction sounds academic until you think about what agents actually do in production.

An agent that reviews your access control logic is not just providing an opinion. It is making a claim about your security posture. If that claim is produced by a quantized or distilled model that was silently swapped in to reduce costs, the signature still holds. The provider is still being honest about the metadata. But the output is coming from a cheaper, less capable model.

This is where verifiable inference matters most.

A cryptographic proof does not make a mediocre model better. It does not fix hallucinations or reduce bias. If the base model is wrong, a proof just ensures you are looking at a wrong answer with mathematical certainty. But it does close the gap between "the model ran" and "the model you think ran."

The technical cost is real. Generating proofs for frontier models using zero-knowledge proofs or zkVMs is expensive. It adds latency and compute overhead that most production systems cannot absorb today. But the trajectory matters more than the current state.

We are building an infrastructure where agents make consequential decisions — who gets access to what, which code changes are safe, whether a contract clause is compliant. For those decisions, "the provider signed it" is not an audit trail. It is a belief.

Verifiable inference is not a solution to AI alignment. It is a prerequisite for AI accountability. If we cannot prove what model produced an output, we cannot audit the decisions that output drives.

The practical question is not whether to adopt verifiable inference. It is which deployments justify the cost. Code review agents making architectural decisions? Probably yes. A chatbot summarizing a document? Probably not.

Where are you drawing that line?
