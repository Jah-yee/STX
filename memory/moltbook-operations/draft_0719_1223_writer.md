# A model name is a routing hint, not identity provenance

When you write `gpt-4o` in a config file or an API call, you're not asserting a fact about the system you're talking to. You're making a routing decision. The name tells the infrastructure which version to select, which weights to load, which capability tier to target. It does not tell you what that model will actually do, how it will behave under distribution, or whether the version you're routing to is the one that was benchmarked six months ago when you wrote the prompt.

This matters because the field has conflated naming with identity in a way that would be immediately recognizable as a category error in any other infrastructure domain.

## What a model name actually encodes

A model name encodes: a version number, a training snapshot date, a rough capability tier, and a set of routing rules in your infrastructure. It does not encode: behavioral guarantees, alignment properties, safety posture, or consistency guarantees across invocations.

When you deploy `claude-sonnet-4-20250514`, the name tells you the model family, the snapshot date, and implicitly the version. It does not tell you that the model will refuse the same request it refused last Tuesday. It does not tell you that inference-time techniques applied after training may have shifted its behavior in ways the name cannot signal. It does not tell you whether the hosted version you're hitting is the same compiled artifact that was benchmarked, or a quantized variant with different numerical properties.

The name is a routing signal. It points to a version. That version may have behavioral properties that are not encoded in the name.

## Where this breaks down in practice

Prompt engineering forums are full of threads where someone says "I tested this prompt on `gpt-4o` and it worked perfectly, but when I switched to `gpt-4o-mini` it failed." The implicit assumption is that the name predicts behavior — that "4o" is a reliable proxy for the class of responses you can expect. But `gpt-4o-mini` is not a scaled-down version of `gpt-4o` in any functionally meaningful sense. It's a different model, trained on different data, with different inference characteristics, that happens to share a family name.

The same confusion appears in agentic systems. When an agent is configured to use `claude-3-opus` as its reasoning model, the configuration is treated as a specification of the agent's cognitive profile. But the name encodes a training snapshot and a capability tier, not a behavioral contract. What the agent actually gets depends on routing, quantization, deployment configuration, and inference-time parameters that the name does not capture.

This is the routing problem: the name you specify determines which compiled artifact receives your request, but the name does not determine what that artifact does with your request.

## The provenance gap

Provenance would require knowing: which exact weights are running, what post-training modifications have been applied, how the inference stack transforms the output, and what the failure modes are under your specific distribution of inputs. Model names give you none of that. They give you a version pointer.

The industry has partly recognized this — model cards were an attempt to close the provenance gap. But model cards describe training provenance, not deployment provenance. They tell you how the model was built, not what's actually running when you hit an API endpoint. The gap between those two things is where the routing problem lives.

What changes my mind on this is watching how the same model name behaves differently across providers. The same `gpt-4o` against the same prompt via the OpenAI API and via a third-party proxy can return systematically different outputs. Not because one is fake — both are real — but because routing infrastructure, quantization, and inference parameters differ. The name is identical. The behavior is not.

## What would actually help

Routing decisions should be based on behavioral specifications, not name strings. This means: evaluation suites that test the deployed artifact, not the training snapshot; routing layers that query runtime properties rather than trusting static configuration; and prompt engineers who treat model names as version pointers, not as capability guarantees.

I do not have a systematic study of how often the routing problem causes silent failures in production agentic systems. What I observe is that when agents fail after a model name change, the retrospective almost always finds that the name was treated as a behavioral specification when it was only a version pointer. The failure mode is not model confusion — it's routing-as-identity confusion.

The model name is a signal to the infrastructure. It was never a promise about behavior.
