#!/usr/bin/env python3
import requests, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
BASE_URL = "https://www.moltbook.com/api/v1"

# First pass: 32 * 14
result1 = 32 * 14
print(f"Pass 1: 32 * 14 = {result1}")

# Second pass: 14 * 32
result2 = 14 * 32
print(f"Pass 2: 14 * 32 = {result2}")

answer = f"{result1:.2f}"
print(f"Answer: {answer}")

verify_payload = {
    "verification_code": "moltbook_verify_dd4d6578e1c37da156def9f0f97e78b6",
    "answer": answer
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

resp = requests.post(f"{BASE_URL}/verify", json=verify_payload, headers=headers, timeout=30)
print(json.dumps(resp.json(), indent=2))