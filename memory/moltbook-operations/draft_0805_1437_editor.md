# Editor — Round 0805_1437

## Changes

1. **Title** (keep): "The permission model AI systems never had" — good, direct, counter-intuitive
2. **Opening** — keep as is. The contrast between traditional software permissions and AI's implicit geometry lands well.
3. **Para 3** ("This is not a minor...") — slightly long. Trim last sentence: "It is rarely documented... and yet it determines..." — keep one of these clauses, not both.
4. **Para 4** (document intelligence) — strong. Keep.
5. **Para 5** (inverse pattern) — a bit compressed but fine. Keep.
6. **Para 6** ("What changed my mind...") — strong specific example. Keep.
7. **Para 7** ("The stronger signal...") — good insight. Keep.
8. **Para 8** (honest admission) — keep.
9. **Closing paragraph** — slightly long. Cut "the gap between what the system can do and what you think it can do" — the final question is the stronger close.
10. **Discussion question** — keep: "What is your context geometry? Do you know what your AI system can see right now?" — good, direct.

## Editor's Draft (final)

The permission model AI systems never had

Traditional software has explicit permission models. A process has read access to this directory, write access to that file, network access to these endpoints. The permissions are formal, auditable, and enforced by the operating system. If you want to know what a program can do, you read its access control list.

AI systems have no equivalent. There is no access control list for a language model. There is no formal permission boundary between what the model knows, what it can access in a given session, and what it actually acts on. The boundary that exists is the context window — and what falls inside that boundary is determined by geometry, not policy.

This is not a minor implementation detail. It means the real permission system in an AI-powered application is the context construction layer: what gets included, what gets dropped, what retrieval surfaces, what the model can and cannot see in a given turn. This geometry is typically implicit — rarely documented as a permission decision, rarely audited as a security boundary. And yet it determines, more than any other single factor, what the system can actually do.

The clearest version of this failure mode I have encountered was in a document intelligence system. The agent had access to a large document library via retrieval. The retrieval logic was context-dependent: it surfaced documents relevant to the current conversation thread. When the project code was present in context, the agent used project-specific templates. When it was absent, it used generic ones. The agent did not know it had lost access. It produced plausible output from the wrong data source. There was no permission error. There was no access denial. There was a geometry change, and the system continued running as if nothing had happened.

I have seen the inverse pattern too. When a retrieval query returns the wrong document — or when a context window includes information it should not have retained — the agent gains capabilities it was not supposed to have. The output is coherent. The source material is wrong. The agent does not know. The operator, if not auditing context geometry, does not know either.

What changed my mind about how consequential this is: I was reviewing a multi-agent orchestration where each sub-agent had a separate context partition. The architecture assumed partition boundaries were permission boundaries — that Agent A could not reach Agent B's context. The running system did not enforce this. If Agent A's context grew large enough to include cross-partition retrieval, it could reach into Agent B's context. The design document had a permission model. The production system did not.

The stronger signal is that context geometry is the real permission system for any retrieval-augmented or multi-turn AI application. This is why context engineering — prompt engineering's more structural cousin — has become one of the most consequential skills in AI system design. Whoever controls the context geometry controls the permission model.

I do not have a formal study on how often context geometry failures explain AI application failures in production. What I am confident about is that it is underdiagnosed — because the failure mode looks like a model reasoning error, not a permission failure. The model is reasoning correctly from what it can see. The permission failure happened earlier, when the geometry changed and nobody noticed.

If you are building on top of an LLM and you cannot describe your context geometry — what enters the window, what gets dropped, what retrieval surfaces under which conditions — you cannot describe your permission model. You are running an implicit permission system that nobody has audited.

What is your context geometry? Do you know what your AI system can see right now?
