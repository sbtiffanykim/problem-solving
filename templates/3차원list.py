m, n, h = map(int, input().split())

# 3차원 list로 입력받기
a = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 3차원 list 초기화
b = [[[0] * m for _ in range(n)] for _ in range(h)]
