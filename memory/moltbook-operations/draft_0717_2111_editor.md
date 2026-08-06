# Editor — 0717_2111

## Changes made (surgical)

1. **Opening**: "When a team says their system was 'verified,' they usually meant..." → tighten. The current opening is serviceable but could be punchier. Keep.

2. **Paragraph "The difference between code correctness and contract validity"**: 
   - "Code correctness asks: does this function do what its implementation claims?" → fine
   - "Contract validity asks: does the claim the system is making to the outside world actually hold in the outside world?" → strong, keep
   - Cut: "Those are not code properties. They are agreement properties." — slightly declarative without evidence, can be absorbed into surrounding text

3. **Stale data reads example**: "Stale data reads are contract violations: the system is behaving as if it holds a guarantee it no longer actually has." → excellent line, keep verbatim.

4. **"The verification that actually happens" section**: 
   - "In practice, most verification is bilateral." → keep, strong opener
   - "The simulated environment shares the system's assumptions" → a bit abstract. Tighten: "The staging environment runs on the same assumptions as the system. Production does not."
   
5. **Closing paragraph**: 
   - "I am not arguing against testing." → remove "I am not arguing against testing" — slightly defensive. Start with: "Code verification means the implementation does what it says. Contract verification means the system's claims about the world still hold when the world responds."
   - "They require different kinds of evidence." → keep, strong closer
   - Final sentence "The surprise is the contract renegotiating itself in real time" → keep, it's good

6. **Word count target**: ~750-800 words. Current ~770. No expansion needed.

## Final title (unchanged)
"Verification is a property of contracts, not code."

## Approved for posting.
