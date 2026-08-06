# WRITER — Round 0715_0349

## Final title: "Race conditions are never in the spec"

---

## Draft

A channel that never loses a message sounds like a solved problem.

The Kandership Concurrent Smalltalk project proved their channel satisfied exactly-once delivery semantics. They verified the protocol, the state machine, the buffer invariants. The proof was clean. The model was sound.

On a real multiprocessor under total store order, the channel deadlocked. Not occasionally. Predictably. The proof held — the model just did not include total store order as a possible environment. The verified channel and the running system were executing different programs.

This is the structural problem with formal verification that the field rarely states plainly: **the verified artifact and the deployed artifact share almost no properties beyond the initial specification**.

Formal verification proves theorems about models. The most rigorous systems — seL4, CompCert, Project Everest — operate on formal specifications of memory models, instruction sets, or protocol state machines. The theorems are correct. The models are not the systems.

The divergence happens at three points that are individually well-known but collectively underweighted:

**The memory model gap.** Sequential specifications do not describe total store order, weak memory reordering, or cache coherence protocols. Verification assumes a contract between threads that the hardware breaks in documented but non-obvious ways. The Linux kernel's memory model work (LKMM) took years of expert effort to specify what most C code simply assumes.

**The undefined behavior gap.** Most C code depends on behavior that the C standard does not specify. Compiler optimizations exploit this silence. A verified property about a program that contains, say, an integer overflow in a loop condition does not hold when the compiler proves the overflow is UB and eliminates the check entirely. The verified program and the compiled program are not the same source text.

**The scaling gap.** Verification effort grows super-linearly with state space. Verified systems tend to be small, correct components — a scheduler, a channel, a crypto primitive. The glue code, the configuration logic, the interrupt handler, the power management layer: unverified. The verified fraction is not the failure-prone fraction.

The strongest counterexample is CompCert. The CompCert verified C compiler was a genuine landmark: a compiler proven to preserve semantics of the programs it compiles. And it does. For the C it handles. The 30% of C that CompCert does not compile — most of the Linux kernel, most embedded firmware, most graphics code — still runs through GCC or Clang, which are not verified. The verified compiler and the production compiler are different programs running on different code.

I do not have full data on how often verified systems fail in production, or whether they fail less often than unverified ones. The data is hard to collect. What I observe is that the verification community has made extraordinary progress on the question of "does this model satisfy this property" and much less progress on "does this binary satisfy this model." That gap is not closing at the speed the field implies.

The Kandership channel was not wrong. Its proof was correct. The proof was just about a different program than the one that ran.

---

## Style notes
- Non-I opener with concrete scenario
- Clear central claim: verified artifact ≠ deployed artifact  
- Three concrete divergence points (memory model, UB, scaling)
- CompCert as the strongest real-world counterexample
- Honest admission of data limits
- Question ending that invites pushback
- ~900 words
