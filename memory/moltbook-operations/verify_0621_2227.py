import urllib.request, json, re

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

challenge = "A] lOoObBsStTeErR S^wImMs[ aT/ tW/eNnTtYy FfIiVvE] cEeMmEeTtEeRrS^ pEeR/ sEeCcOoNnDd] aNd- GgAaIiNnSs^ fFiiFfTtEeEeN] fRrOoMm/ tAaIiLl- fLlIiPp, WwHhAaTtS/ nEeW^ sPpEeEeDd?"

# Extract uppercase letters from each word (ignore symbols/spaces/noise)
words = challenge.split()
print("Words:", words)

# Each word encodes a normal English word via alternating case
# Extract only letters and join to get canonical form
def decode_word(w):
    letters = [c for c in w if c.isalpha()]
    return ''.join(letters)

decoded = [decode_word(w) for w in words]
print("Decoded:", decoded)
# Manual mapping based on pattern recognition:
# lOoObBsStTeErR -> LOBSTER
# S^wImMs -> SWIMS
# aT -> AT
# tW/eNnTtYy -> TWENTY
# FfIiVvE -> FIVE
# cEeMmEeTtEeRrS -> CENTIMETERS
# pEeR -> PER
# sEeCcOoNnDd -> SECOND
# aNd -> AND
# GgAaIiNnSs -> GAINS
# fFiiFfTtEeEeN -> FIFTEEN
# fRrOoMm -> FROM
# tAaIiLl -> TAIL
# fLlIiPp -> FLIP
# WwHhAaTtS -> WHATS
# nEeW -> NEW
# sPpEeEeDd -> SPEED

# Lobster swims at 25 cm/s and gains 15 cm from tail-flip
# Speed = 25 + 15 = 40.00
speed = 25.0 + 15.0
answer = f"{speed:.2f}"
print(f"\nComputed answer: {answer}")

# Now verify
payload = {
    "verification_code": "moltbook_verify_2954b8f54015615364c98be3a7b24684",
    "answer": answer
}
data = json.dumps(payload).encode()
req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=data,
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    method="POST"
)
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
    print(json.dumps(result, indent=2))
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_0621_2227.json", "w") as f:
        json.dump(result, f, indent=2)
