#!/usr/bin/env python3
import re

def alpha_sum(word):
    return sum(ord(c.upper()) - ord('A') + 1 for c in word if c.isalpha())

# The challenge asks: what is the total force?
# Parse the first part as describing the LOBSTER-CLAW-FORCE claw force
# LoOoBbSsTtEr = LOBSTER = 91
# lO.bS tEr = lO + bS + tEr = 27 + 21 + 43 = 91
# ClAw = CLAW = 39
# FoRcE = FORCE = 47
# Total claw force = 268.00

# The second part (after "Is~") seems to be a separate equation
# Is~ TwEnTy SeX {nOoOtOnS} aNd/ iT GaAiInSs- NiNe<
# Interpret: TWENTY + SIX + (AND + IT + GAINS + NINE?) - or just the numbers

# Maybe "TwEnTy SeX" means twenty six = 26 (T=20, W=23, E=5, N=14, T=20, Y=25 for TWENTY... no that's too complex)
# Actually "TwEnTy" as word sum = T(20)+w(23)+E(5)+n(14)+T(20)+y(25) = 107
# "SeX" = S(19)+e(5)+X(24) = 48

# But "Twenty six" as digits = 20 + 6 = 26
# If the intended values are: TWENTY=20, SIX=6, NINE=9
# Then the equation: TWENTY + SIX + (something about IT GAINS NINE) = ?
# "iT GaAiInSs-" = IT GAINS = add IT (29)
# "NiNe<" = NINE = 42 or maybe just 9?

# Actually "TwEnTy SeX {nOoOtOnS} aNd/ iT GaAiInSs- NiNe<"
# If we parse operators: ~ = +, / = ?, - = -, < = ?
# Maybe the formula is just asking: what is the total force?
# And the answer is: LOBSTER_CLAW_FORCE = 268

# Alternative reading: the challenge says "LoOoBbSsTtEr] lO.bS tEr^ ClAw- FoRcE| Is~ TwEnTy SeX {nOoOtOnS} aNd/ iT GaAiInSs- NiNe<, wHaT| iS~ ThE ToTaL FoRcEe?"
# The comma separates two clauses:
# 1. "LoOoBbSsTtEr] lO.bS tEr^ ClAw- FoRcE| Is~ TwEnTy SeX {nOoOtOnS} aNd/ iT GaAiInSs- NiNe<" 
#    = "LOBSTER lO.bS tEr CLAW FORCE is twenty six nootoons and it gains nine"
# 2. "wHaT| iS~ ThE ToTaL FoRcEe?"
#    = "What is the total force?"

# If the first clause is describing the force:
# "is twenty six nootoons and it gains nine" = is 26 + 9 = 35?

# But the first part has LOBSTER + lO.bS.tEr + CLAW + FORCE
# Which totals 268

# Maybe the second part is just context: "is 26 nootoons and it gains 9"
# So the answer is 35 (26 + 9)

# Or maybe we add them: 268 + 26 + 9 = 303

# Let me try both
answers = [268.00, 303.00]
for a in answers:
    print(f"{a:.2f}")