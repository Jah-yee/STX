import requests, json

API_KEY = open('api_key.txt').read().strip()

# Verification challenge: 
# A] LoO b-StErr ClA w] FoR cE^ Is ThI rTy yyy Noo-tOnS um + OtHeR ClAw H aS TwE lV e noo tOns, ToTaL F oR cE?? ]
# 
# "Noo-tOnS" = ninety = 90 (case-mangled)
# "TwE lV e" = twelve = 12 (case-mangled)
# First part: LoO b-StErr ClA w FoR cE^ Is ThI rTy yyy Noo-tOnS
#
# Pattern discovery from prior verifications:
#   tWeNtY ThReE = 23  → T(20)+h(8)+R(18)+E(5) = 51? No.
#   Actually: T+ReE = 20+3 = 23. Uppercase letter positions.
#   FfIiVvEe = 5       → F(6)+R(5)+E(5)? No.
#   Let's try: sum of letter positions / 10? 51/10=5.1 (close)
#   Better: uppercase letters only give the number.
#   "tWeNtY" → T+ReE → T=20, R=18, E=5 → 20+18+5=43... no
#
# Another pattern: count uppercase letters × something?
# "tWeNtY ThReE" has 5 uppercase letters (T,T,H,R,E) and gives 23.
# "FfIiVvEe" has 5 uppercase letters (F,F,V,E,E) and gives 5.
# No.
#
# Another: take letter position of uppercase chars only, divide by something.
# T=20, h=8, R=18, e=5, E=5 → 20+8+18+5+5=56? No.
#
# Another: reading case-mangled words as actual number words:
# "twenty" case-scrambled as tWeNtY → decimal 20
# "three" case-scrambled as ThReE → decimal 3
# "twelve" case-scrambled as TwElVe → decimal 12
#
# So LoO b-StErr ClA w FoR cE^ Is ThI rTy yyy Noo-tOnS = some_number
# Where Noo-tOnS = ninety = 90 (confirmed from case-mangled pattern)
#
# LoO b-StErr = ? If "b" = "b" (b=2), "StErr" = "stErr" → ?
# b-StErr: b + stErr → b(2) + stErr → stErr letters: s,t,E,r,r = 19,20,5,18,18
# Could be 2+? = ?
# 
# Actually, looking at the structure: "yyy Noo-tOnS" = (yyy) + ninety
# "yyy" = 3 y's = maybe 3?
# So LoO b-StErr ClA w FoR cE^ Is ThI rTy = some number ending in 90
# E.g. "xxx ninety" could mean xxx + 90 = some total.
#
# If we remove "yyy Noo-tOnS" (yyy=3, Noo-tOnS=90) we get 93.
# Or "yyy" modifies the preceding "rTy" (irty?) → "irty" could be 90-3=87.
#
# "ThI rTy" = ? "thirty" case-scrambled → 30
# "rTy" = r+T+y = 18+20+25=63? No.
# But "irty" in "ThI rTy" → thirty = 30.
#
# "FoR cE^ Is" = "Forces" = plural of force → ?
#
# OK new approach: the first part "LoO b-StErr ClA w FoR cE^ Is ThI rTy yyy Noo-tOnS"
# can be broken into number words:
# - LoO = "loo" = 100 (British slang)
# - b-StErr = ?
# - ClA w = "claw" = 0?
# - FoR cE^ = "force" = ?
# - Is = "is" 
# - ThI rTy = "thirty" = 30
# - yyy = 3 * y = 3? 
# - Noo-tOnS = "ninety" = 90
#
# LoO(100) + b-StErr + ClA w(0?) + FoR cE^(?) + Is + ThI rTy(30) + yyy(3) + Noo-tOnS(90) = total
# 
# If ClA w = 0 and the unknown parts = -3, then 100 + 30 + 3 + 90 = 223.
# But this is all speculation.
#
# Let me try a simpler approach: the challenge says:
# "[first thing] + [second thing] = total?"
# The second thing "OtHeR ClAw H aS TwE lV e noo tOns" = "other claw has twelve ninety" = 12+90=102? 
# No, "twelve ninety" doesn't make sense as 12+90=102.
# More likely: "TwE lV e noo tOns" = twelve ninety = 12 + 90 = 102
#
# First thing: "LoO b-StErr ClA w FoR cE^ Is ThI rTy yyy Noo-tOnS"
# "ThI rTy yyy Noo-tOnS" = "thirty yyy ninety" = 30 + (yyy) + 90
# "yyy" could be "why" = ? Or just 3 letters y = 3
# If yyy = 3: 30 + 3 + 90 = 123
#
# "LoO b-StErr ClA w FoR cE^ Is" = "loo b-stErr claw w force is" 
# = "loo" = 100, "claw" = 0, "force" = ? 
# LoO(100) + b-StErr(?) + ClA w(0) + FoR cE^(?) + Is + 123 = total
# = 223 + b-StErr + FoR cE^
#
# This is too guessing. Let me try another method:
# The challenge uses the EXACT same encoding as previous successes.
# Previous: "tWeNtY ThReE" = 23 → T(20)+h(8)+R(18)+e(5)+e(5) = 56? No.
# Actually, look at the letter pairs: T-h, R-e, e-e
# T=20, h=8 → 28, R=18, e=5 → 23. Yes! First letter (uppercase) + last letter (lowercase).
# tWeNtY: T(uppercase, pos 20) + Y(uppercase, pos 25)? 
# No: T + Y = 20+25=45. Not 23.
#
# Let's try: uppercase first letter + lowercase last letter of each word, then sum.
# tWeNtY: T(20) + Y(25) = 45. But result is 23.
#
# Another: sum of (uppercase letters positions) for the NUMBER WORD ITSELF, not the scrambled version.
# "twenty" letters: t(20)+w(23)+e(5)+n(14)+t(20)+y(25) = 107. Not 23.
# But "tWeNtY" scrambled gives 23.
#
# Let me compute "tWeNtY ThReE" more carefully:
# tWeNtY = t(20)+W(23)+e(5)+N(14)+t(20)+Y(25) = 107
# ThReE = T(20)+h(8)+R(18)+e(5)+E(5) = 56
# 107+56=163. Not 23.
#
# Hmm. What if we take only the letters that are DIFFERENT case from the original?
# "tWeNtY" vs "TWENTY": the lowercase letters in the scrambled version are the ones that were uppercase in original.
# In "tWeNtY", w and e are lowercase → W(23)+E(5) = 28. Not 23.
#
# What if we use (position of letter in word) as a filter?
# tWeNtY → positions 1,3,5 of the alphabet letters? T(20)+e(5)+t(20)=45. Not 23.
#
# Let's try an extreme simplification: the ANSWER is the sum of the POSITIONS of the 
# FIRST LETTER of each word, divided by something.
# "tWeNtY ThReE" = 2 words. First letters T and T. T=20, T=20. Sum=40. 40/？=23.
# No.
#
# OK here's another observation: "tWeNtY" (20) "ThReE" (3) = 23
# The WORD "twenty" = 20, "three" = 3.
# The scrambled version is just the word spelled with mixed case.
# So "LoO b-StErr" should be readable as a number word.
# "loo" could be "lo" = 50 (Roman L=50, O=0... no)
# "b-sterr" → "bester" → ? "bester" isn't a number.
# "b-sterr" → "buster" → ?
# "b-StErr" → b + stErr = b + 5? No.
# "b" = one = 1. "stErr" could be "star" = ? No.
#
# "LoO" could be "L + OO" = 50 + 111 = 161? No.
# Could "LoO" = "100" in some encoding? L=50, O=0, O=0 → 500? No.
#
# OK what if I just compute the sum of ALL letter positions (a=1, b=2) and then mod by something?
# tWeNtY: t=20, W=23, e=5, N=14, t=20, Y=25 → sum=107 → 107 mod ? = 23?
# 107 - 84 = 23. 84 = 6*14. N=14 (the middle letter).
# ThReE: T=20, h=8, R=18, e=5, E=5 → sum=56 → 56 - 33 = 23. 33 = ?
# 107+56=163. 163/7 = 23.28. Close to 23.
# 163/71 = 2.29. No.
#
# Actually: 20+3=23. The word "twenty" has the letters T,W,E,N,T,Y.
# T+W+E+N+T+Y = 20+23+5+14+20+25 = 107.
# 107/4.65 ≈ 23.
#
# Here's the theory: answer = sum of letter positions for the number word, divided by the number of letters that match case between original and scrambled.
# "twenty" (6 letters) and "tWeNtY" (6 chars): in "tWeNtY", the UPPERCASE letters are T, N, T, Y = positions 20,14,20,25 → sum=79. Not 23.
# LOWERCASE: w, e = 23, 5 → sum=28. Not 23.
# MIXED: T(20)+e(5)+N(14)+t(20) = 59. No.
#
# Let me just try a practical approach: the challenge has TWO clear number words:
# "Noo-tOnS" = ninety = 90
# "TwE lV e" = twelve = 12
# So the second part = 102 (twelve + ninety = 12+90=102)
# 
# The first part: "LoO b-StErr ClA w FoR cE^ Is ThI rTy yyy Noo-tOnS"
# Maybe this is ALSO "something ninety" = X + 90
# And the total = something + 90 + 90 = something + 180
#
# What could "LoO b-StErr ClA w FoR cE^ Is ThI rTy yyy" be as a number?
# "ThI rTy" = thirty = 30
# "yyy" = y*3 = y=25 → 75? Or just 3?
# "yyy" could be "why" = Y(25)+H(8)+Y(25) = 58. No.
# "yyy" = "triple y" = 3*25=75. 
#
# If ThI rTy(30) + yyy(? or 3) + Noo-tOnS(90) = the part after FoR cE^
# And LoO b-StErr ClA w FoR cE^ Is = some phrase before that.
# 
# "Is ThI rTy yyy Noo-tOnS" = "is thirty yyy ninety"
# If yyy=3: "is thirty three ninety" makes no sense.
# If yyy modifies: "irty" = 90-3 = 87? Thirtyy ninety → thirty ninety = 30 + 90 = 120? No.
#
# I'm going to make a decision. I'll try the following reasoning:
# 1. "Noo-tOnS" = ninety = 90
# 2. "TwE lV e" = twelve = 12
# 3. "ThI rTy" = thirty = 30
# 4. "yyy" = 3 (letter y position 25, but let's just treat it as 3)
# 5. So "ThI rTy yyy Noo-tOnS" = 30 + 3 + 90 = 123
#
