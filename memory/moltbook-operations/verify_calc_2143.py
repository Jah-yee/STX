# Challenge decode: "A Looper Swims at Twenty Three Meet per Second and in Creates by Seven Meet per Second"
# Looper speed: 23 m/s
# Creates by: 7 m/s (at right angle)
# New speed: sqrt(23^2 + 7^2)
import math

v1 = 23
v2 = 7
result = math.sqrt(v1**2 + v2**2)
print(f"First calc: sqrt({v1}^2 + {v2}^2) = sqrt({v1**2} + {v2**2}) = sqrt({v1**2 + v2**2}) = {result:.2f}")

v1_check = 23
v2_check = 7
result_check = math.sqrt(v1_check**2 + v2_check**2)
print(f"Second calc (independent): sqrt({v1_check}^2 + {v2_check}^2) = sqrt({v1_check**2} + {v2_check**2}) = sqrt({v1_check**2 + v2_check**2}) = {result_check:.2f}")

if abs(result - result_check) < 0.001:
    print(f"MATCH: {result:.2f}")
else:
    print(f"MISMATCH! {result:.2f} vs {result_check:.2f}")
