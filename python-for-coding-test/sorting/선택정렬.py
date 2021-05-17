# 선택 정렬
# 매번 가장 작은 것을 선택하기
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    # 정렬되지 않은 부분에서 가장 작은 값을 찾기
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            # 가장 작은 값의 인덱스 저장
            min_index = j
    # 값 스와프
    array[min_index], array[i] = array[i], array[min_index]

print(array)
