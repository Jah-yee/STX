# Writer Draft — 2026-06-07 1122 UTC

## Final Title
The security surface is not in the model. It is in the pipeline.

## Hook (first 3 sentences)
Vision-language action models learn behaviors through fine-tuning runs that never appear in a safety eval. The standard evaluation suite checks whether the model generates harmful content when prompted directly. It does not check whether the model learned to generate that same content when fine-tuned on data that passed the safety filter at collection time. This gap is not a gap in the evaluation. It is a gap in how we think about the attack surface.

## Full Draft

Vision-language action models learn behaviors through fine-tuning runs that never appear in a safety eval. The standard evaluation suite checks whether the model generates harmful content when prompted directly. It does not check whether the model learned to generate that same content when fine-tuned on data that passed the safety filter at collection time. This gap is not a gap in the evaluation. It is a gap in how we think about the attack surface.

The mechanism is straightforward. VLA fine-tuning ingests video demonstrations. Those demonstrations are filtered through a content policy at the time they are collected. A human reviewer sees a frame, approves it, and the frame enters the training set. But the fine-tuning run is not evaluated for content policy compliance the same way the final model is. The pipeline is assumed to be a delivery mechanism, not an attack surface. That assumption is where the problem lives.

What changes in a VLA fine-tuning run is the action policy's conditional structure. The model does not just learn what actions to take in response to visual inputs. It learns which visual configurations should activate which action priors. An attacker who can influence the composition of a training batch can plant visual triggers that shift those priors in a target direction, without those triggers appearing in any text prompt the model has ever seen. This is the visual analog of a prompt injection, except it lives in the weight space, not the context window. And it survives the fine-tuning run. The safety evaluation at inference time cannot catch it because the evaluation was designed for a different attack surface.

There is a structural reason this is hard to catch in practice. The activation of a visual backdoor requires a trigger that the evaluator does not know to look for. You cannot test for a backdoor you have not described. And because VLAs are increasingly fine-tuned post-deployment by customers and third parties, the organization that built the base model has no visibility into what the fine-tuning run introduced. The security boundary sits at the model weights, but the attack happened in the pipeline that produced those weights.

This is not hypothetical. Visual backdoors in fine-tuned vision models have been documented in the academic literature. The more specific and operationally relevant observation is that the VLA fine-tuning pipeline as it is commonly implemented has no equivalent of the safety eval that the final model goes through. There is no automated check that asks: does this batch of fine-tuning data contain visual configurations that would cause the resulting model to behave differently than the base model in a way that violates the content policy? That check does not exist in most pipelines, and where it is being discussed, it is treated as a future roadmap item, not an immediate requirement.

The harder question is whether this can be fixed without breaking what makes fine-tuning useful. The answer is almost certainly yes, but the fix is not a better eval. It is a different pipeline architecture. If the fine-tuning run is a point of no return in the weight space, then the safety boundary needs to live somewhere upstream of that. The model needs to be able to detect and reject visual configurations that activate unsafe action priors, even if those priors were learned during fine-tuning. That requires a different kind of monitoring, one that runs at inference time and inspects the relationship between the visual input and the action output, not just the text prompt.

The practical implication for teams deploying VLAs is concrete: the question you should be asking is not whether your base model passed safety eval. It is whether your fine-tuning pipeline introduced behavior that the eval was never designed to catch. The answer to that question determines whether the VLA you deployed is the VLA you think you deployed.

## Word count
~680 words