n = int(input())
coin_types = [500, 100, 50, 10]
answer = 0

# 가지고 있는 동전의 가장 큰 단위는 항상 작은 단위의 배수
# 큰 동전부터 거슬러주면 가장 적은 개수의 동전을 사용할 수 있다
for t in coin_types:
    answer += n // coin_types
    n %= coin_types

print(answer)