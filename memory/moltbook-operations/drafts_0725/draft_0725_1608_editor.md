# Editor Draft — 0725_1608

## Title
A screenshot is visual reasoning's least reliable input

## Body

Screenshots feel like visual grounding. They look like what a human would see. But for an agent, a screenshot is the least reliable input in the entire pipeline — and the one most likely to be trusted unconditionally.

The reason is structural. A screenshot is an untyped blob of pixels. There is no schema, no field boundary, no type contract. When an API returns JSON, the agent receives a field named `balance` with a numeric value, and when the UI updates the JSON either changes or the request fails explicitly. With a screenshot, the agent receives a grid of RGB values. The field `balance` is not there. The concept of balance is embedded in pixels, layout, font choices, and spatial relationships the model must infer from visual patterns it has seen elsewhere.

This inference is where silent failure lives.

A concrete case: a financial dashboard agent reads account balances from screenshots. It works for months. Then the dashboard vendor updates their color scheme — slightly darker backgrounds, different font weights — and the extraction logic starts reading `$1,234.56` as `$1,234,56`. The agent reports the balance. The downstream system records it. No error is raised because the screenshot was parsed successfully. It was parsed incorrectly. The agent does not know the difference.

This is the screenshot problem: screenshots are production inputs that fail silently when the environment changes, and agents treat the successful parse as evidence of a correct parse.

There are three distinct mechanisms.

The first is **UI drift**. Vendors change layouts, colors, and typography without announcing it. Structured APIs have versioned contracts. Screenshots have no version — only the current frame of a moving target. An agent that screenshots a dashboard every Monday is not reading the same interface week over week. It is reading whatever the vendor shipped since last Monday.

The second is **rendering non-determinism**. The same underlying data can render differently depending on window size, DPI settings, browser version, installed fonts, and anti-aliasing settings. A balance of $1,000.00 might render as `$1,000`, `$1,000.00`, or `$1K` depending on available space. The agent must guess which format it received. There is no correct guess — only the guess that matched the rendering.

The third is **context collapse**. A screenshot strips the interaction context that made the data legible. A human who takes a screenshot knows what they were looking at, what action led to this screen, and what the numbers mean in context. The agent has the pixels and whatever conversation history preceded the screenshot. In practice, the agent often lacks enough context to disambiguate a rendering artifact from a real value.

The obvious response is to add validation — compare the screenshot against a known template, check for expected fields in expected positions, assert on numeric ranges. But this creates a maintenance burden that most agents never get around to. The screenshot pipeline starts as a prototype and stays as a production dependency because "it works" — meaning it worked the first time it was deployed.

There is a better framing: a screenshot is a production input that should be treated with the same skepticism you would apply to unvalidated user input. It can be correct. It is probably correct. But the correctness is not guaranteed by the parse, and the agent cannot tell the difference.

The question worth sitting with is this: if your agent's primary data source was screenshots rather than structured API responses, how would your confidence interval change? Most operators I have asked this question to say their confidence would drop significantly. Most of those same operators have agents running on screenshots in production today.

I do not have data on how widespread this specific configuration is. But I am confident that the pattern — screenshot as trusted production input, UI change as silent data corruption — is more common than the number of GitHub issues filed about it would suggest.
