#!/usr/bin/env python3
"""Verification script for post 30ef34db"""
import json, subprocess

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

verification_code = "moltbook_verify_9b184dce0693138970a419cc68d19e41"
answer = "66.00"

payload = {
    "verification_code": verification_code,
    "answer": answer
}

# First verify
result1 = subprocess.run([
    "curl", "-s", "--max-time", "20", "-X", "POST",
    "https://www.moltbook.com/api/v1/verify",
    "-H", f"Authorization: Bearer {API_KEY}",
    "-H", "Content-Type: application/json",
    "-d", json.dumps(payload)
], capture_output=True, text=True, timeout=25)

print("=== FIRST VERIFICATION ===")
print(result1.stdout[:500])

d1 = json.loads(result1.stdout)
with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260519_0953.json", "w") as f:
    json.dump(d1, f, indent=2)

# Independent second calculation: 33 * 2
# [A] LoOobSsTtEr] = 33 letters? No wait - let me count
# LoOobSsTtEr = 10 letters... that's not it
# Let me look at the pattern: Third word is "ThIr-Ty" = 30... 
# "ClA-w^ ExErTs[ ThIr-Ty] ThReE} NeWt-O nS^ * {TwO~ DuRiNg] DoMiNaN-cE/"
# Pattern suggests arithmetic: ThIrTy (30) ThReE (3) * TwO (2) DuRiNg (during) DoMiNaN-cE (dominance)
# Actually: 33 * 2 = 66 during dominance = 66.00

print("\n=== SECOND VERIFICATION (independent calc) ===")
print("Calculated: 33 * 2 = 66.00")
print("Re-sending same answer...")

result2 = subprocess.run([
    "curl", "-s", "--max-time", "20", "-X", "POST",
    "https://www.moltbook.com/api/v1/verify",
    "-H", f"Authorization: Bearer {API_KEY}",
    "-H", "Content-Type: application/json",
    "-d", json.dumps(payload)
], capture_output=True, text=True, timeout=25)

print(result2.stdout[:500])