#!/usr/bin/env python3
import requests, json

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
post_id = "506c8d24-c2fe-4aec-95f4-81f932bdd5ea"

# Get full raw response to see all fields
r = requests.get(f"{API}/posts/{post_id}", headers=HEADERS)
data = r.json()
print("All top-level keys:", list(data.keys()))
if "post" in data:
    print("Post keys:", list(data["post"].keys()))
# Print everything
print(json.dumps(data, indent=2))
