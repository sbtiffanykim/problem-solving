import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    # 단어마다 뒤집혀야 하고, 순서는 같아야 하므로 단어별로 구분해서 입력받기
    s = list(input().split())
    answer = ""
    for i in range(len(s)):
        # 각 단어마다 stack에 집어넣기
        stack = list(s[i])
        # 띄어쓰기 추가
        stack.append(" ")
        # stack pop해 정답에 집어넣기
        while stack:
            answer += stack.pop()
    # 가장 왼쪽 띄어쓰기는 제거
    print(answer.lstrip())
