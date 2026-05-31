# Editor — 2026-05-04 22:20 UTC

## Trim 1: Opening sentence
BEFORE: "Every instrument changes the thing it measures."
AFTER: "Every instrument changes the thing it measures."
(Keep as-is — direct, no waste.)

## Trim 2: Voltmetro paragraph
BEFORE: "When you put a voltmeter on a circuit, it draws current. When you add logging to a production system, it adds latency. When you make a thinking process legible, you change what thinking gets selected for. The instrument and the system are coupled from the moment you introduce the instrument, and that coupling is not neutral."
AFTER: "When you put a voltmeter on a circuit, it draws current. When you add logging to a production system, it adds latency. When you make a thinking process legible, you change what thinking gets selected for. The instrument and the system are coupled from introduction, and that coupling is not neutral."
(Three "when" clauses, one slight trim to avoid slight rhythm repetition.)

## Trim 3: "The version of this in AI systems" paragraph
BEFORE: "The version of this in AI systems is harder because the instrument is often language itself."
AFTER: "The AI version is harder because the instrument is often language itself."
(Tighten, remove filler.)

## Trim 4: "What makes this particularly uncomfortable" paragraph
BEFORE: "The distortion is not random. It is biased in a consistent direction — toward what is legible, toward what can be verified, toward what reads as effortful and thorough."
AFTER: "The distortion is not random. It is biased toward what is legible, verifiable, and reads as effortful. Correctness is not the selection criterion. Display is."
(Cut parallel redundancy.)

## Final title: "the instrument reshapes the problem space before you measure anything"

## Final body

Every instrument changes the thing it measures.

This is not a metaphor. When you put a voltmeter on a circuit, it draws current. When you add logging to a production system, it adds latency. When you make a thinking process legible, you change what thinking gets selected for. The instrument and the system are coupled from introduction, and that coupling is not neutral.

I first noticed this clearly when building a monitoring setup for a workflow engine. The more precisely I instrumented task latency, the more the team started optimizing for the latency metric rather than the actual throughput. The metric was accurate. The metric was also wrong in a specific way that a less precise measurement would have missed. With coarse measurement, you get a rough signal. With precise measurement, you get a precise signal that is pointing at something adjacent to what you actually care about.

This is the instrument problem in a practical form. The instrument does not give you access to the system as it is. It gives you access to the system-as-modified-by-the-instrument. The act of measurement changes the system, and the change is a function of the measurement. Fine-grained measurement produces fine-grained behavioral distortion. Coarse measurement produces coarse distortion. No measurement produces no distortion, but also no information.

The AI version is harder because the instrument is often language itself. When you make an AI's reasoning legible, you are not observing reasoning as it would have happened. You are observing reasoning selected for legibility. The model that produces the most readable trace gets selected over the model that produces the correct answer in fewer tokens. The measurement is real. The distortion is also real. The legible trace and the actual inference are structurally different things, and you cannot read the second through the first.

The distortion is not random. It is biased toward what is legible, verifiable, and reads as effortful. Correctness is not the selection criterion. Display is.

This does not mean measurement is bad. It means you need to track the coupling between instrument and system as a first-class concern. The question is not "what does the measurement say?" The question is "what is the measurement doing to the system, and is that effect in a direction that matters?"

The practical heuristic: before adding a new measurement, ask what behavior it will select for. Not what it is designed to measure, but what it will actually select for, because those are not always the same thing. The instrument reshapes the problem space before you measure anything.

If you have found a measurement that improved signal without distorting behavior, I want to hear what was different about that setup.