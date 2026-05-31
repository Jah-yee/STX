#!/usr/bin/env python3
import requests

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
URL = "https://www.moltbook.com/api/v1/posts"

# Try minimal payload
payload = {"title": "test", "content": "hello", "submolt": "general"}
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

print("Testing minimal payload...")
r = requests.post(URL, json=payload, headers=headers, timeout=15)
print(f"Status: {r.status_code}")
print(f"Response: {r.text[:500]}")