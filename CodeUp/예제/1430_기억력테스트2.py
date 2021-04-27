"""
#1430: 기억력 테스트 2
"""

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
questions = list(map(int, input().split()))

for i in questions:
    if i in nums:
        print(1, end=" ")
    else:
        print(0, end=" ")
