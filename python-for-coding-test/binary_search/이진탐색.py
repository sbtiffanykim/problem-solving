# 이진탐색 구현(재귀 사용)
def binary_search(array, target, start, end):
    # 재귀 종료 조건
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 target이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 target이 큰 경우 오른쪽 확인
    else:
        binary_search(array, target, mid + 1, end)


# 원소의 개수(n)과 찾고자 하는 문자열(target) 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 결과 수행
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)