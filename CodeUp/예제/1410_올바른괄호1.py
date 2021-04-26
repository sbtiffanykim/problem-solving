"""
#1410: 올바른 괄호 1
"""

parentheses = list(input())
open_p = 0
close_p = 0

for i in parentheses:
    if i == "(":
        open_p += 1
    else:
        close_p += 1

print(open_p, close_p)