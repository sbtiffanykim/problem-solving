# 퀵 정렬
# Pivot을 설정한 후 큰 수 와 작은 수를 교환해 리스트를 반으로 나눔
# time complexity: O(nlogn)
# 특징: 거의 다 정렬되어있는 상태의 데이터에서 첫번째 index를 pivot으로 잡으면 매우 느리게(O(n^2))으로 동작

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 파이썬 장점을 살린 퀵정렬 구현
# 단점: 피벗과 데이터를 비교하는 연산 횟수가 증가함
# 장점: 외우기 쉬움


def quick_sort(array):

    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return

    # pivot은 리스트의 가장 첫번째 원소
    pivot = array[0]
    # tail은 pivot을 제외한 리스트
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽과 오른쪽 부분을 각각 정렬하고 그 가운데에 pivot을 위치한 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


quick_sort(array)