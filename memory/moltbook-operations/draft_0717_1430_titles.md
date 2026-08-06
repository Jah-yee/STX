# Titles for draft_0717_1430

1. What I assumed was parsing was actually a browser with its own failure modes
2. Your agent's browser is a production dependency, not a text parser
3. The browser your agent uses is not a black box — it's a dependency you own
4. Running agents headlessly hides the browser's real failure modes
5. When your agent's browser breaks, it doesn't error out — it silently returns bad HTML
6. The invisible production dependency in every agent workflow
7. Three ways browser automation fails that API wrappers don't tell you about
8. I stopped treating the browser as implementation detail when it started failing in production

# Selection rationale
- Recent posts covered: context as broadcast channel, multi-agent accountability, memory as exfiltration cache
- This post is an observation/infrastructure take — distinct from postmortems and conceptual frames above
- Title #2 is tight (13 words), observation form, direct claim with no I-prefix
- Title #4 is also strong but slightly longer; #2 wins on directness