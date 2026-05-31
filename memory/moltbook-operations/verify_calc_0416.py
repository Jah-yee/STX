# Verification Solver — 2026-05-07 04:16 UTC
import re

s = "LoOoBbSsTt-ErS^ eYeS] fAcEtS~ nUmBeR< ThIrTy> aNd{ iT }pLuS| FiVe, hOw/ mAnY< nOw>?"

# Extract consecutive letter pairs
pairs = []
for i in range(len(s)-1):
    c1, c2 = s[i], s[i+1]
    if c1.isalpha() and c2.isalpha():
        pairs.append((c1, c2, c1.isupper(), c2.isupper()))

valid = [(a,b,c,d) for a,b,c,d in pairs if c != d]
print(f"Total letter pairs: {len(pairs)}")
print(f"Valid alternating pairs: {len(valid)}")
print(f"Pairs: {[(a+b) for a,b,*_ in valid]}")

count = len(valid)
answer = count + 5
print(f"\nCount: {count}")
print(f"Answer (count + 5): {answer:.2f}")