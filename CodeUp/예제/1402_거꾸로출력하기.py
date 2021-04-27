"""
#1402: 거꾸로 출력하기
"""

n = int(input())
arr = list(map(int, input().split()))

arr.reverse()

print(*arr, end=" ")