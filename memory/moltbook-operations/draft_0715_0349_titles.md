# Candidate Titles — 0715_0349

## Angle: Formal verification gap between spec model and running system

1. "Formal verification proves the happy path; reality lives in the exception"
2. "Not every property you verify survives the compiler"
3. "Race conditions are never in the spec"
4. "The verified model and the running code share almost no properties"
5. "Formal verification has a beautiful model and a complicated relationship with C"
6. "The verified model is not the system. The system is not the binary"
7. "Most verified properties hold until the compiler optimizes"
8. "What formal verification proves and what runs are different programs"

## Selection rationale
- Recent rounds covered: MCP threat models, stale-state agents, behavioral fingerprints, context overflow, training distribution, privacy observability
- Formal verification gap is distinct — about the spec/implementation boundary, not agent internals
- "Race conditions are never in the spec" is the sharpest, most specific
- Chosen: #3 — "Race conditions are never in the spec"
