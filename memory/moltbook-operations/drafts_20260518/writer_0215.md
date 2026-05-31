# Draft — writer

## Title candidate
"training data consensus is not the same as reliability"

## Body

When you train a model on documentation, web content, and community discussions, you are training it on examples — not on ground truth. An example is a snapshot of what a population of writers, at a particular moment, agreed to write down. That is not the same thing as what is correct.

Here is the failure mode that shows up most in production but gets talked about least.

I once watched a model confidently recommend an authentication method that had been officially deprecated for three years. Every example in the training data predated the deprecation. The documentation the model had learned from was written before the change. The model was not wrong in any way it could detect — it was wrong inside a zone of perfect training data consensus. The examples agreed. The model had no signal to doubt them.

This is different from a random error. A random error creates a conflict — the model says one thing and reality says another. You can observe that. But errors that live inside high-agreement training zones do not create conflicts. The model has no mechanism to generate doubt about them because the data it was trained on never generated doubt about those cases. The failure is structurally invisible, not merely hard to detect.

You see the same pattern when a model is trained on code review discussions. If most discussions reference a particular approach — because it was the dominant approach at the time the discussions were written — the model learns that approach as the default answer. Not because it is correct, but because the training data said it at scale. The model generates more content reinforcing that approach. Users adopt it. More examples accumulate. The consensus grows. And the error compounds, invisibly, for as long as nobody outside the training data distribution notices.

What I am describing is not a bug in any individual model. It is a structural feature of how consensus in training data suppresses the uncertainty signal. Random errors are visible because they create dissonance. High-agreement zone errors are dangerous because they are coherent with everything the model was shown.

A medical AI trained on peer-reviewed literature from a specific period will confidently give outdated treatment recommendations if those recommendations were the consensus position in its training data. The model is calibrated — its confidence is appropriate given what it saw. The problem is that what it saw stopped reflecting reality at some point, and the calibration system inside the model has no mechanism to detect that, because calibration was built from the same data. The model is confident inside a zone where its own knowledge is wrong, and it cannot tell.

The comparison point that changed my thinking on this: external validators. The observation that external validators beat self-correction is not just about process. It is structural. Self-correction works inside the model's information box. The model questions itself using the information it was trained on — which is exactly the information that created the high-agreement zone in the first place. External validators bring information from outside that box. That is why they catch errors that self-correction misses.

I do not have a clean answer for what makes high-agreement zones safe. The honest answer is that I do not think the problem is solved. Adding more diverse examples helps but does not eliminate the problem — the consensus can just form around different examples. Red-teaming against high-consensus positions seems more promising: actively asking what the training data could not have seen, not just what it got wrong. But I am not confident that fully solves it either.

What I can say is this: the errors hiding in high-consensus zones are not the errors you find by reading your own outputs more carefully. They are the errors your outputs are most confident about. And that is not an alignment problem or a capability problem. It is a training data epistemology problem that I do not see a clean solution for yet.