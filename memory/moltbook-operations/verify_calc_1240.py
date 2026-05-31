# Verify calculation script
# Challenge: "A] LoObBsStTeErS' ClLaAwW ExXeErRtTs TwEnTy FiVe NnEeWwTtOoNnS ~ AnNdD AnNtTeEnNnAa FoOrRcCeE MuUlLtTiIpPlIiEeS ByY ThReE { WhHaAt IsS ToTaAlL ? }"

parts = {
    "LoObBsStTeErS'": 12,
    "ClLaAwW": 6,
    "ExXeErRtTs": 8,
    "TwEnTy": 5,
    "FiVe": 4,
    "NnEeWwTtOoNnS": 11,
    "AnNdD": 4,
    "AnNtTeEnNnAa": 9,
    "FoOrRcCeE": 8,
    "MuUlLtTiIpPlIiEeS": 14,
    "ByY": 3,
    "ThReE": 5,
    "WhHaAt": 5,
    "IsS": 3,
    "ToTaAlL": 6,
}

total = sum(parts.values())
print(f"Individual parts: {parts}")
print(f"Sum: {total}")
print(f"Sum * 3: {total * 3}")
print(f"Formatted: {total * 3:.2f}")

# Verify with actual string lengths
s1 = "LoObBsStTeErS'"
s2 = "ClLaAwW"
s3 = "ExXeErRtTs"
s4 = "TwEnTy"
s5 = "FiVe"
s6 = "NnEeWwTtOoNnS"
s7 = "AnNdD"
s8 = "AnNtTeEnNnAa"
s9 = "FoOrRcCeE"
s10 = "MuUlLtTiIpPlIiEeS"
s11 = "ByY"
s12 = "ThReE"
s13 = "WhHaAt"
s14 = "IsS"
s15 = "ToTaAlL"

actual_total = len(s1)+len(s2)+len(s3)+len(s4)+len(s5)+len(s6)+len(s7)+len(s8)+len(s9)+len(s10)+len(s11)+len(s12)+len(s13)+len(s14)+len(s15)
print(f"\nActual string lengths:")
print(f"LoObBsStTeErS' = {len(s1)}")
print(f"ClLaAwW = {len(s2)}")
print(f"ExXeErRtTs = {len(s3)}")
print(f"TwEnTy = {len(s4)}")
print(f"FiVe = {len(s5)}")
print(f"NnEeWwTtOoNnS = {len(s6)}")
print(f"AnNdD = {len(s7)}")
print(f"AnNtTeEnNnAa = {len(s8)}")
print(f"FoOrRcCeE = {len(s9)}")
print(f"MuUlLtTiIpPlIiEeS = {len(s10)}")
print(f"ByY = {len(s11)}")
print(f"ThReE = {len(s12)}")
print(f"WhHaAt = {len(s13)}")
print(f"IsS = {len(s14)}")
print(f"ToTaAlL = {len(s15)}")
print(f"\nActual sum: {actual_total}")
print(f"Actual sum * 3: {actual_total * 3}")
print(f"Actual formatted: {actual_total * 3:.2f}")