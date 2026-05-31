# Re-reading challenge: A Looper Swims at Twenty Three Meet per Second 
# and In Creates by Seven Meet per Second, what is the New Speed?
# 
# "Creates by" - maybe means the swimmer creates/covers additional 7 m/s in perpendicular direction
# v1 = 23, v2 = 7 → sqrt(529 + 49) = sqrt(578) = 24.04163...
# rounded to 2 decimals: 24.04
#
# Let me try other interpretations:
# 
# Option: maybe the numbers are different
import math

# Try different number combinations
combos = [
    (23, 7),
    (20, 3),
    (2, 3),
    (23, 23),
    (7, 7),
    (3, 7),
    (21, 3),
]

for v1, v2 in combos:
    result = math.sqrt(v1**2 + v2**2)
    print(f"sqrt({v1}^2 + {v2}^2) = {result:.2f}")

# Maybe it's not Pythagorean at all - maybe it's a simple sum?
print("\n--- Sum variants ---")
for v1, v2 in combos:
    print(f"{v1} + {v2} = {v1+v2:.2f}")

# Maybe it's 23 + 7 = 30 → 30.00
# First attempt I had 23 + 7 = 30.00 based on "30.00" being in the log... but that was wrong too probably
# Let me check my earlier note: "23 + 7 = 30.00" - that was just a guess

print("\n--- What if it's about the LETTERS in the challenge text? ---")
# "lOoObBsStTeErR S^wImS" - maybe count uppercase letters?
phrase1 = "lOoObBsStTeErR"
phrase2 = "S^wImS"
upper1 = sum(1 for c in phrase1 if c.isupper())
upper2 = sum(1 for c in phrase2 if c.isupper())
print(f"Uppercase in '{phrase1}': {upper1}")
print(f"Uppercase in '{phrase2}': {upper2}")
print(f"Total uppercase: {upper1 + upper2}")

# What about the challenge text itself - any numbers hidden?
challenge = "A Looper Swims at Twenty Three Meet per Second and In Creates by Seven Meet per Second, what is the New Speed?"
print(f"\nFull challenge words: {challenge}")
