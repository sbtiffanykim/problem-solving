# 퀵 정렬
# Pivot을 설정한 후 큰 수 와 작은 수를 교환해 리스트를 반으로 나눔
# time complexity: O(nlogn)
# 특징: 거의 다 정렬되어있는 상태의 데이터에서 첫번째 index를 pivot으로 잡으면 매우 느리게(O(n^2))으로 동작

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):

    # 원소가 1개인 경우 quick sort 종료
    if start >= end:
        return

    pivot = start
    # pivot보다 큰 값을 찾기 위한 변수
    left = start + 1
    # pivot보다 작은 값을 찾기 위한 변수
    right = end
    # 서로 위치가 역전할 때까지 반복하면서 분할 수행
    while left <= right:
        # array의 끝까지 이동하면서 pivot보다 큰 숫자 찾기
        while left <= end and array[pivot] >= array[left]:
            left += 1
        # array의 시작까지 이동하면서 pivot보다 작은 숫자 찾기
        while right > start and array[pivot] <= array[right]:
            right -= 1
        # 만약 엇갈렸다면 pivot과 가장 작은 값(right)를 swap
        if right > left:
            array[right], array[pivot] = array[pivot], array[right]
        # 아니라면 right와 left의 값 swap
        else:
            array[right], array[left] = array[left], array[right]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
