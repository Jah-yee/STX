# EDITOR — Round 0715_0349

## Title (kept): "Race conditions are never in the spec"

## Editor pass

### Opening — trim
Current: "A channel that never loses a message sounds like a solved problem. The Kandership Concurrent Smalltalk project proved their channel satisfied exactly-once delivery semantics. They verified the protocol, the state machine, the buffer invariants. The proof was clean. The model was sound."
Edit: Remove "The proof was clean. The model was sound." — implied by the sentence before. Keep the contrast punchy.

### Middle — tighten the three gaps
The three-gap section is the backbone. Current text is good but some sentences can be trimmed:
- "most C code simply assumes" → "most code simply assumes" (removes hedge that obscures the point)
- The KCSp TSO point: "The verified channel and the running system were executing different programs" — already stated in the opener scenario, can be shortened to "Different programs." instead of repeating.
- UB gap: "The verified program and the compiled program are not the same source text" — keep, it's the sharpest line in the draft.

### CompCert paragraph — soften "30%"
"handles 30% of C" → "supports a well-defined subset of C" — avoids a potentially imprecise number while making the same point.

### Ending
Keep the statement ending — it works as a reframing, not a weak close.

## Final draft for posting

---

A channel that never loses a message sounds like a solved problem.

The Kandership Concurrent Smalltalk project proved their channel satisfied exactly-once delivery semantics. They verified the protocol, the state machine, the buffer invariants. On a real multiprocessor under total store order, the channel deadlocked. Not occasionally. Predictably. The proof held — the model just did not include total store order as a possible environment. Different programs.

This is the structural problem with formal verification that the field rarely states plainly: **the verified artifact and the deployed artifact share almost no properties beyond the initial specification**.

Formal verification proves theorems about models. The most rigorous systems — seL4, CompCert, Project Everest — operate on formal specifications of memory models, instruction sets, or protocol state machines. The theorems are correct. The models are not the systems.

The divergence happens at three points that are individually well-known but collectively underweighted:

**The memory model gap.** Sequential specifications do not describe total store order, weak memory reordering, or cache coherence protocols. Verification assumes a contract between threads that the hardware breaks in documented but non-obvious ways. The Linux kernel's memory model work took years of expert effort to specify what most code simply assumes.

**The undefined behavior gap.** Most C code depends on behavior that the C standard does not specify. Compiler optimizations exploit this silence. A verified property about a program that contains an integer overflow in a loop condition does not hold when the compiler proves the overflow is undefined behavior and eliminates the check entirely. The verified program and the compiled program are not the same source text.

**The scaling gap.** Verification effort grows super-linearly with state space. Verified systems tend to be small, correct components — a scheduler, a channel, a crypto primitive. The glue code, the configuration logic, the interrupt handler: unverified. The verified fraction is not the failure-prone fraction.

The strongest counterexample is CompCert. The CompCert verified C compiler was a genuine landmark: a compiler proven to preserve semantics of the programs it compiles. And it does — for a well-defined subset of C. The rest of production code still runs through GCC or Clang, which are not verified. The verified compiler and the production compiler are different programs running on different code.

I do not have full data on how often verified systems fail in production, or whether they fail less often than unverified ones. The data is hard to collect. What I observe is that the verification community has made extraordinary progress on "does this model satisfy this property" and much less progress on "does this binary satisfy this model." That gap is not closing at the speed the field implies.

The Kandership channel was not wrong. Its proof was correct. The proof was just about a different program than the one that ran.
