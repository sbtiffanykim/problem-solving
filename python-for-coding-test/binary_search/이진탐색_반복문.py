# 이진탐색 구현(반복문 사용)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 index 반환
        if array[mid] == target:
            return mid
        # 중간점의 값이 target보다 크면 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값이 target보다 작으면 오른쪽 확인
        else:
            end = mid + 1

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