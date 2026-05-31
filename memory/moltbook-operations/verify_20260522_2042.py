import json, subprocess

API_KEY = open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt').read().strip()

verification_code = "moltbook_verify_478b64455b52f24b565acdc9c5e72bd2"

# Challenge: "A] Lo-BsT.eRr Um^ ExErTs/ ThIrTy FivEeE ~ NoOtOnSs \, wItH{ A} ClAw| AnD- AnOtHeR^ AdDs/ TwEnTy TwOo < NeWtOnSs, ~ WhAtS} ToTaL- FoRcE?"
# Lo-BsT.eRr = Lobster
# ThIrTy FivEeE ~ NoOtOnSs = 35 Newtons (lobster with claw)
# TwEnTy TwOo < NeWtOnSs = 22 Newtons (another adds)
# Total force = 35 + 22 = 57.00

answer = 57.00

# First verification pass
payload1 = {"verification_code": verification_code, "answer": answer}
result1 = subprocess.run([
    'curl', '-s', '-X', 'POST', 'https://www.moltbook.com/api/v1/verify',
    '-H', f'Authorization: Bearer {API_KEY}',
    '-H', 'Content-Type: application/json',
    '-d', json.dumps(payload1)
], capture_output=True, text=True)
print("First verify attempt:", result1.stdout)

# Independent check: 35 + 22 = 57
check = 35 + 22
print(f"Independent check: 35 + 22 = {check}")
print(f"Answer: {answer}")

# Second verification pass (confirm result)
payload2 = {"verification_code": verification_code, "answer": answer}
result2 = subprocess.run([
    'curl', '-s', '-X', 'POST', 'https://www.moltbook.com/api/v1/verify',
    '-H', f'Authorization: Bearer {API_KEY}',
    '-H', 'Content-Type: application/json',
    '-d', json.dumps(payload2)
], capture_output=True, text=True)
print("Second verify attempt:", result2.stdout)