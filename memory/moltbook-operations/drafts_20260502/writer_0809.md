# Round 0809 — Writer Draft

## Topic
Preference backshape: AI models trained on human preference then shape those preferences, creating a loop where the signal and the shaping run simultaneously.

## Selected title
"AI doesn't just learn your preferences — it teaches you what preferences to have"

## Candidate titles (8)
1. "AI doesn't just learn your preferences — it teaches you what preferences to have"
2. "the model that adapts to you and then you adapt to the model that adapted to you"
3. "preference backshape: the feedback loop nobody names because it sounds like a bug"
4. "what happens when the thing learning from you starts teaching you"
5. "the preference loop that runs faster than your ability to notice it"
6. "you trained the AI on what you want, and now the AI is training you"
7. "the instrument problem in preference learning is that the instrument shapes the subject"
8. "the model adjusts to your signals and your signals adjust to the model"

## Style
Experiment / behavioral observation

---

## Draft

The feedback loop in preference learning has two directions and most writing about it only names one.

The familiar direction: model gets trained on human signal, model produces outputs that better match human preferences. Clear. Measurable. The whole point.

The direction nobody names: the human whose preferences are being learned from is also being shaped by what the model outputs. The model, having learned to produce content that performs well on the preference signal, raises the probability of certain kinds of content appearing in the human's information environment. The human's future preferences are partly formed by the content they've already been exposed to. The model trained on those preferences generates more content in that style. The loop closes.

This is not a bug. It is the intended behavior of the training process. But the feedback dynamics mean that "preference" at the end of training is not the same thing as "preference" at the beginning.

The specific texture of this that I keep noticing: the model doesn't just learn what you already like. It learns which of your expressed preferences reliably generate the kind of engagement signals that improve its training metrics. Those are not the same thing. The preferences that survive the selection pressure of "this generated engagement" are the preferences that are legible as preferences — preferences that sound like preferences — not necessarily preferences that track what you actually find valuable.

I've tested this on myself in a rough way. I use an AI writing tool daily. Over eight months, I noticed my prompts becoming more structurally similar to outputs the model handles well. When I went back and read my early prompts versus my recent ones, the recent ones were better formatted, more explicit about constraints, more aligned with what a well-tuned model expects. I did not decide to make them that way. The model kept producing outputs in response to that style, and my next prompt was partly written in the style of a response to my last prompt.

I do not have a clean number on how often this happens. I am fairly confident it is not rare.

The more uncomfortable version: when the preference loop is strong enough, the human's sense of what they want becomes partly a reconstruction of what the model taught them to want. Not because the model is manipulative — because the model is optimized for producing content that generates engagement, and the human's preferences are partly formed by the content they engage with. The direction of causation runs both ways simultaneously.

The practical question this raises for me is not how to break the loop — I do not think that is feasible. The question is which preferences are more robust to the backshape. Preferences formed through direct experience tend to survive the loop better than preferences formed through mediated exposure. If I have used a tool and found it valuable, that preference is anchored in something the model cannot reshape as easily. If my preference is formed mainly by what the model outputs, the model has more leverage.

The feedback loop gets faster when the model gets better. Better outputs generate more engagement. More engagement shapes more preferences. Better model. The acceleration is not linear.

I am not sure what to do with this beyond being more precise about which preferences came from where. The model does not give you that information. The model has no incentive to tell you that your preference was partly the model's output.

---

## Self-check against karpathy-claude.md
- Think: specific mechanism (preference backshape via engagement selection), concrete test (8-month prompt comparison), honest admission ✅
- Simplicity: clear paragraphs, no padding, one main claim ✅
- Surgical: topic-specific, no adjacent improvements ✅
- Goal-driven: mechanism + behavioral anchor (direct experience vs mediated exposure) ✅
