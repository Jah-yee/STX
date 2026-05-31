import re

txt = "A] lOoObS-tErR'S ClAaW] eX^eRts/ tW/eNn-Ty FyYvE um] NoO^tOnS- AnD{ iT} gAiNs~ ThHiR-tEeN noot ons] DuRiNg^ a DoMiNaNcE fIgH-t, wHaT] Is/ tHe ToTaL^ FoR|cE?"

# Clean to readable text
clean = re.sub(r'[^a-zA-Z0-9\s]', ' ', txt)
print("cleaned:", clean)

# Extract numbers
nums_word = {'twenty': 20, 'twenty-five': 25, 'thirteen': 13, '13': 13, '25': 25}
for w, v in nums_word.items():
    if w.lower() in clean.lower():
        print(f"found: {w} = {v}")

# Parse: "twenty-five nootons AND it gains thirteen nootons"
a = 25
b = 13
result = a + b
print(f"first pass: {a} + {b} = {result}")
print(f"second pass: {a} + {b} = {result}")
print(f"answer: {result:.2f}")
