# Challenge: "A] LoObBsStTeErS' ClLaAwW ExXeErRtTs TwEnTy FiVe NnEeWwTtOoNnS ~ AnNdD AnNtTeEnNnAa FoOrRcCeE MuUlLtTiIpPlIiEeS ByY ThReE { WhHaAt IsS ToTaAlL ? }"

s = "A] LoObBsStTeErS' ClLaAwW ExXeErRtTs TwEnTy FiVe NnEeWwTtOoNnS ~ AnNdD AnNtTeEnNnAa FoOrRcCeE MuUlLtTiIpPlIiEeS ByY ThReE { WhHaAt IsS ToTaAlL ? }"

# Method 1: sum of word lengths
words = s.split()
sum_words = sum(len(w) for w in words)
print(f"Sum of word lengths: {sum_words}")
print(f"Words: {words}")
print(f"Each: {[len(w) for w in words]}")
print(f"Sum*3 = {sum_words*3}")

# Method 2: strip the leading "A] " prefix and process just the word string
core = s[3:].strip()
print(f"\nCore: {core}")
core_words = core.split()
print(f"Core word count: {sum(len(w) for w in core_words)}")
print(f"Core words: {core_words}")
print(f"Core each: {[len(w) for w in core_words]}")

# Method 3: try ignoring non-letter chars
import re
letters_only = re.sub(r'[^a-zA-Z]', '', s)
print(f"\nLetters only length: {len(letters_only)}")
print(f"Letters: {letters_only}")
print(f"Letters*3 = {len(letters_only)*3}")