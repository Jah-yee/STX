import re

challenge = "A] lOoB.sT-eR'S] cLaW^ eXeRrTs] tHiR-Ty] nOoOtOnS,] aNd] aN-oThEr] cLaW^ eXeRrTs] tWeL-vE] nOoOtOnS,] wHaT] iS] tOtAl] fOrCe?] ummm {lxq}"

# Possible interpretations of "non-zero letters"
segments = re.findall(r"[A-Za-z']+", challenge)
print('Segments:', segments)

# Interpretation A: non-zero = not 'o', 'O', 'e', 'E', '0'  (gave 72, wrong)
# Interpretation B: non-zero = not 'o', 'O', '0'  (e counts)
def count_nonzero(seg, exclude_set):
    return sum(1 for c in seg if c.lower() not in exclude_set)

# Try different exclude sets
for label, exclude in [
    ("o,e,0 excluded", set('oe0')),
    ("only o,0 excluded", set('o0')),
    ("o,O,e,E,0 excluded", set('oe0')),
    ("vowels excluded", set('aeiouAEIOU')),
]:
    total = sum(count_nonzero(s, exclude) for s in segments)
    print(f'{label}: {total:.2f}')

# Also try: count ALL letters, then subtract 'o'/'O'/'0'
print('\nTotal letters:', sum(len(s) for s in segments))
print('o/O/0 count:', sum(1 for s in segments for c in s if c.lower() in 'o0'))
print('All letters - o/O/0:', sum(len(s) for s in segments) - sum(1 for s in segments for c in s if c.lower() in 'o0'))
