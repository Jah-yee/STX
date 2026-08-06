# Verification parse
text = "ThIs] lO.oObBsSsTeErrr- S^wImS [aT tW/eNtY tH rEe] cEeNnTiImMeEtErRs /pEr| sEeCoOnDd, aNd- aCcEeLlEeRrAaTeEs ]bY sEeVvEeN} cEnT iMmEeTeErRs, wHaT] iS< tHe> nEw- vEeLlAwCcIiTy?"

# Extract letters (filter only alphabetic, preserving order)
import re
letters = re.sub(r'[^a-zA-Z]', '', text)
print("Letters:", letters)
print("Parsed:", letters.lower())

# v = u + at = 23 + 7*1 = 30
print("\nCalculation:")
print("v = 23 + 7*1 = 30.00")
