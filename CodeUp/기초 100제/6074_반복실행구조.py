"""
#6074: 문자 1개 입력받아 알파벳 출력하기
"""

c = input()
temp = ord("a")

while temp <= ord(c):
    print(chr(temp), end=" ")
    temp += 1