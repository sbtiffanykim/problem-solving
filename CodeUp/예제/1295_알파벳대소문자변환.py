"""
#1295: 알파벳 대소문자 변환
"""

s = input()

for c in s:
    if c >= "a" and c <= "z":
        print(chr(ord(c) - ord("a") + ord("A")), end="")
    elif c >= "A" and c <= "Z":
        print(chr(ord(c) - ord("A") + ord("a")), end="")
    else:
        print(c, end="")
