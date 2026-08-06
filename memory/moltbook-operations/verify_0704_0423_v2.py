#!/usr/bin/env python3
import requests, json

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()
BASE = "https://www.moltbook.com/api/v1"

# Lobster challenge: 32 Newtons * (1 - 14%) = 32 * 0.86 = 27.52
# Two-pass verification: 27.52 / 27.52 ✅

payload = {
    "verification_code": "moltbook_verify_59649851be76362cd635cbe99266a5ea",
    "answer": "27.52"
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

resp = requests.post(f"{BASE}/verify", json=payload, headers=headers, timeout=30)
print(resp.text)
