import math

# Challenge: Looper Swims at Twenty Three meters per Second, and Its Claw Exerts Five Newtons, what is the Product?
# Velocity = 23 m/s
# Force = 5 Newtons
# Product = 23 * 5

v = 23
f = 5
result1 = v * f
print(f"First calc: {v} * {f} = {result1:.2f}")

# Re-check independently
v2 = 23
f2 = 5
result2 = v2 * f2
print(f"Second calc: {v2} * {f2} = {result2:.2f}")

if result1 == result2:
    print(f"MATCH: {result1:.2f}")
else:
    print(f"MISMATCH!")
