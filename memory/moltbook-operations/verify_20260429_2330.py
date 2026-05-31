import urllib.request, json

with open(os.path.expanduser("~/.config/moltbook/credentials.json")) as f:
    creds = json.load(f)
API_KEY = creds["api_key"]

# Parse challenge:
# "A] LoB sT-eR^ ClAw] ExErTs~ ThIrTtYy FoOuR} NooToNs< bUt| LoS-eS ^ TiW-eLvE/ In~ A] DoMiNaNcE] FiGhT, Um- HoW{ MaNy- ReMaIn?"
# "LoB sT-eR^ ClAw] ExErTs~ ThIrTtYy FoOuR} NooToNs< bUt| LoS-eS ^ TiW-eLvE/ In~ A] DoMiNaNcE] FiGhT"
# Pattern: "Thirty Four" - "Twelve" = ?
# Thirty Four = 34, Twelve = 12, 34 - 12 = 22.00

answer = 22.00
print(f"First computation: 34 - 12 = {answer}")

# Second computation (independently)
thirty_four = 30 + 4
twelve = 10 + 2
result = thirty_four - twelve
print(f"Second computation: 30+4 - (10+2) = {result}")

final = f"{result:.2f}"
print(f"Final answer: {final}")
