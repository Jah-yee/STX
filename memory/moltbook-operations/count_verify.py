#!/usr/bin/env python3
# The challenge text split by whitespace/punctuation
# Based on: A] LoObBsSt-Er ExErT sS^tHriRrTy FivE NoOtOnS- WiTh ClAw Um, BuT/ DuRiNg MoLtInG It LoOsEs TwElVe } NooToNs~ HoW MaNy NeW^tOnS ReMaIn?

# Words as they appear in the challenge (splitting on whitespace and punctuation)
phrase1 = "LoObBsSt-Er ExErT sS^tHriRrTy FivE NoOtOnS-"
phrase2 = "WiTh ClAw Um BuT/ DuRiNg MoLtInG It LoOsEs TwElVe NooToNs~"
phrase3 = "HoW MaNy NeW^tOnS ReMaIn?"

def count_letters(text):
    return sum(1 for c in text if c.isalpha())

words1 = phrase1.split()
words2 = phrase2.split()
words3 = phrase3.split()

print("=== Phrase 1 (start) ===")
t1 = 0
for w in words1:
    n = count_letters(w)
    print(f"  {w!r} = {n}")
    t1 += n
print(f"Phrase 1 total: {t1}")

print("\n=== Phrase 2 (loses) ===")
t2 = 0
for w in words2:
    n = count_letters(w)
    print(f"  {w!r} = {n}")
    t2 += n
print(f"Phrase 2 total: {t2}")

print("\n=== Phrase 3 (question) ===")
t3 = 0
for w in words3:
    n = count_letters(w)
    print(f"  {w!r} = {n}")
    t3 += n
print(f"Phrase 3 total: {t3}")

print(f"\nGrand total: {t1+t2+t3}")
print(f"If start = {t1} and loses TwElVe ({count_letters('TwElVe')}) = {t1 - count_letters('TwElVe')}")
print(f"If start = {t1+t2} and loses TwElVe ({count_letters('TwElVe')}) = {t1+t2 - count_letters('TwElVe')}")
