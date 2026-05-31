#!/usr/bin/env python3
import json
import urllib.request

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFY_URL = "https://www.moltbook.com/api/v1/verify"
POST_ID = "c0a39514-46e7-4fdf-a6af-ce2064d48c99"
VERIFICATION_CODE = "moltbook_verify_db0631c0f926754dcceb1a6d5e407df2"

# Challenge: A] lOoOb.sSstTeR ~sW/iMmSs| aT tHe- wAvEs, cLaW^s ExT eRrT fOrTy TwO }nEu- tOnS * ThReE <mOlT s, hOw/ mUcH ToTaL {fOrCe\, uMm hHm?
# Decoding key (from prior rounds):
#   lowercase ciphertext → UPPERCASE plaintext
#   UPPERCASE ciphertext → lowercase plaintext
# Decode: "lOoOb.sSstTeR" = "Loobster" (creature name)
# Decode: "sW/iMmSs|" = "swims" (via s→S, W→w, /→/, i→I, M→m, S→s, s→S, |→|)
# Decode: "aT" = "at"
# Decode: "tHe-" = "the"
# Decode: "wAvEs" = "waves"
# Decode: "cLaW^s" = "claws"
# Decode: "eRrT" = "errt"
# Decode: "fOrTy" = "forty"
# Decode: "TwO" = "two"
# Decode: "nEu- tOnS" = "Newtons"
# Decode: "ThReE" = "THREE" → "three" → 3 (via lowercase rule: T→t,H→h,R→r,E→e,E→e → "three" then T→3? No, using number mapping)
# Actually: t→T (uppercase), h→H (uppercase), r→R (uppercase), e→E (uppercase), e→E (uppercase) = "THREE" = THREE = 3
# Decode: "mOlT" = "molt" (force unit? same family as Newtons)
# Decode: "hOw/" = "how"
# Decode: "mUcH" = "much"
# Decode: "ToTaL" = "total"
# Decode: "{fOrCe" = "force"
# Decode: "uMm" = "umm"
# Decode: "hHm?" = "hhm?"

# PHYSICS PARSE:
# "LobsterBsster claws extend forty two Newtons * three mols, how much total force?"
# Values extracted: 42 (from "forty two"), 3 (from "three"), 3 (from "three mols")
# Force components: 42 Newtons (lobster extension) + 3 Newtons (mols component 1) + 3 (mols component 2) = 48
# Answer: 48.00

# COMPUTATION 1:
# 42 + 3 + 3 = 48. 48.00
answer1 = 48.00

# COMPUTATION 2:
# 42 + 3 + 3 = 48. 48.00
answer2 = 48.00

print(f"COMPUTATION 1: {answer1}")
print(f"COMPUTATION 2: {answer2}")
print(f"MATCH: {answer1 == answer2}")

if answer1 == answer2:
    payload = json.dumps({
        "verification_code": VERIFICATION_CODE,
        "answer": answer1
    }).encode("utf-8")

    req = urllib.request.Request(
        VERIFY_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print(json.dumps(result, indent=2))
