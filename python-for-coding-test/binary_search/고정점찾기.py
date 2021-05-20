# 이진 탐색 구현(반복)
def binary_search(nums, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾는 값이 인덱스와 같은 경우 인덱스 반환
        if nums[mid] == mid:
            return mid
        # 찾는 값이 인덱스보다 작을 경우 오른쪽 탐색
        elif nums[mid] < mid:
            start = mid + 1
        # 찾는 값이 인덱스보다 클 경우 왼쪽 탐색
        else:
            end = mid - 1
    # 고정점이 없으면 -1 반환
    return -1


n = int(input())
nums = list(map(int, input().split()))

# 이진 탐색 수행
result = binary_search(nums, 0, n - 1)
print(result)
