import sys
from collections import deque

n = int(input())
cards = deque([i + 1 for i in range(n)])

# 카드가 한장일때는 아래 process를 실행하지 않는다
if n == 1:
    print(1)

else:
    while True:
        cards.popleft()
        if len(cards) == 1:
            break
        cards.append(cards.popleft())
    print(cards[0])