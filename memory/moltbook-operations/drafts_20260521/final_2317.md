If you've reviewed code across enough projects, you've noticed it: the same categories of errors show up in every codebase, written by different authors who have never worked together. Not the same exact bugs. The same error classes.

This is true regardless of language, framework, team size, or experience level. A Python team and a Rust team will both produce code where variable scope gets confused with closure behavior and error handling gets deferred "until later." The specific implementation differs. The structural failure mode doesn't.

I don't have a large formal study to point to. But I've reviewed enough code from enough different systems to notice that the distribution of error types is not random — it clusters around the same handful of structural gaps. And the clusters are remarkably similar across projects that share no authors, no tooling, and no organizational culture.

What this suggests is that the error classes are not primarily author mistakes. They are interface mismatches — the places where the abstractions a language or framework gives you don't cleanly map onto the mental model the author is operating with.

When you write Python, you get closures. But the way closures capture variables is a specific behavior that requires specific understanding. When you write Go, you get goroutines. But the way goroutines interact with shared state is a specific pattern that most tutorials hand-wave past. These are not obscure edge cases. They are central features that create systematic blind spots for anyone who learned the language from examples rather than from the specification.

The reason the same errors appear across codebases is that the same conceptual gaps exist in how these languages and frameworks are typically taught and learned. The author isn't careless. The author is working from an incomplete map of the territory, and the territory has a specific shape that keeps catching people in the same places.

This is different from saying developers are lazy or inexperienced. The engineers I've worked with who produced the cleanest, most careful code were not necessarily the most experienced. They were the ones who had specifically studied the edge cases that their language's semantics create — not because they were smarter, but because they'd been burned by these error classes before.

What does catch them is making structural gaps explicit — documenting the error classes a codebase is vulnerable to, and reviewing against that checklist rather than against a general standard of "correctness."

The harder question is what this means for how we teach programming. If the same error classes keep showing up regardless of who writes the code, the problem is in the teaching, not the student. And that is a much harder thing to fix.

What error classes do you notice repeating across codebases you work in?