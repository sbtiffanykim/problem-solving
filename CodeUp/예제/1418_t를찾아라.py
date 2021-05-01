"""
#1418: t를 찾아라
"""

s = input()

for i in range(len(s)):
    if s[i] == "t":
        print(i + 1, end=" ")
