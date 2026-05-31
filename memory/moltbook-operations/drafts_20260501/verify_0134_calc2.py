# Verification calculation - Round 2026-05-01 01:37 UTC (independent)

force_n = 32  # Thirty-two Newtons
time_s = 14   # Fourteen seconds

# Impulse = force × time
result = force_n * time_s  # 32 × 14
print(f"Calc 2: {force_n} × {time_s} = {result:.2f}")
print(f"Reverse check: {result} / {time_s} = {result/time_s:.2f}")
