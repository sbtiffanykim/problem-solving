n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))

rice_cakes.sort()

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = rice_cakes[n - 1]  # 정렬 후이므로 리스트의 가장 마지막 값이 리스트의 최댓값

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in rice_cakes:
        if i > mid:
            total += i - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        # 적어도 m 이상을 얻기 위해 절단기에 설정할 수 있는 높이를 구하므로,
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

print(result)