#!/usr/bin/env python3
def decode(token):
    total = 0
    for c in token:
        if c.islower():
            total += ord(c) - ord('a')
        elif c.isupper():
            total += ord(c) - ord('A') + 1
    return total

# Parse challenge tokens
tokens = ['lO', 'oBbS', 'tErR', 'lOoobssstErr', 'ClAw',
          'fO^rCe', 'Is', 'tHiR', 'tY', 'fI', 'vE',
          'nEu-TonSs', 'tWeN', 'tY', 'tWo', 'nEu-TonSs']

for t in tokens:
    clean = t.replace('-','')
    val = decode(clean)
    print(f"{t:20s} -> {clean:20s} = {val}")

print("\n--- Sum by section ---")
claw = sum(decode(t.replace('-','')) for t in ['lO','oBbS','tErR','lOoobssstErr','ClAw'])
print(f"ClAw sum: {claw}")

force1 = sum(decode(t.replace('-','')) for t in ['fO^rCe','Is','tHiR','tY','fI','vE'])
print(f"Force1 sum: {force1}")

neutons1 = decode('nEu-TonSs')
neutons2 = sum(decode(t) for t in ['tWeN','tY','tWo','nEu-TonSs'])
neutons3 = decode('nEu-TonSs')

total = claw + force1 + neutons1 + neutons2 + neutons3
print(f"\nTOTAL: {total:.2f}")