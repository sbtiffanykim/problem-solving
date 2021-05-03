s = input()
s = list(map(int, s))
# 첫번째 숫자로 초기화
answer = s[0]

# 두번째 숫자부터 마지막 숫자까지 계산하기
for i in range(1, len(s)):
    # 현재 숫자가 0/1이거나 첫번째 숫자가 0이면 현재 숫자를 더하는 게 유리
    if s[i] == 1 or s[i] == 0 or answer == 0:
        answer += s[i]
    # 나머지 경우는 곱하는 게 더 유리
    else:
        answer *= s[i]

print(answer)