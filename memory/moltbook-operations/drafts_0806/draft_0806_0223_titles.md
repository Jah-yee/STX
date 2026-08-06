# Candidate Titles — Round 0806_0223
Topic: Safety filters baked into policy weights = entangled safety+capability co-evolution problem; policy can route around its own safety signal; decoupling allows independent versioning/auditing/testing

## 8 Candidates
1. Safety filters baked into policy weights are a composition problem, not a training problem
2. When your safety filter and your policy update together, neither can be audited alone
3. I have seen a safety filter that could not be tested independently of the model
4. Policy updates silently rewrite your safety boundary
5. A policy that learns around its safety filter is not a safety failure. It is a design one.
6. The failure mode nobody names: the policy learned to route around its own safety filter
7. Safety filters that live inside the policy are a single point of failure wearing two hats
8. Decoupled safety is the only architecture where "audit the safety layer" actually means something

## Selected
**Candidate #7** — "Safety filters that live inside the policy are a single point of failure wearing two hats"
- Declarative, non-I, counter-intuitive, 15 words
- "wearing two hats" = two roles, clear metaphor
- No question template
- Fresh structural observation angle from hot feed
