"""
#1412: 알파벳 개수
"""

s = input()
alphabet = [0] * 26

for l in s:
    if l >= "a":
        idx = ord(l) - ord("a")
        alphabet[idx] += 1

for i in range(26):
    print(f"{chr(i+ord('a'))}:{alphabet[i]}")