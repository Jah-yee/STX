#!/usr/bin/env python3
import re

def alpha_sum(word):
    return sum(ord(c.upper()) - ord('A') + 1 for c in word if c.isalpha())

# Challenge text
text = "LoOoBbSsTtEr] lO.bS tEr^ ClAw- FoRcE| Is~ TwEnTy SeX {nOoOtOnS} aNd/ iT GaAiInSs- NiNe<, wHaT| iS~ ThE ToTaL FoRcEe?"

# Extract word groups (letters only, preserving case)
parts = re.findall(r'[A-Za-z]+', text)
print("Word groups:", parts)

total = 0
for p in parts:
    s = alpha_sum(p)
    print(f"  {p} = {s}")
    total += s

print(f"\nSum = {total}")
print(f"Formatted: {total:.2f}")

# Also try: LOBSTER group separately
# Group 1: LoOoBbSsTtEr = LOBSTER
g1 = alpha_sum('LoOoBbSsTtEr')
g2 = alpha_sum('lO') + alpha_sum('bS') + alpha_sum('tEr')
g3 = alpha_sum('ClAw')
g4 = alpha_sum('FoRcE')
print(f"\nLOBSTER approach: {g1} + {g2} + {g3} + {g4} = {g1+g2+g3+g4}")

# Also: try the numeric interpretation
# TwEnTy = 20 (first letter T=20)
# SeX = ? (S=19)
# Maybe TwEnTy SeX = 20 + 6 = 26?

# Try just the claw force: LOBSTER + lO.bS.tEr + CLAW + FORCE
# Lo.bS.tEr = Lo + bS + tEr
g2_breakdown = alpha_sum('lO') + alpha_sum('bS') + alpha_sum('tEr')
print(f"lO.bS.tEr breakdown: {alpha_sum('lO')} + {alpha_sum('bS')} + {alpha_sum('tEr')} = {g2_breakdown}")
print(f"Claw force: {g1} + {g2_breakdown} + {g3} + {g4} = {g1+g2_breakdown+g3+g4}")

# The formula seems to ask: "what is the total force?"
# Let's try: 268 (g1+g2_breakdown+g3+g4)

# For the "TwEnTy SeX" part - maybe it's telling us how to combine
# "Twenty six" = 26
# "{nOoOtOnS}" = ? maybe a number like 127
# "aNd/" - maybe AND = add
# "iT" = it (refers back to something)
# "GaAiInSs-" = GAINS = add
# "NiNe<" = NINE, less than something

# Actually I think the formula might be simpler:
# Total = LOBSTER + TWENTY + SIX + NINE = ?
print(f"\nSimple sum: LOBSTER({g1}) + TWENTY({alpha_sum('TwEnTy')}) + SIX({alpha_sum('SeX')}) + NINE({alpha_sum('NiNe')}) = {g1+alpha_sum('TwEnTy')+alpha_sum('SeX')+alpha_sum('NiNe')}")

# And the other words might be noise/red herrings
# 91 + 84 + 48 + 42 = 265