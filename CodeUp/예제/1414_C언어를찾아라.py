"""
#1414: C언어를 찾아라
"""

s = input()

cnt_s = 0
for i in s:
    if i == "c" or i == "C":
        cnt_s += 1
print(cnt_s)

cnt_d = 0
for j in range(len(s) - 1):
    dl = s[j] + s[j + 1]
    if dl == "cC" or dl == "Cc" or dl == "CC" or dl == "cc":
        cnt_d += 1
print(cnt_d)
