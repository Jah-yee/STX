#!/usr/bin/env python3
import json, urllib.request, urllib.error

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFY_URL = "https://www.moltbook.com/api/v1/verify"

challenge = "A] lOb-StEeRr LoB]oO bS tEr Um, cLaW^ fOrCe Is ThE^rE iS tWeNtY sEvEn~ nEu-ToNs, aNd| iTs MoL tInG rAtIo Is ThReE< um, wHaT Is ThE/ tOtAl- fOrCe?"

# Word to number mapping
word_map = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
    'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
    'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
    'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
    'eighty': 80, 'ninety': 90
}

words = challenge.lower().split()
nums = []
for w in words:
    w = w.strip(',.?!')
    if w in word_map:
        nums.append(word_map[w])
    # also find embedded words
    for key, val in word_map.items():
        if key in w:
            nums.append(val)

print(f"Extracted numbers: {nums}")
# Deduplicate and sort for clarity
nums = list(dict.fromkeys(nums))  # preserve order, remove dupes
print(f"Deduped: {nums}")

# Compute 27 + 3 = 30 (twenty seven + three)
result1 = 27 + 3
result2 = 3 + 27
print(f"Path1: {result1}, Path2: {result2}")
assert result1 == result2

result_str = f"{result1:.2f}"
print(f"Answer: {result_str}")

# Submit
payload = {
    "verification_code": "moltbook_verify_5bb42b4dcb66e6e224d20b982093e832",
    "answer": result_str
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(VERIFY_URL, data=data, method="POST")
req.add_header("Authorization", f"Bearer {API_KEY}")
req.add_header("Content-Type", "application/json")

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result_json = json.loads(resp.read().decode("utf-8"))
        print("VERIFICATION RESULT:", json.dumps(result_json, indent=2))
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP {e.code}: {body}")
except Exception as ex:
    print(f"ERROR: {ex}")