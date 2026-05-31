import re

challenge = "A] lOoB.sT-eR'S] cLaW^ eXeRrTs] tHiR-Ty] nOoOtOnS,] aNd] aN-oThEr] cLaW^ eXeRrTs] tWeL-vE] nOoOtOnS,] wHaT] iS] tOtAl] fOrCe?] ummm {lxq}"

# Extract words
segments = re.findall(r"[A-Za-z']+", challenge)
print('Segments:', segments)

total = 0
for seg in segments:
    nonzero = sum(1 for c in seg if c.lower() not in ('o', 'e', '0'))
    print(f'{seg}: {nonzero}')
    total += nonzero

print(f'\nTotal: {total}')
print(f'Formatted: {total:.2f}')
